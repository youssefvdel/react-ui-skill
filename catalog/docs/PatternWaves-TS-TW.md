# PatternWaves
**Registry**: `PatternWaves-TS-TW` · **Deps**: `ogl@^1.0.11` · **Files**: `PatternWaves/PatternWaves.tsx`

**What it does** — Fills a box with a grid of dots, dashes, plus marks or ASCII glyphs whose size and brightness follow a moving height field, so the surface reads as silk, swell or pond water lit from one side. Moving the cursor drops ripples into it; the presets are silk, ocean, pond, lines, terminal and mesh.

**Props**
- `preset` ('silk' | 'ocean' | 'pond' | 'lines' | 'terminal' | 'mesh', 'silk') — a bundle of the settings below.
- `pattern` ('dot' | 'square' | 'plus' | 'line' | 'glyph') — the mark; glyphs use the `characters` atlas.
- `wave` ('silk' | 'swell' | 'ripple') — the height field's behaviour.
- `spacing` / `markSize` (9 / 0.95) — grid pitch and mark size as a fraction of the cell.
- `depth` / `shine` / `contrast` (0.95 / 0.8 / 1.2) — fold depth, specular lift, and how hard the light/dark split is.
- `color` / `backgroundColor` ('#ffffff' / '#000000') — ink and ground, both parsed through a 1×1 canvas.
- `fade` / `fadeSize` ('edges' | 'center' | 'bottom' | 'top' | 'none' / 0.5) — how the field dissolves at its borders.
- `interactive` / `cursorSize` / `cursorStrength` (true / 50 / 0.6) — cursor ripples and their reach.

**Motion** — three WebGL passes per frame: a height/normal field, a half-float ping-pong ripple simulation (1/8 resolution, 60 Hz, damped), and a mark pass drawing instanced dots or glyphs from a generated atlas; pointer movement injects impulses. Time-driven; reduced motion freezes time and removes ripples but keeps the surface.

**Cost** — `ogl` ^1.0.11 (~15 KB gzip) plus 31 KB source (~3.5 KB gzip). Dpr is clamped by a 4.5 MP pixel budget, the grid is capped at 4096×4096 cells, and ripples need `EXT_color_buffer_float` — without it the surface still draws, without ripples. WebGL2 only, and it appends its own canvas, so it must be client-only and given an explicit height.

**Fit for ARKRETE** — no fit. It would be a third procedural surface competing with the photographs and with the ceiling assembly already drawn in CSS on services.

**Verdict** — skip — a beautiful texture with no job, bought with a WebGL dependency and three passes a frame.
