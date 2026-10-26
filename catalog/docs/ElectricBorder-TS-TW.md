# ElectricBorder

**Registry**: `ElectricBorder-TS-TW` · **Deps**: none · **Files**: `ElectricBorder/ElectricBorder.tsx`

**What it does** — Measures the rounded rectangle of whatever it wraps and draws crackling electric strands along that edge on a canvas overlay. A soft glow sits under the strands, arcs occasionally leap off the border, and the current brightens and surges toward the cursor.

**Props**
- `children` (ReactNode, —) — the element being outlined; the canvas sits above it.
- `color` (string, `#7df9ff`) — strand and halo colour.
- `speed` (number, 1) — how fast the current moves.
- `chaos` (number, 0.5) — how ragged the strands are.
- `strands` (number, 3) — strand count, clamped 1–6.
- `thickness` (number, 1.5) — line width in px.
- `arcs` (number, 1) — average arcs thrown off the border.
- `cursorRadius` (number, 90) — reach of the cursor surge.

**Motion** — Continuous time-driven jitter along the perimeter, with random arcs and a cursor-following power surge; WebGL2 fragment shader, no library. It runs a rAF whenever the element is on screen. Reduced motion kills flicker and new sparks and slows time to 20%, but the border still shimmers rather than sitting still.

**Cost** — no dependencies, 29 KB TSX (~8.8 KB gzipped source). A full-size transparent canvas overlay plus a per-frame path update; cheap per pixel but always running while visible. Client-only; needs WebGL2 or the border disappears entirely.

**Fit for ARKRETE** — no fit. Cyan electric edging is a second accent and pure decoration; a hairline brass border already does the job.

**Verdict** — skip — neon current fights the brass accent and has no static state worth shipping.
