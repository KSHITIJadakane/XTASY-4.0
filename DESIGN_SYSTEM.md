---
name: Kinetic Dystopia (v2 — corrected build)
status: implemented in squid-game-landing.html
colors:
  background: '#000000'
  surface: '#0c0c0c'
  text-primary: 'rgba(255,255,255,1)'
  text-secondary: 'rgba(255,255,255,0.70)'
  text-muted: 'rgba(255,255,255,0.38)'
  gridline: 'rgba(255,255,255,0.10)'
  primary-pink: '#FF007F'
  primary-magenta: '#E41A4A'
  contestant-green: '#037A4B'
  contestant-green-light: '#249C6B'
typography:
  display: { family: 'Space Grotesk', weight: 700, transform: uppercase }
  body: { family: 'Inter', weight: 400-600 }
  label: { family: 'Space Mono', weight: 400-700, transform: uppercase, tracking: wide }
---

## What changed from the Stitch export, and why

The original `code.html` from Stitch was a strong first pass — it already had scroll-reveal
and a parallax scaffold — but it shipped with one structural bug and a shallow motion layer:

1. **Hero collision (the bug in your screenshot).** The guard image sat on top of the
   "SQUID GAME" headline using `mix-blend-mode: screen`. That trick only disappears cleanly
   if the image's backdrop is *exactly* pure black — the AI-generated guard image isn't, so
   a visible dark rectangle sat over the middle of the word and ate the letters (you can see
   it in your screenshot: only "D" and "IE" survive). **Fix:** the guard image now sits
   *below* the headline in its own row, and is feathered at the edges with a CSS
   `mask-image: radial-gradient(...)` instead of a blend mode — that fades to transparent
   regardless of the source image's actual background color, so it always dissolves into the
   black page seamlessly.
2. **Flat, single-speed motion.** Everything used the same fade-up on scroll. There was no
   page-load moment, no cursor response, no sense of depth between layers.
3. **Decorative shapes collided with content.** The wireframe circle/triangle in "Rules of
   Survival" were positioned close enough to the rule numbers that they visually merged at
   certain viewport widths.
4. **Tailwind was loaded from the CDN `<script>` at runtime.** That's fine for prototyping in
   Stitch, but it re-computes the entire utility stylesheet in the browser on every load and
   will silently break if the CDN is blocked by a network policy or ad blocker. The shipped
   file now compiles Tailwind ahead of time into a single inlined stylesheet — same visual
   result, faster paint, no runtime dependency.

## Motion & interaction layer (new)

Per the brief's cinematic-suspense direction, motion is used to imply **surveillance,
tension, and depth** — not decoration. One orchestrated entrance, then purposeful responses
to the user's own scrolling and cursor:

| Moment | Effect | Why |
|---|---|---|
| Page load | Circle → triangle → square draw themselves in stroke-by-stroke, then the loader dissolves and "SQUID GAME" types on letter-by-letter | A single, deliberate opening beat, echoing the show's own title-card logic, instead of every element fading in independently |
| Scroll (hero) | Headline and guard image move at slightly different speeds (parallax) | Reads as physical depth rather than a flat cutout |
| Scroll (sections) | Each section rises 22px and fades in once, the first time it enters view | Restrained — no repeated bounce, no per-card stagger overload |
| Rules reveal | Numbers cascade in with a 110ms stagger, each pulsing its neon glow once as it lands | Rules "arrive" like a countdown, matching the section's content |
| Buttons | Magnetic pull toward the cursor within a small radius, plus the existing neon halo on hover | A tactile, "live" feeling on the two calls to action |
| Invitation card | 3D tilt that follows the cursor (`rotateX`/`rotateY` on mouse move) | The card feels handled, not just floating |
| Gallery images | Slow zoom + saturation lift on hover, label slides up | Environments feel like they're being "observed" rather than just displayed |
| Footer mask | Slow breathing glow behind the mask | Keeps the closing moment alive without looping motion elsewhere |
| Global | Fixed film-grain (SVG turbulence, 5% opacity, blend-mode overlay) + a soft vignette | Adds cinematic depth to flat black without adding a single extra HTTP request |
| Accessibility | Every animation is disabled via `prefers-reduced-motion: reduce`, falling back to instant, static states | Motion is a layer, not a requirement to use the page |

## Structural notes for future edits

- **Single file, no build step required to run.** Tailwind is pre-compiled into the `<style>`
  block, so the file opens and works standalone (double-click, or any static host).
- **To change copy or add sections:** edit `squid-game-landing.html` directly — Tailwind
  utility classes are inlined as plain CSS, so no rebuild is needed unless you introduce a
  utility class that isn't already present in the file (see `PRD.md` → "Regenerating the
  stylesheet" if you do).
- **Images are hot-linked from Google's temporary AI-image host** (`lh3.googleusercontent.com`),
  carried over from the Stitch export. These URLs are tied to a generation session and are
  **not guaranteed to stay online** — before shipping this to production, download each image
  and self-host it (see PRD → Known Risks).
