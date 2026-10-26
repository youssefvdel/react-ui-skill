# GooeyNav

**Registry**: `GooeyNav-TS-TW` · **Deps**: none · **Files**: `GooeyNav/GooeyNav.tsx`

**What it does** — A pill sits behind the active link and, when you pick another, breaks into up to 32 goo blobs that fly across the bar and merge into the new link. The active label is recoloured through a clip-path cut-out of the same blob field, so the text appears to be swallowed by the pill.

**Props** — `items` (GooeyNavItem[], four demo links) — labels, hrefs, icons; `activeIndex` (number, unset → internal state) — controlled selection; `onChange` ((index, item) => void) — fires on pick; `theme` ('dark' | 'light', 'dark') — frame and ink palette; `color` (hex, theme white) — pill fill; `size` ('sm' | 'md' | 'lg', 'md') — padding and type scale; `particleCount` (15) — blobs per travel; `gooeyness` (0.5) — metaball merge radius.

**Motion** — WebGL2 fragment shader blends up to four pill SDFs and 32 capsule drops per frame; triggered by click, with a hover highlight that eases toward the pointed link. Needs WebGL2 but no GSAP, Framer Motion or three.js; without WebGL2 a fallback span shows a plain sliding pill, and reduced motion snaps the pill instantly while the hover glow still eases.

**Cost** — 940 lines, 9.3 KB gzip of source, React only, no npm deps. One nav-sized canvas with a 72 px bleed at DPR ≤ 2, a duplicated `<ul>` overlay, and a per-scanline SVG clip-path trace while blobs move; rAF stops when the pill settles. Client-only; server output is just the two lists. Without WebGL2 the goo is gone, only the fallback pill remains.

**Fit for ARKRETE** — no fit. The header on every page is four links and should be quiet; a shader there is a second show.

**Verdict** — skip — 900+ lines and a WebGL2 shader to move four nav links, when the nav's job is to be invisible.
