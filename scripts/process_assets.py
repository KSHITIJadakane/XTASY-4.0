import os
from PIL import Image, ImageFilter
import numpy as np
from collections import deque

def process_pink_guard():
    src_path = r"C:\Users\rajur\.gemini\antigravity-ide\brain\f8486acf-8315-457e-ba54-d9902e5c8298\pink_guard_reference_match_1788640751360.jpg"
    img = Image.open(src_path)
    arr = np.array(img)
    h, w, _ = arr.shape
    max_c = np.max(arr, axis=2)

    # BFS from outer borders to find solid black background
    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    for x in range(w):
        if max_c[0, x] < 12:
            q.append((0, x))
            visited[0, x] = True
        if max_c[h-1, x] < 12:
            q.append((h-1, x))
            visited[h-1, x] = True
    for y in range(h):
        if max_c[y, 0] < 12:
            q.append((y, 0))
            visited[y, 0] = True
        if max_c[y, w-1] < 12:
            q.append((y, w-1))
            visited[y, w-1] = True

    while q:
        y, x = q.popleft()
        for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx]:
                if max_c[ny, nx] < 12:
                    visited[ny, nx] = True
                    q.append((ny, nx))

    # Guard mask is ~visited
    guard_mask = (~visited).astype(np.uint8) * 255
    
    # Smooth edge slightly for beautiful anti-aliasing
    mask_im = Image.fromarray(guard_mask, 'L')
    mask_im = mask_im.filter(ImageFilter.GaussianBlur(radius=0.8))
    
    # Create RGBA
    rgba = np.dstack([arr, np.array(mask_im)])
    guard_rgba = Image.fromarray(rgba, 'RGBA')

    # Bounding box of guard
    ys, xs = np.where(guard_mask > 0)
    min_y, max_y = np.min(ys), np.max(ys)
    min_x, max_x = np.min(xs), np.max(xs)
    guard_crop = guard_rgba.crop((min_x, min_y, max_x, max_y))

    # Target canvas 1600x976
    canvas = Image.new('RGBA', (1600, 976), (0, 0, 0, 0))
    
    # We want guard head at y = 310, centered at x = 800
    # Guard width in crop:
    cw, ch = guard_crop.size
    # Target height: from y=310 down to 976 is 666px
    target_h = 700
    target_w = int(cw * (target_h / ch))
    guard_scaled = guard_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    paste_x = 800 - target_w // 2
    paste_y = 310
    canvas.paste(guard_scaled, (paste_x, paste_y), guard_scaled)
    
    os.makedirs('assets', exist_ok=True)
    canvas.save('assets/guard_clean_cutout.png')
    print(f"Guard cutout created: {target_w}x{target_h} at ({paste_x}, {paste_y})")

def process_crowd():
    src_path = r"C:\Users\rajur\.gemini\antigravity-ide\brain\f8486acf-8315-457e-ba54-d9902e5c8298\standing_squid_players_crowd_1788641196572.jpg"
    img = Image.open(src_path)
    arr = np.array(img)
    h, w, _ = arr.shape
    br = np.max(arr, axis=2)

    # For each column, find upper contour (first pixel with br > 14)
    top_y = np.zeros(w, dtype=int)
    for x in range(w):
        hits = np.where(br[:, x] > 14)[0]
        if len(hits) > 0:
            top_y[x] = hits[0]
        else:
            top_y[x] = h

    # Build 100% solid mask below contour for every column
    # This guarantees NO holes, NO transparent bodies, 100% solid standing players!
    mask = np.zeros((h, w), dtype=np.uint8)
    for x in range(w):
        mask[top_y[x]:, x] = 255

    mask_im = Image.fromarray(mask, 'L').filter(ImageFilter.GaussianBlur(radius=1.2))
    rgba = np.dstack([arr, np.array(mask_im)])
    crowd_rgba = Image.fromarray(rgba, 'RGBA')

    # Bounding box of crowd from min_top_y to h
    min_top_y = np.min(top_y)
    crowd_crop = crowd_rgba.crop((0, min_top_y, w, h))
    
    # Scale to canvas 1600x976
    # Width = 1600
    crowd_w, crowd_h = crowd_crop.size
    target_w = 1600
    target_h = int(crowd_h * (target_w / crowd_w))
    crowd_scaled = crowd_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Target height on canvas: 330px so highest head is at y=646
    target_h_canvas = 330
    crowd_final = crowd_scaled.resize((1600, target_h_canvas), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (1600, 976), (0, 0, 0, 0))
    paste_y = 976 - target_h_canvas
    canvas.paste(crowd_final, (0, paste_y), crowd_final)
    canvas.save('assets/hero_players_foreground.png')
    print(f"Crowd cutout created: 1600x{target_h_canvas} pasted at y={paste_y}. Highest head at y={paste_y}")

if __name__ == '__main__':
    process_pink_guard()
    process_crowd()
