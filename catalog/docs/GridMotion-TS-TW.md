# GridMotion

**Registry**: `GridMotion-TS-TW` · **Deps**: none · **Files**: `GridMotion/GridMotion.tsx`

**What it does** — A tilted wall of image or text tiles in rows that drift sideways in alternating directions and shift with the pointer, with a soft spotlight on the tiles under the cursor. The edges feather into the page.

**Props** — `items` (ReactNode | { src, alt }[], required) — tile content; `rows` (4) — wall rows; `aspectRatio` (1.33) — tile shape; `gap` (16) — space between tiles; `angle` (-12) — wall rotation; `tilt` (0) — rotateX lean; `speed` (24) — px/s drift; `spotlight` (0.6) — cursor light and dim recovery.

**Motion** — DOM, not canvas: each row is a `translate3d` marquee and each tile's brightness is a CSS variable eased toward pointer distance; continuous rAF while visible, plus a 0.9 s intro fade. No GSAP, Framer Motion or three.js. Reduced motion stops drift and parallax but still runs rAF and repaints the static wall.

**Cost** — 384 lines, 4.7 KB gzip, no deps, but the heaviest DOM in the batch: rows × tiles-per-row × copies can reach several hundred nodes with a style write per lit tile, and images have no lazy loading. SSR-safe wrapper, client-only motion.

**Fit for ARKRETE** — no fit. Projects already has a scroll stack of rooms; a second drifting wall would compete with it and out-shout the photographs.

**Verdict** — skip — a marquee wall is decoration when the project stack already does the job with real rooms.
