import re
import take_snap

with open('index.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Update crowd-layer CSS with edge gradient mask to ensure zero boxed cuts
base_html = base_html.replace(
    '.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(280px,40vh,480px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(24px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1)}',
    '.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(280px,40vh,480px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(24px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1);mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%);-webkit-mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%)}'
)

s1_svg = """<g id="frontTitle40" filter="url(#softShadow)">
                  <!-- '4': Sharp diagonal, flat horizontal shelf, solid vertical spine with athletic stencil break -->
                  <path d="M 1125 405 L 1045 490 L 1180 490" stroke="url(#pinkNeon4)" stroke-width="36" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
                  <path d="M 1135 395 L 1135 468" stroke="url(#pinkNeon4)" stroke-width="36" stroke-linecap="butt"/>
                  <path d="M 1135 506 L 1135 550" stroke="url(#pinkNeon4)" stroke-width="36" stroke-linecap="butt"/>
                  <!-- Dot '.' (square architectural block) -->
                  <rect x="1215" y="520" width="24" height="24" fill="url(#metallicWhite40)"/>
                  <!-- '0': Bold architectural squircle with flat top and bottom -->
                  <rect x="1270" y="405" width="95" height="140" rx="26" stroke="url(#metallicWhite40)" stroke-width="34" fill="none"/>
                  <!-- Horizontal extending laser beam shooting directly from 0 center -->
                  <path d="M 1365 475 L 1620 475" stroke="url(#extLine)" stroke-width="34" stroke-linecap="butt"/>
                  <path d="M 1595 452 L 1620 475 L 1595 498" stroke="url(#extLine)" stroke-width="14" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
                </g>"""

s2_svg = """<g id="frontTitle40" filter="url(#softShadow)">
                  <!-- '4': Equilateral Triangle peak on top (Soldier mask Triangle) -->
                  <polygon points="1100,395 1040,490 1170,490" stroke="url(#pinkNeon4)" stroke-width="32" stroke-linejoin="round" fill="none"/>
                  <line x1="1135" y1="480" x2="1135" y2="550" stroke="url(#pinkNeon4)" stroke-width="36" stroke-linecap="butt"/>
                  <!-- Dot '.' (Square mask) -->
                  <rect x="1210" y="520" width="26" height="26" fill="url(#metallicWhite40)"/>
                  <!-- '0': Worker Circle with laser beam -->
                  <ellipse cx="1315" cy="475" rx="54" ry="68" stroke="url(#metallicWhite40)" stroke-width="32" fill="none"/>
                  <line x1="1369" y1="475" x2="1620" y2="475" stroke="url(#extLine)" stroke-width="32" stroke-linecap="butt"/>
                  <path d="M 1595 454 L 1620 475 L 1595 496" stroke="url(#extLine)" stroke-width="12" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
                </g>"""

s3_svg = """<g id="frontTitle40" filter="url(#softShadow)">
                  <!-- '4': Chamfered polygon font matching GAME- -->
                  <path d="M 1125 398 L 1040 490 L 1180 490" stroke="url(#pinkNeon4)" stroke-width="34" stroke-linecap="square" stroke-linejoin="bevel" fill="none"/>
                  <line x1="1135" y1="398" x2="1135" y2="550" stroke="url(#pinkNeon4)" stroke-width="34" stroke-linecap="square"/>
                  <!-- Dot '.' (Chamfered diamond) -->
                  <polygon points="1225,518 1238,532 1225,546 1212,532" fill="url(#metallicWhite40)"/>
                  <!-- '0': Chamfered Octagonal 0 -->
                  <path d="M 1290 405 L 1340 405 L 1360 425 L 1360 525 L 1340 545 L 1290 545 L 1270 525 L 1270 425 Z" stroke="url(#metallicWhite40)" stroke-width="32" stroke-linejoin="miter" fill="none"/>
                  <line x1="1360" y1="475" x2="1620" y2="475" stroke="url(#extLine)" stroke-width="32" stroke-linecap="butt"/>
                  <path d="M 1595 452 L 1620 475 L 1595 498" stroke="url(#extLine)" stroke-width="14" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>
                </g>"""

# Replace in base_html
pattern = r'<g id="frontTitle40".*?</g>\s*</g>'
h1 = re.sub(pattern, s1_svg + '\n              </g>', base_html, flags=re.DOTALL)
h2 = re.sub(pattern, s2_svg + '\n              </g>', base_html, flags=re.DOTALL)
h3 = re.sub(pattern, s3_svg + '\n              </g>', base_html, flags=re.DOTALL)

# Fix asset paths for files in scratch_frames
h1 = h1.replace('src="assets/', 'src="../assets/')
h2 = h2.replace('src="assets/', 'src="../assets/')
h3 = h3.replace('src="assets/', 'src="../assets/')

with open('scratch_frames/test_hero_s1.html', 'w', encoding='utf-8') as f: f.write(h1)
with open('scratch_frames/test_hero_s2.html', 'w', encoding='utf-8') as f: f.write(h2)
with open('scratch_frames/test_hero_s3.html', 'w', encoding='utf-8') as f: f.write(h3)

print('Taking snapshots of 3 candidate styles...')
take_snap.take_snapshot('scratch_frames/test_hero_s1.html', 'scratch_frames/snap_hero_s1.png', delay_s=2.5, width=1440, height=900)
take_snap.take_snapshot('scratch_frames/test_hero_s2.html', 'scratch_frames/snap_hero_s2.png', delay_s=2.5, width=1440, height=900)
take_snap.take_snapshot('scratch_frames/test_hero_s3.html', 'scratch_frames/snap_hero_s3.png', delay_s=2.5, width=1440, height=900)

print('All 3 hero candidate snapshots taken!')
