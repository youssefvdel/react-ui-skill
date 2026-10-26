# Threads
**Registry**: `Threads-TS-TW` · **Deps**: none · **Files**: `Threads/Threads.tsx`
**What it does** — Fills its box with a WebGL2 canvas of fine parallel lines — 90 by default — that flow, fray into separate strands and part around the pointer, lit like silk or contour lines. Colour can shift toward an accent near the cursor.
**Props**
- `lineCount` (number, `90`, clamped 1–400) — how many strands.
- `amplitude` / `distance` (number, `1.7` / `0.4`) — wave height and spacing between lines.
- `thickness` / `softness` (number, `0.6` / `1.3`) — stroke body and edge blur.
- `speed` (number, `0.6`) — drift rate of the noise field.
- `fray` / `parting` (number, `0.5` / `0`) — how far strands separate and how wide the cursor gap.
- `color` / `accentColor` (CSS colour or RGB array, white) — base and cursor tint.
- `enableMouseInteraction` (boolean, `false`) — pointer parting.
- `paused` (boolean, `false`) — freezes time without unmounting.
**Motion** — Continuous time-driven vertex shader (Perlin displacement) with a pointer-eased parting field, rendered in two passes: instanced line strips into an FBO, then a tone-mapped full-screen quad. rAF stops offscreen and on hidden tabs. Reduced motion freezes time, leaving one static frame.
**Cost** — No dependencies, ~20 KB source / 5.7 KB gzip with shaders inline. One canvas, one offscreen pass, 90 instanced strips at up to 2× DPR — continuous GPU load while visible, and it will show on phones. Server render is an empty div.
**Fit for ARKRETE** — no fit. Every section already carries a photograph; an abstract line field behind it is decoration with a real GPU bill.
**Verdict** — skip — good-looking and unemployed, and a permanent WebGL loop is the wrong cost for this page weight.
