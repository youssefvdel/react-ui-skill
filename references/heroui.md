# HeroUI (v3)

`https://www.heroui.com/en/docs/react/components` · npm package · **72 components**

An installed component library — not a copy-paste registry. You add it as a
dependency, import from `@heroui/react`, and it updates with the package.

- Built on **React 19 + Tailwind CSS v4 + React Aria Components**.
- Accessibility is React Aria's, not theirs: focus management, keyboard
  navigation and screen-reader semantics come from Adobe's primitives. That is
  the single strongest reason to pick it over a copy-paste kit.
- Animated by default (it ships its own motion), themed through CSS variables.
- There is also a HeroUI **MCP server** and a `heroui.pro` paid tier; neither is
  needed to use the free components.

## Install

```bash
bun add @heroui/styles @heroui/react
```

```css
/* main stylesheet — order matters, Tailwind first */
@import "tailwindcss";
@import "@heroui/styles";
```

```tsx
import { Button } from '@heroui/react'
```

**Version trap:** v2 (formerly NextUI) and v3 are different libraries. v2 wanted
a Tailwind plugin plus `framer-motion`; v3 wants `@heroui/styles` and React 19.
Half the tutorials and model memorised snippets still show v2. Check the version
on the page you are reading before pasting anything.

## What is in it, by category

| Category | Components |
|---|---|
| Buttons | Button, ButtonGroup, ToggleButton, ToggleButtonGroup, CloseButton |
| Collections | Dropdown, ListBox, TagGroup |
| Colors | ColorArea, ColorField, ColorPicker, ColorSlider, ColorSwatch, ColorSwatchPicker |
| Controls | Checkbox, CheckboxGroup, Switch, RadioGroup, Slider |
| Data Display | Avatar, AvatarGroup, Badge, Chip, Table, Kbd, Description, Meter, ProgressBar, ProgressCircle, Skeleton, Spinner |
| Date and Time | Calendar, RangeCalendar, DateField, DatePicker, DateRangePicker, TimeField |
| Feedback | Alert, Toast |
| Forms | Form, Fieldset, FieldError, Label, Input, InputGroup, InputOTP, TextArea, TextField, NumberField, SearchField, Select, ComboBox, Autocomplete, ErrorMessage |
| Layout | Card, Separator, Surface, ScrollShadow, Toolbar |
| Media | — (no image/video components) |
| Navigation | Breadcrumbs, Link, Pagination, Tabs |
| Overlays | Modal, AlertDialog, Drawer, Popover, Tooltip |
| Pickers | (covered above — the pickers are Select/ComboBox/Date groups) |
| Typography | Typography, Description, Kbd |
| Utilities | Disclosure, DisclosureGroup, Accordion, Form |

## When it is the right answer

- A **product surface**: dashboards, account areas, admin panels, settings,
  anything with tables, modals, date pickers, comboboxes or form validation.
- A project that must be accessible **without** hand-auditing every control.
- A Tailwind v4 + React 19 codebase where you want behaviour and a11y solved and
  the look restyled, not a design system you must adopt wholesale.

## When it is the wrong answer

- A **marketing site with an art direction of its own**. The components carry a
  recognisable HeroUI surface (radius, shadow, motion timing) and each one you
  restyle costs more than writing the element.
- Anything where the visual is the product: hero, editorial sections, image
  grids, ceremony.
- Server-rendered brochure pages with no interactivity beyond a nav.

## Gotchas

- `@heroui/styles` must come **after** `tailwindcss` in the CSS import order, or
  utilities win against component styles in the wrong places.
- Provider setup is required (`HeroUIProvider`) for overlays and toasts to
  portal and to read the theme.
- Its default motion is its own; a site with a strict motion budget must either
  accept it or override the timing tokens globally.
- Compound components (`<Select><Select.Item/></Select>`) — reading the docs page
  matters. Guessing the parts from the component name produces errors that look
  like type failures.
