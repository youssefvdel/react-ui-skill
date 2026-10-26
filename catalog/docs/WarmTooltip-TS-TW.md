# WarmTooltip

**Registry**: `WarmTooltip-TS-TW` · **Deps**: `react-dom@^19.0.0`, `motion@^12.23.12` · **Files**: `WarmTooltip/WarmTooltip.tsx`

**What it does** — A tooltip group where the first label waits 400 ms, then sibling labels open instantly while the group is "warm" and the tooltip springs from one trigger to the next. Labels portal to the body, follow their trigger on scroll, and can show a keyboard-shortcut chip.

**Props** — `content` (ReactNode) — the label; `side` ('top' | 'bottom' | 'left' | 'right', 'top') — placement and arrow origin; `delay` / `warmWindow` (number, 400 / 300) — cold wait and how long siblings stay instant; `size` ('sm' | 'md' | 'lg', 'md') — 11.5–13.5 px preset; `surfaceColor` / `inkColor` (string, '#f5f5f5' / '#18181b') — plate and text; `gap` / `radius` / `arrow` (number, 8 / 8 / true) — spacing, corner, arrow; `popDuration` / `popScale` / `popBlur` (number, 160 / 0.94 / 4) — cold-open pop; `longPress` / `showFuse` (number, 500 / false) — touch hold and a progress fuse.

**Motion** — Cold opens pop from 0.94 scale with a 4 px blur over 160 ms; warm swaps slide 10 px and blur out the old label; the whole plate travels between triggers on a 320 ms spring with the arrow tracking the anchor, and optional `lean` rotates it with pointer velocity. Hover, focus, touch long-press, and Escape; needs `motion` plus a react-dom portal.

**Cost** — `motion@^12` plus react-dom, about 25 KB source (~7 KB gzip before the motion runtime); one portal node and a global scroll/resize listener while open, plus per-trigger timers. Trigger markup prerenders; the overlay is client-only.

**Fit for ARKRETE** — No fit. Header and footer are text links with visible labels, and hiding an office address behind hover on contact would cost the reader a discovery rather than save space.

**Verdict** — skip — a motion-heavy tooltip system for a site with no icon-only controls.
