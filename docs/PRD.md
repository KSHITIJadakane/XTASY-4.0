# Project Requirements Document (PRD)
## XTASY 4.0: Industrial IoT Event Registration Website (Squid Game Theme)

---

### 1. Executive Summary
The **XTASY 4.0 Event Registration Website** (formerly conceptualized as a Quest Room landing page) is an immersive, high-fidelity promotional web experience for the Industrial IoT department's technical events. Inspired by the aesthetics of the global phenomenon *Squid Game*, this platform serves as the central registration hub for four major technical events: **Automystica**, **Hack the Hardware**, **Triguna**, and **VisionExpo**. Designed to push the boundaries of creative front-end web development, the project replicates the visual tension, dystopian atmosphere, and motion language of a high-budget cinematic trailer while serving a practical event-management purpose.

The standout **Unique Selling Proposition (USP)** is the **4-stage electrical power-on intro sequence**, featuring sequential illumination of the Pink Soldier, glitch title reveals, synthesized Web Audio sound effects, and atmospheric background scoring, leading into a continuous, natural-scrolling interactive website containing the real-world event details and registration portals.

---

### 2. Objectives & Value Proposition
- **Showcase Aesthetic Excellence**: Provide an ultra-premium, dark-mode visual experience combining deep pure blacks (`#000000`), vibrant neon pinks (`#FF007F`), and piercing cyber cyans (`#00F0FF`).
- **Faithful Motion Engineering**: Recreate the exact motion dynamics from the original 15-second design concept video, including the iconic power-on sequence and letter-gliding transitions.
- **Natural Web Architecture**: Deliver a seamless, continuous-scrolling website rather than a rigid slide-locked PowerPoint presentation, free from intrusive slide-navigation dots.
- **Zero-Dependency Portability**: Run directly in any modern web browser without build tooling (`npm`, `webpack`, `vite`), external CDNs, or network-bound asset dependencies.

---

### 3. Target Audience & Personas
1. **Engineering & Technical Students**: Participants from IIoT and other branches looking to register for the technical events (Automystica, Hack the Hardware, Triguna, VisionExpo).
2. **Interactive Design Enthusiasts & Recruiters**: Reviewers evaluating advanced CSS animation, Web Audio synthesis, micro-interactions, and canvas/DOM compositing.
3. **Faculty & Industry Judges**: Evaluators and guests looking for event details, rules, and schedules.

---

### 4. Feature Specifications

#### 4.1. The 4-Stage Power-On Intro Sequence (Core USP)
- **Stage 0 (Darkness)**: Complete void with guard silhouette faintly visible (`hero_intro_0.png`).
- **Stage 1 (Ignition / Red Lines)**: Subtle visor and seam activation with electrical spark sound (`hero_intro_1.png`).
- **Stage 2 (Suit Energization)**: Neon pink illumination floods the guard's torso and hood (`hero_intro_2.png`).
- **Stage 3 (Full Neon Burst)**: High-voltage floodlight flare illuminates the guard and foreground player silhouettes (`hero_intro_3.png`), triggering typographic reveal.
- **Glitch & Typographic Entry**: "SQUID GAME" letterforms drop and glide in with chromatic aberration and audio pulse.
- **Audio Synchronization**: Synthesized electrical hum and high-voltage power-up audio FX synthesized via Web Audio API, transitioning into the ambient theme track.

#### 4.2. Navigation Subsystem (`<nav>`)
- **Brand Mark**: `XTASY 4.0` logo featuring a glowing neon pink loop on the letter "Q" (or adapted typographic logo).
- **Navigation Links**: "Events", "Schedule", "Rules", "Contact", each with glowing underline hover states.
- **Audio Control**: Dynamic sound toggle with animated 3-bar equalizer visualizing playback state (Ambient Music ON / MUTE).
- **Primary CTA**: High-visibility neon pill button "Register Now" with magnetic hover pull.

#### 4.3. Interactive Sections Catalog
1. **Hero Section (`#hero`)**:
   - Massive stylized typography: "SQ" (left) and "ID" (right) flanking the centered 3D guard composite.
   - Distinctive "GAME" wordmark with neon pink hooked "G" and elongated "E".
   - Atmospheric subtitle: *"Build. Adapt. Survive. XTASY 4.0 is here."*.
   - Subtle mouse-tracking parallax effect for depth.
