# Motion — Rule Catalog (T2)

Canonical motion authority: this file is the *only* motion decision system in this skill. No other reference file defines a competing duration table, easing rule, or property list — they reference these ids. Source: Emil Kowalski's framework, judged in `FORENSIC-EXTRACTION.md` §9 as the deepest, most rigorously reasoned motion content across all six sources; non-overlapping contributions from Anthropic and Hallmark are merged in, not kept as separate tables.

Canonical decision sequence (walk in order): should it animate → purpose → interaction type → property → easing → duration → interruptibility → accessibility → performance → gesture physics (`gesture-physics.md`, T4, loaded only if drag/gesture is in scope).

---

### MOTION-001 — Frequency gates whether it animates at all
- **category:** motion · **layer:** P5 (UX)
- **principle:** 100+ exposures/day (keyboard shortcuts, command-palette toggles) → never animate. Tens/day → remove or drastically reduce. Occasional → standard treatment. Rare/first-time → delight budget applies.
- **severity:** major
- **applicability:** universal; generalizes past animation to any repeat-exposure UI decision (notifications, tooltips, onboarding hints).
- **exceptions:** none — this is the entry gate, not a style choice.
- **evidence:** high-frequency motion becomes fatigue, not delight; this is the single most transferable, evidence-backed rule found across all six sources.
- **freshness:** status: permanent.
- **validation:** self-critique-prompt (ask: how often does a user see this element per session?).
- **remediation:** if frequency is high and motion exists, delete it before doing anything else — cheaper than tuning it.

### MOTION-002 — Purpose must come from a fixed vocabulary
- **category:** motion · **layer:** P5
- **principle:** every animation must be justifiable as feedback, spatial consistency, state indication, preventing a jarring change, explanation, or delight-at-rare-tier-only. "It looked cool" is explicitly disqualified.
- **severity:** major
- **applicability:** universal. `MOTION_INTENSITY` band (SKILL.md §4) gates which purposes are eligible by default — Low band suppresses the delight tier.
- **exceptions:** none.
- **evidence:** gives a falsifiable test instead of "use tasteful animation."
- **freshness:** status: permanent.
- **validation:** self-critique-prompt.
- **remediation:** if no purpose from the list applies, remove the animation.

### MOTION-003 — Interaction type: decorative vs. communicative
- **category:** motion · **layer:** P5
- **principle:** motion that answers a user's action (opening, expanding, confirming) is welcome without restriction, because it shows what changed. Non-triggered, decorative motion (scattered fade-and-slide-up-per-section, hover-on-every-card) should be restricted to one orchestrated moment, not scattered everywhere.
- **severity:** major
- **applicability:** universal.
- **exceptions:** narrative/marketing sequences where the decorative moment IS the point — declare it explicitly, don't default to it.
- **evidence:** distinguishes the single most common generic-AI-output motion pattern (scattered decorative reveal) from legitimate state-change motion.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (count non-triggered animation instances per page; flag >1 orchestrated moment without justification).
- **remediation:** consolidate scattered decorative motion into one moment, or cut it.

### MOTION-004 — Property restriction: no layout-affecting animation
- **category:** motion · **layer:** P7 (performance)
- **principle:** never animate a property that triggers layout/reflow — `width`/`height`/`margin`/`padding`/`top`/`left`/`right`/`bottom`, or a framework's `x`/`y`/`scale` shorthand applied over a non-composited property. That is the specific harm this rule exists to prevent, not a ban on animation generally. `transform`, `opacity`, and `clip-path` are the preferred, GPU-composited properties for movement, scale, and reveal effects and remain the default choice for that purpose. Paint-only properties — `color`, `border-color`, `background-color` — do not trigger layout/reflow, so a hover or state transition on them is not a MOTION-004 finding; this is a scoped carve-out for paint-only feedback, not a general license to animate anything, and it does not relax MOTION-001/002/003's purpose and frequency gates. `prefers-reduced-motion` handling for any transition, paint-only included, stays MOTION-007's responsibility, not this rule's.
- **severity:** critical
- **applicability:** universal — established web-performance fact, not opinion.
- **exceptions:** none.
- **evidence:** non-composited, layout-affecting property animation causes layout thrash and jank, especially on mobile — the specific, measurable harm this rule targets. Paint-only property changes repaint without triggering layout and do not cause that harm, which is why they sit outside this rule's scope rather than inside a disclosed exception to it.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (grep animated/transitioned CSS properties; flag any that trigger layout/reflow per the list above; `color`/`border-color`/`background-color` are not flagged).
- **remediation:** rewrite a layout-affecting animated property to a transform/opacity equivalent (e.g. `grid-template-rows: 0fr → 1fr` for height, not `height: auto`). Paint-only properties need no rewrite.

