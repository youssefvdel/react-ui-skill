# GradualBlur

**Registry**: `GradualBlur-TS-TW` · **Deps**: none · **Files**: `GradualBlur/GradualBlur.tsx`

**What it does** — Stacks 8 (up to 16) masked backdrop-blur layers along one edge so content dissolves into the page instead of ending on a hard line, with an optional tint wash. Sits over content and adds no colour of its own unless tinted.

**Props** — `position` ('top' | 'bottom' | 'left' | 'right', 'bottom') — edge to fade; `height` ('6rem') — depth of the fade; `strength` (2) — max blur radius, ×12 px; `layers` (8) — blur steps, clamped 1–16; `curve` ('linear' | 'bezier' | 'ease-in' | 'ease-out' | 'ease-in-out') — falloff; `tint` ('transparent') — colour wash at the edge; `autoHide` (false) — fade the blur out at the ends of a scroller; `target` ('parent' | 'page', 'parent') — absolute in a container or fixed to the viewport.

**Motion** — No animation of its own: one scroll listener when `autoHide` is on, plus an optional hover boost that scales the blur. Pure CSS `backdrop-filter` and `mask-image`; no GSAP, Framer Motion or three.js, and nothing to disable for reduced motion.

**Cost** — 273 lines, 3.1 KB gzip, zero deps, DOM only. Eight full-width layers each running a backdrop-filter is a real compositing cost on mobile — four layers at `strength` 2 is the sane ceiling, and a tint adds one more. Markup is SSR-safe; the effects are client-only. No WebGL.

**Fit for ARKRETE** — home: the fixed header over the six-room reel, so rooms dissolve under the bar instead of meeting a border; also project captions over the scroll stack.

**Verdict** — adapt — the one keeper here, cut to 4 layers and scoped to the header.
