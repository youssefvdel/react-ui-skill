# ParticleText
**Registry**: `ParticleText-TS-TW` · **Deps**: none · **Files**: `ParticleText/ParticleText.tsx`

**What it does** — Samples a line of text into a few thousand dots on an offscreen canvas, then animates them from scattered positions into the letterforms. Once formed the word drifts, parts around the cursor, and bursts outward on click before settling back.

**Props**
- `text` (string, 'React Bits') — what the particles spell; real text stays in an `sr-only` span.
- `particleSize` / `density` (2 / 4) — dot radius and sampling step; density is the particle count dial.
- `color` ('currentColor') — base dot colour, so it inherits the surrounding ink.
- `highlightColor` / `highlightMode` ('#ff5a36' / 'motion') — the second colour, applied to fast-moving dots or as a gradient.
- `intro` ('gather' | 'rain' | 'spiral' | 'scan', 'gather') — how the letters arrive.
- `gatherDuration` / `stagger` (1600 ms / 420 ms) — assembly time and per-particle delay spread.
- `clickBurst` / `burstStrength` / `pointerRepel` (true / 1 / 40) — click shockwave and how hard the cursor pushes dots aside.
- `idleDrift` (0.7) — constant drift once formed; 0 leaves the word still.

**Motion** — canvas 2D, one rAF: the intro eases each particle to its sampled glyph target with a stagger, then idle drift and pointer repel keep it alive, and a click sends a damped spring burst outward. Fonts are awaited before sampling so the word doesn't re-flow after load. Under reduced motion the particles sit at their targets and nothing moves.

**Cost** — 30 KB source, ~3.5 KB gzip, no deps. One canvas drawing thousands of 1-pixel fills per frame, bucketed into 96 tone/fade groups to avoid per-particle state changes; the glyph sampling re-runs only when text, size, weight or density changes. Client-only (needs canvas metrics and `document.fonts`).

**Fit for ARKRETE** — the 404 page only: the monument line reassembling out of dust, in bone, with no highlight colour. Not the home wordmark — the mark is the argument's first beat and should be still.

**Verdict** — adapt — worth exactly one lazy use on the 404 with `highlightColor` set to bone and `idleDrift` at 0.
