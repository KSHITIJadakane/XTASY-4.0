import os, sys
sys.path.insert(0, os.path.abspath('.'))
import take_snap
from PIL import Image, ImageChops, ImageStat

os.makedirs('scratch_frames/verify_final', exist_ok=True)

# 1. Capture start state
take_snap.take_snapshot('index.html?s=start', 'scratch_frames/verify_final/start_state.png', delay_s=0.5, width=1440, height=900)
# 2. Capture end state
take_snap.take_snapshot('index.html?s=end', 'scratch_frames/verify_final/end_state.png', delay_s=0.5, width=1440, height=900)
# 3. Capture natural intro completion at delay=3.0s
take_snap.take_snapshot('index.html', 'scratch_frames/verify_final/natural_settled.png', delay_s=3.0, width=1440, height=900)

im_start = Image.open('scratch_frames/verify_final/start_state.png')
im_end = Image.open('scratch_frames/verify_final/end_state.png')
im_nat = Image.open('scratch_frames/verify_final/natural_settled.png')

print("Verification Extrema:")
print("Start state extrema:", im_start.getextrema())
print("End state extrema:", im_end.getextrema())
print("Natural settled extrema:", im_nat.getextrema())

diff_end_nat = ImageChops.difference(im_end, im_nat)
diff_stat = ImageStat.Stat(diff_end_nat).mean
print("Difference between end_state and natural_settled:", diff_stat)

# Verify start has 0 text brightness in the XTASY text region
crop_start_text = im_start.crop((200, 150, 600, 350))
print("Start text crop mean RGB:", [round(x, 2) for x in ImageStat.Stat(crop_start_text).mean])

# Verify natural settled has full text brightness
crop_nat_text = im_nat.crop((200, 150, 600, 350))
print("Natural settled text crop mean RGB:", [round(x, 2) for x in ImageStat.Stat(crop_nat_text).mean])
