# GradientText

**Registry**: `GradientText-TS-TW` · **Deps**: none · **Files**: `GradientText/GradientText.tsx`

**What it does** — Fills a text span with a gradient that slides, drifts as blobs, or swings as a conic fan, with an optional glow and gradient border. The letters are the animation; nothing moves in space.

**Props** — `variant` ('linear' | 'flow' | 'conic', 'linear') — gradient behaviour; `colors` (string[], violet/pink) — colour stops; `animationSpeed` (8) — seconds per cycle; `angle` (90) — gradient direction in degrees; `scale` (3) — pattern repeat width; `yoyo` (true) — swing back instead of wrapping; `glow` (0, 0–1) — blurred duplicate behind the text; `followPointer` (false) — first blob leans toward the cursor.

**Motion** — A rAF loop rebuilds a CSS gradient string and writes it into a custom property, so the text repaints each frame. No canvas, no GSAP, Framer Motion or three.js; reduced motion pauses the clock and the loop settles.

**Cost** — 237 lines, 2.8 KB gzip, zero deps, no GPU canvas. Cheap in bytes, less cheap in paint: a full `background-clip: text` repaint every frame on a large heading, and the glow doubles the text layers. Server render shows the static gradient from props; only the animation is client-side.

**Fit for ARKRETE** — no fit. The only type that could carry a gradient is the home monument wordmark, and that must stay bone.

**Verdict** — skip — gradient type is a second and third accent in a one-accent world.
