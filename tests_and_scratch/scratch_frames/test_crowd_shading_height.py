import os, sys
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Current .crowd-layer rule in index.html
old_crowd_css = """.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(280px,40vh,480px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(24px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1);mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%);-webkit-mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%)}"""

old_crowd_img = """.crowd-layer img{width:100%;height:100%;object-fit:cover;object-position:center top;display:block}"""

# Candidate 1: height 26vh (clamp 180px, 26vh, 290px), subtle shading overlay & color grade
c1_css = """.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(180px,26vh,290px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(20px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1);mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%);-webkit-mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%)}
    .crowd-layer::after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.92) 0%,rgba(0,0,0,.6) 32%,rgba(0,0,0,.15) 65%,transparent 100%);pointer-events:none}"""

c1_img = """.crowd-layer img{width:100%;height:100%;object-fit:cover;object-position:center top;display:block;filter:brightness(.86) contrast(1.18) saturate(.85)}"""

# Candidate 2: height 24vh (clamp 170px, 24vh, 270px), slightly deeper trim and shading
c2_css = """.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(170px,24vh,270px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(20px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1);mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%);-webkit-mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%)}
    .crowd-layer::after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.94) 0%,rgba(0,0,0,.68) 35%,rgba(0,0,0,.2) 70%,transparent 100%);pointer-events:none}"""

c2_img = """.crowd-layer img{width:100%;height:100%;object-fit:cover;object-position:center top;display:block;filter:brightness(.84) contrast(1.2) saturate(.82)}"""

# Candidate 3: height 28vh (clamp 190px, 28vh, 310px), moderate shading
c3_css = """.crowd-layer{position:absolute;bottom:0;left:0;right:0;width:100%;height:clamp(190px,28vh,310px);pointer-events:none;z-index:35;overflow:hidden;opacity:0;transform:translateY(20px);transition:opacity 2s cubic-bezier(.16,1,.3,1),transform 2s cubic-bezier(.16,1,.3,1);mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%);-webkit-mask-image:linear-gradient(to right,transparent 0%,black 2%,black 98%,transparent 100%)}
    .crowd-layer::after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.9) 0%,rgba(0,0,0,.55) 30%,rgba(0,0,0,.12) 60%,transparent 100%);pointer-events:none}"""

c3_img = """.crowd-layer img{width:100%;height:100%;object-fit:cover;object-position:center top;display:block;filter:brightness(.88) contrast(1.15) saturate(.88)}"""

h1 = html.replace(old_crowd_css, c1_css).replace(old_crowd_img, c1_img)
with open('test_crowd_c1.html', 'w', encoding='utf-8') as f:
    f.write(h1)

h2 = html.replace(old_crowd_css, c2_css).replace(old_crowd_img, c2_img)
with open('test_crowd_c2.html', 'w', encoding='utf-8') as f:
    f.write(h2)

h3 = html.replace(old_crowd_css, c3_css).replace(old_crowd_img, c3_img)
with open('test_crowd_c3.html', 'w', encoding='utf-8') as f:
    f.write(h3)

print('Generated HTML variants for Candidate 1, 2, and 3.')
take_snap.take_snapshot('test_crowd_c1.html', 'scratch_frames/snap_c1.png', delay_s=2.5, width=1440, height=900)
take_snap.take_snapshot('test_crowd_c2.html', 'scratch_frames/snap_c2.png', delay_s=2.5, width=1440, height=900)
take_snap.take_snapshot('test_crowd_c3.html', 'scratch_frames/snap_c3.png', delay_s=2.5, width=1440, height=900)
print('Completed snapshots for c1, c2, c3.')

# Build comparison image with ref_screen_from_user
ref = Image.open('scratch_frames/ref_screen_from_user.png')
# Resize ref to height 450 keeping aspect ratio
ref_resized = ref.resize((int(ref.width * (450 / ref.height)), 450), Image.Resampling.LANCZOS)

s1 = Image.open('scratch_frames/snap_c1.png').resize((int(1440 * (450 / 900)), 450), Image.Resampling.LANCZOS)
s2 = Image.open('scratch_frames/snap_c2.png').resize((int(1440 * (450 / 900)), 450), Image.Resampling.LANCZOS)
s3 = Image.open('scratch_frames/snap_c3.png').resize((int(1440 * (450 / 900)), 450), Image.Resampling.LANCZOS)

# Create 2x2 grid:
# Top Left: Reference Screen
# Top Right: Candidate 1 (26vh, balanced)
# Bottom Left: Candidate 2 (24vh, trimmed lower)
# Bottom Right: Candidate 3 (28vh, moderate)
grid_w = ref_resized.width + s1.width + 40
grid_h = 450 * 2 + 60
comp = Image.new('RGB', (grid_w, grid_h), (10, 10, 10))

comp.paste(ref_resized, (20, 20))
comp.paste(s1, (ref_resized.width + 30, 20))
comp.paste(s2, (20, 450 + 40))
comp.paste(s3, (ref_resized.width + 30, 450 + 40))

comp.save('scratch_frames/compare_crowd_candidates.png')
print('Saved compare_crowd_candidates.png')
