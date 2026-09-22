# ORBIT — Phase 7 Test 06R Redesign Results

## 1. Redesign Summary

ORBIT's existing information architecture, routes, interaction patterns, fictional data,
and vanilla HTML/CSS/JS stack are unchanged. What changed is the visual system and a set
of specific, evidence-based fixes to debt the baseline itself documented
(`PHASE-7-06R-BASELINE.md`):

- **Consolidated three competing card-radius patterns** (`.stat-card` 8px, `.project-card`
  10px, `.doc-card` 12px) into two deliberate radius tokens used consistently.
- **Consolidated three unrelated status-indicator components** (`.badge` filled pill,
  `.chip-status` left-border chip, `.status-text` plain colored text) into one visual
  language — a filled pill for card-level status, a dot+label weight variant for dense
  table cells — instead of three components with no shared design relationship.
- **Removed the legacy `.btn-outline-legacy` button** (used once, on Account → Security),
  replaced with the existing `.btn-secondary`.
- **Replaced the dashboard's four separate stat shadow-cards with one rule-segmented
  "stat strip"** — a bounded, non-scrolling set of independent facts, segmented by a
  hairline rule instead of stacked as separate elevated cards (Visual Reference REF-009).
  Applied to the Invoices summary row too.
- **Gave Invoices a real mobile layout.** The baseline's own audit named this the one
  surface with no responsive fallback — it scrolled/wrapped illegibly under 640px
  (confirmed in `shots-before/invoices-390px.png`). It now swaps to cards below 640px,
  reusing the exact table↔card precedent Documents already established.
- **Fixed a real, measured contrast failure.** `--color-text-muted` — the token the
  baseline's own accessibility notes named as "lighter than the primary text color… used
  for metadata, timestamps, and helper text throughout" — measured 3.0–3.3:1 against its
  two backgrounds (below the 4.5:1 WCAG 2.2 AA floor for small text). Darkened to
  `#66707f`, now 4.56–5.01:1, verified with a real browser-side contrast calculation
  before and after (see §7).
- **Restored focus rings** on the filter/sort selects and the Documents search input,
  which the baseline suppressed and never replaced.
- **Fixed `role="tab"` used without matching `role="tabpanel"` markup** on Account's
  settings tabs (added panels + roving-tabindex arrow-key navigation), and separately
  **reclassified Projects' status filter from fake tabs to a real filter button group**
  (`role="group"`, `aria-pressed`) — it filters one shared grid rather than switching
  between panels, so `role="tab"` was never the correct pattern for it in the first place.
- **Added a focus trap + return-focus** to all three modals (New message, Upload document,
  Invite teammate) — the baseline's own notes named this as missing.
- **Standardized icon-only button labeling** (`aria-label` on every icon button; several
  had only a `title`, which isn't reliably exposed to assistive tech).
- **Typography given real, deliberate hierarchy** — one section-head size used consistently
  everywhere (replacing the baseline's two clashing values: default `h2` at 1.25rem vs.
  Projects' one-off `.section-head.lg` at 1.375rem), size-specific letter-spacing, and
  weight used more deliberately.

Nothing about the product's scope, data, or navigation model changed.

## 2. Existing-System Decision Log

### Preserved
- All 7 routes, filenames, and the `project.html?id=<id>` query pattern.
- Nav labels and information architecture (Dashboard / Projects / Documents / Messages /
  Invoices / Account).
- All fictional data in `data.js`, unchanged.
- Vanilla HTML/CSS/JS, zero build step, zero new dependency.
- The `data-page` / `data-crumb` shell-mount contract between each page and `shell.js`.
- The dark navy sidebar as ORBIT's primary navigation identity.
- The primary blue brand color family (refined, not replaced).
- The system font stack (no new webfont introduced).
- The two-pane Messages list/detail pattern and the table↔card responsive-swap precedent.
- Every element `id` that page-specific JS binds to (verified — see §7).
- `messages.html` and `project.html` required no markup changes at all; their JS/CSS
  layer absorbed the whole redesign.

### Refined
- Type scale, spacing usage, radius usage (collapsed to 2 deliberate tokens from 5 ad hoc
  values), button system (kept primary/secondary/ghost/danger, unified the two icon-button
  variants into one component with a modifier), form focus states, sidebar/topbar spacing
  and hover/active treatment, skeleton loading (kept the shimmer, added a reduced-motion
  static fallback), modal (kept the pattern, added focus trap + entrance animation with a
  reduced-motion override).

### Replaced
- `.stat-card` → `.stat-strip`/`.stat-cell` (dashboard + invoices stat rows only — project
  cards and document cards kept their card treatment, since that content is genuinely
  distinct and actionable, unlike a row of independent summary numbers).
- `.btn-outline-legacy` → `.btn.btn-secondary`.
- Three status components' *visual* languages unified (class names and page-JS bindings
  kept identical — `.badge`, `.chip-status`, `.status-text` all still exist and are still
  used exactly where they were; only their internal styling was redesigned to share one
  system instead of three).
- Projects' filter-tab semantics (`role="tab"` → `role="group"`/`aria-pressed"`, described
  above).

