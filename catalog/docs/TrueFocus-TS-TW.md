# TrueFocus
**Registry**: `TrueFocus-TS-TW` · **Deps**: `motion@^12.23.12` · **Files**: `TrueFocus/TrueFocus.tsx`
**What it does** — Splits a sentence into words, keeps one sharp and blurs the rest, and walks a bracket, box, underline or highlight frame from word to word on a timer. Hovering a word takes over when `manualMode` is on.
**Props**
- `sentence` (string, `"True Focus"`) — the words to cycle.
- `focusStyle` (`brackets` | `box` | `underline` | `highlight`, `brackets`) — the frame.
- `blurAmount` (number, `5`) — blur on the inactive words, in px.
- `animationDuration` / `pauseBetweenAnimations` (number, `0.5` / `1`) — dwell and travel.
- `manualMode` (boolean, `false`) — hover instead of the automatic timer.
- `order` (`sequential` | `random`, `sequential`) — cycle order.
- `borderColor` / `glowColor` (CSS colour, `green` / transparent) — frame colour.
- `focusScale` (number, `1`) — size of the focused word.
**Motion** — A `setInterval` advances the active word; motion/react springs or eases the frame rectangle while CSS transitions filter, opacity and scale on every word. Reduced motion sets duration to 0 and drops the spring, so the frame jumps.
**Cost** — motion for the frame; ~8 KB source / 2.5 KB gzip plus the runtime. A blur filter on each word creates a composited layer per word, sizes are hardcoded at `3rem font-black`, so it only works as display type. The prerendered HTML shows the sentence blurred around word one until hydration.
**Fit for ARKRETE** — no fit. The site never shows one word of a sentence at a time, and a camera-focus bracket is a metaphor with no meaning for a fit-out firm; the default green is a second accent.
**Verdict** — skip — a hero gadget that hides copy and adds a motion runtime for a frame.
