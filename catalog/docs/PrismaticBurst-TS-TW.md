# PrismaticBurst
**Registry**: `PrismaticBurst-TS-TW` · **Deps**: none · **Files**: `PrismaticBurst/PrismaticBurst.tsx`
**What it does** — Fires a fan of straight light rays out of the centre, coloured along a gradient and bloomed through four blur levels so it reads as a prismatic starburst. It leans toward the pointer and sends a ring of light outward on click.
**Props** — `colors` (string[], built-in violet set) — gradient stops across the ray fan; `intensity` (number, 2) — ray brightness; `speed` (number, 0.5) — rotation rate; `animationType` ('rotate' | 'rotate3d' | 'hover', 'rotate3d'); `rayCount` (number, 0) — 0 lets the shader pick density; `rayWidth` (number, 1) — 0.2–2.5; `glow` (number, 0) — extra bloom; `clickBurst` (boolean, true) — ring pulse on pointerdown.
**Motion** — Constant ray rotation plus a damped lean toward the cursor and a click-driven pulse that expands and fades; a four-level bloom chain runs every frame. Reduced motion stops the rotation, the lean and the burst. WebGL2, no three.js.
**Cost** — No npm dependencies, about 9 KB gzip of source. The scene renders to an offscreen target at 70 % resolution (`quality: 'high'`, or `resolution`), followed by four downsample/blur/upsample passes at DPR ≤ 2, with an adaptive governor that lowers scale when frames run long. Client-only; without WebGL2 the box stays empty.
**Fit for ARKRETE** — No fit. A starburst is a second accent with no job on any of the five pages, and click-to-burst is a demo gesture rather than an inquiry.
**Verdict** — skip — four-pass bloom for a decoration this brand cannot use.
