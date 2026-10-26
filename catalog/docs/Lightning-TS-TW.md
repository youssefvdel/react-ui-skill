# Lightning
**Registry**: `Lightning-TS-TW` · **Deps**: none · **Files**: `Lightning/Lightning.tsx`
**What it does** — A full-bleed canvas draws one or more jagged bolts that crackle, fork and dim on a loop, leaning toward the pointer and striking upward from wherever you click.
**Props** — `color` (string, `#4d6bff`) — bolt tint; `bolts` (number, 1) — parallel bolts, capped at 4; `branches` (0–1, 0.5) — fork density; `angle` (deg, 0) — rotates the strike axis; `intensity` (number, 1) — glow gain; `speed` (number, 1) — drift and flicker rate; `flicker` (0–1, 0.6) — stutter amount; `clickStrike` (bool, true) — click fires a 1.3 s strike.
**Motion** — Time-driven fragment shader: bolts drift and flicker continuously, the cursor warps the nearest bolt and heats its glow, click sends a strike bolt and a flash. WebGL2 only; no GSAP, Framer Motion or three.js.
**Cost** — ~21 KB source, ~6.5 KB gzip, no dependencies. One full-screen shader at DPR ≤2, up to 4 bolts and 4 strikes, 7–8 octave noise per pixel; rAF stops offscreen, on tab hide, and whenever nothing is moving. Client-only — the canvas is blank on prerender. Reduced motion kills flicker, drift and strikes but still paints a static bolt.
**Fit for ARKRETE** — no fit. The home reel is photography; electric blue lightning would introduce a second, theatrical material in a world built on stone and low light.
**Verdict** — skip — heavy per-pixel work for decoration that argues with the photography.
