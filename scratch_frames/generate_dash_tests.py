import sys, os
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''                  <!-- Horizontal extending laser beam shooting directly from 0 center -->
                  <path d="M 1365 475 L 1620 475" stroke="url(#extLine)" stroke-width="34" stroke-linecap="butt"/>
                  <path d="M 1595 452 L 1620 475 L 1595 498" stroke="url(#extLine)" stroke-width="14" stroke-linecap="butt" stroke-linejoin="miter" fill="none"/>'''

# Test 1: Round cap proportional dash (100px)
t1 = html.replace(
    target,
    '                  <!-- Proportional dash with rounded cap matching XTASY caps -->\n                  <path d="M 1365 475 L 1465 475" stroke="url(#metallicWhite40)" stroke-width="34" stroke-linecap="round"/>'
)
with open('scratch_frames/test_dash_round.html', 'w', encoding='utf-8') as f:
    f.write(t1)

# Test 2: Butt cap proportional dash (90px)
t2 = html.replace(
    target,
    '                  <!-- Proportional architectural flat dash matching GAME- -->\n                  <path d="M 1365 475 L 1455 475" stroke="url(#metallicWhite40)" stroke-width="34" stroke-linecap="butt"/>'
)
with open('scratch_frames/test_dash_butt.html', 'w', encoding='utf-8') as f:
    f.write(t2)

# Test 3: Pure 4.0 (no dash)
t3 = html.replace(
    target,
    '                  <!-- Pure 4.0 without dash -->'
)
with open('scratch_frames/test_dash_none.html', 'w', encoding='utf-8') as f:
    f.write(t3)

take_snap.take_snapshot('scratch_frames/test_dash_round.html', 'scratch_frames/snap_dash_round.png', delay_s=2.5)
take_snap.take_snapshot('scratch_frames/test_dash_butt.html', 'scratch_frames/snap_dash_butt.png', delay_s=2.5)
take_snap.take_snapshot('scratch_frames/test_dash_none.html', 'scratch_frames/snap_dash_none.png', delay_s=2.5)

# Now crop the 4.0 area from each and stitch together
im_round = Image.open('scratch_frames/snap_dash_round.png')
im_butt = Image.open('scratch_frames/snap_dash_butt.png')
im_none = Image.open('scratch_frames/snap_dash_none.png')

# 4.0 bounding box in 1440x900 viewport:
# svg is 1600x976, preserveAspectRatio xMidYMid
# Let's crop around x: 800 to 1400, y: 300 to 650
crop_box = (800, 300, 1400, 600)
c_round = im_round.crop(crop_box)
c_butt = im_butt.crop(crop_box)
c_none = im_none.crop(crop_box)

# Stack vertically
w = 600
h = 300 * 3
combined = Image.new('RGB', (w, h), (0, 0, 0))
combined.paste(c_round, (0, 0))
combined.paste(c_butt, (0, 300))
combined.paste(c_none, (0, 600))
combined.save('scratch_frames/compare_dash_options.png')
print('Successfully generated comparison image.')
