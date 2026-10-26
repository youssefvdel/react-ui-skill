# Topography
**Registry**: `Topography-TS-TW` · **Deps**: none · **Files**: `Topography/Topography.tsx`
**What it does** — Draws a 3D landscape in glowing contour lines that drifts under a tilted camera, rises where the pointer rests and sends a ring across the terrain on click. Optional plus or dot markers sit on the surface.
**Props**
- `color` (CSS colour, `#4f7cff`) — line colour.
- `lineCount` / `lineWidth` (number, `22` / `1.2`) — contour density and stroke.
- `elevation` / `scale` (number, `1` / `1`) — terrain height and feature size.
- `tilt` (number, `32`) — camera pitch in degrees.
- `speed` / `direction` (`forward` | `backward` | `left` | `right`, `0.25` / `forward`) — drift.
- `glow` / `depthOfField` / `fog` (number, `0.6` / `0.4` / `0.35`) — atmosphere.
- `mouseInteraction` / `hoverEffect` (`lift` | `trace` | `light`, `true` / `lift`).
- `clickEffect` (`pulse` | `peak` | `none`, `pulse`) — what a click does to the field.
**Motion** — A WebGL2 grid terrain with contour lines shaded in the fragment shader: noise drifts with time, the pointer sculpts a height texture, clicks add pulse rings, and an optional intro raises the land. Camera leans with the pointer. Pauses offscreen and when the tab is hidden; reduced motion skips intro, parallax and glitch but keeps the drift.
**Cost** — No dependencies, but ~58 KB source / ~15 KB gzip of inline GLSL — the heaviest file in the batch. Four bloom levels, float targets where available, up to 200k cells per rebuild, DPR capped at 2. A full-screen WebGL loop that will dominate a mid-range phone; server render is an empty canvas.
**Fit for ARKRETE** — no fit. A glowing abstract terrain has no job next to room photography, and its default blue is a second accent.
**Verdict** — skip — the most expensive thing here and the furthest from the brand.
