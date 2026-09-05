import os
from PIL import Image

# Let's track the left edge of 'S' in the text across frames f_002 to f_016
for i in range(1, 18):
    im = Image.open(f'scratch_frames/intro_crops/crop_{i:03d}.png').convert('L')
    # Row strip across the middle of the 'S' letter: y from 130 to 180, x from 50 to 200
    strip = im.crop((50, 150, 200, 151))
    pixels = list(strip.getdata())
    # find first pixel exceeding threshold 35
    first_x = None
    for x_idx, p in enumerate(pixels):
        if p > 35:
            first_x = 50 + x_idx
            break
    t = round((i - 1) * 0.1, 1)
    print(f"t={t:.1f}s (f_{i:03d}): 'S' left edge x = {first_x}")
