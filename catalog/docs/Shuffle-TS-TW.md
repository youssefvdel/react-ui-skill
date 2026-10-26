# Shuffle

**Registry**: `Shuffle-TS-TW` · **Deps**: gsap@^3.13.0, @gsap/react@^2.1.2 · **Files**: `Shuffle/Shuffle.tsx`

**What it does** — On scroll or hover, the letters of a heading leave their positions, shuffle through random glyphs and slide back into the sentence; colour can cross-fade during the shuffle.

**Props** — `text` — the line to animate; `tag` ('p') — rendered element; `shuffleDirection` ('right') — travel direction; `duration` (.35) — seconds per character; `shuffleTimes` (1) — number of reshuffles; `animationMode` ('evenodd' | 'sequence' | 'center' | 'random') — character order; `stagger` (.03) — seconds between characters; `effect` ('slide' | 'flip' | 'blur') — how each glyph moves.

**Motion** — GSAP `SplitText` breaks the line into characters, then a timeline moves each one out and back while swapping in scramble characters; `ScrollTrigger` starts it at `threshold` / `rootMargin`, and a pointer-radius hover can replay it. Reduced motion leaves the text untouched.

**Cost** — 703 lines, 6.3 KB gzip, plus GSAP core, ScrollTrigger, SplitText and `@gsap/react` — roughly 40–50 KB gzip. A span per character plus word and line wrappers, rebuilt on every text or prop change after `document.fonts.ready`. Client-only splitting; prerender shows plain text.

**Fit for ARKRETE** — no fit. A heading that scrambles is theatre; the site's type should arrive like a caption, not a slot machine.

**Verdict** — skip — half the JS budget for a party trick on a five-word heading.
