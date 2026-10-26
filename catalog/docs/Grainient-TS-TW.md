# Grainient

**Registry**: `Grainient-TS-TW` · **Deps**: none · **Files**: `Grainient/Grainient.tsx`

**What it does** — A slow field of grainy, silk-lit gradient bands that drifts and can be stirred with the pointer, with a click twirl. The default palette is ember orange on near-black, and the output is opaque and full-bleed.

**Props** — `colors` (string[], five ember stops) — gradient ramp; `type` ('linear' | 'radial', 'linear') — band geometry; `bands` (1) — hard repeats of the ramp; `speed` (1) — drift rate; `flow` (0.8) — noise warp depth; `silk` (0.35) — fake relief lighting; `grainAmount` (0.08) — film grain; `interactive` (true) — pointer stirring and click twirl.

**Motion** — Two WebGL2 passes: a half-res field (domain-warped Lab gradient, optional silk shading) and a full-res grain composite; pointer trail and click twirl feed uniforms. No GSAP, Framer Motion or three.js. Reduced motion freezes time, grain animation, stirring and the intro.

**Cost** — 688 lines, 7.1 KB gzip, no deps; half-res field plus full-res grain pass at DPR ≤ 2, opaque, so it has to be a background. No WebGL2 means an empty box. Client-only.

**Fit for ARKRETE** — no fit. A flowing gradient behind copy is a second accent and cuts contrast; the grain it sells is a 1 KB static noise layer.

**Verdict** — skip — ambience where the site wants a photograph, and its grain does not need a shader.
