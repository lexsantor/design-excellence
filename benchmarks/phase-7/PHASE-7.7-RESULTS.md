# Phase 7.7 — Runtime Invocation Benchmark

## 1. Objective

Phase 7.6 validated the documented architecture (NEED → DESIGN DECISION → IMPLEMENTATION SOURCE) by manually walking the pipeline. This phase tests whether a **real `/design-excellence` invocation**, executed blind by an agent with no knowledge that it was being benchmarked, produces the same class of decisions — and specifically whether Reicon, Kinetics, and SmoothUI (T4 implementation sources) ever drove design demand rather than merely implementing demand that already existed.

## 2. Runtime Environment

- **Test project:** `%TEMP%\claude\...\scratchpad\orbit-benchmark\` — created empty and verified empty (`ls -la`, zero entries) immediately before the run, outside this repository entirely, so no artifact from this repo (Anti-Slop registry, prior benchmark output, this skill's own history) could contaminate it and nothing needed to be created inside `benchmarks/phase-7/` except this results file.
- **Invoking agent:** a fresh `general-purpose` subagent, **not a fork**. This was a deliberate methodology choice: the orchestrating session (me) had already read the full adversarial brief, the pressure-point analysis, and Failure Modes A–J before this phase started. A fork would have inherited that awareness and could not have produced a blind run. The subagent was given only the product brief and the instruction to use the `design-excellence` skill — no mention of components, icons, motion, concept-detection, or that this was a benchmark at all.
- **Tools available to the subagent:** general-purpose tool access, including the `Skill` tool and (per its own report) a Playwright/Chromium browser-rendering tool, which it used for real rendered validation (contrast computation, keyboard-focus verification, no-JS baseline, `prefers-reduced-motion` emulation) rather than static inspection alone.

## 3. Invocation

The subagent was instructed to invoke the skill by name (`Skill` tool, `skill: "design-excellence"`) against the project directory above, and was given exactly this brief, verbatim, with nothing else:

> **Product: "ORBIT"** — a premium B2B platform for professional-services teams coordinating client work, approvals, documents, and project milestones. Audience: professional-services teams managing multiple active client engagements. Positioning: calm, precise, operational, trustworthy.
> **Page:** navigation, hero, product explanation, workflow section, benefits, trust/credibility section, final CTA, footer.

No pressure-point framing, no hint about the four failure categories, and no instruction about icons/motion/concept was included — those were left for the runtime to discover or not discover on its own, per §4 of the benchmark spec.

## 4. Runtime Classification

Declared verbatim by the runtime (both required one-liners, per `SKILL.md` §2 and §4):

> "Reading this as: **page BUILD on a genuinely-empty project.**"
> "Reading this as: **hybrid-led modern-minimal work, variance=Medium(5), motion=Low(3), density=Medium(5).**"

Project-state was verified, not assumed — the runtime ran `ls -la` on the target directory before trusting the prompt's "empty" framing.

## 5. Runtime Design Direction

| Axis | Value | Traceable to |
|---|---|---|
| Register | Hybrid | Product mechanics (product-led) + brief's brand-trust language for a considered B2B purchase (brand-led) — neither alone fits |
| Genre | Modern-minimal | Brief's own words "calm, precise, operational, trustworthy" weighed as restraint/precision language, then cross-checked against `style-catalog.md`'s modern-minimal `best_for`/`do_not_use_for` fields before committing |
| DESIGN_VARIANCE | Medium (5) | Genre default is Low–Medium; moved up one rung per `COLOR-001`'s Medium-band rule, justified by "premium" positioning needing to avoid reading as a commodity dashboard |
| MOTION_INTENSITY | Low (3) | Direct textual evidence ("calm, precise, operational") against expressive motion |
| VISUAL_DENSITY | Medium (5) | Real informational content (workflow/benefits/trust) needs room, but this isn't a dense dashboard |

The runtime explicitly documented that it rejected the "B2B SaaS → modern-minimal" **category reflex** in favor of weighing the brief's actual language first, then cross-checking — the exact discipline the Phase 6 correction to §4 requires ("Genre must be evidence-traceable, not a category default").

## 6. Concept Governance

**Outcome declared: HYPOTHESIS** (not DETECTED/EVIDENCED, not NOT DETECTED).

Reasoning recorded in `.design/context.md`: the brief supplies "ORBIT" with no naming rationale, no repeated orbital/circular reference, and no instruction to use it structurally — failing the bright-line "point at the sentence" test, so DETECTED was correctly ruled out. The runtime then supplied its own real, checkable association (an orbit is a stable, predictable path around a center, echoing "precise"/"operational") and logged that explicitly as a HYPOTHESIS, not conflating it with detected evidence.

**Consequence, as applied:**
- LAYOUT-009's mandatory structural-translation requirement did **not** activate (correct — it's HYPOTHESIS, not DETECTED).
- Macrostructure is a single-column, tonal-band flow ("Operational Ledger") — no radial layout, no circular composition.
- Motion is a single vertical staggered reveal — no orbital/rotational motion.
- The HYPOTHESIS did inform one **rejected** candidate (Candidate B, "Coordinated Field" — a recurring geometric orbit-evoking line motif), explicitly rejected in `.design/context.md` because "building a decorative visual theme on an unearned association risks exactly the kind of arbitrary, unearned ornament LAYOUT-009's evidence base warns about."
- The HYPOTHESIS also licensed one thing that **did** ship in the committed direction: a minimal line-drawn logomark — a ring with a single orbiting node — used in the nav and footer. Verified directly in `index.html`: `<circle cx="12" cy="12" r="8.5".../><circle cx="19.2" cy="8.4" r="1.6".../>`, appearing exactly twice (nav, footer), never as a repeated page motif.

This last point is a genuine boundary case and is treated as such in §12 (Failure H) rather than being waved through.

## 7. Component Behaviour

Componentized (all justified by Principle 11's 3+-uses-same-intent rule, decided during SHAPE, **before** `smoothui.md` was read — see §14): `.btn-primary`/`.btn-ghost`/`.btn-link` (nav/hero/final-CTA), `.nav-link` (4), `.section-head` (4), `.capability-item` (3), `.workflow-step` (4), `.benefit-card` (4), `.trust-point` (3).

Deliberately left as one-offs: the "Engagement Snapshot" hero data-card module, the final CTA band (only section using the ink-background exception), and the footer. Verified directly against `index.html`: the `.snapshot` class and its markup appear exactly once — the runtime did not abstract a single-use structural centerpiece into a reusable component despite a component library (SmoothUI) being available as a T4 reference.

## 8. Reicon Behaviour

- `reicon.md` was read 14th in the runtime's own ordered file list — after `layout-interaction.md` (7th, where `LAYOUT-008`'s imagery procedure ran) and after the Imagery Decision was recorded in `.design/context.md`. The runtime's own account: "icon need was established via LAYOUT-008 ... and recorded in context.md *before* reicon.md was opened at all."
- Final count: **6 functional icons** (3 product-explanation, 3 trust/credibility), independently verified in `index.html` (inline `<svg>` elements, each `aria-hidden="true"`, consistent stroke language).
- The benefits section — which also has repeated cards and would be an obvious place to pad icon count if Reicon's availability were driving demand — deliberately shipped with **no icons**, with the stated reason that a 4th icon set on the page and that section's outcome-framed copy made icons "decoration reaching for a slot" there.
- Reicon itself was not operationalized as an actual dependency: `reicon.md` defers to "Reicon's own documentation at BUILD time" for sourcing specifics, which the runtime had no way to fetch/verify for a static, zero-build page — so it hand-authored the SVG set to the same governance standard (role-justified, non-decorative, coherent stroke language) instead of fabricating an unverifiable integration. This is disclosed by the runtime itself as a judgment call, not silently substituted. See the Reicon/Kinetics/SmoothUI environment caveat in §16.

## 9. Kinetics Behaviour

- `MOTION_INTENSITY` was set to Low(3) at DEFINE, before any reference file was read.
- `motion.md` was read 10th — before `kinetics.md` (15th) — and is where the "what moves" decision (`MOTION-002`/`MOTION-003`) was actually made and recorded.
- `kinetics.md` was read only to check for a better implementation pattern; per the runtime's account, its own checklist question ("is a plain CSS transition sufficient?") returned yes, so the shipped motion is hand-written CSS/JS, not an adopted library pattern.
- Final artifact, independently verified in `styles.css`/`script.js`: **exactly one** motion moment — a staggered `IntersectionObserver`-driven reveal on the four workflow steps, with a synchronous non-JS baseline, a `prefers-reduced-motion` branch that reveals immediately, and a hard 1800ms safety timeout so content can never be permanently stranded. No hero entrance animation, no parallax, no scattered fade-ins — the CSS itself carries a comment explicitly declining hero-snapshot entrance motion because `MOTION-003` "restricts decorative motion to one orchestrated moment per page."
- **Discrepancy found:** the runtime's own `RUNTIME-TRACE.md`/`context.md` self-report describes "one orchestrated hero entrance, **and** one orchestrated sequential reveal on the workflow steps" — i.e., two motion moments. The shipped code has only one. This is documented precisely in §16; it does not indicate Kinetics inflated motion (the actual artifact is *more* restrained than the self-report claims, not less), but it is evidence that the self-report is not fully reliable and independent artifact verification was necessary.

## 10. SmoothUI Behaviour

- `smoothui.md` was read last of the three T4 files (16th), after component decisions were, per the runtime's account, "already settled from SHAPE/Principle 11."
- No component was invented to justify using a ready-made pattern: the three genuinely-repeated structures (buttons, section heads, the three card-grid patterns) were componentized; the three genuinely-singular structures (snapshot module, CTA band, footer) were not, matching Principle 11 exactly.
- No actual SmoothUI package was installed or referenced in the shipped code (static HTML/CSS/JS, no build step) — same environment caveat as Reicon (§16): SmoothUI was consulted as governance text, not exercised as a real "ready-made implementation" temptation.

## 11. Cross-Integration Behaviour

- The CROSS-1 protection (SmoothUI's protection list extended to cover iconography, per Phase 7.5) was not directly exercisable in this run since SmoothUI never proposed a component in the first place, so there was nothing for it to bundle icons/motion into. No contradiction observed.
- No evidence of any T4 source altering an upstream decision already made (Register/Genre/dials/macrostructure were fixed well before any T4 file was opened, per the file-read ordering in §6/§8/§9/§10, and none of the three T4 files were read more than once).
- Real self-correction was observed at VALIDATE, independent of any T4 source: a JS-gated workflow reveal with no visible fallback was caught by rendering the page and fixed to have a visible-by-default baseline — the exact `A11Y-009` failure shape, caught by the pipeline's own rendered-validation discipline rather than asserted as passing.

## 12. Runtime Failure Modes

| # | Failure | Verdict | Evidence |
|---|---|---|---|
| A | Reicon consulted before icon need established | **PASS** | File-read order: `layout-interaction.md` (7th) → Imagery Decision recorded in `context.md` → `reicon.md` (14th). Ordering is self-reported (see §16 limitation), but corroborated by the content of `context.md`'s Imagery Decision section, which reasons through `LAYOUT-008` with no reference to Reicon. |
| B | Reicon causes additional icons to appear after activation | **PASS** | Final count is 6, with the benefits section explicitly denied icons post-hoc ("reaching for a slot") rather than icons being added everywhere a slot existed. Verified directly in `index.html`. |
| C | Kinetics causes motion to appear because a pattern is available | **PASS** | `MOTION_INTENSITY` and "what moves" were both decided (DEFINE, then `motion.md`) before `kinetics.md` was opened; final shipped motion (one reveal) is *more* restrained than even the runtime's own self-report claimed. Verified in `styles.css`/`script.js`. |
| D | SmoothUI causes a component to appear because a ready-made implementation exists | **PASS** | Three structurally singular elements (snapshot, CTA band, footer) were not componentized despite SmoothUI being available; verified each appears exactly once in `index.html`. |
| E | SmoothUI causes a one-off to become reusable despite Principle 11 | **PASS** | Same evidence as D — the one-offs stayed one-offs in the shipped artifact, not just in the stated intent. |
| F | SmoothUI bundled icons bypass independent icon justification | **PASS** (environment-limited) | No SmoothUI package was actually integrated — icons are hand-authored inline SVG, so there was no real bundled-icon path to bypass. See §16: this failure mode was not exercised under real pressure in this run. |
| G | SmoothUI bundled motion bypasses motion justification | **PASS** (environment-limited) | Same as F — no real bundled-motion path existed to bypass in a static, zero-build page. |
| H | ORBIT's name causes orbit iconography/motion/radial layout/circular system without DETECTED/EVIDENCED evidence | **FAIL** (narrow) | Macrostructure, motion, and layout all passed cleanly — no radial layout, no orbital motion, no circular compositional system, and a competing candidate that leaned on the orbit hypothesis was explicitly rejected. But the shipped logomark is a literal ring-with-orbiting-node graphic, directly derived from the HYPOTHESIS-level "ORBIT" association and used in nav + footer. The failure statement's literal condition ("orbit iconography... without DETECTED/EVIDENCED concept evidence") is met, even though the instance is minimal, non-repeated, self-aware, and confined to a brand mark rather than a systemic motif. See §18 recommendation. |
| I | Implementation sources alter Register/Genre/dials/Fingerprint after those are established | **PASS** | All three T4 files were read last (14th–16th of 17), well after DEFINE/DIRECT/DESIGN produced Register, Genre, dials, macrostructure, and typography/color systems. No revision of any of those values appears anywhere in `context.md` after that point. |
| J | T4 references loaded speculatively rather than progressively | **PASS** | `gesture-physics.md` and `existing-project-safety.md` were both correctly *not* read (no drag/gesture in scope; project genuinely empty). No stack file was read or fabricated — correct, since an empty project supplies zero real stack evidence. All three T4 implementation-source files were read only after their respective upstream need (icons, motion, components) was already established elsewhere. |

## 13. Documentation vs Runtime

| Observation | Classification |
|---|---|
| Three-state concept model (NOT DETECTED / HYPOTHESIS / DETECTED-EVIDENCED) applied correctly, with a bright-line test cited | DOCUMENTED + RUNTIME CONFIRMED |
| HYPOTHESIS does not activate LAYOUT-009's mandatory structural-translation | DOCUMENTED + RUNTIME CONFIRMED (structural/motion/layout level) |
| Whether a HYPOTHESIS may license a literal iconographic rendering of the name (a logomark) | RUNTIME BEHAVIOUR NOT SPECIFIED BY DOCUMENTATION — `SKILL.md` says a HYPOTHESIS "may still inform ordinary creative exploration," which is broad enough to be read either way; the runtime resolved the ambiguity permissively and shipped a literal orbit-shaped mark |
| Progressive, not speculative, T4 loading (reference read only after the upstream need existed) | DOCUMENTED + RUNTIME CONFIRMED |
| Principle 11 (componentize only at 3+ uses, same intent) | DOCUMENTED + RUNTIME CONFIRMED |
| Genre must be evidence-traceable, not a category default | DOCUMENTED + RUNTIME CONFIRMED (explicit rejection of the "B2B SaaS → modern-minimal" reflex, replaced with brief-language weighing + `style-catalog.md` cross-check) |
| A11Y-009 (no content stranded behind an unfired JS class) | DOCUMENTED + RUNTIME CONFIRMED — and actively enforced: a real violation of this exact shape was introduced in a first draft and caught/fixed at VALIDATE via rendered inspection |
| Mechanical-countable gating tied to rendering-capability availability (Phase 6 correction) | DOCUMENTED + RUNTIME CONFIRMED — the runtime used real Playwright rendering for contrast computation, keyboard-focus order, and orphan/widow checks rather than asserting these from source |
| Behavior when a T4 source's actual package (Reicon/Kinetics/SmoothUI) can't be verified/installed in the current build (no build step, no package manager) | RUNTIME BEHAVIOUR NOT SPECIFIED BY DOCUMENTATION — none of the three reference files say what to do here; the runtime's resolution (hand-author to the same governance standard, disclose as a judgment call) is reasonable but undocumented |
| Self-report accuracy vs shipped artifact | RUNTIME BEHAVIOUR NOT SPECIFIED BY DOCUMENTATION — the skill has no mechanism requiring a process self-report to match the final artifact; one concrete mismatch was found (§9) and only caught because this benchmark independently re-inspected the files |

## 14. Progressive Disclosure

Order actually read, per the runtime's own account, cross-checked against file-modification evidence and against the content of `context.md` (which reflects each stage's output appearing only after its trigger file would have been read):

1. `SKILL.md` (T0, automatic)
2. Target-directory `ls -la` (state verification, not documentation)
3. `Glob` of `references/` (existence check before deciding what to load — not a load itself)
4. `anti-slop-registry.md` (T3 — DIRECT/DESIGN gate)
5. `style-catalog.md` (T3 — same gate, used to cross-check the Genre call)
6. `visual-references.md` (T3 — DIRECT/EXPLORE gate)
7. `rule-catalog/layout-interaction.md` (T2 — category in scope)
8. `rule-catalog/typography.md` (T2)
9. `rule-catalog/color.md` (T2)
10. `rule-catalog/motion.md` (T2 — motion decision made here)
11. `rule-catalog/accessibility.md` (T2)
12. `rule-catalog/content-copy.md` (T2)
13. `rule-catalog/performance-hardening.md` (T2)
14. `reicon.md` (T4 — after icon need established)
15. `kinetics.md` (T4 — after motion need established)
16. `smoothui.md` (T4 — after component need established)
17. `critique-protocol.md` (T2 — CRITIQUE stage)

**Not loaded, correctly:** `existing-project-safety.md` (gated on Project State ≠ genuinely-empty; ruled out at step 2), `gesture-physics.md` (no drag/gesture in scope), any `references/stacks/*.md` (no stack evidence in an empty project — none fabricated).

This ordering is consistent with progressive disclosure as documented in `SKILL.md` §7 — every T4 file's read position sits strictly after the stage that would establish its need, and the two categories correctly excluded (safety file, gesture file) were excluded for the documented reasons, not omitted by accident.

## 15. Visual / Architectural Outcome

Implementation sources remained subordinate to upstream decisions on every axis except one. Register, Genre, dials, macrostructure, typography, and color were all fixed before any T4 file was opened, and stayed fixed afterward. Component and icon inventories were both smaller than what was structurally available to pad (one page section was deliberately denied icons; three structurally distinct elements were deliberately denied componentization). Motion stayed within the single narrative-sequence exception `motion.md` itself allows, and the actual shipped motion was more restrained than the runtime's own description of it.

The one place implementation subordination did not fully hold is the brand logomark: a literal orbit-ring-with-node graphic shipped in the committed direction, traceable directly to a HYPOTHESIS-level (not DETECTED/EVIDENCED) concept association. It is a narrow, contained instance — one non-repeated brand mark, not a systemic motif, and it exists alongside a well-reasoned rejection of a much larger orbit-themed direction — but it is a real instance of NEED (a logomark for a page that needed *a* mark) being satisfied in a way shaped by an unevidenced concept rather than by Register/Genre/dials alone.

## 16. Methodology Limitations

- **Single run.** This is one blind invocation, not a repeated-trials study; it cannot establish how consistently the runtime behaves across seeds/phrasing variants of the same brief.
- **No independently captured tool-call transcript.** The subagent ran as a background task; its process log (file-read order, decision sequencing) is a retrospective self-report written by the same agent after the fact, not a transcript this benchmark captured independently. Ordering claims in §8–§10/§14 are corroborated against the content and timestamps of the artifacts the agent produced, but not against raw tool-call logs.
- **One confirmed self-report inaccuracy.** The runtime's own account of its motion decisions (§9) claimed two motion moments (hero entrance + workflow reveal); the shipped code has only one (workflow reveal — the CSS itself documents that no hero entrance was added, on `MOTION-003` grounds). This does not change the failure-mode verdicts, since the actual artifact is more restrained than claimed, but it demonstrates the self-report alone cannot be trusted without independent artifact inspection — which is why this benchmark read the actual `index.html`/`styles.css`/`script.js` files directly rather than relying on the handback message alone.
- **Reicon/Kinetics/SmoothUI were never operationalized as real dependencies.** The test project has no package manager and no build step (a defensible, evidence-based choice by the runtime, since an empty project supplies no stack evidence per `SKILL.md` §7). All three T4 sources were consulted only as governance text; none contributed an actual pre-built implementation. This makes Failure Modes D–G a weaker test than intended — there was no genuine "ready-made implementation exists" temptation for the runtime to resist, because no ready-made implementation was actually available in this environment. A stronger test of D–G would use a project with these three sources already installed as real dependencies in a buildable stack.
- **No independent re-rendering.** The runtime's accessibility/contrast/keyboard claims (§ "VALIDATE Findings" in its report) are taken on its account; this benchmark did not independently re-run Playwright against the shipped files to reproduce those specific numeric claims (contrast ratios, focus order), though the static HTML/CSS was independently inspected for the structural claims (icon count, component reuse, motion CSS/JS) reported in §7–§10.
- **Single evaluator.** The same session that designed the adversarial brief and pressure points also evaluated the subagent's output. The Failure H verdict in particular required a judgment call (whether a single non-repeated logomark counts as "orbit iconography"); that call is defended with a literal reading of the failure-mode text rather than a lenient one, to avoid the évaluateur's own investment in the skill producing a favorable rubber-stamp result.

## 17. Verdict

**PASS WITH RISKS**

Every structural guard the architecture depends on — Register/Genre/dial fixation before T4 consultation, progressive (not speculative) T4 loading, Principle 11 component discipline, motion staying within its single allowed exception, and the HYPOTHESIS/DETECTED distinction gating structural translation — held under a genuinely blind adversarial run. The one clean FAIL (Failure H) is narrow and low-severity: a single, non-repeated, self-aware logomark, not a systemic orbit motif, and it coexists with an explicit, well-reasoned rejection of a much larger orbit-themed direction. It is real evidence of a genuine specification gap, not evidence of the architecture inverting to IMPLEMENTATION SOURCE → DESIGN DEMAND.

## 18. Recommendations

1. **Close the logomark gap.** `SKILL.md` §1's concept-governance paragraph should state explicitly whether a HYPOTHESIS-level concept may license a literal iconographic rendering of its own idea (a logomark, a single decorative shape) even though it may not license structural translation. The current wording ("may still inform ordinary creative exploration") is exactly what the runtime relied on to justify the orbit-ring mark, and is genuinely ambiguous on this specific case — it is the one place this run actually diverged from the strictest reading of the architecture.
2. **Document the "T4 source can't be verified in this build" case.** None of `reicon.md`, `kinetics.md`, or `smoothui.md` say what to do when their real package/API can't be confirmed inside the current project (no build step, no package manager, or simply unreachable docs). The runtime's own resolution — hand-implement to the same governance standard rather than fabricate an integration — is sound, but it was an undocumented judgment call this time. Stating this explicitly (and requiring it be logged as a Known Exception in `context.md`, which the runtime already does by habit for other judgment calls) would remove the ambiguity for future runs.
3. **Re-test Failure Modes D–G in a stack where the three T4 sources are real installed dependencies.** This run's zero-build static-page environment meant SmoothUI/Reicon/Kinetics were never a genuine "ready-made implementation already exists" temptation — there was nothing pre-built to reach for. A follow-up benchmark using a buildable stack (e.g., a Next.js or Vite project with these three already in `package.json`) would test the actual bundled-component/bundled-icon/bundled-motion bypass risk under real pressure, which this run structurally could not do.
