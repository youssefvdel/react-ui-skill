# SlideCommit
**Registry**: `SlideCommit-TS-TW` · **Deps**: motion, @hugeicons/react, @hugeicons/core-free-icons · **Files**: `SlideCommit/SlideCommit.tsx`
**What it does** — A pill track with a round handle you drag to the far end; crossing it commits the action. While a promise resolves the handle turns into a spinner, then the capsule unfurls into a tick pill reading the done label.
**Props** — `label` ("Slide to pay") prompt text · `onConfirm` (() => void | Promise) awaited, drives pending/done/error · `doneLabel` / `errorLabel` result copy · `width` (280) / `height` (56) track size · `speed` (50) maps to spring stiffness 260–900 · `holdMs` (1500) how long the done pill stays · `disabled` (false).
**Motion** — Handle tracks the pointer and squashes past its left edge, springs home on release with the release velocity, the capsule unfurls by `clip-path`, errors shake the track. Reduced motion swaps springs for 0.2 s tweens and skips the dip. Needs motion; keyboard is real (role=slider, arrows step, End commits, Escape returns).
**Cost** — 3.8 KB gzip of its own code, plus `motion` (roughly 30 KB gzip of runtime, not installed here) and two Hugeicons packages imported for two glyphs. Client-only.
**Fit for ARKRETE** — Argued for the contact form's "Send inquiry" button, and rejected: sending an inquiry is neither destructive nor irreversible.
**Verdict** — skip — friction on the site's single conversion, three dependencies for one control.