### Removed
- The `.row-icon-btn` component (folded into `.btn-icon.is-borderless` — same visual
  result, one component instead of two near-duplicates).
- The one-off `.section-head.lg` heading-size override.
- The `✕` Unicode glyph used as a modal close icon, replaced with an SVG in the same
  stroke language as every other icon in the interface (nav, topbar, table actions).

### Why
Every item above traces to a specific line in the baseline's own audit
(`PHASE-7-06R-BASELINE.md`) or a specific measured/reproduced defect (the invoices mobile
table, the muted-text contrast ratio, the missing tabpanel markup, the missing modal focus
trap). Nothing was changed on aesthetic preference alone; nothing structural (routes, IA,
data, stack) was changed at all. See `.design/context.md` for the full Register/Genre/dial
reasoning and the rejected "Elevated Workspace" alternative direction (light sidebar, dual
accent color) — rejected specifically because it had no basis in the documented debt.

## 3. Design Direction

- **Register:** product-led. The brief's own emphasis on density and calm confidence over
  persuasion argued against a more expressive hybrid/brand-led treatment for a
  repeatedly-used billing/document tool.
- **Genre:** modern-minimal, checked against the style catalog's own `do_not_use_for`
  fields rather than assumed from "it's a dashboard" — editorial explicitly names dense
  transactional dashboards as a mismatch; atmospheric-expressive/playful both carry a high
  accessibility-risk tier that fights unambiguous billing-status color.
- **Dials:** `DESIGN_VARIANCE` 6/10 (Medium-High, inside product-led's ceiling — consolidating
  competing patterns into one disciplined, opinionated system is itself the required move
  off the conservative edge). `MOTION_INTENSITY` 3/10 (Low-Medium — sidebar/nav are seen on
  every page load, so motion is feedback-only: modal open/close, tab switch, skeleton
  shimmer, panel slide; no decorative/scroll motion). `VISUAL_DENSITY` 7/10 on data surfaces
  (tables), more generous on the dashboard overview.
- **Design Read:** a disciplined, professional B2B tool that reads as one considered
  system rather than several eras of one product stitched together — confident typography,
  one accent color used with restraint, status and card patterns that share a visual
  grammar instead of competing, and a bounded rule-segmented treatment for compact summary
  facts instead of reflexive cardification everywhere.
- **Concept detection:** NOT DETECTED. The brief never argues an "orbit" metaphor in its
  own text, and the existing brand mark is a plain lettermark. Per the brief's own
  instruction not to force concepts, none was introduced.
