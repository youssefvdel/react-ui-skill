# React UI — a skill for agents

An agent skill for navigating the modern React UI ecosystem:
- **Base Primitives**: **[shadcn/ui](https://ui.shadcn.com)** (~50 Radix primitives, the de-facto registry format).
- **Motion & Art**: **[React Bits](https://reactbits.dev)** (218 standalone motion components, visually surveyed), plus **[Magic UI](https://magicui.design)** (shadcn-native motion) and **[Aceternity UI](https://ui.aceternity.com)** (maximalist hero visuals).
- **Accessible Behavior**: **[HeroUI](https://www.heroui.com/en/docs/react/components)** (72 React Aria components for complex forms/inputs).
- **Floor Plans & Blocks**: **[Untitled UI React](https://www.untitledui.com/react/components)** (101 groups, MIT core), **[Origin UI](https://originui.com)** (500+ form inputs), and **[Tailwind Plus](https://tailwindui.com)**.
- **Data & Dashboards**: **[Tremor / Tremor Raw](https://tremor.so)** (charts, metrics, analytics).

The core rule: **shadcn is the skeleton, React Bits/Magic UI is art, HeroUI is behavior, Untitled UI is a floor plan, and Tremor is data.** Pick the archetype before the library.

The React Bits half was written by an agent that did the work: 218 components
fetched, read, judged and re-audited against their source, then the verdicts used
to refactor a live site. The other two are documented from their live docs,
including where they are the wrong answer for a brand-led site.

## What's in it

| Path | What it is |
|---|---|
| `SKILL.md` | The skill itself — two modes (pick one / survey all), the judgements, the pitfalls |
| `references/catalog.md` | Worked example: 218 components with a verdict and a reason each |
| `references/porting.md` | How to vendor a component without importing its demo look |
| `references/brief-template.md` | The rubric to paste into each subagent when fanning out |
| `references/shadcn.md` | shadcn/ui — the base registry archetype, components.json, Radix primitives, Tailwind CSS variables |
| `references/motion-sources.md` | Motion peers: Magic UI (shadcn-native), Aceternity UI (maximalist), Motion Primitives, Animata |
| `references/heroui.md` | HeroUI v3 — install, the 72 components, the v2/v3 trap, when to refuse it |
| `references/blocks-sources.md` | Block sets & dashboards: Origin UI (500+ form inputs), Tremor (charts & metrics), Tailwind Plus |
| `references/untitled-ui.md` | Untitled UI React — MIT scope vs paid, CLI, the 101 groups, what it costs you |
| `scripts/fetch_catalog.py` | Pull the registry and all 218 TS+Tailwind payloads |
| `scripts/make_batches.py` | Split the payload list into per-agent batches |
| `scripts/build_catalog.py` | Aggregate the per-component docs into `catalog.json` |
| `scripts/verify_catalog.py` | Re-read every payload and check the docs against the real source |
| `scripts/make_reauth_batches.py` | Slice the catalogue for a second-opinion re-audit |
| `catalog/docs/` | All 218 per-component documents |

## Install as a Hermes skill

```bash
git clone https://github.com/youssefvdel/reactbits-skill.git ~/Projects/reactbits-skill
ln -s ~/Projects/reactbits-skill ~/.hermes/skills/reactbits
```

Any agent that reads `SKILL.md` can use it; nothing in it is Hermes-specific
except the paths in the install line.

## The one thing worth taking away

A component's description is a marketing line. Its `dependencies` array and its
source are the truth, and the gap between the two is where budget disappears.
This skill exists so that gap gets measured instead of discovered in production.

## Licence

MIT for the skill text and scripts. The component docs describe code from
[React Bits](https://github.com/DavidHDev/react-bits), which is MIT too — the
verdicts and prose are ours.
