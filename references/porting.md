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
