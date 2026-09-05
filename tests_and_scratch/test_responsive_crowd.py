import take_snap

resolutions = [
    ("1920x1080", 1920, 1080),
    ("1366x768", 1366, 768),
    ("1600x900", 1600, 900),
    ("2560x1440", 2560, 1440),
]

for name, w, h in resolutions:
    out_file = f"scratch_frames/res_check_{name}.png"
    print(f"Testing {name} ({w}x{h})...")
    take_snap.take_snapshot("scratch_frames/test_hero_s1.html", out_file, delay_s=2.5, width=w, height=h)
    print(f"Done {name}")

print("All resolution checks complete!")
