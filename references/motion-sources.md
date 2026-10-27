# Motion & Effect Sources

Peers and alternatives to React Bits in the motion spectrum. Unlike React Bits (which is a standalone JSON registry with no runtime assumptions), several of these build directly on the **shadcn registry format** or focus on specific aesthetic niches.

*Note: None of these collections have been surveyed component-by-component with rendered screenshots the way React Bits was in `visual-review.md`. They are documented here by architectural archetype, license, and fit.*

---

## 1. Magic UI

`https://magicui.design` · shadcn-compatible registry · **MIT License** · **~150+ components**

The closest direct peer to React Bits. It provides animated landing page components, interactive backgrounds, and micro-interactions built on **Framer Motion / Motion + Tailwind CSS**.

- **Key Difference vs React Bits**: Native integration with the shadcn ecosystem. Every component can be added directly via the shadcn CLI:
  ```bash
  npx shadcn@latest add "https://magicui.design/r/<component-name>"
  ```
- **Aesthetic**: Strong emphasis on SVG lines, border beams, animated beams, dotted/grid patterns, retro grids, and particle orbits. More geometric and vector-based than React Bits (less canvas/WebGL).
- **When it is the right answer**: You have an existing shadcn codebase and want modern landing page motion installed cleanly through your existing `components.json` workflow without manual vendoring.
- **When it is the wrong answer**:
  - Tight bundle limits: pulls in Framer Motion / `motion`.
  - Bespoke art direction: its border beams and glowing card effects have become very recognizable across AI/SaaS landing pages and can read as a template.
  - No-JS environments: heavily reliant on client-side Framer Motion hooks.

---

## 2. Aceternity UI

`https://ui.aceternity.com` · copy-paste & shadcn CLI · **Free components + Paid Pro templates**

High-velocity, maximalist landing-page components designed for instant visual impact. Built with **Tailwind CSS + Framer Motion**.

- **Install**:
  ```bash
  # Individual components via copy-paste or npx shadcn
  npx shadcn@latest add "https://ui.aceternity.com/r/<component-name>"
  ```
- **License**: Core components free for personal and commercial projects. "Aceternity UI Pro" is a paid subscription for full templates and advanced sections.
- **Aesthetic**: The far end of the visual spectrum — 3D pin effects, background beams, macbook scroll views, glowing sparkles, canvas reveals, and floating navigation bars.
- **When it is the right answer**: Fast-moving prototypes, hackathons, or high-concept agency pitches where you need immediate "wow factor" and high animation density.
- **When it is the wrong answer**:
  - **Brand-led luxury or serious corporate sites**: Easily tilts into visual noise and AI-generated template territory if more than 1–2 effects are used on a page.
  - Accessibility: Many complex canvas/3D interactions do not have out-of-the-box reduced motion fallbacks or screen reader narratives.

---

## 3. Motion Primitives

`https://motion-primitives.com` · copy-paste · **MIT License**

A collection of restrained, highly polished micro-interactions and UI animation primitives created by Emil Kowalski and the design engineering community.

- **Stack**: Tailwind CSS + Framer Motion.
- **Aesthetic**: Focuses on micro-interactions: smooth accordion expansions, morphing dialogs, spring-based popovers, segmented controls, and tasteful hover transitions.
- **When it is the right answer**: You need subtle, native-feeling software interactions rather than flashy landing page banners. Highest craft bar in the Framer Motion ecosystem.
- **When it is the wrong answer**: You need full section marketing effects (heroes, particle meshes, 3D cards).

---

## 4. Animata

`https://animata.design` · copy-paste · **MIT License**

A lightweight, community-driven collection of hand-crafted animations, cards, and text effects built with Tailwind CSS.

- **Stack**: Tailwind CSS (mostly pure CSS transitions or minimal Framer Motion).
- **When it is the right answer**: You want small, isolated animation tricks (animated shiny borders, bento grids, subtle text highlights) without taking on large canvas or GSAP dependencies.

---

## Summary / Ecosystem Mention

Other shadcn-registry motion libraries exist in the ecosystem (**Cult UI**, **Kokonut UI**, **Eldora UI**). They share the same underlying architecture (shadcn CLI + Tailwind + Motion). Treat them as specialized variants of the Magic UI model rather than distinct frameworks.
