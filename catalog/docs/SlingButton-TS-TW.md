# SlingButton
**Registry**: `SlingButton-TS-TW` · **Deps**: motion, @hugeicons/react, @hugeicons/core-free-icons · **Files**: `SlingButton/SlingButton.tsx`
**What it does** — A round pad sits in a well with a slack band across it. Drag the pad away and the band stretches, an arc around the rim fills, and past the arm point a release flings a burst of dots and fires `onSend`.
**Props** — `onSend` fires on armed release or tap · `size` (56 px) pad diameter · `armAt` (48 px) pull that arms it · `maxPull` (160 px) rubber-band ceiling · `particles` (14) dots per launch · `axis` ("any" | "horizontal" | "vertical") constrained pull · `tapSends` (true) plain click also sends · `padColor` / `accentColor`.
**Motion** — Pointer drag with rubber-band resistance, band path and power arc redrawn per frame, dots launched with the Web Animations API, spring recoil. Reduced motion drops the dots, fades the tension and settles instantly. Needs motion and a Hugeicons arrow.
**Cost** — 3.7 KB gzip plus motion and two Hugeicons packages; SVG band/arc plus one span per particle; rAF only while dragging or settling. Client-only.
**Fit for ARKRETE** — No fit. A slingshot on the enquiry CTA reads as a game, and the contact page already ends in a plain submit.
**Verdict** — skip — play physics on the one button that should feel like a handshake.
