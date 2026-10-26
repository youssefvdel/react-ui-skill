# Silk
**Registry**: `Silk-TS-TW` · **Deps**: none · **Files**: `Silk/Silk.tsx`
**What it does** — A full-bleed canvas paints a satin sheet: soft diagonal folds, a moving specular highlight and fine grain. Moving the pointer drags the fabric and tilts the light toward it; a click sends a ring ripple across the surface.
**Props** — `speed` (5) drift rate · `scale` (1) fold density · `color` (#7B7481) base tone · `sheenColor` (#ffffff) highlight tint · `sheen` (0.5) gloss strength · `depth` (0.5) fold relief · `glow` (0.3) bloom, 0 skips the second pass · `fade` (0) edge mask to transparent.
**Motion** — Time-driven flow, a 2.2 s unfold on mount, pointer drag plus a light that leans toward the cursor, and up to four click ripples. Under reduced motion the intro is skipped, flow freezes, pointer and click are ignored, and it draws a single static frame; it also stops offscreen. WebGL2 only, no library.
**Cost** — 5.1 KB gzip of JS, no dependencies. One WebGL2 context; a quarter-res field pass plus a full-res composite, and a `generateMipmap` per frame when `glow > 0`; DPR capped at 2. Client-only: prerender emits an empty div, so it has to mount after paint rather than block the hero.
**Fit for ARKRETE** — The about page lede, the one text-only section with no photograph, at ~25% opacity in bone on near-black; not the home hero, which is already full-bleed rooms.
**Verdict** — adapt — 5 KB buys a material ground where photography is absent, but only one instance, `glow` 0, brass sheen, lazy-loaded.
