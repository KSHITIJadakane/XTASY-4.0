import re

files = ['automystica.html', 'hackthehardware.html', 'triguna.html', 'visionexpo.html']

clean_event_style = """    <style>
      /* Page Load Animations */
      @keyframes pageFadeIn { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes bgFadeIn { from { opacity: 0; transform: scale(1.15); filter: blur(50px) brightness(0.1); } to { opacity: 1; transform: scale(1.1); filter: blur(40px) brightness(0.2) saturate(0.5); } }

      .event-hero-bg { position: fixed; inset: 0; z-index: 1; pointer-events: none; }
      .event-hero-bg img { width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.2) saturate(0.5); transform: scale(1.1); animation: bgFadeIn 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
      .event-hero-bg .overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.95)); }
      
      .event-detail-sec { z-index: 10; position: relative; padding-top: 100px; padding-bottom: 120px; align-items: flex-start; min-height: 100vh; }
      .ed-wrap { width: 100%; max-width: 1200px; margin: 0 auto; display: flex; gap: 60px; padding: 20px; align-items: center; opacity: 0; animation: pageFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards; }
      
      .ed-left { flex: 1; display: flex; justify-content: center; }
      .ed-image-wrap { width: 100%; max-width: 500px; aspect-ratio: 1/1; border: 1px solid rgba(255,0,127,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 0 50px rgba(0,0,0,0.9), 0 0 30px rgba(255,0,127,0.15); }
      .ed-image-wrap img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }
      .ed-image-wrap:hover img { transform: scale(1.05); }
      
      .ed-right { flex: 1.2; display: flex; flex-direction: column; align-items: flex-start; }
      .ed-title { font-family: 'Space Grotesk', sans-serif; font-size: clamp(42px, 5vw, 72px); font-weight: 800; color: var(--pink); line-height: 1; letter-spacing: 0.02em; text-shadow: 0 0 30px rgba(255,0,127,0.6); margin-bottom: 10px; text-transform: uppercase; }
      .ed-tagline { font-family: 'Space Grotesk', sans-serif; font-size: clamp(16px, 2vw, 22px); font-weight: 600; color: var(--cyan); letter-spacing: 0.15em; margin-bottom: 30px; text-transform: uppercase; text-shadow: 0 0 10px rgba(0,240,255,0.4); }
      
      .ed-desc { font-family: 'Inter', sans-serif; font-size: 16px; color: #ccc; line-height: 1.6; margin-bottom: 40px; }
      .ed-challenge-box { margin-top: 25px; padding: 20px; background: rgba(255,0,127,0.05); border-left: 3px solid var(--pink); border-radius: 0 8px 8px 0; }
      .ed-challenge-box h3 { font-family: 'Space Grotesk', sans-serif; color: #fff; font-size: 14px; letter-spacing: 0.1em; margin-bottom: 8px; }
      
      .ed-specs { display: flex; gap: 30px; margin-bottom: 40px; width: 100%; }
      .ed-spec { display: flex; flex-direction: column; background: rgba(255,255,255,0.03); padding: 15px 25px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08); }
      .ed-spec .lbl { font-family: 'Space Grotesk', sans-serif; font-size: 11px; color: var(--t70); letter-spacing: 0.2em; margin-bottom: 4px; }
      .ed-spec .val { font-family: 'Space Mono', monospace; font-size: 18px; color: #fff; font-weight: 700; }
      
      .ed-cta { background: var(--pink); border: none; color: #fff; font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 700; padding: 16px 40px; border-radius: 4px; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 0 25px rgba(255,0,127,0.4); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 25px; }
      .ed-cta:hover { background: #ff1a8c; transform: translateY(-3px); box-shadow: 0 0 45px rgba(255,0,127,0.7); }
      
      .ed-back { color: var(--t70); font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-decoration: none; transition: color 0.3s; }
      .ed-back:hover { color: #fff; }

      /* Scroll Indicator */
      .scroll-indicator { position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; gap: 8px; cursor: pointer; opacity: 0.6; transition: opacity 0.3s; z-index: 20; }
      .scroll-indicator:hover { opacity: 1; }
      .scroll-indicator span { font-family: 'Space Grotesk', sans-serif; color: #fff; font-size: 10px; letter-spacing: 0.3em; }
      .scroll-indicator .arrow { color: var(--pink); font-size: 18px; animation: bounce 2s infinite; }
      @keyframes bounce { 0%, 20%, 50%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-10px); } 60% { transform: translateY(-5px); } }

      /* Quick Access Toolbar */
      #xtasy-toolbar { position: fixed; top: 80px; left: 40px; background: rgba(10, 10, 10, 0.7); backdrop-filter: blur(25px); border: 1px solid rgba(255, 0, 127, 0.3); border-radius: 12px; padding: 10px; display: flex; flex-direction: column; gap: 5px; min-width: 220px; opacity: 0; pointer-events: none; transform: translateY(-15px); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 9999; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.9), 0 0 25px rgba(255, 0, 127, 0.2); }
      #xtasy-toolbar.active { opacity: 1; pointer-events: auto; transform: translateY(0); }
      .xt-item { display: flex; align-items: center; gap: 15px; padding: 14px 18px; border-radius: 8px; color: #ddd; font-family: 'Space Grotesk', sans-serif; font-size: 15px; font-weight: 600; letter-spacing: 0.05em; cursor: pointer; transition: background 0.2s, color 0.2s; }
      .xt-item:hover { background: rgba(255, 0, 127, 0.15); color: var(--pink); }
      .xt-icon { font-size: 20px; color: var(--cyan); }

      /* Extended Details Section */
      .event-extended-sec { position: relative; z-index: 10; background: #050505; padding: 100px 20px; border-top: 1px solid rgba(255,0,127,0.15); box-shadow: 0 -20px 50px rgba(0,0,0,0.8); }
      .ext-wrap { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 50px; opacity: 0; animation: pageFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards; }
      .ext-block h3 { font-family: 'Space Grotesk', sans-serif; color: var(--cyan); font-size: 28px; letter-spacing: 0.05em; margin-bottom: 20px; text-transform: uppercase; }
      .ext-block p { font-family: 'Inter', sans-serif; color: #aaa; font-size: 17px; line-height: 1.8; margin-bottom: 20px; }
      .ext-block ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 15px; }
      .ext-block li { font-family: 'Inter', sans-serif; color: #aaa; font-size: 16px; line-height: 1.6; background: rgba(255,255,255,0.02); padding: 20px 25px; border-left: 3px solid var(--pink); border-radius: 0 8px 8px 0; transition: background 0.3s; }
      .ext-block li:hover { background: rgba(255,255,255,0.05); }
      .ext-block li strong { color: #fff; font-family: 'Space Grotesk', sans-serif; letter-spacing: 0.05em; display: block; margin-bottom: 5px; color: var(--pink); }

      /* Mobile Overrides (max-width: 900px) */
      @media (max-width: 900px) {
        .event-detail-sec { padding-top: 80px; padding-bottom: 110px; }
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
        .ed-back { display: inline-block; padding: 8px 16px; margin-bottom: 8px; }
        .scroll-indicator { bottom: 20px; }
        .scroll-indicator span { font-size: 9px; letter-spacing: 0.25em; }
        .scroll-indicator .arrow { font-size: 16px; }
        #xtasy-toolbar { top: 75px; left: 50%; transform: translateX(-50%) translateY(-15px); width: calc(100% - 32px); max-width: 320px; }
        #xtasy-toolbar.active { transform: translateX(-50%) translateY(0); }
        .event-extended-sec { padding: 50px 16px; }
        .ext-wrap { gap: 32px; }
        .ext-block h3 { font-size: 20px; margin-bottom: 14px; }
        .ext-block p { font-size: 14.5px; line-height: 1.6; margin-bottom: 14px; }
        .ext-block li { padding: 14px 16px; font-size: 13.5px; line-height: 1.5; }
      }
    </style>"""