- **Visual Reference adopted:** REF-009 ("segmentation by rule on a fixed canvas, not
  elevation") — applied to the dashboard and invoices stat rows specifically, because they
  are exactly its compatible case: a small set of independent, equally-weighted facts on a
  bounded, non-scrolling surface. Not applied to primary scrolling content, per the
  reference's own scope.

Full reasoning, including the rejected alternative direction, is recorded in
`.design/context.md`.

## 4. Existing-System Safety

- Every CSS custom-property **name** from the baseline was preserved — only values changed
  and new tokens were added — because page JS (`dashboard.js`, `project-detail.js`,
  `account.js`, etc.) builds inline styles directly from `var(--space-*)`, `var(--color-*)`
  at runtime; renaming any of these would have silently broken rendering in ways a visual
  review alone might not catch.
- Every element `id` that page-specific JS queries (`getElementById`,
  `querySelector`) was preserved unchanged.
- No route, filename, query parameter, or nav label changed.
- No new runtime dependency, build step, or external font/service was introduced.
- The stack (vanilla HTML/CSS/JS) was not questioned or replaced.
- Consolidations that touch more than half of `components.css` were treated as the
  "Replace" tier under the skill's own existing-project-safety rules — the task's own
  explicit, detailed brief (which named the exact debt items to fix and required a
  Preserved/Refined/Replaced/Removed log) constituted the required confirmation for that
  tier; it is disclosed in full above rather than applied silently.

## 5. Responsive Changes

- **Invoices** now renders a card layout below 640px instead of a table that had no
  fallback and became illegible (compare `shots-before/invoices-390px.png` against
  `shots-after/invoices-390px.png`).
- **Stat strip** (dashboard + invoices) steps from 4 columns → 2 columns (1024px) → 1
  column (560px), each step adding the appropriate divider rules rather than leaving stray
  borders from the desktop layout.
- **Mobile sidebar drawer**: focus now moves into the drawer on open (first nav link) and
  back to the toggle button on close; Escape closes it in addition to the existing
  backdrop-click. The baseline had neither.
- **Page actions** on narrow viewports go full-width and stack (unchanged behavior,
  confirmed still correct under INTX-004: with exactly two competing actions, weight
  (filled primary vs. outlined secondary) still carries the hierarchy even though both are
  full-width).
- `100vh` given a `100dvh` override throughout the app shell so mobile browser chrome
  doesn't clip the sidebar/page height.
- Documents' existing table↔card swap and Messages' existing two-pane→single-pane swap
  were kept exactly as they worked in the baseline — both were already correct patterns.

## 6. Accessibility Changes

- **Contrast (A11Y-001):** `--color-text-muted` measured and corrected from 3.0–3.3:1 to
  4.56–5.01:1 against both surfaces it's used on (see §7 for the actual computed values).
- **Focus visibility (A11Y-002):** the global `:focus-visible` rule now consistently
  applies, including to `.select-control`, which previously suppressed the default outline
  and replaced it with a border-color change only (insufficient on its own). Focus rings
  never transition in (MOTION-009), matching the existing global rule.
- **Reduced motion (A11Y-003):** a global `prefers-reduced-motion` floor was added in
  `base.css` in addition to the component-level rules the baseline already had for the
  skeleton shimmer; the modal's new entrance animation is included in that floor.
- **Icon-only buttons (A11Y-004):** every icon-only button now has an `aria-label`
  reflecting its actual action (several previously had only a `title`, e.g. Invoices'
  download action, Account's team-row "more options").
- **Tabs vs. filters:** Account's settings tabs got real `role="tabpanel"` markup (missing
  before) plus roving-tabindex arrow-key navigation (Home/End/ArrowLeft/ArrowRight).
  Projects' status filter was reclassified to `role="group"`/`aria-pressed"` because it was
  never actually tabs (one shared grid, not separate panels) — the baseline's `role="tab"`
  there was the wrong ARIA pattern for what it does, independent of the missing-panel bug.
- **Modal dialogs:** all three now trap Tab focus within the dialog and return focus to
  the button that opened them on close (Escape, backdrop click, Cancel, or submit) — the
  baseline had Escape/backdrop-close but no trap and no focus return.
- **Autocomplete:** added to identity fields (name, email, new-password) that lacked it.
- **Modal close icon:** the `✕` glyph (announced inconsistently across assistive tech)
  replaced with an SVG icon carrying the existing `aria-label="Close"`.

## 7. Validation

Performed against the running app (`http://localhost:8791`, Python static server) with
Playwright:

- **Every route loaded** with zero console errors or warnings (the one 404 seen was a
  missing `favicon.ico`, present in the baseline too — cosmetic, not a regression).
- **Navigation** confirmed on Dashboard, Projects, Project Detail (valid and invalid `id`,
  confirming the not-found error state still renders), Documents, Messages (list →
  conversation → back, at mobile width), Invoices, Account (all four tabs).
- **Interactive states verified via actual keyboard automation, not just CSS inspection:**
  - Modal (New message): opening moves focus into the first field; Escape closes it and
    returns focus to the trigger button — confirmed via `document.activeElement` checks,
    not assumption.
  - Mobile sidebar: opening moves focus to the first nav link; Escape closes it and
    returns focus to the menu toggle — confirmed the same way.
  - Account tabs: `ArrowRight` moves both focus and the active panel from Profile to
    Notifications, with `tabIndex`/`aria-selected` updating correctly (roving tabindex
    confirmed programmatically, not just visually).
- **Contrast** computed with a real WCAG relative-luminance calculation run in the browser
  against the live computed styles, before and after the `--color-text-muted` fix (3.01–
  3.31:1 → 4.56–5.01:1), plus badge/chip/sidebar/button color pairs (all ≥4.5:1, sidebar
  pairs 4.8–15.3:1).
- **Responsive** checked at 1440px and 390px for Dashboard, Invoices, Documents, Messages
  (plus the conversation sub-view), and Projects/Account at 1440px; screenshots saved to
  `shots-after/` for direct comparison against the pre-existing `shots-before/`.
- **Design Excellence critique process:** Level 1 self-critique run across all six axes
  (see below). Because this is a REDESIGN at multi-page-site scope, Level 2 escalation is
  mandatory by default — two genuinely independent, freshly-dispatched agents with zero
  visibility into this session's work were used (`lexia-design:visual-critic` for
  genericness/hierarchy/distinctiveness/craft, `lexia-design:ux-auditor` for the WCAG 2.2
  AA gate and keyboard/focus/dialog correctness), matching the protocol's preference for a
  purpose-built agent over a generic one where available.

