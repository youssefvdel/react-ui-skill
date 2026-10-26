# AcidSquares
**Registry**: `AcidSquares-TS-TW` · **Deps**: none · **Files**: `AcidSquares/AcidSquares.tsx`
**What it does** — Fills the frame with a perspective ground of glossy rounded squares, each tile bulged by a shared height field so the plane rolls in slow waves under two drifting coloured lights. Periodic pulses travel out from the centre, and pointer or click drops ripples into the same field.
**Props**
- `color` / `accentColor` / `secondaryColor` ('#120f17' / '#ff4fb8' / '#3b6bff') — ground, light A, light B.
- `tileSize` / `gap` / `roundness` / `bulge` (1 / 0.12 / 0.25 / 0.3) — tile grid and shape.
- `waves` / `waveScale` / `speed` (1 / 1 / 0.6) — height-field motion.
- `pulse` / `pulseSpeed` / `pulseSpacing` / `pulseOrigin` (1 / 0.45 / 1 / 'center') — travelling rings.
- `lighting` ('split' | 'backlit' | 'overhead', 'split') — two-light rig.
- `tilt` / `zoom` / `depth` (0.7 / 1 / 10) — camera pitch, distance, draw distance.
- `detail` ('low' | 'medium' | 'high', 'medium') — 150 / 210 / 280 mesh subdivisions.
- `hoverEffect` ('press' | 'lift' | 'none', 'press') and `pulseOnClick` (true) — pointer coupling.
**Motion** — A CPU camera with spring-damped yaw and pitch feeds a vertex-displaced mesh (210 × 210 quads, ~88k triangles at default detail) and a fragment shader for gloss, grain and two orbiting lights. Time drives the swell and light orbit; the pointer adds a hover dent and the camera drifts a few degrees. WebGL2 only, no library. Reduced motion renders one static frame and stops the loop, which also parks whenever nothing is settling.
**Cost** — 10 KB gzip, no dependencies. ~88k triangles submitted every frame plus per-pixel lighting, DPR clamped to 2 and the longest side to 2400 px. Client-only: prerenders an empty div and never draws until the effect runs.
**Fit for ARKRETE** — no fit. An acid-pink and electric-blue nightclub floor, two accents past brass, competing with the rooms that are supposed to carry the page.
**Verdict** — skip — a strong second palette and a surface with no job behind the photography.
