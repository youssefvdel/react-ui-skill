---
name: react-ui
description: "Use when choosing React UI for a page: primitive registry (shadcn/ui), motion/art (React Bits, Magic UI, Aceternity), accessible product surfaces (HeroUI), or turnkey blocks & dashboards (Untitled UI, Origin UI, Tremor, Tailwind Plus). Routes the archetype before the component."
version: 2.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [frontend, react, component-library, animation, design-system, shadcn, magic-ui, heroui, untitled-ui, origin-ui, tremor, research]
    related_skills: [port-ui-components, pick-ui-library, impeccable, animation-performance]
---

# React UI: the ecosystem archetypes

Choose the architectural archetype before you choose a component library.
Picking a HeroUI modal to decorate a hero, or a React Bits canvas on an admin
settings form, is how a page ends up looking disjointed.

| Archetype | Leading Libraries | Reach for it when | Reference |
|---|---|---|---|
| **The Base Registry** | **shadcn/ui** (~50 primitives, Radix UI) | Core product foundations; atomic building blocks you own and modify in your repo | `references/shadcn.md` |
| **Motion & Art** | **React Bits** (~218 reviewed, standalone), **Magic UI**, **Aceternity UI** | High-craft moments, landing page hero effects, interactive motion layers | this file, `references/motion-sources.md` |
| **Accessible Behavior** | **HeroUI** (72 components, React Aria + Tailwind v4) | Complex accessible inputs, date pickers, tables, and product surfaces with zero setup | `references/heroui.md` |
| **Floor Plan & Blocks** | **Untitled UI React** (101 groups), **Origin UI** (500+ inputs), **Tailwind Plus** | Full marketing sections, dense form inputs, or turnkey SaaS layouts | `references/untitled-ui.md`, `references/blocks-sources.md` |
| **Dashboards & Charts** | **Tremor / Tremor Raw** (copy-paste analytics) | Data visualization, metric cards, KPI grids, and analytics portals | `references/blocks-sources.md` |

The short rule: **shadcn is the skeleton, React Bits/Magic UI is art, HeroUI is behavior, Untitled UI is a floor plan, and Tremor is data.**

Two modes, chosen by what was asked:

| The ask | Mode | Section |
|---|---|---|
| "add a shiny button", "find me a text animation" | **Pick one** | Pick one component |
| "what else could we use", "audit every component", "rebuild this page around a gallery" | **Survey all** | Survey all 218 |

Never survey 218 components to answer a question about one, and never pick a
single component by name when the task is "make this page better" — the library
is big and the obvious first result is usually the demo-looking one.

The rest of this file is React Bits, because that is the library that needs a
catalogue, a survey procedure and a visual verdict per component. The other two
are documented in `references/`: what they contain, what they cost, and — more
usefully — when they are the wrong answer.

---

## What is actually in the registry

Verified against `https://reactbits.dev/r/registry.json` (1,274 entries):

- Each component ships in four dialects: `Name-JS-CSS`, `Name-JS-TW`,
  `Name-TS-CSS`, `Name-TS-TW`. **Filter to `-TS-TW`** — TypeScript + Tailwind.
  That is the 218 real components. The other three are the same component in
  another dialect, and documenting them triples the work for no gain.
- A registry item carries `name`, `title`, `description`, `type`,
  `dependencies[]`, `registryDependencies[]`, `files[].path` — and **no
  category, and no file content**. `files[].content` is empty in the index.
- The source lives at `https://reactbits.dev/r/<Name>-TS-TW.json`. Fetch that;
  it is where `files[].content` is filled in.
- Dependencies are declared as ranges, e.g. `["gsap@^3.13.0"]`. In the 218:
  `motion` 28, `gsap` 18, `ogl` 10, `three` 6, `@gsap/react` and friends ~59,
  `matter-js` 2, `vgpu` 2. The rest are dependency-free.
- Descriptions are marketing lines. `"smooth scroll gallery"` can be 900 lines
  of WebGL. The `dependencies` array is the only honest cost signal in the
  index, and even it misses imports the file does itself.

---

## Pick one component

