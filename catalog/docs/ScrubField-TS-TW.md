# ScrubField

**Registry**: `ScrubField-TS-TW` · **Deps**: motion@^12.23.12 · **Files**: `ScrubField/ScrubField.tsx`

**What it does** — A compact number chip with a label, value, suffix and fill bar: drag it sideways and the number scrubs, with a rubber-band past the limits and a delta bubble above the chip. A click turns it into a text field for typing an exact value.

**Props** — `value` / `defaultValue` (24) — controlled or initial number; `min` (0) / `max` (100) — clamp range; `step` (1) — rounding increment; `label` ('Radius') — leading caption; `suffix` ('px') — unit; `sensitivity` (2) — px of drag per step; `rubberReach` (8) — percent of range it stretches past a limit; `accent` ('#f5f5f5') — fill, bubble and chip colours.

**Motion** — Pointer drag updates a Motion value; past the limits a log curve bends the travel and release springs back over `returnDuration` (300 ms). Click or Enter opens typing, arrows step, Shift ×10, Alt ×0.1, Home/End jump. Uses Motion's `animate` and `useMotionValue`; reduced motion snaps back instead of springing.

**Cost** — 406 lines, 4.5 KB gzip, plus `motion` (about 34 KB gzip). One chip, one input and one absolutely positioned bubble; pointer listeners exist only during a drag. Prerender output is a normal input carrying its value.

**Fit for ARKRETE** — no fit. The contact form wants a plain budget field; a drag-to-scrub chip hides its affordance and fights the calm tone.

**Verdict** — skip — a designer's toy for a form that should take thirty quiet seconds.
