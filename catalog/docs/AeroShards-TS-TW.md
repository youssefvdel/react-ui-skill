# AeroShards
**Registry**: `AeroShards-TS-TW` · **Deps**: `vgpu@^0.3.1` · **Files**: `AeroShards/AeroShards.tsx`
**What it does** — Streams a ribbon of thick glass shards across five layered depths, with small survey crosses floating between them, edges catching light and a bloom pass over the whole frame. Holding the pointer gathers the shards toward the cursor; clicking sends a ring through the stream.
**Props**
- `count` / `shardSize` / `spread` (1300 / 1 / 1) — flock density and footprint.
- `material` ('glass' | 'chrome', 'glass') — refraction or mirror.
- `placement` ('full' | 'left' | 'right' | 'center', 'full') — where the ribbon sits.
- `shardColor` / `accentColor` / `backgroundColor` ('#896ABD' / '#A855F7' / transparent).
- `twist` / `billow` / `speed` (1 / 1 / 1) — ribbon deformation and drift.
- `depthOfField` / `glow` / `grain` / `vignette` (0.75 / 0.35 / 0.06 / 0.3) — post chain.
- `markers` ('plus' | 'dots' | 'none', 'plus') — survey crosses between the layers.
- `holdToGather` (true), `pulseOnClick` (true), `parallax` (0.5), `onError` — interaction and failure hook.
**Motion** — A WebGPU pipeline built with `vgpu`: 1300 shards across five depth bands following 160-point paths, four bloom levels, depth of field, grain and markers, all recomputed per frame. Time drives travel, roll and twist; the pointer adds parallax and a hold-to-gather spring; clicks emit rings. WebGPU only — `navigator.gpu` is checked and there is no WebGL2 fallback. Reduced motion stops travel, twist and pointer coupling, freezing the field, but the rAF loop keeps ticking.
**Cost** — 21 KB gzip of own source plus the `vgpu` runtime (not counted here), the heaviest thing in this batch: five instanced shard layers, four bloom targets and a full-screen post chain per frame. Client-only: the component renders a bare div and appends its canvas in an effect, so prerender contains nothing. Any browser without WebGPU gets a blank rectangle and an `onError` callback.
**Fit for ARKRETE** — no fit. An abstract glass ribbon is atmosphere where the site needs rooms, and a WebGPU-only layer blanks the section on browsers that cannot run it.
**Verdict** — skip — the largest payload here, no fallback, decoration with no informational job.
