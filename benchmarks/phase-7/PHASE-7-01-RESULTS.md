# PHASE 7 — TEST 01 — Benchmark Results

## 1. Brief

Build a complete, production-quality responsive website for MOVA, a premium
physiotherapy and movement clinic in Barcelona, for adults dealing with
musculoskeletal pain, mobility limitations, postural issues, sports-related
discomfort, or long-term physical wellbeing goals. Five pages: Home,
Tratamientos, El centro, Equipo, Contacto. All copy in Spanish. Hard
constraint: no fabricated medical claims, certifications, stats, named staff,
credentials, or testimonials — any real information that doesn't exist yet
(address, phone, team photos/names) must appear as a clearly-marked
placeholder, never disguised as real content. Design direction: distinctive
and intentional, explicitly not a generic SaaS/wellness/medical template, and
explicitly not a generic "premium editorial" template either — with an
equally explicit instruction not to manufacture a conceptual metaphor purely
to manufacture distinctiveness.

## 2. Routing

- **Scope:** multi-page site (5 pages, one shared design system)
- **Project state:** genuinely-empty (project directory contained only the
  design-excellence skill symlink and an unrelated `ruvector.db` file; no
  prior design decisions existed)
- **Task mode:** BUILD
- **Register:** brand-led
- **Genre:** editorial
- **DESIGN_VARIANCE:** 7/10 (Medium band, upper end)
- **MOTION_INTENSITY:** 3/10 (Low band)
- **VISUAL_DENSITY:** 5/10 (Medium band)

Full reasoning for each is recorded in `.design/context.md`, written after
DEFINE per the skill's own sequencing rule (context file created only once
the classification exists).

## 3. Design Direction

### Design Read

A calm, content-forward editorial system built for someone deciding whether
to trust a clinic before they've met anyone there: generous asymmetric
rhythm, a warm stone-and-bronze palette that avoids both the wellness-green
and medical-blue category reflexes, humanist sans typography (not serif) to
keep "premium" from reading as "cold formality," and structural devices —
an index-style list of who the clinic helps, oversized numerals marking the
first-visit sequence, a rule-segmented contact block — doing the work that
decorative cards or icons would otherwise be reached for reflexively. Each of
the five pages has its own content-derived macrostructure (no repeated
hero→cards→CTA template) while sharing one type/color system for brand
coherence.

### Concept

**HYPOTHESIS**, not DETECTED / EVIDENCED.

The brief's own text gives no naming rationale, no request to embody a
specific idea, and no recurring reference object treated as central to the
identity — so DETECTED / EVIDENCED does not apply. A real, checkable
hypothesis does exist and is disclosed here for completeness: "MOVA"
phonetically echoes the Spanish/Catalan verb root for "move" (mover/moure),
which resonates with a movement-focused physiotherapy clinic. This is a
plausible, checkable association I am supplying, not something the brief
states — per the three-state model, that makes it a HYPOTHESIS by
definition, and per the benchmark's own explicit instruction not to
manufacture a concept for distinctiveness's sake, it was deliberately **not**
promoted into a structural organizing principle anywhere in the build. It
does not appear in the Rejected Directions log as a concept-detected entry,
is not a hidden justification for any layout choice, and could be deleted
from this report with zero effect on the actual design.

### Concept → Structure (LAYOUT-009)

**Not activated.** LAYOUT-009's mandatory translation procedure only fires
on a DEFINE outcome of DETECTED / EVIDENCED. This project's outcome is
HYPOTHESIS, which explicitly does not trigger it (Phase 6.5 tightening,
`layout-interaction.md`). No rule was bypassed here — the rule's own stated
applicability excludes this case.

### Visual References (LAYOUT-010)

Loaded (T3, `visual-references.md`), as required whenever DIRECT/EXPLORE
runs for a new visual system at page/multi-page-site scope. All 9 entries
were read; 2–3 were weighed seriously per the rule's own "consider at most
2–3, never the whole file" guidance, the rest screened out at the
compatibility/applicability stage.

