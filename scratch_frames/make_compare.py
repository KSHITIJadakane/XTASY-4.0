import os, sys
sys.path.append('.')
import take_snap

html_content = """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@700&family=Space+Grotesk:wght@800&family=Space+Mono:wght@700&display=swap" rel="stylesheet"/>
<style>
  body { background: #000; color: #fff; margin: 40px; font-family: sans-serif; }
  .row { margin-bottom: 45px; }
  h3 { color: #aaa; font-size: 14px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; }
  svg { background: #080808; border: 1px solid #222; border-radius: 8px; display: block; }
</style>
</head>
<body>

<div class="row">
  <h3>Style 1: Architectural Razor-Sharp Stencil (Crisp square cuts, miter joins, matching GAME-)</h3>
  <svg width="700" height="180" viewBox="1000 380 650 200">
    <defs>
      <linearGradient id="pink1" x1="0" y1="380" x2="0" y2="560" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#BA134D"/>
        <stop offset="60%" stop-color="#A10E42"/>
        <stop offset="100%" stop-color="#780A30"/>
      </linearGradient>
      <linearGradient id="white1" x1="0" y1="380" x2="0" y2="560" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#FFFFFF"/>
        <stop offset="60%" stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
      <linearGradient id="ext1" x1="1350" y1="475" x2="1620" y2="475" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#FFFFFF"/>
        <stop offset="70%" stop-color="rgba(255,255,255,0.75)"/>
        <stop offset="100%" stop-color="transparent"/>
      </linearGradient>
    </defs>
    <!-- Style 1: Architectural Razor-Sharp -->
    <g>
      <path d="M 1125 405 L 1050 488 L 1175 488" stroke="url(#pink1)" stroke-width="40" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
      <path d="M 1135 395 L 1135 550" stroke="url(#pink1)" stroke-width="40" stroke-linecap="butt"/>
      <rect x="1208" y="515" width="24" height="24" fill="url(#white1)"/>
      <rect x="1260" y="405" width="92" height="140" rx="24" stroke="url(#white1)" stroke-width="38" fill="none"/>
      <path d="M 1352 475 L 1620 475" stroke="url(#ext1)" stroke-width="38" stroke-linecap="butt"/>
      <path d="M 1595 450 L 1620 475 L 1595 500" stroke="url(#ext1)" stroke-width="16" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
    </g>
  </svg>
</div>

<div class="row">
  <h3>Style 2: Futuristic Chamfered Octagonal Tech (Digital Clock / Squid Game Piggy Bank Stencil)</h3>
  <svg width="700" height="180" viewBox="1000 380 650 200">
    <g>
      <path d="M 1138 395 L 1050 485 L 1050 515 L 1175 515 L 1175 480 L 1138 480 L 1138 435 L 1088 485 L 1138 485 Z" fill="url(#pink1)"/>
      <rect x="1122" y="395" width="36" height="155" fill="url(#pink1)"/>
      <polygon points="1210,530 1225,515 1240,530 1225,545" fill="url(#white1)"/>
      <path d="M 1290 400 L 1335 400 L 1365 435 L 1365 515 L 1335 550 L 1290 550 L 1260 515 L 1260 435 Z" stroke="url(#white1)" stroke-width="34" stroke-linejoin="miter" fill="none"/>
      <path d="M 1365 475 L 1620 475" stroke="url(#ext1)" stroke-width="34" stroke-linecap="butt"/>
      <polygon points="1600,455 1630,475 1600,495" fill="url(#white1)"/>
    </g>
  </svg>
</div>

<div class="row">
  <h3>Style 3: Ultra-Bold Antonio Display (Condensed, Powerful, High-Impact Typographic)</h3>
  <svg width="700" height="180" viewBox="1000 380 650 200">
    <text x="1045" y="540" font-family="'Antonio', sans-serif" font-size="180" font-weight="700" fill="url(#pink1)" letter-spacing="-2">4</text>
    <text x="1175" y="535" font-family="'Antonio', sans-serif" font-size="180" font-weight="700" fill="url(#white1)">.</text>
    <text x="1225" y="540" font-family="'Antonio', sans-serif" font-size="180" font-weight="700" fill="url(#white1)" letter-spacing="-2">0</text>
    <path d="M 1350 472 L 1620 472" stroke="url(#ext1)" stroke-width="34" stroke-linecap="butt"/>
    <path d="M 1595 450 L 1620 472 L 1595 494" stroke="url(#ext1)" stroke-width="14" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
  </svg>
</div>

</body>
</html>
"""

with open('scratch_frames/compare_40.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

take_snap.take_snapshot('scratch_frames/compare_40.html', 'scratch_frames/compare_40.png', delay_s=2.5, width=900, height=750)
print('Comparison snapshot captured!')
