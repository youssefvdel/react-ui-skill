# shadcn/ui

`https://ui.shadcn.com` · copy-into-codebase registry · MIT · **~50 primitive components**

The archetype that created the modern React registry ecosystem. Not a library you
install as an npm dependency: you initialise a configuration file (`components.json`)
and copy component source directly into your repository.

- **Stack**: React + Tailwind CSS + **Radix UI** primitives + `class-variance-authority` (cva) + `clsx` / `tailwind-merge`.
- **The Core Difference vs HeroUI**: shadcn uses **Radix UI** primitives for accessibility and headless behavior; HeroUI uses **React Aria**. Radix is simpler and lighter; React Aria is more exhaustive on complex inputs (date pickers, internationalization, mobile touch edge-cases).
- **The Registry Standard**: Almost all modern motion and block kits (Magic UI, Origin UI, Aceternity, Cult UI) format their components to work with the `shadcn` CLI.

## Installation & Workflow

```bash
# Initialize in a project
npx shadcn@latest init

# Add components
npx shadcn@latest add button dialog dropdown-menu
```

Configuration lives in `components.json`:
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  }
}
```

## When it is the right answer

- **Core product surfaces**: Web applications, dashboards, settings, SaaS tools where you need complete ownership over every component's markup.
- **Teams with strict design systems**: You want accessible headless primitives (Radix) styled with Tailwind classes that you can modify without fighting library overrides.
- **Projects using ecosystem registries**: You plan to pull in specialized components from Magic UI, Origin UI, or Aceternity via `npx shadcn add`.

## When it is the wrong answer

- **Turnkey marketing pages**: shadcn provides building blocks (Buttons, Dialogs, Cards), not finished marketing hero sections, pricing grids, or testimonial carousels.
- **Projects where zero boilerplate is required**: You inherit ~50 lines of code per component in your repo that you are responsible for maintaining.
- **High-craft bespoke animations**: Its default components have minimal motion (subtle popovers/dialog fades). High-end motion requires layering an animation library on top.

## Gotchas

- **CLI package name**: The official CLI is `shadcn`, not `shadcn-ui` (which is the deprecated legacy package). Always use `npx shadcn@latest`.
- **Tailwind v4 support**: In Tailwind v4, CSS variables are defined directly in CSS using `@theme` rather than `tailwind.config.js`. Newer versions of the shadcn CLI support CSS-first configuration.
- **Radix peer dependencies**: Adding a component installs `@radix-ui/react-<primitive>` packages. Keep your lockfile clean by pruning unused primitives if you delete a component.
