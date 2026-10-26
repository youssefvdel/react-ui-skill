# DotField

**Registry**: `DotField-TS-TW` · **Deps**: none · **Files**: `DotField/DotField.tsx`

**What it does** — Draws a canvas field of small dots on a grid, hex, spiral or scatter lattice, coloured by a two-stop gradient. A circular lens tracks the cursor and magnifies, pinches or twists the dots inside it, with a soft glow and an optional slow wave.

**Props**
- `pattern` ('grid' | 'hex' | 'spiral' | 'scatter', 'grid') — lattice layout.
- `dotRadius` (number, 1.5) — dot size in px.
- `dotSpacing` (number, 14) — gap between dots.
- `gradientFrom` (string, `#5227FF`) — first stop of the dot colour ramp.
- `gradientTo` (string, `#FF9FFC`) — second stop of the ramp.
- `cursorRadius` (number, 240) — reach of the lens.
- `bulgeStrength` (number, 0.6) — magnify (+) or pinch (−) inside the lens.
- `twist` (degrees, 0) — swirl applied through the lens.

**Motion** — The lens is pointer-driven and re-renders every frame while it moves, settling when the cursor stops; wave and sparkle are time-driven, and holding the pointer down zooms the field. Everything is a WebGL2 vertex/fragment shader over instanced quads, with no animation library.

**Cost** — no dependencies, 24 KB TSX (~7.7 KB gzipped source). Up to 120k instanced quads under a 9 MP pixel budget, DPR capped at 2; rAF runs only while something moves and the page is visible. Reduced motion freezes time and skips the intro, leaving static dots with the lens still available. Client-only; a browser without WebGL2 shows an empty box.

**Fit for ARKRETE** — no fit. It is ground texture, not content; a static CSS or SVG dot pattern costs nothing and stays quieter behind the wordmark.

**Verdict** — skip — 8 KB of WebGL for a background no section is asking for.
