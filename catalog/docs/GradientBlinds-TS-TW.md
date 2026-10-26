# GradientBlinds

**Registry**: `GradientBlinds-TS-TW` · **Deps**: none · **Files**: `GradientBlinds/GradientBlinds.tsx`

**What it does** — A wall of satin gradient slats tilted toward a light that follows the pointer, each slat catching a sheen as the bank sways. Clicking sends a ripple across the slats; the canvas fills its container edge to edge.

**Props** — `gradientColors` (string[], pink/violet) — slat colour stops; `angle` (0) — slat direction in degrees; `blindCount` (16) — maximum slats; `blindMinWidth` (60) — width floor that caps the count on small screens; `spotlightRadius` (0.5) — light reach as a fraction of the short side; `sway` (0.35) — idle tilt drift; `noise` (0.3) — film grain; `clickEffect` ('ripple' | 'none', 'ripple').

**Motion** — One WebGL2 fragment shader; each slat's tilt is a function of pointer distance plus a sine sway, and ripples are four timed waves. No GSAP, Framer Motion or three.js. Reduced motion removes sway, ripples and the intro, but grain and gradient shift keep the loop alive unless `noise` and `gradientSpeed` are zeroed.

**Cost** — 656 lines, 6.4 KB gzip, no deps; one opaque full-bleed canvas at DPR ≤ 2 with alpha disabled and `mix-blend-mode: lighten` by default, so it must be the ground layer, not an overlay. rAF idles only when noise, shift, sway and pointer are all still. No WebGL2 means a blank panel. Client-only.

**Fit for ARKRETE** — no fit. It sits exactly where a room photograph belongs on home or projects, and the pink/violet ramp is a second accent.

**Verdict** — skip — beautifully made, but it replaces the photography with synthetic satin: decoration with no job.
