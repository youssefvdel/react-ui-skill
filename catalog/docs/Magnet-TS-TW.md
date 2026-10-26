# Magnet
**Registry**: `Magnet-TS-TW` · **Deps**: none · **Files**: `Magnet/Magnet.tsx`
**What it does** — Wraps any child in a div that eases toward the cursor once it comes within a padding ring, then springs back to rest; optional tilt and scale ride the same pull.
**Props** — `padding` (px, 100) — activation ring; `magnetStrength` (2) — divisor on the offset; `maxOffset` (px, none) — clamp on travel; `axis` (`both|x|y`, both); `tilt` (deg, 0); `scale` (1); `spring` (`{stiffness 170, damping 16, mass 1}`); `onActiveChange` (fn) — engagement callback.
**Motion** — Pointer-driven spring integrated in up to 120 Hz substeps, written as `translate3d` plus optional perspective and rotate; a module-level registry lets only the nearest magnet engage when `exclusive` is left on. No library, and the rAF stops once the element is at rest.
**Cost** — ~9 KB source, ~2.8 KB gzip, no dependencies; one transform per frame on one element, listeners shared across every instance. Prerenders fine — plain markup, motion starts after mount. Reduced motion disables it completely, and touch pointers are ignored.
**Fit for ARKRETE** — contact page, the single brass inquiry action only (submit or the "start a project" mail link), with `maxOffset` ~8 and `tilt` 0.
**Verdict** — adapt — the cheapest motion in the batch, and it can be confined to the one element meant to invite a click.
