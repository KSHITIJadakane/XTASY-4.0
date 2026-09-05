import os, sys
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Setup test for Option A (Exponential Light Decay)
opt_a_defs = '''      <!-- Diffusion 1: Multi-stop Exponential Light Decay (1365 to 1650) -->
      <linearGradient id="diffuseBeam" x1="1365" y1="475" x2="1650" y2="475" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
        <stop offset="25%" stop-color="#F1F5F9" stop-opacity="0.85"/>
        <stop offset="50%" stop-color="#CBD5E1" stop-opacity="0.45"/>
        <stop offset="75%" stop-color="#94A3B8" stop-opacity="0.15"/>
        <stop offset="90%" stop-color="#64748B" stop-opacity="0.04"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </linearGradient>'''

opt_a_elem = '''                  <!-- Option A: Exponential Diffusion Laser Beam -->
                  <path d="M 1365 475 L 1650 475" stroke="url(#diffuseBeam)" stroke-width="34" stroke-linecap="butt"/>'''

target_dash = '''                  <!-- Proportional sleek dash matching GAME- DNA with rounded cap (no boxy corners) -->
                  <path d="M 1365 475 L 1455 475" stroke="url(#metallicWhite40)" stroke-width="34" stroke-linecap="round"/>'''

# Replace for Option A
h_a = html.replace('</defs>', opt_a_defs + '\n    </defs>').replace(target_dash, opt_a_elem)
with open('index_opt_a.html', 'w', encoding='utf-8') as f:
    f.write(h_a)

# Setup test for Option D (Dual-Layer Glow Diffusion)
opt_d_defs = '''      <!-- Diffusion D: Core + Atmospheric Aura -->
      <linearGradient id="diffuseBeam" x1="1365" y1="475" x2="1650" y2="475" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
        <stop offset="25%" stop-color="#F1F5F9" stop-opacity="0.85"/>
        <stop offset="50%" stop-color="#CBD5E1" stop-opacity="0.45"/>
        <stop offset="75%" stop-color="#94A3B8" stop-opacity="0.15"/>
        <stop offset="90%" stop-color="#64748B" stop-opacity="0.04"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </linearGradient>
      <filter id="auraBlur" x="-20%" y="-100%" width="140%" height="300%">
        <feGaussianBlur stdDeviation="8"/>
      </filter>
      <linearGradient id="auraGrad" x1="1365" y1="475" x2="1680" y2="475" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
        <stop offset="30%" stop-color="#E2E8F0" stop-opacity="0.4"/>
        <stop offset="70%" stop-color="#94A3B8" stop-opacity="0.12"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </linearGradient>'''

opt_d_elem = '''                  <!-- Option D: Dual-Layer Glow Diffusion -->
                  <path d="M 1365 475 L 1680 475" stroke="url(#auraGrad)" stroke-width="54" filter="url(#auraBlur)"/>
                  <path d="M 1365 475 L 1650 475" stroke="url(#diffuseBeam)" stroke-width="34" stroke-linecap="butt"/>'''

h_d = html.replace('</defs>', opt_d_defs + '\n    </defs>').replace(target_dash, opt_d_elem)
with open('index_opt_d.html', 'w', encoding='utf-8') as f:
    f.write(h_d)

take_snap.take_snapshot('index_opt_a.html', 'scratch_frames/snap_opt_a.png', delay_s=2.5)
take_snap.take_snapshot('index_opt_d.html', 'scratch_frames/snap_opt_d.png', delay_s=2.5)

# Generate zoomed crops of 4.0 for both
im_a = Image.open('scratch_frames/snap_opt_a.png')
crop_a = im_a.crop((850, 340, 1440, 560))
crop_a.save('scratch_frames/crop_opt_a.png')

im_d = Image.open('scratch_frames/snap_opt_d.png')
crop_d = im_d.crop((850, 340, 1440, 560))
crop_d.save('scratch_frames/crop_opt_d.png')

print('Rendered full page and crops for Option A and Option D')
