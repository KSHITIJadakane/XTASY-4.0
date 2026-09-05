# Design System & Visual Guidelines
## XTASY 4.0 / Industrial IoT Event Registration Visual Identity

---

### 1. Aesthetic Vision & Mood
The visual architecture of the **XTASY 4.0** landing page is rooted in **Dystopian Brutalism fused with Cyberpunk Neon Minimalist Polish**. It retains the Squid Game aesthetic to create psychological tension through:
- **Absolute Contrast**: Pitch black abyss backgrounds (`#000000`) pierced by high-voltage neon pink (`#FF007F`) and icy cyber cyan (`#00F0FF`).
- **Geometric Hierarchy**: Sacred geometric shapes (○ Worker, △ Soldier, □ Manager) and the faceted polygon geometry of the Frontman's mask.
- **Atmospheric Depth**: Film-grain textures, soft neon light blooms, and glassmorphic frosted surfaces (`backdrop-filter: blur()`).

---

### 2. Color Palette & Token System

```
+---------------------------------------------------------------------------------------+
|                                    COLOR SWATCHES                                     |
|                                                                                       |
|   [ #FF007F ]        [ #00F0FF ]        [ #000000 ]        [ #0A0A0C ]                |
|   Neon Pink          Cyber Cyan         Pure Black         Surface Dark               |
|   (Primary CTA/Glow) (Numerals/Accents) (Background Void)  (Cards/Modals)             |
|                                                                                       |
|   [ #E41A4A ]        [ #037A4B ]        [ #FFFFFF ]        [ rgba(255,255,255,0.7) ]  |
|   Magenta Edge       Tracksuit Green    Primary Text       Secondary Text             |
+---------------------------------------------------------------------------------------+
```

#### CSS Variable Mapping (`:root`)
```css
:root {
  /* Brand Chromatic Tokens */
  --pink-neon: #FF007F;
  --pink-glow: rgba(255, 0, 127, 0.45);
  --pink-deep: #E41A4A;
  
  --cyan-neon: #00F0FF;
  --cyan-glow: rgba(0, 240, 255, 0.45);
  --cyan-dim: #00A3B0;

  --contestant-green: #037A4B;
  --contestant-green-light: #249C6B;

  /* Surfaces & Neutral Foundations */
  --bg-black: #000000;
  --bg-surface: #0A0A0C;
  --bg-card: rgba(16, 16, 20, 0.75);
  --glass-border: rgba(255, 255, 255, 0.08);

  /* Typography Colors */
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255, 255, 255, 0.70);
  --text-muted: rgba(255, 255, 255, 0.38);

  /* Motion Curves */
  --ease-cinema: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

### 3. Typography System

The typography creates a contrast between massive, commanding display titles and crisp, utilitarian technical information.

| Role | Font Family | Weights | Usage & Characteristics |
| :--- | :--- | :---: | :--- |
| **Hero Title** | `Antonio`, `sans-serif` | 700 | Condensed, razor-sharp vertical proportion for oversized hero titles ("SQUID GAME"). |
| **Section Headings** | `Space Grotesk`, `sans-serif` | 700, 800 | Uppercase, wide letter-spacing (`0.12em`), geometric modernism ("RULES OF SURVIVAL", "INSIDE THE GAME"). |
| **Technical / Numbers**| `Orbitron` / `Space Mono` | 600, 700 | Cyan glowing numerals (`1`, `2`, `3`, `4`), badge markers, system coordinates. |
| **Body & UI Copy** | `Inter`, `sans-serif` | 300, 400, 500 | Clean, neutral readability for descriptions, modals, navigation items, and button labels. |

#### Typographic Scale Hierarchy
- **Hero Display H1**: `clamp(4rem, 12vw, 10.5rem)` | Letter-spacing: `0.04em` | Line-height: `0.88`
- **Section Heading H2**: `clamp(2.5rem, 5vw, 4.5rem)` | Letter-spacing: `0.08em` | Line-height: `1.05`
- **Sub-heading H3**: `clamp(1.25rem, 2vw, 1.85rem)` | Letter-spacing: `0.05em` | Line-height: `1.2`
- **Body Text**: `1rem (16px)` | Letter-spacing: `0.01em` | Line-height: `1.65`
- **Monospace Badge**: `0.85rem (13.6px)` | Letter-spacing: `0.18em` | Uppercase

---

### 4. Sacred Geometry & Iconic Motifs

1. **The Core Symbols (○ △ □)**:
   - Used as subtle glowing wireframe watermarks in the background of Section 3.
   - SVG vector rendered with `stroke: var(--pink-neon)` or `stroke: var(--cyan-neon)` with `stroke-width: 1.5px` and low opacity (0.15–0.3).
2. **The Frontman Polygonal Mask**:
   - Integrated directly into typography in Section 5 (**"RE [Mask] DY TO PLAY?"**), visually replacing the character "A" with the faceted black mask.
   - Framed with subtle breathing back-glow pulse (`filter: drop-shadow(0 0 20px rgba(255, 0, 127, 0.35))`).
3. **Scanlines & Atmospheric Grain**:
   - Micro-scanline texture overlay:
     ```css
     .scanlines {
       background: repeating-linear-gradient(
         0deg,
         rgba(0, 0, 0, 0.15),
         rgba(0, 0, 0, 0.15) 1px,
         transparent 1px,
         transparent 2px
       );
       pointer-events: none;
     }
     ```

---

### 5. Motion Language & Choreography

All motion in this design is deliberate, cinematic, and heavy. It avoids trivial bounciness in favor of cold, surgical suspense:

```
[0.0s] Blackout & Silence
  ↓
[0.6s] Visor Ignition Spark (Red Line Flares)
  ↓
[1.4s] Torso & Seam Neon Flood (Deep Synth Hum)
  ↓
[2.2s] Full High-Voltage Floodlight (Bass Drop + Silhouette Reveal)
  ↓
[2.8s] Typographic Drop ("SQUID GAME" Glides Down + Glitch Aberration)
  ↓
[3.5s] Interface Active (Smooth Document Scrolling Unlocked)
```

#### Transition Standards
- **Hover Transitions**: `all 0.28s var(--ease-cinema)`
- **Gliding Scroll Reveal**: `transform 0.85s var(--ease-cinema), opacity 0.85s ease`
- **3D Tilt Persistence**: `transform 0.12s ease-out` for snappy cursor responsiveness
- **Modal Backdrop Reveal**: `opacity 0.35s ease, backdrop-filter 0.35s ease`

---

### 6. Component Style Blueprints

#### 6.1. Primary Magnetic Pill Button
- **Shape**: Fully rounded capsule (`border-radius: 9999px`).
- **Fill**: Solid Neon Pink (`var(--pink-neon)`) or pure black with neon pink border.
- **Hover State**: Glowing neon halo (`box-shadow: 0 0 35px var(--pink-glow)`), text scale `1.04`, subtle cursor magnetic pull.

#### 6.2. 3D Invitation Kraft Card
- **Materiality**: Rich textured brown Kraft cardstock with debossed circle, triangle, square symbols.
- **Lighting**: Dynamic specular highlight gradient moving across the card surface in inverse sync with mouse rotation coordinates.

#### 6.3. Rules of Survival 4-Column Strip
- **Layout**: 4 vertical columns with hairline dividers (`border-right: 1px solid rgba(255, 255, 255, 0.08)`).
- **Numerals**: Glowing cyber cyan (`#00F0FF`) with drop shadow bloom (`drop-shadow(0 0 12px var(--cyan-glow))`).
- **Interaction**: Subtle vertical translation (`translateY(-8px)`) and brightening on column hover.
