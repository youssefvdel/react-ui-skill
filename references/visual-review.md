# Visual review — 216 React Bits demos, looked at

The written catalogue judged components from their source. This is the other
half: every demo was photographed from reactbits.dev (`.preview-stage`, 1280×900,
2.2 s after load so the animation had started), tiled into 14 contact sheets and
reviewed by looking at them.

Coverage: **216 of 217** mapped components. `EvilEye` has no demo page on the
site; everything else has a capture. 14 of them failed the first pass when
headless Chromium died mid-run (SwiftShader, ~20 WebGL demos per browser) and
were captured by a resumable retry.

## What looking changed

Six things the source docs had ranked as usable looked wrong in pixels, and four
things the docs had dismissed looked right:

| Component | Docs said | Pixels said |
| --- | --- | --- |
| BlurText | adapt — text reveal | a complete hero headline with three buttons; the mechanism is the reveal, the rest is demo furniture |
| CircularGallery | adapt | a curved wall of photographs — the strongest gallery in the library, and a third gallery mechanism on a site that already has two |
| MaskedHeading | adapt, gsap, 703 lines | letters filled with a photograph. The single best fit for a photography-led site; ported without gsap |
| ScrollExpand | adapt | a plate that opens to full bleed. Exactly what a project hero wants |
| BorderGlow | adapt | a glowing card — the thing the client had just removed from the site |
| SpotlightCard | adapt | same rounded card with a brass spotlight; rejected twice for the same reason |
| DomeGallery | (no strong opinion) | a fisheye dome of tiles: spectacular, and unusable behind a headline |
| TextPressure | reject | genuinely striking, but it is a variable-font playground, not a heading |

## The eight that shipped

| Component | Where | Why it survived |
| --- | --- | --- |
| Magnet | Home hero action, project tender action | pulls only on the one primary action; the rest of the page stays still |
| ScrollVelocity | between hero and reel | one line of words as a threshold; speed follows the scroll |
| MaskedHeading | About statement | the photograph is inside the letters — the only place on the site where type is large enough to carry it |
| HalftoneReveal | About founder photograph | a printed dot screen that lifts once, then never again |
| RefineFrame | Projects plates | arrives as a grid, settles into the photograph |
| ScrollExpand | Project detail hero | the room opens from 64% to full bleed across the section's own travel |
| SpecularButton | Project tender action | brass catches the light under the pointer |
| ParticleText | 404 | the words assemble from dust, once, then the canvas leaves |

## Rejected on sight, though the docs allowed them

- **CardNav / BubbleMenu / GooeyNav** — pill navigation. The site has a wordmark
  and four links; a floating pill would be a second chrome system.
- **CircularCarousel / DomeGallery / DepthCarousel / OrbitImages** — four more
  gallery mechanisms against a home reel that already does this better.
- **ImageTrail / SwarmCursor / GhostCursor / GlowCursor** — cursor theatre. It
  does not survive a trackpad, a tablet, or a client on a laptop in a meeting.
- **Anything with a colour ramp** (ColorBends, Prism, LiquidEther, Hyperspeed,
  PlasmaWave, Threads, WebThreads) — a second brand colour, which this site
  refuses by rule.
- **Anything that needs content the firm does not have** (CountUp stat rows,
  Masonry of stock photography, Testimonial-style walls).

## The method, if it is run again

1. Map registry names to demo URLs by kebab-casing the name and matching the last
   path segment of the sitemap (217/218 resolved).
2. Screenshot `.preview-stage` per page, 2.2 s after `domcontentloaded`; restart
   the browser every 25 pages and skip files that already exist.
3. Tile 16 per sheet at 440×190 with the component name under each cell.
4. Ask for a compact table — renders / look / fit — plus the three best for the
   site. Anything longer is a paragraph nobody re-reads.
