# WarpText

**Registry**: `WarpText-TS-TW` · **Deps**: `ogl@^1.0.11` · **Files**: `WarpText/WarpText.tsx`

**What it does** — Rasterises a headline to an offscreen canvas, uploads it as a WebGL texture, and warps it with fbm noise and a pointer lens, adding refraction and optional chromatic split; clicks send shockwave rings through the letters. The raster is re-cut on resize, font load, and colour change so the type stays sharp.

**Props** — `text` (string, 'Bend the moment') — the headline; `color` (string, 'currentColor') — ink, read into the raster; `warpStrength` / `warpScale` (number, 0.08 / 1.7) — noise displacement and frequency; `speed` (number, 0.55) — idle motion rate; `pointerInfluence` / `pointerStrength` (number, 0.42 / 0.38) — lens radius and bend; `refraction` / `chromatic` (number, 0.018 / 0) — edge split and colour fringing; `ripple` / `clickRipple` (boolean, true / true) — pointer and click waves; `lens` ('bulge' | 'pinch' | 'swirl', 'bulge') / `intro` (boolean, true) — lens shape and 1.6 s reveal.

**Motion** — Pointer move bends and refracts the texture around a lens; fbm drift keeps it alive when idle; clicks spawn up to four ripple rings; the intro reveals the text over 1.6 s. Needs WebGL2 through `ogl` and a continuous RAF while the canvas is in view; reduced motion freezes time and dampens the pointer.

**Cost** — `ogl@^1.0.11` (~8 KB gzip), about 25 KB source, a full-viewport fragment shader with seven texture taps per pixel and a canvas raster per resize; one WebGL context per instance. Client-only: prerender emits an empty `div` with an `aria-label`, and text is an image, not selectable.

**Fit for ARKRETE** — No fit. The home monument is a fixed SVG wordmark and section titles are plain text; turning either into a shader texture would make the strongest typographic asset unselectable and soft.

**Verdict** — skip — a WebGL text toy that spends a context and a hero on decoration.
