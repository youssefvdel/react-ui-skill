# ThoughtLine
**Registry**: `ThoughtLine-TS-TW` · **Deps**: `motion@^12.23.12`, `@hugeicons/react@^1.1.10`, `@hugeicons/core-free-icons@^4.3.3` · **Files**: `ThoughtLine/ThoughtLine.tsx`
**What it does** — An AI "thinking" status line: glyph, label and a live timer that expands into a list of steps, ticks them off as they finish, then folds into one line reading "Thought for 3.2s". Steps cross-fade in and dim when done.
**Props**
- `label` / `doneLabel` (string, `"Thinking…"` / timer text) — working and finished wording.
- `steps` (string[], `[]`) — the reasoning trace listed under the header.
- `working` (boolean, `true`) — drives breathing, timer and completion.
- `glyph` (`sparkle` | `dot` | `none` | ReactNode, `sparkle`) — leading mark.
- `showTimer` (boolean, `true`) — counts elapsed time in tenths.
- `collapsible` / `collapseOnSettle` (boolean, both `true`) — click to open; fold when done.
- `settleDuration` (number, `350`) — length of the fold and blur.
- `onSettle` (function) — fires with the elapsed seconds.
**Motion** — motion/react loops a breathing opacity on label and glyph and animates height/opacity on settle; a CSS keyframe pulses unfinished step dots and a shimmer sweeps the label. `useReducedMotion` damps the breath and drops the shimmer. Click toggles the trace.
**Cost** — motion plus two Hugeicons packages for three glyphs; ~14 KB source / 3.8 KB gzip before those. A live timer re-renders every 100 ms, and an `aria-live` region announces the label. Client-only by nature.
**Fit for ARKRETE** — no fit. There is no assistant, agent or asynchronous process on the site to narrate; a "Thinking…" row on an interior fit-out page is nonsense.
**Verdict** — skip — an AI chat primitive with no surface here.
