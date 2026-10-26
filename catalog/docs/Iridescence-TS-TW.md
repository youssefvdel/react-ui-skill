# Iridescence
**Registry**: `Iridescence-TS-TW` · **Deps**: none · **Files**: Iridescence/Iridescence.tsx
**What it does** — A full-bleed liquid surface of broad iridescent folds that shift from teal through green to magenta as they move, with optional grain, sheen and fade. The pointer stirs the field and clicks drop swirls that unwind slowly.
**Props** — `color` (string | [r,g,b], white) — base tint; `speed` (number, 1); `amplitude` (number, 0.1); `scale` (number, 1); `detail` (number, 8) — fold count; `warp` (number, 1); `hueShift` (number, 0), `saturation` (number, 1), `brightness` (number, 1.5); `stir` (number, 0.5) and `clickSwirl` (boolean, true) — pointer response; `resolution` (number, 1) — render scale.
**Motion** — A continuous WebGL2 fragment shader with six live swirl uniforms and a small field texture for the stir; time drives the folds, pointer movement and clicks modulate them. Reduced motion freezes the phase and disables stir and swirl. No library.
**Cost** — No deps, ~5.6 KB gzip, one full-screen pass at DPR ≤ 2 (drop `resolution` to 0.6 on mobile), paused offscreen. Fragment cost scales with area, so full-bleed on a large display is the expensive case. Prerenders as a blank canvas.
**Fit for ARKRETE** — no fit — a rainbow soap film is a second palette and pure decoration; no section needs a moving background behind photography.
**Verdict** — skip — a beautiful shader that fights the one-accent, near-black rule for no functional gain.
