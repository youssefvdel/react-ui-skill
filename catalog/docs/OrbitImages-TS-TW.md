# OrbitImages
**Registry**: `OrbitImages-TS-TW` · **Deps**: none · **Files**: `OrbitImages/OrbitImages.tsx`

**What it does** — Spaces images at even intervals along an SVG path — ellipse by default, also circle, square, rectangle, triangle, star, heart, infinity, wave or a path you supply — and carries them around it forever, enlarging the ones at the front and dimming those behind. Drag to spin it with inertia, click an image to bring it to the front, optionally show the path or put content in the middle.

**Props**
- `images` (string[] | {src, alt}[], []) — the orbit's payload; strings get generated alt text.
- `shape` (ellipse | circle | square | star | heart | infinity | wave | custom, 'ellipse') — the track.
- `radiusX` / `radiusY` (700 / 170) — track size in the component's own units, scaled to fit.
- `duration` (seconds, 40) — one lap.
- `itemSize` (px, 64) — image box before depth scaling.
- `depth` (0–1, 0.5) — front/back size and opacity difference.
- `fill` (boolean, true) — spread items evenly around the whole path vs. park them at the front.
- `draggable` / `clickToFront` / `onItemClick` — drag with glide, click to seek an item to the front.

**Motion** — one rAF advances a lap counter, samples a 720-point lookup table of the path, and writes `translate3d`, `scale`, `opacity` and `z-index` per item; hover eases the speed down, dragging adds a manual offset with inertia, and the intro spreads items out from the front over 1.3 s. SVG plus DOM transforms, no animation library.

**Cost** — 33 KB source, ~4.5 KB gzip, no deps. Builds the LUT with `getTotalLength`/`getPointAtLength` on resize, reads layout rects while dragging, then transforms N images per frame — the images are the real weight. Client-only in practice: before hydration every image sits unsized at the top-left, so reserve an aspect ratio or the box collapses.

**Fit for ARKRETE** — no fit. Home already moves six rooms on a scroll-driven reel and projects already stacks rooms; a third device for "rooms in motion" repeats the same idea with a weaker argument, and dragging photographs is a gesture no client asked for.

**Verdict** — skip — a well-built toy that duplicates two sections we already have.
