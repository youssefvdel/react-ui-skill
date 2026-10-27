# Vendoring a React Bits component

Installing a component means dropping the author's demo into your site. Vendoring
means keeping what the component *does* and replacing how it looks, so the site
stays the site. Do this whenever the project has a design language — a palette,
a type system, a corner radius, or an opinion about cards.

## The five edits, in order

1. **Kill the wrapper.** Most components ship a rounded, bordered, glassy or
   gradient-filled container with its own padding. That container is the demo's
   frame, not the component. Delete it and let the parent section own spacing,
   background and borders — the site's hairlines, not the library's 32 px radius.

2. **Rebind colour to tokens.** Every literal (`#fff`, `rgba(255,255,255,.1)`,
   `#8b5cf6`) becomes the project's own variable — `var(--color-ink)`,
   `var(--color-line)`, `var(--color-accent)`. A component that keeps its
   palette is a second brand on the page. If a component's identity *is* its
   colour ramp (colour-bends backgrounds), it does not belong on a site with one
   accent.

3. **Cut the dependency, or keep it deliberately.** Many components reach for
   GSAP, `motion`, `three` or `ogl` to do something a browser primitive already
   does: a rAF loop, `IntersectionObserver`, a CSS transition, a `pointermove`
   handler. Rewrite the mechanism in plain React and the component's cost
   collapses — the accordion in the worked example went from a GSAP timeline to
   measured `panel.animate()` calls with no dependency at all. When the
   dependency is genuinely required (WebGL), keep it and code-split the
   component; never let it into the initial bundle.

4. **Give it a reduced-motion branch.** Components almost never ship one. The
   branch must show the **end state**, not a broken half state: no scale, no
   auto-sweep, no parallax, and content visible. A component whose resting state
   is `opacity: 0` and whose only path to visible is an animation is a blank
   section for anyone who asks for less motion.

5. **Make it operable.** Anything clickable becomes a `<button>` (not a `div`
   with `role="button"` inside a list item — that removes the item from the
   list), gets `aria-current`/`aria-expanded` where it acts as a control, a
   24×24 minimum hit area (44×44 on touch), and keyboard handling that matches
   the pointer behaviour.

## The traps that actually bit

- **Layout shift from animated widths.** Animating `width` re-lays-out every
  frame and the copy inside moves with it: 0.12 CLS on first paint, before the
  visitor touched anything. Animate `opacity` and `transform` instead; a row
  that reveals with a fade and an 18 px rise costs no layout and measures 0.000.
- **Scroll-tripped hovers.** A wide panel with `onMouseEnter` fires as the page
  scrolls under a stationary cursor, opening several panels in a row. Guard on
  the gesture, not a timer: the pointer must have moved recently *and* the page
  must not have scrolled recently.
- **`visibility: hidden` hides pseudo-elements.** If you hide a wrapper to
  measure or screenshot the background behind type, hide its children instead —
  a `::before` scrim disappears with the wrapper and the measurement becomes
  fiction.
- **Module-scope browser access.** `window.matchMedia` at import time, a GL
  context created at module scope, `document` in a top-level initialiser: all
  of them break static prerendering. Move them into `useEffect`.
- **Text over photography.** Cream type on a bright wall measured 2.59:1 in the
  worked example. A gradient band under the type raised it to 8.18:1 median
  without flattening the photograph — measure the pixels the letters sit on, not
  the token's nominal colour.
- **The demo's own CSS.** Components that ship a `.css` file bring class names
  that collide with a design system. Port the styles into the project's
  stylesheet under the project's own naming, or scope them.

## Checklist before it merges

- [ ] No literal colours; everything is a token
- [ ] No new dependency unless it is code-split and justified
- [ ] `prefers-reduced-motion` shows the end state
- [ ] Keyboard reaches every control; focus is visible
- [ ] Hit areas ≥ 24×24 (44×44 touch)
- [ ] No layout shift at load (measure CLS, not by eye)
- [ ] Prerender passes with JS disabled: the section still reads
- [ ] Screenshot at 1440 and 390, in both motion modes

## What actually broke when eight were ported into a live site

