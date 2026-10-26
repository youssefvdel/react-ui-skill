# Catalogue — 218 React Bits components, judged

A worked example. The site this was judged for is a dark, photography-led marketing
site for an interior fit-out contractor: one accent (brass), hairlines instead of
cards, a 150 KB gzip JS budget, static prerendering, and an explicit refusal of stat
rows, second accents and decorative motion.

**Adopt 1 · adapt 26 · skip 191** — from 218 components.

The point of publishing this is not the verdicts: it is that a verdict without a
reason is a preference. Every row names the work it would have to displace.


## Adopted

| Component | Registry | Deps | Why it earned a section |
| :-- | :-- | :-- | :-- |
| **GlareHover** | `GlareHover-TS-TW` | none | Contact, the single brass "Send inquiry" button: a `sheen` pass at low opacity reads as the metal catching light, and it only exists on the one action… |
| **BlurText** | `BlurText-TS-TW` | motion | Services, the five trade headings; About, the opening line of the firm paragraph — one reveal per viewport, never the hero. |
| **BounceCards** | `BounceCards-TS-TW` | none | About, the "its trades" section: five cards as material samples that sit fanned on the table and open on hover, each linking into services. |
| **DepthText** | `DepthText-TS-TW` | none | Home, on the monument wordmark: six to ten layers, `depth` near 0.8, `autoOrbit` off, `depthColor` a bone-on-black step, `tilt` under 4. |
| **DriftWall** | `DriftWall-TS-TW` | none | projects, a full-bleed band under the room stack, at `speed` 10 rather than 42, `dim` 0.25, `grayscale` off, `pauseOnHover` true, and a flat two-row g… |
| **EchoText** | `EchoText-TS-TW` | none | home, the monument wordmark: `mode="entrance"`, 3 echoes, `offset` 10, `blur` 0, `tint={false}`, 700 ms, then still. The pointer trail is not invited. |
| **FadeContent** | `FadeContent-TS-TW` | gsap | Home, the caption under each of the six rooms in the reel; About, the why-it paragraphs. |
| **FlipCard** | `FlipCard-TS-TW` | motion | Services, the five trade cards: photograph and trade name on the front, the scope of that trade on the back. |
| **GlideSelect** | `GlideSelect-TS-TW` | ,  | Contact, the inquiry form's "project type" field (residence, hospitality, office, retail): the gliding highlight is a calm, precise response that suit… |
| **GradualBlur** | `GradualBlur-TS-TW` | none | home: the fixed header over the six-room reel, so rooms dissolve under the bar instead of meeting a border; also project captions over the scroll stac… |
| **HalftoneReveal** | `HalftoneReveal-TS-TW` | none | About, the firm section: one archival frame — workshop, drawing, material sample — printed in bone ink on near-black, resolving under the pointer. One… |
| **HoldButton** | `HoldButton-TS-TW` | none | Contact, the inquiry form's submit: brass fill, bone label, ~1.2 s hold, "Hold to send" becoming "Sent". It makes the one action on the site deliberat… |
| **LineSidebar** | `LineSidebar-TS-TW` | none | services page, a left rail beside the five trades: numerals off, marker in brass, `maxShift` ~10, so it reads as an index rather than a toy. |
| **LogoLoop** | `LogoLoop-TS-TW` | none | about page, one muted line of material houses and suppliers under "its trades" — line layout, no bend, no drag. |
| **Magnet** | `Magnet-TS-TW` | none | contact page, the single brass inquiry action only (submit or the "start a project" mail link), with `maxOffset` ~8 and `tilt` 0. |
| **Noise** | `Noise-TS-TW` | none | Home, the hero plate and the six-room reel: one grain at ~0.06 over all six photographs makes them read as a single shoot instead of six files. Nothin… |
| **ParticleText** | `ParticleText-TS-TW` | none | the 404 page only: the monument line reassembling out of dust, in bone, with no highlight colour. Not the home wordmark — the mark is the argument's f… |
| **RefineFrame** | `RefineFrame-TS-TW` | ,  | Projects page grid and the home reel panels: keep the mosaic-to-sharp resolve, drop the chip and the generation wording, and drive `status` from the i… |
| **ScrollExpand** | `ScrollExpand-TS-TW` | none | home, the six-room reel: each room arrives as a framed plate and opens to full bleed, driven by window scroll. Also the head of the projects stack. Re… |
| **ScrollReveal** | `ScrollReveal-TS-TW` | gsap | about, the statement paragraph under the firm's name: words settle as you read and the block straightens from 2°. Also the project captions. Use `mode… |
| **ScrollStack** | `ScrollStack-TS-TW` | none | Projects, the scroll stack of rooms: this is that mechanic already built, with depth, dim and hold tuned. |
| **Silk** | `Silk-TS-TW` | none | The about page lede, the one text-only section with no photograph, at ~25% opacity in bone on near-black; not the home hero, which is already full-ble… |
| **SpecularButton** | `SpecularButton-TS-TW` | none | The single brass action: the "Send inquiry" submit at the end of the contact form's three steps. One instance, nowhere in the nav. |
| **SplitText** | `SplitText-TS-TW` | gsap,  | Home, the monument wordmark at first paint: one slow per-letter rise on the firm name, then nothing else on the page moves until the reel. |
| **SpotlightCard** | `SpotlightCard-TS-TW` | none | Services, the five trade cards: a faint brass light under the pointer gives the text panels a material quality without a second accent. |
| **Stepper** | `Stepper-TS-TW` | ,  | Contact, if the inquiry is split into three calm steps (the space, the scope, you). The step machinery and height tween are the useful part; the tiles… |
| **StrokeText** | `StrokeText-TS-TW` | gsap | services, the five-trades intro heading: brass stroke drawing on, then filling to bone, once on scroll. Nowhere else — the home wordmark must stay typ… |

