# WakeSlider

**Registry**: `WakeSlider-TS-TW` · **Deps**: `motion@^12.23.12` · **Files**: `WakeSlider/WakeSlider.tsx`

**What it does** — A thumbless range slider drawn as 32 thin vertical bars: filled bars light up to the value, and the bar tops lift in a travelling wake whose height follows drag velocity, then settle. It is a real control — pointer drag, click-to-seek, arrow/Page/Home/End keys, and ARIA slider attributes.

**Props** — `value` / `defaultValue` (number, undefined / 50) — controlled or initial value; `min` / `max` / `step` (number, 0 / 100 / 1) — range and snapping; `bars` / `height` / `restHeight` (number, 32 / 56 / 12) — bar count and track geometry; `fillColor` / `trackColor` / `crestColor` (string) — lit, unlit, and wake colours; `sensitivity` / `reach` / `skew` (number, 1 / 6 / 0.6) — wake amplitude, spread, and asymmetry; `glide` / `smoothing` (number, 0.3 / 100) — handle spring and velocity smoothing; `showValue` / `formatValue` (boolean, false / fn) — readout beside the track; `disabled` / `ariaLabel` (boolean, false / string) — inert state and accessible name.

**Motion** — The handle position is a `useSpring` on the value, with a second spring on its velocity; bar `scaleY` and crest opacity are painted per frame from both, so the wake leads or trails the handle by `skew` and decays with `glide`/`smoothing`. Drag, click, and keyboard trigger it; needs `motion` (the Framer Motion successor).

**Cost** — `motion@^12` adds the motion runtime (tens of KB gzip depending on tree-shaking), about 9 KB component source; 32 spans transformed per frame while moving, no canvas. Reduced motion renders a flat fill and no springs. Prerenders its bars, but the interaction and springs are client-only.

**Fit for ARKRETE** — No fit. The site has no numeric control anywhere — no budget slider, no stat row, no configurator — so the control has no question to answer.

**Verdict** — skip — a nicely made slider for a site that never asks for a number.
