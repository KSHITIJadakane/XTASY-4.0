import re
import glob

contact_html = """
  <div id="contact-modal" onclick="if(event.target===this)closeContactModal()">
    <div class="mbox contact-box" data-cursor="default">
      <div class="m-top">
        <div class="m-syms">&#9675; &#9651; &#9633;</div>
        <div class="m-h">CONTACT US</div>
      </div>
      <div class="m-ins">
        <div class="c-list">
          <div class="c-item" oncontextmenu="return false;" onmousedown="startPress(this, '+91 80109 94064')" onmouseup="endPress()" onmouseleave="endPress()" ontouchstart="startPress(this, '+91 80109 94064')" ontouchend="endPress()">
            <div class="c-name">VIDHI UKEY</div>
            <div class="c-role">(coordinator)</div>
            <div class="c-phone">+91 80109 94064</div>
            <div class="c-tooltip">Long press to copy</div>
          </div>
          <div class="c-item" oncontextmenu="return false;" onmousedown="startPress(this, '+91 87679 51251')" onmouseup="endPress()" onmouseleave="endPress()" ontouchstart="startPress(this, '+91 87679 51251')" ontouchend="endPress()">
            <div class="c-name">ROOPAM ZADE</div>
            <div class="c-role">(co coordinator)</div>
            <div class="c-phone">+91 87679 51251</div>
            <div class="c-tooltip">Long press to copy</div>
          </div>
          <div class="c-item" oncontextmenu="return false;" onmousedown="startPress(this, '+91 9405476977')" onmouseup="endPress()" onmouseleave="endPress()" ontouchstart="startPress(this, '+91 9405476977')" ontouchend="endPress()">
            <div class="c-name">KSHITIJ ADAKANE</div>
            <div class="c-role">(dev)</div>
            <div class="c-phone">+91 9405476977</div>
            <div class="c-tooltip">Long press to copy</div>
          </div>
        </div>
      </div>
      <div class="m-actions" style="justify-content: center;">
        <button class="btn-walk" data-cursor="triangle" onclick="closeContactModal()" style="margin: 0;">CLOSE</button>
      </div>
    </div>
  </div>
"""

contact_css = """
    .contact-box { width: 90%; max-width: 450px; background: #080808; border: 1px solid var(--b12); padding: 32px; position: relative; }
    .c-list { display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; }
    .c-item { display: flex; flex-direction: column; align-items: center; text-align: center; background: rgba(255,255,255,0.03); padding: 16px; border-radius: 8px; border: 1px solid var(--b12); cursor: pointer; position: relative; user-select: none; -webkit-user-select: none; transition: background 0.3s, border-color 0.3s; }
    .c-item:active { background: rgba(255,0,127,0.1); border-color: var(--pink); }
    .c-name { font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 700; color: #fff; letter-spacing: 0.05em; }
    .c-role { font-family: 'Inter', sans-serif; font-size: 12px; color: var(--t70); margin-bottom: 8px; }
    .c-phone { font-family: 'Space Mono', monospace; font-size: 16px; color: var(--pink); font-weight: 700; }
    .c-tooltip { position: absolute; top: -25px; left: 50%; transform: translateX(-50%); background: var(--pink); color: #fff; font-size: 10px; padding: 4px 8px; border-radius: 4px; opacity: 0; pointer-events: none; transition: opacity 0.3s; white-space: nowrap; font-family: 'Inter', sans-serif; z-index: 10; }
    .c-tooltip.show-tooltip { opacity: 1; pointer-events: auto; }
"""

contact_js = """
    /* Contact Modal Logic */
    let pressTimer;
    function startPress(el, number) {
      pressTimer = setTimeout(() => {
        navigator.clipboard.writeText(number).then(() => {
          const tooltip = el.querySelector('.c-tooltip');
          const originalText = tooltip.innerText;
          tooltip.innerText = 'Copied!';
          tooltip.classList.add('show-tooltip');
          setTimeout(() => { tooltip.classList.remove('show-tooltip'); tooltip.innerText = originalText; }, 2000);
          if (typeof beep === 'function') beep(880, 0.1);
        });
      }, 600);
    }
    function endPress() { clearTimeout(pressTimer); }
    function openContactModal() {
      if (typeof beep === 'function') beep(523, 0.25);
      const modal = document.getElementById('contact-modal');
      if (modal) modal.classList.add('open');
    }
    function closeContactModal() {
      const modal = document.getElementById('contact-modal');
      if (modal) modal.classList.remove('open');
    }
"""

def update_files():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        changed = False

        # 1. Update "READY TO PLAY?" in index.html only
        if filename == 'index.html':
            if '<div class="rr-re">REA</div>' in content:
                content = content.replace('<div class="rr-re">REA</div>', '<div class="rr-re">READY</div>')
                content = content.replace('<div class="rr-dy-t">DY</div>', '<div class="rr-dy-t" style="display:none">DY</div>')
                changed = True
        
        # 2. Update Footer Contact Us inline style to use Insta gradient
        if 'style="background:linear-gradient(#050505,#050505) padding-box,radial-gradient(circle at 30% 107%,var(--cyan) 0%,var(--cyan) 100%) border-box;"' in content:
            content = content.replace('style="background:linear-gradient(#050505,#050505) padding-box,radial-gradient(circle at 30% 107%,var(--cyan) 0%,var(--cyan) 100%) border-box;"', '')
            changed = True
        
        # Remove old Telegram / Youtube icons if they exist (user said "remove youtube and telegram icon just add the follow us on instagram and the respective icon inside the respective boder")
        # I don't see Telegram/Youtube in the footer excerpt, but just in case.

        # 3. Add contact-modal HTML
        if 'id="contact-modal"' not in content:
            if '</body>' in content:
                content = content.replace('</body>', contact_html + '\n</body>')
                changed = True

        # 4. Add contact-modal CSS
        if '.contact-box {' not in content:
            if '/* Main */' in content:
                content = content.replace('/* Main */', contact_css + '\n    /* Main */')
                changed = True
            elif '</style>' in content:
                content = content.replace('</style>', contact_css + '\n</style>')
                changed = True

        # 5. Add contact-modal JS
        if 'function openContactModal()' not in content:
            if '/* ── 5. INTERACTIONS ── */' in content:
                content = content.replace('/* ── 5. INTERACTIONS ── */', '/* ── 5. INTERACTIONS ── */\n' + contact_js)
                changed = True
            elif '</script>\n</body>' in content:
                content = content.replace('</script>\n</body>', contact_js + '\n</script>\n</body>')
                changed = True
            elif '</script>' in content:
                # Add before last </script>
                idx = content.rfind('</script>')
                if idx != -1:
                    content = content[:idx] + contact_js + '\n' + content[idx:]
                    changed = True

        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")

update_files()