for fn in files:
    content = open(fn, 'r', encoding='utf-8').read()
    
    # 1. Fix Block 1: remove extraneous rules and extra brace after @media (max-width: 820px)
    old_b1_pattern = r'(\.dept-watermark\s*\{\s*display:\s*none\s*!important;\s*\}\s*\})\s*\.btn-cta\s*\{\s*display:\s*none;\s*\}\s*\.snd-toggle\s*\{\s*display:\s*none;\s*\}\s*\.mobile-menu-btn\s*\{\s*display:\s*flex;\s*\}\s*\}\s*</style>'
    match = re.search(old_b1_pattern, content)
    if match:
        content = re.sub(old_b1_pattern, r'\1\n  </style>', content)
        print(f"Fixed Block 1 in {fn}")
    else:
        print(f"Block 1 pattern not matched in {fn}")
        
    # 2. Fix Block 2: replace entire second <style> block
    # Second style block is right after </script> around line 567
    old_b2_pattern = r'<style>\s*/\* Page Load Animations \*/.*?</style>'
    match2 = re.search(old_b2_pattern, content, re.DOTALL)
    if match2:
        content = re.sub(old_b2_pattern, clean_event_style.strip(), content, count=1, flags=re.DOTALL)
        print(f"Fixed Block 2 in {fn}")
    else:
        print(f"Block 2 pattern not matched in {fn}")
        
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished fixing event detail files.")
