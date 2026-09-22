# Phase 7 — Test 02 Results

## 1. Brief

Build a complete, production-quality, responsive marketing website (in Spanish) for "Signal," a fictional collaborative customer-feedback platform for product teams. Six pages: Home, Cómo funciona, Producto, Precios, Recursos, Contacto. The product moves teams from scattered customer feedback → recurring themes → patterns → prioritized opportunities → product decisions. Primary CTA "Probar Signal," secondary CTA "Ver cómo funciona." Explicit instructions to avoid generic SaaS/AI-startup visual tells (gradient heroes, glassmorphism, dashboard-screenshot heroes, repetitive card grids, fabricated metrics/testimonials/logos) and to find a stronger, product-specific way to communicate the hero's value proposition. No conceptual metaphor was to be manufactured unless the brief actually supported one.

## 2. Routing

- **Scope:** multi-page site
- **Project state:** genuinely-empty (only `.claude/` existed)
- **Task mode:** BUILD
- **Register:** product-led
- **Genre:** modern-minimal
- **DESIGN_VARIANCE:** 5 (Medium)
- **MOTION_INTENSITY:** 3 (Low)
- **VISUAL_DENSITY:** 6 (Medium)

## 3. Design Direction

### Design Read

"Reading this as: product-led modern-minimal work, variance=Medium, motion=Low, density=Medium." Evidence: the brief's own descriptors (intelligent, precise, confident, contemporary, useful, trustworthy, product-focused; "serious modern software product, not a generic AI startup") map to `modern-minimal`'s definition (functional hierarchy, low decoration, restrained-to-committed color) more directly than to `editorial` (narrative/publication register — this brief is operational), `atmospheric-expressive` (explicitly contradicted by the brief's own avoidance list), or `playful` (B2B tool for PMs/CS, not consumer/youth). This was checked against the brief's actual language, not defaulted from "SaaS = modern-minimal."

### Concept

**HYPOTHESIS**, not detected. "Signal" plausibly evokes the signal-vs-noise sense (extracting a meaningful signal from noisy, repetitive feedback) — a real, checkable association given the product's stated mechanism. But the brief's own text never states this naming rationale, never gives it recurring emphasis, and the user never instructed the system to build around it. Per the three-state model, a brand name alone is never sufficient for DETECTED/EVIDENCED. This was logged as a hypothesis only and was deliberately not turned into a governing visual metaphor (no oscilloscope/waveform imagery, no literal "noise vs. signal" motif) — it was allowed to loosely touch one line of copy at most and nothing structural.

### Concept → Structure

**LAYOUT-009 not activated.** Its applicability is scoped to a DEFINE outcome of DETECTED/EVIDENCED specifically; a HYPOTHESIS outcome does not activate the mandatory translation requirement. Since Concept Detection resolved to HYPOTHESIS, this rule correctly did not fire, and no organizing-surface translation was logged as concept-derived. The hero's "pipeline spine" macrostructure (below) was chosen for other, independent reasons — it directly visualizes the workflow the brief itself enumerates (Collect→Organize→Identify→Prioritize→Decide), not a translation of the signal/noise hypothesis.

### Visual References

Loaded at DIRECT (new visual system, greenfield). All 9 entries in `visual-references.md` were considered against Register=product-led / Genre=modern-minimal / dials above:

- **Rejected — incompatible with product-led register:** REF-001 (asymmetric column pairing), REF-003 (wayfinding as index), REF-004 (oversized numerals as dividers). Each names product-led explicitly in `do_not_apply_to`.
- **Rejected — motion band too low:** REF-002 (dominant fixed focal element through scroll) and REF-006 (counted-index reveal transitions) both require Medium–High `MOTION_INTENSITY`; this brief is Low (3).
- **Rejected — no real subject match:** REF-005 (process imagery over polished photography) — Signal has no physical "process" to photograph; using it would have meant fabricating process imagery.
- **Rejected — wrong content type:** REF-008 (task-state hierarchy over persuasion hierarchy) explicitly excludes brand/marketing landing content whose job is persuasion before commitment, which is what this entire site is.
- **Adopted, narrow scope — REF-007** (color as the wayfinding system itself): the brief's own 5-stage workflow is a genuinely bounded, nameable, parallel-path structure. Applied only to the Cómo funciona page's 5-stage timeline and echoed with 2 of the 5 hues in the Home hero's compression visualization — deliberately not propagated to Producto/Precios/Recursos, which have no equivalent structure. Not adopted because it was available; adopted because the brief's own enumerated 5-step workflow is exactly the "bounded, nameable set of parallel paths" the entry calls for.
- **Adopted — REF-009** (rule-segmentation over elevation for bounded summary surfaces): used throughout the product-UI mockup fragments (feedback rows, decision records, pricing feature rows) — fields separated by a hairline rule rather than nested cards/shadows, which also served as direct `SLOP-007` (card-in-card) avoidance.

No reference was used merely because it was considered; 7 of 9 were rejected with a specific, checkable reason each.

## 4. Major Design Decisions

- **Macrostructure:** a "pipeline spine" — the site's structure follows the brief's own stated workflow rather than a generic hero→features→CTA rhythm. The hero doesn't show a screenshot; it constructs a small, believable compression visualization (scattered feedback chips → grouped theme chips with counts → one decision panel) built from real HTML/CSS, directly answering the brief's explicit instruction to avoid a static-headline-plus-dashboard-screenshot hero.
- **Navigation:** nav labels translated to Spanish for internal consistency ("Inicio" rather than the brief's literal "Home," since every other label and both CTAs are Spanish); sticky header, disclosure-based mobile menu with `aria-expanded`, active-page state via `aria-current="page"`.
- **Typography:** Space Grotesk (display/headings) + Manrope (body/UI), a 2-family cap (`TYPE-001` hard cap for product-led). Fixed rem scale (`TYPE-005` product-register), not fluid `clamp()`.
- **Color:** OKLCH-built warm-neutral paper, near-black (not pure black) ink, and a single moss-green brand accent — deliberately not blue/purple/neon/gradient, matching the brief's explicit avoidance list without reaching for an opposite cliché. A secondary 5-hue "stage index" (from adopted REF-007) is scoped only to the workflow page and hero, used exclusively as small markers/dots/borders, never as text fill, to keep the accessibility surface small.
- **Layout:** no repeating feature-card grid anywhere. Producto's six capabilities are single-column stacked sections with alternating left/right rhythm; Recursos is an editorial list, not a card grid; pricing cards are the one deliberate, brief-legitimate exception (3 genuinely distinct, actionable tiers).
- **Product UI:** every interface fragment (feedback inbox rows, theme lists, decision records, pricing feature rows) is rule-segmented (REF-009) rather than nested cards, and every numeric value is explicitly sample data, disclosed in visible captions on every page that shows one.
- **Imagery:** no photography (`LAYOUT-008` procedure: yes the subject warrants visual weight, but the right medium is constructed interface fragments and diagrams, not photography — there is no real customer/office to photograph and the brief discourages heavy photography).
- **Interaction:** functional, not decorative — a working (if front-end-only) contact form with real validation/error/success states, a working category filter on Recursos, a working mobile disclosure menu, native `<details>` for FAQ/pricing accordion (platform feature over custom JS).
- **Motion:** Low intensity. One orchestrated hero reveal (the compression visualization's staged fade-in, one-shot keyframes) is the sole delight-tier exception, declared explicitly; everything else is state-transition feedback only, gated behind `(hover: hover) and (pointer: fine)`, respecting `prefers-reduced-motion`.
- **Responsive behavior:** mobile nav collapses to a labeled disclosure menu with its own CTA; the pricing comparison table becomes a per-plan `<details>` accordion below 768px instead of a scrolling table; the pricing grid's 3-column breakpoint was deliberately set at 880px (not the more common 768px) after real content (the "Personalizado" price label) proved the tighter width didn't fit.
- **CTA hierarchy:** primary "Probar Signal" always filled/solid; secondary actions always outlined; on the pricing page, the Business tier's CTA is intentionally different ("Hablar con ventas") rather than reusing "Probar Signal" on a tier that wouldn't realistically self-serve a trial — a deliberate `INTX-004` judgment call, not a copy-paste oversight.

## 5. Critique

### Level 1

Self-critique run across the six standing axes:

1. **Genericness — 4/5.** Gestalt-checked against `SLOP-011`'s four named clusters as a combination, not per-element: not cluster 1 (no serif, no cream+terracotta pairing — sans-only, green accent), not cluster 2 (light mode, no near-black+neon), not cluster 3 (not broadsheet/newspaper), not cluster 4 (card-in-card deliberately avoided via REF-009). Passes. The hero, Cómo funciona timeline, and Producto's alternating layout are specifically derived from this brief's own workflow; the audience row and benefits grid are the least distinctive sections (functional but plainer).
2. **Hierarchy — 5/5.** Squint test holds at every breakpoint checked: primary (headline/CTA) → secondary (viz/panels) → tertiary (body) reads clearly through scale and weight contrast alone.
3. **Distinctiveness (fingerprint) — not yet applicable.** This is Entry 1 in `.design/context.md`'s Fingerprint History for this project; nothing to compare against per `SKILL.md` §6.
4. **Craft correctness — 4/5.** Spot-checked against the rule-catalog categories actually in scope (layout-interaction, motion, typography, color, accessibility, content-copy, performance-hardening). Several real defects were found and fixed during rendered validation (§6) — the process caught them, which is what it's for, but their initial presence keeps this below 5.
5. **Accessibility — 5/5 on the always-on P1 floor**, verified by actual computed-pixel contrast measurement (not estimated): ink/paper 16.4:1, on-accent/accent 9.14:1, ink-soft/paper 9.25:1, accent/paper 8.92:1, and a genuine failure on ink-faint/paper (4.31:1, below the 4.5:1 floor) that was found and corrected to 5.54:1. Focus-visible is universal (never bare `:focus`), reduced-motion block present and gentler-not-zero, hover gated behind capability query, icons role-conditional.
6. **Technical correctness — 4/5.** `MOTION-004` (transform/opacity/clip-path only) respected throughout, including in the one keyframe animation. Four rendered-only bugs were found and fixed (§6) — a flex-sizing SVG quirk, a sub-400px nav overflow, two `min-width:auto` grid-child overflows, and one word-overflow at a specific breakpoint. None were visible from reading the source; all four were only found by actually rendering at real viewport widths, which is the reason this axis isn't a 5.

### Level 2

- **Triggered: NO.**
- **Reason:** none of the stated trigger conditions fired. This is BUILD (not REDESIGN, which escalates by default). The brief is genuinely-empty, multi-page-site scope, but does not use an explicit brand-quality bar phrase ("premium," "flagship," "brand identity," or equivalent) — it says "production-quality," which the routing table treats as the ordinary bar, not the elevated one. Level 1's automatic escalation trigger (same axis scoring below 3 on two consecutive passes) never fired since this is the first and only self-critique pass. Per the protocol's own instruction ("running it on every task defeats the point of having a cheap floor at all"), Level 2 was not run.
- **Findings:** n/a (not run).

## 6. Refinements

All of the following were found through actual rendered-browser validation (Playwright, at 320/375/640/768/960/1024/1440px, plus computed-style contrast measurement), not static code review:

1. **Contrast failure:** `--color-ink-faint` measured 4.31:1 against `--color-paper` (below WCAG 2.2's 4.5:1 floor for normal text), used throughout for meta text (timestamps, source labels, footer copyright, sample-data captions). Corrected from `oklch(56% 0.012 90)` to `oklch(50% 0.012 90)`, re-measured at 5.54:1.
2. **Logo icon invisible:** the inline SVG wordmark collapsed to 0px width as a direct child of a flex row, despite explicit `width` in both CSS and HTML attributes (a real Chromium flex-sizing behavior for bare SVG flex items, confirmed by testing — CSS `!important` on the SVG itself still didn't resolve it). Fixed by wrapping the SVG in a normally-sized `<span class="mark">` and having the SVG fill it at 100%/100%, sidestepping the SVG-as-flex-item sizing path entirely. Applied identically across all 12 instances (header + footer × 6 pages).
3. **Nav overflow below 400px:** logo + CTA + hamburger didn't fit one row at 320–399px, producing ~20px of horizontal page overflow. Fixed by hiding the header's inline CTA under 400px and adding an equivalent "Probar Signal" button inside the mobile disclosure menu, which is also a more realistic mobile-nav pattern than forcing everything into one cramped row.
4. **Pricing-tier and contact-info grid overflow:** both are CSS Grid children that don't shrink below their content's intrinsic width by default (`HARDEN-003`, previously stated in the catalog only for flex — this build found the identical failure mode in Grid). Fixed with `min-width: 0` on the grid children, plus `overflow-wrap: break-word` on the long unbroken email address in the contact info.
5. **"Personalizado" price label:** overflowed/broke mid-word specifically in the 768–879px range, where the pricing grid's 3-column layout left too little room for that one non-numeric price label. Fixed by giving it its own smaller size token and raising the 3-column breakpoint from 768px to 880px, rather than shrinking type further and further to fight an increasingly cramped column.

No other findings from Level 1 required code changes; the genericness and hierarchy scores were addressed by the initial design decisions, not by post-hoc patching.

## 7. Final Assessment

### Strengths
A hero that actually demonstrates the product's mechanic instead of describing it; consistent rule-segmented product UI instead of card-in-card; a workflow-driven macrostructure that ties the whole site together; disciplined, evidence-traced rejection of 7 of 9 visual references instead of forcing adoption; every accessibility and layout defect found was actually fixed and re-verified in a rendered browser, not assumed correct from source.

### Weaknesses
The audience row and benefits grid (Home) are the least distinctive sections — functionally clear but visually closer to a default pattern than the hero or Producto page. The stage-color system, while scoped narrowly and deliberately, is still an additional system a reviewer has to learn; a simpler numbered-only treatment was the safer default and was consciously not chosen. No automated axe-core-equivalent accessibility scan was run — contrast was verified computationally, but a full screen-reader pass was not performed (see §11).

### Visual Personality
Legible and specific to a workflow-driven product tool: warm-neutral paper, a single confident moss-green accent, geometric display type paired with a warmer body face, rule-based (not card-based) product UI. Recognizable across all six pages without needing color or logo to identify it.

### Distinctiveness
No fingerprint comparison was possible (first generation for this project), but the gestalt check against the four named self-tell clusters passed cleanly, and the hero specifically avoids the exact pattern the brief called out as generic (headline + paragraph + two buttons + dashboard screenshot).

### Product Communication
Strong. A visitor can trace "what happens to my feedback" through the hero alone, then again in more detail on Cómo funciona, then again as discrete capabilities on Producto — the same mechanic told three times at three levels of detail, in three different structural treatments (compressed illustration, timeline, capability deep-dive), not three copies of the same layout.

### UX Quality
Clear nav, consistent CTA hierarchy, functional (not decorative) interactive states on the form and resource filter, native `<details>` used over custom JS where it was the right tool. `INTX-004` was applied deliberately on the pricing page's differentiated CTA treatment rather than left to default.

### Responsive Quality
Verified, not assumed, at 320/375/640/768/880/960/1024/1440px, with two genuine breakpoint-specific bugs found and fixed rather than only checked at the two or three "obvious" widths.

### Accessibility
WCAG 2.2 contrast floor verified computationally across all primary and secondary color pairs, one real failure found and fixed. Focus-visible universal, reduced-motion respected, icons role-conditional, forms follow the border-width/helper-slot/disabled-state hardening rules. Full assistive-technology walkthrough not performed (disclosed as a remaining risk, §11).

### Performance
No custom web fonts beyond the two chosen families (loaded via `preconnect` + `display=swap`), no JS dependencies, no layout-triggering CSS animation properties, `content-visibility`/lazy-loading not needed at this page weight. Not measured with an actual Lighthouse/CWV run (disclosed in §11).

### Maintainability
Four small, purpose-named CSS files (tokens/base/components/sections) instead of one large stylesheet, consistent BEM-adjacent naming, no build step required for a static 6-page site of this size — appropriate for the project's actual scope, not under- or over-engineered for it.

## 8. Genericness Check

This reads as a **genuinely specific product design**, not a generic SaaS template or a "sophisticated AI-generated SaaS" pattern. Concrete evidence: the hero is not headline+paragraph+two-buttons+dashboard-screenshot (the exact pattern the brief named as the thing to avoid, and the thing most AI-generated SaaS heroes default to); no card-in-card anywhere; no purple/blue gradient; no glassmorphism; no fabricated metrics, testimonials, or logos; copy is specific to the actual feedback/theme/insight/decision vocabulary of this product rather than generic "streamline your workflow" filler; the pricing page's Business-tier CTA is deliberately different from the other two rather than uniformly repeated. The weakest sections (audience row, benefits grid) are plain but not templated — they don't reach for pills, gradients, or icon-card grids either; they're simply the least visually ambitious parts of an otherwise specific system.

## 9. Unexpected Behavior

- A separate, automated `lexia-design` detector hook fired after several file writes (not part of `design-excellence`, an independent tool present in this environment) and flagged two things: repeated em-dash characters and a repeated 4+ word phrase. Both were verified against context and judged **FALSE_POSITIVE / MITIGATED**: the "em-dashes" were the single `—` glyph used three separate times as a table/list "not included" data marker (identical to the desktop comparison table's own CSS-generated convention), not prose punctuation; the repeated phrase was "Probar Signal" (the brief's own mandated, exact CTA text, correctly reused per `CONTENT-001`'s vocabulary-consistency rule) and "Artículo de ejemplo" (a required per-item placeholder-content disclosure, correctly repeated once per independent placeholder article). Neither required a content change.
- The SVG-as-flex-item 0-width bug (§6, item 2) was a genuine surprise: neither the CSS `width`, the HTML `width` attribute, nor an inline `!important` override resolved it while the SVG was a direct flex child, which is not a design-excellence rule gap — it's a real browser rendering interaction outside this skill's scope, caught only because VALIDATE actually rendered the page instead of trusting the source.
- `HARDEN-003` (`layout-interaction.md`/`performance-hardening.md`) is written scoped to flex children ("a flex or grid child..." — it does name both, on closer reading), and the grid-child failure mode this build hit matches it exactly; no rule gap here, just confirmation that the existing rule's grid half is just as load-bearing as its flex half.

## 10. Rule Failures

No `design-excellence` rule produced an incorrect instruction in this run. The one near-miss worth recording: `COLOR-001`'s Medium-`DESIGN_VARIANCE` language ("must visibly move at least one rung off that default's most conservative edge") is a qualitative judgment call with no mechanical test attached to *how far* is enough — this build interpreted it as "a deliberate solid-fill CTA/accent band in addition to the Restrained baseline," which is defensible but not the only reasonable reading. Not a failure, just a rule whose satisfaction can't be mechanically verified the way `COLOR-001`'s own coverage-percentage check can for the *tier ceiling* itself.

## 11. Remaining Risks

- No full keyboard-only / screen-reader walkthrough was performed (mobile menu toggle and form states were verified via automated clicks and computed styles, not a manual assistive-technology pass).
- No Lighthouse/Core Web Vitals measurement was run against the live pages; performance claims in §7 are based on the absence of known anti-patterns (no JS framework, no layout-triggering animation, no unoptimized images — there are none), not a measured score.
- The stage-color system (Cómo funciona + Home hero) adds a second small color vocabulary alongside the brand accent; it was deliberately scoped narrow, but a future editor adding a similar treatment to another page without re-reading `.design/context.md`'s Visual References section could over-extend it.
- Google Fonts is loaded from an external CDN (`fonts.googleapis.com`/`fonts.gstatic.com`); no self-hosting or CSP was set up, since no build/deploy pipeline exists yet for this static file set — reasonable for the project's current genuinely-empty/static state, but worth revisiting if this moves to a real deployment.
- Pricing, resource, and contact content are explicitly placeholder/fictional per the brief; nothing here should be mistaken for a real commercial offering if reused elsewhere.

## 12. Verdict

**PASS.**

This benchmark run produced a coherent, brief-derived, non-generic six-page site with a genuinely product-specific hero, disciplined and evidence-traced use of the Visual References and Anti-Slop mechanisms, an honest (not forced) Concept and Level-2-critique determination, and real defects found and fixed through actual rendered-browser validation rather than assumed correct from source. The verdict describes this specific build, not a general claim about the skill.
