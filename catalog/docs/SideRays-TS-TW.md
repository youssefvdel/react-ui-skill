# SideRays

**Registry**: `SideRays-TS-TW` · **Deps**: none · **Files**: `SideRays/SideRays.tsx`

**What it does** — Soft shafts of light fan in from a corner or side of the box, shimmer slowly and lean toward the pointer, with optional dust motes. It is a procedural light wash, not an image.

**Props** — `origin` ('top-right') — corner or side the rays enter from; `rayColor1` ('#FFC46B') / `rayColor2` ('#96c8ff') — the two shaft colours; `blend` (.6) — mix between them; `intensity` (2) — brightness; `spread` (2) — fan width; `density` (5) — shaft count; `sharpness` (.5) — edge hardness; `followMouse` (true) — rays lean toward the cursor.

**Motion** — One fullscreen WebGL2 fragment shader marches procedural shafts over a hash-based dust field; time advances the shimmer and pointer angle eases into an aim uniform. `intro` fades the wash in over 1.6 s. Reduced motion renders a single static frame with no sway and no tracking.

**Cost** — 523 lines, 5.6 KB gzip, no deps; one triangle, DPR ≤ 2 and a 2.4 MP pixel budget, so cheap per frame but a permanent WebGL2 context with no fallback. rAF stops off screen and on hidden tabs. Client-only; prerender is an empty canvas.

**Fit for ARKRETE** — no fit. ARKRETE's light comes from the rooms in the photography; painted shafts in the hero compete with the reel.

**Verdict** — skip — a synthetic light rig for a site whose argument is real light on real interiors.
