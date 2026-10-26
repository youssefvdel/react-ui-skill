# Particles
**Registry**: `Particles-TS-TW` · **Deps**: none · **Files**: `Particles/Particles.tsx`

**What it does** — Fills a box with a slow 3D cloud of glowing dots that drift and twinkle in a dark space, optionally strung together with faint constellation lines. The pointer parallaxes, repels or attracts the field, and a click sends a shockwave ring through it.

**Props**
- `particleCount` (number, 200) — dots drawn, capped at 20 000.
- `particleSpread` / `cameraDistance` (10 / 20) — cloud size and how far the camera sits back.
- `particleColors` (string[], `['#ffffff']`) — per-dot tints, picked from the list.
- `particleBaseSize` / `sizeRandomness` (100 / 1) — dot size and how uneven it is.
- `shape` ('circle' | 'square' | 'ring' | 'sparkle', 'circle') — the dot glyph.
- `glow` / `twinkle` / `depthOfField` (0.5 / 0.3 / 0) — halo, shimmer, and blur by distance.
- `connections` / `connectionDistance` (false / 110) — draw constellation lines between near dots.
- `hoverEffect` / `hoverRadius` ('parallax' | 'repel' | 'attract' / 140) — how the pointer disturbs the field.

**Motion** — WebGL2 instanced quads. Each frame the CPU advances the rotation, drift and pointer state and projects the first 900 dots for the connection pass, while the vertex shader places and sizes every instance from the same uniforms and the fragment shader draws the glyph with a halo; rotation, twinkle, drift, intro reveal and click bursts are time- or pointer-driven. Sleeps off-screen and on hidden tabs, freezes under reduced motion.

**Cost** — 34 KB source, ~4 KB gzip, no deps. Two GLSL programs, up to 20 000 instances, an optional bucketed proximity pass emitting at most 9 000 line segments, dpr capped at 2. Client-only: WebGL2 or nothing. The 200-dot default is cheap; the ceiling is not.

**Fit for ARKRETE** — no fit. A starfield with constellation lines is the visual language of software, not of rooms; there is no section where it would be more than atmosphere.

**Verdict** — skip — generic tech ambience, and the site's atmosphere comes from photographs.
