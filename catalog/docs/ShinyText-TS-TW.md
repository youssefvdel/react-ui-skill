# ShinyText

**Registry**: `ShinyText-TS-TW` · **Deps**: none · **Files**: `ShinyText/ShinyText.tsx`

**What it does** — A band of light sweeps across a line of text, from a soft sheen to chrome-like parallel bands, with optional glow; the glyphs themselves stay put. It can loop, fire on hover, or run once when scrolled into view.

**Props** — `text` / `children` — the copy to shine; `color` ('#b5b5b5') — base ink; `shineColor` ('#ffffff') — highlight; `speed` (2) — seconds per pass; `shineWidth` (40) — percent of the box the band covers; `bands` (1–3) — parallel highlights; `trigger` ('loop' | 'hover' | 'view') — what starts a pass; `glow` (0–1) — blurred duplicate behind the text.

**Motion** — A rAF loop moves a position through a `background-clip: text` gradient, rebuilding the gradient string and writing it to the span each frame of a pass; when a pass ends it waits `delay` before repeating. No dependencies. Reduced motion suppresses the loop and hover sweep, leaving flat ink.

**Cost** — 412 lines, 3.8 KB gzip, no deps. Each frame repaints the text layer and, with `glow`, a blurred duplicate: cheap on a label, measurable on a 120 px wordmark. Text stays real DOM and selectable; server render shows the flat colour.

**Fit for ARKRETE** — no fit. The monument wordmark is bone and the one brass accent is reserved for action; a sheen would be a second finish on the brand.

**Verdict** — skip — a gradient sweep on the only type that could carry it, when that type must stay still.
