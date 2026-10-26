# ShapeBlur

**Registry**: `ShapeBlur-TS-TW` · **Deps**: none · **Files**: `ShapeBlur/ShapeBlur.tsx`

**What it does** — Draws a crisp generated shape — rectangle, circle, polygon, star or a custom SVG path — on a canvas, then puts a camera lens over it: the patch under the pointer goes soft with chromatic fringing while the rest stays sharp.

**Props** — `shape` ('rect') — geometry preset; `src` — SVG path data for a custom mark; `size` (.8) — fraction of the box; `fill` (false) — solid instead of outline; `echoes` (1) — offset copies of the outline; `blur` (16) — maximum lens blur; `lensSize` (.3) — lens radius as a fraction of the box; `focus` (false) — inverts, keeping the lens sharp and blurring the rest.

**Motion** — Pointer position and presence feed a WebGL2 composite: the shape renders to a texture, a downsampled blur pyramid is built, then a lens-weighted mix with a chroma split. `idle` (true) adds a slow drift. No GSAP, Motion or three.js; no pointer means a crisp still.

**Cost** — 802 lines, 7.4 KB gzip, no npm deps but three shader programs, several framebuffer textures and a blur pyramid; one WebGL2 context at DPR ≤ 2. Redraws only while visible and while the pointer or idle drift asks it to. Client-only; without WebGL2 the canvas stays empty and `children` still show.

**Fit for ARKRETE** — no fit. It is a lens for a logo or mark, and ARKRETE's argument is photography, not a generated shape.

**Verdict** — skip — 800 lines of shader for a hover trick with no section to carry.
