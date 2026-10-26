# Shredder

**Registry**: `Shredder-TS-TW` · **Deps**: react-dom@^19.0.0 · **Files**: `Shredder/Shredder.tsx`

**What it does** — A vertical list with a slit at the bottom: drag a row into it and the row is cut into curling paper strips that fall away while the remaining rows close up. Rows can also be reordered by dragging, and the whole rig can feed itself.

**Props** — `items` / `renderItem` — data and row renderer; `onShred` / `onReorder` — callbacks; `width` (340) / `height` (460) — rig size; `feedSpeed` (180) — px/s through the slit; `stripWidth` (10) — cut width; `curl` (1) — strip curl; `autoFeed` (true) — swallow a row dropped on the slit; `autoAnimate` (false) — demo loop that shreds rows on a timer.

**Motion** — Custom pointer physics drag and tilt a row; on drop the row is snapshotted through an SVG `foreignObject` into a canvas, sliced into strips, and each strip falls with spring, curl and flutter. No GSAP or Motion; the physics are hand-rolled.

**Cost** — 1224 lines, 10.1 KB gzip; `react-dom` only, for `flushSync`. Each shred rasterises the row — fonts and images included, images pre-fetched as data URLs — and animates dozens of canvas strips at DPR 2. The heaviest CPU item in the batch, and snapshot fidelity varies by browser. Client-only.

**Fit for ARKRETE** — no fit. A paper shredder is a joke component; no page should make deleting a room look like office equipment.

**Verdict** — skip — 1,200 lines and a DOM rasteriser for a gag.
