# Phase 7 — Test 04 Results

## 1. Brief

Design and build a complete, production-quality responsive e-commerce website for **FORMA**, a fictional independent contemporary furniture and home-objects brand (chairs, tables, lighting, storage, small objects), targeting design-literate adults. Six pages: Inicio, Tienda, Categorías, Producto, Sobre FORMA, Contacto. The brand must read as "premium without feeling luxurious or inaccessible" — distinctive, considered, tactile, confident, functional — while the shopping experience (discovery, filtering, sorting, product evaluation, purchase) stays fully functional and efficient. All copy in Spanish; no fabricated reviews, stats, certifications, or policies. Explicitly banned: the default hero+3cards+grid+newsletter+footer homepage formula, and a long list of generic "AI e-commerce" visual tells.

Built as a static HTML/CSS/JS site (no framework, no build step) — genuinely-empty project, so this was the sensible-modern-stack default per the skill's own TECHNICAL guidance.

## 2. Routing

- **Scope:** multi-page-site
- **Project state:** genuinely-empty
- **Task mode:** BUILD
- **Register:** hybrid (brand personality + commerce efficiency, both explicitly required, neither subordinate)
- **Genre:** modern-minimal
- **DESIGN_VARIANCE:** 6/10 (Medium)
- **MOTION_INTENSITY:** 3/10 (Low)
- **VISUAL_DENSITY:** 7/10 (Medium-High)

## 3. Design Direction

### Design Read
Hybrid-led modern-minimal work: a catalogue-forward "Specimen Index" macrostructure carrying real brand personality through a category-color wayfinding system and a spec-sheet-derived typography pairing, disciplined by commerce-efficiency requirements (scannable grids, real filtering, undisguised prices/availability).

### Concept
**HYPOTHESIS**, not DETECTED/EVIDENCED. "FORMA" plausibly echoes Spanish/Latin *forma* ("shape"/"form") — a real, checkable linguistic association. The brief's own text gives no naming rationale, no recurring reference object, and no instruction to embody an idea; this is model-supplied, not brief-evidenced. Declared as a HYPOTHESIS per the three-state model and allowed to loosely inform ordinary creative choices (attention to object silhouette in the placeholder-imagery system) without being logged as an organizing-surface decision.

### Concept → Structure
**Not activated.** LAYOUT-009's mandatory structural-translation requirement only fires on a DETECTED/EVIDENCED concept outcome. Since DEFINE recorded HYPOTHESIS only, this rule correctly did not engage — matching its own stated exception ("HYPOTHESIS... does not activate this rule's mandatory translation requirement").

### Visual References
References loaded (`visual-references.md`, 9 entries) at the DIRECT/EXPLORE step.

- **Adopted — REF-007** (color as the wayfinding system itself, not a decorative accent on top of one): the catalogue's 5 categories are a genuinely bounded, nameable, parallel set — exactly REF-007's applicability condition. Informed the category-dot/tag coding used across nav, cards, filters, and the category directory page.
- **Adopted — REF-009** (segmentation by rule on a fixed canvas, not elevation): the product-detail spec panel (material/dimensions/availability/SKU) is a small set of independent, equally-weighted facts on a bounded surface — informed the rule-divided field-list treatment instead of a card grid.
- **Considered and rejected:** REF-001 (fixed nav/content column) — steals working screen area from a grid-scanning commerce UI, against its own `do_not_apply_to`. REF-002 (stationary scroll anchor) — needs Medium-High motion, this build is Low. REF-003 (wayfinding-as-index nav) — explicitly excludes product-led/growing catalogues. REF-004 (oversized numerals as dividers) — explicitly excluded for modern-minimal/product-led. REF-005 (process imagery) — no real process photography exists to fabricate. REF-006 (counted-index reveal) — needs Medium-High motion and a fixed countable sequence, homepage content isn't one. REF-008 (task-state-first hierarchy) — fits a committed task flow (checkout), not discovery pages; considered for the filter panel, judged unnecessary.
- Not claimed useful merely because considered — two of nine were actually adopted, seven were evaluated and rejected with stated reasons, matching the skill's "considered, judged unnecessary is as valid as adopted" instruction.

## 4. Major Design Decisions

