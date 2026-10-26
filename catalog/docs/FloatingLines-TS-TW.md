# FloatingLines
**Registry**: `FloatingLines-TS-TW` · **Deps**: none · **Files**: FloatingLines/FloatingLines.tsx
**What it does** — Draws fine glowing lines in three wave bands that drift and curl across a dark canvas, fading at the edges with depth blur. The pointer bends the lines aside and a click sends a swirl through them.
**Props** — `linesGradient` (string[], ['#e945f5', '#ffffff']) — the colour ramp along each line; `enabledWaves` (('top' | 'middle' | 'bottom')[], all three) — which bands draw; `lineCount` (number | number[], 10) — lines per band; `lineDistance` (number | number[], 6) — pixels between them; `amplitude` (number, 1) — wave height; `glow` (number, 1) — bloom around each line; `interactive` (boolean, true) — cursor bend; `clickSwirl` (boolean, true) — vortex on click.
**Motion** — A custom WebGL line shader: the wave phase advances with time, the pointer adds a spring-damped bend within `bendRadius`, and clicks add decaying vortices. The loop pauses offscreen and on hidden tabs; reduced motion freezes time and switches off the pointer response.
**Cost** — 24 KB of source (about 7 KB gzip), no dependencies, one full-screen pass at DPR up to 2 — cheap per frame for a shader, but still a permanent render loop wherever it sits, and it has no static fallback beyond the frozen first frame. Client-only.
**Fit for ARKRETE** — no fit — a magenta line field behind the contact form is decoration with no job, and a second accent.
**Verdict** — skip — pretty, weightless, and says nothing about rooms.
