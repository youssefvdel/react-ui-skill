# PulseHeart
**Registry**: `PulseHeart-TS-TW` · **Deps**: `@hugeicons/core-free-icons` · **Files**: `PulseHeart/PulseHeart.tsx`
**What it does** — A pill-shaped like button: on click the icon shrinks to a dot, flips from grey outline to filled colour, springs back with a beat, and the count digit rolls to its new value. Heart, star and thumb glyphs ship with it.
**Props** — `liked` / `defaultLiked` (boolean) — controlled or uncontrolled; `count` (number, 0) — displayed total; `onChange` (liked, count) — fires once the swap commits; `showCount` (boolean, true); `icon` ('heart' | 'star' | 'thumb' | ReactNode, 'heart'); `size` (number, 40) — pill scale in px; `likedColor` (string, '#ff4d6d'); `duration` (number, 560) — pulse length in ms.
**Motion** — Click-triggered only: an rAF timeline scales the glyph down to `dotSize` and back with a back-out overshoot, compresses the pill by `beat` percent, and flips `data-liked` at the midpoint so the colour transition lands with the pop; the changed digit rolls on a CSS transform. Keyboard activation skips the animation, and reduced motion commits instantly.
**Cost** — One icon package for three glyphs, about 3.8 KB gzip of source, a handful of spans, no canvas. SSR-safe; the button prerenders with `aria-pressed`, a disabled state and an sr-only label.
**Fit for ARKRETE** — No fit. Nothing on the site is liked or counted, and a like pill would put the only number on a page that deliberately has no stat rows.
**Verdict** — skip — a social gesture with no place in an inquiry-driven site.
