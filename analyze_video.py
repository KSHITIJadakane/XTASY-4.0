import os
import subprocess
import cv2

video_path = r"c:\Users\rajur\OneDrive\Desktop\xtasy\Squid Game landing page — design concept in motion.Bold, immersive, and deadly clean.#design #we.mp4"
out_dir = r"c:\Users\rajur\OneDrive\Desktop\xtasy\scratch_frames"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Video: {width}x{height}, FPS: {fps}, Total frames: {total_frames}, Duration: {duration:.2f}s")

# Extract frame every 0.5s or key transition points
step = int(fps * 0.5)
saved = 0
for i in range(0, total_frames, step):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if ret:
        t = i / fps
        fn = os.path.join(out_dir, f"frame_{saved:03d}_{t:.2f}s.jpg")
        cv2.imwrite(fn, frame)
        saved += 1

print(f"Saved {saved} sample frames to {out_dir}")
cap.release()
