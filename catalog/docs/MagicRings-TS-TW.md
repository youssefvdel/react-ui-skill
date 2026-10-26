# MagicRings
**Registry**: `MagicRings-TS-TW` · **Deps**: none · **Files**: `MagicRings/MagicRings.tsx`
**What it does** — Concentric glowing rings pulse outward from the middle of a canvas, swelling toward the cursor, tilting in parallax, and flaring into extra rings on click.
**Props** — `color` / `colorTwo` (hex) — ring gradient; `ringCount` (1–12, 6); `motion` (`pulse|ripple|breathe`, pulse) — emission pattern; `speed` (1) — expansion rate; `lineThickness` (2); `glow` (0–3, 1); `followMouse` (false) with `mouseInfluence` (0.2); `clickBurst` (true) — burst rings.
**Motion** — Continuous: each ring carries its own radius and life, hover springs the centre and scale, click adds up to three expanding bursts. WebGL2 — a glow pass into a float buffer, a compose pass and an instanced 128-segment strip pass.
**Cost** — ~33 KB source, ~9.7 KB gzip, no dependencies; three programs, 15 instanced ring slots at 128 segments each, an FBO for the glow. Client-only, blank without WebGL2. Reduced motion freezes time and drops hover and bursts, which does produce a still frame.
**Fit for ARKRETE** — no fit as implemented. The same mark — thin concentric rings in one brass — is a two-path SVG at zero runtime cost.
**Verdict** — skip — a full render pipeline for an image SVG draws for free.