1. **Find it.** Either ask the registry (works everywhere):

   ```bash
   curl -s --max-time 90 --compressed https://reactbits.dev/r/registry.json \
     | python3 -c "import json,sys; [print(i['name'], '-', i['description']) for i in json.load(sys.stdin)['items'] if i['name'].endswith('-TS-TW')]" \
     | grep -i "text animation"
   ```

   or, if React Bits MCP tooling is connected, use it — but **check the tool
   names first** with `tool_search('reactbits registry component')`. Names
   differ between installs: this Hermes ships a registry-backed server whose
   tools are `mcp__React_Bit__search_items_in_registries`,
   `view_items_in_registries`, `get_add_command_for_items`,
   `get_item_examples_from_registries`, `list_items_in_registries`. The names
   `mcp__reactbits__list_components` / `get_component` that circulate in older
   copies of this skill belong to a different MCP server that may not exist.

2. **Read the source before believing anything.**

   ```bash
   curl -s --max-time 90 --compressed \
     "https://reactbits.dev/r/BlurText-TS-TW.json" -o /tmp/comp.json
   python3 -c "
   import json; d=json.load(open('/tmp/comp.json'))
   print(d['dependencies'])
   for f in d['files']: print('---', f['path']); print(f['content'][:2000])
   "
   ```

3. **Price it.** `gzip -c <file> | wc -c` on the source is the number that
   matters, plus the dependency it drags in. A 4 KB component carrying
   `three@0.180` is not a 4 KB component.

4. **Install or vendor.**
   - *Install* (the project has no design system to violate): `npx shadcn@latest
     add https://reactbits.dev/r/BlurText-TS-TW` if the project is
     shadcn-configured, otherwise write `files[].content` into
     `src/components/…` and add the declared dependencies to `package.json`.
   - *Vendor* (the project has a look of its own): see `references/porting.md`.
     React Bits' demo styling — rounded 32 px corners, purple gradients,
     `#fff` on `#000`, GSAP timelines with no reduced-motion branch — will fight
     a designed site. Vendoring means keeping the mechanism and replacing the
     skin.

5. **Guard the prerender.** If the project statically prerenders (Next, Astro,
   `vite-react-ssg`), any component that touches `window`, `document`,
   `matchMedia`, `ResizeObserver` or a GL context at module scope breaks the
   build. Move it behind a client-only wrapper and a code-split import.

---

## Survey all 218

Run this when the question is "what should this site use", not "how do I add X".

1. **Pull the index.**

   ```bash
   curl -s --max-time 90 --compressed https://reactbits.dev/r/registry.json \
     -o registry.json     # ~530 KB, the CDN is slow; 90 s timeout, always compressed
   ```

2. **Fetch every payload.** `scripts/fetch_catalog.py --all` does it: 218
   requests at `xargs -P 12`, ~5.6 MB, about 90 seconds, into
   `docs/reactbits/raw/<Name>-TS-TW.json`. **Never use a page-extraction tool
   for this** — it summarises and truncates, which destroys the source you need
   to parse. Re-fetch stragglers serially; a handful always time out, and a
   missing payload shows up later as a component nobody can judge.

3. **Write the rubric once, not in every prompt.** The brief states: the site's
   world (palette, type rules, what it refuses), the hard JS budget, the page
   list, and the exact per-component output template. Template:
   `references/brief-template.md`. If the template drifts between agents the
   catalogue cannot be aggregated.

4. **Batch and fan out.** `scripts/make_batches.py` writes
   `batches/batch-NN.json` at ~9 components each — 24 agents for 218. One child
   per batch, each writing `components/<Name>-TS-TW.md` and returning one line
   per component. **Children write separate files, always**; two children
   writing the same file is an unmergeable mess, and children must stay inside
   the docs directory — one stray write into `src/` during a 24-agent fan-out is
   hard to trace afterwards.

5. **Aggregate from disk, never from chat.** Read every `components/*.md` and
   build the table in code (name, deps, mechanism, verdict). The chat only ever
   sees the summary, so counts must come from files.

6. **Verify before trusting.** `scripts/verify_catalog.py` re-reads every
   payload and checks that each doc parses, that its `Deps` header matches the
   payload's `dependencies`, and that its Props section names at least one prop
   the source really declares. That last check is the one that catches an agent
   that only read `description` — it produces a confident doc about a component
   it never opened. Its first version reported 218 failures because the prop
   extractor matched inner option objects (`AnimateOpts`) instead of the
   component's own props; the fixed version is what makes it worth running.

7. **Re-audit with fresh eyes.** `scripts/make_reauth_batches.py` slices the
   catalogue into 12 batches; one agent per batch re-reads the source and
   answers only "does the doc match the code, and is the verdict still
   defensible". Disagreements, not agreement, are the output you want.

