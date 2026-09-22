# Accessibility — Rule Catalog (T2)

**Correction note (Phase 4):** this file previously declared every rule P1 "by construction." That was an Authority Hierarchy violation — `SKILL.md` §3's P1 list is narrow and enumerated (contrast, focus-visible, keyboard operability, reduced-motion, plus the non-accessibility items on that list). Only a rule that genuinely matches one of those four named floors is P1; every other rule here is real, load-bearing accessibility guidance, just not one with authority to override an explicit user instruction. Each rule below now states its own `layer` individually — see `AUDIT-3.5.md` for the correction record.

Split into **always-on** (every task, every scope) and **conditional** (scoped to the platform/interaction actually present — do not let these bleed into contexts they don't apply to).

---

## Always-on

### A11Y-001 — Contrast, current through WCAG 2.2
- **category:** accessibility · **layer:** P1 (safety — matches "contrast" on the `SKILL.md` §3 enumerated list)
- **principle:** meet WCAG 2.2 contrast criteria, not folklore frozen at 2.0/2.1. Includes newer, less-known criteria a model is least likely to know natively: `focus-not-obscured` (2.2 AA), `web-target-size` (2.2 AA, 24×24 CSS px minimum — do not substitute native units), `consistent-help` (2.2 A), `redundant-entry` (2.2 A).
- **severity:** critical
- **applicability:** universal, including placeholder text (still needs 4.5:1 — commonly missed).
- **exceptions:** none.
- **evidence:** these are exactly the criteria most likely absent from a model's baseline knowledge, making them the highest-leverage to hard-code.
- **freshness:** source: WCAG 2.2 spec (external authority, not one of the six extracted sources — cite the spec directly, not this file, for the full criteria list). status: review_interval_days: 365 (WCAG revisions are infrequent but do happen).
- **validation:** mechanical-countable (compute contrast ratio for every (foreground, background) pair).
- **remediation:** adjust lightness, not hue, to restore contrast where possible (see COLOR-005); document any deliberate override in `.design/context.md` Known Exceptions.

### A11Y-002 — Keyboard operability + `:focus-visible`
- **category:** accessibility · **layer:** P1 (safety — matches both "focus-visible" and "keyboard operability" on the enumerated list)
- **principle:** every interactive element reachable and operable by keyboard alone; focus indicator via `:focus-visible` (never bare `:focus`, which fires on mouse click too), 3:1 contrast against its background, 2–3px, consistent treatment across the interface.
- **severity:** critical
- **applicability:** universal.
- **exceptions:** none.
- **evidence:** "designing hover without focus" is the single most common a11y miss — keyboard users never see hover.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (static: every `:hover` rule has a `:focus-visible` counterpart) + rendered (Enhanced mode only: actual keyboard walk).
- **remediation:** add the missing `:focus-visible` rule; never remove focus outlines without a compliant replacement.

### A11Y-003 — Reduced motion
- **category:** accessibility · **layer:** P1 (safety — matches "reduced-motion respect" on the enumerated list)
- **principle:** cross-reference `MOTION-007`. Stated here because it is a hard accessibility gate, not optional motion polish. This entry is a pointer, not a duplicate — full content lives at MOTION-007.
- **severity:** critical
- **applicability:** universal.
- **validation:** mechanical-countable.
- **remediation:** see MOTION-007.

### A11Y-004 — Icon accessibility is role-conditional
- **category:** accessibility · **layer:** P5 (UX/usability — a real, important accessibility concern, but not one of the four items named on the `SKILL.md` §3 enumerated P1 list; it does not carry authority to override an explicit user instruction)
- **principle:** the same icon's accessibility treatment depends on usage: decorative-beside-visible-text → hidden from the accessibility tree (`aria-hidden="true"`); meaningful-standalone → needs a text alternative; interactive-control → needs an accessible name and state.
- **severity:** major
- **applicability:** universal — "icons need alt text" is wrong roughly as often as it's right; this makes it conditional on role, the actually-correct WCAG position.
- **exceptions:** none — this rule *is* the exception-handling for the naive version.
- **evidence:** common source of both over-correction (redundant alt text next to a labeled button) and under-correction (an icon-only button with no accessible name).
- **freshness:** status: permanent.
- **validation:** mechanical-countable (check icon usage context against the three cases).
- **remediation:** apply the matching treatment for the detected role.

## Conditional (scoped — never applied outside the stated context)

### A11Y-005 — Touch target size
- **category:** accessibility · **layer:** P5 (UX/usability — not on the `SKILL.md` §3 enumerated P1 list; explicitly named in the Phase 4 correction as an example of a rule that must not carry P1 override authority)
- **principle:** minimum 24×24 CSS px (WCAG 2.2 AA); native/mobile app contexts commonly target 44×44pt.
- **severity:** major
- **applicability:** native/mobile or touch-capable interfaces only. **Do not apply to a mouse-driven desktop dashboard** — it's noise there, not signal.
- **exceptions:** desktop-only, no-touch interfaces.
- **evidence:** UI UX Pro Max's own explicit platform-scope banner pattern — a positive example of correctly scoping a real rule, kept intentionally narrow here.
- **freshness:** status: permanent.
- **validation:** mechanical-countable, only when platform scope = mobile/native/touch.
- **remediation:** enlarge the tap target via padding, not just visual size.

### A11Y-006 — Dragging alternative
- **category:** accessibility · **layer:** P1 (safety — a drag-only interaction with no keyboard alternative is a direct "keyboard operability" failure, the item named on the enumerated list; kept P1 on that basis, not as a general drag/UX preference)
- **principle:** any author-created drag interaction needs a single-pointer and keyboard alternative (WCAG 2.2 AA).
- **severity:** major
- **applicability:** only when the build includes drag interactions.
- **exceptions:** none once drag exists.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** add a non-drag path (buttons, keyboard reorder) alongside the drag interaction.

### A11Y-007 — Form-field state bugs
- **category:** accessibility · **layer:** P7 (production hardening — these are implementation-correctness bugs, not on the `SKILL.md` §3 enumerated P1 list; explicitly named in the Phase 4 correction as an example — "form-field implementation preferences" — that must not carry P1 override authority)
- **principle:** border-width must never change between input states (use color/outline/box-shadow instead — width changes shift layout); focus ring is `outline`, not `border`; input height matches adjacent button height on the same form; helper-text slot reserves `min-height: 1lh` even empty, so an appearing error doesn't reflow the page; disabled state uses three simultaneous signals (opacity + cursor + the native `disabled` attribute), never opacity alone.
- **severity:** major
- **applicability:** only when the build includes form UI.
- **exceptions:** none.
- **evidence:** named, specific, recurring implementation bugs generic "handle all states" advice doesn't catch — several read as mined from real production incidents.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (border-width diff across states; helper-text min-height presence; disabled-state signal count).
- **remediation:** apply the specific fix listed for the detected violation.

### A11Y-008 — Never disable zoom
- **category:** accessibility · **layer:** P5 (UX/usability — not on the `SKILL.md` §3 enumerated P1 list; explicitly named in the Phase 4 correction — "zoom behavior" — as an example that must not carry P1 override authority)
- **principle:** `user-scalable=no` / `maximum-scale=1` is an accessibility failure. If it was added to prevent iOS input-zoom, fix the root cause (16px minimum input font-size) instead.
- **severity:** critical
- **applicability:** universal wherever a viewport meta tag is set.
- **exceptions:** none.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (grep viewport meta tag + input font-size).
- **remediation:** remove the scale lock; set input font-size ≥16px.
