# Untitled UI React

`https://www.untitledui.com/react/components` · source copied into your project
· **~101 component groups** across six sections

Not a dependency. You fetch the source into your repo and own it — the same
model as shadcn, at a much larger scale. Built with **React Aria + TypeScript +
Tailwind CSS v4.3**.

## Licence — read this before promising a client anything

- The **base components** (30 groups) and the **core application UI** (tables,
  tabs, date pickers, charts, pagination, modals, navigation) are **MIT**.
- **Each marketing section category has one free variant**; the rest is the paid
  PRO kit.
- The Figma side is a separate paid product with its own free tier.

So: usable free in commercial work, but the free half is the *components*, not
the polished page examples.

## Install

```bash
# scaffold a new project (Next.js) with everything wired
npx untitledui@latest init

# add one component to an existing project
npx untitledui@latest add [component-name]

# update a component you already copied — REPLACES your local edits
npx untitledui@latest add [component-name] --overwrite
```

Manual install needs Tailwind first, then:

```bash
bun add @untitledui/icons react-aria-components tailwindcss-react-aria-components tailwind-merge tailwindcss-animate
```

…plus their `theme.css` and `globals.css` copied in and imported from your main
stylesheet. Skipping those files is the usual reason a copied component renders
unstyled.

## What is in it

**Base components (30)** — Avatars, Badge groups, Badges, Button groups,
Buttons, Checkboxes, Context menus, Credit cards, Dropdowns, Featured icons,
Illustrations, Inputs, Mobile app store buttons, Progress indicators, QR codes,
Radio buttons, Radio groups, Rating, Rich text editors, Select + multi-select,
Sliders, Social buttons, Tags, Textareas, Toggles, Tooltips, Utility buttons,
Verification code inputs, Video players.

**Application UI (37)** — Activity feeds, gauges, Alerts, Breadcrumbs,
Calendars, Card headers, Carousels, Code snippets, Color pickers, Command menus,
Content dividers, Date pickers, Empty states, File uploaders, Filter bars,
Gradient pickers, Header navigations, Image pickers, Inline CTAs, Line & bar
charts, Loading indicators, Messaging, Metrics, Modals, Notifications, Page
headers, Paginations, Pie charts, Progress steps, Radar charts, Section
footers/headers, Sidebar navigations, Drawers, Tables, Tabs, Tree views.

**Marketing sections (18 categories, one free variant each)** — Banners, Blog,
Careers, Contact, Content & rich text, CTA, FAQ, Features, Footers, Header
navigations, Hero header, Header, Metrics, Newsletter CTA, Pricing, Social
proof, Team, Testimonial.

**Page examples** — shared auth pages (log in, sign up, verification, forgot
password, 404, email templates), 6 dashboards/settings/informational page
examples, 10 marketing page examples (about, blog, contact, FAQ, landing, legal,
pricing, team, 404).

## When it is the right answer

- You need a **whole surface fast** and the design is allowed to look like a
  product rather than a brand: dashboards, settings, auth flows, pricing pages,
  marketing scaffolds for a SaaS.
- You want patterns already solved at the layout level — filter bars, empty
  states, progress steps, page headers — instead of assembling primitives.
- The team is happy **owning the source**: this is a fork you accept maintenance
  for.

## When it is the wrong answer

- A **brand-led site** with a point of view. Every section arrives with the
  Untitled UI look (soft cards, `brand-*` purple ramp, generous radius, muted
  grey body). Restyling a whole marketing section costs more than writing it, and
  half-restyled is the worst outcome: it reads as a template.
- A project with a tight JS budget: React Aria components are heavier than a
  hand-written `<button>`, and each copied component drags its imports with it.
- Anything the client will keep editing with no engineer: copied source has no
  version to bump.

## Gotchas

- `--overwrite` **destroys local edits**. Commit before updating a component.
- The theme is CSS variables (`--color-brand-*`, `--color-neutral-*`). Pointing
  those at your palette is the one change that makes it not look like Untitled
  UI — do that first, before touching individual components.
- Copying a component without its `theme.css`/`globals.css` is the #1 cause of
  "it renders unstyled".
- Their icons are a separate package (`@untitledui/icons`); the components assume
  it.
- This is a catalogue, not a survey: nothing here has been visually reviewed
  component-by-component the way the React Bits set has.
