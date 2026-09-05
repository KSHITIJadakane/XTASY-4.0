import os, sys, time
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image, ImageStat, ImageChops

test_file = 'scratch_frames/test_smooth_transition.html'
timestamps = [0.05, 0.3, 0.6, 1.0, 1.5, 2.45]
labels = ['0.05s (Start Void)', '0.3s (Gentle Awakening)', '0.6s (Smooth Glide)', '1.0s (Mid Flight)', '1.5s (Decelerating)', '2.45s (Settled Rest)']

snaps = []
os.makedirs('scratch_frames/smooth_run', exist_ok=True)

print(f"{'Time':<8} | {'Label':<25} | {'Text Region Brightness':<25} | {'Crowd Brightness':<20}")
print('-'*80)

for idx, (t, lbl) in enumerate(zip(timestamps, labels)):
    out_path = f'scratch_frames/smooth_run/frame_{idx}.png'
    take_snap.take_snapshot(test_file, out_path, delay_s=t, width=1024, height=575)
    im = Image.open(out_path)
    snaps.append(im)
    
    # Measure text region
    crop_text = im.crop((100, 100, 350, 250))
    stat_text = ImageStat.Stat(crop_text).mean[0]
    
    # Measure crowd region
    crop_crowd = im.crop((50, 420, 950, 560))
    stat_crowd = ImageStat.Stat(crop_crowd).mean[0]
    
    print(f"{t:<8.2f} | {lbl:<25} | {stat_text:<25.2f} | {stat_crowd:<20.2f}")

# Create visual comparison montage
w, h = 512, 287
montage = Image.new('RGB', (w * 2, h * 3), (0, 0, 0))
for idx, im in enumerate(snaps):
    r = idx // 2
    c = idx % 2
    thumb = im.resize((w, h), Image.Resampling.LANCZOS)
    montage.paste(thumb, (c * w, r * h))

montage.save('scratch_frames/smooth_montage.png')
print('Saved scratch_frames/smooth_montage.png')

# Also generate high-quality GIF
gif_frames = [im.resize((640, 360), Image.Resampling.LANCZOS) for im in snaps]
gif_frames = gif_frames + [gif_frames[-1]] * 4
gif_frames[0].save(
    'scratch_frames/smooth_transition.gif',
    save_all=True,
    append_images=gif_frames[1:],
    duration=[250, 300, 400, 500, 500, 700, 300, 300, 300, 300],
    loop=0
)
print('Saved scratch_frames/smooth_transition.gif')
