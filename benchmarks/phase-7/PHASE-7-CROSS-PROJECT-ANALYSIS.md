# Phase 7 — Cross-Project Analysis

Source: `PHASE-7-01-RESULTS.md` through `PHASE-7-06R-RESULTS.md` (six benchmark runs,
read in full from `~/Desktop/`). Architecture cross-checked against `SKILL.md` and
`references/{critique-protocol,rule-catalog/*}.md` only where a report's claim about a
mechanism needed verification. This document is analysis only — no skill file was
modified to produce it.

---

## 1. Executive Summary

**Status:** Phase 7 passed. Five of six runs recorded an explicit verdict (three PASS,
two PASS WITH RISKS); the sixth (06R/ORBIT) is a genuinely strong redesign but its own
report is structurally incomplete — it stops at §8 (Remaining Risks) without the
Genericness Check / Unexpected Behavior / Rule Failures / Verdict sections every other
report carries. That is a reporting gap, not evidence of a weaker build; it is called
out explicitly wherever it narrows this analysis's evidence base (Benchmark Matrix,
§8).

**Strongest validated mechanisms:** rendered-browser validation (every test found real,
source-invisible bugs this way — image collapses, overflow, focus traps, contrast
failures); the Level 2 dual-blind critique escalation, which fired exactly where its
own stated trigger conditions predict (4/6) and correctly did not fire where they don't
(2/6), and caught genuinely independent, previously-unmissed defects every time it ran;
and Concept Governance, which resolved HYPOTHESIS or NOT DETECTED in all six runs with
zero false DETECTED/EVIDENCED outcomes and zero forced concept-metaphors.

**Most important recurring issue:** a cluster of individually defensible, often
brief-justified design decisions — restrained neutral palette with one muted accent,
near-zero shadow/radius, rule-segmentation over cards, and near-uniform Low motion —
recurred across all six genuinely different domains, and two independently dispatched
critic agents (Test 01, Test 04) named the resemblance to a recognizable aesthetic
unprompted. A second, narrower pattern — REF-009 (rule-segmentation) adopted in 6/6
tests — is the single most load-bearing recurring structural decision in the entire
benchmark.

**Evidence of refined-AI convergence:** worth monitoring. Real and specific (not vague
aesthetic complaint), but confounded by the fact that nearly every brief in this
benchmark itself explicitly instructs against card grids, gradients, and generic
category tells — meaning some of the convergence is a correct, repeated response to a
repeated instruction, not proof of an independent skill bias. Not strong enough to
justify a new rule (§5.4, §9).

**Architecture verdict:** no core changes required before Reicon/Kinetics/SmoothUI
integration. Two narrow, textually concrete rule-catalog gaps (MOTION-004/007 tension;
no rule names JS-independent content visibility) recurred or produced real defects and
are worth a targeted correction pass first (§10, §11 — Option B).

---

## 2. Benchmark Matrix

| Test | Domain | Project State | Register / Genre | Result | Level 2 | Visual References | Concept Status | Main Finding |
|---|---|---|---|---|---|---|---|---|
| 01 MOVA | Local/professional service (physiotherapy clinic) | genuinely-empty | brand-led / editorial | PASS WITH RISKS | Triggered — explicit brand-quality-bar phrase | Adopted REF-004, REF-009; 7 rejected | HYPOTHESIS | Level 2 caught a CRITICAL JS-dependent hero-content bug and a SLOP-011-adjacent palette; both fixed |
| 02 Signal | SaaS product marketing | genuinely-empty | product-led / modern-minimal | PASS | Not triggered — no brand-quality-bar phrase | Adopted REF-007 (narrow scope), REF-009; 7 rejected | HYPOTHESIS | Hero avoided the brief-named dashboard-screenshot cliché; 4 rendered-only bugs found and fixed |
| 03 NORTE | Editorial publication (cities/architecture) | genuinely-empty | brand-led / editorial | PASS | Triggered — explicit quality-bar phrase | Adopted REF-001, REF-009; 6 rejected | NOT DETECTED | MOTION-004/007 tension named explicitly; Level 2 flagged an under-committed accent color |
| 04 FORMA | E-commerce (furniture) | genuinely-empty | hybrid / modern-minimal | PASS WITH RISKS | Triggered — explicit brand-quality-bar phrase | Adopted REF-007, REF-009; 7 rejected | HYPOTHESIS | Distinctiveness front-loaded on the homepage; Level 2 caught a CRITICAL focus-trap gap and a color self-collision |
| 05 PULSE | Ops dashboard (B2B) | genuinely-empty | product-led / modern-minimal | PASS | Not triggered — no brand-quality-bar phrase | Adopted REF-008, REF-009; REF-001 informed a rejection; 5 rejected | HYPOTHESIS | Self-caught a brand mark that accidentally embodied the rejected concept; anti-slop registry loaded late (self-disclosed) |
| 06R ORBIT | Existing B2B product | existing, documented baseline | product-led / modern-minimal | **REDESIGN.** Report ends at §8; no explicit verdict/genericness-check/rule-failures section exists to cite | Triggered — REDESIGN escalates by default | Adopted REF-009 only | NOT DETECTED | Consolidated three competing status-component languages and three radius scales into one system; fixed a measured contrast failure |

