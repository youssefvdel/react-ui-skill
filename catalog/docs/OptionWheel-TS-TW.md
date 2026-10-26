# OptionWheel
**Registry**: `OptionWheel-TS-TW` · **Deps**: none · **Files**: `OptionWheel/OptionWheel.tsx`

**What it does** — Lays a list of words on a circle at the left or right edge, so the one at the centre sits upright and large while its neighbours curl away, tilt, blur and fade. Wheel, drag or arrow keys spin the wheel to a stop with one item selected.

**Props**
- `items` (string[], twelve music genres) — the options; the demo list is a genre picker.
- `defaultSelected` (number, 3) — index the wheel starts on.
- `onChange` ((index, item) => void) — fires on every change of the centred item.
- `side` ('left' | 'right', 'left') — which edge the arc grows from.
- `fontSize` (number, 3) — size in rem; sets the row height with `spacing`.
- `tilt` (number, 6) — degrees between neighbours; 0 flattens the wheel to a plain list.
- `blur` / `fade` (2 / 0.25) — how fast options away from the centre go soft and dim.
- `smoothing` (number, 200) — ms of easing behind the target position.

**Motion** — one rAF eases the wheel position toward its target with frame-rate-independent exponential smoothing, then writes `translate`, `rotate`, `opacity` and `blur()` per row; the loop stops when it settles. Wheel events are captured non-passively and `preventDefault`-ed, with a 140 ms settle after the last event; drag uses pointer capture after 4 px; arrows step by one. Optional audio tick per selection. No libraries.

**Cost** — 12 KB source, ~2 KB gzip, no deps. Twelve absolutely-positioned nodes, each carrying a CSS blur while off-centre — up to twelve blurred layers compositing, which is the real cost on a phone. A non-passive wheel listener that swallows the gesture will fight Lenis on the home page; it also reads `getComputedStyle` during render to get rem size.

**Fit for ARKRETE** — no fit. The only option list on the site is the "project type" select in the contact enquiry form, and a full-height curved wheel is the wrong instrument for one step of a five-step form.

**Verdict** — skip — a picker for a list we don't have, that takes the wheel away from Lenis.
