# SlicedWaves
**Registry**: `SlicedWaves-TS-TW` · **Deps**: none · **Files**: `SlicedWaves/SlicedWaves.tsx`
**What it does** — Instanced bars of glowing light stand in a row and recede in perspective, like a rack of neon ribbons. Each column runs a three-stop palette along its height, and a depth-of-field plane pulls focus to whichever bar the cursor is nearest.
**Props** — `color1`/`color2`/`color3` (#ffd9a8 / #ff5fa2 / #5b8cff) palette · `ribbons` (3, max 6) bars per column · `spacing` (28 px) column pitch · `perspective` (0.45) yaw of the plane · `slices` (0) cut ribbons into slats · `blur` (0.6) defocus away from focus · `position` (0.78) vertical baseline · `speed` (1) wave travel.
**Motion** — Continuous time-driven wave, a 1.5 s intro sweep, cursor-driven focus spring (stiffness 36, damping 11) and a lift under the pointer. Reduced motion freezes time and focus but still renders. WebGL2 with instanced draws and a half-float target, byte fallback.
**Cost** — 5.6 KB gzip, no dependencies. One context, HDR target up to 2560 px on the long side, instance buffer rebuilt every frame, additive blending. Fill-bound on retina; client-only.
**Fit for ARKRETE** — No fit. Three saturated colours plus glow add two accents the palette does not have, and the read is nightclub, not interiors.
**Verdict** — skip — a neon tri-colour light rig has no section on a bone-and-brass site.
