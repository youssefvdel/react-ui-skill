# React Bits — a skill for agents

An agent skill for working with [React Bits](https://reactbits.dev): find a
component, price it honestly, install it, or vendor it into a design system —
and, when the question is bigger than one component, survey all **218** of them
before touching a page.

Written by an agent that did exactly that: 218 components fetched, read, judged
and re-audited against their source, then the verdicts used to refactor a live
site.

## What's in it

| Path | What it is |
|---|---|
| `SKILL.md` | The skill itself — two modes (pick one / survey all), the judgements, the pitfalls |
| `references/catalog.md` | Worked example: 218 components with a verdict and a reason each |
| `references/porting.md` | How to vendor a component without importing its demo look |
| `references/brief-template.md` | The rubric to paste into each subagent when fanning out |
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
