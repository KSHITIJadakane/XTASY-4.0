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
      
      <div class="scroll-indicator" onclick="window.scrollTo({{top: window.innerHeight, behavior: 'smooth'}})" data-cursor="pointer">
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
    </style>
  </main>'''

    content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


ext_auto = """
<div class="ext-block">
  <h3>WHAT IS AUTOMYSTICA?</h3>
  <p>Imagine that you are an automation engineer. You are given a situation such as: A greenhouse is experiencing excessive temperature while soil moisture is simultaneously decreasing. An automated system is required to monitor the environment and control the necessary equipment.</p>
  <p>You build it. You program it. You test it. You connect it to a dashboard. You think you're done.</p>
  <p>Then comes <strong>the twist</strong>. The coordinators introduce a new limitation: "The system can no longer operate both actuators simultaneously." Now your original solution may no longer be sufficient. You have to rethink your automation logic, modify your code and make it work.</p>
</div>
<div class="ext-block">
  <h3>THE STAGES</h3>
  <ul>
    <li><strong>STAGE 1 (UNDERSTAND)</strong> Teams receive their assigned scenario and must understand the problem and required outputs.</li>
    <li><strong>STAGE 2 (BUILD)</strong> Teams create their solution using Wokwi. Connect sensors, ESP32, and actuators.</li>
    <li><strong>STAGE 3 (DASHBOARD)</strong> Integrate the system with a web dashboard representing actual simulated data.</li>
    <li><strong>STAGE 4 (ADAPTATION)</strong> The TWIST is revealed. Teams get a limited time to respond, modify their logic, and survive.</li>
  </ul>
</div>
"""

update_page(
    'automystica.html', 
    'IMG_9183.png', 
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
  <h3>CONQUER THE ARENA</h3>
  <p>Hack the Hardware is a hands-on robotics and hardware challenge where participants put their engineering skills to the test. After learning the fundamentals of building and controlling a Bluetooth-controlled bot through a preparatory workshop, teams must assemble and program their bot during the competition and then take it into a physical maze arena.</p>
  <p>With time, control and wall collisions influencing their performance, teams must navigate the arena with precision and efficiency. The team that demonstrates the strongest overall performance takes the win.</p>
</div>
<div class="ext-block">
  <h3>THE STAGES</h3>
  <ul>
    <li><strong>GREEN LIGHT - BUILD</strong> Assemble and program your bot using provided components.</li>
    <li><strong>RED LIGHT - TEST</strong> Test your bot and ensure that it responds correctly.</li>
    <li><strong>GREEN LIGHT - ARENA</strong> Enter the maze. Navigate the treacherous paths with your Bluetooth controller.</li>
    <li><strong>RED LIGHT - COLLISION</strong> Every mistake matters. Wall collisions and time dictate your final score.</li>
  </ul>
</div>
"""

update_page(
    'hackthehardware.html', 
    'IMG_9207.jpg', 
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
  <h3>EXPECTATIONS</h3>
  <ul>
    <li><strong>VISUALIZE</strong> Present a clear, visually striking poster communicating an industrial or technical concept.</li>
    <li><strong>INNOVATE</strong> Showcase novel ideas in lean manufacturing, IoT, or industrial automation.</li>
    <li><strong>EXCEL</strong> Defend your ideas and answer technical queries from industry experts and judges.</li>
  </ul>
</div>
"""

update_page(
    'visionexpo.html', 
    'IMG_9219.png', 
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
  <h3>THE CORE PHILOSOPHY</h3>
  <ul>
    <li><strong>IDENTIFY</strong> Find a real problem and understand its root cause in the agricultural sector.</li>
    <li><strong>DEVELOP</strong> Build an innovative, frugal, and affordable solution.</li>
    <li><strong>DEMONSTRATE</strong> Prove its technical feasibility and suitability for real-world agricultural conditions.</li>
    <li><strong>PITCH</strong> Present the economic value and impact to the jury.</li>
  </ul>
</div>
"""

update_page(
    'triguna.html', 
    'logo_automystica.jpg', 
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

