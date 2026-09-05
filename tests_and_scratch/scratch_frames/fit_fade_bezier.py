import numpy as np
from scipy.optimize import minimize

def bezier_pt(p0, p1, p2, p3, t):
    return (1-t)**3 * p0 + 3*(1-t)**2 * t * p1 + 3*(1-t) * t**2 * p2 + t**3 * p3

target_times = [0.0, 0.15, 0.30, 0.50, 0.70, 1.0]
target_vals =  [0.0, 0.06, 0.24, 0.60, 0.85, 1.0]

def loss(params):
    p1x, p1y, p2x, p2y = params
    ts = np.linspace(0, 1, 400)
    xs = [bezier_pt(0, p1x, p2x, 1, t) for t in ts]
    ys = [bezier_pt(0, p1y, p2y, 1, t) for t in ts]
    total_err = 0.0
    for tt, tv in zip(target_times, target_vals):
        idx = np.argmin(np.abs(np.array(xs) - tt))
        total_err += (ys[idx] - tv)**2
    return total_err

res = minimize(loss, [0.4, 0.0, 0.2, 1.0], bounds=[(0.01, 0.99), (-0.5, 1.5), (0.01, 0.99), (-0.5, 1.5)])
p1x, p1y, p2x, p2y = [round(x, 2) for x in res.x]
print(f"Optimal Bezier for Fade-In: cubic-bezier({p1x}, {p1y}, {p2x}, {p2y})")

# Let's test standard curves like cubic-bezier(0.4, 0, 0.2, 1) [Material standard / EaseInOut], cubic-bezier(0.25, 0.1, 0.25, 1), etc.
for name, p in [
    ("Optimized Fit", (p1x, p1y, p2x, p2y)),
    ("Ease-In-Out (0.4, 0, 0.2, 1)", (0.4, 0.0, 0.2, 1.0)),
    ("Smooth Cine Fade (0.35, 0, 0.25, 1)", (0.35, 0.0, 0.25, 1.0)),
    ("Gentle Ease-Out (0.2, 0.8, 0.2, 1)", (0.2, 0.8, 0.2, 1.0)),
]:
    ts = np.linspace(0, 1, 400)
    xs = [bezier_pt(0, p[0], p[2], 1, t) for t in ts]
    ys = [bezier_pt(0, p[1], p[3], 1, t) for t in ts]
    vals = []
    for tt in target_times:
        idx = np.argmin(np.abs(np.array(xs) - tt))
        vals.append(round(ys[idx], 3))
    print(f"{name:<35}: {vals}")
