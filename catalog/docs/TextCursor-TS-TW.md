# TextCursor
**Registry**: `TextCursor-TS-TW` · **Deps**: none · **Files**: `TextCursor/TextCursor.tsx`
**What it does** — Stamps copies of a word or emoji along the path the pointer travels, each turned to the direction of travel and shrinking and fading behind the head. `stamp` drops a copy every `spacing` pixels, `chain` keeps a fixed tail of copies alive, `ribbon` lays the word's individual letters along the trail.
**Props**
- `text` (string, `"Hello"`) — the glyphs repeated; in ribbon mode each letter is one link.
- `mode` (`stamp` | `chain` | `ribbon`, `stamp`) — discrete stamps, a steady tail, or a letter ribbon.
- `spacing` (number, `88`) — gap between stamps and the unit measured for ribbon letters.
- `maxPoints` (number, `7`) — chain length; unused in stamp mode.
- `smoothing` (number, `0.3`) — pointer lag, 0 raw, higher heavier.
- `fade` / `shrink` / `exitDuration` (number, `0.6` / `0.5` / `0.5`) — how fast the tail dissolves.
- `fontSize` / `fontWeight` / `fontFamily` (28 / 600 / inherit) — the type of the trail.
- `hideCursor` (boolean, `false`) — hides the native cursor over the container.
**Motion** — Pointer-driven rAF loop: copies pop in, rotate to the path heading, optionally drift, then scale down and fade on a removal timer; the loop parks once the tail is empty. No library. `prefers-reduced-motion` kills the pop and float but keeps the stamping.
**Cost** — No dependencies, ~14 KB source / ~4 KB gzip. One absolutely positioned span per stamp, recycled through a pool, plus a pruned path array; transform and opacity written per element per frame. Server render is an empty layer, so no hydration mismatch, but the trail is client-only.
**Fit for ARKRETE** — no fit. The home hero is a logo lockup over photography and a text trail there competes with the room; no other section of the five pages has a free cursor surface.
**Verdict** — skip — decoration with no job, and the only reusable part is the pointer-path maths.
