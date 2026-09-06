import glob

new_toggle_sound = """    function toggleSound() {
      var snd = document.getElementById('snd');
      var btns = [document.getElementById('sound-btn'), document.getElementById('sound-btn-mobile')];
      if(!snd) return;
      if (snd.paused) {
        snd.volume = 0.5; // Smooth volume
        snd.play().then(function() {
          btns.forEach(btn => {
            if (btn) {
              btn.classList.add('playing');
              var txt = btn.querySelector('.snd-toggle-txt');
              if (txt) txt.innerText = 'SOUND ON';
            }
          });
        }).catch(function(e) { console.log(e); });
      } else {
        snd.pause();
        btns.forEach(btn => {
          if (btn) {
            btn.classList.remove('playing');
            var txt = btn.querySelector('.snd-toggle-txt');
            if (txt) txt.innerText = 'SOUND OFF';
          }
        });
      }
    }"""

def update_sound_toggle():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the function toggleSound()
        start = content.find('function toggleSound() {')
        if start != -1:
            # Find the closing brace of toggleSound
            end = content.find('    }\n', start)
            if end != -1:
                end += 6
                old_func = content[start:end]
                content = content.replace(old_func, new_toggle_sound + '\n')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated sound toggle in {filename}")

update_sound_toggle()
