# TextPressure
**Registry**: `TextPressure-TS-TW` · **Deps**: none · **Files**: `TextPressure/TextPressure.tsx`
**What it does** — Splits a headline into one span per character and pushes each character's variable-font axes — weight 100–1000, width 5–205, italic, alpha — by how close the pointer is, so letters swell and thicken as you pass. Optional idle wave or pulse and a click ripple that travels through the line.
**Props**
- `text` (string, `"Compressa"`) — the headline.
- `fontFamily` / `fontUrl` (`Roboto Flex` / Google Fonts CSS) — the variable font it deforms.
- `width` / `weight` / `italic` (boolean, all `true`) — which axes get driven.
- `alpha` (boolean, `false`) — fades characters toward the pointer edge.
- `radius` (number, `0.5`) — reach of the pressure field as a fraction of the headline width.
- `smoothing` (number, `0.5`) — how lazily the pressure point follows the cursor.
- `idle` (`none` | `wave` | `pulse`, `none`) — ambient motion when the pointer is away.
- `clickRipple` (boolean, `true`) — a ripple of pressure from each click.
**Motion** — Pointer proximity measured per glyph on every rAF frame; the loop parks after about 60 idle frames. Idle wave/pulse only run while the pointer is outside. No library — but it needs a variable font, and the default pulls Roboto Flex from Google Fonts at runtime.
**Cost** — No JS dependencies, ~13 KB source / ~4 KB gzip. One span per character and a `getBoundingClientRect` for every character on every running frame, so long headlines cause layout work. Adds a remote stylesheet and font file (third-party connection, FOUT) and bakes `uppercase` into the `h1`. Prerenders at `minFontSize` then resizes after hydration.
**Fit for ARKRETE** — no fit. The hero is an SVG wordmark, every other heading is sentence case, and a headline that warps under the cursor fights the calm the brand is built on.
**Verdict** — skip — needs an external variable font and an uppercase text heading the site doesn't have.
