# DomeGallery

**Registry**: `DomeGallery-TS-TW` · **Deps**: `@use-gesture/react@^10.2.27` · **Files**: `DomeGallery/DomeGallery.tsx`

**What it does** — Projects up to 175 image tiles onto the inside of a sphere, five staggered rows around 35 columns, with a dark blurred rim and grayscale photos. Dragging spins the dome horizontally with inertia; clicking a tile lifts it into a centred enlarged frame over a blurred backdrop.

**Props**
- `images` (ImageItem[], seven stock defaults) — photos, cycled to fill every tile.
- `segments` (number, 35) — columns around the dome; rows stay at five.
- `fit` (number, 0.5) — dome radius as a fraction of the viewport basis.
- `maxVerticalRotationDeg` (number, 5) — how far a drag can tip the dome up or down.
- `dragSensitivity` (number, 20) — drag pixels per degree of rotation.
- `grayscale` (boolean, true) — filters every photo to grey.
- `openedImageWidth` (string, `400px`) — width of the clicked frame.
- `openedImageHeight` (string, `400px`) — height of the clicked frame.

**Motion** — Drag rotates the sphere and releases into a rAF inertia decay; opening a tile animates it from its dome position to the centre over 300 ms. Nothing moves on hover. There is no `prefers-reduced-motion` branch at all, so reduced-motion users still get the full spin.

**Cost** — `@use-gesture/react` plus its core package, 33 KB of TSX (~8 KB gzipped source) and a runtime `<style>` block. 175 absolutely positioned image tiles under CSS 3D transforms: heavy paint on mobile, and every photo is a separate request. DOM measurement and pointer handling make it client-only; prerender leaves an empty stage.

**Fit for ARKRETE** — no fit. Projects already carries the rooms as a scroll stack; a sphere crops the architecture, greys it, and hides the work behind a drag nobody will discover.

**Verdict** — skip — the photography is the argument, and this makes it smaller, darker and harder to reach.
