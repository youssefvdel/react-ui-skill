# TextLoop
**Registry**: `TextLoop-TS-TW` · **Deps**: `gsap@^3.13.0` · **Files**: `TextLoop/TextLoop.tsx`
**What it does** — Repeats a string along an SVG path — wave, circle, infinity, arch, line, or your own path data — and slides it continuously, with an optional solid ribbon strip under the letters and an optional second path crossing it. Both ends are masked to fade out.
**Props**
- `text` (string, `"React ✦ Bits"`) — the phrase repeated to fill the path.
- `shape` (`wave` | `circle` | `infinity` | `arch` | `line`, `wave`) — the built-in curve.
- `speed` (number, `90`) — pixels per second along the path.
- `fontSize` / `fontWeight` / `letterSpacing` (46 / 800 / 2) — letter sizing.
- `ribbon` (boolean, `true`) + `ribbonColor` (`#5227FF`) — the tape strip under the text.
- `edgeFade` (number, `0`) — softness of the fade at both ends.
- `pauseOnHover` (boolean, `true`) — eases the flow to a stop under the pointer.
- `draggable` (boolean, `false`) — grab and fling the text, with decaying momentum.
**Motion** — Time-driven offset along the path, advanced by `gsap.ticker`; only runs while the SVG is in view. Hover eases the base speed to zero, drag release throws a fling, and `scrollBoost` adds scroll velocity. Reduced motion sets base speed to 0 and never starts the ticker, leaving static text on the path.
**Cost** — GSAP is the only dependency and the site has none, so this brings ~23 KB gzip for a ticker and one hover tween. SVG `textPath` with the string repeated to fill the path; the first server render is one repetition, then measurement after fonts load reflows it to N. IntersectionObserver stops it offscreen.
**Fit for ARKRETE** — no fit. A perpetual marquee is the one kind of motion the design deliberately avoids, and the default violet ribbon is a second accent.
**Verdict** — skip — 23 KB of GSAP to run a ticker, for a strip the pages have no place for.
