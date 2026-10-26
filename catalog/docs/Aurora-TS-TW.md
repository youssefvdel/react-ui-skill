# Aurora
**Registry**: `Aurora-TS-TW` · **Deps**: none · **Files**: `Aurora/Aurora.tsx`
**What it does** — Paints a soft horizontal aurora band across the top or bottom of its container, built from up to three noise-warped layers with a colour ramp interpolated in OKLCH. It brightens and lifts locally toward the pointer and fades in over 2.4 s on mount.
**Props**
- `colorStops` (string[], purple/green/purple) — up to five ramp stops.
- `amplitude` / `height` / `scale` (1 / 0.45 / 1) — band wave height, hem position, noise frequency.
- `blend` / `glow` / `brightness` / `opacity` (0.5 / 0.6 / 1 / 1) — softness and strength.
- `layers` (1, max 3) — stacked depth; later layers are thinner and dimmer.
- `direction` ('top' | 'bottom', 'top') — which edge it hangs from.
- `speed` (1) / `time` (number, optional) — clock rate, or a fixed time for a still.
- `mouseInteraction` (true) — pointer lifts the hem within a gaussian reach.
- `paused` / `lightMode` / `dpr` (false / false / auto) — freeze, ink-on-paper mode, resolution.
**Motion** — One full-screen fragment shader: simplex noise warps a hem line per layer, the clock advances every frame, and the pointer pulls the hem up within a soft radius on a 0.6 s follow. WebGL2 only, no library. Reduced motion freezes the clock so the band is still, but the rAF loop keeps running while visible; `paused` renders one frame and parks.
**Cost** — 5 KB gzip, no dependencies. Four noise evaluations per layer per pixel, up to three layers, every frame at DPR up to 2 — a full-viewport fill that never idles while on screen. Client-only: prerenders an empty div, so the static HTML and the first paint over FTP carry no band at all.
**Fit for ARKRETE** — no fit. A coloured bloom behind the monument wordmark or the closing stage adds a second light source to a page lit by photography, and the stock ramp is the purple-green SaaS aurora.
**Verdict** — skip — atmosphere that fights the photograph and keeps the GPU awake for it.
