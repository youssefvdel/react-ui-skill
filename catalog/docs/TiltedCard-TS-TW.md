# TiltedCard
**Registry**: `TiltedCard-TS-TW` · **Deps**: none · **Files**: `TiltedCard/TiltedCard.tsx`
**What it does** — A card that rotates in 3D toward the pointer with a moving glare, a soft ground shadow and inner layers that parallax at different depths. An optional back face flips into place on click or Enter.
**Props**
- `imageSrc` / `altText` — the front image and its alt text.
- `rotateAmplitude` (number, `12`) — maximum tilt in degrees.
- `scaleOnHover` (number, `1.05`) — lift under the pointer.
- `glare` (number, `0.5`) — strength of the moving highlight; `glareColor` tints it.
- `shadow` (number, `0.5`) — opacity of the ground shadow.
- `overlayContent` / `overlayDepth` — content floated above the image.
- `backContent` / `flipOnClick` (ReactNode / `true`) — the reverse face and its trigger.
- `gyroscope` (boolean, `true`) — device-orientation tilt on phones.
**Motion** — `pointermove` feeds an eased rAF that writes rotateX/rotateY and translates each layer by its depth; the flip is a 180° rotateY with a spring settle; optional intro rise. Reduced motion cuts tilt to 30%, drops the intro and float, and flips instantly. No library.
**Cost** — No dependencies, ~25 KB source / 6.7 KB gzip. Five-plus absolutely positioned layers per face, two radial-gradient overlays and a masked rim, `preserve-3d` and backface hiding; rAF only while moving or settling. SSR-safe markup, interaction client-only.
**Fit for ARKRETE** — no fit. Projects are a full-bleed scroll stack and services a flex accordion; a tilting card with glare belongs to a product grid the site never uses.
**Verdict** — skip — strong for a shop, the wrong idiom for full-bleed rooms.
