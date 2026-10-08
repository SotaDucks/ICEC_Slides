# Scroll Dive · ICEC 2026 WIP slides

直接用 Chrome 或 Edge 打开本目录的 index.html。这是合并后的正式演示入口，无需启动服务器。

## 播放顺序

1. Cover（Pen 第 1 页）
2. SFV Use and the Exit Problem（Pen 第 2 页）
3. Design for Disengagement（Pen 第 3 页）
4. Research Question（Pen 第 4 页）
5. Prototype 动态说明：Pre-dive → Diving & viewing → Approaching maximum time cues → Ascent & Return to the surface
6. Preliminary User Study（Pen 第 5 页）
7. Study Conditions（Pen 第 6 页）
8. Study Results（Pen 第 7 页）
9. Preliminary Insights（Pen 第 8 页）

总计 9 个网页页面；prototype 页面内部包含 4 个可单独播放的阶段。Pen 页面中原有的编号和排版保留，网页底部显示合并后的页码。

旧动态网页从 “An endless feed needs a designed ending” 起的所有后续页面已从正式网页及构建输入中移除。

## 操作

- 空格 / 右方向键 / Continue：普通页面翻页；prototype 页面推进演示阶段，最后进入 Preliminary User Study。
- 左方向键：普通页面返回上一页；prototype 页面先返回上一阶段，在第一阶段返回 Research Question。
- R：重播当前 prototype 阶段。也可以点 01–04 阶段按钮。
- Esc：打开或关闭页面索引。
- F：全屏；B：切换动态 / 静态背景。
- Home / End：跳转至第一页 / 最后一页。

进入 prototype 页面时开始播放，分别在 5.5 秒、20.4 秒、31.0 秒停留，最后一段播放至视频结束。若浏览器阻止播放，点击视频或 Continue 即可。

## 文件与构建

请一起保留 index.html、ScrollDiveVideoDemo.mp4、assets、images 和 design 文件夹。

- design/pen-slides.html：通过 Pen MCP 导出的 8 页原始 HTML，包含画布上的全部页面。
- design/images：Pen 导出所引用的图片，包括已保存到本地的背景照片。
- assets/immersive-demo.html：仅包含 prototype 演示页面。
- assets/deck-shell.html：演示样式、翻页与视频阶段控制。
- merge_deck.py：读取 Pen 导出，将 prototype 插在第 4、5 页之间并生成正式网页。
- build_deck.py：构建入口，运行 python build_deck.py 即可重新生成 index.html。

若以后从 Pen 重新导出，请使用同一组 8 个顶层 frame，输出到 design/pen-slides.html，并将图片放在 design/images。网页由原生 HTML/CSS/JavaScript 组成，构建脚本只使用 Python 标准库。

按项目约定，本次没有运行测试，播放效果由用户确认。
