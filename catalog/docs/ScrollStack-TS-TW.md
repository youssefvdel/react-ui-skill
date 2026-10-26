# ScrollStack

**Registry**: `ScrollStack-TS-TW` · **Deps**: none · **Files**: `ScrollStack/ScrollStack.tsx`

**What it does** — Cards pin one under another as you scroll; each arriving card pushes the ones above it deeper, scaling, dimming and tilting them back into a deck. When the last card has covered the stack the deck holds, then releases.

**Props** — `itemDistance` (100) — px of scroll between cards; `itemStackDistance` (24) — px each pinned card steps down; `stackPosition` ('15%') — pin line from the top of the viewport; `baseScale` (0.8) — floor a buried card can shrink to; `itemScale` (0.05) — extra shrink per card of depth; `dimAmount` (0.2) — black overlay per depth; `smoothScroll` (true) — wheel glide that takes over native scroll; `snap` (false) — settle to the nearest card after 140 ms.

**Motion** — Sticky slots handle the pinning; a rAF loop reads each card's position and writes `transform` (scale, `rotateX` lean, alternating rotation) and a `--scroll-stack-dim` property only when values change. No GSAP, Motion or three.js. Reduced motion kills the wheel glide and snap but keeps the scroll-linked scale and dim, so the deck still reads.

**Cost** — 392 lines, 3.9 KB gzip, zero deps. One sticky wrapper plus spacer per card; each scroll frame reads `offsetHeight` and `getBoundingClientRect` per card, fine for six rooms, not fifty. `useLayoutEffect` means the server ships a plain stack and measurements start after hydration; the dim property is only consumed by the bundled `ScrollStackItem`, so custom children need their own overlay.

**Fit for ARKRETE** — Projects, the scroll stack of rooms: this is that mechanic already built, with depth, dim and hold tuned.

**Verdict** — adapt — right engine, but strip the white card, 320 px height and shadow, and turn `smoothScroll` off so the page keeps native scrolling.
