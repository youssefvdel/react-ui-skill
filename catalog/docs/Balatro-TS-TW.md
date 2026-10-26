# Balatro
**Registry**: `Balatro-TS-TW` · **Deps**: none · **Files**: `Balatro/Balatro.tsx`
**What it does** — Runs the swirling, high-contrast Balatro paint shader across its container, quantised into visible pixels, with a cursor that stirs the paint through a persistent velocity field and clicks that leave spinning whirlpools. An optional CRT pass adds scanlines and a vignette, and a 2.2 s opening unwinds the swirl into place.
**Props**
- `color1` / `color2` / `color3` ('#DE443B' / '#006BB4' / '#162325') — the three paint bands.
- `contrast` / `lighting` / `swirl` (3.5 / 0.4 / 0.25) — paint character.
- `speed` / `rotationSpeed` / `scale` (1 / 0 / 1) — flow, spin, texture zoom.
- `detail` (5, 1–8) — warp loop iterations per pixel; the main cost dial.
- `pixelSize` (1.5) / `crt` (0) — block size in device px and scanline strength.
- `offset` ([0, 0]) / `opacity` (1) — framing and blend.
- `mouseInteraction` / `mouseStrength` / `clickSwirl` (true / 1 / true) — stirring.
- `intro` / `lightMode` / `maxDevicePixelRatio` (true / false / 2).
**Motion** — Two shader passes (paint, optional CRT) and a ping-pong RG16F velocity field that records pointer movement and decays; time drives flow and spin, clicks add twirls with a 3.2 s life. WebGL2, no library. Reduced motion still advances at 0.2× — it never freezes — though the loop parks when speed and rotation are zero and nothing is settling.
**Cost** — 7 KB gzip, no dependencies. Device pixels are capped at a 2.4 MP budget, but the paint shader loops five times per pixel by default plus a field pass — the most expensive per-pixel shader in this batch. Client-only: prerenders an empty div.
**Fit for ARKRETE** — no fit. A psychedelic card-game shader would put a red and blue swirl behind rooms that are the whole argument.
**Verdict** — skip — spectacle with no subject, and reduced motion slows the swirl to a fifth of its pace, cuts its amount, skips the opening and drops the click swirl — it calms rather than stops.
