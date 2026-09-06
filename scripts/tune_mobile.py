import re

files = ['automystica.html', 'hackthehardware.html', 'triguna.html', 'visionexpo.html']

redundant_media = """    @media(max-width:820px){
      .nav{display:none}
      .t-xtasy{font-size:clamp(52px,18vw,200px)}
      .t-40{font-size:clamp(28px,10vw,120px)}
      .wg{grid-template-columns:1fr;gap:28px}
      .glove{max-height:38vh}
      .rules-grid{grid-template-columns:repeat(2,1fr);min-height:auto}
      .rc{border-bottom:1px solid rgba(255,255,255,.1)}
      .ready-row{flex-direction:column;gap:16px}
      .rr-re,.rr-dy-t{font-size:64px!important}
      .rr-dy{align-items:center;text-align:center}
      .rr-dy-extras{position:static;margin-top:16px;align-items:center}
      .collage{height:420px}
      .rules-hdr{justify-content:flex-start}
      .rh-p,.rh-w{text-align:left}
    }"""

new_header_mobile = """    /* Mobile Menu & Touch Tuning */
    .hdr-right { display: flex; align-items: center; gap: 16px; }
    .mobile-menu-btn { display: none; background: transparent; border: none; cursor: pointer; flex-direction: column; gap: 4px; z-index: 1001; padding: 8px; min-width: 44px; min-height: 44px; justify-content: center; align-items: center; }
    .mobile-menu-btn .bar { width: 24px; height: 2px; background: #fff; transition: 0.3s; display: block; }
    .mobile-menu-btn.active .bar:nth-child(1), .mobile-menu-btn.open .bar:nth-child(1) { transform: translateY(6px) rotate(45deg); }
    .mobile-menu-btn.active .bar:nth-child(2), .mobile-menu-btn.open .bar:nth-child(2) { opacity: 0; }
    .mobile-menu-btn.active .bar:nth-child(3), .mobile-menu-btn.open .bar:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }
    
    .mobile-nav-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.95); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); z-index: 999; display: flex; flex-direction: column; justify-content: center; align-items: center; opacity: 0; pointer-events: none; transition: opacity 0.4s var(--ease); }
    .mobile-nav-overlay.active, .mobile-nav-overlay.open { opacity: 1; pointer-events: auto; }
    .mobile-nav-content { display: flex; flex-direction: column; align-items: center; gap: 28px; transform: translateY(20px); transition: transform 0.4s var(--ease); width: 100%; max-width: 320px; padding: 20px; }
    .mobile-nav-overlay.active .mobile-nav-content, .mobile-nav-overlay.open .mobile-nav-content { transform: translateY(0); }
    .mobile-nav-content .nav-a { font-size: 20px; font-weight: 700; letter-spacing: 0.08em; }

    /* Touch Devices */
    @media (hover: none) or (pointer: coarse) {
      .cdot, .cring { display: none !important; }
      body { cursor: auto !important; }
      a, button, [onclick] { cursor: pointer !important; }
    }

    @media (max-width: 820px) {
      .nav { display: none !important; }
      #hdr .btn-cta, .hdr-right .btn-cta { display: none !important; }
      #hdr .snd-toggle, .hdr-right .snd-toggle { display: none !important; }
      .mobile-menu-btn { display: flex; }
      #hdr { height: 62px; padding: 0 16px; }

      .dept-watermark { display: none !important; }
    }"""

old_mobile_menu_css_regex = r'/\* Mobile Menu Styles \*/[\s\S]*?@media \(max-width: 820px\) \{[\s\S]*?\}'

enhanced_900 = """      @media(max-width: 900px) {
        .event-detail-sec { padding-top: 80px; padding-bottom: 50px; }
        .ed-wrap { flex-direction: column; text-align: center; gap: 28px; padding: 16px; }
        .ed-right { align-items: center; width: 100%; }
        .ed-image-wrap { max-width: 280px; width: 100%; aspect-ratio: 1/1; }
        .ed-title { font-size: clamp(32px, 8vw, 52px); }
        .ed-tagline { font-size: 15px; margin-bottom: 20px; }
        .ed-desc { font-size: 14.5px; margin-bottom: 24px; }
        .ed-challenge-box { text-align: left; padding: 16px; margin-top: 16px; }
        .ed-specs { justify-content: center; gap: 16px; margin-bottom: 28px; }
        .ed-spec { flex: 1; max-width: 140px; padding: 10px 16px; text-align: center; }
        .ed-spec .val { font-size: 16px; }
        .ed-cta { width: 100%; max-width: 320px; padding: 15px 24px; font-size: 16px; border-radius: 8px; margin-bottom: 18px; }
        #xtasy-toolbar { top: 75px; left: 50%; transform: translateX(-50%) translateY(-15px); width: calc(100% - 32px); max-width: 320px; }
        #xtasy-toolbar.active { transform: translateX(-50%) translateY(0); }
        .event-extended-sec { padding: 50px 16px; }
        .ext-wrap { gap: 32px; }
        .ext-block h3 { font-size: 20px; margin-bottom: 14px; }
        .ext-block p { font-size: 14.5px; line-height: 1.6; margin-bottom: 14px; }
        .ext-block li { padding: 14px 16px; font-size: 13.5px; line-height: 1.5; }
      }"""

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Remove redundant media query
    c = c.replace(redundant_media, '')

    # 2. Replace old mobile menu styles with new_header_mobile
    c = re.sub(old_mobile_menu_css_regex, new_header_mobile, c)

    # 3. Add All Events CTA in mobileNav if not present
    if "All Events" not in c.split('id="mobileNav"')[1].split('</div>\n  </div>')[0]:
        c = c.replace(
            '<span class="nav-a" onclick="openContactModal(); toggleMobileMenu()">Contact</span>',
            '<span class="nav-a" onclick="openContactModal(); toggleMobileMenu()">Contact</span>\n      <button class="btn-cta" style="padding:12px 36px;font-size:14px;box-shadow:0 0 25px rgba(255,0,127,.8);margin:6px 0;" onclick="window.location.href=\'events.html\'; toggleMobileMenu()">All Events</button>'
        )

    # 4. Enhance @media(max-width: 900px)
    # Remove existing scattered rules for max-width: 900px
    c = re.sub(r'@media\s*\(max-width:\s*900px\)\s*\{[^\}]+\}\s*', '', c)
    # Insert enhanced_900 right after .ed-wrap rule
    target_ed_wrap = '.ed-wrap { width: 100%; max-width: 1200px; margin: 0 auto; display: flex; gap: 60px; padding: 20px; align-items: center; opacity: 0; animation: pageFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards; }'
    if target_ed_wrap in c:
        c = c.replace(target_ed_wrap, target_ed_wrap + '\n' + enhanced_900)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Successfully tuned mobile responsiveness for: {fpath}')
