# SplashCursor
**Registry**: `SplashCursor-TS-TW` · **Deps**: none · **Files**: `SplashCursor/SplashCursor.tsx`
**What it does** — A full-viewport fluid simulation follows the pointer: dye is injected along the movement, swirled by vorticity and bled away over a second or two. Clicks drop a crown-shaped splat of colour that drifts with the flow.
**Props** — `colors` (3 hex defaults) palette · `rainbow` (true) full-spectrum cycling instead of the palette · `quality` ("high") sim 128 / dye 1440 / 20 pressure iterations, low is 64 / 512 / 10 · `intensity` (1) dye per move · `swirl` (3) vorticity · `trail` (1) dissipation · `size` (1) splat radius · `contained` (false) fixed overlay versus parent bounds.
**Motion** — Runs while the pointer moves, then idles to a cleared canvas after ~2.6 s; an intro stroke draws itself once. Reduced motion is checked only for the intro — the trail still runs, so an off switch has to be added. WebGL2, multi-pass.
**Cost** — 6.7 KB gzip, no dependencies, but 14 shader programs and eight-plus framebuffers; per frame: curl, vorticity, divergence, 16–20 Jacobi pressure iterations, gradient, two advections, optional four-level bloom. The heaviest GPU load in the batch by a wide margin. Client-only.
**Fit for ARKRETE** — No fit. Rainbow dye over architectural photography would be the loudest object on the site.
**Verdict** — skip — a fluid sim is a second accent, a GPU budget and a personality the brand does not have.
