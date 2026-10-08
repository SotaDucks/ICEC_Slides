"""Build the combined web deck using Python's standard library."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
FRAME_IDS = ('IzKGm', 'bi8Au', 'w3Tm0', 'JVxBa', 'yLIxL', 'VuYuT', 'FoE8f', 'u15rcN')


class PenFrames(HTMLParser):
    """Extract frame markup without changing the exported text or inline styles."""

    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.offsets = [0]
        for line in source.splitlines(keepends=True):
            self.offsets.append(self.offsets[-1] + len(line))
        self.frames = {}
        self.depth = 0
        self.current = None
        self.feed(source)

    def source_offset(self):
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def handle_starttag(self, tag, attrs):
        if tag != 'div':
            return
        self.depth += 1
        attrs = dict(attrs)
        node_id = attrs.get('data-pencil-id')
        if node_id in FRAME_IDS:
            self.current = (node_id, attrs.get('data-pencil-name', node_id), self.source_offset(), self.depth)

    def handle_endtag(self, tag):
        if tag != 'div':
            return
        if self.current and self.depth == self.current[3]:
            node_id, name, start, _ = self.current
            end = self.source.index('>', self.source_offset()) + 1
            self.frames[node_id] = (name, self.source[start:end])
            self.current = None
        self.depth -= 1


PEN_CSS = r'''
/* Fit the original 1920 × 1080 Pen canvas inside the viewport. */
body.canvas-mode .slide.pen-slide{display:block;background:#02070b;padding:0}
.pen-stage{left:50%!important;top:50%!important;position:absolute!important;
 width:1920px!important;height:1080px!important;transform-origin:center center;
 transform:translate(-50%,-50%) scale(var(--pen-scale,1));font-feature-settings:normal}
body.pen-page #immersive-atmosphere,body.pen-page #bg-grid{visibility:hidden}
body.pen-page #page-buttons,body.pen-page #nav,body.pen-page #hint{opacity:1;pointer-events:auto}
/* Hide footer copy and buttons while retaining keyboard controls and page dots. */
#page-buttons,#hint{display:none!important}
#nav{left:50%;right:auto;transform:translateX(-50%)}
body.pen-page.cursor-rest{cursor:auto}
#overview .pen-stage{opacity:1!important}
#overview .slide{background:#02070b!important}
#overview [data-pencil-id]{visibility:visible}
/* A quiet moving image on the cover, toned like the photograph on page two. */
.cover-prototype{position:absolute;left:1280px;top:40px;width:600px;height:1000px;
 overflow:hidden;pointer-events:none;z-index:0;background:#02070b}
.cover-prototype video{display:block;width:100%;height:100%;object-fit:contain;
 filter:brightness(.58) saturate(.65);opacity:.9}
.cover-prototype::after{content:"";position:absolute;inset:0;
 background:linear-gradient(90deg,#02070b 0%,#02070b80 12%,#02070b00 32%,#02070b00 82%,#02070b 100%),
 linear-gradient(180deg,#02070b 0%,#02070b00 12%,#02070b00 84%,#02070b 100%),#02070b45}
#overview .slide .cover-prototype video{display:block}
#overview .cover-prototype{background:#02070b url('images/01-before-dive.jpg') center/contain no-repeat}
'''
PEN_RESIZE = r'''
(() => {
 function fitPenSlides(){
  document.documentElement.style.setProperty('--pen-scale',Math.min(innerWidth/1920,innerHeight/1080));
 }
 fitPenSlides();
 addEventListener('resize',fitPenSlides,{passive:true});
})();
/* The cover loop is separate from the presenter-controlled demonstration. */
(() => {
 const video=document.getElementById('cover-video');
 if(!video)return;
 let pending=false;
 const visible=()=>window.__currentSlideIndex===0&&!overviewOn&&!document.hidden&&!window.__lowPowerMode;
 async function updateCover(){
  if(!visible()){video.pause();return;}
  if(pending||!video.paused)return;
  pending=true;
  try{await video.play();if(!visible())video.pause();}catch(_){}
  finally{pending=false;}
 }
 ['scroll-dive-page-change','scroll-dive-overview-change','swiss-low-power-change',
  'pointerdown','keydown'].forEach(event=>addEventListener(event,updateCover));
 document.addEventListener('visibilitychange',updateCover);
 updateCover();
})();
'''

COVER_VIDEO = '''
<div class="cover-prototype" aria-hidden="true">
 <video id="cover-video" src="Beforedive&amp;diving.mp4" poster="images/01-before-dive.jpg"
  muted loop playsinline preload="metadata" tabindex="-1"></video>
</div>
'''


def build():
    exported = (ROOT / 'design' / 'pen-slides.html').read_text(encoding='utf-8')
    parsed = PenFrames(exported)
    sections = []
    for node_id in FRAME_IDS:
        name, markup = parsed.frames[node_id]
        markup = markup.replace('<div', '<div class="pen-stage"', 1)
        markup = re.sub(r"url\('images/", "url('design/images/", markup)
        if node_id == FRAME_IDS[0]:
            markup = re.sub(r'(<div\b[^>]*>)', lambda match: match[0] + COVER_VIDEO, markup, count=1)
        sections.append(f'<section class="slide dark pen-slide" aria-label="{escape(name, quote=True)}">\n{markup}\n</section>')
    prototype = (ROOT / 'assets' / 'immersive-demo.html').read_text(encoding='utf-8')
    sections.insert(4, prototype)
    shell = (ROOT / 'assets' / 'deck-shell.html').read_text(encoding='utf-8')
    shell = shell.replace('{{SLIDES}}', '\n'.join(sections))
    shell = shell.replace('{{PEN_CSS}}', PEN_CSS).replace('{{PEN_RESIZE}}', PEN_RESIZE)
    (ROOT / 'index.html').write_text(shell, encoding='utf-8')
    print('Built index.html: Pen pages 1–4 → four-phase prototype → Pen pages 5–8 (9 pages).')


if __name__ == '__main__':
    build()
