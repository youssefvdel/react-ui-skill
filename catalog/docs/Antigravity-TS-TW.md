# Antigravity
**Registry**: `Antigravity-TS-TW` · **Deps**: none · **Files**: `Antigravity/Antigravity.tsx`
**What it does** — Scatters a field of small particles in a loose grid, then lifts them into a glowing ring around the cursor where they orbit, banded by travelling waves. Clicking bursts them outward, and when the pointer goes idle an invisible cursor drifts on its own so the ring keeps moving.
**Props**
- `count` / `particleSize` (1500 / 0.9) — population and dot size.
- `magnetRadius` / `ringRadius` / `fieldStrength` (9 / 7 / 10) — capture radius, ring radius, spring tightness.
- `waveSpeed` / `waveAmplitude` / `waveCount` (0.4 / 1 / 3) — the banding on the ring.
- `color` / `colors` (three stops) / `colorMode` ('conic' | 'radial' | 'random').
- `colorSpeed` / `particleVariance` / `depthFactor` (0.05 / 1 / 1) — hue drift, size scatter, parallax.
- `particleShape` ('capsule' | 'sphere' | 'box' | 'tetrahedron', 'capsule').
- `lerpSpeed` / `rotationSpeed` / `pulseSpeed` (0.05 / 0 / 3) — response, orbit, pulse.
- `interactive` / `clickBurst` / `autoAnimate` / `ambient` (true / true / true / 0.25).
**Motion** — The CPU integrates 1500 spring bodies per frame (up to four substeps each) and uploads a per-particle buffer to one instanced WebGL2 draw; a second-order cursor follows the pointer, clicks add a radial impulse, and `autoAnimate` takes over after 2 s idle. No library. Reduced motion scales the clock to 0.3 — it still moves — and the loop runs whenever the canvas is visible.
**Cost** — 8 KB gzip, no dependencies. A 1500-body loop plus a 24 KB attribute upload every frame, blended full-screen; comfortable on desktop, measurable on a low-end phone. Client-only: prerenders an empty div with the canvas filled in after mount.
**Fit for ARKRETE** — no fit. A particle halo chasing the cursor is a product-launch gesture, and its coloured glow would sit on top of whatever section adopted it.
**Verdict** — skip — decoration that never comes to rest and costs CPU on every frame.
