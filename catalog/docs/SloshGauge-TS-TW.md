# SloshGauge
**Registry**: `SloshGauge-TS-TW` · **Deps**: none · **Files**: `SloshGauge/SloshGauge.tsx`
**What it does** — A vertical glass capsule holds liquid that settles at a level, its surface tilting with velocity and splashing against the ends as it moves. The percentage is printed twice, half in the glass and half in the fill, so the number appears to sit in the liquid.
**Props** — `value` (0–100, controlled) level · `interactive` (false) makes it a drag/keyboard slider · `viscosity` (0.15) damping, 0 snaps · `tilt` (0.45) surface lean per velocity · `splash` (0.42) bounce at the ends · `showValue` (true) prints the number · `width`/`height` (88×180) capsule · `ticks` (4) right-edge graduations.
**Motion** — Spring integrator in 120 Hz substeps, rAF only until it parks; pointer drag, arrows/Page/Home/End. Reduced motion forces critical damping, no tilt, no splash. No library.
**Cost** — 2.7 KB gzip, no dependencies; one div, a handful of children, `clip-path` fill. Renders statically, interactive only on the client.
**Fit for ARKRETE** — No fit. The site reports no figures, and a numbered gauge is the stat-row decoration the brief rules out.
**Verdict** — skip — a meter with nothing true to measure.
