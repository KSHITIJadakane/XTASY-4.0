import os
import subprocess
import time
from PIL import Image

def take_snapshot(file_path, out_png, delay_s=2.5, width=1440, height=900):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    
    abs_out = os.path.abspath(out_png)
    if os.path.exists(abs_out):
        try: os.remove(abs_out)
        except: pass
    
    suffix = ""
    clean_path = file_path
    if "#" in file_path:
        clean_path, hash_part = file_path.split("#", 1)
        suffix = "#" + hash_part
    elif "?" in file_path:
        clean_path, q_part = file_path.split("?", 1)
        suffix = "?" + q_part

    url = "file:///" + os.path.abspath(clean_path).replace("\\", "/") + suffix
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={width},{height}",
        f"--screenshot={abs_out}",
        f"--virtual-time-budget={int(delay_s * 1000)}",
        url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.exists(abs_out)

if __name__ == "__main__":
    # Test preview end state
    ok = take_snapshot("scratch_frames/test_preview.html", "scratch_frames/preview_snap_end.png", delay_s=2.5)
    print("End state snapshot:", ok)
    # Test preview start state
    ok0 = take_snapshot("scratch_frames/test_preview.html", "scratch_frames/preview_snap_start.png", delay_s=0.05)
    print("Start state snapshot:", ok0)
