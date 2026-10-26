# Noise
**Registry**: `Noise-TS-TW` · **Deps**: none · **Files**: `Noise/Noise.tsx`

**What it does** — Lays a tiled film-grain texture over whatever sits behind it, with optional dust specks, hairs, drifting scratches, scanlines and a flicker. At low opacity it stops reading as an effect and starts reading as one camera, one stock, one shoot.

**Props**
- `opacity` (number, 0.2) — grain strength; over photography the usable band is 0.05–0.08.
- `size` (number, 1) — tile scale; 1 is a 256 px tile, higher values coarsen the grain.
- `fps` (number, 24) — how often the grain re-shuffles; 0 freezes it.
- `blendMode` ('overlay' | 'soft-light' | 'multiply' | 'screen' | 'difference', 'overlay') — how the tile mixes with the plate.
- `contrast` (number, 0.6) — spread of the noise, from fine 35 mm to TV static.
- `dust`, `scratches`, `scanlines`, `flicker` (0–1, 0) — old-print damage; every one is off by default.
- `fixed` (boolean, false) — covers the viewport instead of the parent box.
- `zIndex` (number, undefined) — stacking, for sitting above an image but below the header.

**Motion** — the grain tile nudges its background position at `fps` and optionally drops its opacity for a flicker; the dust canvas redraws specks and hairs and ages a couple of drifting scratches. Time is the only trigger — no hover, no scroll. It stops when off-screen (IntersectionObserver) and, under reduced motion, paints once and holds still. Plain DOM plus canvas 2D: no GSAP, no Framer, no WebGL.

**Cost** — 11 KB source, roughly 1.7 KB gzip, zero dependencies. One 256×256 canvas becomes a blob-URL background (allocated once, then reused); the dust canvas only clears itself unless `dust` or `scratches` is above zero. A `mix-blend-mode` layer makes the compositor re-blend everything under it, so mount it section-sized rather than `fixed` on phones. Prerenders safely: it emits a wrapper div and starts in `useEffect`.

**Fit for ARKRETE** — Home, the hero plate and the six-room reel: one grain at ~0.06 over all six photographs makes them read as a single shoot instead of six files. Nothing else on the site needs it.

**Verdict** — adapt — the grain is the one texture this dark world is missing, but drop dust, scratches and scanlines and run it section-sized at 0.06.
