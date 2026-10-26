# ElectricLogo

**Registry**: `ElectricLogo-TS-TW` · **Deps**: `ogl@^1.0.11` · **Files**: `ElectricLogo/ElectricLogo.tsx`

**What it does** — Rasterises a logo image into a distance field and traces its silhouette with four jittering lightning strands and a glow. Arcs leap off the edges, the current bends toward the cursor, and a click sends a pulse and a burst of sparks.

**Props**
- `src` (string, built-in bolt SVG) — logo to trace; any image with transparency.
- `color` (string, `#ecc7ff`) — strand colour.
- `glowColor` (string, `#ad6dff`) — halo colour.
- `scale` (number, 0.7) — logo size within the container.
- `thickness` (number, 1.5) — strand width.
- `strands` (number, 4) — number of strands, 1–6.
- `bend` (number, 0.6) — how far strands wander from the silhouette.
- `crackle` (number, 1.5) — jaggedness of each strand.

**Motion** — A shader animates the strands continuously; the pointer bends the current, clicks add pulses and sparks, and changing `src` morphs between two rasterised shapes. Uses `ogl` for WebGL rendering, plus a CPU distance transform and three blur passes per logo load. Reduced motion slows time to 20%, zeroes flicker and stops hover and click sparks, but the outline still drifts.

**Cost** — `ogl@^1.0.11` renderer on top of 35 KB of component code (~10.5 KB gzipped source). At load it rasterises the logo at 560 px, runs an exact distance transform and blur, and uploads two textures; then a full-screen quad each frame while visible. Client-only; the container is an empty div with no text fallback and no static logo.

**Fit for ARKRETE** — no fit. Lightning around the ARKRETE mark would fight the brass accent and turn a quiet luxury wordmark into a gaming logo.

**Verdict** — skip — a heavy second accent wrapped around the one asset that must stay still.
