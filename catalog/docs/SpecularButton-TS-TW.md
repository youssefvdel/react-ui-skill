# SpecularButton
**Registry**: `SpecularButton-TS-TW` · **Deps**: none · **Files**: `SpecularButton/SpecularButton.tsx`
**What it does** — A button whose 1 px rim carries a moving specular highlight: a faint lit arc at rest that brightens and slides around the perimeter as the cursor nears, flaring on press. The face is a translucent tint with the label above the canvas.
**Props** — `lineColor` (#ffffff) the rim light · `baseColor` (#525252) unlit hairline · `idleIntensity` (0.35) resting rim brightness · `intensity` (1) lit peak · `followMouse` (true) light tracks the cursor · `proximity` (250 px) pull radius · `shineSize` / `shineFade` (10 / 34) arc length and falloff · `autoAnimate` (false) perpetual orbit.
**Motion** — The highlight eases toward the nearest point on the rounded-rect perimeter each frame, brightness follows pointer distance, press flare decays over ~200 ms; the loop parks when settled. Reduced motion only turns off `autoAnimate`, so hover still moves — gate `followMouse` yourself. WebGL2, no library.
**Cost** — 4.4 KB gzip, no dependencies. One WebGL2 context per button, canvas 48 px wider and taller than the button, DPR capped at 3, idle rAF stopped. Client-only; prerender shows the plain tinted button and label, which is a fine fallback.
**Fit for ARKRETE** — The single brass action: the "Send inquiry" submit at the end of the contact form's three steps. One instance, nowhere in the nav.
**Verdict** — adapt — brass `lineColor`, `tintOpacity` 0, `glow` ~0.4, `autoAnimate` false; or port the rim maths to a conic-gradient mask and drop the GL context.
