# Radar
**Registry**: `Radar-TS-TW` · **Deps**: none · **Files**: `Radar/Radar.tsx`
**What it does** — Renders a radar scope: concentric rings, up to twelve spokes, tick marks, a beam that sweeps around leaving a phosphor afterglow, and up to sixteen contacts that drift, brighten as the beam crosses them and leave fading echoes. The whole plane tilts toward the pointer.
**Props** — `color` (string, '#3ef09a') — phosphor green; `mode` ('sweep' | 'pulse', 'sweep') — rotating beam or expanding rings; `speed` (number, 1); `trail` (number, 0.35) — afterglow length; `ringCount` (number, 6); `targets` (number, 6, max 16); `clutter` (number, 0.35) — specks of noise; `tilt` (number, 0) — plane rotation in degrees.
**Motion** — Time-driven sweep or pulse rings, contact drift with heading and turn, sprite halos and a five-level bloom chain every frame; pointer position tilts the plane; `prefers-reduced-motion` stops the sweep, the contacts and the tilt. WebGL2, no three.js.
**Cost** — No dependencies, about 10.1 KB gzip of source. Two offscreen passes plus five downsample/upsample bloom levels at DPR ≤ 2, sixteen sprite quads, float buffers when `EXT_color_buffer_float` exists. Client-only, blank without WebGL2, and the container needs an explicit height or it collapses.
**Fit for ARKRETE** — No fit. A surveillance scope is the wrong metaphor for fit-out work, and no section of home, projects, services, about or contact is a live display.
**Verdict** — skip — a well-built toy that says security operations, not interiors.
