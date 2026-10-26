# VariableProximity

**Registry**: `VariableProximity-TS-TW` · **Deps**: none · **Files**: `VariableProximity/VariableProximity.tsx`

**What it does** — Splits a line of text into single-letter spans and drives each letter's variable-font axes from its distance to the cursor, so weight and optical size swell under the pointer and settle back as it leaves. An optional idle wave rolls the same swell across the line on a loop, and line breaks are re-measured so the effect survives wrapping.

**Props** — `label` (string, "") — the text, split into letters and word spans; `fromFontVariationSettings` / `toFontVariationSettings` (string, `'wght' 400, 'opsz' 9` / `'wght' 1000, 'opsz' 40`) — axis values at rest and at full proximity; `radius` (number, 50) — pointer distance in px over which the effect fades; `falloff` ('linear' | 'exponential' | 'gaussian', 'linear') — distance curve; `smoothing` (number, 0.2) — easing time constant; `fromColor` / `toColor` (string, undefined) — optional colour mix on the same distance; `scale` / `lift` (number, 1 / 0) — per-letter growth and rise; `idleWave` (boolean, false) — self-running wave when the pointer is away.

**Motion** — Per-letter `font-variation-settings` (and optional colour and transform) are written in a RAF loop, eased toward pointer-derived targets; the loop only runs while letters are settling or the idle wave is on. Triggered by window-level `mousemove`/`touchmove`, scroll, and font load; no animation library, but it needs a variable font with the named axes.

**Cost** — Zero npm dependencies, about 15 KB source (~5 KB gzip), but it injects a Google Fonts `@import` for Roboto Flex and hardcodes that family, so it brings a second typeface. One span per letter plus a `getBoundingClientRect` per letter on pointer frames, and a full re-measure on resize/font load; the markup prerenders, the interaction is client-only.

**Fit for ARKRETE** — No fit. The home monument is an SVG `Logo`, not text, and every heading is set in the site's Archivo/Schibsted faces; swapping in Roboto Flex to make letters breathe under the cursor adds a second typographic voice for a hover flourish.

**Verdict** — skip — needs Roboto Flex and per-letter hit-testing for a hover effect that fights the monument wordmark.
