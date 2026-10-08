/* Atmosphere is drawn from the main video: one decoder, no second video stream. */
(() => {
 const video=document.getElementById('prototype-video');
 const canvas=document.getElementById('immersive-ambient');
 const context=canvas.getContext('2d',{alpha:false});
 const demo=document.getElementById('demo');
 let animation=0,lastPaint=0,idle=0;
 canvas.width=320;canvas.height=180;
 function draw(source){
  if(!context)return;
  const w=source.videoWidth||source.naturalWidth,h=source.videoHeight||source.naturalHeight;
  if(!w||!h)return;
  const ratio=canvas.width/canvas.height;
  const cropHeight=Math.min(h,w/ratio),cropWidth=Math.min(w,h*ratio);
  try{context.drawImage(source,(w-cropWidth)/2,(h-cropHeight)/2,cropWidth,cropHeight,0,0,canvas.width,canvas.height);}catch(e){}
 }
 const poster=new Image();poster.onload=()=>{if(video.readyState<2)draw(poster);};poster.src='images/01-before-dive.jpg';
 function stopAtmosphere(){if(animation)cancelAnimationFrame(animation);animation=0;}
 function tick(now){
  animation=0;
  if(video.paused||document.hidden||window.__lowPowerMode)return;
  if(now-lastPaint>110){draw(video);lastPaint=now;}
  animation=requestAnimationFrame(tick);
 }
 function startAtmosphere(){if(!animation&&!window.__lowPowerMode&&!video.paused)animation=requestAnimationFrame(tick);}
 function isDemo(){return window.__currentSlideIndex===0&&!overviewOn;}
 window.__paintImmersion=()=>{
  const active=isDemo();
  const running=active&&!video.paused&&!video.ended;
  document.body.classList.toggle('demo-active',active);
  document.body.classList.toggle('video-running',running);
  const copy=demo.querySelector('.demo-copy');
  copy.inert=false;copy.removeAttribute('aria-hidden');
  if(!running){stopAtmosphere();if(video.readyState>=2)draw(video);}else startAtmosphere();
 };
 function hideControls(){
  idle=0;
  if(overviewOn||document.querySelector('button:focus-visible,a:focus-visible'))return;
  document.body.classList.remove('controls-visible');
  if(matchMedia('(pointer:fine)').matches)document.body.classList.add('cursor-rest');
 }
 function revealControls(event){
  if(event&&event.type==='pointermove'&&Math.abs(event.movementX||0)+Math.abs(event.movementY||0)<2)return;
  document.body.classList.add('controls-visible');document.body.classList.remove('cursor-rest');
  clearTimeout(idle);idle=setTimeout(hideControls,2200);
 }
 // Clicking the empty atmosphere has the same behavior as clicking the video.
 demo.addEventListener('click',e=>{if(e.target.closest('button,a,video,.demo-copy'))return;document.getElementById('continue-video').click();});
 ['play','pause','ended','loadeddata','seeked','error'].forEach(name=>video.addEventListener(name,window.__paintImmersion));
 addEventListener('scroll-dive-page-change',()=>{window.__paintImmersion();revealControls();});
 addEventListener('scroll-dive-overview-change',()=>{window.__paintImmersion();revealControls();});
 addEventListener('swiss-low-power-change',()=>{stopAtmosphere();window.__paintImmersion();});
 addEventListener('pointermove',revealControls,{passive:true});
 addEventListener('pointerdown',revealControls,{passive:true});
 addEventListener('focusin',revealControls);
 document.addEventListener('visibilitychange',()=>{if(document.hidden)stopAtmosphere();else window.__paintImmersion();});
 addEventListener('keydown',e=>{
  if(e.ctrlKey||e.metaKey||e.altKey||e.target.closest('input,textarea,select'))return;
  if(e.key==='Tab'||e.key==='Escape')revealControls();
 });
 window.__paintImmersion();
 idle=setTimeout(hideControls,1800);
})();