---

## Judging: the rules that survive

A component earns its place only if it carries a section or does a job the page
already needs. These are the tests that rejected 191 of 218 in the worked
example (`references/catalog.md`):

- **Cost against the section.** If the dependency (three/ogl/gsap) is heavier
  than the section it improves, it loses. Heavy components count against the
  deferred budget and must be code-split — never the initial one.
- **One accent.** A component shipping its own colour ramp is a second brand.
  Recolour it or reject it.
- **No decoration without a job.** Particles behind a headline, cursors that
  trail, marquees with nothing to say — reject.
- **The demo look.** Rounded 24–32 px cards, glassmorphism, purple gradients:
  these are the library's house style, not the site's. Judge the mechanism, not
  the skin.
- **Content the component demands.** A stats band, a testimonial wall, a logo
  cloud each want copy the site may not have. A component that needs six
  invented numbers is worse than no component.
- **Motion honesty.** Every animation answers a trigger the user touched, and a
  reduced-motion path shows the end state. A component with no
  `prefers-reduced-motion` branch needs one added before it ships.

---

## Pitfalls

- **`mcp__reactbits__*` may not exist.** Verify tool names before writing code
  that calls them; the registry route needs no MCP at all.
- **`-TS-TW` is the filter.** `-JS-TW`, `-TS-CSS` and the Pro variants are the
  same component in another dialect.
- **The index has no source.** `files[].content` is empty there; only
  `/r/<name>.json` carries it.
- **The CDN is slow.** `--max-time 90 --compressed`, `xargs -P 12`, and expect
  stragglers.
- **Descriptions lie about cost.** Read `dependencies` *and* the imports in the
  file; a component can import three modules the index never lists.
- **Prerender is the usual breakage.** `window`, `document`, GL contexts at
  module scope, and `matchMedia` at import time all fail a static build.
- **Framer Motion's import path changed.** Newer components import
  `motion/react`; older ones `framer-motion`. Match the project's installed
  version instead of adding a second animation library.
- **A vendor port must keep the mechanism and drop the skin.** Copy-pasting the
  demo styling is how a designed site starts to look like a component gallery.
- **Never repeat a doc's claim that a component ignores reduced motion.**
  Fifteen of 218 docs said it; three were genuinely wrong and the rest were
  prose that reads like the same claim ("No GSAP; reduced motion drops the
  shake"). Grep the payload for `matchMedia('(prefers-reduced-motion` and read
  how the flag is used before writing the sentence — a regex cannot tell the two
  apart, which is why this check is prose and not a script.
- **Count the flags, not the words.** A component that reads the query and only
  skips its intro is not "reduced-motion aware". Say what it actually stops.

---

## Verify

```bash
python3 scripts/verify_catalog.py                 # this repo's catalogue
python3 scripts/verify_catalog.py ../some-site/docs/reactbits   # a survey root
ls catalog/docs/*.md | wc -l        # must equal the payload count (218)
```

Then open three docs at random and check they name a real prop from the source.
A catalogue that passes the script but reads like marketing was written from
`description` alone.

## Files

- `references/catalog.md` — worked example: 218 components judged from their
  source for a dark, photography-led site, with the reason each one was adopted,
  adapted or rejected.
- `references/visual-review.md` — the same catalogue looked at: 216 demos
  photographed, tiled and reviewed by eye, and the six verdicts the pixels
  overturned.
- `references/porting.md` — how to vendor a component into a design system
  without importing its demo look.
- `references/brief-template.md` — the rubric to paste into each subagent.
- `references/shadcn.md` — shadcn/ui: the base registry archetype, components.json, Radix primitives, Tailwind CSS variables.
- `references/motion-sources.md` — Motion peers: Magic UI (shadcn-compatible), Aceternity UI (maximalist), Motion Primitives, Animata.
- `references/blocks-sources.md` — Block sets & dashboards: Origin UI (500+ form inputs), Tremor (charts & metrics), Tailwind Plus (commercial).
- `references/heroui.md` — HeroUI v3: install, the 72 components by category,
  what its React Aria base buys you, and the v2/v3 trap.
- `references/untitled-ui.md` — Untitled UI React: what is MIT and what is paid,
  CLI and manual install, the 101 groups, and why `--overwrite` is dangerous.
- `scripts/` — fetch, batch, verify, re-audit.
