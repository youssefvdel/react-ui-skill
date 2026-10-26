# Ribbons
**Registry**: `Ribbons-TS-TW` · **Deps**: none · **Files**: `Ribbons/Ribbons.tsx`
**What it does** — Three coloured ribbons trail the cursor across a transparent canvas, each a fifty-point spring chain drawn as a tapered strip in lens, comet or even width profiles, with an optional travelling wave along its length.
**Props** — `colors` (string[], indigo trio `#3847ff` / `#7c84ff` / `#c7cbff`); `thickness` (number, 30) — base width in px; `length` (number, 1.4) — chain length multiplier; `spread` (number, 18) — start offset; `stiffness` (number, 0.5) and `bounce` (number, 0.5) — spring feel; `shape` ('lens' | 'comet' | 'even', 'lens'); `wave` (number, 0) — ripple along the ribbon.
**Motion** — Pointer-driven spring physics integrated at a fixed 120 Hz step, then each spine expanded into a GPU triangle strip with soft edges; it only draws while the pointer moves or the canvas is visible. WebGL2. There is no `prefers-reduced-motion` branch at all, so the ribbons keep trailing the cursor.
**Cost** — No dependencies, about 5.1 KB gzip of source, three draw calls, 150 simulated points total. Client-only and `pointer-events-none`, so it never blocks clicks, but adopting it means adding the reduced-motion check and a static frame yourself.
**Fit for ARKRETE** — No fit. Cursor ribbons are coloured decoration laid over the photography, and three blues would read as a second accent.
**Verdict** — skip — playful and off-brand, and it fails the calm-static-state rule out of the box.