Evidence from one real integration (dark, photography-led marketing site, eight
components across five pages). Every one of these was caught by a measurement,
not by reading the code back.

- **`aria-hidden` on the wrapper silently removes the label.** A decorative
  wrapper that contains the button's text must not be hidden from assistive
  technology — the link then has no accessible name. The axe rule is
  `link-name`, and it fires on the *link*, not the wrapper, so it reads as if the
  button were empty.
- **A clipped-background heading needs a visible fallback.** `background-clip:
  text` with `color: transparent` is invisible until the image decodes. If the
  decode fails, the heading is blank. Start with plain ink and switch the fill on
  once `img.decode()` resolves.
- **A frame with a fixed height needs its children to fill it.** An image inside
  a `height: 62svh` frame keeps its own aspect ratio and leaves a black bar under
  itself on a phone. `.frame > * { height: 100% }` — the wrapper is part of the
  layout, not a bystander.
- **Marquees need an edge mask, not an overflow.** A word sliced by the frame
  reads as a bug; a two-line `mask-image` fade reads as motion. It is also one
  line of CSS.
- **Element-level screenshots fight scroll-hijacking layouts.** On a page with a
  custom scroll stack, `scrollIntoViewIfNeeded` + element screenshot closed the
  browser repeatedly. Take a viewport screenshot instead, or the crash reads as a
  bug in the component.
- **Headless Chromium on SwiftShader dies after ~20 WebGL demos.** Restart the
  browser every N pages and make the capture resumable, or the second half of the
  survey silently does not exist.
- **Masked type only works at display size.** At 2rem the photograph inside the
  letters is a faint gradient; at 4.6rem it is a photograph. If the effect has to
  justify itself, give it the size it needs or drop it.

- **A divider that hides a seam is not a fix.** The marquee band sat between the
  hero and the next section, so nobody saw that the hero photograph ended on a
  hard cut. Removing the band exposed it; a 12vh bottom fade into the ground is
  the actual fix. When a decorative element is deleted, look at what it was
  covering.
- **Effects that draw over a photograph while it loads are the first thing to
  cut.** A mosaic grid that "resolves" into the image reads as a slow load to
  everyone who did not build it. `loading=lazy` + a correct srcset is the whole
  feature.

## GSAP components on a prerendered site

- **Load GSAP dynamically, once.** `gsap` + `ScrollTrigger` is ~44 KB gzip. A
  static `import` bills it to first paint; a promise that both components share
  puts it in the deferred chunk. Initial budget: unchanged.
- **Apply the from-state from JS, never from CSS.** The scroll-reveal a GSAP
  component replaces usually lives in a stylesheet as `opacity: 0` plus an
  observer class. That is the fragile version: a thrown bundle leaves the content
  invisible. `gsap.set()` inside the effect can only animate something that was
  already visible.
- **A scrub timeline's first piece finishes early.** With `stagger` on a scrub
  timeline, total duration is `1 + maxDelay`, so sampler code that checks
  `pieces[0]` reports "already settled" at 60% progress. Sample the middle piece
  when verifying, and walk the scroll in steps rather than jumping to one offset.
- **`back.out` overshoots scale.** On a piece rising from `scaleY: 2.1`, a back
  ease drives it *under* 1 for a few frames — a visible squash. `power2.out` keeps
  the settle monotonic.
- **Clamp a stagger over long lists.** `stagger: 0.08` across forty children is
  still arriving three seconds later. A function stagger with
  `Math.min(i * each, 0.4)` lands as a wave instead of a queue.
- **Splitting text creates an accessibility bug in two directions.** Hide the
  pieces from AT and give the heading one `sr-only` copy of the sentence — do not
  put `aria-label` on the element and leave the characters readable as well.

## Two edits that only fail in the accessibility tree

- A control with `aria-label="Jump to room 1"` showing the text `01` trips
  axe's `label-content-name-mismatch`: the visible text must appear in the
  accessible name. Add the words beside the number instead of replacing it.
- `background-clip: text` with `color: transparent` is invisible in forced-colors
  and in any engine without the property. Guard with
  `@media (forced-colors: active)` and `@supports not (background-clip: text)`.
