# EchoText

**Registry**: `EchoText-TS-TW` · **Deps**: none · **Files**: `EchoText/EchoText.tsx`

**What it does** — Stacks up to 24 copies of a line behind the real text, each offset along a direction and progressively faded and blurred. The copies lag behind the pointer, bend toward it and settle into a single word; clicking scatters them outward and they spring home.

**Props**
- `text` (string, 'Motion Echo') — the line to duplicate.
- `echoes` (number, 12) — number of ghost copies, clamped 0–24.
- `offset` (number, 36) — distance of the furthest copy in px.
- `direction` ('right' | 'left' | 'up' | 'down' | 'diagonal', 'right') — trail axis.
- `lag` (number, 0.24) — how slowly copies follow.
- `blur` (number, 3) — blur applied to the furthest copy.
- `tint` (string | false, '#7dd3fc') — colour mixed into the ghosts.
- `mode` ('entrance' | 'pointer' | 'both', 'both') — whether copies move on mount, with the pointer, or both.

**Motion** — Each copy is transformed every frame: an entrance ramp on mount, pointer-follow inside `cursorRadius`, an idle drift, or a scroll offset — then a damped return to rest. Click bursts push copies outward on a 1.1 s life. DOM spans and rAF only, no library.

**Cost** — no dependencies, 17 KB TSX (~5.1 KB gzipped source). Up to 25 text spans with `filter: blur()` and `will-change: transform`, which is a lot of GPU layers at display sizes and scales with font size. Reduced motion renders zero echoes, so the text is plain and static. Client-only for the animation; the server output is the text plus copies.

**Fit for ARKRETE** — home, the monument wordmark: `mode="entrance"`, 3 echoes, `offset` 10, `blur` 0, `tint={false}`, 700 ms, then still. The pointer trail is not invited.

**Verdict** — adapt — one settle behind the wordmark is on-brand; the shipped twelve tinted, blurred copies would be a second accent.