**Adopted:**
- **REF-004** (oversized structural numerals as dividers) — used for the
  "Cómo funciona tu primera visita" three-step sequence on Home. It replaces
  what would otherwise default to a 3-card layout (the exact pattern the
  brief bans) with numerals doing real structural work — marking sequence
  boundaries — rather than decoration.
- **REF-009** (segmentation-by-rule on a bounded canvas) — used for the
  Contacto page's address/phone/email/hours block. That block is a genuinely
  bounded, non-scrolling set of independent facts, which is exactly what this
  reference's `compatible_with` scopes it to.

**Considered and rejected**, with the specific reason each failed
compatibility, applicability, or register fit — full detail in
`.design/context.md`: REF-001 (fixed nav column — mobile-collapse risk),
REF-002 (motion-weight mismatch with this project's Low band), REF-003
(index-as-nav — usability cost for a first-time trust-evaluating visitor),
REF-005 (no real process photography exists — adopting it risks implying
fabricated authenticity), REF-006 (motion-weight mismatch), REF-007
(register/genre mismatch, and a multi-color-coded system would undercut the
calm register), REF-008 (its own `do_not_apply_to` names "brand-led
marketing content whose job is persuasion before commitment" — an exact
match to this brief, making rejection closer to mechanical than judgment).

No reference was adopted merely because it was available — REF-001, 002,
003, 005, 006, 007, 008 were all seriously weighed and explicitly rejected,
not skipped.

## 4. Major Design Decisions

- **Macrostructure:** one content-derived bundle per page (Home:
  narrative-conversion; Tratamientos: flat structured index, no hero;
  El centro: alternating long-form text/image bands; Equipo: directory grid
  plus a short statement; Contacto: bounded utility block plus a form) —
  never the same hero→3-card→CTA shape repeated with different copy.
- **Navigation:** conventional persistent top nav plus a full-screen mobile
  disclosure, not an index-as-navigation pattern (REF-003, rejected) — a
  first-time visitor deciding whether to trust a clinic needs fast, familiar
  wayfinding to Contacto more than a novel pattern.
- **Typography:** General Sans (display) + IBM Plex Sans (body), chosen via
  the TYPE-002 voice-word procedure (calm/expert/human → "a quiet room" / "a
  calibrated instrument" / "a handwritten note"), explicitly rejecting the
  current serif-editorial reflex (Fraunces/Playfair-adjacent) and the
  soft-wellness reflex (Poppins/Quicksand-adjacent) alike.
- **Color:** OKLCH-constructed warm stone paper / warm near-black ink / muted
  bronze accent — deliberately clear of both the wellness-green and
  medical-blue category defaults (SLOP-013) and clear of the
  cream+serif+terracotta self-tell cluster (SLOP-011) because type is sans,
  not serif, and paper is a greyer stone, not cream.
- **Layout:** index-list and rule-segmented structures used in place of card
  grids wherever the content was a flat set of comparable items; cards used
  only twice, in small counts (2 and 3), for genuinely distinct content —
  never the "every section is a card" default the brief bans.
- **Imagery:** no real photography exists, so hero/environment imagery is
  represented by honest abstract CSS placeholder panels, explicitly labeled
  as pending, never styled to resemble real photography. Tratamientos and
  Contacto carry no imagery at all — a deliberate LAYOUT-008 decision, not an
  oversight, because imagery there would be decorative filler on utility
  pages.
- **Interaction:** hover/focus/active/disabled states built for every
  interactive element; hover specifically gated behind
  `(hover: hover) and (pointer: fine)` after a VALIDATE-stage check caught it
  missing (see §5/§6).
- **Motion:** one orchestrated hero reveal (IntersectionObserver-gated,
  respects `prefers-reduced-motion`), everything else is functional
  state-transition motion only — no scroll-triggered decorative reveals.
- **Responsive behavior:** the header CTA text moves into the mobile menu
  below 900px rather than crowding the header (INTX-004 — multiple competing
  actions in one narrow region); the mobile nav is a real full-screen
  disclosure with a focus trap, not a shrunk desktop nav.
- **CTA hierarchy:** "Reservar una primera visita" (primary, filled) always
  outranks "Conocer el centro" (secondary, outlined) wherever both appear
  together, and the label never changes across header/hero/CTA-band/footer
  (CONTENT-001 vocabulary consistency).

## 5. Critique

### Level 1 (self-critique floor, run during BUILD/VALIDATE)

Scored informally against the six axes as the build progressed, ahead of
dispatching Level 2:

1. **Genericness** — 4/5 at first pass. Macrostructure and typography read
   as content-derived, not defaulted. Flagged myself that the color anchor
   deserved real scrutiny against SLOP-011's clusters rather than a quick
   "it's not literally cream/serif/terracotta" pass — Level 2 confirmed this
   instinct was right (see below).
2. **Hierarchy** — 5/5. Squint test passed on every page at build time.
3. **Distinctiveness** — 4/5. Five genuinely different page shapes,
   documented in the Fingerprint History table.
4. **Craft correctness** — one self-flagged tension, not resolved by simply
   deferring to the rule's letter: `MOTION-004` restricts animation to
   `transform`/`opacity`/`clip-path`, but `.btn`/`.nav-primary__list a`/
   `.text-link` transition `background-color`/`border-color`/`color` too.
   Reasoned in the moment that these are repaint-only, not layout-triggering,
   properties — the specific harm `MOTION-004`'s own evidence names
   ("layout thrash and jank") doesn't actually apply to a color transition —
   and kept them as the industry-standard hover treatment rather than
   stripping every color transition to satisfy the rule's literal text. Logged
   here rather than silently deviated from; see §10.
5. **Accessibility** — computed, not assumed: every text/non-text contrast
   pair verified via a canvas-based OKLCH→sRGB→WCAG-luminance script during
   VALIDATE, which is how the `ink-faint` (3.89:1, failed) and `line-strong`
   (2.26:1, failed) contrast bugs were caught and fixed before Level 2 ever
   ran (documented in `.design/context.md` Known Exceptions).
6. **Technical correctness** — mechanical checks run at build time: no
   horizontal overflow at 320/375px (all 5 pages), no `@keyframes` anywhere,
   `prefers-reduced-motion` verified via media emulation, hover states
   confirmed gated behind `(hover: hover) and (pointer: fine)` after a
   self-caught bug (all bare `:hover` rules were originally unguarded).

### Level 2 (independent critique — triggered)

**Triggered: YES.** Reason: `critique-protocol.md`'s explicit trigger —
Task Mode = BUILD, Project State = genuinely-empty, multi-page-site scope,
and the brief states an explicit brand-quality bar ("premium physiotherapy
and movement clinic," used repeatedly). This is the named trigger condition,
not a judgment call.

**Mechanism:** two genuinely fresh, isolated agents (not forks — this
session's context was withheld from both), matching `critique-protocol.md`'s
preference for a purpose-built specialist agent over a generic one:
`lexia-design:visual-critic` (genericness/hierarchy/distinctiveness/craft,
against the requested six-axis rubric) and `lexia-design:ux-auditor`
(WCAG/keyboard/forms/content-integrity). Both were given the brief, the live
site, the file paths, and the six-axis rubric — neither was given this
session's own Level 1 scores or findings, per the protocol's dual-blind
requirement.

**Visual-critic findings (verdict: "B-tier, not A"):**
- **HIGH** — `.info-panel__placeholder`'s accent-text color token (tuned for
  the paper background) was reused verbatim inside the dark footer on all 5
  pages, producing low-contrast placeholder text next to legible white nav
  links on the same background. **Confirmed and fixed** (§6).
- **MEDIUM** — the paper+accent color gestalt, judged as a combination
  rather than dimension-by-dimension, still read close to SLOP-011's
  cluster 1 ("warm cream + serif + terracotta") even after the serif→sans
  divergence — the typeface swap was real but was carrying the whole
  distinctiveness argument alone. **Confirmed and fixed** (§6) — the entire
  palette hue was rotated from ~50° (rust/terracotta) to ~78–90°
  (brass/ochre), every lightness value held constant so every already-verified
  contrast ratio stayed valid.
- **LOW** — eyebrow/kicker micro-labels exceeded the registry's own quota
  (≤1 per 3 sections, SLOP-003) on Home (4 in 5 sections) and El centro (3 in
  4). **Confirmed and fixed** (§6).
- **LOW** — the "editorial" genre label, read against a *different* skill
  package's own taxonomy (the critic agent's own `lexia-design` system, which
  defines "editorial" as serif-requiring), looks mislabeled; against this
  project's actual governing taxonomy (`style-catalog.md`'s
  STYLE-EDITORIAL-01, which explicitly rejects serif-as-default) it isn't.
  **Addressed via documentation**, not a design change (§6) — this is a
  naming-ambiguity risk for a future reader, not an execution defect.
- What the critic verified as genuinely solid (not just claimed): no serif
  reflex, no gradient text, no italic display type, no em-dash-as-separator,
  no middle-dot meta strings, no arrow-on-every-link, zero `box-shadow`
  anywhere, one accent color used consistently across all 5 pages, motion
  claims verified in code (not just asserted), five genuinely distinct
  macrostructures confirmed visually.

**UX-auditor findings:**
- **CRITICAL** — primary hero content (H1, lede, both CTAs) was opacity-0 by
  default in CSS, with only JavaScript ever adding the class that reveals it,
  and no `<noscript>` fallback; the mobile nav toggle is also fully
  JS-dependent with no non-JS affordance. A JS failure (blocked, CSP,
  ad-blocker, script error, disabled) would leave a mobile visitor with
  invisible primary content and an inert hamburger button. **Confirmed and
  fixed** (§6) — this is the single most serious finding of the whole
  benchmark.
- **HIGH** — the contact form's only functional path was
  `method="post" action="mailto:contacto@example.com"`, a combination the
  auditor correctly identified as producing inconsistent cross-browser
  behavior, pointed at a guaranteed-undeliverable placeholder address, with
  no success/error state shown to the user. **Confirmed and fixed** (§6).
- **HIGH** — the mobile nav panel had no `overflow-y`, so on a sufficiently
  short viewport (landscape phone, a split-screen pane) its content —
  including the primary CTA — could render past the reachable area while
  page scroll was locked. **Confirmed and fixed** (§6).
- **MODERATE** — the open mobile nav didn't mark background `<main>` content
  `inert`/`aria-hidden`, so swipe/virtual-cursor screen-reader navigation
  (the primary mobile AT mode, which ignores the keyboard focus trap) could
  still reach fully-occluded content behind the overlay. **Confirmed and
  fixed** (§6).
- **MODERATE** — the nav-toggle button's `aria-label` stayed
  "Abrir menú..." even while open and functioning as a close control (only
  `aria-expanded` updated). **Confirmed and fixed** (§6).
- **MODERATE** — a real, self-inflicted regression: fixing the visual-critic's
  HIGH footer-contrast finding by stripping `.info-panel__placeholder`'s
  class from the footer spans also stripped the *visual signal* that the
  text was a placeholder at all, creating a fresh inconsistency against the
  Contacto page's own info-panel, which still used the accent-colored
  treatment for the same kind of content. **Confirmed and fixed** (§6, §9).
- **MINOR** — no `aria-live` error-count summary on form submit (partially
  mitigated by existing focus-to-first-error + per-field
  `aria-describedby`). **Confirmed and fixed** (§6).
- What the auditor verified as genuinely solid (independently recomputed,
  not taken on trust): every contrast pair in the *current* (post-hue-rotation)
  palette, reduced-motion (double-covered — CSS media query and a JS
  short-circuit), consistent `:focus-visible` treatment site-wide, correctly
  gated hover states, a correctly implemented Tab-cycling keyboard trap,
  16px input font-size (iOS zoom prevention), reserved error-hint space (no
  reflow), zero fabricated claims anywhere across all 5 pages, correct
  landmark labeling, and clean sequential heading structure on every page.

## 6. Refinements

Every confirmed finding above was fixed, verified by rendered/computed
re-check (not re-asserted), in this order:

1. **Footer contrast (visual-critic HIGH):** removed the light-surface-tuned
   `.info-panel__placeholder` class from the footer spans. Verified:
   3.89:1→(was already fixed to 5.45:1 pre-critique for the label text; the
   nested placeholder span specifically went from an unmeasured/likely-failing
   pair to correctly inheriting the dark-surface-safe token).
2. **Color-gestalt genericness (visual-critic MEDIUM):** rotated the entire
   OKLCH palette (paper/ink/neutrals/accent) from a ~50° rust/terracotta hue
   family to a ~78–90° brass/ochre family, holding every lightness value
   constant. Re-verified all 8 contrast pairs post-rotation — all still pass
   (`ink/paper` 15.14:1, `accent-text/paper` 9.00:1, `on-accent/accent`
   6.26:1, `line-strong/paper` 4.92:1, etc.).
3. **Eyebrow quota (visual-critic LOW):** removed 3 of 4 eyebrows on Home
   (kept only the hero eyebrow) and 1 of 3 on El centro (kept "El centro" and
   "Filosofía," cut the one directly duplicating its adjacent h2). Both pages
   now sit at or under `ceil(sectionCount/3)`.
4. **Genre-label ambiguity (visual-critic LOW):** added an explicit note to
   `.design/context.md` clarifying "editorial" follows this skill's own
   STYLE-EDITORIAL-01 definition (serif not required), not a
   serif-defining taxonomy a different reviewer might assume.
5. **Hero content JS-dependency (ux-auditor CRITICAL):** restructured the
   reveal so `.hero__reveal` is visible by default in CSS; JavaScript now
   opts the element *into* a hidden `.is-pending` state only at the moment
   it also sets up the `IntersectionObserver` guaranteed to reveal it.
   Verified by computing the element's style with the JS-added classes
   stripped: `opacity: 1` — confirmed safe with JS absent or failed.
6. **Contact form reliability + missing states (ux-auditor HIGH):** removed
   the unreliable `method="post" action="mailto:"` combination; JS now
   builds the `mailto:` URL from the actual field values and navigates to it
   on valid submit, and a `role="status"` region shows a real confirmation
   message ("se está abriendo tu aplicación de correo...") or a real
   validation-error count ("Faltan completar N campos"). The disclosure copy
   was rewritten to say plainly that no real inbox is connected yet, rather
   than implying the current path works and will merely be upgraded later.
7. **Mobile nav overflow (ux-auditor HIGH):** added `overflow-y: auto` and
   `overscroll-behavior: contain` to `.nav-mobile`.
8. **Background inertness (ux-auditor MODERATE):** JS now toggles `inert` on
   `<main>` and the header wordmark link whenever the mobile nav is open.
   Verified: `main.hasAttribute('inert')` is `true` while open, `false`
   after close.
9. **Stale toggle label (ux-auditor MODERATE):** `aria-label` now flips
   between "Abrir menú de navegación" / "Cerrar menú de navegación" in the
   same function that already updates `aria-expanded`. Verified live.
10. **Placeholder-signal regression (ux-auditor MODERATE, caused by fix #1):**
    added a new dark-surface-safe token, `--color-accent-on-dark`
    (oklch(68% 0.1 78), 5.80:1 on `--color-ink`), and a `.placeholder-on-dark`
    class, restoring the accent-colored "this is unresolved" visual signal in
    the footer without reintroducing the original contrast failure.
11. **Error-count announcement (ux-auditor MINOR):** the same `role="status"`
    region added for fix #6 also announces the invalid-field count on a
    failed submit, closing this gap as a side effect.
12. **Self-caught regression during refinement:** the bulk find/replace used
    for fix #1 was string-based and not scoped to the footer, and also
    matched two light-background paragraphs on the Contacto page (the info
    panel's disclosure line and the form's own disclosure line), flipping
    them to the dark-surface token on a light background — the inverse
    contrast bug. Caught by grepping every `on-dark-faint` usage across all 5
    files before considering the fix complete, not by an external reviewer.
    Reverted those two lines to `--color-ink-faint`.

## 7. Final Assessment

### Strengths
Content-derived macrostructure per page (no repeated hero→cards→CTA
template); a color/type system that was measurably, not just assertedly,
pushed clear of the current AI-generation self-tell clusters after an
independent reviewer caught the first draft sitting too close to one;
zero fabricated content anywhere across 5 pages (independently verified);
a genuinely solid accessibility foundation (contrast, focus, reduced motion,
landmarks, keyboard trap) that held up under independent re-measurement;
a caught-and-fixed critical JS-dependency bug that would otherwise have
shipped a broken mobile experience.

### Weaknesses
The mobile nav toggle itself still has no non-JS affordance (mitigated by
the hero CTAs and footer nav both being plain, always-functional `<a>`
tags — see §11); the contact form has no real backend and cannot, since none
was supplied — the `mailto:` approach is now honestly disclosed and more
reliable than the original, but it's still not a working booking system;
three of five pages (Tratamientos, El centro, Equipo) were not directly
screenshotted by the UX auditor at 320/375/768px (shared header/nav/grid
patterns make a major divergence unlikely, but this is an honest coverage
gap, not a verified pass).

### Visual Personality
Calm, restrained, structurally confident — oversized numerals and
rule-segmented lists as the signature devices, per the adopted Visual
References. An independent reviewer's fair characterization: distinctiveness
is currently carried by those two structural devices more than by the base
palette/type combination alone, even after the hue correction.

### Distinctiveness
Real but not maximal — five genuinely different page shapes sharing one
brand system, which is the intended, deliberate outcome (LAYOUT-001's own
exception for consistent cross-page branding), not a shortfall against a
higher bar the brief actually asked for.

### UX Quality
Strong component-level craft (states, validation, focus management)
undermined, before Level 2, by one critical macro-level gap (content
existing only behind JavaScript) that no amount of component polish would
have caught without an independent, fresh-context review actually exercising
the failure condition.

### Responsive Quality
No horizontal overflow at 320px on any of the 5 pages (verified directly, all
5); no wrapped clickable text observed at any tested breakpoint; the header
CTA correctly moves into the mobile menu below 900px rather than crowding the
header. Mobile nav short-viewport reachability was a real, now-fixed risk.

### Accessibility
WCAG 2.2 AA contrast holds across every measured pair (computed twice,
independently, by two different scripts — mine during VALIDATE, the
auditor's during Level 2 — landing on the same conclusions). The one
critical gap (content behind JS) is fixed. `inert` on background content
during the mobile nav overlay and a live status region for form
validation/confirmation are now in place.

### Performance
No real `<img>` elements exist anywhere (all imagery is CSS-drawn honest
placeholders), which structurally eliminates the entire
lazy-loaded-LCP/missing-dimensions/CLS class of finding rather than avoiding
it through discipline. Two web fonts loaded with `font-display: swap` and
`preconnect` hints. No JS framework, no build step, ~130 lines of hand-written
JS total.

### Maintainability
Plain HTML/CSS/JS, zero dependencies to install, deployable by copying files
to any static host. The single 919-line `styles.css` exceeds the general
800-line file-size guideline — a deliberate, disclosed choice (§11), not an
oversight.

## 8. Genericness Check

Closer to **a genuinely specific design** than the other three options, but
not by the widest possible margin, and only after a real correction. The
first-draft palette (rust/terracotta accent on a slightly cream-leaning
paper) would have landed closer to "sophisticated AI-generated website" —
specifically, close enough to one of the four named current self-tell
clusters (`SLOP-011`) that an independent reviewer flagged it as a gestalt
match even though every individual element passed its own atomic rule. That
finding, and the fact that this system caught and fixed it rather than
asserting the first draft was already fine, is itself evidence for how this
benchmark should be read: the mechanism worked, but the first attempt alone
would not have been enough. What's left after the fix is genuinely
brief-derived (five content-shaped macrostructures, a typeface pairing
reasoned from voice-words and cross-checked against the category stereotype,
oversized numerals and rule-segmentation doing real structural work) rather
than a template with MOVA's name inserted — but an independent reviewer's
own words are worth keeping rather than softening: "cover the MOVA wordmark
on the home screenshot and this could plausibly ship for an architecture
studio, a dental practice, or a boutique consultancy." That is a genuine,
fair limit on how far the distinctiveness claim should be pushed.

## 9. Unexpected Behavior

- The single most consequential finding of this benchmark (invisible hero
  content without JS) was not something any of the rule-catalog files,
  the anti-slop registry, or my own Level 1 self-critique caught — it took
  an independent agent actually reasoning about the JS-dependency chain in
  the source, which is exactly the class of blind spot Level 2 critique
  exists to catch and which this benchmark's own critique-protocol.md
  predicted in the abstract ("a second, differently-biased reviewer earns
  its cost").
- Fixing one Level 2 finding (visual-critic's footer contrast bug) directly
  caused a second, different Level 2 finding (ux-auditor's placeholder-signal
  regression) in the same code path — the two independent reviewers were
  genuinely looking at different snapshots in time and caught two different
  real problems in the same three lines of markup, which is a small,
  concrete demonstration of why the protocol insists on isolation instead of
  a single reviewer trying to hold both concerns at once.
- My own REFINE-stage fix for that first bug was itself sloppy — a
  string-based find/replace not scoped narrowly enough — and introduced a
  third, real regression (dark-surface text token applied to a light
  background) that neither agent happened to catch, because it landed after
  their review. I found it myself only by grepping every usage of the token
  before considering the fix complete, which is the discipline this
  benchmark's VALIDATE stage is supposed to instill, applied a second time
  during REFINE rather than only once during BUILD.
- The visual-critic agent evaluated this project's "editorial" genre label
  against a different skill package's own taxonomy (its own `lexia-design`
  system) rather than the taxonomy actually governing this build
  (`design-excellence`'s `style-catalog.md`). The finding is still useful
  (a future reader could make the same category error), but it's worth
  naming explicitly that an independent critic agent came with its own
  priors from outside this skill's own rule system.

## 10. Rule Failures

Documented, not fixed in the skill, per instructions:

- **No rule in the loaded catalog names "content must never depend on
  JavaScript to become visible/reachable" as its own check.**
  `accessibility.md`'s enumerated P1 list covers contrast,
  keyboard operability, and reduced-motion — all real and all checked — but
  a JS-failure content-visibility gate isn't one of the four, and no other
  file in `references/rule-catalog/` names it either. This benchmark's most
  severe finding fell through that specific gap and was only caught because
  a Level 2 reviewer happened to read the interaction code closely enough to
  trace the causal chain manually. Given how common motion-on-load /
  reveal-on-scroll patterns are in exactly the kind of premium/brand-led
  build this skill targets, this looks like a real, addressable gap rather
  than an edge case.
- **`MOTION-004`'s literal text is stricter than its own stated
  justification.** The rule restricts animation to
  `transform`/`opacity`/`clip-path` and calls anything else "a performance
  finding," justified by "layout thrash and jank." `background-color`,
  `border-color`, and `color` transitions (used throughout for hover/focus
  states in this build) are repaint-only, not layout-triggering — the
  specific harm the rule's own evidence names doesn't actually apply to
  them. Applied here as a disclosed, reasoned exception (§5) rather than a
  silent deviation, but the rule as written doesn't leave room for that
  exception explicitly, unlike `MOTION-011`'s bounce/elastic entry, which
  does carve out its own conditional cases.
- **`LAYOUT-007`'s Medium-band spacing guidance is genuinely ambiguous in a
  way that mattered in practice.** The rule states Low band = "generous...
  48–96px separation between major sections" and Medium "sits between the
  two [Low and High] and is the default." Read literally, Medium's actual
  pixel range is *undefined* — "between Low's 48–96px and High's smaller
  range" doesn't resolve to a number without also knowing High's range,
  which the rule doesn't state either. I made a judgment call (a combined
  inter-section gap in the 90–130px range, using `--space-xl`/`--space-lg`
  tokens) and adjusted it once by eye during VALIDATE, but this is a
  real spec gap, not a case where I simply failed to read carefully enough.

## 11. Remaining Risks

- **Mobile nav toggle has no non-JS fallback.** If JavaScript fails on a
  mobile device, the hamburger button does nothing. This is meaningfully
  de-risked by the CRITICAL fix in §6 (hero CTAs are plain `<a>` tags,
  always functional) and by the footer nav (also plain `<a>` tags, always
  present) — a JS-failure visitor retains a path to every page, just not via
  the header menu — but it is not a full fix, and I did not attempt a
  `<details>`-based native-fallback rebuild of the mobile nav under this
  benchmark's time budget, because that would have been a larger, riskier
  change than I could fully re-validate.
- **The contact form has no real backend**, by necessity (no real MOVA
  business exists to receive email). The `mailto:` approach is now honestly
  disclosed and technically more reliable than the original, but it remains
  a stand-in a real integration must eventually replace.
- **Three pages (Tratamientos, El centro, Equipo) were not independently
  screenshotted at mobile widths by the Level 2 UX audit** — flagged
  honestly by that agent as a coverage gap in its own report, not asserted
  as a pass. I did verify all 5 pages have zero horizontal overflow at
  320px directly (§6/VALIDATE), but a full mobile visual pass on those 3
  pages specifically was not independently re-confirmed after the palette
  and eyebrow changes in §6.
- **`styles.css` is 919 lines**, above the general 800-line file-size
  guideline. Deliberate: splitting a single small design-token system for a
  5-page static site with no build step would trade one clear file for
  either a build dependency (contradicting "avoid unnecessary dependencies")
  or several more render-blocking requests (working against `PERF-001`).
  Worth revisiting only if this project grows substantially past 5 pages.
- **No automated test suite.** Not requested by the brief, and this task
  type (a static marketing site, not an application with logic to regress)
  doesn't obviously call for one — but noted for completeness rather than
  silently assumed to be out of scope.
- **All contact/team information is placeholder**, by design, pending real
  business data — the site cannot go live as-is, which is the correct and
  intended state for this benchmark, not a defect.

## 12. Verdict

**PASS WITH RISKS.**

The benchmark surfaced a genuine CRITICAL defect (content invisible without
JavaScript) that Level 1 self-critique, mechanical VALIDATE checks, and the
builder's own judgment all missed, and that only the mandated Level 2
independent review caught — a direct, concrete justification for why that
stakes-gated escalation exists rather than being a default-off nicety. It
also surfaced a real MEDIUM genericness finding (a color gestalt too close
to a named current self-tell cluster despite a genuine, defensible serif→sans
divergence) that Level 1's own gestalt-check instruction should have caught
more decisively than it did. Both were fixed and re-verified, not merely
acknowledged. The process also caught its own follow-on mistakes (a fix that
broke a different property, and a bulk edit that overshot its scope) before
calling the work finished, rather than stopping at the first green check.
What remains is disclosed, not hidden: a partial (not complete) JS-dependency
fix on the mobile nav toggle, a contact form that is honestly a stand-in for
infrastructure that doesn't exist yet, and one un-reconfirmed mobile-viewport
coverage gap across three pages. None of these block the verdict from being
a pass; all of them are reasons it isn't an unqualified one.
