# ScrollVelocity

**Registry**: `ScrollVelocity-TS-TW` · **Deps**: motion@^12.23.12 · **Files**: `ScrollVelocity/ScrollVelocity.tsx`

**What it does** — Lines of text repeat as a marquee whose speed and direction follow page-scroll velocity; fast scrolling stretches the type vertically and skews it, and rows can alternate solid and outlined.

**Props** — `texts` (ReactNode[], `[]`) — one marquee row per entry; `velocity` (100) — base px/s; `numCopies` (6) — repeats per row to fill the width; `damping` (50) / `stiffness` (400) — spring that smooths scroll velocity; `velocityMapping` ({input:[0,1000], output:[0,5]}) — scroll rate to speed multiplier; `pauseOnHover` (false) — stops the row under the pointer; `fadeEdges` (false) — masks both ends; `draggable` (false) — grab and fling a row.

**Motion** — A `useAnimationFrame` loop moves `x` every frame, flips direction with the scroll sign and multiplies base speed by a spring-smoothed scroll velocity; `skewWithVelocity` and `scaleWithVelocity` add lean and squash. Requires `motion/react`; reduced motion freezes the marquee and leaves the text still.

**Cost** — 3.4 KB gzip of source plus the `motion` runtime (about 34 KB gzip). No IntersectionObserver, so the rAF loop runs for the life of the component even off screen. `numCopies` spans of real text per row, widths measured by ResizeObserver. Prerenders as static repeated text.

**Fit for ARKRETE** — no fit. A repeating marquee is the ambient copy the site avoids, and services already has five quiet panels.

**Verdict** — skip — a permanent rAF marquee plus 34 KB of Motion for text that repeats itself.
