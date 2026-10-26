# LiquidEther
**Registry**: `LiquidEther-TS-TW` · **Deps**: none · **Files**: `LiquidEther/LiquidEther.tsx`
**What it does** — A GPU fluid solver turns pointer movement into coloured ink that swirls, folds and slowly fades; when nobody is moving, a canned demo path keeps the surface alive.
**Props** — `colors` (string[], violet/pink/lilac) — ink palette; `mouseForce` (20) — push strength; `cursorSize` (4–600, 100) — splat radius; `persistence` (0–1, 0.75) — how long dye lingers; `viscosity` (0–1, 0) — diffusion; `resolution` (0.05–1, 0.5) — simulation grid scale; `autoDemo` (true) — idle self-motion; `clickBurst` (true) — impulse on click.
**Motion** — A real per-frame fluid step — splat, smooth, divergence, 32 Jacobi pressure iterations, project, advect — with pointer velocity as force; the idle demo resumes 1 s after the last input. WebGL2 with half-float targets and a 256 px palette texture.
**Cost** — ~29 KB source, ~7.9 KB gzip, no dependencies; the heaviest component in this batch: seven programs and ~32 texture passes per frame over up to 140 000 cells. Client-only, and it bails out entirely without float render targets. Reduced motion disables the demo, intro and click burst, but pointer dye still moves.
**Fit for ARKRETE** — no fit. A multicoloured ink palette is a second accent by definition, and a solver this heavy cannot be justified by a background.
**Verdict** — skip — the worst cost-to-meaning ratio in the batch.
