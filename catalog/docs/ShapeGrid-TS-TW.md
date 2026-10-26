# ShapeGrid

**Registry**: `ShapeGrid-TS-TW` · **Deps**: none · **Files**: `ShapeGrid/ShapeGrid.tsx`

**What it does** — A canvas grid of small shapes — squares, hexagons, diamonds, dots — drifts diagonally; cells near the cursor light up and leave a short trail, and a click sends a cascade of light across the plane.

**Props** — `shape` ('square') — cell glyph, eight options; `cellSize` (40) — grid pitch in px; `lineColor` ('#2a2734') — resting stroke; `hoverColor` ('#ffffff') — lit stroke; `fillOpacity` (.15) — hover fill; `tiltX` / `tiltY` (0) — perspective lean; `trail` (.6) — how long lit cells fade; `glow` (.35) — bloom around the pointer.

**Motion** — Canvas 2D redraws every frame: a projected grid offset drifts with time, pointer proximity raises per-cell light with spring decay, and clicks seed expanding cascades. Reduced motion stops the drift and twinkle but keeps hover light; rAF pauses off screen.

**Cost** — 856 lines, 7.6 KB gzip, no deps. One full-bleed canvas at DPR ≤ 2, cell count set by area ÷ `cellSize`²; a 1440×900 hero at 40 px is about 800 cells redrawn per frame. Client-only; prerender is an empty canvas.

**Fit for ARKRETE** — no fit. A technical grid under interiors reads as a dashboard, and the hover light duplicates the single accent.

**Verdict** — skip — decoration with no job, and a permanent full-bleed repaint.
