# SoftAurora
**Registry**: `SoftAurora-TS-TW` · **Deps**: none · **Files**: `SoftAurora/SoftAurora.tsx`
**What it does** — A soft aurora band hangs across the canvas: layered 3D Perlin noise through an exponential falloff, two tinted layers blended, plus grain. The band bends toward the pointer and a click sends a pulse travelling along it.
**Props** — `color1` (#f7f7f7) / `color2` (#e100ff) layer tints · `speed` (0.6) drift · `bandHeight` (0.5) vertical position · `bandSpread` (1) falloff width · `spectrum` (1) hue cycling versus flat two-colour · `scale` (1.5) noise size · `opacity` (1) · `lightMode` (false) ink-on-paper inversion.
**Motion** — Time-driven flow and hue drift, a 2 s opening fade, cursor bend/shift, up to four click pulses. Reduced motion only slows it to 0.35×, so it has no true static state; it does stop offscreen and when the tab is hidden. WebGL2.
**Cost** — 4.9 KB gzip, no dependencies; one context, drawn at 0.5–1× CSS resolution by design, but three octaves of 3D gradient noise across two layers per pixel, so fill rate is the limit, not canvas size. Client-only.
**Fit for ARKRETE** — No fit. Magenta and violet are a second and third accent, and coloured glow fights near-black plus brass.
**Verdict** — skip — a rainbow aurora is the opposite of one accent used only for the action.
