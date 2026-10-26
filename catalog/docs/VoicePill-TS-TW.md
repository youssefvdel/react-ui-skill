# VoicePill

**Registry**: `VoicePill-TS-TW` · **Deps**: `@hugeicons/react@^1.1.10`, `@hugeicons/core-free-icons@^4.3.3` · **Files**: `VoicePill/VoicePill.tsx`

**What it does** — A 28 px mic button that opens into a capsule with a live canvas equalizer and a running timer while recording; drag left past 64 px to cancel, release to stop. With `reactive="mic"` it reads the real microphone through an `AnalyserNode`, otherwise it plays a canned syllable envelope.

**Props** — `size` / `shape` (number, 28 / 'pill' | 'rounded') — button size and corner treatment; `mode` ('auto' | 'hold' | 'toggle', 'auto') — whether a tap latches or a press must be held; `reactive` ('simulated' | 'mic', 'simulated') — canned waveform or real microphone; `showTime` / `waveform` (boolean, true / true) — timer and canvas bars; `slideToCancel` / `cancelDistance` (boolean, true / number, 64) — drag-left cancel and its threshold; `attack` / `release` (number, 40 / 240) — envelope times in ms; `accentColor` / `background` (string, '#f5f5f5' / '#27272a') — capsule and icon colours; `onStart` / `onStop` (callback) — recording lifecycle with stop reason and duration.

**Motion** — The capsule's background clip-path opens leftward over 200 ms; the mic icon blurs and scales into a stop square; a 2D canvas draws an 80-sample scrolling equalizer at 60 fps while recording; dragging translates the pill and fades in a "Cancel" row. CSS transitions plus a RAF canvas, no animation library.

**Cost** — Two Hugeicons packages, tree-shaken down to the mic and arrow icons, about 19 KB source (~6 KB gzip), canvas and RAF only while recording, plus `AudioContext` and a `getUserMedia` permission prompt in mic mode. Client-only: pointer capture, audio hardware, and a permission gate.

**Fit for ARKRETE** — No fit. The contact form is a written inquiry; a mic permission prompt is a trust cost on a contractor's page and there is no voice-note pipeline behind it.

**Verdict** — skip — a voice-recording affordance with no job on a typed inquiry form.