2. **The Invitation (`#welcome`)**:
   - Top banner: Letter-spaced glowing marquee `WELCOME PLAYERS`.
   - Left Column: Typographic block `HOLD THE CARD`, cyan subheading `Begin the game.`, copy explaining XTASY 4.0, and glowing `Accept` button.
   - Right Column: Black leather-gloved hand holding the iconic Kraft invitation card.
   - Interaction: Dynamic 3D card tilt responding directly to mouse cursor coordinates with realistic specular highlights.
3. **Rules of Survival (`#rules`)**:
   - Header: `RULES OF SURVIVAL` with extended typographical geometry.
   - 4-Column Layout: Minimalist vertical column dividers with cyan neon numerals `1`, `2`, `3`, `4`. Outlining general event guidelines (e.g. Teams, Conduct, Deadlines, Evaluation).
   - Atmospheric Glyphs: Floating wireframe geometric shapes (○, △, □) and Frontman wireframe bust.
   - Gliding Reveal: Staggered upward gliding motion triggered via `IntersectionObserver`.
4. **The Events (`#gallery` -> `#events`)**:
   - Section Header: `THE GAMES (EVENTS)`.
   - Interactive Showcase of the 4 core IIoT Departmental events:
     - **Automystica**: IoT + Automation Challenge (Build, Adapt, Survive)
     - **Hack the Hardware**: Hardware + Robotics Arena Challenge
     - **Triguna**: Agriculture Innovation Pitching Challenge
     - **VisionExpo**: Poster Presentation Competition (Lean Manufacturing & Industrial Excellence)
   - Interaction: Smooth hover effects revealing event details, registration fees, and team formats.
5. **Ready to Play / CTA (`#cta`)**:
   - Typography Integration: Frontman faceted black mask embedded as the letter "A" in the giant wordmark **"RE [Mask] DY"**.
   - Sub-headline: *"TO REGISTER?"* with "Register Now" action button.
   - Registration Trigger: Opens the interactive player onboarding modal.
6. **Footer**:
   - `XTASY 4.0` logo, social links (Telegram, Instagram, YouTube), copyright disclaimer, and geometric glyphs.

#### 4.4. Audio Engine & Sound Design
- **Ambient Soundtrack**: `assets/squid_theme.mp3` playing in a loop with smooth fade-in/fade-out logic.
- **Synthesizer Subsystem (Web Audio API)**:
  - Intro electrical surge and power-on boom.
  - Card hover tactile frequency sweep (800Hz sine chirp).
  - Button click punch (low-frequency square wave drop).
  - Zero external sound library dependencies.

#### 4.5. Event Registration Modal
- Glassmorphic modal overlay (`backdrop-filter: blur(20px)`).
- Input fields: Participant Name(s), Contact Details, Department/Year, and Event Selection (Automystica, Hack the Hardware, Triguna, VisionExpo).
- Audio-tactile validation and submission feedback.

---

### 5. Non-Functional Requirements (NFR)
- **Performance**: 60 FPS fluid rendering on standard desktop and mobile hardware. Animations restricted to GPU-composited properties (`transform`, `opacity`, `filter`).
- **Asset Self-Containment**: 100% of assets stored locally in `./assets/`. No third-party image host dependencies that expire or require active internet.
- **Responsiveness**: Fully fluid from 375px (mobile) to 2560px (ultra-wide monitors).
- **Zero-Build Deployment**: Standalone single HTML file structure that opens instantly via `file:///` protocol or any static web server (GitHub Pages, Vercel, Netlify, Apache, Nginx).
- **Accessibility (a11y)**:
  - Respect `prefers-reduced-motion` media queries by disabling camera shakes and heavy parallax.
  - High color contrast meeting WCAG AA standards for all body and informational copy.
  - Semantic HTML tags (`<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).

---

### 6. Out of Scope / Non-Goals
- Full multi-player real-time online game engine (this is a cinematic marketing & onboarding experience).
- Payment gateway or real-money wagering processing.
- Direct trademark violation: Features original fan-concept artwork and stylistic homage to geometric dystopia.
