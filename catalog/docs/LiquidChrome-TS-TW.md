# LiquidChrome
**Registry**: `LiquidChrome-TS-TW` · **Deps**: none · **Files**: `LiquidChrome/LiquidChrome.tsx`
**What it does** — Renders soft ribbons of liquid chrome swirling in a dark pool, lit like a studio product shot; the pointer drags ripples through the surface and tilts the reflection.
**Props** — `color` (hex or `[r,g,b]`, `#ffffff`) — reflection tint; `speed` (0.2) — flow rate; `amplitude` (0–2, 0.3) — ribbon depth; `thickness` (0.25–4, 1) — highlight sharpness; `roughness` (0–1, 0.3) — reflection blur; `exposure` (1) — brightness; `interactive` (true) — ripple strokes; `tilt` (1) — parallax swing from the cursor.
**Motion** — Always-on shader: sine-warped ribbon field shaded with a four-tap studio environment, plus a fluid height-field simulation (ping-pong half-float targets, up to 4 steps per frame) that the cursor strokes disturb; view yaw and pitch spring toward the pointer or drift on their own.
**Cost** — ~25 KB source, ~7.3 KB gzip, no dependencies; three WebGL2 programs with float render targets, and the most expensive shading loop in this batch. Without `EXT_color_buffer_float` it silently falls back to the static chrome pass. Client-only; reduced motion slows time and kills the parallax, but keeps animating.
**Fit for ARKRETE** — no fit. Liquid chrome is a material study; as a hero it would read as a second brand rather than a room.
**Verdict** — skip — costly, and it competes with the photography instead of framing it.
