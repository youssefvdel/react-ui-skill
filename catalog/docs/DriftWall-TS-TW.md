# DriftWall

**Registry**: `DriftWall-TS-TW` · **Deps**: none · **Files**: `DriftWall/DriftWall.tsx`

**What it does** — Builds a tilted perspective wall of image tiles in vertical columns that drift past at slightly different speeds, alternating direction column by column. Hovering a tile lifts and brightens it; the whole plane tilts a little with the pointer.

**Props**
- `items` (DriftWallItem[], 15 picsum defaults) — `{ image, title?, href? }` tiles.
- `columns` (number, 5) — number of drifting columns.
- `speed` (number, 42) — drift in px/s per column.
- `direction` ('up' | 'down', 'up') — base travel direction.
- `variance` (number, 0.45) — spread of column speeds.
- `tilt` (degrees, 16) — forward lean of the wall.
- `depth` (px, 120) — distance the plane is pushed back.
- `pauseOnHover` (boolean, false) — stop the wall while the pointer is on it.

**Motion** — A rAF loop translates each column track and eases velocity when a column is hovered or the wall is paused; pointer position damps into a small extra tilt; hover lifts one tile. All DOM and CSS 3D transforms, no library.

**Cost** — no dependencies, 13 KB TSX (~4.1 KB gzipped source). Five columns duplicated 2–4 times to cover 1.6× the container height — roughly 30–60 `<img>` tiles, all requested on mount. Reduced motion stops drift and parallax, leaving a still perspective grid. Client-only for measurement.

**Fit for ARKRETE** — projects, a full-bleed band under the room stack, at `speed` 10 rather than 42, `dim` 0.25, `grayscale` off, `pauseOnHover` true, and a flat two-row grid when motion is reduced. It would read as breadth after the large rooms, not before them.

**Verdict** — adapt — cheap and thematically right, but only at a quarter of its shipped speed and without the tilt.
