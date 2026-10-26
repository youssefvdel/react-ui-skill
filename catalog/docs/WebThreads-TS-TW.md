# WebThreads

**Registry**: `WebThreads-TS-TW` · **Deps**: none · **Files**: `WebThreads/WebThreads.tsx`

**What it does** — A full-screen shader weaving up to 24 glowing threads that pinch through one or more nodes; the strand nearest the cursor brightens while the others dim, and a click sends a light surge along the bundle. Palette, pinch point, node count, angle and grain are all props.

**Props** — `colors` / `coreColor` (string[], ['#5227FF', '#FF9FFC'] / '#FFFFFF') — palette and hot core; `threadCount` / `speed` / `frequency` (number, 6 / 0.2 / 5) — strand count and wave rate; `spread` / `taper` / `position` / `pinch` (number, 0.18 / 1 / 0.5 / 0.5) — fan width, taper, baseline, pinch point; `nodes` / `angle` (number, 1 / 0) — pinch count and rotation; `glow` / `falloff` / `thickness` / `brightness` (number, 0.02 / 0.6 / 1.1 / 0.6) — light profile; `mirror` (boolean, true) / `pulses` (number, 0) / `shimmer` (boolean, false) — symmetry and travelling light; `mouseInteraction` / `pulseOnClick` (boolean, true / true) — hover focus and click surge; `intro` / `paused` (boolean, true / false) — stroke-in reveal and freeze.

**Motion** — Threads undulate and shimmer with time; hover runs a CPU distance test against each strand, then eases focus and dims the rest; click fires a travelling surge; intro strokes the bundle in. Requires WebGL2, no library; after three quiet frames it stops re-rendering, though the RAF keeps ticking.

**Cost** — Zero dependencies, about 24 KB source (~7 KB gzip), a full-screen fragment shader looping over up to 24 threads per pixel, one canvas and RAF while visible, DPR capped at 2 by default. Client-only; without WebGL2 it renders an empty transparent div.

**Fit for ARKRETE** — No fit. Luminous neon threads read as a crypto or AI-studio motif, not plaster, stone and joinery, and no ARKRETE section needs a glowing backdrop.

**Verdict** — skip — a striking tech-brand background with nothing to say about interior fit-out.
