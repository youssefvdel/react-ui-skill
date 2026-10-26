# PaperCrumple
**Registry**: `PaperCrumple-TS-TW` · **Deps**: `three@^0.180.0` · **Files**: `PaperCrumple/PaperCrumple.tsx`

**What it does** — Maps a photograph onto a simulated sheet of paper: press and drag and the sheet closes into a wrinkled, creased ball that follows your hand and tilts with the drag; let go and it unfolds back to flat. The print stays on the paper the whole way, with soft stock showing at the torn edges.

**Props**
- `src` (string, required) — the image; remote files must allow CORS or it reports an error and shows the plain image.
- `width` / `height` (320 / 400) — sheet size in px, scaled to fit its box.
- `releaseBehavior` ('stay' | 'restore' | 'creased', 'restore') — what happens on release.
- `crumpleAmount` / `crumpleDuration` (0.85 / 0.55 s) — how far it crushes, over how long.
- `foldCount` / `foldSharpness` / `wrinkleDepth` (6 / 0.6 / 0.65) — fold guides, crease hardness, wrinkle amplitude.
- `paperColor` / `roughness` / `paperTexture` (— / 0.92 / 0.08) — the stock seen at edges and behind the print.
- `lightAngle` / `lightIntensity` / `shadow` (-35° / 1.8 / true) — the raking light that makes the folds read.
- `detail` / `seed` (64 / 7) — mesh resolution and the fixed fold pattern.

**Motion** — pointer hold and drag drive springs from flat to crumpled, with the sheet following the drag and returning to origin; release unfolds on a second spring, or leaves it creased. The crumple itself is precomputed at mount by a position-based-dynamics solve — 64 sampled frames, hinge and edge constraints, layer separation — and played back, so there is no physics at runtime. three.js WebGL scene with a custom depth material for the sheet's own shadow. Reduced motion snaps the springs instead of tweening them and kills the drag tilt.

**Cost** — `three` ^0.180 is roughly 170 KB gzip tree-shaken, more than the entire 150 KB initial budget on its own, plus 45 KB source (~5 KB gzip). Mount runs hundreds of solver passes over a `detail`² grid before the sheet appears — tens to hundreds of milliseconds of blocked main thread — and it needs a WebGL context with shadow maps. Non-negotiable: lazy chunk, client-only guard, static `<img>` as the poster, and a fallback when the context is lost.

**Fit for ARKRETE** — no fit. The photography is the argument; crumpling a finished room into a ball of waste paper argues the opposite of what the page is for.

**Verdict** — skip — a lovely demo that spends a three.js budget to damage the one asset the site sells.
