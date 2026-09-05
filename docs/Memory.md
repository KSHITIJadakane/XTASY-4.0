# Project Context Memory & Decision Records
## Living Context Bank for AI Pair-Programmers & Engineers

---

### 1. Project Snapshot & Core Mission
- **Project Name**: Squid Game / Quest Room Cinematic Landing Page
- **Repository Location**: `c:\Users\rajur\OneDrive\Desktop\xtasy`
- **Primary Runtime File**: [`squid-game-landing.html`](file:///c:/Users/rajur/OneDrive/Desktop/xtasy/squid-game-landing.html)
- **Primary Objective**: An ultra-high-fidelity, 100% video-faithful cinematic promotional website inspired by the Squid Game concept motion video (`Squid Game landing page — design concept in motion...mp4`).
- **Core USP**: The **4-Stage Electrical Power-On Intro Sequence**, with synchronized procedural Web Audio sound design, gliding typography, and smooth continuous document scrolling.

---

### 2. Active File Inventory & Asset Register

```
c:\Users\rajur\OneDrive\Desktop\xtasy/
├── squid-game-landing.html          # Monolithic production file (HTML5 + Inlined CSS3 + ES6)
├── assets/                          # Local production assets (11 items, 0 remote dependencies)
│   ├── hero_intro_0.png             # Stage 0: Guard silhouette in pure darkness
│   ├── hero_intro_1.png             # Stage 1: Red visor and seam ignition
│   ├── hero_intro_2.png             # Stage 2: Neon pink suit energization
│   ├── hero_intro_3.png             # Stage 3: Full neon burst + player silhouettes
│   ├── invite_hand_hd.jpg           # Section 2: Leather gloved reaching hand
│   ├── card_cutout.png              # Section 2: 3D interactive Kraft card
│   ├── pink_corridor_hd.jpg         # Section 4: Pink guard corridor gallery
│   ├── neon_hall_hd.jpg             # Section 4: Cyan/magenta tunnel gallery
│   ├── gameplay_hd.jpg              # Section 4: Contestant game arena gallery
│   ├── frontman_mask_hd.jpg         # Section 5: Frontman faceted black mask
│   └── squid_theme.mp3              # Ambient suspense theme track
├── analyze_video.py                 # OpenCV Python utility used for frame extraction
├── PRD.md                           # Product Requirements Document
├── Architecture.md                  # System architecture, lifecycle, and subsystems
├── Rules.md                         # Strict boundaries and AI coding guidelines
├── Phases.md                        # Delivery milestones, status, and roadmap
├── Design.md                        # Visual tokens, typography scale, motion curves
└── Memory.md                        # This living context memory file
```

---

### 3. Architectural Decision Records (ADRs)

#### ADR-00: [2026-09-05] Major Pivot to XTASY 4.0 Departmental Event Registration
- **Context**: The project was originally built as a generic "Squid Game Cinematic Landing Page / Quest Room" promotional site. The user clarified that the overarching goal is to build an event registration website for their department (Industrial IoT) for a departmental event called **XTASY 4.0**.
- **Decision**: The project documentation and UI are being transitioned from a fictional "Quest Room" to the actual XTASY 4.0 registration hub. The Squid Game theme will be retained as the aesthetic layer. The site will feature and facilitate registration for 4 core events: **Automystica**, **Hack the Hardware**, **Triguna**, and **VisionExpo**.
- **Result**: `PRD.md`, `Architecture.md`, `Phases.md`, and `Design.md` were updated to reflect this new strategic direction. The UI components will be subsequently re-aligned.

#### ADR-01: 4-Stage Multi-Frame Guard Illumination vs. Simple CSS Fade
- **Context**: The original Stitch prototype tried to fade the guard in using a basic CSS `opacity: 0` to `1`.
- **Decision**: Extracted 4 distinct illumination milestones directly from the concept video (`hero_intro_0.png` through `3`).
- **Why**: In the video, the guard doesn't just fade in—electrical power travels through the visor seam (Stage 1), energizes the pink suit fabric (Stage 2), and then hits full floodlight power with the players in the foreground (Stage 3). Using 4 stacked images with timed cross-fades reproduces the exact cinematic realism.

#### ADR-02: Continuous Document Scrolling vs. Slide-Lock / Wheel-Hijacking
- **Context**: An earlier build implemented full-screen 100vh section snapping with side navigation dots, resembling a presentation deck.
- **Decision**: **Permanently eliminated slide-lock and deleted right-side navigation dots**. Converted the site to a natural continuous scrolling document (`overflow-y: auto; scroll-behavior: smooth;`) powered by `IntersectionObserver` gliding reveals.
- **Why**: The user explicitly instructed: *"make it site not ppt... remove the right side dots... copy those gliding ditto text and fades in and all"*. Slide-locking traps user scrolling, creates trackpad friction, and feels like a pitch deck rather than a premier interactive website.

#### ADR-03: Zero-Build Monolithic Runtime vs. Modern Framework Bundler
- **Context**: Deciding whether to migrate the project to Vite / Next.js / Tailwind CLI.
- **Decision**: Retained `squid-game-landing.html` as a self-contained, zero-build monolithic application with inlined vanilla CSS3 and vanilla ES6 JavaScript.
- **Why**: The page loads instantaneously from local disk (`file:///`), can be deployed to any static host with zero compilation steps, has zero dependency vulnerabilities, and avoids npm package rot.

#### ADR-04: Hybrid Dual-Engine Audio Architecture
- **Context**: Need both ambient cinematic scoring and hyper-responsive tactile sound effects without adding megabytes of sound libraries.
- **Decision**:
  1. `HTML5 Audio` element streams `assets/squid_theme.mp3` with looping and smooth gain fading.
  2. `Web Audio API` procedurally synthesizes micro-interactions (electrical power spark, sub-bass boom, card hover chirp, button punch) directly via oscillators and gain envelopes.
- **Why**: Procedural sound generation costs 0 bytes of network transfer, executes with 0ms latency, and will never fail to load due to 404s.

#### ADR-05: 100% Localized Asset Pipeline
- **Context**: The Stitch prototype hot-linked images from temporary Google user content URLs (`lh3.googleusercontent.com`).
- **Decision**: Replaced all remote URLs with local files residing in `./assets/`.
- **Why**: Google user content URLs expire and break without notice. Local storage guarantees 100% offline capability and permanence.

#### ADR-06: Laptop Mockup Frame Border Removal & 2-Second Motion Blur Glide
- **Context**: Video reference showed the website running inside a MacBook laptop mockup. Early frame extractions included the laptop screen bezel (white vertical lines on left and right), creating an unintended boxed frame in the hero.
- **Decision**: Cropped strictly inside the laptop display coordinate space, feathered all 4 boundaries to pure `[0,0,0]`, and created separated layers for:
  1. `hero_start_clean.png` (Starting Frame: Guard alone on pure black, zero borders).
  2. `hero_left_text.png` ("SQ" and quote gliding inward from left).
  3. `hero_right_text.png` ("UID" and "GAME" gliding inward from right).
  4. `hero_players_layer.png` (Hooded contestant silhouettes gliding upward).
  5. `hero_end_clean.png` (Ending Frame: Master 100% crisp lock).
  Set transition duration to exactly 2.0s with `cubic-bezier(0.16, 1, 0.3, 1)` and `filter: blur(14px) -> blur(0px)`.
- **Why**: The user explicitly flagged: *"remove the boader in the original video its made seems like its playing on a laptop so dont make that frame that i have attached the current web too... starting and ending frame is done in 2 seconnds smoothly through gliding"*. This eliminates all borders and delivers a borderless full-bleed edge-to-edge experience.

---

### 4. Critical Invariants & Rules for Future AI Sessions
If you are an AI picking up this project in a new session, you **MUST NEVER**:
1. **Never re-add slide dots or PPT markers on the right side of the screen.**
2. **Never trap or lock scrolling (`overflow: hidden` on body or wheel hijacking).**
3. **Never replace local assets in `./assets/` with external CDN URLs.**
4. **Never install or inject Tailwind CDN, Bootstrap, or React unless explicitly ordered by the user.**
5. **Never re-introduce the laptop mockup bezel borders into the hero section.**

---

### 5. Historical Bugs Resolved (Do Not Re-introduce)

| Bug ID | Symptom in Early Prototype | Root Cause | Permanent Resolution |
| :--- | :--- | :--- | :--- |
| **BUG-01** | "SQUID GAME" title obscured and unreadable in hero | Guard image placed directly over text with improper blend mode (`mix-blend-mode: screen`) | Re-positioned guard layer, flanked text as "SQ" and "ID", feathered bottom edge with radial gradient mask. |
| **BUG-02** | Page silent and sterile | No audio engine implemented | Added dual-engine audio: ambient score toggle + synthesized Web Audio SFX. |
| **BUG-03** | PowerPoint slide-locked feeling | Viewport fixed to 100vh with transform translation | Unlocked standard native scrolling with IntersectionObserver gliding text. |
| **BUG-04** | Remote images failing or slow | Stitch export used temporary Google session URLs | Extracted and generated permanent local HD assets in `./assets/`. |
| **BUG-05** | White vertical lines / borders in hero | Laptop screen bezel from video mockup was included in cropped images | Re-cropped strictly inside display coordinates, feathered edges to pure `#000000`, making hero 100% full-bleed and borderless. |

---

### 6. Quick Start & Verification for Any Future Developer
- **To View the Website**: Double click [`squid-game-landing.html`](file:///c:/Users/rajur/OneDrive/Desktop/xtasy/squid-game-landing.html) or run a local HTTP server:
  ```powershell
  python -m http.server 8000
  ```
  Then visit `http://localhost:8000/squid-game-landing.html`.
- **To Inspect Assets**: View the `./assets/` folder. All 11 visual and audio files must be present.
- **Audio Verification**: Click the "SOUND" equalizer button or "Play Game" button in the navigation bar to unlock the audio context.
