# Phase 6.3 Benchmark Report — Clínica Atlas

Benchmark of the current `design-excellence` skill against the brief in `brief.md`. This report documents the actual routed pipeline, the design decisions made, the Concept → Structure mechanism, validation performed, and an honest distinctiveness assessment — including a real Level 2 independent critique (not simulated) and the fixes it produced.

---

## A. Pipeline

**Route taken:** multi-page-site scope, BUILD task mode, genuinely-empty project state → full pipeline minus AUDIT-stage (per `SKILL.md` §1/§2).

**Stages executed:** UNDERSTAND (read brief.md) → DEFINE (classification + concept detection) → DIRECT (2-candidate EXPLORE, concept translation) → SHAPE (per-page IA) → DESIGN (typography/color/motion/layout system) → BUILD (5 pages + CSS + JS) → VALIDATE (live-rendered, multiple widths) → CRITIQUE (Level 1 floor + Level 2 escalation, real) → REFINE (fixes applied) → SHIP. INSPECT and AUDIT-stage correctly skipped (genuinely-empty, not REDESIGN/AUDIT/CRITIQUE/DISCOVER mode).

**References loaded and why:** `layout-interaction.md` (LAYOUT-001/002/009 — macrostructure, squint test, concept→structure procedure), `typography.md` (TYPE-001/002/003/005/006), `color.md` (COLOR-001/003/004/005/007), `motion.md` (full — MOTION_INTENSITY consumer), `accessibility.md` (full — P1 floor), `content-copy.md` (CONTENT-001/002/003), `performance-hardening.md`, `anti-slop-registry.md` (T3, DIRECT/DESIGN new-visual-system trigger), `style-catalog.md` (T3, genre lookup + cross-check), `critique-protocol.md`. All loaded because DEFINE/DIRECT/DESIGN ran for a page/multi-page BUILD with a new visual system — not bundled by default.

**Classification declared:** hybrid register, editorial genre, DESIGN_VARIANCE=6 (Medium), MOTION_INTENSITY=3 (Low), VISUAL_DENSITY=4 (Medium-low). Full rationale in `.design/context.md`.

---

## B. Design decisions

