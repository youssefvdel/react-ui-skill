# GradientWaves

**Registry**: `GradientWaves-TS-TW` · **Deps**: none · **Files**: `GradientWaves/GradientWaves.tsx`

**What it does** — A raymarched ocean of satin waves under a hazy horizon, seen from a low camera, with a light that follows the pointer and a swell that rises where you click. It fills its container, grading from horizon colour to crest.

**Props** — `horizonColor` ('#5227FF') — sky/haze colour; `waveColor` ('#FF9FFC') — wave body; `crestColor` ('#FFFFFF') — crest highlight; `tilt` (64) — camera pitch in degrees; `amplitude` (2.5) — wave height; `speed` (0.4) — time scale; `quality` ('low' | 'medium' | 'high', 'medium') — 56/84/120 march steps; `mouseInteraction` (true) — parallax and light steering.

**Motion** — A WebGL2 fragment shader ray-marches a height field per pixel; pointer parallax and click swells arrive as uniforms. No GSAP, Framer Motion or three.js. Reduced motion freezes time, skips the intro and ignores clicks, and the loop stops after a few quiet frames.

**Cost** — 680 lines, 6.9 KB gzip, no deps; the heaviest GPU item in this batch: up to 120 steps per pixel at DPR 2 across a full-bleed area. Must be code-split and never placed behind text. No WebGL2 means an empty div. Client-only.

**Fit for ARKRETE** — no fit. A synthetic sea is the opposite of a Cairo or Dubai room, and it would take the hero slot the wordmark and reel own.

**Verdict** — skip — the most expensive way in this batch to put a gradient where a photograph goes.
