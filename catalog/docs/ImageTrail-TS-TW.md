# ImageTrail
**Registry**: `ImageTrail-TS-TW` · **Deps**: gsap@^3.13.0 · **Files**: ImageTrail/ImageTrail.tsx
**What it does** — Every time the pointer travels `threshold` pixels inside the container, the next image in the list pops in at the cursor, turns toward the direction of travel and fades out a moment later, leaving a short trail of photographs. With `stack` it keeps the last few on screen instead of retiring each one immediately.
**Props** — `items` (string[], empty) — image URLs, one absolutely positioned div each; `size` (number, 190) — card width; `aspectRatio` (number, 1.1); `threshold` (number, 80) — px of travel between spawns; `lifetime` (number, 0.4) — seconds before exit; `exitScale` (number, 0.2); `rotation` (number, 0) and `alignToMotion` (boolean, false) — spin, or align to the pointer's heading; `stack` (number, 0) — how many stay.
**Motion** — GSAP timelines per image (scale, rotation, x/y, opacity) plus one rAF lerp for the spawn point; nothing runs until the pointer moves. `prefers-reduced-motion` stops spawning entirely, so the container stays empty — no static version at all.
**Cost** — `gsap@^3.13` (~25 KB gzip) plus 2.6 KB of component; DOM only, one div per item with a CSS background image, so every image may be decoded. Prerender safe but invisible until script runs, and there is no touch equivalent — on a phone it is dead weight.
**Fit for ARKRETE** — no fit — a cursor toy, and the home page already has a scroll reel of six rooms; on mobile there is no cursor.
**Verdict** — skip — decoration with no job that still charges a GSAP dependency.