---

## 3. Proven Mechanisms

**Project-state detection** — Evidence: correctly identified genuinely-empty in 01–05
and a documented existing baseline in 06R, each confirmed by matching downstream
behavior (full pipeline vs. REDESIGN's Preserved/Refined/Replaced/Removed discipline).
Strength: **Strong**. Limitations: none observed. Decision: **KEEP**.

**BUILD / REDESIGN routing** — Evidence: 06R correctly routed to REDESIGN and
executed the full existing-system-safety sequence (baseline audit reference,
CSS-custom-property-name preservation tied to actual runtime JS dependencies, explicit
Preserved/Refined/Replaced/Removed log). Strength: **Strong**, though single-project.
Limitations: only one REDESIGN case in the benchmark; the "Replace tier" confirmation
path (needing explicit sign-off) was only exercised because the brief itself supplied
the required detail — an easier bar than a REDESIGN brief with less specificity.
Decision: **KEEP**.

**Register / Genre** — Evidence: all six classifications are argued from brief
language against `style-catalog.md`'s own `best_for`/`do_not_use_for` fields, not
defaulted from category reflex (Test 05 explicitly rejects "dashboard → X" default
reasoning; Test 06R explicitly checks genre against `do_not_use_for` rather than
assuming "it's a dashboard"). Strength: **Strong**. Limitations: none observed.
Decision: **KEEP**.

**DESIGN_VARIANCE** — Evidence: assigned and reasoned in all six; the mechanism itself
(Genre sets default → brief moves it → Register caps it) was never violated. But its
Medium-band language produced real ambiguity in two independent rules that consume it
(LAYOUT-007's spacing range, COLOR-001's "visibly move at least one rung" — both
confirmed genuinely underspecified on inspection of the rule text, §7). Strength:
**Moderate**. Limitations: Medium band is well-defined as a *concept* but
under-specified as an *operational threshold* in at least two of its consumers.
Decision: **INVESTIGATE** (narrow textual clarification, not a mechanism redesign).

**Concept Governance (three-state model)** — Evidence: HYPOTHESIS in 01/02/04/05,
NOT DETECTED in 03/06R, zero DETECTED/EVIDENCED outcomes across all six. Every
HYPOTHESIS was disclosed and explicitly kept out of structural decisions; Test 05
self-caught and fixed a brand mark that accidentally rendered its own rejected
hypothesis as decoration. Strength: **Strong** where exercised. Limitations: the
DETECTED/EVIDENCED path — and therefore LAYOUT-009's mandatory translation procedure —
was never activated in this benchmark. That is a coverage gap in the benchmark, not a
finding against the mechanism: nothing here demonstrates LAYOUT-009 works, only that
its gate correctly stayed closed six times. Decision: **KEEP**; flag as untested-by-Phase-7
for a future benchmark brief that actually earns DETECTED/EVIDENCED.

**Visual References (LAYOUT-010)** — Evidence: loaded and reasoned in all six; the
large majority of entries were rejected with a specific, checkable reason each run
(7/9, 7/9, 6/8, 7/9, 6/9, 8/9). REF-009 (segmentation-by-rule) was adopted in **all
six** — the single highest-frequency decision in the whole benchmark. REF-001 was
adopted once (03) and explicitly rejected-but-informing once more (05). Strength:
**Strong** as a discipline mechanism (reject-by-default behavior holds). Limitations:
REF-009's 6/6 adoption rate is exactly the kind of repeated-structural-device pattern
the convergence question (§5) needs to take seriously — the mechanism is working as
specified, but its output is not neutral across projects. Decision: **KEEP** the
mechanism; **monitor** REF-009's adoption rate as a possible new default reflex.

**Anti-Slop** — Evidence: the SLOP-011 gestalt check (checking a finished palette +
type + accent combination as a whole, not atomic rules) caught a real near-miss in 01
(fixed by hue rotation) and was explicitly checked-and-avoided in 03; SLOP-017
(em-dash ban) caught real violations in 03/04/05; SLOP-005 (middle-dot) produced one
reasoned, disclosed exception (05) rather than a silent violation. Strength: **Strong**.
Limitations: SLOP-005's framing (decorative marketing meta-chrome) doesn't cleanly
cover dense operational metadata — a real but narrow ambiguity (§7). Decision: **KEEP**.

**Visual Fingerprint** — Evidence: explicitly N/A in 02 and 05 (first entry, nothing
to compare against); explicitly invoked and correctly exempted in 06R (consistent
macrostructure across one product's own pages is the named legitimate exception, not
a violation). Strength: **Weak-by-construction** — a single-shot benchmark structurally
cannot exercise a cross-session mechanism. Limitations: this benchmark provides no
real evidence the fingerprint check catches anything; it only shows the mechanism
didn't misfire. Decision: **KEEP**; validation will only come from accumulated real
usage, not from Phase 7.

**Existing-System Safety** — Evidence: single project (06R), but deep — CSS
custom-property names preserved specifically because page JS builds inline styles from
`var(--space-*)`/`var(--color-*)` at runtime (a reasoned, not reflexive, preservation
decision), every element `id` JS queries verified unchanged, "Replace tier" invoked
only with the brief's own explicit confirmation. Strength: **Strong**, single-project.
Decision: **KEEP**.

**Level 1 critique** — Evidence: self-caught real defects in all six runs (rendering
bugs, contrast failures, content violations, heading-order breaks, `[hidden]`-cascade
bugs). But Level 1 also *missed* the most severe defect of the whole benchmark (Test
01's JS-dependent hero content) and a CRITICAL focus-trap gap (Test 04) — both caught
only by Level 2. Strength: **Strong** as a floor, by design not a ceiling. Decision:
**KEEP**.

**Level 2 critique** — Evidence: triggered in exactly the cases its own stated
conditions predict (01, 03, 04 — BUILD + genuinely-empty + explicit brand-quality-bar
phrase; 06R — REDESIGN, mandatory) and correctly did not trigger in 02/05, where no
such phrase exists in the brief. Every triggered run produced genuinely new,
previously-unnoticed findings; Test 04 explicitly notes the two dispatched reviewers
"converged on almost nothing in common" yet both found real defects — direct evidence
for the value of orthogonal, dual-blind review rather than a single broader one.
Strength: **Strong**. Decision: **KEEP**.

**Responsive validation** — Evidence: a real, breakpoint-specific bug was found and
fixed in every single test (01: mobile nav overflow; 02: sub-400px nav overflow + grid
overflow; 03: 46–49rem nav-wrap dead zone; 04: mobile hero-cluster overflow; 05: mobile
header overflow; 06R: Invoices had no mobile fallback at all). Every report states
these were invisible from source and only found by actually rendering at real
viewport widths. Strength: **Strong**. Decision: **KEEP**.

**Accessibility validation** — Evidence: contrast failures found and fixed in four of
six (01, 02, 04, 06R — see the recurring pattern in §4.2); focus-trap/management gaps
found in three of six (01, 04, 06R baseline-inherited). All measurements were computed
(OKLCH→sRGB/WCAG luminance scripts, live keyboard automation), not estimated. Strength:
**Strong**, with one consistent, honestly-disclosed limitation: no automated
axe-core/Lighthouse run occurred in any of the six tests. Decision: **KEEP** the
current computed-manual approach; **INVESTIGATE** whether an automated tool should
supplement it (not replace it — the manual computation caught things a generic tool
might not phrase as clearly, e.g. hue-distance collisions).

---

## 4. Recurring Cross-Project Findings

### 4.1 Validated strengths
- Rendered-browser validation catches real, source-invisible bugs — 6/6.
- Level 2 dual-blind critique catches genuinely new defects whenever it runs — 4/4
  triggered runs.
- Visual References produces reject-more-than-adopt behavior with stated reasons — 6/6.
- Concept governance prevents forced metaphor with zero false positives — 6/6.
- Zero fabricated content (stats, testimonials, credentials, certifications) — 6/6,
  a hard brief constraint that held under audit in every test.
- The SLOP-011 gestalt check (combination, not atomic) catches what individual rules
  miss — demonstrated concretely in 01, checked-and-avoided in 03.

### 4.2 Recurring quality risks
- **A "faint/muted" neutral text token undershoots WCAG 4.5:1** — 4/6 (01: `ink-faint`
  3.89:1 and `line-strong` 2.26:1; 02: `ink-faint` 4.31:1; 04: `ink-faint` 3.61:1 and
  two status-badge colors 3.77:1; 06R: `text-muted` 3.0–3.3:1). Same failure shape,
  four independent sessions, four different palettes. This is the strongest recurring
  quality-risk pattern in the benchmark.
- **Focus-management gaps on off-canvas/modal surfaces** — 3/6 (01: background
  `<main>` not marked `inert` during mobile-nav overlay; 04: CRITICAL — mobile filter
  dialog had zero focus management; 06R: baseline had no modal focus trap, fixed
  during redesign). 05 self-caught and fixed the equivalent bug pre-emptively during
  its own VALIDATE pass, which is worth reading as the same underlying risk shape
  caught one step earlier.
- **SLOP-017 (em-dash as clause separator) appears in generated sample/body copy** —
  3/6 (03, 04, 05), despite being an absolute-ban rule with no "sparingly" exception.
  Suggests a default prose habit independent of design-system discipline.
- **No automated axe-core/Lighthouse tooling used** — 6/6, consistently disclosed as
  a remaining risk rather than silently assumed clean.

### 4.3 Rule ambiguities
- **MOTION-004 vs. MOTION-007** — recurred independently in 3/6 (01, 03, 06R), each
  time resolved identically (color/border-color hover transitions judged paint-only,
  outside MOTION-004's stated harm, kept as a disclosed exception). Three independent
  sessions reaching the same interpretation independently is unusually strong
  convergent evidence of a genuine textual gap (§7).
- **LAYOUT-007's Medium-band spacing range is undefined** relative to Low/High — 1/6
  explicit (01), single-project observation, confirmed on inspection of the rule text.
- **COLOR-001's Medium-band "visibly move at least one rung"** has no mechanical test
  — 1/6 explicit (02), single-project observation, also confirmed on inspection.
- **No mechanical check for a new token colliding (by hue) with an already-committed
  one** — 1/6 (04's category-hue-35-vs-accent-32 near-miss), single-project but
  concrete and directly mechanically checkable.
- **SLOP-005 (middle-dot)** framed for decorative marketing meta-chrome, ambiguous for
  dense operational metadata — 1/6 (05), disclosed as a reasoned exception, not a
  violation.

### 4.4 Single-project anomalies
- SVG-as-flex-item zero-width rendering bug (02) — a real browser behavior outside
  the skill's scope.
- A `claude-mem` plugin hook intermittently truncated file reads and redirected
  toward unavailable tools (03) — environment noise; both the main session and the
  independently dispatched critic correctly treated it as untrusted and ignored it.
- A Playwright element-scoped screenshot stitching artifact briefly read as a false
  rendering bug (03) — resolved by a full-viewport screenshot; recorded so it isn't
  mistaken for real on a later pass.
- A stray `ruvector.db` appeared mid-session from a dispatched subagent's own tooling
  (04) — cleaned up, not part of the deliverable.
- Browser-cache false positives on script/CSS errors after file edits (04, 05) —
  resolved by cache-busting or a fresh origin, not real code defects.
- A literal `\n` string leaked into visible markup across all seven pages from a
  scripted multi-file edit (05) — caught only via a mobile screenshot; a tooling-process
  risk (bulk scripted edits vs. per-file edits), not a rule-catalog gap.

---

## 5. Visual Convergence Analysis

### 5.1 Genericness

The clearest, most defensible case of actual genericness is **Test 04 (FORMA)**:
distinctiveness is explicitly front-loaded onto the homepage and category directory,
while Tienda/Producto lean on a conventional sidebar-filter/product-grid vocabulary —
self-disclosed by the builder and independently confirmed by the dispatched
visual-critic ("reads closer to a generic furniture-store template once the logo is
covered"). This is *structural* genericness on interior/utility pages under real
task/commerce pressure (grid-scanning, filter UI), not visual-only.

Two milder, single-project instances are worth naming precisely so they aren't
overweighted: Test 02's audience-row/benefits-grid ("functionally clear but visually
closer to a default pattern... not templated") is plain, not templated — no pills,
gradients, or icon-cards were reached for. Test 05's observation that PULSE's visual
language "would look identical for a different small-service-business vertical" is
**not** genericness under the report's own (correct) reasoning: register/genre
discipline deliberately derives the palette from the product's operational register,
not the business's vertical, which is exactly what SLOP-013 requires. Treating this as
a defect would be a misapplication of the genericness test — worth flagging explicitly
so it is not miscounted in a future pass.

Genericness in this benchmark is domain-linked (commerce interior pages under task
pressure), not evenly distributed across all six tests.

### 5.2 Refined AI convergence

Checking the hypothesis — "even when the skill avoids obvious AI-slop patterns,
several conservative design decisions can combine into a recognizable refined-AI
aesthetic" — against concrete, checkable evidence rather than impression:

- **Palette:** a restrained neutral paper/near-black ink + one muted, desaturated
  accent recurs in 5/6 tests (01 after correction, 02, 03, 04, 05); 06R refines an
  existing navy/blue system toward the same restraint. This specific combination
  (paper/ink/single-muted-accent via OKLCH construction) is the dominant color
  strategy across the whole benchmark.
- **Typography:** the IBM Plex family (Sans or Mono) appears as a chosen face in 3/6
  tests (01: IBM Plex Sans body; 04: IBM Plex Sans body + IBM Plex Mono outlier; 03:
  IBM Plex Mono outlier) — a specific, checkable recurrence, not a vague "feels
  similar" impression. Each was reasoned independently via `TYPE-002`'s voice-word
  procedure, and each session explicitly rejected the more obvious reflex fonts for
  its genre — but the procedure converged on the same family three separate times.
- **Structural device:** REF-009 (rule-segmentation over cards/shadows) was adopted
  in **6/6** tests — the single strongest structural-convergence signal in the
  benchmark (§3, §4.1).
- **Motion:** all six tests, without exception, landed at Low `MOTION_INTENSITY`
  (2–3/10), including the hybrid e-commerce test and the dense operational dashboard —
  domains that could plausibly support more. One orchestrated reveal plus
  state-transition-only feedback is the universal shape.
- **Shadow/radius:** near-zero `box-shadow` and small/near-zero radii are explicit or
  independently-verified in 01 ("zero `box-shadow` anywhere"), 04 (flagged by Level 2
  as broadsheet-adjacent), 05 ("panels carry no shadow"), and consistent with 06R's
  redesign direction.

Two independent, differently-dispatched critic agents named the resemblance to a
recognizable aesthetic **unprompted**, in two unrelated domains: Test 01's reviewer
("cover the MOVA wordmark on the home screenshot and this could plausibly ship for an
architecture studio, a dental practice, or a boutique consultancy") and Test 04's
reviewer (the hairline/near-zero-radius/spec-sheet idiom "sits close enough to a
recognizable current AI-agent-commerce vocabulary" to flag). This is genuine,
specific evidence — the combination recurs across genuinely unrelated domains (a
clinic, a SaaS product, an editorial magazine, a furniture store, an ops tool), not
just within one register/genre pairing.

### 5.3 Appropriate convention

Several of the same-looking decisions are correctly domain-driven, not convergence:
Register correctly capping product-led work (02, 05) at Restrained/Committed color
tiers is the mechanism working as designed — a genuinely High-variance SaaS dashboard
would fight its own usability requirements. Low motion in dense operational UI (05)
and reading-first editorial (03) is explicitly brief-mandated in both cases, not a
default. Existing-system preservation in 06R (kept navy sidebar, kept blue family,
kept stack) is REDESIGN discipline, correctly not counted as a fresh aesthetic choice.

Critically: **avoiding card grids is an explicit instruction in nearly every one of
the six briefs** ("no repetitive card grids," "not the default hero+3cards+grid,"
"avoid decorative dashboard cards"). REF-009's 6/6 adoption rate is therefore
substantially a correct, repeated response to a repeated *input* instruction, not
purely an unprompted skill bias — this is the single most important caveat on the
convergence hypothesis and should not be dropped when interpreting §5.2's evidence.

Where the evidence becomes less defensible as functional convention: the *palette
strategy* (restrained neutral + one muted accent) and the *near-universal Low motion*
are not equally explained by explicit brief instructions — several briefs ask to avoid
specific clichés (gradients, glassmorphism, neon) without mandating restraint as the
only alternative, yet every test converged on restraint anyway. That gap between
"brief bans X" and "skill consistently produces the same non-X" is the part of the
evidence that most plausibly reflects the skill's own bias rather than the brief's
instruction.

### 5.4 Current conclusion

**Evidence worth monitoring.** The pattern is real, specific, and independently
noticed by two separate critic agents in two unrelated domains — not "insufficient
evidence." It falls short of "clear recurring convergence" for three concrete reasons:
(1) several of the recurring decisions are directly explained by explicit,
repeated brief instructions rather than an unprompted skill default; (2) the sample is
six tests from one benchmark author, whose brief-writing conventions (Spanish-language
copy, explicit "avoid generic AI [X]" instructions, similar structural bans) are
themselves a confound not separated from skill behavior; (3) no controlled comparison
exists — no test in this set omits the anti-genericness instruction, and none clearly
calls for High variance or High motion, so the benchmark cannot currently distinguish
"the skill converges regardless of brief" from "these six briefs converge, and the
skill correctly followed them."

Per the instructions governing this analysis: **do not propose a new Anti-Slop rule**
on this evidence. The more defensible next steps are broader exploration and reference
diversity (already a live mechanism, §3), and — concretely — a future benchmark test
whose brief does not contain an explicit anti-genericness instruction and one that
plausibly calls for High variance/motion, to separate brief-bias from skill-bias
before drawing a stronger conclusion (§10, §11).

---

## 6. Critique & Validation Analysis

**What Level 1 caught, alone:** rendering bugs invisible from source (image-placeholder
collapse via inline-element `display`, SVG-as-flex-item zero-width, `[hidden]`-cascade
overrides), contrast failures on primary/secondary text pairs, content-copy anti-slop
violations (em-dashes, middle-dots), heading-hierarchy breaks, typography-discipline
slips (an outlier face bleeding into unrelated roles), and one literal string-leak bug.
Every one of these was found through actual rendered-browser measurement, not a
source-only read — repeatedly stated across reports as something a code-only review
would have missed.

**What Level 2 caught that Level 1 did not:** the single most severe defect in the
whole benchmark (Test 01 — primary content and the mobile nav toggle both invisible
and inert without JavaScript, no `<noscript>` fallback); a CRITICAL zero-focus-management
modal dialog (Test 04); an invalid interactive-in-interactive HTML content model —
a button nested inside an anchor (Test 04); an under-committed accent color relative
to the project's own stated design intent (Test 03); and, in Test 01, a second-order
finding where fixing Level 2's own first finding (footer contrast) introduced a new,
different Level 2-caught regression (a placeholder-signal loss) — a concrete
demonstration of why the protocol insists on genuinely isolated, differently-focused
reviewers rather than one reviewer trying to hold every concern at once.

**Did Level 2 add meaningful value?** Yes, unambiguously, in every triggered run.
Test 04 states it plainly: the two dispatched reviewers "converged on almost nothing
in common" (as expected from orthogonal rubrics) yet both independently surfaced real,
previously-unnoticed defects.

**Were its trigger conditions appropriate?** Yes. It fired in 01/03/04 (BUILD +
genuinely-empty + multi-page-site + an explicit brand-quality-bar phrase in the brief)
and in 06R (REDESIGN, which escalates by default) — and it correctly did *not* fire in
02/05, where the brief asks for "production-quality" without the elevated phrase the
trigger requires. This is discriminating behavior, not over- or under-firing.

**Recurring critique gaps, by axis:**
- **JS-independent content visibility** — not named by any rule-catalog file; caught
  exactly once (Test 01), by a Level 2 reviewer manually tracing the JS dependency
  chain, not by any mechanical check. See §7.
- **Responsive issues** — caught consistently by both levels across all six tests
  (§4.1); no gap here.
- **Focus management** — caught in 3/6 by Level 2/VALIDATE (§4.2); one instance (05)
  self-caught pre-emptively — evidence the pattern is learnable but not yet reliably
  caught at Level 1 across the board.
- **Keyboard accessibility, contrast** — consistently caught and fixed, always via
  computed/measured verification, never assumed (§3).
- **Nested interactive elements** — caught once (04), by Level 2 specifically, not by
  Level 1's own craft-correctness axis.
- **Mobile behavior** — consistently caught by both levels; no gap.
- **Visual hierarchy** — consistently 4–5/5 at Level 1, cross-checked by the squint
  test; no gap surfaced.
- **Brand quality / distinctiveness** — this is where Level 2 earned its keep most
  visibly: three of four triggered runs produced a genericness- or
  distinctiveness-adjacent finding (01's palette, 03's under-committed accent, 04's
  homepage/interior gap) that Level 1's own gestalt-check instruction should have, but
  did not, catch as decisively.
- **Repeated-axis failures** — the contrast-on-faint-token pattern (§4.2) is the
  clearest repeated-axis failure across sessions; worth a rule-catalog look (§7)
  rather than a new critique-protocol rule.

---

## 7. Rule-Catalog Findings

### Motion: MOTION-004 vs. MOTION-007
**Evidence:** `MOTION-004` states an unconditional allowlist (animate only
`transform`/`opacity`/`clip-path`; anything else is a performance finding), justified
entirely by layout-thrash/jank harm. `MOTION-007` (`prefers-reduced-motion`)
explicitly presupposes color/opacity transitions are a legitimate, kept category. Three
independent sessions (01, 03, 06R) each hit this with paint-only `color`/`border-color`/
`background-color` hover transitions, and each independently reached the identical
resolution: judged out of scope of MOTION-004's *stated* harm, kept as a disclosed
exception. **Severity:** low functional impact (every resolution was reasonable and
consistent) but a real textual gap. **Scope:** any build using conventional
color-transition hover states — i.e., nearly all of them. **Confidence:** high — three
independently staffed sessions converging on the same interpretation, unprompted, is
unusually strong evidence this is a genuine spec gap rather than a misreading.
**Recommended action:** narrow MOTION-004's scope explicitly to layout-affecting
properties, or state the paint-only color/border/background exception directly in its
own text rather than leaving it recoverable only by cross-referencing MOTION-007.
Not implemented here, per instructions.

### Progressive enhancement (MOVA finding)
**Evidence:** Test 01's most severe defect — hero content and the mobile nav toggle
both invisible/inert without JavaScript, with no `<noscript>` fallback — was not caught
by any rule in `accessibility.md`'s P1 list or elsewhere in the rule catalog; only a
Level 2 reviewer manually tracing the JS-reveal chain caught it. **Severity:** high —
a CRITICAL production defect that passed Level 1, mechanical VALIDATE, and the
builder's own judgment. **Scope:** single-project finding, but the causal shape
(opacity-0-by-default + JS-only reveal class) is a common pattern in exactly the kind
of load/scroll-reveal motion this skill's brand-led builds reach for, so it reads as a
plausible, addressable gap rather than a MOVA-specific fluke. **Confidence:**
moderate-high on severity and specificity, single-project on frequency. **Recommended
action:** a candidate rule ("critical content must render visible by default in CSS;
JavaScript may only add a hidden state it also guarantees removing") for the
accessibility/technical-correctness category — analysis only, not implemented.

### Color collision (FORMA finding)
**Evidence:** a category-coding palette introduced during DIRECT/DESIGN landed 3° hue
from the already-committed brand accent, contradicting the project's own
`.design/context.md` separation claim; caught by Level 2, not Level 1. **Severity:**
moderate — narrow but real, a specific interaction between COLOR-001/COLOR-004 and a
secondary token system layered on later in the same pass. **Scope:** relevant whenever
a project adds a second color-coding system (category, status) after committing a
brand accent — plausible in dashboard- and e-commerce-shaped builds specifically.
**Confidence:** single-project, but mechanically concrete (hue distance is directly
computable). **Recommended action:** a candidate mechanical check ("new tokens must
clear a minimum hue distance from every already-committed token") added to
COLOR-001/004's `validation` field — analysis only.

### DESIGN_VARIANCE Medium-band operationalization
**Evidence:** two independent rules that consume the Medium band (LAYOUT-007's spacing
range, COLOR-001's "visibly move at least one rung") were confirmed on inspection to
be genuinely underspecified relative to their own Low/High bands, surfaced in two
different tests (01, 02). **Severity:** low-moderate — no test produced a wrong or
broken outcome; each session made a reasonable, disclosed judgment call. **Scope:**
potentially every Medium-declared project (4/6 tests in this benchmark used Medium or
Medium-adjacent bands). **Confidence:** moderate — two independent rules, two
independent tests, same underlying pattern (Medium defined as "between the two" without
either endpoint being numerically anchored). **Recommended action:** either give
Medium-band rules an explicit numeric anchor or label them explicitly as
judgment-call/not-mechanically-verifiable rather than leaving the gap implicit —
analysis only.

---

## 8. Domain-Specific Findings

**Local/professional service — MOVA:** homepage/inner-page identity mostly holds (five
genuinely distinct macrostructures per LAYOUT-001), but the independent critic's own
words ("could plausibly ship for an architecture studio, a dental practice, or a
boutique consultancy") show the convergence risk (§5) is strongest in exactly this
register — trust-building local-service content pulls hardest toward calm-palette +
minimal-shadow restraint.

**SaaS — Signal:** Register correctly suppressed high variance (Restrained/Committed
ceiling, 2-family type cap, fixed rem scale over fluid clamp) — the mechanism working
as designed, not a limitation. The mildly generic sections (audience row, benefits
grid) are a domain-linked outcome — a marketing "who we serve" section has structurally
few distinctive options — more than a skill defect.

**Editorial — NORTE:** genre-appropriate density/motion suppression is explicitly
brief-driven (motion "must not be added merely because the page is editorial"), not a
default. The reading-view density exception (Low-band spacing overriding the
site-wide Medium-High default) is a clean example of a correctly evidence-based dial
override rather than a blanket application.

**E-commerce — FORMA:** the clearest domain-tension case in the benchmark. Commerce
efficiency (consistent, scannable grids and filter conventions) legitimately competes
with, and partially defeats, distinctiveness on interior pages — self-disclosed and
independently confirmed, and explicitly framed in the report as a legitimate trade-off,
not a failure. Treat this as the benchmark's primary evidence for where functional
convention properly bounds distinctiveness ambition (§5.3).

**Dashboard — PULSE:** high density solved through hierarchy, not shrinking — a clean
validated application of LAYOUT-007's High band together with REF-008/REF-009. The
vertical-neutral palette is explicitly reasoned as *correct* under SLOP-013 (register-
derived, not vertical-derived), not a shortfall — an important precedent against
misreading register-correct neutrality as genericness in future dashboard/product-UI
tests (§5.1).

**Existing-product redesign — ORBIT:** the only test exercising Existing-System Safety
end-to-end; behaved correctly, including the reasoning tying CSS-variable-name
preservation to actual runtime JS dependencies rather than blanket caution. Notably the
only report of the six missing its closing sections (Genericness Check, Unexpected
Behavior, Rule Failures, an explicit Verdict) — this narrows what can be claimed about
06R specifically in this analysis (marked "not stated" in the Matrix rather than
inferred) and should be treated as a reporting completeness gap to close before this
run is cited as full evidence in a future pass.

---

## 9. What We Should NOT Change

Frozen unless materially stronger evidence appears:

- **Routing architecture** (project-state detection, BUILD/REDESIGN split) — 6/6
  correct, no ambiguity surfaced.
- **Concept Governance** (three-state model, LAYOUT-009's gating) — 6/6 correct
  resolution, zero false positives; the DETECTED/EVIDENCED path is untested, not
  broken.
- **Visual References architecture** (LAYOUT-010, Observe→Abstract→Adapt, the priority
  order) — reject-by-default discipline held in every test; REF-009's adoption rate is
  a signal to monitor, not evidence the selection mechanism itself misbehaved.
- **Anti-Slop registry** — caught real, near-miss and outright violations across
  multiple tests; no false positive or false negative surfaced.
- **Visual Fingerprint** — unexercised by this benchmark's single-shot structure, not
  disproven.
- **Existing-System Safety** — the one REDESIGN test it ran on behaved correctly and
  carefully.
- **Level 1 / Level 2 critique architecture**, including the trigger conditions —
  discriminated correctly across all six tests; do not lower the bar or make Level 2
  default-on.
- **Register / Genre** and **DESIGN_VARIANCE** as mechanisms (as opposed to specific
  Medium-band rule text, §7) — no misclassification observed in six tests.
- **LAYOUT-009**, **LAYOUT-010** — see above; both behaved exactly as specified.

**Explicitly: do not add another broad Anti-Slop rule solely to fight the
refined-AI-convergence hypothesis.** The evidence in §5 supports monitoring and a
controlled follow-up benchmark, not a new rule — several of the recurring decisions
trace directly to repeated, explicit brief instructions rather than to an unforced
skill default, and a new rule risks penalizing correct behavior to chase a pattern
that isn't yet isolated from its confound.

---

## 10. Phase 8 Candidate Interventions

### A. Reicon (default iconography system)
**Why it belongs:** every test hand-built its own icons ad hoc, and a meaningful share
of the accessibility findings across this benchmark were icon-related (aria-hidden on
decorative SVGs, aria-label on icon-only buttons, ORBIT's `✕`-glyph → SVG swap for
reliable AT exposure). A shared default system could structurally prevent a class of
small, repeated defect rather than relying on VALIDATE to catch each instance per
project. **Risks:** must not override an existing project's icon language — ORBIT
explicitly preserved its existing stroke language, and Reicon must yield to that kind
of instruction, not compete with it. **Interaction with explicit user instructions:**
subordinate — brief/existing-system instructions win. **Progressive disclosure:** load
only when a project needs new iconography, never bundled by default.

### B. Kinetics (motion and microinteraction repertoire)
**Why it's relevant:** motion was Low in 6/6 tests, including domains that could
plausibly support more (§5.2) — this is exactly the situation where importing a richer
motion vocabulary carries real convergence risk if it becomes a new default reach
rather than something genuinely calibrated per project. **How it should stay a
repertoire:** it must remain strictly gated by `MOTION_INTENSITY`'s existing dial
mechanism (§3) — the same discipline that currently keeps motion Low where the brief
calls for Low must keep Kinetics from becoming the default answer once it exists.
**Risk of importing aesthetic behavior indiscriminately:** high if ungated, given the
near-universal Low-motion baseline this benchmark demonstrates — a repertoire that
looks appealing in isolation could become the new reflex the same way REF-009 already
shows a single structural device can dominate adoption.

### C. SmoothUI (optional component implementation source)
**Why it's useful:** every test hand-built its own component layer from scratch (rule-
segmented lists, filter chips, modal dialogs, card systems) — real, repeated
engineering cost visible across all six reports. **Why it must not become the design
system:** REF-009's 6/6 adoption rate already demonstrates a structural-pattern
convergence risk; layering a shared component-implementation source on top without
discipline could accelerate visual sameness rather than reduce engineering cost
without cost. **How it should coexist:** as an implementation shortcut for a
brief-derived pattern already decided by DIRECT, never a substitute for deciding the
pattern. **Progressive disclosure:** load only when scope genuinely calls for a
component library — never silently substituted for a custom, brief-derived pattern.

### D. Targeted rule corrections
Recommended before integrations, not after: the MOTION-004/MOTION-007 text
clarification (§7) and a JS-independent-content-visibility rule candidate (§7) are
both concrete, convergent (the motion one recurred independently three times), and
low-risk to state more precisely. Both are directly relevant to Kinetics, which will
generate more motion/interaction code subject to exactly these ambiguities — fixing
the rule text first is cheaper than carrying the ambiguity into three new integration
surfaces. The COLOR-001/004 token-collision check (§7) is a reasonable third candidate
but lower urgency (single-project evidence, narrower scope).

Not implemented here, per instructions — this section is evaluation only.

---

## 11. Phase 8 Decision Gate

**OPTION B: TARGETED CORRECTIONS BEFORE INTEGRATIONS.**

The architecture itself — routing, Concept Governance, Visual References, Anti-Slop,
critique escalation — produced no failures across six genuinely different domains
(§3, §9), which rules out Option C: nothing in this evidence suggests a structural
problem serious enough to warrant an architecture correction, and doing one anyway
would be exactly the benchmark-driven overfitting this analysis is instructed to guard
against.

Option A (proceed straight to integrations) is not the strongest choice because two
concrete, convergent, narrowly-scoped gaps exist and are directly relevant to the next
phase: the MOTION-004/007 tension recurred independently in three of six sessions with
identical resolutions (strong convergent evidence, not noise), and the
JS-content-visibility gap produced the single most severe defect in the entire
benchmark. Both sit exactly in the surface area Kinetics and SmoothUI are about to
expand — carrying them forward unaddressed means the next phase generates more code
subject to the same known ambiguities before they're fixed. Fixing rule *text*, not
architecture, is a small, low-risk, targeted change, which is why this is Option B and
not Option C.

---

## 12. Phase 7 Final Decision

**Status:** Phase 7 passed. Five of six runs recorded PASS or PASS WITH RISKS with
full evidence; the sixth (06R/ORBIT) is a strong redesign whose own report is
incomplete past §8 — treat its findings as directionally trustworthy but its coverage
as thinner than the other five until a completed report exists.

**What is frozen:** routing architecture, Concept Governance (including LAYOUT-009's
gating), Visual References architecture (including LAYOUT-010's priority order),
Anti-Slop registry, Visual Fingerprint, Existing-System Safety, Level 1/Level 2
critique architecture and trigger conditions, Register/Genre, and the DESIGN_VARIANCE
mechanism itself.

**What remains under observation:** the refined-AI-convergence hypothesis
(palette + type + motion + REF-009 combination, §5) — real and specific, but confounded
by this benchmark's own brief-writing conventions and not yet separated from a
legitimate, repeated brief instruction to avoid card grids and category clichés;
REF-009's 6/6 adoption rate specifically; the recurring faint-text-contrast failure
pattern (§4.2); and e-commerce-style interior-page genericness under task pressure
(§5.1, §8).

**What should happen next:** a targeted correction pass on MOTION-004/007's text and
a JS-independent-content-visibility rule candidate (§7, §10D) — analysis only in this
document, implementation is a separate future step — followed by Reicon/Kinetics/
SmoothUI integration, each gated by progressive disclosure and by the existing dial
mechanisms (register/genre/MOTION_INTENSITY) exactly as strictly as current rules are
gated. A future benchmark test whose brief omits the explicit anti-genericness
instruction, and one that plausibly calls for High variance or High motion, would
meaningfully advance the convergence question beyond "worth monitoring."

**What must NOT happen next:** do not add a new broad Anti-Slop rule to fight the
convergence hypothesis (§5.4, §9); do not weaken Visual References' reject-by-default
discipline in the name of "more distinctiveness"; do not let Reicon, Kinetics, or
SmoothUI become defaults that override an explicit brief or existing-system
instruction; do not treat 06R's incomplete report structure as evidence of weaker work
without first getting a completed report; do not open a new phase or stage beyond the
targeted corrections and integrations named above.
