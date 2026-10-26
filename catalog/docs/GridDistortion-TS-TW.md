# GridDistortion

**Registry**: `GridDistortion-TS-TW` · **Deps**: none · **Files**: `GridDistortion/GridDistortion.tsx`

**What it does** — Covers a panel with one image and breaks it into a grid of blocks around the pointer, which spring back into place; drag, push or swirl change how the blocks move. Optional chromatic split separates the channels while the grid is displaced.

**Props** — `imageSrc` (string, required) — the image; `grid` (15) — cells across; `radius` (0.18) — brush reach as a fraction of width; `strength` (0.15) — displacement gain; `relaxation` (0.96) — how fast cells settle; `mode` ('drag' | 'push' | 'swirl', 'drag') — block reaction; `softness` (0) — blocky versus smooth field; `chroma` (0) — RGB split.

**Motion** — Pointer-driven CPU spring simulation over grid² cells, uploaded as an RG32F texture each frame, sampled by a WebGL2 shader. No GSAP, Framer Motion or three.js. Reduced motion kills idle drift, ripples and the intro, but pointer drags still deform the grid — a guard is needed.

**Cost** — 486 lines, 5.1 KB gzip, no deps; one image texture, loaded with `crossOrigin="anonymous"` so remote images must send CORS headers, plus a grid texture upload on every active frame. DPR ≤ 2, opaque canvas. No WebGL2 means a blank panel. Client-only.

**Fit for ARKRETE** — no fit. It turns room photography — the argument — into a cursor toy, and its default idle wander keeps moving with no input.

**Verdict** — skip — the photography is strong enough without being made to wobble.
