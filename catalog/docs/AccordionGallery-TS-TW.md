# AccordionGallery
**Registry**: `AccordionGallery-TS-TW` · **Deps**: `gsap@^3.13.0` · **Files**: `AccordionGallery/AccordionGallery.tsx`
**What it does** — Lays a set of image panels in one strip; the panel you point at grows to its share of the width while the others compress, its photo drifts against its neighbours, colour returns to it and its caption slides in beside a lit bar. Panels with a link navigate; arrow keys and focus move the open panel too.
**Props**
- `items` ({ image, label, link, alt }[], five picsum defaults) — the panels.
- `defaultIndex` (number, 2) — which panel starts open.
- `expandRatio` (number, 0.52) — width share given to the open panel, clamped 0.2–0.9.
- `orientation` ('horizontal' | 'vertical', 'horizontal') — strip direction; forced to a column under 520 px.
- `trigger` ('hover' | 'click', 'hover') — hover opens, or only click.
- `parallax` / `tilt` / `stagger` (0.5 / 8 / 0.06) — image drift, panel rotation, caption cascade.
- `grayscale` (boolean, true) — closed panels desaturate.
- `height` / `gap` / `radius` (460 / 10 / 16) — frame geometry in px.
**Motion** — A GSAP timeline animates `flexGrow`, `rotateY`/`rotateX`, image translate and a `--ag-gray`/`--ag-dim` CSS pair over 0.6 s `power3.out`; captions fade and slide with a 0.06 s stagger. Triggered by hover, focus, click or arrow keys, recomputed by ResizeObserver. Needs `gsap` core only, no ScrollTrigger. `prefers-reduced-motion` is read once at render and collapses every duration to 0, so it switches instantly rather than animating.
**Cost** — 3 KB gzip of source plus GSAP core (~23 KB gzip). Five panels animating `flex-grow` means layout on every frame of the 0.6 s move — fine at this count, not something to scale to twenty. SSR-safe: no window at module scope, markup prerenders, the matchMedia read is guarded, so no hydration mismatch.
**Fit for ARKRETE** — Services › "The five trades" strip. It is already there, hand-ported to `src/components/reactbits/AccordionGallery.tsx` with trade bullets, arrow keys and a reduced-motion branch, without GSAP.
**Verdict** — skip — the site already ships a better version of this exact component; the registry build adds GSAP for the same flex-grow.
