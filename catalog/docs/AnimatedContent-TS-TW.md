# AnimatedContent
**Registry**: `AnimatedContent-TS-TW` · **Deps**: `gsap@^3.13.0` · **Files**: `AnimatedContent/AnimatedContent.tsx`
**What it does** — Wraps a block and animates it into place when it enters the viewport: it travels, scales, blurs, rotates or tilts, optionally wiping in through a CSS mask. With `stagger` set it animates each direct child in sequence instead of the wrapper, and it can play on mount or scrub with scroll.
**Props**
- `distance` / `direction` / `reverse` (100 / 'vertical' / false) — travel and its axis.
- `duration` / `ease` / `delay` (0.8 / 'power3.out' / 0) — timing.
- `initialOpacity` / `animateOpacity` / `scale` (0 / true / 1) — starting state.
- `blur` / `rotate` / `tilt` (0 / 0 / 0) — filter and 3D extras; tilt sets perspective 900.
- `wipe` ('none' | 'up' | 'down' | 'left' | 'right' | 'center', 'none') — mask reveal.
- `stagger` / `staggerFrom` (0 / 'start') — child cascade and its origin.
- `threshold` / `once` / `trigger` / `scrub` (0.1 / true / 'scroll' / false) — when it fires.
- `disappearAfter` / `disappearDuration` (0 / 0.5) — optional exit after arrival.
**Motion** — A paused GSAP timeline is played by a ScrollTrigger at `top (1 − threshold)%`, animating transform, filter, opacity and a `--ac-wipe` custom property used by a mask gradient; children stagger. Needs `gsap` plus `ScrollTrigger`, registered at module load. Reduced motion is handled: it un-hides and completes immediately.
**Cost** — 2 KB gzip of source plus GSAP core (~23 KB gzip) and ScrollTrigger (~11 KB gzip), one trigger and timeline per instance. The wrapper ships with `invisible` and is only un-hidden by JS, so a failed or blocked bundle leaves the section blank — precisely the failure the site's own reveal layer is built to survive. Markup is SSR-safe; content is not visible without hydration.
**Fit for ARKRETE** — every page's scroll reveal, but that job is already done by `src/lib/useReveal.ts` (IntersectionObserver + CSS, mutation-aware, failsafe-gated) at zero KB. The only idea not already present is the CSS mask wipe.
**Verdict** — skip — 34 KB of GSAP to re-implement a reveal layer the site already built more carefully; copy the mask gradient as CSS if the wipe is wanted.
