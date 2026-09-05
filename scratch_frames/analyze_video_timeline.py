import os
from PIL import Image, ImageChops, ImageStat

crop_box = (60, 460, 660, 820)
frames = []
for i in range(1, 31):
    f_path = f'scratch_frames/intro_detail/f_{i:03d}.png'
    im = Image.open(f_path).crop(crop_box)
    out_crop = f'scratch_frames/intro_crops/crop_{i:03d}.png'
    im.save(out_crop)
    frames.append(im)

settled = frames[24] # f_025 is t=2.4s
start = frames[0]   # f_001 is t=0.0s

print(f"{'t (s)':<8} | {'Frame':<8} | {'Text Region (S Q)':<20} | {'Crowd Region':<18} | {'Total Diff':<15} | {'Normalized % Progress':<22}")
print('-'*100)

stat_diff_max = ImageStat.Stat(ImageChops.difference(settled, start)).mean[0]

timeline_data = []
for i in range(30):
    t = round(i * 0.1, 1)
    im = frames[i]
    crop_text = im.crop((40, 100, 200, 240))
    stat_text = ImageStat.Stat(crop_text).mean[0]
    
    crop_crowd = im.crop((40, 270, 560, 350))
    stat_crowd = ImageStat.Stat(crop_crowd).mean[0]
    
    diff = ImageChops.difference(im, start)
    stat_diff = ImageStat.Stat(diff).mean[0]
    pct = min(100.0, (stat_diff / (stat_diff_max + 1e-5)) * 100.0)
    timeline_data.append((t, f"f_{i+1:03d}", stat_text, stat_crowd, stat_diff, pct))
    print(f"{t:<8.1f} | f_{i+1:03d}   | {stat_text:<20.2f} | {stat_crowd:<18.2f} | {stat_diff:<15.2f} | {pct:<22.1f}%")