- **Macrostructure:** named bundle "Specimen Index" — compact left-aligned intro band (no full-bleed hero) + asymmetric bento product clusters + a category wayfinding strip + an editorial materials/philosophy band + a real-navigation footer. Chosen specifically to avoid the brief-banned hero+3cards+grid+newsletter+footer default.
- **Navigation:** sticky header, primary nav collapses to a full-screen sheet below 900px (not a cramped dropdown); breadcrumbs on every non-home page; category pages reachable both from a home strip and a dedicated directory.
- **Information architecture:** 5 fixed categories (Seating/Tables/Lighting/Storage/Objects) as the primary organizing axis, cross-cut by material/color/price/availability filters on Tienda. Categorías is a lightweight index, not a taxonomy generator.
- **Typography:** ran the TYPE-002 procedure (voice words: *tactile, confident, functional* → reject reflex defaults Inter/Helvetica/system-ui → framed as "a furniture spec sheet / technical drawing label" → picked). Archivo (display/headlines/prices) + IBM Plex Sans (body/UI) — 2-family cap per TYPE-001's hybrid default. IBM Plex Mono as a documented 3rd outlier, capped to 2 usage slots (SKU codes, dimension spec values only).
- **Color:** OKLCH paper/ink/neutral/accent construction (COLOR-004). Accent derived from a concrete furniture-production detail (powder-coated steel frames/legs are a real contemporary-furniture signature color move), not a category stereotype — explicit SLOP-013 avoidance. Restrained-to-Committed tier with one declared exception (solid CTA fills).
- **Layout:** CSS Grid throughout, `minmax(0,1fr)` on every image-bearing track (LAYOUT-005), `overflow-x: clip` not `hidden` (LAYOUT-004).
- **Product grid:** 2/3/4-column responsive grid on Tienda, consistent 4:5 placeholder-frame ratio for scanability, varied bento tile sizes only on the homepage's curated clusters (not the utilitarian shop grid).
- **Product cards:** `<article>` container with a non-nested `<a>` (name/image/meta) and a sibling quick-add `<button>` — restructured mid-build after an independent review caught the original markup nesting a button inside an anchor.
- **Product detail:** gallery with labeled placeholder "views," quantity stepper, spec panel as a rule-segmented fact list (REF-009), related products, sticky mobile purchase bar.
- **Filtering and sorting:** category/material/color/price/availability filters with faceted counts (each option's count respects every *other* active filter, not just a static global tally), 5 sort orders, 12-per-page pagination, full URL state round-trip (refresh/back preserves every filter, not just category), a real empty state with a recovery action.
- **Imagery:** ran the LAYOUT-008 procedure explicitly — yes, imagery is warranted; no real photography exists, so the medium is a clearly-labeled flat placeholder (category-tinted ground + line-drawing silhouette + "Imagen de producto: [name]" caption), never fake photography or fake 3D.
- **Interaction:** 8-state coverage on interactive components where applicable; hover gated behind `(hover: hover) and (pointer: fine)` via existing CSS conventions; quick-add and purchase actions produce visible toast/inline confirmation.
- **Motion:** Low tier — feedback/state-transition only (filter sheet open/close, toast, focus states, gallery thumbnail swap); no scattered decorative scroll reveals.
- **Responsive behavior:** dedicated mobile treatments, not desktop-stacked-vertically — full-screen filter sheet (not a cramped inline panel) with a real focus trap, sticky purchase bar, deliberate bento collapse order.
- **CTA hierarchy:** "Comprar" reserved for the two sitewide marketing-level placements the brief specifies (home hero → Tienda, secondary "Ver colección" → Categorías); the actual per-product transactional action is "Añadir a la cesta," chosen so confirmation copy shares the same verb root as its trigger (CONTENT-001).

## 5. Critique

### Level 1
Self-administered throughout BUILD and in a dedicated pass before Level 2. Caught and fixed before external review: a bento-grid sizing bug (size class landed on the `<a>` instead of the grid's direct `<li>` child), a duplicate/leaking mobile filter panel visible at desktop widths, a blank price-range max label on load, facet counts that ignored other active filters, a crash in the availability-filter checkbox handler, the cart-feedback toast overlapping the sticky mobile purchase bar, several SLOP-005/SLOP-017 content-copy violations (middle-dot meta strings, em-dash title separators and clause use), and a systemic WCAG contrast failure on `--ink-faint` and the low/ok status-badge colors (3.61:1 / 3.77:1 against a 4.5:1 floor).

### Level 2
- **Triggered:** YES.
- **Reason:** BUILD mode, genuinely-empty project, multi-page-site scope, and the brief states an explicit brand-quality bar ("premium without feeling luxurious or inaccessible") — matches the critique protocol's BUILD-escalation trigger.
- **Mechanism:** two genuinely fresh, isolated subagents dispatched in parallel (`lexia-design:visual-critic` for genericness/distinctiveness, `lexia-design:ux-auditor` for UX/accessibility), neither given this session's own Level 1 scores or findings, matching the protocol's dual-blind requirement.
- **Findings (visual-critic):** HIGH — mobile hero cluster (`.intro-cluster`) had no responsive breakpoint, unlike its sibling grids, causing the category label + availability badge to overflow their card at narrow widths (confirmed via `getBoundingClientRect()`: content exceeded the row by 48–56px). MEDIUM-HIGH — the Asientos category hue (35) sat 3° from the brand accent hue (32), reading as the same red and contradicting this project's own `.design/context.md` claim of "distinct from the single brand accent hue." MEDIUM — Tienda/Producto don't carry the homepage's bento signature forward, reading closer to a generic furniture-store template once the logo is covered. MEDIUM — the hairline-rule/near-zero-radius/numbered-index/bold-geometric-type combination sits close to (though doesn't fully match) the "broadsheet" self-tell cluster, as a gestalt judgment. LOW — status badges are a common colored-chip pattern.
- **Findings (ux-auditor):** CRITICAL — the mobile filter sheet (`role="dialog"`) had zero focus management: no initial focus, no Tab trap, no Escape handler, no focus restore, inconsistent with the mobile nav's (better, still incomplete) pattern on the same site. SERIOUS — a quick-add `<button>` was nested inside a product-card `<a>`, an invalid interactive-in-interactive HTML content model. SERIOUS — the filter-tag remove button was 20×20px, below the WCAG 2.5.8 24×24 floor. SERIOUS — URL state only round-tripped the category filter; refresh/back silently dropped material/color/availability/price/sort/page. MODERATE — `--cat-iluminacion` icon contrast against its own background was 2.93:1, below the WCAG 1.4.11 3:1 floor for meaningful graphics; the contact form's topic `<select>` got `aria-invalid` but no visible error text on failed submit; the quantity stepper and gallery thumbnail swap changed state with no screen-reader announcement. MINOR — decorative SVG icons lacked explicit `aria-hidden`; icon buttons clear the 24px AA floor but miss the 44px mobile-practical floor (not fixed — WCAG AA is already met).
- **Disagreement worth surfacing:** the two reviewers converged on almost nothing in common (expected, given orthogonal rubrics) but both independently flagged real, previously-unnoticed defects — a genuine value demonstration for the dual-review mechanism, not a redundant pass.

## 6. Refinements

All ten findings above a MINOR/accepted-risk threshold were fixed and re-verified in the browser (not just edited and assumed correct):

1. `.intro-cluster` given a 2-column mobile breakpoint (matching `.bento`'s own collapse pattern) plus a defensive `flex-wrap` on `.product-card__top-row`; verified via `getBoundingClientRect()` that no card content overflows at 390px.
2. Mobile filter sheet rewired through a new shared `window.FORMA.bindDialog()` helper (initial focus, Tab trap, Escape, focus restore) — also used to upgrade the mobile nav's own (previously partial) implementation for consistency. Verified: Tab from the last focusable element wraps to the first; Escape closes and restores focus to the trigger.
3. Product-card markup restructured everywhere (`shop.js`, `home.js`, `product.js`) to `<article><a class="product-card__link">…</a><button>…</button></article>` — the quick-add button is now a sibling of the link, never nested inside it. Verified: zero `a button` matches site-wide.
4. `--cat-asientos` moved from hue 35 to hue 195 (teal) — maximally distant from the accent (32) and every other category hue; `.design/context.md` corrected to match reality instead of asserting a separation that didn't hold.
5. `.filter-tag` remove button enlarged to a 24×24px hit target (visual chip stays compact via negative margin).
6. `--cat-iluminacion` darkened from 64% to 52% lightness — contrast against its own tinted background verified at a comfortable margin above 3:1.
7. Contact form's `#topic` select given a helper span + change-time validator, matching its sibling fields.
8. Quantity stepper and gallery thumbnail swap given visually-hidden `aria-live="polite"` status regions; verified both announce correctly on interaction.
9. `aria-hidden="true"` added to all five decorative placeholder SVG icons.
10. URL state extended to round-trip category, material, color, availability, price, sort, and page (previously only category); verified a full filter combination survives a hard page reload.

`--ink-faint` and the `--status-ok`/`--status-low` tokens (Level 1 finding) were darkened before Level 2 ran; Level 2 did not re-flag these, consistent with the fix holding.

**Not fixed, documented as an accepted risk:** the visual-critic's MEDIUM finding that Tienda/Producto don't carry the homepage's distinctive bento composition forward. Judged correct under this project's hybrid-register reasoning — commerce efficiency (consistent scannable grids) legitimately wins on the pages where a user is actually comparing products — but it's a real, honest limit on distinctiveness past the homepage, not resolved by this pass.

## 7. Final Assessment

### Strengths
A macrostructure that is genuinely not the banned default; a color-as-wayfinding system that does real navigational work once its self-consistency bug was fixed; honest placeholder imagery with a stated rationale; zero fabricated content anywhere (reviews, stats, certifications, policies); working faceted filtering/sorting/pagination with correct empty-state recovery; two independently-caught, real accessibility defects (focus trap, contrast) fixed and verified rather than left as findings on paper.

### Weaknesses
Distinctiveness is front-loaded onto the homepage; Tienda and Producto lean on a more conventional sidebar-filter/product-grid vocabulary once past the entry screen. The hairline/near-zero-radius/spec-sheet idiom, while not a literal match for any single banned pattern, sits close enough to a recognizable "premium agent-commerce" register that an outside viewer flagged it unprompted — worth naming honestly rather than smoothing over.

### Visual Personality
Present and legible from the first screen (asymmetric bento, category-coded dots, a powder-coat accent with a stated non-arbitrary rationale) — the visual-critic's own "3-line memory test" concluded a visitor would retain a real, specific impression, not a generic one.

### Distinctiveness
Uneven across the site: strong on Inicio and Categorías, weaker on Tienda/Producto/Sobre FORMA/Contacto, which lean on well-established, defensible-but-common commerce/content patterns.

### Product Discovery
Functionally solid: working filters with correct faceted counts, 5 sort orders, real pagination, a category directory, breadcrumbs throughout, and (after refinement) full URL-state persistence.

### Commerce UX
Price, availability, and category are visible at every touchpoint; quantity and purchase actions give clear feedback; the mobile filter sheet and purchase bar are deliberately reworked, not desktop-stacked; the one CRITICAL interaction defect found (filter-sheet focus trap) is fixed and verified.

### Product Communication
The single built product-detail page (Silla Costa) covers every required element — name, price, gallery, description, material, dimensions, availability, quantity, purchase action, related products — using a rule-segmented spec panel rather than a card grid.

### Responsive Quality
Verified, not assumed: 375px and 1440px spot-checked live in-browser for every page, including the two defects (hero-cluster overflow, filter-sheet focus) that only manifest at mobile widths.

### Accessibility
WCAG 2.2 AA was actively tested (canvas-based contrast measurement against real rendered colors, not eyeballing), not just declared: two real contrast failures and one real keyboard-trap failure were found and fixed across both the self-critique pass and the independent review. Remaining, not fixed: icon buttons sit at the 24px AA floor rather than the 44px "practical" mobile-HIG guideline (a preference, not a WCAG requirement).

### Performance
No render-blocking resources beyond two Google Fonts requests; LCP-eligible imagery is inline SVG (no lazy-loading anti-pattern possible); motion restricted to compositor-friendly properties throughout, verified in the skip-link fix during BUILD.

### Maintainability
Plain HTML/CSS/JS, no build step, token-driven CSS (`tokens.css`), one shared product-card/dialog pattern reused across all rendering call sites — genuinely simple for a project this size, not under-built relative to its actual complexity.

## 8. Genericness Check

**(a) genuinely specific e-commerce brand** on the homepage and category directory — the color-wayfinding system (once corrected), the powder-coat accent rationale, and the asymmetric bento composition are traceable to this specific brief, not swappable for another furniture brand's site without the copy changing. **Closer to (c) sophisticated-but-recognizable once past the homepage** — Tienda's sidebar-filter/product-grid pattern and the site-wide hairline/near-zero-radius/spec-sheet vocabulary are real, current AI-agent-commerce defaults, not literal matches for any single banned SLOP-011 cluster but adjacent to one as a gestalt (the visual-critic's own finding #4, taken at face value rather than argued away). This is the honest verdict, not a favorable rounding: the build clears every individual Anti-Slop entry it was checked against, and still reads as "a well-executed example of a genre" rather than "unmistakably FORMA" once a viewer scrolls past the first screen.

## 9. Unexpected Behavior

- Both independent Level 2 reviewers found real, previously-unnoticed defects that survived an already-thorough self-QA pass (mobile hero-cluster overflow; the color self-collision; the focus-trap gap; the nested-button HTML violation) — the dual-review mechanism paid for itself concretely in this run, not just procedurally.
- A stray `ruvector.db` (~1.5MB) appeared at the project root partway through the session, evidently a side effect of one of the dispatched lexia-design subagents' own tooling running from the project's working directory. Removed as cleanup; not part of the deliverable and not referenced by anything in the site.
- A browser-cache false alarm: after reordering `<script>` tags in `tienda.html`, the running Playwright session kept reporting `window.FORMA.bindDialog is not a function` even though a direct `fetch(..., {cache:'no-store'})` confirmed the served file was correct — resolved by moving to a fresh server port (new origin, no stale cache), not a real code defect. Documented here so it isn't mistaken for one.

## 10. Rule Failures

None identified in the `design-excellence` skill's own mechanism. The three-state Concept model, the DIRECT/EXPLORE candidate-distinctness requirement, LAYOUT-008's imagery procedure, LAYOUT-010's reference-selection priority order, and the Level 2 critique's dual-blind dispatch all behaved exactly as documented and caught real defects a single-pass self-review had already missed. The skill does not currently ask DIRECT to sanity-check color-token separation *between* an already-committed accent and a category-coding system introduced later in the same DIRECT/DESIGN pass — the hue-collision bug slipped through Level 1 self-critique specifically because nothing in the catalog's `validation` fields for COLOR-001/COLOR-004 treats "does this new token collide with an existing one" as a mechanical-countable check. This is a genuine gap worth naming, not a rule that fired incorrectly — logged here per the instruction to document, not fix, apparent skill defects during this benchmark.

## 11. Remaining Risks

- Distinctiveness gap on Tienda/Producto/Sobre FORMA/Contacto relative to the homepage, accepted as a documented trade-off (§6) rather than resolved.
- No automated axe-core/Lighthouse run was performed; all accessibility verification was manual/scripted (canvas-based contrast math, live keyboard-trap testing, live-region content checks) rather than tool-audited end-to-end.
- The 24-product sample dataset is small enough that some filter combinations (e.g. a single material within a single category) return exactly one result — correct behavior, but not stress-tested against a catalogue several orders of magnitude larger.
- Dark mode is explicitly unshipped (documented in `tokens.css`) per the brief's own "don't default to dark mode" instruction — a deliberate omission, not an oversight, but worth naming as scope not covered.
- The hairline/near-zero-radius/spec-sheet visual idiom's proximity to a recognizable agent-commerce register (§8) has not been redesigned away; it's disclosed, not resolved.

## 12. Verdict

**PASS WITH RISKS.**

The build is functional, accessible after refinement, honestly scoped, and free of fabricated content — a real, working six-page e-commerce site with correct filtering/sorting/pagination logic, a defensible non-default homepage macrostructure, and two independently-verified, fixed accessibility defects that would have shipped broken otherwise. It falls short of an unqualified PASS because genuine distinctiveness is concentrated on the homepage rather than sustained across the full shopping flow, and because the site's visual idiom — while clearing every individual Anti-Slop rule it was checked against — sits close enough to a recognizable current AI-commerce vocabulary that an independent reviewer flagged it unprompted. Both risks are disclosed above rather than argued away, which is what keeps this a PASS WITH RISKS rather than a FAIL: the defects that would have been silent or hidden (the color collision, the focus trap, the mobile overflow) were caught and fixed; the one that remains (site-wide distinctiveness past the homepage) is a real, acknowledged limitation of this specific build, not a concealed one.