### MOTION-005 — Duration budget by element type
- **category:** motion · **layer:** P5
- **principle:** press feedback 100–160ms, tooltips 125–200ms, dropdowns 150–250ms, modals 200–500ms, hard ceiling ~300ms for any UI (non-marketing) motion.
- **severity:** moderate
- **applicability:** the *shape* (budget scoped by element type, not one global duration) is universal; the specific millisecond values are swappable defaults, not physical law.
- **exceptions:** marketing/narrative sequences may run longer, declared explicitly.
- **evidence:** per-element-type budgets prevent both "everything is instant" and "everything drags."
- **freshness:** status: permanent (structural pattern); specific ms values: source Emil Kowalski, confidence: house-style-default, review not required (not an AI-tell, a design-system convention).
- **validation:** mechanical-countable (parse declared durations against the table).
- **remediation:** clamp outlier durations to the nearest budget band.

### MOTION-006 — Interruptibility: transitions/springs, not keyframes
- **category:** motion · **layer:** P5
- **principle:** use CSS transitions (or springs) — never `@keyframes` — for anything triggered rapidly or interruptibly (toasts, toggles, drags), because transitions retarget from the current value while keyframes restart from zero. Use springs specifically for gesture-driven/interruptible motion, because springs carry velocity through interruption.
- **severity:** major
- **applicability:** universal for any re-triggerable UI.
- **exceptions:** one-shot, non-interruptible sequences (a page-load reveal that only ever plays once) may use keyframes.
- **evidence:** the single most common motion bug in generated interfaces — a rapidly re-toggled element visibly "jumps" because keyframes restarted.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag `@keyframes` on interactive/toggleable elements).
- **remediation:** convert to a CSS transition or spring config.

### MOTION-007 — `prefers-reduced-motion`: gentler, not zero
- **category:** motion · **layer:** P1 (safety — on the enumerated accessibility list)
- **principle:** under `prefers-reduced-motion`, keep opacity/color transitions that aid comprehension; drop movement/position changes.
- **severity:** critical
- **applicability:** universal, WCAG-aligned.
- **exceptions:** none.
- **evidence:** motion-triggered vestibular disorders; zeroing everything also removes comprehension cues, so "gentler" beats "off."
- **freshness:** status: permanent.
- **validation:** mechanical-countable (verify a `@media (prefers-reduced-motion: reduce)` block exists and movement-class properties are neutralized within it).
- **remediation:** add the media query block; do not ship without it.

### MOTION-008 — Hover gated behind `(hover: hover) and (pointer: fine)`
- **category:** motion · **layer:** P5
- **principle:** gate hover-triggered animation behind capability detection, not screen-size proxying, to prevent sticky-hover-after-tap on touch devices.
- **severity:** major
- **applicability:** universal.
- **exceptions:** none.
- **evidence:** touch devices fire `:hover` on tap and never clear it — a well-documented, easy-to-miss bug class.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag bare `:hover` rules on interactive elements without the media-query guard).
- **remediation:** wrap hover-triggered rules in the capability query.

### MOTION-009 — Focus rings appear instantly, never transition in
- **category:** motion · **layer:** P1 (safety)
- **principle:** a focus indicator must exist at the start of any transition, not after it completes — a keyboard user needs it immediately.
- **severity:** critical
- **applicability:** universal.
- **exceptions:** none.
- **evidence:** adding "polish" transitions indiscriminately catches the one indicator that must never animate in.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag `transition` on `:focus-visible` outline/box-shadow properties).
- **remediation:** remove the transition on the focus-ring property specifically; other properties on the same element may still transition.

### MOTION-010 — Tooltip delay differentiated by input modality
- **category:** motion · **layer:** P5
- **principle:** hover-triggered tooltip delay 800–1000ms (user is scanning, not committed); focus-triggered delay 0ms (keyboard user already committed via Tab). Equal delays for both is a named tell of not having considered input modality.
- **severity:** moderate
- **applicability:** universal interaction-design fact.
- **exceptions:** none.
- **evidence:** hover and focus signal different confidence levels; treating them identically ignores that.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** split the delay by trigger type.

### MOTION-011 — Bounce/elastic easing: conditional, not banned
- **category:** motion · **layer:** P8 (aesthetic)
- **principle:** default off for UI state transitions (toggles, tab switches). Allowed for gesture-driven/drag-to-dismiss interactions and playful-genre contexts, because springs there carry velocity through interruption and bounce is expected physically.
- **severity:** minor
- **applicability:** `genre: playful` or any gesture/drag interaction raises eligibility; `genre: modern-minimal` or `product-led` register lowers it toward off.
- **exceptions:** declared per-genre as above — this is itself the resolved form of a cross-source conflict (one source banned bounce absolutely; the more physically-grounded source allows it for gesture contexts). See `FORENSIC-EXTRACTION.md` Conflict Map #1.
- **evidence:** an absolute ban contradicts legitimate gesture-physics use; an absolute allowance produces dated-feeling static-UI bounce.
- **freshness:** status: permanent (the resolution is structural, not trend-dependent).
- **validation:** self-critique-prompt.
- **remediation:** if bounce appears on a non-gesture, non-playful-genre element, remove it.
