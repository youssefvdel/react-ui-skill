# Orb
**Registry**: `Orb-TS-TW` · **Deps**: none · **Files**: `Orb/Orb.tsx`

**What it does** — Draws a glowing ring of swirling colour that breathes and wobbles, with a bright point orbiting inside it and leaving a trail. The ring leans toward the cursor, brightens as the pointer nears, and pulses outward on click.

**Props**
- `colors` (string[], `['#9c43fe', '#4cc2e9', '#101499']`) — the three-stop palette mixed around the ring.
- `size` (number, 1) — ring diameter inside the box.
- `glow` / `bleed` (1 / 1) — halo tightness and how far the body's colour bleeds into its centre.
- `wobble` / `highlight` / `trail` (1 / 1 / 1) — edge noise, the orbiting point, and its comet tail.
- `tiltX` / `tiltY` (degrees, 0) — tilts the ring onto a plane; the shader intersects a ray per pixel.
- `hoverIntensity` (number, 1) — how far the near edge reaches toward the pointer.
- `followCursor` / `rotateOnHover` (true / true) — orbit chases the pointer, body turns while hovered.
- `intro` / `paused` (true / false) — 1.1 s scale-in on mount; freezes on a rendered frame.

**Motion** — everything is one WebGL2 fragment shader: noise-warped radius, rotating colour ramp, an orbiting light with a lag-based trail, echo rings after a click, and a spring that pulls the rim toward the cursor. Time and pointer drive it; the loop sleeps off-screen, on hidden tabs and while `paused`, and reduced motion keeps one static frame with no intro, reach or pulse.

**Cost** — 21 KB source (about 9 KB of it GLSL), ~3 KB gzip, no deps. One full-viewport fragment shader evaluating 3D simplex noise per pixel, at dpr capped to 2 — 1–2 MP of noise every frame, the heaviest per-pixel work in this batch. WebGL2 only: without a context it renders nothing at all. Must be client-only.

**Fit for ARKRETE** — no fit. A purple-and-blue glowing orb introduces a second accent to a site whose single accent is brass, and there is no section it would be doing a job in.

**Verdict** — skip — decoration with a competing palette and the highest per-pixel cost here.