- **Register:** hybrid — strong brand/trust-building need combined with a single, explicit conversion goal (not pure brand storytelling, not a product UI).
- **Genre:** editorial. Atmospheric-expressive was the category-stereotype default for a "calm healthcare/wellness brief" and was explicitly rejected after cross-checking `style-catalog.md`'s own fields against the brief: the brief bans glassmorphism/blobs/gradients/"generic wellness aesthetics" that atmospheric-expressive licenses by default, and its Medium–High motion default contradicts the brief's explicit Low-motion mandate.
- **Dials:** DESIGN_VARIANCE 6 (Medium — editorial's Restrained-to-Committed default, moved one rung to Committed per the Medium-band rule), MOTION_INTENSITY 3 (Low — directly evidenced: "avoid animation that exists only for decoration"), VISUAL_DENSITY 4 (Medium-low — "calm" is a direct brief word).
- **Macrostructure:** "Anchored Datum" — one named bundle (LAYOUT-001) applied identically across all 5 pages: fixed hairline-anchored nav, one hairline rule as the only section-divider language, left-anchored asymmetric headings, single orchestrated hero reveal.
- **Typography:** Frank Ruhl Libre (display) + Public Sans (body), selected via TYPE-002's physical-object procedure ("a hand-set stone lintel," "a cartographer's engraved brass instrument," "a well-worn anatomy-textbook plate"), cap of 2 families.
- **Color:** warm-stone paper/ink neutrals + a single Committed-tier cedar-green accent, derived from the Atlas Mountains/Atlas cedar reference (SLOP-013-conscious, not category-reflex), explicitly not landing on SLOP-011's cluster-#1 (warm cream + terracotta). All pairs contrast-verified 6.2:1–14.2:1.
- **Imagery/art direction:** no photography (LAYOUT-008 procedure — no real photos exist, and stock/fabricated "team" or "clinic" imagery would silently imply false credibility) — an original abstract contour-line SVG system instead, extending the hairline/datum language rather than decorating separately.
- **Interaction/motion:** one hero-only orchestrated reveal, transform/opacity-only properties, hover gated behind `(hover: hover) and (pointer: fine)`, reduced-motion split into independent movement vs. fade duration tracks so opacity/color transitions survive `prefers-reduced-motion` while movement is neutralized.
- **Responsive strategy:** mobile-first, real layout changes (not compression) — mobile nav disclosure pattern, spine-list reflow, DOM-order-preserving `order` swaps for text-before-graphic on mobile; breakpoints normalized to a 640/768/1024 scale during refinement (was inconsistently 640/768/900/1024).

---

## C. Concept → Structure

**Detected concept (DEFINE stage):** the brand name "Atlas" — factually grounded in the atlas (C1) vertebra that bears the skull's weight and enables the head's range of motion, and in the Atlas Mountains / Atlas cedar (*Cedrus atlantica*) as a material/color reference. This is real evidence (the given brand name and verifiable anatomy/geography), not an invented concept.

**Abstract structural principle** (concept stripped of literal imagery): a single foundational reference line that the rest of the structure aligns to and is measured against — remove or misalign that first support and everything built on it is affected.

**Candidate A — "Anchored Datum":** a persistent, unmoving hairline-anchored nav bar + one hairline rule used as the only section-divider language, site-wide. Organizing surfaces: macrostructure + navigation.

**Candidate B — "Ascending Path" (rejected):** homepage content ordered as a narrative arc (problem → pivot → resolution) with a scroll-linked vertical progress rail tracking position against a fixed "trust" anchor section. Organizing surfaces: content architecture + section transitions + interaction. Rejected because its distinctiveness depends on a scroll-linked motion device that sits in tension with the brief's explicit Low `MOTION_INTENSITY` mandate, and because it is Home-specific rather than a system-wide device applicable across all 5 pages.

**Distinctness check:** Candidate A vs. B differ on composition, interaction, and color — passes the ≥2-of-6-dimensions requirement.

**Selected expression, as originally built:** Candidate A — datum line lived in the nav (fixed, hairline-anchored) and in section dividers (one hairline rule, used everywhere).

**Selected expression, after Level 2 critique:** an independent reviewer found the original expression insufficient — a sticky nav with hairline dividers is too close to a generic, common editorial pattern to carry the concept without the About-page prose explaining it outright, and two sections (trust reasons, team roles) were literal equal-weight 3-up grids that directly contradicted this project's own stated "never a uniform 3-card grid" macrostructure principle. **Fixed:** every repeated-content list on the site — services (via a numeral anchor-list), approach steps, trust reasons, and team roles — now attaches to one consistent structural device: either the numbered anchor-list or the single-column vertical spine-list, never a grid. This is a real, verified rewrite (see §D), not a cosmetic relabel — it removes the last two grid-shaped sections on the site and makes the "one line everything attaches to" idea a site-wide discipline instead of a one-page motif.

**Rejected structural direction (logged):** Candidate B, "Ascending Path" (motion-dependent narrative rail) — see above.

---

## D. Validation

**Responsive widths tested:** 320/390 (mobile), 768 (tablet), 1024, 1280/1440 (desktop) — rendered live via a local HTTP server. `resize_window` proved unreliable in this sandboxed browser environment (confirmed via `window.innerWidth` returning inconsistent values — 1282, then 3440 — independent of the requested size), so a same-page `<iframe>` viewport-harness technique was used instead to get a true, verifiable CSS viewport width per breakpoint.

**Accessibility checks:** contrast computed by hand via the WCAG relative-luminance formula for every color-token pair, and independently re-verified by the ux-auditor reviewer (6.2:1–14.3:1 across all pairs checked, all pass AA, most pass AAA); full keyboard walk (skip link → nav → mobile toggle → form fields, no traps, Escape closes mobile nav and returns focus); focus-visible only, never bare `:focus`; reduced-motion split verified in code; zoom not disabled (no `maximum-scale`/`user-scalable=no`); icon-only buttons (hamburger) have correct, state-flipping accessible names.

**Mechanical checks:** `overflow-x: clip` not `hidden` on html/body (LAYOUT-004); `minmax(0,1fr)` (not bare `1fr`) on SVG-bearing grid tracks (LAYOUT-005); motion restricted to transform/opacity/clip-path only (MOTION-004); hover states gated behind `(hover: hover) and (pointer: fine)` (MOTION-008); clickable text never wraps (INTX-003, `white-space: nowrap` on `.btn`).

**Level 1 findings (self-critique floor):** scored 6 axes 1–5 against the skill's own rubric; no axis scored below 3, so the automatic Level 2 escalation trigger from repeated low scores didn't independently fire — but Level 2 fired anyway via the separate, explicit trigger: BUILD + genuinely-empty + multi-page-site + the brief's own explicit brand-quality bar ("premium").

**Level 2 findings — real, isolated dispatch, not simulated.** Two genuinely fresh subagents were dispatched (`lexia-design:visual-critic`, `lexia-design:ux-auditor`), each given a self-contained brief (code + screenshots + relevant rule IDs + the six-axis rubric) with no visibility into the other's findings or into any Level 1 self-scoring, per `critique-protocol.md`'s isolation requirement.

*visual-critic:* HIGH — structural test substantially failed as originally built (concept lived mainly in copy/decoration; two sections used generic 3-up grids contradicting the project's own stated principle). MEDIUM — SLOP-013 category-reflex palette risk (legitimate derivation, but a plausible first guess for the vertical by output alone). MEDIUM — TYPE-006 widow control applied to only one heading. LOW — breakpoint drift (900px vs. 1024px caused a composed-desktop/mobile-nav mismatch window). Positive, independently verified: contrast discipline, token architecture, family-cap discipline.

*ux-auditor:* CRITICAL — contact form claimed a fabricated success ("Hemos recibido tu solicitud") with literally no submission mechanism (no `action`, no `fetch`, nothing transmitted). CRITICAL — focus ring invisible (contrast ~1:1–1.7:1) on `.cta-band` and `.site-footer`, because the default ring color matched or nearly matched those sections' own backgrounds; a `.btn--on-dark` class existed for exactly this case but was never wired up anywhere. HIGH — "Home" left in English site-wide despite the brief's explicit Spanish-only mandate. HIGH — form fields had no `aria-describedby`. MEDIUM — footer CTA label drifted ("Reservar una visita" vs. the mandated "Reservar una primera visita"). MEDIUM — nav/footer hover states not gated behind the hover-capability media query. LOW — footer link tap targets borderline under 24px; hero content had no no-JS fallback; missing `white-space: nowrap` on `.btn`. Verified clean: zero fabricated medical/statistical/credential claims anywhere on the site (the P1 gate this review exists to catch), correct `aria-current`, no keyboard traps, correctly-scoped icon accessible names.

**Fixes made (all of the above, applied in one consolidated pass and re-verified live in-browser after):**
- Structural: `.commitment-grid`/`.team-grid` rewritten to reuse the single-column spine-list device (`.step-list`/`.step`) instead of 3-up grids — verified by live re-render (screenshots confirm both sections now render as a continuous vertical line, not a grid).
- Contact form: fabricated success message replaced with a real `mailto:` fallback (to a clearly-placeholder `.example`-domain address) and honest status copy describing exactly what will happen. Submit button now disables briefly during the transition. Verified: empty-submit still shows correct validation errors, no console errors, `aria-invalid`/`aria-describedby` correctly wired (checked via DOM query).
- Focus ring: `--color-focus-ring` locally overridden inside `.cta-band` (→ on-accent) and `.site-footer` (→ paper) — verified live via keyboard Tab + zoomed screenshot showing a clearly visible ring in both locations.
- "Home" → "Inicio" (15 instances across 5 pages); footer CTA label unified to the mandated string (5 instances) — both verified live.
- `aria-describedby="X-hint X-error"` added to all 4 form fields.
- `TYPE-006` widow/orphan nbsp treatment extended from 1 heading to all 5 page H1s + all 4 CTA-band H2s.
- Breakpoints normalized: every `900px` → `1024px` (now a clean 640/768/1024 scale).
- Hover-gating added to nav-links and footer-col link states; `<noscript>` fallback added for the hero (guards against JS failure leaving hero content at `opacity: 0` forever); footer link tap-target padding added; dead `.btn--on-dark` class removed.
- Also fixed, found during my own live-rendering pass **before** Level 2 (not from either reviewer): a horizontal-overflow bug caused by an over-joined `&nbsp;` phrase in the hero H1 at mobile width, and a mobile content-ordering bug where an unscoped `order: 2` pushed the contact form below the placeholder info list on mobile (the primary task was landing second).

**Remaining limitations (disclosed, not fixed this pass):**
- The `mailto:` fallback is a real, functional mechanism, but not a production-grade booking system — a genuine backend/endpoint must replace it before this ships.
- The palette's SLOP-013 guessability risk is named but not acted on: the derivation is legitimate and it passes the specific SLOP-011 cluster check, but an independent reviewer still flagged it as a plausible first guess for this vertical by output alone. Judged not worth a late, high-risk palette change on an unconfirmed (vs. a demonstrated) defect — flagged for a future review instead of silently dropped.
- A handful of non-H1 section headings were not individually TYPE-006-checked at every breakpoint (H1s and the largest CTA-band H2s were prioritized) — a proportional-effort call, disclosed rather than claimed as full coverage.
- No automated axe-core-equivalent scanner exists in this environment; accessibility coverage is thorough manual/computed verification (contrast formula, live keyboard walks, DOM inspection) cross-checked by an independent reviewer, not exhaustive automated tooling.

---

## E. Distinctiveness

**"Would this structure still make sense if the brand name, copy, colors, imagery, and decorative motifs were removed?"**

Partially, and more honestly than before the fix — but not completely, and it's worth being precise rather than generous here. Strip everything decorative and what remains is: a fixed nav anchored to a hairline; one hairline rule as the *only* section-divider language, used identically on every page; and every repeated list on the site — services, approach, trust, team — attaching to the same single-column vertical spine rather than to a grid. That last part is the concrete structural evidence that changed after Level 2: before the fix, two of those four lists (trust, team) were generic equal-weight 3-up grids that could belong to any professional-services site; now all four use one consistent, non-default attachment device. That consistency is genuinely traceable to the brief's specific subject (a foundation everything aligns to), logged in `.design/context.md`'s DIRECT-stage reasoning, not a stock pattern reached for by default.

What this report won't claim is that a viewer encountering the bare structure would spontaneously think "vertebra" or "Atlas" — a hairline-anchored nav is still a recognizable general pattern, and the visual-critic's core point stands: the concept's legibility still leans partly on the Sobre Nosotros prose that names it outright. The honest claim is narrower: the structure is *consistent with* the concept and was *derived from* it (traceable in the DIRECT/LAYOUT-009 reasoning and in the actual rejection of a grid-based alternative), not that the structure alone would make a stranger guess the brand name unaided.

---

## F. Final quality assessment

**Strongest aspect:** the production/craft floor — accessibility, contrast, focus handling, motion discipline, and the honesty of the placeholder/fabrication handling (team, contact info, and now the form-submission mechanism) are all genuinely solid and were independently verified, not just self-reported.

**Weakest aspect:** distinctiveness still carries real, disclosed risk at the palette level (SLOP-013 — warm stone + cedar green is a plausible first guess for this vertical even with a legitimate derivation story) and, more structurally, the concept's legibility still depends partly on being told in copy, not purely on being seen in structure.

**Biggest remaining risk:** the contact form's `mailto:` fallback is a real, honest mechanism but not a production-grade one — it must be replaced with an actual booking/email backend before this ships, and that limitation is flagged explicitly rather than left to read as finished.

**Would this swap into another premium professional-services site?** Less easily than before the Level 2 fixes, but not zero. The typography pairing, the single consistent spine device (not a grid) for every repeated list, and the subject-derived (if guessable) palette are real, checkable points of derivation from this specific brief — evidenced by the DIRECT-stage rejection log, the concrete structural rewrite the critique forced, and the computed color/contrast trail. What keeps it from a clean "no" is that the underlying pattern family (hairline nav, spine-attached lists, solid CTA band, inverted footer) is still a competently-executed instance of a broader editorial-services vocabulary, not a wholly novel one — which is a fair, not a failing, place to land for a calm, professional, "premium without pretentious" brief that explicitly asked to avoid decorative excess.

---

## G. Summary — Successes and Gaps

### Successes

- **Concept Detection works.** The Atlas naming/symbol rationale was identified at DEFINE as real, brief-supplied evidence, not invented.
- **Concept → Structure works.** The concept was translated into an organizing decision (macrostructure + navigation, later extended to every repeated list), not left as decoration.
- **LAYOUT-009 works.** The three-step procedure (brief concept → abstract structural principle → selected structural expression) ran as specified and produced a traceable, non-decorative result.
- **EXPLORE incorporates structural interpretations.** DIRECT's two-candidate comparison carried genuinely different structural expressions of the same concept (Anchored Datum vs. Ascending Path), not just two skins.
- **Level 2 detected that the first implementation was still too generic.** An independent, isolated reviewer caught exactly the gap the mechanism exists to catch — the concept was still leaning on copy/decoration more than structure — rather than rubber-stamping the first pass.
- **Refinement turned the concept into a real structural pattern.** The post-critique fix was a genuine structural rewrite (two grid-shaped sections converted to the same spine device used elsewhere), not a cosmetic patch, and was re-verified live in-browser afterward.
- **No regressions from Phase 6.1.**

### Gaps

- **The visual language still converges toward editorial-premium.** Even with a subject-derived, non-category-reflex justification, the palette and macrostructure land inside a recognizable editorial-premium band rather than somewhere more surprising.
- **The identity still partially depends on copy/concept explanation.** The structure is consistent with and derived from the concept, but a viewer encountering the bare structure alone likely would not infer "Atlas" without the About-page prose naming it.
- **CTA/action hierarchy on mobile is not sufficiently defined.** Validation covered responsive layout, overflow, and focus correctness at mobile widths, but did not separately interrogate whether the primary/secondary CTA weighting and repetition are the right hierarchy for a mobile conversion flow specifically.
- **Visual quality is improving, but the exploration space needs to widen before selecting a direction.** DIRECT generated two candidates and picked between them; it did not range widely enough to test whether a materially different visual language (beyond editorial-premium) could have served this brief as well or better.
