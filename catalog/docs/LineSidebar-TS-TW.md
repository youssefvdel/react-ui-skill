# LineSidebar
**Registry**: `LineSidebar-TS-TW` · **Deps**: none · **Files**: `LineSidebar/LineSidebar.tsx`
**What it does** — A vertical text list where items near the cursor slide right, warm to the accent colour and grow a tick mark; clicking an item makes it the active one and fires a callback.
**Props** — `items` (string[], twelve demo labels) — the list; `accentColor` (string, `#A855F7`) — proximity colour; `showIndex` (bool, true) — 01/02 numerals; `showMarker` (bool, true) — left rule and tick per item; `proximityRadius` (px, 100) — hover reach; `maxShift` (px, 30) — slide distance; `falloff` (`linear|smooth|sharp`, smooth) — proximity curve; `onItemClick` (fn) — selection callback.
**Motion** — Pointer proximity only: one rAF loop eases a `--effect` custom property per item over ~100 ms, and that single value drives colour mix, translateX, tick scale and index opacity. Plain CSS variables and JS; no animation library.
**Cost** — ~7 KB source, ~2.5 KB gzip, no dependencies; a list of text nodes, one rAF that stops as soon as values settle. Prerenders as a static list — all browser reads happen in pointer handlers. Reduced motion is not handled, so the shift would need to be disabled by hand.
**Fit for ARKRETE** — services page, a left rail beside the five trades: numerals off, marker in brass, `maxShift` ~10, so it reads as an index rather than a toy.
**Verdict** — adapt — a real navigation with no dependency; drop the mono numerals, the purple default and the 30 px slide.
