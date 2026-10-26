# LineWaves
**Registry**: `LineWaves-TS-TW` · **Deps**: none · **Files**: `LineWaves/LineWaves.tsx`
**What it does** — A canvas fills with ~72 hairline curves flowing in slow waves across a dark ground, a brighter band of light drifting through them; a lens near the cursor bends the lines and a click drops a ripple.
**Props** — `lineCount` (2–400, 72) — density; `lineWidth` (0.25–12, 1.3) — stroke weight; `speed` (0.3) — flow rate; `warpIntensity` / `warpScale` (1, 1) — wave amplitude and scale; `rotation` (deg, −33) — field angle; `highlight` (0–1, 1) — light-band strength; `edgeFade` (0–1, 0) — vignette; `enableMouseInteraction` (true) — cursor lens and click ripple.
**Motion** — Continuous time-driven shader; the palette cycles through three colours, the cursor drags a displacement lens, click adds a ripple, and an intro sweeps a reveal across the field. WebGL2, one pass, fwidth-based anti-aliased lines.
**Cost** — ~19 KB source, ~5.8 KB gzip, no dependencies; one full-screen shader capped at 2.4 MP, rAF whenever visible. Client-only, blank on prerender. Reduced motion only drops time to quarter speed — it never becomes a still image.
**Fit for ARKRETE** — no fit. Fine-line waves behind a form or footer would be texture with no job, and they compete with the photography.
**Verdict** — skip — decorative, and its reduced-motion path is a slow animation rather than a calm static frame.
