# DotGrid

**Registry**: `DotGrid-TS-TW` · **Deps**: none · **Files**: `DotGrid/DotGrid.tsx`

**What it does** — A canvas lattice of dots that spring out of the cursor's way, stretch into capsules along a fast flick, and ripple outward from a click before easing back. Dots near the pointer lighten toward the active colour.

**Props**
- `dotSize` (number, 5) — resting dot diameter.
- `gap` (number, 18) — spacing between dots.
- `baseColor` (string, `#3a3446`) — colour at rest.
- `activeColor` (string, `#ffffff`) — colour when excited by the cursor.
- `proximity` (number, 140) — cursor radius that disturbs the grid.
- `strength` (number, 1) — push force.
- `bounce` (number, 0.6) — springiness of the return.
- `shockRadius` (number, 320) — reach of the click shockwave.

**Motion** — Pointer proximity pushes dots with spring physics; pointer velocity stretches them along the axis of travel; clicks emit a shockwave; an intro bloom settles the grid. WebGL2 instanced quads, no library.

**Cost** — no dependencies, 23 KB TSX (~6.2 KB gzipped source), one program and one instance buffer. rAF runs while dots are moving and idles cheaply. Reduced motion zeroes swell, stretch and shock and skips the intro, leaving a plain static grid. Client-only.

**Fit for ARKRETE** — no fit. Jelly physics under a luxury interior site reads as a toy, and no page needs a second interactive surface.

**Verdict** — skip — playful cursor physics with no content job and no brass restraint.
