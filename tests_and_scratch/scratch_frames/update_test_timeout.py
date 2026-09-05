import os

content = open('scratch_frames/test_smooth_transition.html', 'r', encoding='utf-8').read()

old_play = """    function playIntro(){
      timers.forEach(function(t){clearTimeout(t)});timers=[];
      document.body.classList.remove('intro-active','lit','settled');
      // Double requestAnimationFrame guarantees hardware V-Sync synchronization & zero dropped start frames
      requestAnimationFrame(function(){
        requestAnimationFrame(function(){
          document.body.classList.add('intro-active','lit');
          synthIntro();
          timers.push(setTimeout(function(){
            document.body.classList.add('settled');
          }, 2450));
        });
      });
    }"""

new_play = """    function playIntro(){
      timers.forEach(function(t){clearTimeout(t)});timers=[];
      document.body.classList.remove('intro-active','lit','settled');
      timers.push(setTimeout(function(){
        document.body.classList.add('intro-active','lit');
        synthIntro();
        timers.push(setTimeout(function(){
          document.body.classList.add('settled');
        }, 2450));
      }, 30));
    }"""

content = content.replace(old_play, new_play)
with open('scratch_frames/test_smooth_transition.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated test_smooth_transition.html with setTimeout')
