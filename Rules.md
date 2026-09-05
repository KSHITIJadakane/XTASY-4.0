# Development Rules & AI Boundaries
## Squid Game / Quest Room Project Guidelines

---

### 1. Fundamental Principles
1. **Cinematic Immersion First**: Every interaction, animation, and color choice must serve the tension, suspense, and high-contrast dystopian aesthetic of the Squid Game universe.
2. **Zero-Dependency Architecture**: The project must remain 100% functional as a self-contained static application with zero build tools (`npm`, `webpack`), zero runtime UI frameworks (`React`, `Vue`), and zero external CSS libraries (`Tailwind`, `Bootstrap`).
3. **Respect User Freedom**: The experience is a **continuous scrolling website**, NOT a locked PowerPoint-style presentation or wheel-hijacking widget.

---

### 2. Strict AI & Developer Boundaries

#### ❌ FORBIDDEN PRACTICES (What You Must NEVER Do)
| Rule # | Forbidden Action | Reason & Impact |
| :--- | :--- | :--- |
| **R-01** | **NO External Frameworks** (Tailwind CDN, React, Bootstrap, jQuery) | Destroys zero-build portability, causes version drift, introduces render-blocking network latency. |
| **R-02** | **NO Wheel-Hijacking / Slide-Locking** (`overflow: hidden` on body, `translateY(-100vh)` lock) | Frustrates visitors on trackpads/touch screens and violates the user's explicit directive to make it a natural website. |
| **R-03** | **NO Right-Side Slide Dots** | Explicitly rejected by client. Re-introducing slide dots or PPT markers is a direct regression. |
| **R-04** | **NO Remote Asset Hotlinking** (Googleusercontent, Imgur, Unsplash, external CDNs) | External links expire, get blocked by CORS/adblockers, or break offline usage. All media must reside in `./assets/`. |
| **R-05** | **NO Unsolicited Audio Autoplay** | Violates browser security policies; triggers user annoyance and console warnings. Audio must await explicit user gesture. |
| **R-06** | **NO Layout-Thrashing Animations** (animating `width`, `height`, `top`, `left`, `margin`, `padding`) | Triggers CPU reflow and drops frame rates below 60 FPS. Only animate `transform` and `opacity`. |
| **R-07** | **NO Invasive Popups or Third-Party Trackers** | Keeps the experience pristine, fast, and privacy-conscious. |

---

#### ✅ MANDATORY PRACTICES (What You MUST Always Do)
| Rule # | Required Action | Standard & Rationale |
| :--- | :--- | :--- |
| **R-08** | **Preserve the 4-Stage Power-On Intro (USP)** | Maintain the exact 4-stage illumination sequence (`hero_intro_0.png` through `hero_intro_3.png`) as the project's signature visual hook. |
| **R-09** | **Continuous Natural Scrolling** | Use native CSS scrolling (`overflow-y: auto; scroll-behavior: smooth;`) with `IntersectionObserver` for gliding text reveals. |
| **R-10** | **100% Local Asset Integrity** | All images and audio must be referenced via relative paths `./assets/<filename>`. Verify file presence before adding new assets. |
| **R-11** | **Hardware-Accelerated Compositing** | Force GPU rendering layers on dynamic elements using `will-change: transform, opacity` and `transform: translate3d(0,0,0)`. |
| **R-12** | **Full Accessibility Compliance** | Implement `@media (prefers-reduced-motion: reduce)` to disable heavy camera shake and rapid flickering for motion-sensitive users. |
| **R-13** | **Robust Error Handling** | Encapsulate Web Audio API and media playback in `try...catch` blocks to prevent silent JavaScript crashes. |

---

### 3. Coding Standards & Conventions

#### 3.1. CSS Architecture & Custom Properties
- All theme tokens must be defined at `:root` in `squid-game-landing.html`.
- Never use magic hex codes directly inside CSS rules; always reference standard tokens:
  ```css
  /* CORRECT */
  color: var(--pink-neon);
  box-shadow: 0 0 25px var(--pink-glow);

  /* FORBIDDEN */
  color: #FF007F;
  box-shadow: 0 0 25px rgba(255, 0, 127, 0.4);
  ```
- Use standardized easing curves:
  - Cinema Ease: `var(--ease-cinema)` (`cubic-bezier(0.16, 1, 0.3, 1)`)
  - Snappy Ease: `cubic-bezier(0.4, 0, 0.2, 1)`

#### 3.2. JavaScript Standards
- Write modular, readable ES6+ JavaScript.
- Avoid polluting the global window object. Encapsulate subsystems within a scoped namespace or self-executing lifecycle module.
- Always use feature detection:
  ```javascript
  const AudioContext = window.AudioContext || window.webkitAudioContext;
  if (AudioContext) {
    // initialize synthesizer safely
  }
  ```
- Use `requestAnimationFrame` for high-frequency coordinate tracking (custom cursor, 3D card tilt) to prevent micro-stutter.

---

### 4. Error Handling & Resilience Matrix

```
+---------------------------+-----------------------------------+-----------------------------------+
| Event / Failure Mode      | Vulnerability                     | Implemented Fallback / Recovery   |
+---------------------------+-----------------------------------+-----------------------------------+
| AudioContext Blocked      | Browser security policy blocks    | Catch exception; wait for first   |
| by Autoplay Policy        | programmatic audio synthesis      | user click on page to resume.     |
+---------------------------+-----------------------------------+-----------------------------------+
| MP3 Media Load Failure    | Corrupt file or network error     | Fallback gracefully to procedural |
|                           |                                   | Web Audio synthesizer; keep UI ok.|
+---------------------------+-----------------------------------+-----------------------------------+
| User Prefers Reduced      | Vestibular discomfort from        | Instantly skip 4-stage intro to   |
| Motion                    | camera shake or rapid flashes     | final stage; disable lerp cursor. |
+---------------------------+-----------------------------------+-----------------------------------+
| Mobile Touch Device       | Custom cursor lags or overlaps    | Automatically hide custom cursor  |
|                           | system touch points               | via `@media (hover: none)`.       |
+---------------------------+-----------------------------------+-----------------------------------+
```

---

### 5. Review & Acceptance Checklist for Future Changes
Before submitting or finalizing any code modification:
- [ ] Does the page open instantly in standard Chromium, Firefox, and Safari?
- [ ] Does the 4-stage intro run smoothly without missing frames or audio glitches?
- [ ] Does scrolling feel completely natural and unhindered on both mouse wheel and trackpad?
- [ ] Are all 11 assets loading from `./assets/` with 0 console 404 errors?
- [ ] Is there zero console error or uncaught exception during the entire user journey?
- [ ] Are right-side slide dots strictly absent?
