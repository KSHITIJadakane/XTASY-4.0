import os
from PIL import Image

# Check vertical position of the crowd top edge across frames f_002 to f_016
# In crop_xxx.png, crowd heads are roughly y=250 to 290
for i in range(1, 18):
    im = Image.open(f'scratch_frames/intro_crops/crop_{i:03d}.png').convert('L')
    # Column strip at x=150 (over player heads), y from 220 to 320
    strip = im.crop((150, 220, 151, 320))
    pixels = list(strip.get_flattened_data())
    # find first pixel exceeding threshold 30
    first_y = None
    for y_idx, p in enumerate(pixels):
        if p > 30:
            first_y = 220 + y_idx
            break
    t = round((i - 1) * 0.1, 1)
    print(f"t={t:.1f}s (f_{i:03d}): Crowd top edge y = {first_y}")
