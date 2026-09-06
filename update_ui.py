import re
import glob

def update_all_html():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Add mobile nav HTML
        if '<div class="mobile-nav-overlay"' not in content:
            nav_html = """
    </nav>
    <button class="mobile-menu-btn" onclick="toggleMobileMenu()">
      <div class="bar"></div><div class="bar"></div><div class="bar"></div>
    </button>
    <button class="btn-cta" data-cursor="triangle" onclick="goTo('ready')">Play Game</button>
  </header>
  
  <!-- Mobile Navigation Overlay -->
  <div class="mobile-nav-overlay" id="mobileNav">
    <div class="mobile-nav-content">
      <span class="nav-a on" onclick="goTo('hero'); toggleMobileMenu()">About the Game</span>
      <span class="nav-a" onclick="goTo('rules'); toggleMobileMenu()">Pricing</span>
      <span class="nav-a" onclick="openContactModal(); toggleMobileMenu()">Contact</span>
      <div id="sound-btn-mobile" class="snd-toggle" onclick="toggleSound()">
        <span class="snd-toggle-txt">SOUND OFF</span>
        <div class="bars">
          <div class="bar"></div><div class="bar"></div><div class="bar"></div>
        </div>
      </div>
    </div>
  </div>
"""
            # Replace the closing tag and CTA button
            # Note: the spaces/indentation might differ slightly, using a regex
            new_content = re.sub(r'</nav>\s*<button class="btn-cta"[^>]*>Play Game</button>\s*</header>', nav_html, content)
            if new_content != content:
                content = new_content
                changed = True

        # Add mobile menu JS
        if 'function toggleMobileMenu' not in content:
            js_code = """
    /* Mobile Menu Toggle */
    function toggleMobileMenu() {
      const menu = document.getElementById('mobileNav');
      const btn = document.querySelector('.mobile-menu-btn');
      if (menu) menu.classList.toggle('open');
      if (btn) btn.classList.toggle('open');
      if (typeof beep === 'function') beep(880, 0.1);
    }
"""
            if '/* ── 5. INTERACTIONS ── */' in content:
                content = content.replace('/* ── 5. INTERACTIONS ── */', '/* ── 5. INTERACTIONS ── */\n' + js_code)
                changed = True
            else:
                # Add before closing script tag
                content = content.replace('</script>\n</body>', js_code + '\n</script>\n</body>')
                changed = True

        # Add CSS for mobile menu
        if '.mobile-menu-btn' not in content:
            css_code = """
    /* Mobile Nav */
    .mobile-menu-btn { display: none; background: none; border: none; flex-direction: column; gap: 5px; cursor: pointer; z-index: 2000; position: relative; margin-right: 12px; }
    .mobile-menu-btn .bar { width: 24px; height: 2px; background: #fff; transition: all 0.3s; box-shadow: 0 0 8px rgba(255,255,255,0.4); }
    .mobile-menu-btn.open .bar:nth-child(1) { transform: translateY(7px) rotate(45deg); background: var(--pink); box-shadow: 0 0 8px var(--pink); }
    .mobile-menu-btn.open .bar:nth-child(2) { opacity: 0; }
    .mobile-menu-btn.open .bar:nth-child(3) { transform: translateY(-7px) rotate(-45deg); background: var(--pink); box-shadow: 0 0 8px var(--pink); }
    
    .mobile-nav-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0,0,0,0.95); backdrop-filter: blur(20px); z-index: 1500; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
    .mobile-nav-overlay.open { opacity: 1; pointer-events: auto; }
    .mobile-nav-content { display: flex; flex-direction: column; align-items: center; gap: 32px; transform: translateY(20px); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
    .mobile-nav-overlay.open .mobile-nav-content { transform: translateY(0); }
    .mobile-nav-content .nav-a { font-size: 24px; }
    .mobile-nav-content .snd-toggle { transform: scale(1.5); margin-left: 0; }
"""
            if '/* Main */' in content:
                content = content.replace('/* Main */', css_code + '\n    /* Main */')
                changed = True
            else:
                # find closing style
                content = content.replace('</style>', css_code + '\n</style>')
                changed = True

        # Update media query for header elements
        if 'display:flex' not in content.split('@media(max-width:820px)')[1] if '@media(max-width:820px)' in content else False:
            content = content.replace('.nav{display:none}', '.nav{display:none}\n      .mobile-menu-btn { display: flex; }\n      .btn-cta { padding: 6px 16px; font-size: 10px; }\n      #hdr { padding: 0 20px; }')
            changed = True
            
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")

update_all_html()
