# TextType
**Registry**: `TextType-TS-TW` · **Deps**: `gsap@^3.13.0` · **Files**: `TextType/TextType.tsx`
**What it does** — Types one or more sentences character by character behind a blinking caret, pauses, deletes and moves to the next. It can plant deliberate typos and animate each new character with a fade, blur or rise.
**Props**
- `text` (string | string[], required) — one sentence, or a list to cycle.
- `typingSpeed` / `deletingSpeed` (number, `50` / `30`) — ms per character in each direction.
- `pauseDuration` (number, `2000`) — hold time on a finished sentence.
- `loop` (boolean, `true`) — start over after the list ends.
- `showCursor` (boolean, `true`) + `cursorStyle` (`character` | `bar` | `block` | `underscore`, `character`).
- `mistakes` (number, `0`) — probability of typing a neighbouring key and correcting it.
- `typeEffect` (`none` | `fade` | `blur` | `rise`, `none`) — per-character entrance.
- `startOnVisible` (boolean, `false`) — waits for the element to scroll into view.
**Motion** — A `setTimeout` cadence per character, not a frame loop; GSAP drives the caret blink and its glide from the end of one line to the start of the next. `startOnVisible` uses an IntersectionObserver. Reduced motion sets the whole string at once and kills the blink and the character effects.
**Cost** — GSAP is a hard dependency and is used only for a blinking caret and a small glide — ~23 KB gzip for two tweens on a site that has no GSAP. One span per visible character plus the caret; the full sentence is duplicated in an sr-only span so prerender and crawlers get it. Effectively client-only.
**Fit for ARKRETE** — no fit. Every heading is a fixed statement, and the one place copy appears in response to an action — the contact confirmation — has to be instant.
**Verdict** — skip — a typewriter delays reading and drags in GSAP for a caret.
