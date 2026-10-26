# Ballpit
**Registry**: `Ballpit-TS-TW` · **Deps**: none · **Files**: `Ballpit/Ballpit.tsx`
**What it does** — Drops a pit of glossy balls into the frame; they fall, collide and pile on the floor under a studio light rig, and the cursor shoves them, drags and throws the grabbed one. A click bursts the pile apart, and the balls can be satin, matte, gloss, frosted or metal.
**Props**
- `count` / `minSize` / `maxSize` (200 / 0.5 / 1) — population and ball scale, capped at 4000.
- `colors` (string[], white) — ball palette.
- `material` ('satin' | 'matte' | 'gloss' | 'frosted' | 'metal', 'satin').
- `gravity` / `friction` / `bounce` / `wallBounce` (0.5 / 0.9975 / 0.85 / 0.95).
- `depth` / `drift` (2 / 0) — pit depth and idle wander.
- `followCursor` / `cursorSize` / `grab` (true / 1 / true) — pointer coupling.
- `clickEffect` ('burst' | 'none', 'burst') — click response.
- `lightColor` / `lightIntensity` / `exposure` / `shadows` (white / 1 / 1 / 0.6).
**Motion** — A CPU physics step (gravity, hashed ball–ball contacts, wall bounce, grab spring) writes screen-space sphere instances that a custom WebGL2 shader raymarches with studio lighting and contact shading — no three.js. Cursor moves push, drag grabs and throws, click bursts. Reduced motion drops the intro fall, drift and burst; the pit still settles, then the loop parks after 0.8 s of quiet.
**Cost** — 11 KB gzip, no dependencies. 200 bodies with hash-grid contacts is modest CPU; the fragment shader does per-pixel sphere lighting over the covered area, resolution capped at DPR 2. Client-only: prerenders an empty div.
**Fit for ARKRETE** — no fit. A play pit is a toy; the bar here is a section that carries photography, not a physics demo.
**Verdict** — skip — charming, and completely wrong for a fit-out contractor's portfolio.
