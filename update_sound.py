import glob
import re

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
        
        # Safely replace toggleSound using balanced brace regex
        pattern = r'[ \t]*function toggleSound\(\)\s*\{[\s\S]*?\n[ \t]*\}'
        if re.search(pattern, content):
            content = re.sub(pattern, new_toggle_sound, content)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated sound toggle in {filename}")

if __name__ == '__main__':
    update_sound_toggle()
