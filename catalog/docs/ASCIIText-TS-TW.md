# ASCIIText
**Registry**: `ASCIIText-TS-TW` · **Deps**: none · **Files**: `ASCIIText/ASCIIText.tsx`
**What it does** — Draws a word as a field of monospace glyphs on a WebGL2 canvas, picking each character from an ASCII brightness ramp, so the type reads as a living halftone. It leans in 3D toward the pointer, scrambles glyphs around the cursor, ripples outward on click, and decodes from solid blocks into characters on first paint.
**Props**
- `text` (string, `'Hey!'`) — the word rasterised; also the only accessible name.
- `asciiFontSize` (number, 8) — glyph cell height in CSS px; smaller is denser and costlier.
- `charset` (string, ` .'`^",:;Il!…@$` ramp) — characters sampled for luminance.
- `colors` (string[], pink/orange/yellow) — three-stop tint across the frame.
- `blocks` (number, 0.9) — how much solid letterform survives under the glyphs.
- `scramble` (number, 0.6) — radius of pointer glyph noise; `clickRipple` adds the ring.
- `tilt` (number, 1) — how far the text plane leans at the pointer, or idles.
- `theme` ('dark' | 'light', 'dark') — inverts the composite.
**Motion** — Every frame is one fragment shader: sine waves displace the text plane, the pointer lerps tilt and hue over ~0.3s, a click pushes one of four expanding ripple rings, and an intro decodes glyphs over 1.4s. WebGL2 only — no GSAP, Framer Motion or three.js. Reduced motion freezes the clock and skips the intro but still rasterises frames; without WebGL2 it falls back to a plain text div.
**Cost** — 6 KB gzip of source, no dependencies. One full-screen fragment shader doing a glyph-atlas lookup per pixel at an 8 px cell and DPR up to 2, two textures re-uploaded when the font loads, rAF parked by IntersectionObserver when scrolled out but never idle while visible. Client-only: prerender emits an empty positioned div, the text exists only in `aria-label`, so it must be lazy-loaded and given a sized parent.
**Fit for ARKRETE** — no fit. Home's monument wordmark is a drawn SVG (LiveMark); an ASCII raster would replace the one exact mark on the site with a pixel effect, and the pink/orange/yellow ramp is three accents against brass.
**Verdict** — skip — a full-screen shader whose only job is making the wordmark less legible.
