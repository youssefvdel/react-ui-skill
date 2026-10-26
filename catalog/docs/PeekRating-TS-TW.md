# PeekRating
**Registry**: `PeekRating-TS-TW` · **Deps**: `@hugeicons/react@^1.1.10`, `@hugeicons/core-free-icons@^4.3.3` · **Files**: `PeekRating/PeekRating.tsx`

**What it does** — A row of five stars, hearts or bolts where hovering lifts the stars up to the cursor in a travelling wave, magnifies the one under the pointer and previews the score. Clicking commits it with a pop, a second click clears, and an optional tooltip names the level.

**Props**
- `value` / `defaultValue` (number, 0) — controlled or uncontrolled score.
- `onChange` / `onPreview` ((value) => void) — committed score, and hovered score or null.
- `count` (number, 5) — how many marks.
- `shape` ('star' | 'heart' | 'bolt', 'star') — built-in glyph; `icon` replaces it.
- `labels` (string[], []) — per-mark names, used in the tooltip and the aria-label.
- `activeColor` / `idleColor` ('#f5b400' / '#52525b') — lit and unlit ink.
- `size` / `lift` / `magnify` (28 / 6 / 1.15) — mark size, hover rise, hovered scale.
- `showTip` / `allowClear` / `readOnly` (true / true / false) — tooltip, click-to-clear, static display.

**Motion** — CSS only: `transform` over 320 ms on the hover wave, colour over 160 ms, and a scale pop on commit. State lives in refs with direct style writes — no rAF, no library. Reduced motion drops the lift, the magnify and the pop and just changes colour.

**Cost** — two Hugeicons packages, of which only the three used glyphs are bundled (roughly 6–8 KB gzip); 13 KB source, ~1.8 KB gzip. Five buttons, no timers, no canvas. It calls `useLayoutEffect` to place the tooltip, so prerender needs the isomorphic-hook swap or React's SSR warning.

**Fit for ARKRETE** — no fit. Nothing on the site is rated, and the default gold star is exactly the second accent the brief forbids; the enquiry form asks for a project, not a score.

**Verdict** — skip — a rating control for a site that has nothing to rate.
