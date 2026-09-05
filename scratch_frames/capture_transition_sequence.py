import os, sys, time
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image

timestamps = [0.08, 0.4, 0.8, 1.3, 1.8, 2.45]
labels = ['0.08s (Start)', '0.4s (Early Fade)', '0.8s (Mid Glide)', '1.3s (Decelerating)', '1.8s (Near Rest)', '2.45s (Settled)']

snaps = []
for idx, (t, lbl) in enumerate(zip(timestamps, labels)):
    out_path = f'scratch_frames/site_transition_t{idx}.png'
    take_snap.take_snapshot('index.html', out_path, delay_s=t, width=1024, height=575)
    snaps.append(Image.open(out_path))
    print(f'Captured {out_path} at delay {t}s ({lbl})')

# Create a 3x2 montage
w, h = 512, 287
montage = Image.new('RGB', (w * 2, h * 3), (0, 0, 0))

for idx, im in enumerate(snaps):
    r = idx // 2
    c = idx % 2
    thumb = im.resize((w, h), Image.Resampling.LANCZOS)
    montage.paste(thumb, (c * w, r * h))

montage.save('scratch_frames/site_transition_timeline.png')
print('Saved site_transition_timeline.png')

# Also export as animated GIF!
gif_frames = [im.resize((640, 360), Image.Resampling.LANCZOS) for im in snaps]
# Repeat settled frame a few times for pause
gif_frames = gif_frames + [gif_frames[-1]] * 4
gif_frames[0].save(
    'scratch_frames/site_transition_preview.gif',
    save_all=True,
    append_images=gif_frames[1:],
    duration=[200, 350, 450, 450, 450, 600, 300, 300, 300, 300],
    loop=0
)
print('Saved site_transition_preview.gif')
