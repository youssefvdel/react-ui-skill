# Brief template for one batch of React Bits components

Copy to `<site>/docs/reactbits/BRIEF.md` and replace the section marked below
with the real site. Everything else stays as-is — the output template must be
identical for every component or the catalogue cannot be aggregated.

---

You are documenting components from React Bits so the site team can decide
what to adopt. You are not editing the site. You write documentation only.

## Inputs

- Your batch file: `<site>/docs/reactbits/batches/<BATCH>.json` — a JSON array
  of registry names, e.g. `["AnimatedContent-TS-TW", ...]`.
- For each name the raw payload is at `<site>/docs/reactbits/raw/<name>.json`
  with `title`, `description`, `dependencies`, and `files[]` (`path` +
  `content`, the real TSX). Read the source; the description alone is marketing.

## Output

One file per component: `<site>/docs/reactbits/components/<name>.md`, under 45
lines, in exactly this shape:

```
# <Title>
**Registry**: `<name>` · **Deps**: <deps or "none"> · **Files**: <paths>
**What it does** — two sentences, concrete. What you see, not what it "enables".
**Props** — up to eight, one clause each: `prop` (type, default) — what it changes.
**Motion** — what animates, what triggers it (hover / scroll / click / time),
and whether it needs GSAP, Framer Motion, three.js or WebGL.
**Cost** — dependencies, rough weight, DOM or CPU cost, and whether it survives
server prerender or must be client-only.
**Fit for <SITE>** — the exact page and section it would improve, or "no fit".
**Verdict** — adopt / adapt / skip — one line with the reason.
```

## The site you are judging for

<!-- REPLACE: who the site is for, its world (palette, type, what it refuses),
its stack and its hard JS budget, its pages and the job of each one. -->

## Rules

- Write only inside `<site>/docs/reactbits/components/`.
- Never modify the site, its styles, or its `package.json`.
- If a payload is missing or empty, still write the file with what you know and
  say so under **Cost**.

## Return

One line per component, in batch order:

`Name — verdict — one-clause reason`

Nothing else. No preamble, no summary paragraph.