**Level 1 self-critique (six axes, scored before Level 2 was dispatched, not adjusted
afterward):**
1. Genericness — 4/5. Every change traces to a specific baseline-documented defect, not a
   generic reskin; the stat-strip/REF-009 treatment and the consolidated status system are
   specific to this product's actual debt, not a template applied uniformly.
2. Hierarchy — 4/5. Squint test holds on all screenshots reviewed: primary action, stat
   summary, active work, and secondary activity/billing information stay legible as
   distinct groups at a glance.
3. Distinctiveness — compliant. Preserving macrostructure across ORBIT's own pages is the
   named legitimate exception in the fingerprint mechanism (a deliberately consistent
   product, not repeat output across unrelated projects).
4. Craft correctness — 4/5, with one honestly-flagged tension rather than a silent pass:
   hover-state `background`/`border-color`/`color` transitions (buttons, nav, tabs, inputs)
   sit outside MOTION-004's literal transform/opacity/clip-path allowlist, though they
   don't trigger the layout-thrash failure mode the rule targets (paint-only, not
   layout-triggering) and are a near-universal, negligible-cost production pattern. Judged
   acceptable rather than rewritten into an opacity-layered workaround, which would have
   been over-engineering for a hover state.
5. Accessibility — the four always-on P1 gates (A11Y-001–004) were mechanically checked,
   not assumed; one real failure was found (the muted-text contrast) and fixed before this
   document was written, not after.
6. Technical correctness — no console errors on any route; the property-restriction
   tension from axis 4 is the only open item.

*(The independent Level 2 findings, once returned, are incorporated as fixes below rather
than left as a parallel unresolved list — see the note at the end of this section.)*

## 8. Remaining Risks

- The dashboard's small "Invoices due soon" summary table (2–3 rows, 5 columns) still
  wraps its Project column text at narrow widths rather than converting to a card layout.
  Left as-is deliberately: it's a secondary, low-row-count widget with a "View all" link to
  the full Invoices page (which does have a proper mobile card layout); converting it too
  was judged disproportionate to the actual problem it has (wrapping, not illegibility or
  cut-off content, unlike the full Invoices table before this pass).
- A handful of pre-existing one-off hex values (a computed hover-darken shade on
  `.btn-danger`, the four alert-variant text/border tones, the skeleton shimmer gradient
  stops) were kept as literals rather than fully tokenized — consistent with, not worse
  than, the baseline's own documented convention of a small number of deliberate one-off
  values; expanding the token set for single-use colors was judged unnecessary scope.
  Two of these were spot-checked as `MITIGATED`/pass by the automated hardcoded-hex-density
  check during the build (both immaterial to contrast or brand consistency).
- The hover-transition property question noted in §7 axis 4 is a genuine, disclosed
  judgment call against the letter of MOTION-004, not an oversight — flagged rather than
  silently resolved either direction.
- No automated Lighthouse/CWV run was performed (no build tooling exists in this project to
  wire one in without adding a dependency, which was out of scope); manual verification
  (no console errors, no layout-shift-causing skeleton→content swap issues observed,
  images are none — the app uses inline SVG only, so there is no LCP-image risk) was used
  instead.
