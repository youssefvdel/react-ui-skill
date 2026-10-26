# LogoLoop
**Registry**: `LogoLoop-TS-TW` · **Deps**: none · **Files**: `LogoLoop/LogoLoop.tsx`
**What it does** — A seamless marquee of logos or custom nodes that can run as a straight line, a wave, an arc or a ring, faded at both edges; items can carry a link, a label or a hover colour, and the track can be dragged.
**Props** — `logos` (`{src|node, href, alt, title}[]`, required) — items; `speed` (px/s, 120) — drift; `direction` (`left|right|up|down`, left); `logoHeight` (px, 28); `gap` (px, 32); `layout` (`line|wave|arc|orbit`, line) — geometry; `pauseOnHover` (bool, on) — halt under the cursor; `draggable` (true) — pointer drag with fling.
**Motion** — A JS engine writes `translate3d` and opacity per item on a measured, tripled track: constant drift, hover deceleration, drag inertia, optional scroll boost, tilt or ring projection, and a staggered intro. DOM and transforms only; no library.
**Cost** — ~43 KB source, ~11.8 KB gzip, no dependencies but the list duplicated several times in the DOM and a permanent rAF while visible. Prerenders to a static row, so it degrades sanely; the engine starts after mount. Reduced motion sets speed to zero and skips magnify, leaving a still row.
**Fit for ARKRETE** — about page, one muted line of material houses and suppliers under "its trades" — line layout, no bend, no drag.
**Verdict** — adapt — a real credibility element done without dependencies; use line only, and only if the names are worth showing.
