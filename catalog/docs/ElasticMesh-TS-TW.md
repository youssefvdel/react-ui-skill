# ElasticMesh

**Registry**: `ElasticMesh-TS-TW` · **Deps**: none · **Files**: `ElasticMesh/ElasticMesh.tsx`

**What it does** — Rasterises a word or logo, builds a dense mesh from its silhouette and inflates it into a glossy, pillow-like object with a soft drop shadow. You can grab and drag it out of shape, press it in and let go; four material presets change the finish.

**Props**
- `text` (string, 'Squish') — word to inflate when no image is given.
- `src` (string, '') — logo image to inflate instead.
- `material` ('balloon' | 'chrome' | 'jelly' | 'clay', 'balloon') — surface finish.
- `inflate` (number, 1) — puffiness of the extrusion.
- `stiffness` (number, 0.5) — spring firmness.
- `wobble` (number, 0.6) — residual shake after a press.
- `grabRadius` (number, 70) — pointer reach for grabbing.
- `stretch` (number, 0.5) — how far a drag pulls the surface.

**Motion** — A spring simulation moves mesh vertices toward their rest positions; pointer drag grabs a region and stretches it, a quick click pokes a dent, and the intro drops the object in as up to 64 pieces arrive on damped springs. All in WebGL2 shaders, no library.

**Cost** — no dependencies, 50 KB TSX (~13 KB gzipped source, the heaviest file in this batch), 1,437 lines including two shader programs, a canvas-2D rasteriser and per-frame vertex uploads. Client-only; needs WebGL2 and canvas 2D. Reduced motion skips the intro, but pressing and stretching still answer the pointer.

**Fit for ARKRETE** — no fit. An inflated jelly wordmark is playful; the ARKRETE monument has to stay typographic and still.

**Verdict** — skip — 13 KB and a full physics mesh for a gag the brand cannot use.
