import os, sys, subprocess, time
from PIL import Image

test_html_content = open('index.html', 'r', encoding='utf-8').read()

# Replace the transitions in CSS with the tuned decoupled bezier curves:
# transform: 2.35s cubic-bezier(0.16, 1, 0.3, 1)
# opacity: 2.25s cubic-bezier(0.35, 0, 0.25, 1)
old_css_glide = """.glide-left{opacity:0;transform:translate3d(-96px,0,0);transition:opacity 2.35s cubic-bezier(.16,1,.3,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}
    .glide-right{opacity:0;transform:translate3d(96px,0,0);transition:opacity 2.35s cubic-bezier(.16,1,.3,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}
    .glide-center{opacity:0;transform:scale(.9) translate3d(0,-18px,0);transform-origin:809px 340px;transition:opacity 2.35s cubic-bezier(.16,1,.3,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}"""

new_css_glide = """.glide-left{opacity:0;transform:translate3d(-88px,0,0);transition:opacity 2.25s cubic-bezier(.35,0,.25,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}
    .glide-right{opacity:0;transform:translate3d(88px,0,0);transition:opacity 2.25s cubic-bezier(.35,0,.25,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}
    .glide-center{opacity:0;transform:scale(.92) translate3d(0,-20px,0);transform-origin:809px 340px;transition:opacity 2.25s cubic-bezier(.35,0,.25,1),transform 2.35s cubic-bezier(.16,1,.3,1);will-change:opacity,transform}"""

test_html_content = test_html_content.replace(old_css_glide, new_css_glide)

# Also update crowd and ambient-bloom
old_crowd = "transition:opacity 2.35s cubic-bezier(.16,1,.3,1),transform 2.35s cubic-bezier(.16,1,.3,1);"
new_crowd = "transition:opacity 2.25s cubic-bezier(.35,0,.25,1),transform 2.35s cubic-bezier(.16,1,.3,1);"
test_html_content = test_html_content.replace(old_crowd, new_crowd)

old_bloom = "transition:opacity 2.35s cubic-bezier(.16,1,.3,1),transform 2.35s cubic-bezier(.16,1,.3,1);"
new_bloom = "transition:opacity 2.35s cubic-bezier(.35,0,.25,1),transform 2.35s cubic-bezier(.16,1,.3,1);"
test_html_content = test_html_content.replace(old_bloom, new_bloom)

# Update the JS trigger so it doesn't wait for window.load
old_js = """    window.addEventListener('DOMContentLoaded',function(){
      var sp=new URLSearchParams(location.search);
      if(sp.get('s')==='end'||location.hash==='#end')document.body.classList.add('intro-active','lit','settled');
      else if(sp.get('s')==='start'||location.hash==='#start')document.body.classList.remove('intro-active','lit','settled');
      else {
        if(document.readyState==='complete')playIntro();
        else window.addEventListener('load',function(){playIntro()});
      }
      var h=document.getElementById('hero');
      if(h)h.addEventListener('click',function(e){if(!e.target.closest('button,a'))replayIntro()});
    });"""

new_js = """    function initIntro(){
      var sp=new URLSearchParams(location.search);
      if(sp.get('s')==='end'||location.hash==='#end')document.body.classList.add('intro-active','lit','settled');
      else if(sp.get('s')==='start'||location.hash==='#start')document.body.classList.remove('intro-active','lit','settled');
      else playIntro();
      var h=document.getElementById('hero');
      if(h)h.addEventListener('click',function(e){if(!e.target.closest('button,a'))replayIntro()});
    }
    if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',initIntro);
    }else{
      initIntro();
    }"""

test_html_content = test_html_content.replace(old_js, new_js)

with open('scratch_frames/test_smooth_transition.html', 'w', encoding='utf-8') as f:
    f.write(test_html_content)

print('Wrote scratch_frames/test_smooth_transition.html')
