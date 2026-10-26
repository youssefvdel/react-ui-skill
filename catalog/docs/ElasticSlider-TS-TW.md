# ElasticSlider

**Registry**: `ElasticSlider-TS-TW` · **Deps**: `@hugeicons/react@^1.1.10`, `@hugeicons/core-free-icons@^4.3.3` · **Files**: `ElasticSlider/ElasticSlider.tsx`

**What it does** — A horizontal or vertical slider whose track thickens under the cursor, whose filled portion clips a second value layer, and whose fill stretches past either end like rubber before springing back. It ships volume-low and volume-high icons at each end by default.

**Props**
- `value` (number, —) — controlled value.
- `defaultValue` (number, 50) — initial value when uncontrolled.
- `maxValue` (number, 100) — top of the range.
- `isStepped` (boolean, false) — snap to whole steps.
- `orientation` ('horizontal' | 'vertical', 'horizontal') — axis.
- `maxStretch` (number, 50) — how far the fill can be pulled past an end.
- `bounce` (number, 0.5) — springiness of the return.
- `onChange` (function, —) — fires on every value change.

**Motion** — Pointer drag with a spring loop; dragging past an end stretches the fill and pulses the icon, and release springs back. Hover grows the track from 6 to 12 px; wheel and keyboard also move it. Reduced motion snaps straight to the target and skips icon pulses, so it degrades cleanly.

**Cost** — two Hugeicons packages for two icons (tree-shaken to the volume pair, but a new icon runtime), 26 KB TSX (~7.1 KB gzipped source). DOM only, rAF while settling. Client-only for measurement and pointer capture.

**Fit for ARKRETE** — no fit. The contact form's budget field should be a native range or a select; a media-style slider with volume icons and rubber overshoot is the wrong grammar for an inquiry.

**Verdict** — skip — a good slider for a music player, not for a fit-out brief.
