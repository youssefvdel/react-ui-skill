# GradientASCII

**Registry**: `GradientASCII-TS-TW` · **Deps**: none · **Files**: `GradientASCII/GradientASCII.tsx`

**What it does** — Fills a panel with monospace ASCII glyphs whose density follows a soft gradient shape (horizon, pinch, rise or eclipse) in a blue-to-ice ramp. Moving the cursor scrambles glyphs along a 24-point trail and a click sends a wave or burst through them; it reads as a lit CRT, not a photograph.

**Props** — `shape` ('horizon' | 'pinch' | 'rise' | 'eclipse', 'horizon') — gradient silhouette; `colors` (string[], blue/ice ramp) — colour stops; `characters` (' =+xX0S8#@') — glyph ramp from dark to light; `cellSize` (18) — glyph grid in px; `density` (0.8) — share of cells drawn; `glow` (0.2) — halo blur strength; `mouseInteraction` (true) — scramble trail; `intro` (true) — 2.4 s reveal.

**Motion** — All WebGL2: a field pass writes colour plus reveal/scramble into two attachments, a quarter-res glyph pass makes a halo, two blurs, then a composite. Time drives the drift; pointer trail and click wave/burst are extra uniforms. No GSAP, Framer Motion or three.js; reduced motion freezes time, flicker and the intro.

**Cost** — 916 lines, 9.4 KB gzip of source, zero npm deps, but four shader programs and three framebuffers (half-res field, quarter-res halo pair) plus a glyph atlas regenerated whenever the font or character set changes. Full-screen fragment work every visible frame; an IntersectionObserver stops it off-screen. No WebGL2 means an empty box. Client-only.

**Fit for ARKRETE** — no fit. ASCII is a technology signal; even on services it would be a second accent laid over the five trades.

**Verdict** — skip — a full multi-pass renderer for a glyph texture that says "terminal", not "interior".
