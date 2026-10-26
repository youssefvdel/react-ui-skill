# MagicBento
**Registry**: `MagicBento-TS-TW` · **Deps**: `@hugeicons/react@^1.1.10`, `@hugeicons/core-free-icons@^4.3.3` · **Files**: `MagicBento/MagicBento.tsx`
**What it does** — A bento grid of feature cards pre-filled with small product visuals — an area chart, a bar chart, a document with a highlighted selection, a moving cursor — plus an edge light that follows the pointer and a click wave across the grid.
**Props** — `items` (MagicBentoItem[], six demo cards) — content, spans, image, link or custom visual; `columns` (4), `rowHeight` (px, 200), `gap` (12) — grid metrics; `theme` (`dark|light`, dark); `glowColor` (hex, ink) — edge and particle tint; `enableSpotlight` (true) with `spotlightRadius` (300); `enableTilt` / `enableMagnetism` (off) — card 3D and cursor pull; `clickEffect` (true) — radial wave; `enableStars` (off) + `particleCount` (24) — canvas particles.
**Motion** — Per-card springs for tilt, magnet offset and press scale, a radial border highlight tracking the cursor, a click wave that re-triggers card animations, and optional twinkling particles. DOM, CSS and Canvas 2D; no animation library.
**Cost** — ~59 KB source, ~15.1 KB gzip plus two Hugeicons packages; per-card rAF, one 2D canvas per card when stars are on, and `getAnimations()` replays. Client-only engine; markup prerenders but the visuals depend on JS.
**Fit for ARKRETE** — no fit. Its native content is dashboards, metrics and product UI — the stat-row, explanatory register the site rejects.
**Verdict** — skip — a SaaS feature grid with charts, for a firm whose argument is rooms.
