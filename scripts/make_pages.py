import os
import re

def update_page(filename, bg_image, title, tagline, description, challenge, team_size, fee, cta_text, extended_html, form_url):
    filepath = os.path.join(r"c:\Users\rajur\OneDrive\Desktop\xtasy", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_main = f'''<main>
    <div class="event-hero-bg">
      <img src="assets/{bg_image}" alt="Background" />
      <div class="overlay"></div>
    </div>
    <section class="sec event-detail-sec">
      <div class="ed-wrap">
        
        <div class="ed-left">
          <div class="ed-image-wrap">
             <img src="assets/{bg_image}" alt="{title}" />
          </div>
        </div>

        <div class="ed-right">
          <h1 class="ed-title">{title}</h1>
          <h2 class="ed-tagline">{tagline}</h2>
          
          <div class="ed-desc">
            <p>{description}</p>
            <div class="ed-challenge-box">
              <h3>THE CHALLENGE</h3>
              <p>{challenge}</p>
            </div>
          </div>

          <div class="ed-specs">
            <div class="ed-spec">
              <span class="lbl">TEAM</span>
              <span class="val">{team_size}</span>
            </div>
            <div class="ed-spec">
              <span class="lbl">FEE</span>
              <span class="val">{fee}</span>
            </div>
          </div>

          <button class="ed-cta" data-cursor="triangle" onclick="window.open('{form_url}', '_blank')">{cta_text}</button>
          
          <a href="events.html" class="ed-back" data-cursor="circle">← BACK TO EVENTS</a>
        </div>

      </div>
      
      <div class="scroll-indicator" onclick="document.querySelector('.event-extended-sec')?.scrollIntoView({{behavior: 'smooth'}})" data-cursor="pointer">
        <span>SCROLL FOR DETAILS</span>
        <div class="arrow">↓</div>
      </div>
    </section>
    
    <section class="sec event-extended-sec">
      <div class="ext-wrap">
        {extended_html}
      </div>
    </section>

    <script>
      (function() {{
        // Quick Access Toolbar Setup
        const toolbar = document.createElement('div');
        toolbar.id = 'xtasy-toolbar';
        toolbar.innerHTML = `
          <div class="xt-item" onclick="window.history.back()">
            <span class="xt-icon">←</span> Back
          </div>
          <div class="xt-item" onclick="window.location.href='index.html'">
            <span class="xt-icon">⌂</span> Home
          </div>
          <div class="xt-item" style="opacity: 0.5; cursor: not-allowed;">
            <span class="xt-icon">⊞</span> Dashboard (Soon)
          </div>
        `;
        document.body.appendChild(toolbar);

        const logo = document.querySelector('.logo');
        if (logo) {{
          logo.style.cursor = 'pointer';
          logo.setAttribute('onclick', 'toggleToolbar(event)');
        }}

        // Close toolbar when clicking outside
        document.addEventListener('click', (e) => {{
          if (toolbar && !toolbar.contains(e.target) && (!logo || !logo.contains(e.target))) {{
            toolbar.classList.remove('active');
          }}
        }});
      }})();

      function toggleToolbar(e) {{
        if(e) e.stopPropagation();
        const toolbar = document.getElementById('xtasy-toolbar');
        if(toolbar) toolbar.classList.toggle('active');
      }}
    </script>

    <style>
      /* Page Load Animations */
      @keyframes pageFadeIn {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
      @keyframes bgFadeIn {{ from {{ opacity: 0; transform: scale(1.15); filter: blur(50px) brightness(0.1); }} to {{ opacity: 1; transform: scale(1.1); filter: blur(40px) brightness(0.2) saturate(0.5); }} }}

      .event-hero-bg {{ position: fixed; inset: 0; z-index: 1; pointer-events: none; }}
      .event-hero-bg img {{ width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.2) saturate(0.5); transform: scale(1.1); animation: bgFadeIn 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
      .event-hero-bg .overlay {{ position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.95)); }}
      
      .event-detail-sec {{ z-index: 10; position: relative; padding-top: 100px; padding-bottom: 120px; align-items: flex-start; min-height: 100vh; }}
      .ed-wrap {{ width: 100%; max-width: 1200px; margin: 0 auto; display: flex; gap: 60px; padding: 20px; align-items: center; opacity: 0; animation: pageFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards; }}
      
      @media(max-width: 900px) {{ .ed-wrap {{ flex-direction: column; text-align: center; }} }}
      
      .ed-left {{ flex: 1; display: flex; justify-content: center; }}
      .ed-image-wrap {{ width: 100%; max-width: 500px; aspect-ratio: 1/1; border: 1px solid rgba(255,0,127,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 0 50px rgba(0,0,0,0.9), 0 0 30px rgba(255,0,127,0.15); }}
      .ed-image-wrap img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }}
      .ed-image-wrap:hover img {{ transform: scale(1.05); }}
      
      .ed-right {{ flex: 1.2; display: flex; flex-direction: column; align-items: flex-start; }}
      @media(max-width: 900px) {{ .ed-right {{ align-items: center; }} }}
      
      .ed-title {{ font-family: 'Space Grotesk', sans-serif; font-size: clamp(42px, 5vw, 72px); font-weight: 800; color: var(--pink); line-height: 1; letter-spacing: 0.02em; text-shadow: 0 0 30px rgba(255,0,127,0.6); margin-bottom: 10px; text-transform: uppercase; }}
      .ed-tagline {{ font-family: 'Space Grotesk', sans-serif; font-size: clamp(16px, 2vw, 22px); font-weight: 600; color: var(--cyan); letter-spacing: 0.15em; margin-bottom: 30px; text-transform: uppercase; text-shadow: 0 0 10px rgba(0,240,255,0.4); }}
      
      .ed-desc {{ font-family: 'Inter', sans-serif; font-size: 16px; color: #ccc; line-height: 1.6; margin-bottom: 40px; }}
      .ed-challenge-box {{ margin-top: 25px; padding: 20px; background: rgba(255,0,127,0.05); border-left: 3px solid var(--pink); border-radius: 0 8px 8px 0; }}
      .ed-challenge-box h3 {{ font-family: 'Space Grotesk', sans-serif; color: #fff; font-size: 14px; letter-spacing: 0.1em; margin-bottom: 8px; }}
      
      .ed-specs {{ display: flex; gap: 30px; margin-bottom: 40px; width: 100%; }}
      @media(max-width: 900px) {{ .ed-specs {{ justify-content: center; }} }}
      .ed-spec {{ display: flex; flex-direction: column; background: rgba(255,255,255,0.03); padding: 15px 25px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08); }}
      .ed-spec .lbl {{ font-family: 'Space Grotesk', sans-serif; font-size: 11px; color: var(--t70); letter-spacing: 0.2em; margin-bottom: 4px; }}
      .ed-spec .val {{ font-family: 'Space Mono', monospace; font-size: 18px; color: #fff; font-weight: 700; }}
      
      .ed-cta {{ background: var(--pink); border: none; color: #fff; font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 700; padding: 16px 40px; border-radius: 4px; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 0 25px rgba(255,0,127,0.4); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 25px; }}
      .ed-cta:hover {{ background: #ff1a8c; transform: translateY(-3px); box-shadow: 0 0 45px rgba(255,0,127,0.7); }}
      
      .ed-back {{ color: var(--t70); font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-decoration: none; transition: color 0.3s; }}
      .ed-back:hover {{ color: #fff; }}

      /* Scroll Indicator */
      .scroll-indicator {{ position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; gap: 8px; cursor: pointer; opacity: 0.6; transition: opacity 0.3s; z-index: 20; }}
      .scroll-indicator:hover {{ opacity: 1; }}
      .scroll-indicator span {{ font-family: 'Space Grotesk', sans-serif; color: #fff; font-size: 10px; letter-spacing: 0.3em; }}
      .scroll-indicator .arrow {{ color: var(--pink); font-size: 18px; animation: bounce 2s infinite; }}
      @keyframes bounce {{ 0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }} 40% {{ transform: translateY(-10px); }} 60% {{ transform: translateY(-5px); }} }}

      /* Quick Access Toolbar */
      #xtasy-toolbar {{ position: fixed; top: 80px; left: 40px; background: rgba(10, 10, 10, 0.7); backdrop-filter: blur(25px); border: 1px solid rgba(255, 0, 127, 0.3); border-radius: 12px; padding: 10px; display: flex; flex-direction: column; gap: 5px; min-width: 220px; opacity: 0; pointer-events: none; transform: translateY(-15px); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 9999; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.9), 0 0 25px rgba(255, 0, 127, 0.2); }}
      #xtasy-toolbar.active {{ opacity: 1; pointer-events: auto; transform: translateY(0); }}
      .xt-item {{ display: flex; align-items: center; gap: 15px; padding: 14px 18px; border-radius: 8px; color: #ddd; font-family: 'Space Grotesk', sans-serif; font-size: 15px; font-weight: 600; letter-spacing: 0.05em; cursor: pointer; transition: background 0.2s, color 0.2s; }}
      .xt-item:hover {{ background: rgba(255, 0, 127, 0.15); color: var(--pink); }}
      .xt-icon {{ font-size: 20px; color: var(--cyan); }}

      /* Extended Details Section */
      .event-extended-sec {{ position: relative; z-index: 10; background: #050505; padding: 100px 20px; border-top: 1px solid rgba(255,0,127,0.15); box-shadow: 0 -20px 50px rgba(0,0,0,0.8); }}
      .ext-wrap {{ max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 50px; opacity: 0; animation: pageFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards; }}
      .ext-block h3 {{ font-family: 'Space Grotesk', sans-serif; color: var(--cyan); font-size: 28px; letter-spacing: 0.05em; margin-bottom: 20px; text-transform: uppercase; }}
      .ext-block p {{ font-family: 'Inter', sans-serif; color: #aaa; font-size: 17px; line-height: 1.8; margin-bottom: 20px; }}
      .ext-block ul {{ list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 15px; }}
      .ext-block li {{ font-family: 'Inter', sans-serif; color: #aaa; font-size: 16px; line-height: 1.6; background: rgba(255,255,255,0.02); padding: 20px 25px; border-left: 3px solid var(--pink); border-radius: 0 8px 8px 0; transition: background 0.3s; }}
      .ext-block li:hover {{ background: rgba(255,255,255,0.05); }}
      .ext-block li strong {{ color: #fff; font-family: 'Space Grotesk', sans-serif; letter-spacing: 0.05em; display: block; margin-bottom: 5px; color: var(--pink); }}
      
      /* Mobile Overrides (max-width: 900px) */
      @media (max-width: 900px) {{
        .event-detail-sec {{ padding-top: 80px; padding-bottom: 110px; }}
        .ed-wrap {{ flex-direction: column; text-align: center; gap: 28px; padding: 16px; }}
        .ed-right {{ align-items: center; width: 100%; }}
        .ed-image-wrap {{ max-width: 280px; width: 100%; aspect-ratio: 1/1; }}
        .ed-title {{ font-size: clamp(32px, 8vw, 52px); }}
        .ed-tagline {{ font-size: 15px; margin-bottom: 20px; }}
        .ed-desc {{ font-size: 14.5px; margin-bottom: 24px; }}
        .ed-challenge-box {{ text-align: left; padding: 16px; margin-top: 16px; }}
        .ed-specs {{ justify-content: center; gap: 16px; margin-bottom: 28px; }}
        .ed-spec {{ flex: 1; max-width: 140px; padding: 10px 16px; text-align: center; }}
        .ed-spec .val {{ font-size: 16px; }}
        .ed-cta {{ width: 100%; max-width: 320px; padding: 15px 24px; font-size: 16px; border-radius: 8px; margin-bottom: 18px; }}
        .ed-back {{ display: inline-block; padding: 8px 16px; margin-bottom: 8px; }}
        .scroll-indicator {{ bottom: 20px; }}
        .scroll-indicator span {{ font-size: 9px; letter-spacing: 0.25em; }}
        .scroll-indicator .arrow {{ font-size: 16px; }}
        #xtasy-toolbar {{ top: 75px; left: 50%; transform: translateX(-50%) translateY(-15px); width: calc(100% - 32px); max-width: 320px; }}
        #xtasy-toolbar.active {{ transform: translateX(-50%) translateY(0); }}
        .event-extended-sec {{ padding: 50px 16px; }}
        .ext-wrap {{ gap: 32px; }}
        .ext-block h3 {{ font-size: 20px; margin-bottom: 14px; }}
        .ext-block p {{ font-size: 14.5px; line-height: 1.6; margin-bottom: 14px; }}
        .ext-block li {{ padding: 14px 16px; font-size: 13.5px; line-height: 1.5; }}
      }}
    </style>
    <footer class="footer" style="position:relative; z-index:20; background:#050505;">
      <div class="logo" onclick="window.location.href='index.html'">
        <svg viewBox="0 0 100 100" fill="none" stroke="currentColor" style="width:22px;height:22px;color:var(--pink);filter:drop-shadow(0 0 8px rgba(255,0,127,.9))"><circle cx="50" cy="45" r="32" stroke-width="12"/><path d="M68 62 L88 88" stroke-width="14" stroke-linecap="round"/></svg>
        <div class="logo-lbl"><span class="logo-name" style="font-size:14px">XTASY</span><span class="logo-ver" style="font-size:7.5px">4.0</span></div>
      </div>
      <div style="display:flex; gap:16px; align-items:center; flex-wrap:wrap; justify-content:center;">
        <a onclick="openContactModal()" class="soc" title="Contact Us" style="background:linear-gradient(#050505,#050505) padding-box,radial-gradient(circle at 30% 107%,var(--cyan) 0%,var(--cyan) 100%) border-box;">
          <span class="follow-text">Contact Us</span>
          <div class="soc-a" style="background:var(--cyan);box-shadow:0 0 10px rgba(0,240,255,.45);color:#000;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg></div>
        </a>
        <a href="https://www.instagram.com/xtasy_svpcet?utm_source=ig_web_button_share_sheet&stkn=ZDNlZDc0MzIxNw==" target="_blank" rel="noreferrer" class="soc" title="Follow us on Instagram">
          <span class="follow-text">Follow us on Instagram</span>
          <div class="soc-a s-ig"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></div>
        </a>
      </div>
      <div class="copy">© 2026 XTASY 4.0 Quest Room — All Rights Reserved</div>
    </footer>
    
    <div id="contact-modal" onclick="if(event.target===this)closeContactModal()">
      <div class="mbox" data-cursor="default">
        <div class="m-top">
          <div class="m-syms">&#9675; &#9651; &#9633;</div>
          <div class="m-h">CONTACT COMMAND</div>
        </div>
        <p class="m-p">For inquiries, contact the Front Man's operators. Long press or click a number to copy.</p>
        
        <div class="c-list">
          <div class="c-item" onclick="copyNum('8010994064', this)">
            <div class="c-role">COORDINATOR</div>
            <div class="c-name">VIDHI UKEY</div>
            <div class="c-num">+91 80109 94064</div>
          </div>
          <div class="c-item" onclick="copyNum('8767951251', this)">
            <div class="c-role">CO-COORDINATOR</div>
            <div class="c-name">ROOPAM ZADE</div>
            <div class="c-num">+91 87679 51251</div>
          </div>
          <div class="c-item" onclick="copyNum('9405476977', this)">
            <div class="c-role">DEV</div>
            <div class="c-name">KSHITIJ ADAKANE</div>
            <div class="c-num">+91 94054 76977</div>
          </div>
        </div>
        
        <div class="m-actions">
          <button class="btn-walk" data-cursor="triangle" onclick="closeContactModal()">DISMISS</button>
        </div>
      </div>
    </div>
    
    <script>
      function openContactModal() {{
        document.getElementById('contact-modal').classList.add('open');
      }}
      function closeContactModal() {{
        document.getElementById('contact-modal').classList.remove('open');
      }}
      function copyNum(num, el) {{
        if(navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(num).then(function() {{
            el.classList.add('copied');
            setTimeout(function(){{ el.classList.remove('copied'); }}, 1500);
          }});
        }} else {{
          var tempInput = document.createElement('input');
          tempInput.value = num;
          document.body.appendChild(tempInput);
          tempInput.select();
          document.execCommand('copy');
          document.body.removeChild(tempInput);
          el.classList.add('copied');
          setTimeout(function(){{ el.classList.remove('copied'); }}, 1500);
        }}
      }}
    </script>
  </main>'''

    content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


ext_auto = """
<div class="ext-block">
  <h3>PROBLEM STATEMENT</h3>
  <p>A greenhouse is experiencing excessive temperature while soil moisture is simultaneously decreasing. An automated system is required to monitor the environment and control the necessary equipment.</p>
  <p>You build it. You program it. You test it. You connect it to a dashboard. You think you're done. Then comes <strong>the twist</strong>. The coordinators introduce a new limitation: "The system can no longer operate both actuators simultaneously." Now your original solution may no longer be sufficient. You have to rethink your automation logic, modify your code and make it work.</p>
</div>
<div class="ext-block">
  <h3>EXPECTED SOLUTION & THE STAGES</h3>
  <ul>
    <li><strong>EXPECTED SOLUTION:</strong> An automated IoT solution built using Wokwi (sensors, ESP32, actuators) connected to a web dashboard. The solution must successfully adapt to "The Twist" mid-competition.</li>
    <li><strong>STAGE 1 (UNDERSTAND)</strong> Teams receive their assigned scenario and must understand the problem and required outputs.</li>
    <li><strong>STAGE 2 (BUILD)</strong> Teams create their solution using Wokwi. Connect sensors, ESP32, and actuators.</li>
    <li><strong>STAGE 3 (DASHBOARD)</strong> Integrate the system with a web dashboard representing actual simulated data.</li>
    <li><strong>STAGE 4 (ADAPTATION)</strong> The TWIST is revealed. Teams get a limited time to respond, modify their logic, and survive.</li>
  </ul>
</div>
"""

update_page(
    'automystica.html', 
    'IMG_9207.jpg', 
    'AUTOMYSTICA', 
    'Build. Adapt. Survive.', 
    'Master the elements of IoT, optimize your nodes, and build a system that outlasts the rest. The frontline of the Industrial IoT revolution starts here.',
    'Design an automated solution using Wokwi. Then, survive "The Twist"-an unexpected limitation thrown at you mid-competition. Adapt or perish.',
    'DUO', 
    '₹190', 
    'ENTER AUTOMYSTICA',
    ext_auto,
    'https://forms.gle/Hm2fGyhegrfCjUqJ9'
)


ext_hack = """
<div class="ext-block">
  <h3>PROBLEM STATEMENT</h3>
  <p>Participants must assemble and program a Bluetooth-controlled bot during the competition and navigate it through a physical maze arena.</p>
  <p>With time, control and wall collisions influencing their performance, teams must navigate the arena with precision and efficiency. The team that demonstrates the strongest overall performance takes the win.</p>
</div>
<div class="ext-block">
  <h3>EXPECTED SOLUTION & THE STAGES</h3>
  <ul>
    <li><strong>EXPECTED SOLUTION:</strong> A robust, assembled and programmed hardware bot that accurately responds to Bluetooth controls and successfully navigates the maze with minimal wall collisions in the fastest time.</li>
    <li><strong>GREEN LIGHT - BUILD</strong> Assemble and program your bot using provided components.</li>
    <li><strong>RED LIGHT - TEST</strong> Test your bot and ensure that it responds correctly.</li>
    <li><strong>GREEN LIGHT - ARENA</strong> Enter the maze. Navigate the treacherous paths with your Bluetooth controller.</li>
    <li><strong>RED LIGHT - COLLISION</strong> Every mistake matters. Wall collisions and time dictate your final score.</li>
  </ul>
</div>
"""

update_page(
    'hackthehardware.html', 
    'IMG_9183.png', 
    'HACK THE HARDWARE', 
    'Build It. Control It. Conquer the Arena.', 
    'Assemble your bot, refine your circuits, and navigate the treacherous paths. Only the most robust hardware and the sharpest controllers will survive the gauntlet.',
    'You are given hardware components. Assemble, program, and race against time and collisions in a physical maze. Every mistake matters.',
    'SOLO / DUO', 
    '₹70 / ₹100', 
    'ENTER THE ARENA',
    ext_hack,
    'https://forms.gle/87zmURhA2zu9cxM56'
)


ext_vision = """
<div class="ext-block">
  <h3>THE BLUEPRINT</h3>
  <p>The event focuses on presenting technical concepts in a visually appealing and informative manner. Participants will create a poster (digital or physical) and explain their ideas to the judges.</p>
  <p>The goal is to evaluate their understanding of the topic, creativity in presentation, and communication skills. It's not just about what you know, but how effectively you can communicate it to the world.</p>
</div>
<div class="ext-block">
  <h3>OFFICIAL THEMES (CHOOSE ONE)</h3>
  <ul>
    <li><strong>1. 5S</strong> Workplace organization and efficiency (Sort, Set in Order, Shine, Standardize, Sustain).</li>
    <li><strong>2. POKA-YOKE</strong> Mistake-proofing in industrial processes.</li>
    <li><strong>3. 7 WASTES</strong> Identifying and eliminating major forms of waste in manufacturing.</li>
    <li><strong>4. TPM (Total Productive Maintenance)</strong> Proactive and preventive maintenance practices.</li>
    <li><strong>5. 7 QC TOOLS</strong> Fundamental quality-control tools for problem-solving.</li>
    <li><strong>6. VISUAL MANAGEMENT</strong> Communicating info clearly through visual systems.</li>
    <li><strong>7. OHNO CIRCLE</strong> Observing an actual workplace directly to identify problems.</li>
    <li><strong>8. CLIRT</strong> Practical application of CLIRT in industrial operations.</li>
    <li><strong>9. ECRS</strong> Process improvement (Eliminate, Combine, Rearrange, Simplify).</li>
    <li><strong>10. 7 ABNORMALITIES</strong> Recognizing abnormalities before they lead to problems.</li>
    <li><strong>11. MOTION ECONOMY</strong> Reducing unnecessary human movement in operations.</li>
    <li><strong>12. RFT (Right First Time)</strong> Producing correct output at the first attempt.</li>
    <li><strong>13. BASIC SAFETY</strong> Fundamental workplace safety practices and hazard prevention.</li>
    <li><strong>14. KAIZEN</strong> Continuous improvement through small, incremental changes.</li>
  </ul>
</div>
<div class="ext-block">
  <h3>EXPECTED SOLUTION & EXPECTATIONS</h3>
  <ul>
    <li><strong>VISUALIZE</strong> Present a clear, visually striking poster (A3/Chart paper) communicating your industrial concept. AI generated content is discouraged.</li>
    <li><strong>EXPLAIN</strong> Be prepared to answer questions: What is the concept? Why is it important? How is it applied? Can you provide a real-world example?</li>
  </ul>
</div>
"""

update_page(
    'visionexpo.html', 
    'logo_visionexpo.png', 
    'VISION EXPO', 
    'Visualize. Innovate. Excel.', 
    'The blueprint is just the beginning. Present your master plan for lean manufacturing and industrial excellence. In this arena, your ideas are your weapons.',
    'Convert technical concepts into creative, informative posters. Pitch your vision to industry experts and prove your dominance.',
    'INDIVIDUAL', 
    '₹30', 
    'SUBMIT YOUR VISION',
    ext_vision,
    'https://forms.gle/9ZyMedYs6afaeYCPA'
)


ext_triguna = """
<div class="ext-block">
  <h3>AGRICULTURE INNOVATION CHALLENGE</h3>
  <p>TRIGUNA is designed to encourage students to identify genuine problems faced by farmers and develop practical, technically feasible and economically viable solutions.</p>
  <p>The event focuses on the intersection of agriculture, technology, sustainability, frugal engineering, and innovation. Participants are expected to move beyond theoretical ideas and develop solutions that can realistically address problems encountered in agricultural and rural environments.</p>
</div>
<div class="ext-block">
  <h3>PROBLEM TRACKS (CHOOSE ONE)</h3>
  <ul>
    <li><strong>PS-1: THE ₹3,000 SMART FIELD (Precision Irrigation & Pest Alert)</strong> Affordable agricultural automation. <em>Expected Tech: IoT nodes, active/passive mechanisms under ₹3,000.</em></li>
    <li><strong>PS-2: THE 6-HOUR SHIELD (Allied Dairy & Fisheries)</strong> Off-grid technological solutions. <em>Expected Tech: Solar/Peltier cooling, automated aeration, DO/pH monitoring.</em></li>
    <li><strong>PS-3: SHREE ANNA: GRAIN TO GAIN (Traditional Millets)</strong> Improving processing & handling. <em>Expected Tech: Motorized/manual dehulling, low-breakage mechanisms, better packaging.</em></li>
    <li><strong>PS-4: ZERO-CHEMICAL, ZERO-LOSS (Natural & Regenerative Farming)</strong> Supporting natural practices. <em>Expected Tech: Low-cost soil/spectral monitoring, organic pest control systems.</em></li>
    <li><strong>PS-5: MANDI BYPASS: FAIR BID (Digital Marketplaces)</strong> Improving market transparency. <em>Expected Tech: Web/mobile apps, IoT moisture meters, digital auction platforms.</em></li>
    <li><strong>PS-6: OPEN INNOVATION IN AGRICULTURE (Grassroots)</strong> Any other genuine, meaningful agricultural problem. <em>Expected Solution: A working mechanism, prototype, or app (pure abstract ideas not allowed).</em></li>
  </ul>
</div>
<div class="ext-block">
  <h3>EXPECTED DELIVERABLES & EVALUATION</h3>
  <ul>
    <li><strong>WORKING DEMONSTRATION</strong> Physical prototype, hardware circuit, mechanical mechanism, verified simulation, or functional app.</li>
    <li><strong>FARMER ECONOMICS</strong> You must calculate exact Bill of Materials (BOM), expected savings, and payback period.</li>
    <li><strong>PITCH</strong> A 6-minute pitch (6-8 slides) defending the technical feasibility, cost, and practical implementation to the jury.</li>
  </ul>
</div>
"""

update_page(
    'triguna.html', 
    'logo_triguna.png', 
    'TRIGUNA', 
    'Find the Problem. Build the Idea. Pitch the Impact.', 
    'Tackle real-world agricultural problems with practical, technically feasible, and economically viable solutions.',
    'Identify an agricultural challenge. Develop a frugal, sustainable prototype or simulation. Pitch your economic value and feasibility to the jury.',
    'SOLO / TEAM (3)', 
    '₹70 / ₹100', 
    'PITCH YOUR IMPACT',
    ext_triguna,
    'https://forms.gle/iWmCTv5cBrDh4aNT8'
)