## Rejected

| Component | Registry | Deps | Why it lost |
| :-- | :-- | :-- | :-- |
| **ASCIIText** | `ASCIIText-TS-TW` | none | no fit. Home's monument wordmark is a drawn SVG (LiveMark); an ASCII raster would replace the one exact mark on the site with a pixel effect, and the … |
| **AccordionGallery** | `AccordionGallery-TS-TW` | gsap | Services › "The five trades" strip. It is already there, hand-ported to `src/components/reactbits/AccordionGallery.tsx` with trade bullets, arrow keys… |
| **AcidSquares** | `AcidSquares-TS-TW` | none | no fit. An acid-pink and electric-blue nightclub floor, two accents past brass, competing with the rooms that are supposed to carry the page. |
| **AeroShards** | `AeroShards-TS-TW` | vgpu | no fit. An abstract glass ribbon is atmosphere where the site needs rooms, and a WebGPU-only layer blanks the section on browsers that cannot run it. |
| **AnimatedContent** | `AnimatedContent-TS-TW` | gsap | every page's scroll reveal, but that job is already done by `src/lib/useReveal.ts` (IntersectionObserver + CSS, mutation-aware, failsafe-gated) at zer… |
| **AnimatedList** | `AnimatedList-TS-TW` | ,  | No fit. The site has no list UI — services are an accordion strip, work is a scroll reel, the contact page holds a form and two addresses. This is a f… |
| **Antigravity** | `Antigravity-TS-TW` | none | no fit. A particle halo chasing the cursor is a product-launch gesture, and its coloured glow would sit on top of whatever section adopted it. |
| **Aurora** | `Aurora-TS-TW` | none | no fit. A coloured bloom behind the monument wordmark or the closing stage adds a second light source to a page lit by photography, and the stock ramp… |
| **Balatro** | `Balatro-TS-TW` | none | no fit. A psychedelic card-game shader would put a red and blue swirl behind rooms that are the whole argument. |
| **Ballpit** | `Ballpit-TS-TW` | none | no fit. A play pit is a toy; the bar here is a section that carries photography, not a physics demo. |
| **Beams** | `Beams-TS-TW` | none | Home, behind the monument wordmark — the only full-bleed slot where an ambient field could sit. |
| **BellToggle** | `BellToggle-TS-TW` | motion, ,  | No fit — the inquiry form needs a submit, not a notification gimmick, and there is no mailing list to notify. |
| **BlobCursor** | `BlobCursor-TS-TW` | three | No fit — a chrome cursor is a portfolio toy, not a fit-out contractor's first impression. |
| **BorderGlow** | `BorderGlow-TS-TW` | none | No fit — a purple, pink and blue mesh rim introduces two more accents and a soft-light fill that has nothing to say about interiors. |
| **BranchedMenu** | `BranchedMenu-TS-TW` | ,  | Services, a five-trade index with each trade's scope items — but only if the page actually carries a side index. |
| **BubbleMenu** | `BubbleMenu-TS-TW` | gsap | No fit — the brand's nav should be three quiet words in a corner, not a field of pastel bubbles. |
| **CRTWarp** | `CRTWarp-TS-TW` | none | No fit — a violet CRT is a different brand universe and would sit against every room photograph like a joke. |
| **CallChip** | `CallChip-TS-TW` | ,  | no fit. Monospace argument strings, terminal icons, and millisecond counters belong in developer tooling, not an interior fit-out portfolio. |
| **CardNav** | `CardNav-TS-TW` | ,  | No fit. Header.tsx opens with a note that the bar must never gain a ground of its own — a slab over a full-bleed photograph is a seam across the pictu… |
| **CardSwap** | `CardSwap-TS-TW` | ,  | no fit. A tilted, skewed card deck with fling physics trivializes architectural spaces; ARKRETE's projects page already uses a deliberate vertical scr… |
| **Carousel** | `Carousel-TS-TW` | ,  | no fit. Arkrete relies on scroll-driven reels and stacks for room photography; interactive sliders with tilt/cube transitions and progress bars add UI… |
| **ChromaGrid** | `ChromaGrid-TS-TW` | none | no fit. Arkrete treats photography as the argument; draining color from fit-out craft until hovered contradicts the brand, and per-card multicolor acc… |
| **CircularCarousel** | `CircularCarousel-TS-TW` | none | no fit. Slicing interior photography into eight faceted DOM strips warps and fragments architectural lines; Arkrete's photography requires undistorted… |
| **CircularGallery** | `CircularGallery-TS-TW` | none | no fit. Arkrete showcases rooms through deliberate vertical stacks and horizontal reels; a wavy 3D WebGL ribbon is an experimental distraction that th… |
| **CircularText** | `CircularText-TS-TW` | motion | no fit. Arkrete mandates sentence case typography throughout and forbids uppercase mono labels or decorative badges; a spinning circular text badge is… |
| **ClickSpark** | `ClickSpark-TS-TW` | none | no fit. Arkrete is an austere, dark luxury fit-out contractor where photography is the argument; celebratory click sparks or star bursts demean the so… |
| **CodeSlots** | `CodeSlots-TS-TW` | motion, ,  | no fit. Arkrete is an informational portfolio with an inquiry form; the site has no user accounts, client portals, or authentication flows requiring O… |
| **ColorBends** | `ColorBends-TS-TW` | three | No fit. The only full-bleed surfaces are the home reel and the project photography, and both lose to saturated gradient colour; it also introduces a s… |
| **CometDial** | `CometDial-TS-TW` | motion | No fit. Nothing on the site is a bounded quantity a visitor would want to dial. |
| **CountUp** | `CountUp-TS-TW` | motion | No fit. There is no figure on the site worth counting, and the brief rules out stat rows. |
| **Counter** | `Counter-TS-TW` | none | No fit. It exists to make a figure feel expensive, and the site shows no figures. |
| **Crosshair** | `Crosshair-TS-TW` | none | No fit. Mono coordinate tags and a targeting reticle are a technical register the brand explicitly avoids, and the reticle competes with the brass acc… |
| **CrystalizedBall** | `CrystalizedBall-TS-TW` | ogl | No fit. A glowing orb is the decorative second-colour object the brief rules out, and the home hero is a wordmark, not a bauble. |
| **Cubes** | `Cubes-TS-TW` | none | No fit. An outlined cube lattice is an agency/tech motif; over interior photography it reads as decoration. |
| **CursorGrid** | `CursorGrid-TS-TW` | none | No fit. A drafting grid is a blueprint motif; the site's ground is deliberately empty. |
| **CurvedInput** | `CurvedInput-TS-TW` | none | No fit. Contact is the only form, and its first field is a full inquiry, not a bent email chip. |
| **CurvedLoop** | `CurvedLoop-TS-TW` | none | No fit. The home already carries the monument wordmark, and a second moving line of uppercase type breaks both the sentence-case rule and the stillnes… |
| **DarkVeil** | `DarkVeil-TS-TW` | none | Home hero, but only stilled to a near-black brass wash. As shipped it introduces a second light source and a purple default into a page whose wordmark… |
| **DecayCard** | `DecayCard-TS-TW` | none | Projects rooms would be the only home, and there the effect is backwards: it damages the room photography that is the entire argument. |
| **DecryptedText** | `DecryptedText-TS-TW` | motion | No fit. A hacker-style decryption read belongs to a security product, not to a fit-out firm's quiet pages. |
| **DepthCarousel** | `DepthCarousel-TS-TW` | gsap | Projects, where the brief already calls for a scroll stack of rooms; this would be a second, competing way to move through the same images and would t… |
| **Dither** | `Dither-TS-TW` | none | No fit. This is ambient shader behind content; the site's ground should stay a still near-black so the photography is the only texture on the page. |
| **DitherVeil** | `DitherVeil-TS-TW` | ogl | Projects rooms could carry it, but it shows every room as a dither until touched, which undersells the photography the page exists to display. |
| **Dock** | `Dock-TS-TW` | react-dom | No fit. A dock is an operating-system metaphor; the site needs a quiet header with five links, not a launcher. |
| **DodgeField** | `DodgeField-TS-TW` | motion | No fit. Every path on this site ends at "Request a proposal"; a button that runs from the client's cursor is the opposite of the firm's job, and the t… |
| **DomeGallery** | `DomeGallery-TS-TW` |  | no fit. Projects already carries the rooms as a scroll stack; a sphere crops the architecture, greys it, and hides the work behind a drag nobody will … |
| **DotField** | `DotField-TS-TW` | none | no fit. It is ground texture, not content; a static CSS or SVG dot pattern costs nothing and stays quieter behind the wordmark. |
| **DotGrid** | `DotGrid-TS-TW` | none | no fit. Jelly physics under a luxury interior site reads as a toy, and no page needs a second interactive surface. |
| **ElasticMesh** | `ElasticMesh-TS-TW` | none | no fit. An inflated jelly wordmark is playful; the ARKRETE monument has to stay typographic and still. |
| **ElasticSlider** | `ElasticSlider-TS-TW` | ,  | no fit. The contact form's budget field should be a native range or a select; a media-style slider with volume icons and rubber overshoot is the wrong… |
| **ElectricBorder** | `ElectricBorder-TS-TW` | none | no fit. Cyan electric edging is a second accent and pure decoration; a hairline brass border already does the job. |
| **ElectricLogo** | `ElectricLogo-TS-TW` | ogl | no fit. Lightning around the ARKRETE mark would fight the brass accent and turn a quiet luxury wordmark into a gaming logo. |
| **EvilEye** | `EvilEye-TS-TW` | ogl | no fit — a literal eye is a horror motif, and its default orange would be a second accent on a brass-only site. |
| **FallingText** | `FallingText-TS-TW` | matter-js | no fit — the home wordmark is a monument, and a headline that collapses into a heap is a joke at its expense. |
| **FaultyTerminal** | `FaultyTerminal-TS-TW` | none | no fit — a retro terminal would read as a hackathon page, and no section of the site is about technology. |
| **Ferrofluid** | `Ferrofluid-TS-TW` | none | no fit — the only full-bleed surfaces are the hero and the reel, and both are photography of rooms, not liquid metal. |
| **FlexCarousel** | `FlexCarousel-TS-TW` | ogl | no fit — projects is a vertical stack and home is a scroll reel; a horizontal lens row has no slot, and the lens warps the photography that is suppose… |
| **FloatingLines** | `FloatingLines-TS-TW` | none | no fit — a magenta line field behind the contact form is decoration with no job, and a second accent. |
| **FlowingMenu** | `FlowingMenu-TS-TW` | ,  | the nav overlay, if the five pages ever need a full-height menu with room photographs in the band. |
| **FluidGlass** | `FluidGlass-TS-TW` | none | no fit — a floating chromatic glass blob refracting text is a decorative tech demo that distorts architectural photography and breaks editorial typogr… |
| **FluxLines** | `FluxLines-TS-TW` | none | no fit — glowing generative magnetic currents act as decorative wallpaper that distracts from physical materials and adds luminous noise. |
| **FlyingButton** | `FlyingButton-TS-TW` | none | no fit — a rocket button blasting smoke plumes and flying across the screen is an extreme novelty that destroys luxury credibility. |
| **FlyingPosters** | `FlyingPosters-TS-TW` | none | no fit — interior photography must remain planar, stable, and true to proportion, not twisted and flipped in a 3D perspective vortex. |
| **FoldText** | `FoldText-TS-TW` | gsap | no fit — folding origami paper or louvre blinds typography reads as craft-paper novelty rather than solid stone and architectural woodwork. |
| **Folder** | `Folder-TS-TW` | none | no fit — skeuomorphic desktop folder metaphor with fanned documents and draggable paper sheets completely clashes with a dark luxury architectural wor… |
| **FolderFloat** | `FolderFloat-TS-TW` | matter-js | no fit — floating draggable feedback pills springing out of an office folder is playful SaaS product UI, not serious architectural contracting. |
| **FuseButton** | `FuseButton-TS-TW` | ,  | no fit — ARKRETE is an architectural brochure site with no destructive actions, and the contact inquiry form does not need a 4-second undo fuse. |
| **FuzzyText** | `FuzzyText-TS-TW` | none | no fit — shivering CRT glitch static and vibrating fuzzy text reads as cybernetic or distressed VHS horror, the exact opposite of calm, stone-and-bras… |
| **Galaxy** | `Galaxy-TS-TW` | none | No fit. The home hero is a monument and a reel of rooms; a literal galaxy is a different world, and a full-screen shader would fight both the wordmark… |
| **GhostCursor** | `GhostCursor-TS-TW` | none | No fit. Purple smoke chasing the cursor over interior photography is costume, and the overlay would sit above the room reel. |
| **GhostFibers** | `GhostFibers-TS-TW` | none | No fit. A violet fibre curtain is a screensaver, not a room; on the about page it would be decoration with no job and a second accent colour. |
| **GlassIcons** | `GlassIcons-TS-TW` | none | No fit. The contact page's phone and email links should be two lines of text; an app-icon dock belongs to a product, and the coloured plates would add… |
| **GlassSurface** | `GlassSurface-TS-TW` | none | No fit as shipped. A glass scrim over the home room reel would distort the photography, and the default red/green/blue offsets add colour the palette … |
| **GlitchText** | `GlitchText-TS-TW` | none | No fit. Red/cyan channel split adds two accents to a one-accent palette, and the glitch language reads gaming or cyber, the opposite of the firm's cal… |
| **GlowCursor** | `GlowCursor-TS-TW` | none | No fit. A blue fluid light drifting over near-black is a screensaver; even retuned to brass it would be decoration laid on top of the photography, whi… |
| **GooeyNav** | `GooeyNav-TS-TW` | none | no fit. The header on every page is four links and should be quiet; a shader there is a second show. |
| **GradientASCII** | `GradientASCII-TS-TW` | none | no fit. ASCII is a technology signal; even on services it would be a second accent laid over the five trades. |
| **GradientBlinds** | `GradientBlinds-TS-TW` | none | no fit. It sits exactly where a room photograph belongs on home or projects, and the pink/violet ramp is a second accent. |
| **GradientText** | `GradientText-TS-TW` | none | no fit. The only type that could carry a gradient is the home monument wordmark, and that must stay bone. |
| **GradientWaves** | `GradientWaves-TS-TW` | none | no fit. A synthetic sea is the opposite of a Cairo or Dubai room, and it would take the hero slot the wordmark and reel own. |
| **Grainient** | `Grainient-TS-TW` | none | no fit. A flowing gradient behind copy is a second accent and cuts contrast; the grain it sells is a 1 KB static noise layer. |
| **GridDistortion** | `GridDistortion-TS-TW` | none | no fit. It turns room photography — the argument — into a cursor toy, and its default idle wander keeps moving with no input. |
| **GridMotion** | `GridMotion-TS-TW` | none | no fit. Projects already has a scroll stack of rooms; a second drifting wall would compete with it and out-shout the photographs. |
| **GridScan** | `GridScan-TS-TW` | none | no fit — a wireframe grid room is a sci-fi HUD, and ARKRETE's rooms are photographed, not diagrammed; its default scan colour is also a cyan second ac… |
| **HoloCard** | `HoloCard-TS-TW` | none | no fit — a collectible trading card with rainbow foil is the inverse of a near-black, single-accent world, and there is nothing to collect. |
| **Hyperspeed** | `Hyperspeed-TS-TW` | three | no fit — a racing-game highway has nothing to do with interiors, and its palette is neon. |
| **ImageTrail** | `ImageTrail-TS-TW` | gsap | no fit — a cursor toy, and the home page already has a scroll reel of six rooms; on mobile there is no cursor. |
| **InfiniteMenu** | `InfiniteMenu-TS-TW` | none | no fit — projects is deliberately a scroll stack of rooms; a sphere hides five-sixths of the photography behind a drag gesture and costs 64 MB to do i… |
| **InfiniteSpiral** | `InfiniteSpiral-TS-TW` | none | no fit — an infinite carousel hides most of its images and reads as a portfolio widget; the projects stack already owns image sequencing. |
| **Iridescence** | `Iridescence-TS-TW` | none | no fit — a rainbow soap film is a second palette and pure decoration; no section needs a moving background behind photography. |
| **JellyRadio** | `JellyRadio-TS-TW` | motion | no fit. Playful, bouncy rubber-toy physics contradict the quiet, restrained architectural tone of the site. |
| **Lanyard** | `Lanyard-TS-TW` | three | no fit. A 3D tech-conference credential badge has zero relevance to high-end interior architecture fit-out. |
| **LaserFlow** | `LaserFlow-TS-TW` | none | no fit. Sci-fi neon laser beams and glowing liquid spills are alien to an architectural interior fit-out firm. |
| **LatticeLoader** | `LatticeLoader-TS-TW` | none | no fit. A digital LED matrix and stopwatch timer evoke a developer terminal or LLM chat interface, not a luxury fit-out studio. |
| **LetterGlitch** | `LetterGlitch-TS-TW` | none | no fit. Cyberpunk terminal scrambles and matrix letter glitches directly oppose the bone-and-dark architectural aesthetic. |
| **LightPillar** | `LightPillar-TS-TW` | none | no fit. A glowing sci-fi energy column acts as self-serving spectacle that distracts from architectural room photography. |
| **LightRays** | `LightRays-TS-TW` | none | no fit. Superimposing artificial synthetic sunbeams over architectural interior photography falsifies real lighting and craft. |
| **LightTunnel** | `LightTunnel-TS-TW` | none | no fit. A sci-fi hyperspace fiber-optic tunnel has nothing to do with quiet architectural fit-out. |
| **Lightfall** | `Lightfall-TS-TW` | none | no fit. Sci-fi warp speed rain and neon streak tunnels distract completely from physical interior architecture and materials. |
| **Lightning** | `Lightning-TS-TW` | none | no fit. The home reel is photography; electric blue lightning would introduce a second, theatrical material in a world built on stone and low light. |
| **LineWaves** | `LineWaves-TS-TW` | none | no fit. Fine-line waves behind a form or footer would be texture with no job, and they compete with the photography. |
| **LiquidChrome** | `LiquidChrome-TS-TW` | none | no fit. Liquid chrome is a material study; as a hero it would read as a second brand rather than a room. |
| **LiquidEther** | `LiquidEther-TS-TW` | none | no fit. A multicoloured ink palette is a second accent by definition, and a solver this heavy cannot be justified by a background. |
| **MagicBento** | `MagicBento-TS-TW` | ,  | no fit. Its native content is dashboards, metrics and product UI — the stat-row, explanatory register the site rejects. |
| **MagicRings** | `MagicRings-TS-TW` | none | no fit as implemented. The same mark — thin concentric rings in one brass — is a two-path SVG at zero runtime cost. |
| **MagnetLines** | `MagnetLines-TS-TW` | none | no fit. A playful magnetic pointer field is interactive gadgetry suited for a creative tech portfolio; ARKRETE's dark, quiet architectural world deman… |
| **MaskedHeading** | `MaskedHeading-TS-TW` | gsap | no fit. ARKRETE treats interior photography as the argument, displaying full-bleed spatial views; cutting room photography into letterform silhouettes… |
| **Masonry** | `Masonry-TS-TW` | react-dom, ,  | no fit. ARKRETE presents projects as a calm, cinematic vertical scroll stack of rooms where each room commands the screen; a dense Pinterest-style mul… |
| **MetaBalls** | `MetaBalls-TS-TW` | none | no fit. Organic lava-lamp fluid blobs and gooey slime physics belong to experimental creative coding demos; they directly undermine ARKRETE's architec… |
| **MetallicPaint** | `MetallicPaint-TS-TW` | none | no fit. Liquid chrome typography with iridescent rainbow dispersion and constant surface warping is a Y2K/crypto aesthetic that destroys ARKRETE's dar… |
| **MicroSlats** | `MicroSlats-TS-TW` | ogl | no fit. A rolling synthetic sea of purple slats running fluid dynamic equations is purely decorative digital tech art with zero connection to architec… |
| **ModelViewer** | `ModelViewer-TS-TW` | , , three | no fit. ARKRETE is an interior contractor whose core premise is physical finished space captured in high-end photography ("Photography is the argument… |
| **MoltenMetal** | `MoltenMetal-TS-TW` | none | no fit. The caustic incandescent neon lava/plasma aesthetic is diametrically opposed to ARKRETE's palette of near-black ground, bone ink, and quiet ar… |
| **MorphSlider** | `MorphSlider-TS-TW` | ogl, gsap | no fit. ARKRETE's presentation relies on a "scroll-driven reel of six rooms" on home and a "scroll stack of rooms" on projects; melting, rippling, or … |
| **OptionWheel** | `OptionWheel-TS-TW` | none | no fit. The only option list on the site is the "project type" select in the contact enquiry form, and a full-height curved wheel is the wrong instrum… |
| **Orb** | `Orb-TS-TW` | none | no fit. A purple-and-blue glowing orb introduces a second accent to a site whose single accent is brass, and there is no section it would be doing a j… |
| **OrbitImages** | `OrbitImages-TS-TW` | none | no fit. Home already moves six rooms on a scroll-driven reel and projects already stacks rooms; a third device for "rooms in motion" repeats the same … |
| **PaperCrumple** | `PaperCrumple-TS-TW` | three | no fit. The photography is the argument; crumpling a finished room into a ball of waste paper argues the opposite of what the page is for. |
| **Particles** | `Particles-TS-TW` | none | no fit. A starfield with constellation lines is the visual language of software, not of rooms; there is no section where it would be more than atmosph… |
| **PatternWaves** | `PatternWaves-TS-TW` | ogl | no fit. It would be a third procedural surface competing with the photographs and with the ceiling assembly already drawn in CSS on services. |
| **PeekRating** | `PeekRating-TS-TW` | ,  | no fit. Nothing on the site is rated, and the default gold star is exactly the second accent the brief forbids; the enquiry form asks for a project, n… |
| **PillNav** | `PillNav-TS-TW` | none | No fit. ARKRETE's header avoids a floating slab over full-bleed photography, and the site keeps desktop navigation as a quiet typographic row rather t… |
| **PixelBlast** | `PixelBlast-TS-TW` | none | No fit. 8-bit arcade pixel glyphs and shockwave ripples conflict with the dark luxury aesthetic and compete with architectural photography. |
| **PixelCard** | `PixelCard-TS-TW` | none | No fit. Shimmering pixel sparkle cards read as crypto or gaming UI, disrupting the presentation of high-end physical materials and rooms. |
| **PixelSnow** | `PixelSnow-TS-TW` | none | No fit. Pixel snowfall is a seasonal novelty completely out of place for an interior fit-out contractor operating in Cairo and Dubai. |
| **PixelSwap** | `PixelSwap-TS-TW` | none | No fit. Novelty mosaic pixel dissolves and spinning square wipes degrade architectural photography and look like video game transitions. |
| **PixelTrail** | `PixelTrail-TS-TW` | none | No fit. An interactive cursor trail of sparkling, gooey pixels is a toy interaction that distracts from portfolio imagery and lacks reduced-motion sup… |
| **PixelTransition** | `PixelTransition-TS-TW` | none | No fit. An 8-bit blocky pixel curtain wipe between photographs or cards contradicts ARKRETE's refined architectural atmosphere. |
| **Plasma** | `Plasma-TS-TW` | none | No fit. A sci-fi glowing plasma cloud is completely antithetical to physical fit-out craft and real architectural finishes like stone, oak, and brass. |
| **PlasmaWave** | `PlasmaWave-TS-TW` | none | No fit. Glowing neon light tubes and laser bloom belong to nightlife and electronic music visuals, not a quiet Cairo and Dubai fit-out firm. |
| **Prism** | `Prism-TS-TW` | none | No fit. A spectral prism behind the home monument wordmark would add a second accent, and a brass-tinted variant is still a per-pixel raymarch buying … |
| **PrismaticBurst** | `PrismaticBurst-TS-TW` | none | No fit. A starburst is a second accent with no job on any of the five pages, and click-to-burst is a demo gesture rather than an inquiry. |
| **ProfileCard** | `ProfileCard-TS-TW` | ,  | No fit. It is a product-page contact card; the about page is the firm and its trades, and rainbow foil breaks the one-accent rule outright. |
| **PromptBar** | `PromptBar-TS-TW` | motion, ,  | No fit. The contact page is a named-field inquiry form ("Send us the drawings"), not a prompt box, and none of the AI affordances mean anything to a f… |
| **PulseHeart** | `PulseHeart-TS-TW` |  | No fit. Nothing on the site is liked or counted, and a like pill would put the only number on a page that deliberately has no stat rows. |
| **Radar** | `Radar-TS-TW` | none | No fit. A surveillance scope is the wrong metaphor for fit-out work, and no section of home, projects, services, about or contact is a live display. |
| **ReflectiveCard** | `ReflectiveCard-TS-TW` | ,  | No fit. An ID badge that mirrors the visitor is a portfolio trick, camera access on a contractor's site is a bounce, and the card chrome duplicates no… |
| **Ribbons** | `Ribbons-TS-TW` | none | No fit. Cursor ribbons are coloured decoration laid over the photography, and three blues would read as a second accent. |
| **RippleDistortion** | `RippleDistortion-TS-TW` | ogl | no fit. Photography is the argument on every page; a cursor wake that distorts it is decoration aimed at the one thing that must stay legible, and the… |
| **RippleGrid** | `RippleGrid-TS-TW` | none | no fit. A glowing technical grid reads as dashboard, not interiors, and its white cool-toned glow would compete with brass. |
| **RotatingText** | `RotatingText-TS-TW` | motion | home, the line under the monument wordmark — the one place a rotating phrase could go. It is still wrong there: the wordmark is carved and fixed, and … |
| **RubberSegment** | `RubberSegment-TS-TW` | motion | contact, the Cairo/Dubai office switch, the only either/or on the site. Two addresses read better side by side than one hidden behind a toggle, and a … |
| **Scanner** | `Scanner-TS-TW` | none | no fit — a CRT readout belongs to a monitoring product, not a fit-out contractor, and the violet/pink defaults would break the single-accent rule on s… |
| **ScrambledText** | `ScrambledText-TS-TW` | gsap | no fit. Glyph decryption is a terminal trope, the wrong register for interiors, and it imposes its own mono font and 7vw margins. |
| **ScrollFloat** | `ScrollFloat-TS-TW` | gsap | services, the five trade headings, or the about statement. It could be tuned to a 12 px rise with 0.02 stagger, but the presets that justify the libra… |
| **ScrollVelocity** | `ScrollVelocity-TS-TW` | motion | no fit. A repeating marquee is the ambient copy the site avoids, and services already has five quiet panels. |
| **ScrubField** | `ScrubField-TS-TW` | motion | no fit. The contact form wants a plain budget field; a drag-to-scrub chip hides its affordance and fights the calm tone. |
| **ShapeBlur** | `ShapeBlur-TS-TW` | none | no fit. It is a lens for a logo or mark, and ARKRETE's argument is photography, not a generated shape. |
| **ShapeGrid** | `ShapeGrid-TS-TW` | none | no fit. A technical grid under interiors reads as a dashboard, and the hover light duplicates the single accent. |
| **ShapeWaves** | `ShapeWaves-TS-TW` | vgpu | No fit. The only page that could carry it is the home hero, and the hero is a photograph with the wordmark over it; the site's whole argument is the r… |
| **ShinyText** | `ShinyText-TS-TW` | none | no fit. The monument wordmark is bone and the one brass accent is reserved for action; a sheen would be a second finish on the brand. |
| **Shredder** | `Shredder-TS-TW` | react-dom | no fit. A paper shredder is a joke component; no page should make deleting a room look like office equipment. |
| **Shuffle** | `Shuffle-TS-TW` | gsap,  | no fit. A heading that scrambles is theatre; the site's type should arrive like a caption, not a slot machine. |
| **SideRays** | `SideRays-TS-TW` | none | no fit. ARKRETE's light comes from the rooms in the photography; painted shafts in the hero compete with the reel. |
| **SlicedWaves** | `SlicedWaves-TS-TW` | none | No fit. Three saturated colours plus glow add two accents the palette does not have, and the read is nightclub, not interiors. |
| **SlideCommit** | `SlideCommit-TS-TW` | motion, ,  | Argued for the contact form's "Send inquiry" button, and rejected: sending an inquiry is neither destructive nor irreversible. |
| **SlingButton** | `SlingButton-TS-TW` | motion, ,  | No fit. A slingshot on the enquiry CTA reads as a game, and the contact page already ends in a plain submit. |
| **SloshGauge** | `SloshGauge-TS-TW` | none | No fit. The site reports no figures, and a numbered gauge is the stat-row decoration the brief rules out. |
| **SoftAurora** | `SoftAurora-TS-TW` | none | No fit. Magenta and violet are a second and third accent, and coloured glow fights near-black plus brass. |
| **SplashCursor** | `SplashCursor-TS-TW` | none | No fit. Rainbow dye over architectural photography would be the loudest object on the site. |
| **SplitFlapText** | `SplitFlapText-TS-TW` | none | No fit. An uppercase mono board is the departures-hall look the brief rules out, and it types the brand as travel. |
| **SpringCheck** | `SpringCheck-TS-TW` | motion,  | Contact form consent line, if any. But the strike-through says "task done", which is wrong for "I agree to be contacted". |
| **SquishSwitch** | `SquishSwitch-TS-TW` | motion | No fit. Nothing on the site is switched on or off — not the theme, not a filter, not a preference. |
| **Stack** | `Stack-TS-TW` | motion | Projects already has a scroll-driven stack of rooms; this is a drag deck, a different and more playful way to browse the same content. |
| **StaggeredMenu** | `StaggeredMenu-TS-TW` | gsap | The site header, if it ever gets a full menu. But white, uppercase, numbered and blurred is the opposite of the near-black sentence-case world. |
| **StarBorder** | `StarBorder-TS-TW` | none | The one brass action, "Start a project". Which is exactly where a second moving light should not be. |
| **StatusMark** | `StatusMark-TS-TW` | motion | No fit. There is no queue, job or agent state anywhere in a fit-out portfolio. |
| **StickerPeel** | `StickerPeel-TS-TW` | none | no fit. A peelable sticker is a playful, tactile gag; there is no surface on home, projects, services, about or contact where a draggable vinyl decal … |
| **Strands** | `Strands-TS-TW` | none | no fit. The reference is Siri's orb: a seven-colour spectral palette and an "AI assistant" silhouette, dropped into a dark room-photography site. |
| **SwarmCursor** | `SwarmCursor-TS-TW` | none | no fit. A cursor-chasing swarm is ambient noise over photography, and it duplicates the pointer the site already has. |
| **SwipeRow** | `SwipeRow-TS-TW` | motion, ,  | no fit. There is no list, no destructive action and no account surface anywhere on the five pages; the default red action rail is also a second accent… |
| **SwipeToast** | `SwipeToast-TS-TW` | motion, ,  | contact, after the inquiry form submits — but a card with an orange burning fuse is the wrong register; a single inline confirmation line is calmer an… |
| **TargetCursor** | `TargetCursor-TS-TW` | react-dom | no fit. Hiding the native cursor taxes every click on a site whose only job is to show rooms, and a reticle reads as a weapon sight, not a fit-out. |
| **TearTicket** | `TearTicket-TS-TW` | motion | no fit. Tearing a perforated stub is a ticket-and-coupon metaphor; on an interiors site it reads as a promotion, and a fixed 460×250 card fights the f… |
| **TechText** | `TechText-TS-TW` | none | no fit. The home monument wordmark must stay real type in bone ink; the dashed-path, tick-label, selection-handle language is exactly the blueprint/mo… |
| **TextCursor** | `TextCursor-TS-TW` | none | no fit. The home hero is a logo lockup over photography and a text trail there competes with the room; no other section of the five pages has a free c… |
| **TextLoop** | `TextLoop-TS-TW` | gsap | no fit. A perpetual marquee is the one kind of motion the design deliberately avoids, and the default violet ribbon is a second accent. |
| **TextPressure** | `TextPressure-TS-TW` | none | no fit. The hero is an SVG wordmark, every other heading is sentence case, and a headline that warps under the cursor fights the calm the brand is bui… |
| **TextType** | `TextType-TS-TW` | gsap | no fit. Every heading is a fixed statement, and the one place copy appears in response to an action — the contact confirmation — has to be instant. |
| **ThoughtLine** | `ThoughtLine-TS-TW` | motion, ,  | no fit. There is no assistant, agent or asynchronous process on the site to narrate; a "Thinking…" row on an interior fit-out page is nonsense. |
| **Threads** | `Threads-TS-TW` | none | no fit. Every section already carries a photograph; an abstract line field behind it is decoration with a real GPU bill. |
| **TiltedCard** | `TiltedCard-TS-TW` | none | no fit. Projects are a full-bleed scroll stack and services a flex accordion; a tilting card with glare belongs to a product grid the site never uses. |
| **Topography** | `Topography-TS-TW` | none | no fit. A glowing abstract terrain has no job next to room photography, and its default blue is a second accent. |
| **TrueFocus** | `TrueFocus-TS-TW` | motion | no fit. The site never shows one word of a sentence at a time, and a camera-focus bracket is a metaphor with no meaning for a fit-out firm; the defaul… |
| **VariableProximity** | `VariableProximity-TS-TW` | none | No fit. The home monument is an SVG `Logo`, not text, and every heading is set in the site's Archivo/Schibsted faces; swapping in Roboto Flex to make … |
| **VoicePill** | `VoicePill-TS-TW` | ,  | No fit. The contact form is a written inquiry; a mic permission prompt is a trust cost on a contractor's page and there is no voice-note pipeline behi… |
| **WakeSlider** | `WakeSlider-TS-TW` | motion | No fit. The site has no numeric control anywhere — no budget slider, no stat row, no configurator — so the control has no question to answer. |
| **WarmTooltip** | `WarmTooltip-TS-TW` | react-dom, motion | No fit. Header and footer are text links with visible labels, and hiding an office address behind hover on contact would cost the reader a discovery r… |
| **WarpText** | `WarpText-TS-TW` | ogl | No fit. The home monument is a fixed SVG wordmark and section titles are plain text; turning either into a shader texture would make the strongest typ… |
| **Waves** | `Waves-TS-TW` | none | No fit. Home and project pages are carried by full-bleed photography, and a generative line field behind them is a competing texture with no informati… |
| **WebThreads** | `WebThreads-TS-TW` | none | No fit. Luminous neon threads read as a crypto or AI-studio motif, not plaster, stone and joinery, and no ARKRETE section needs a glowing backdrop. |
