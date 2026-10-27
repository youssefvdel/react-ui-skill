# Blocks & Application UI Sources

Pre-built block sets, dashboard kits, and specialized form libraries. Where primitive
registries (shadcn) give you atomic buttons and inputs, these sources provide
turnkey section layouts, complete data-display dashboards, or advanced input variants.

*Note: Documented by architectural archetype and license model. Not surveyed with
rendered screenshots.*

---

## 1. Origin UI

`https://originui.com` · copy-paste & shadcn CLI · **MIT License** · **500+ UI particles / inputs**

A specialized, open-source component collection built on **Tailwind CSS + Base UI / Radix UI**.
Focuses on micro-components, inputs, and complex form controls that standard shadcn leaves plain.

- **Stack**: Tailwind CSS, Base UI / Radix UI, Lucide icons.
- **What it provides**: Over 500 modular UI particles:
  - Advanced inputs (floating labels, password strength meters, prefix/suffix icons, character counters).
  - Toggles, switches, sliders, range inputs, select variants, tags, badges, notifications.
- **When it is the right answer**: You are building an app with heavy form/input requirements and want richer, more polished controls than standard shadcn without paying for Untitled UI Pro.
- **When it is the wrong answer**: Full marketing landing pages or complex dashboard analytics.

---

## 2. Tremor / Tremor Raw

`https://tremor.so` · copy-paste (formerly npm package) · **Apache 2.0**

The standard open-source React toolkit for **dashboards, metrics, and data visualization**.

- **Stack**: React, Tailwind CSS, Recharts / CSS grid.
- **Architecture**:
  - Legacy Tremor (`@tremor/react`) was an npm dependency.
  - **Tremor Raw** pivoted to the shadcn model: copy-paste blocks into your project so you own the styling.
- **What it provides**: Area charts, bar charts, line charts, donut charts, KPI sparklines, data tables, filter bars, metric cards.
- **When it is the right answer**: Analytics platforms, admin portals, internal tools, and financial dashboards requiring dense data representation.
- **When it is the wrong answer**: Editorial marketing sites, artistic landing pages, or consumer apps without analytical data.

---

## 3. Tailwind Plus (formerly Tailwind UI)

`https://tailwindui.com` · copy-paste HTML/React · **Commercial Paid License** ($299 one-time)

The official component directory created by Tailwind Labs (Adam Wathan and team). The canonical reference standard for clean Tailwind styling.

- **License**: **Commercial proprietary**. Lifetime access per developer license. You cannot open-source templates built with it or redistribute the raw component markup.
- **What it provides**:
  - Marketing: Headers, heroes, feature sections, pricing grids, testimonials, footers.
  - Application UI: Shells, stacked layouts, multi-column layouts, tables, forms, modals.
  - Ecommerce: Product overviews, lists, checkout flows.
- **When it is the right answer**: Commercial client work where a corporate or startup design needs to be production-ready immediately, budget is available, and you want zero third-party dependencies.
- **When it is the wrong answer**: Open-source repositories (prohibited by license), projects with zero budget, or sites demanding unique visual art direction.

---

## Other Notable Mentions

| Library | Model | Best For | Note |
|---|---|---|---|
| **Float UI** | Free / Copy-paste | Modern marketing sections & components | Clean Tailwind CSS marketing blocks |
| **Preline UI** | Open-source (MIT) | Large multi-purpose Tailwind UI library | Vanilla JS + React wrappers available |
| **Flowbite React** | Open-source (MIT) | Enterprise UI components | Stricter brand styling, Figma parity |
| **Mantine / Chakra UI** | Heavy npm runtime | Enterprise SaaS back-offices | High runtime JS cost; avoid on marketing/portfolio sites |
