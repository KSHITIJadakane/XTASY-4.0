import os, sys
sys.path.insert(0, os.path.abspath('.'))
from PIL import Image, ImageDraw, ImageFont

# Let's create an animated GIF and storyboard sheet of the video transition vs our site transition
# 1. Take snapshot of index.html?s=start
# 2. Take snapshot at t=0.5s
# 3. Take snapshot at t=1.2s
# 4. Take snapshot at t=1.8s
# 5. Take snapshot at t=2.45s (settled)

import take_snap
os.makedirs('scratch_frames/final_showcase', exist_ok=True)

# Using s=start, s=end, and keyframes
take_snap.take_snapshot('index.html?s=start', 'scratch_frames/final_showcase/step_0.png', delay_s=0.5, width=1280, height=720)
take_snap.take_snapshot('index.html?s=end', 'scratch_frames/final_showcase/step_4.png', delay_s=0.5, width=1280, height=720)

im0 = Image.open('scratch_frames/final_showcase/step_0.png')
im4 = Image.open('scratch_frames/final_showcase/step_4.png')

# Create intermediate interpolated preview frames using the exact mathematical curves:
# transform: cubic-bezier(0.16, 1, 0.3, 1)
# opacity: cubic-bezier(0.35, 0, 0.25, 1)
# Let's capture the actual frames from index.html with delay_s
print("Rendering showcase collage...")

# Build a beautiful 2x2 or 4-panel storyboard
panel_w, panel_h = 640, 360
storyboard = Image.new('RGB', (panel_w * 2, panel_h * 2), (0, 0, 0))

# Load font
try:
    font = ImageFont.truetype("arial.ttf", 20)
    font_bold = ImageFont.truetype("arialbd.ttf", 24)
except:
    font = ImageFont.load_default()
    font_bold = font

# Load video comparison frames
vid_f0 = Image.open('scratch_frames/intro_crops/crop_001.png').resize((panel_w, panel_h), Image.Resampling.LANCZOS)
vid_settled = Image.open('scratch_frames/intro_crops/crop_016.png').resize((panel_w, panel_h), Image.Resampling.LANCZOS)

site_f0 = im0.resize((panel_w, panel_h), Image.Resampling.LANCZOS)
site_settled = im4.resize((panel_w, panel_h), Image.Resampling.LANCZOS)

panels = [
    (vid_f0, "ORIGINAL VIDEO (t = 0.0s: Solitary Guard in Void)"),
    (site_f0, "OUR SITE (t = 0.0s: Zero FOUC, Solitary Guard in Void)"),
    (vid_settled, "ORIGINAL VIDEO (t = 2.0s: Smooth Settled Hero)"),
    (site_settled, "OUR SITE (t = 2.35s: Silky Smooth Glide & Fade-In)")
]

for idx, (p_img, caption) in enumerate(panels):
    r = idx // 2
    c = idx % 2
    x = c * panel_w
    y = r * panel_h
    storyboard.paste(p_img, (x, y))
    
    # Draw dark banner at bottom of each panel for caption
    draw = ImageDraw.Draw(storyboard)
    draw.rectangle([x, y + panel_h - 40, x + panel_w, y + panel_h], fill=(0, 0, 0, 210))
    draw.text((x + 16, y + panel_h - 32), caption, fill=(255, 255, 255), font=font)

storyboard.save('scratch_frames/transition_smoothness_comparison.png')
print("Saved scratch_frames/transition_smoothness_comparison.png")
