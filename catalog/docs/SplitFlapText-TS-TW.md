# SplitFlapText
**Registry**: `SplitFlapText-TS-TW` · **Deps**: none · **Files**: `SplitFlapText/SplitFlapText.tsx`
**What it does** — An airport departures board: each character is a tile split at a hinge, and phrases change by flipping through random glyphs before settling on the target. Tiles cascade left to right, right to left, centre out or at random.
**Props** — `words` (three defaults) phrases cycled · `flipDuration` (0.12 s) one flap · `stagger` (0.06 s) cascade delay per tile · `cycleDelay` (2400 ms) hold between phrases · `flipsPerChar` (8) random glyphs before settling · `charset` ("alphanumeric") scramble alphabet · `tileStyle` ("board" | "minimal") physical tiles or bare split glyphs · `fontSize` (52).
**Motion** — A rAF loop steps each tile's glyphs, CSS 3D `rotateX` flaps carry shading, hinge and optional glare, staggered per the chosen order; loops on a timer and pauses when the tab is hidden. Reduced motion collapses to an instant swap. No library, but it injects a `<style>` block.
**Cost** — 4.3 KB gzip, no dependencies; DOM-heavy — twelve characters is 60+ nodes plus a style tag per instance; the monospace stack is baked into its CSS and its default phrases are uppercase. Prerenders as blanks until hydration.
**Fit for ARKRETE** — No fit. An uppercase mono board is the departures-hall look the brief rules out, and it types the brand as travel.
**Verdict** — skip — the one component whose entire identity contradicts sentence case.
