import numpy as np

def bezier_pt(p0, p1, p2, p3, t):
    return (1-t)**3 * p0 + 3*(1-t)**2 * t * p1 + 3*(1-t) * t**2 * p2 + t**3 * p3

def solve_bezier(p1x, p1y, p2x, p2y, num_pts=100):
    ts = np.linspace(0, 1, num_pts)
    xs = [bezier_pt(0, p1x, p2x, 1, t) for t in ts]
    ys = [bezier_pt(0, p1y, p2y, 1, t) for t in ts]
    return xs, ys

# Compare curves at t = 0.1, 0.2, 0.4, 0.6, 0.8, 1.0
curves = {
    'video_actual': [0.0, 0.06, 0.24, 0.60, 0.85, 1.0], # from our measurement
    'expo_out (0.16, 1, 0.3, 1)': [],
    'smooth_fade (0.25, 1, 0.4, 1)': [],
    'cubic_ease_out (0.33, 1, 0.68, 1)': []
}

test_times = [0.0, 0.15, 0.30, 0.50, 0.70, 1.0]

for name, (p1x, p1y, p2x, p2y) in [
    ('expo_out (0.16, 1, 0.3, 1)', (0.16, 1, 0.3, 1)),
    ('smooth_fade (0.25, 1, 0.4, 1)', (0.25, 1, 0.4, 1)),
    ('cubic_ease_out (0.33, 1, 0.68, 1)', (0.33, 1, 0.68, 1))
]:
    xs, ys = solve_bezier(p1x, p1y, p2x, p2y, 500)
    for tt in test_times:
        # find closest x
        idx = np.argmin(np.abs(np.array(xs) - tt))
        curves[name].append(round(ys[idx], 3))

print(f"{'Time %':<10} | {'Video Actual':<15} | {'Expo Out':<15} | {'Smooth Fade':<15} | {'Cubic Ease Out':<15}")
print('-'*75)
for i, tt in enumerate(test_times):
    print(f"{int(tt*100):<9}% | {curves['video_actual'][i]:<15} | {curves['expo_out (0.16, 1, 0.3, 1)'][i]:<15} | {curves['smooth_fade (0.25, 1, 0.4, 1)'][i]:<15} | {curves['cubic_ease_out (0.33, 1, 0.68, 1)'][i]:<15}")
