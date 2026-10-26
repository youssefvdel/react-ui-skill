# Waves

**Registry**: `Waves-TS-TW` · **Deps**: none · **Files**: `Waves/Waves.tsx`

**What it does** — Draws dense silk-like lines that undulate with Perlin noise, part around the cursor, and spring back when it leaves; clicks send a radial ripple through the strands. Solid or dashed lines, rotation, spacing, fade and a light-mode ink treatment are exposed.

**Props** — `lineColor` / `accentColor` (string, '#ffffff' / undefined) — base and heated line colours; `lineStyle` ('solid' | 'dashed', 'solid') — strand treatment; `spacing` / `lineWidth` (number, 10 / 1) — line pitch and weight; `amplitude` / `scale` / `twist` / `speed` (number, 32 / 1 / 1 / 1) — wave shape and rate; `mouseRadius` / `mouseStrength` / `bounce` / `returnDuration` (number, 175 / 1 / 0.5 / 1.4) — pointer well and spring; `clickRipple` / `intro` (boolean, true / true) — click waves and reveal; `fade` / `opacity` (number, 0 / 1) — edge mask and alpha; `lightMode` / `paused` (boolean, false / false) — ink inversion and freeze.

**Motion** — A vertex shader waves each strand; a CPU spring grid (12 px cells, simulated only inside the pointer's dirty rectangle) displaces it near the cursor and on click, while the noise field flows continuously. Raw WebGL2, no animation library; the RAF stops when off-screen or fully settled.

**Cost** — Zero dependencies, about 26 KB source (~8 KB gzip), one WebGL2 context, an instanced draw capped at 1.6 M vertices, and a JS spring loop over the active grid area per frame. Client-only; no WebGL2 or no JS leaves only the background colour.

**Fit for ARKRETE** — No fit. Home and project pages are carried by full-bleed photography, and a generative line field behind them is a competing texture with no informational job.

**Verdict** — skip — beautiful silk lines that would put a second, abstract world behind the photographs.
