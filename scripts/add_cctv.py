import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML Replacement
old_mask = '<div class="rr-mask"><img src="assets/frontman_mask_hd.jpg" alt="Frontman Mask"/></div>'
new_mask = '''<div class="rr-mask">
  <div class="cctv-glitch-container">
    <img src="assets/frontman_mask_hd.jpg" alt="Frontman Mask" class="frontman-feed"/>
    <div class="cctv-scanlines"></div>
    <div class="cctv-ui">
      <div class="cctv-rec"><span class="rec-dot"></span> REC</div>
      <div class="cctv-time">CAM 04 - 1999/10/29 23:45:00</div>
    </div>
  </div>
</div>'''

if old_mask in content:
    content = content.replace(old_mask, new_mask)
else:
    print("Warning: Could not find exactly `.rr-mask` HTML to replace. Falling back to regex.")
    content = re.sub(
        r'<div class="rr-mask">\s*<img src="assets/frontman_mask_hd\.jpg" alt="Frontman Mask"/>\s*</div>',
        new_mask,
        content,
        flags=re.IGNORECASE
    )


# 2. CSS Injection
cctv_css = '''
    /* ── FRONTMAN CCTV GLITCH ── */
    .cctv-glitch-container {
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
      border-radius: inherit;
    }
    .frontman-feed {
      width: 100%;
      height: 100%;
      object-fit: cover;
      animation: feed-glitch 5s infinite;
      filter: contrast(1.1) brightness(0.9) grayscale(0.2);
    }
    .cctv-scanlines {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(
        to bottom,
        rgba(255,255,255,0),
        rgba(255,255,255,0) 50%,
        rgba(0,0,0,0.1) 50%,
        rgba(0,0,0,0.1)
      );
      background-size: 100% 4px;
      pointer-events: none;
      z-index: 5;
    }
    .cctv-scanlines::after {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 15vh;
      background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.05), transparent);
      animation: tracking-line 4s linear infinite;
    }
    @keyframes tracking-line {
      0% { transform: translateY(-15vh); }
      100% { transform: translateY(115vh); }
    }
    .cctv-ui {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      pointer-events: none;
      z-index: 10;
      font-family: "Courier New", Courier, monospace;
      color: rgba(255,255,255,0.85);
      text-shadow: 1px 1px 2px black;
      font-weight: bold;
    }
    .cctv-rec {
      position: absolute;
      top: 15px;
      left: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 1.1rem;
    }
    .rec-dot {
      width: 12px;
      height: 12px;
      background-color: #ff0000;
      border-radius: 50%;
      box-shadow: 0 0 8px red;
      animation: rec-blink 1s steps(2, start) infinite;
    }
    @keyframes rec-blink {
      to { visibility: hidden; }
    }
    .cctv-time {
      position: absolute;
      bottom: 15px;
      right: 20px;
      font-size: 0.95rem;
      letter-spacing: 1px;
    }
    
    @keyframes feed-glitch {
      0%, 90% { transform: translate(0,0) scale(1); filter: contrast(1.1) brightness(0.9) grayscale(0.2); }
      91% { transform: translate(-2px, 2px) scale(1.02); filter: contrast(1.4) brightness(1.2) hue-rotate(-20deg) grayscale(0.2); }
      93% { transform: translate(3px, -1px) scale(1.01); filter: contrast(1.1) brightness(0.7) hue-rotate(20deg) grayscale(0.2); }
      95% { transform: translate(-1px, 3px) scale(1.02); filter: contrast(1.3) brightness(1.4) grayscale(0); }
      96% { transform: translate(0,0) scale(1); filter: contrast(1.1) brightness(0.9) grayscale(0.2); }
    }
'''

if '.cctv-glitch-container' not in content:
    if '</style>' in content:
        content = content.replace('</style>', cctv_css + '\n  </style>')
    else:
        print("Error: Could not find </style> block.")
else:
    print("CSS already injected.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("CCTV Glitch injected successfully!")
