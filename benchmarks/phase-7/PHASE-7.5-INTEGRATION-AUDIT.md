# Phase 7.5 — Joint Integration Audit

## 1. Scope

Read-only architectural audit of the three Phase 7 implementation-source integrations — Reicon (iconography), Kinetics (motion/microinteraction), SmoothUI (components) — and their interaction with each other and with the governing architecture. No file was modified as part of this audit. The only file created is this report.

**Files inspected (full read):**
- `design-excellence/SKILL.md`
- `design-excellence/references/reicon.md`
- `design-excellence/references/kinetics.md`
- `design-excellence/references/smoothui.md`
- `design-excellence/references/existing-project-safety.md`
- `design-excellence/references/critique-protocol.md`
- `design-excellence/references/gesture-physics.md`
- `design-excellence/references/anti-slop-registry.md`
- `design-excellence/references/style-catalog.md`
- `design-excellence/references/visual-references.md`
- `design-excellence/references/rule-catalog/accessibility.md`
- `design-excellence/references/rule-catalog/motion.md`
- `design-excellence/references/rule-catalog/layout-interaction.md`
- `design-excellence/references/rule-catalog/performance-hardening.md`
- `benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md`
- `benchmarks/phase-7/PHASE-7.1-TARGETED-CORRECTIONS.md`
- `benchmarks/phase-7/PHASE-7.1-INTEGRITY-AUDIT.md`
- `benchmarks/phase-7/PHASE-7.2-REICON-INTEGRATION.md`
- `benchmarks/phase-7/PHASE-7.3-KINETICS-INTEGRATION.md`
- `benchmarks/phase-7/PHASE-7.4-SMOOTHUI-INTEGRATION.md`

**Not read** (out of scope per the audit brief, or non-runtime): `rule-catalog/color.md`, `rule-catalog/typography.md`, `rule-catalog/content-copy.md` — grepped only, to check for cross-references, not read in full, since none of the three integrations claim to touch them. `architecture/ARCHITECTURE.md` and `architecture/FORENSIC-EXTRACTION.md` were not re-read directly; their relevant claims are taken from the three integration reports' own citations, which is a limitation noted in §11.

**Repository state:** clean working tree, `HEAD` at `67ba137` ("feat: integrate SmoothUI as component implementation source"), immediately following the Reicon → Kinetics → SmoothUI integration sequence in that order. No uncommitted changes existed before or after this audit.

## 2. Executive Summary

**The three integrations are architecturally coherent at the single-integration level and largely coherent at the cross-integration level, with one real, evidence-backed gap and several lower-severity consistency issues.** Each file individually does what it claims: it answers *how*, defers *whether* upstream, and states explicit non-activation and precedence rules that route through the existing Authority Hierarchy rather than inventing a parallel one. No new pipeline stage, routing axis, classifier, or scoring mechanism was introduced by any of the three, verified by direct reading, not by trusting the integration reports' own claims.

The audit did not stop at "the documentation says X is forbidden." Two things earn a harder look:

1. **Iconography is the one sub-element not explicitly named as protected from component-bundling bypass.** `smoothui.md`'s "What SmoothUI Must Never Be Used to Justify" list explicitly names "a visual style, density, spacing, color, **or motion decision**" as something SmoothUI's availability can never justify — but does not name iconography. A SmoothUI-implemented component that ships with a bundled icon (a notification card with a bell icon, a nav item with a chevron) has no explicit textual requirement that the icon's presence be independently justified against `reicon.md`'s own Selection/role test before it ships. Motion received this explicit protection; icons did not. This is the most concrete instance of exactly the failure mode §4 of the audit brief calls "one of the most important parts of the audit" ("component exists → icon exists" without the icon's own need ever being separately asked).
2. **The repository already has direct empirical evidence that qualitative, judgment-only gating does not reliably prevent an available-but-optional mechanism from becoming a de facto default.** `visual-references.md`'s REF-009 (segmentation-by-rule) was adopted in 6 of 6 Phase 7 benchmark runs despite being explicitly generative/non-mandatory, gated by the same "considered, then judged unnecessary is a valid outcome" language this skill uses everywhere, including in all three implementation-source files. The Phase 7 cross-project analysis names this as a live risk for Kinetics specifically ("a repertoire that looks appealing in isolation could become the new reflex the same way REF-009 already shows") and for SmoothUI ("REF-009's 6/6 adoption rate already demonstrates a structural-pattern convergence risk"). This is not a hypothetical the audit is inventing — it is a documented, precedented failure mode of the exact governance shape (Activation/Non-Activation prose, "qualitative, not scored" Validation, no mechanical check) all three implementation sources use. None of the three integration reports treat this as resolved; all three residual-risks sections explicitly flag it as unverified in practice.

Neither of these is a **BLOCKER**. The architecture is honest about both: the SmoothUI file's own residual risks name the convergence risk directly, and nothing in any of the three files claims the discipline is mechanically enforced — all three explicitly disclaim scoring and state Validation is qualitative. The gap is real, but it is a known, disclosed, judgment-dependent gap, not a hidden contradiction or a silent architectural violation.

**Verdict: PASS WITH RISKS.** See §14 for the full reasoning.

## 3. Architecture Under Audit

The intended relationship, confirmed present in all three files' opening paragraphs almost verbatim:

```
DESIGN DECISION (brief, SHAPE, motion.md's purpose vocabulary, Principle 11)
      ↓
JUSTIFIED IMPLEMENTATION NEED (icon role established / motion behavior decided / component justified)
      ↓
IMPLEMENTATION SOURCE (Reicon / Kinetics / SmoothUI — "how," never "whether")
      ↓
VALIDATION (qualitative checklist, existing rule-catalog + Anti-Slop, no new scoring)
```

Each file states its own place in this chain in its opening lines:
- `reicon.md:3`: "It answers *how* a required icon gets implemented once an icon is already needed; it never answers *whether* an icon is needed or *what role* it should play."
- `kinetics.md:3`: "It answers *how* an already-decided motion or microinteraction behavior gets implemented; it never answers *whether* the interface should move."
- `smoothui.md:3`: "It answers *how* an already-decided component or interaction pattern gets implemented; it never answers *whether* the interface should have that component."

All three route precedence through `SKILL.md` §3's existing P0–P8 Authority Hierarchy rather than defining a competing one — `kinetics.md` and `smoothui.md` do this explicitly and by name ("Resolved via the existing Authority Hierarchy (`SKILL.md` §3), not a parallel … ordering"); `reicon.md` does it implicitly (see §4.B below — this is a real, if minor, inconsistency).

## 4. Reicon Audit

### Activation
`reicon.md:15-20`. Three conjunctive conditions: iconography genuinely needed (with a stated UX role), no existing icon system covers it, no explicit instruction names a different library/style/"no icons." States explicitly: "This applies at DESIGN/BUILD, once an icon's UX role has already been established — never earlier in the pipeline." **DOCUMENTED and internally consistent** — the gating text cannot fire before an upstream role exists, because the role is one of the three conjunctive conditions.

Can availability create demand? `reicon.md:29` and the Anti-Slop section (`:69`) both explicitly disclaim this: "justifying the addition of an icon that wouldn't otherwise be needed — Reicon's availability is never itself a reason to add an icon." **DOCUMENTED.** Whether it is **STRUCTURALLY ENFORCED** is a separate question — see §9/§11.

Progressive disclosure / T4: correctly placed. `SKILL.md` §7's T4 row (line 166) gates it on "new iconography is genuinely needed and no existing project icon system or explicit user instruction already covers it" — the same condition stated in `reicon.md` itself, not a looser gloss.

### Precedence
`reicon.md:33-38` states a bespoke 4-item order (explicit instruction → existing system → Reicon → other/custom) rather than an explicit P0–P8 walk. This is **the one place Reicon's documentation format diverges from its two siblings** (see §10, Finding REICON-1). The order itself is not wrong — it is a coherent subset of P2 > P4 > (new slot) > P8 — but it never states where Reicon sits relative to P1 (safety), P3 (Register/Genre), P5 (UX), P6 (Anti-Slop), or P7 (performance), because it predates the "resolve via the existing hierarchy explicitly" convention `kinetics.md`/`smoothui.md` later adopted. Functionally this does not create a contradiction — Reicon's separate Accessibility/Anti-Slop sections cover P1/P6 in substance — but it is a **STRUCTURALLY ENFORCED-by-substance, DOCUMENTED-inconsistently-by-form** gap.

### Existing-System Safety
`reicon.md:71-73` correctly points to `existing-project-safety.md`'s Improve/Replace model rather than restating it, and states migration requires the same explicit confirmation any Replace-classified change requires. **STRUCTURALLY ENFORCED** at the textual-reference level (one rule, one place, per `SKILL.md` §9 Principle 5).

Detection gap: `existing-project-safety.md` §1's Inspect scan (lines 5-14) has explicit, named items for fonts, palette, motion-library presence, spacing scale, and framework — but **no explicit line for "existing icon system."** Reicon's own non-activation depends on "no established project icon system already covers it" being detected, but the closest available Inspect item is #6 (generic framework/dependency detection), which will surface a named icon package (`lucide-react`, `heroicons`) but will not reliably surface a hand-rolled, dependency-free icon set with no distinguishing package signature. See Finding INTEGRATION-1 (§12).

### User Instruction
`reicon.md:35`: "Follow it. Never silently substitute Reicon." Unconditional, correctly worded, matches the P2 precedence stated in `SKILL.md` §3 ("wins over P3–P8 unconditionally"). **STRUCTURALLY ENFORCED by cross-reference.**

### Design-Direction Isolation
`reicon.md` never touches Register/Genre/Dials, Visual Fingerprint, or macrostructure. Confirmed by direct read of `SKILL.md` §4/§6 — neither section mentions Reicon, and `reicon.md` itself states in its Anti-Slop section that it "does not create a new Anti-Slop category" and is explicitly subordinate to "Register/Genre/visual direction." No file edit touched §4 or §6 (confirmed via `PHASE-7.2-REICON-INTEGRATION.md` §11 file-change list and independently by reading current `SKILL.md`). **STRUCTURALLY ENFORCED.**

### Anti-Slop
`reicon.md:69` cross-references SLOP-007 (card-kit, where icon-per-card is "often part of the tell") without modifying it. No new Anti-Slop category. **STRUCTURALLY ENFORCED** by absence of edit (verified: `anti-slop-registry.md` contains zero mentions of Reicon, Kinetics, or SmoothUI).

### Accessibility
`reicon.md:65` is a single-sentence deferral to `A11Y-004`, which is confirmed (by direct read of `accessibility.md:41-50`) to already fully specify role-conditional icon accessibility. No duplication, no new accessibility rule. **STRUCTURALLY ENFORCED.**

### Performance
**Gap.** `reicon.md` has no Performance section at all — the only one of the three implementation-source files without one. Icon delivery does carry real, if smaller, performance considerations (icon-font/sprite payload weight, per-icon SVG inlining bloat) that `performance-hardening.md`'s PERF-001 ("universal for any shipped web page") already applies to in principle, but `reicon.md` never says so explicitly the way `kinetics.md` and `smoothui.md` both do for their own domains. See Finding REICON-2 (§12). **Severity: LOW** — the general PERF-001/PERF-002 rules still apply by default (they are universal, not conditional on being name-checked from `reicon.md`), so this is a documentation completeness gap, not a coverage gap.

### Findings
See §12 (REICON-1, REICON-2, INTEGRATION-1).

## 5. Kinetics Audit

### Activation
`kinetics.md:15-20`. Three conjunctive conditions: a motion/microinteraction behavior already justified by `motion.md`'s vocabulary/explicit UX requirement/direction/instruction, the already-selected `MOTION_INTENSITY` band permits it, no existing motion system already covers it. Explicitly: "never earlier in the pipeline, and never as the reason a motion decision gets made." **DOCUMENTED and internally consistent**, same shape as Reicon.

Can availability create demand? `kinetics.md:30,47`: "Kinetics' availability is never itself a reason to animate something" / "'Kinetics has a nice pattern for X' is never sufficient justification." **DOCUMENTED.**

### Precedence
`kinetics.md:34-43` is the strongest of the three — it explicitly walks all 8 P-levels (P1 safety → P2 instruction → P3 Register/Genre/direction → P4 existing system → P5 UX purpose → Kinetics itself → P7 performance → P8 aesthetic) and states plainly this is "resolved via the existing Authority Hierarchy (`SKILL.md` §3), not a parallel Kinetics-specific ordering." This became the template `smoothui.md` copied (confirmed in `PHASE-7.4-SMOOTHUI-INTEGRATION.md` §"Inspected Architecture": "kinetics.md's explicit P1–P8 authority-hierarchy walkthrough is the closest existing precedent"). **STRUCTURALLY ENFORCED by explicit, complete cross-reference** — the strongest precedence documentation of the three.

One disclosed deviation, correctly self-reported: `PHASE-7.3-KINETICS-INTEGRATION.md` §15 notes the task brief's own illustrative precedence list skipped P6, and `kinetics.md` deliberately follows the real P1–P8 hierarchy instead of reproducing that gap — "disclosed here as a deliberate interpretation, not a silent deviation." This is good practice, not a finding.

### Existing-System Safety
`kinetics.md:69-71` correctly defers to `existing-project-safety.md`. Detection hook: `existing-project-safety.md` §1 item 4 is **explicit and named** — "Motion-library presence — is GSAP/Framer Motion/a CSS-only approach already established." This is the one detection hook of the three that is purpose-built rather than generic, and Kinetics is the only integration with a dedicated Inspect-scan line. **STRUCTURALLY ENFORCED**, and asymmetrically stronger than Reicon's or SmoothUI's equivalent (see Finding INTEGRATION-1).

### Design-Direction Isolation
`kinetics.md:51-57` states `MOTION_INTENSITY` "remains fully authoritative and is not modified, extended, or shadowed by a second scale," and walks conformance at each band (Low/Medium/High) as *conforming to*, never *expanding*, the band. `SKILL.md` §4 was not edited (verified directly). **STRUCTURALLY ENFORCED** — this is the clearest, most load-bearing single sentence across all three integrations, because motion intensity is the dial with the most empirically-demonstrated convergence risk in this repository (Low in 6/6 Phase 7 tests, per the cross-project analysis §5.2/§9).

### Anti-Slop
`kinetics.md:81-83` correctly declines a new category, restates `MOTION-002`'s purpose vocabulary as the standing test, and names the specific anti-patterns from the task brief. Confirmed by grep: zero motion-related entries existed in `anti-slop-registry.md` before or after this integration — no reconciliation was needed and none was fabricated. **STRUCTURALLY ENFORCED.**

### Accessibility
`kinetics.md:73-75` defers to `MOTION-007` and `A11Y-003` (itself confirmed, by direct read of `accessibility.md:33-39`, to be a pointer to `MOTION-007`, not a duplicate). Adds one operative constraint not present in the underlying rules: "A Kinetics pattern with no meaningful reduced-motion treatment is not production-ready." This is a reasonable, non-duplicative tightening, not new rule content. **STRUCTURALLY ENFORCED.**

### Performance
`kinetics.md:77-79` defers to `MOTION-004`/`MOTION-005`/`MOTION-006`, confirmed current (post-Phase-7.1 paint-only carve-out) by direct read of `motion.md:42-51`. States Kinetics "must not be used to introduce unnecessary continuous animation, expensive effects, or excessive simultaneous animation beyond what the already-established UX purpose and `MOTION_INTENSITY` band justify." **STRUCTURALLY ENFORCED.**

### Findings
None rising above LOW for Kinetics in isolation. Its cross-integration exposure is covered in §7.

## 6. SmoothUI Audit

### Activation
`smoothui.md:15-22`. The activation clause has a real branch not present in Reicon or Kinetics: component justification requires **either** (a) the component has already cleared `SKILL.md` §9 Principle 11 (3+ uses, same intent), **or** (b) "the user has explicitly requested SmoothUI for this implementation." This is the "P2 escape hatch" — confirmed present in the current file and load-bearing, not vestigial.

This branch is architecturally defensible, not a loophole, for a specific reason stated explicitly at `smoothui.md:22`: "An explicit request to use SmoothUI does not by itself justify extracting a reusable component or abstracting a one-off; `SKILL.md` §9 Core Principle 11 still governs whether abstraction is warranted." The distinction being drawn is between *implementing* a single already-justified UI element via SmoothUI (a one-time BUILD choice) and *abstracting* it into the project's own reusable component library (a Principle 11 decision). These are genuinely different acts. The text is coherent, but it depends on the agent correctly distinguishing "I used SmoothUI once to build this modal" from "I extracted a reusable `<SmoothModal>` wrapper because SmoothUI made it easy" — a distinction with no mechanical check behind it. **Classification: AMBIGUOUS in edge-case practice, DOCUMENTED and internally coherent in principle.** Not a contradiction; a judgment call the architecture correctly flags as still governed by Principle 11, but does not make self-verifying.

### Precedence
`smoothui.md:35-45` walks all 8 P-levels explicitly, matching `kinetics.md`'s template. **STRUCTURALLY ENFORCED by explicit cross-reference**, same as Kinetics.

### Existing-System Safety
`smoothui.md:47-49` defers correctly, and is the only one of the three integrations to **self-disclose** the detection-hook weakness: "No dedicated 'existing component system' detection step exists in `existing-project-safety.md` §1's Inspect scan — item 6 … is the closest existing hook … but it's more general-purpose than the 'motion-library presence' line Kinetics could hook into directly" (`PHASE-7.4-SMOOTHUI-INTEGRATION.md`, Residual Risk #2). This self-disclosure is accurate — confirmed by direct read of `existing-project-safety.md` §1, which indeed has no line naming component/design-system detection. **DOCUMENTED as a known gap by the SmoothUI report itself; the identical gap exists for Reicon but was not self-disclosed there** (Finding INTEGRATION-1, §12).

### User Instruction
`smoothui.md:38`: "Follow it. Never silently substitute SmoothUI." Same unconditional P2 framing as the other two. **STRUCTURALLY ENFORCED.**

### Design-Direction Isolation
`smoothui.md:61` and the closing "What SmoothUI Must Never Be Used to Justify" list (`:95-101`) are the most thorough of the three on this point, explicitly naming "Card usage, button hierarchy, page structure, spacing, typography, color, visual style, density, and interaction model" as staying governed entirely by the existing architecture. `SKILL.md` §4/§6 unedited (verified). **STRUCTURALLY ENFORCED for the dimensions named** — see §12 Finding CROSS-1 for the one dimension *not* named (iconography).

### Anti-Slop
Cites SLOP-007 and SLOP-008 correctly (confirmed both exist and are `category: layout`/`components` respectively, directly applicable). No new category. **STRUCTURALLY ENFORCED.**

### Accessibility
Defers to `A11Y-002`/`A11Y-005`/`A11Y-007`/`A11Y-008`, all confirmed current and correctly characterized by direct read of `accessibility.md`. **STRUCTURALLY ENFORCED.**

### Performance
Defers to `performance-hardening.md` generally and `PERF-002` specifically for above-the-fold components, plus cites Principle 12 and `existing-project-safety.md` §2's Replace threshold for the dependency-footprint question. **STRUCTURALLY ENFORCED.**

### Principle 11 (specific focus, per audit brief §3.I)
Confirmed: `SKILL.md` §9 Principle 11 is unedited (verified byte-level via the "Non-changes" and file-change lists in all three integration reports, and independently by reading the current file — line 192 reads identically to the pre-Phase-7.2 text quoted in `PHASE-7.4-SMOOTHUI-INTEGRATION.md`). `smoothui.md` references it by name six times, always as a gate SmoothUI must clear, never as something SmoothUI's presence weakens. The Design-System Interaction section (`:55-57`) is explicit: "SmoothUI must never be used to justify over-componentizing an interface: it fills an abstraction already justified by repeated use, it does not create the justification." **STRUCTURALLY ENFORCED for the general case; AMBIGUOUS for the explicit-one-off-request branch**, as noted under Activation above.

### Findings
CROSS-1 (§12) is the central SmoothUI-specific finding, more precisely a cross-integration finding — see §7.

## 7. Cross-Integration Audit

### Reicon + SmoothUI
**This is the one genuine gap.** `smoothui.md`'s "What SmoothUI Must Never Be Used to Justify" list (`:95-101`) explicitly protects "a visual style, density, spacing, color, or motion decision" from being justified merely by SmoothUI's availability. **Iconography is not on that list.** A SmoothUI-implemented component that ships with a bundled icon (a card with a status icon, a nav item with a chevron, an alert with a warning glyph) has no explicit textual instruction anywhere in `smoothui.md` requiring that icon to independently clear `reicon.md`'s Selection questions ("What is the icon's purpose... Would text communicate this more clearly... Is this decorative rather than functional?") before shipping. `reicon.md`'s own Non-Activation clause ("justifying the addition of an icon that wouldn't otherwise be needed") protects against *inventing* a new icon because Reicon exists — it does not obviously reach the case where an icon arrives *already embedded* inside an adopted SmoothUI component and is never treated as a separate "new iconography" decision requiring its own Selection pass at all. Classification: **AMBIGUOUS, verging on CONTRADICTED-by-omission** relative to the explicit motion protection sitting one paragraph away in the same file. See Finding CROSS-1.

### Kinetics + SmoothUI
**Adequately covered.** The same "What SmoothUI Must Never Be Used to Justify" list explicitly names "a … motion decision" as protected — a SmoothUI component's bundled animation cannot be justified merely by the component shipping with it; it must still clear `MOTION-002`'s purpose vocabulary and the already-selected `MOTION_INTENSITY` band. This is the asymmetry that makes Finding CROSS-1 legible: the architecture clearly *considered* this exact cross-integration risk for motion and wrote the protection down — it simply didn't extend the same sentence to cover icons. **DOCUMENTED and STRUCTURALLY ENFORCED for motion specifically.**

### Reicon + Kinetics
**Adequately covered, generically.** Neither file mentions the other, but each independently states its own non-activation is unconditional on the other's availability: `kinetics.md:30` bars animating something "that wouldn't otherwise be needed" regardless of what triggered the idea, and `reicon.md:29` bars adding an icon "that wouldn't otherwise be needed" on the same terms. An icon does not become a legitimate animation target merely because both Reicon and Kinetics exist — `MOTION-001`'s frequency gate and `MOTION-002`'s purpose vocabulary apply to an icon-hover animation exactly as they apply to any other element, with no icon-specific exemption anywhere in either file. **STRUCTURALLY ENFORCED by the general motion-decision-sequence, not by anything icon-specific** — sufficient, because the general rule doesn't need an icon-specific carve-out to already cover icons.

### All three together — the "library exists → component exists → icon exists → animation exists" chain
Each individual link in this chain has a textual guard (see above), so no *single* transition is undefended on paper. The residual risk is systemic rather than textual: **all three files rely on the same governance shape** — prose Activation/Non-Activation criteria, explicit disclaimers that availability ≠ justification, and a "qualitative, not scored" Validation section with no mechanical check. All three integration reports self-disclose this as a limitation ("No mechanical validation exists for the Activation/Precedence rules... correct application depends on the agent actually reading and applying [the file] at BUILD"). This is not a flaw unique to these three files — it matches the rest of the T3/T4 material (`LAYOUT-008`/`009`/`010`, `gesture-physics.md`) — but the audit brief specifically asks whether the combined availability of three simultaneous implementation sources raises the systemic risk, and the evidence says it plausibly does: the more optional-but-available mechanisms are live in a single BUILD pass, the more individually-small, individually-justified judgment calls stack up before VALIDATE ever re-examines the result as a whole, and VALIDATE itself has no step that specifically re-traces "was every icon, every animation, and every componentized pattern in this build independently justified, or did some arrive bundled inside another mechanism's output." **This is the direct, present-tense analog of REF-009's already-observed 6/6 convergence** — the same "generative, not a quota, considered-then-rejected is valid" language did not prevent a 100% adoption rate in practice. See Finding CROSS-2.

## 8. Progressive Disclosure Audit

All three files are correctly gated at T4 in `SKILL.md` §7 (line 166), on real-need conditions stated inline and matching each file's own Activation section:
- Reicon: "only when new iconography is genuinely needed and no existing project icon system or explicit user instruction already covers it."
- Kinetics: "only when a motion/microinteraction implementation decision is already in scope (motion need already established by `motion.md`/`MOTION_INTENSITY`) and no existing project motion system or explicit user instruction already covers it."
- SmoothUI: "only when a component or UI pattern has already been established as necessary and implementation is genuinely in scope, and no existing project component system or explicit user instruction already covers it."

**Core skill functions without them:** confirmed. `SKILL.md` T0 content (§1–§6, §8–§9) makes zero references to any of the three; removing all three files would not break any cross-reference elsewhere in the T0/T1/T2 material (verified by grep — all mentions of Reicon/Kinetics/SmoothUI outside their own files are confined to `SKILL.md`'s single T4 table row and the Phase 7 benchmark/report files).

**Do they change upstream reasoning?** No evidence they do, by design — none of the three appear in §1 (Operating Model), §2 (Routing), §4 (Register/Genre/Dials), §5 (Project Context schema), or §6 (Fingerprint). This matches the intended model exactly.

**A pre-existing, non-unique characteristic worth naming, not a new flaw:** "T4, load only when needed" is a documentation convention in an LLM-driven skill, not an access-controlled gate — nothing prevents an agent from reading `reicon.md` speculatively before an icon need is established, the same as nothing prevents speculative reading of `gesture-physics.md` before a drag interaction is in scope. This is a property of the whole progressive-disclosure mechanism, not something these three integrations introduced or worsened, and is out of scope for a finding against them specifically.

## 9. Architectural Integrity

Checked directly, not assumed:
- **New pipeline stage:** none. `SKILL.md` §1's stage table is unedited (confirmed identical to the pre-Phase-7.2 version cited in all three integration reports' "Non-changes"/"file-change" sections, and by direct read).
- **New routing axis:** none. §2's three axes (Scope, Project State, Task Mode) are unedited.
- **New classifier or scoring system:** none. All three files explicitly end their Validation sections with "No numerical scoring is introduced," and none define a compatibility matrix, tier system, or threshold beyond referencing existing ones (`MOTION_INTENSITY`, Principle 11).
- **Duplicated authority:** none found. Each file explicitly resolves precedence via `SKILL.md` §3 rather than restating it (Reicon does so implicitly/by substance, not by explicit P-level walk — see Finding REICON-1, a format inconsistency, not duplicated authority).
- **Duplicated rules:** none found — confirmed by grep for `### [A-Z]+-[0-9]+` rule-ID headers across `references/` and `rule-catalog/`; zero duplicates, matching all three integration reports' own validation claims.
- **Conflicting terminology:** one real distinction, correctly maintained, not drift: "implementation **source**" (Reicon, SmoothUI) vs. "implementation **repertoire**" (Kinetics) is a deliberate, stated difference — `kinetics.md:3` explains Kinetics supplies *patterns*, not a single default *thing to reach for*, matching how `PHASE-7.3-KINETICS-INTEGRATION.md` §3 explains "Reicon is a default source once a slot exists... while Kinetics is a repertoire consulted only once a behavior is already decided." This is intentional precision, not inconsistency.
- **Hidden dependencies:** none found between the three files themselves at the textual level, except the one-directional relationship section in `smoothui.md:71-79` ("Relationship to Reicon and Kinetics"), which is additive documentation, not a functional dependency — `reicon.md` and `kinetics.md` do not need to read or reference `smoothui.md` to be individually correct, and each already states its own non-activation unconditionally (§7 above).
- **Unnecessary loading:** none found — see §8.
- **Architecture existing only to support an external resource:** none — all three files are pure T4 reference material with no `SKILL.md` T0/T1/T2 structural change beyond the single shared table row.

**Compared against the stated principle** ("No new stage, routing axis, classifier or scoring mechanism unless independently justified"): **no violation found.**

## 10. Rule / Terminology Duplication

Searched for: Reicon, Kinetics, SmoothUI, "implementation source," "implementation repertoire," iconography, "motion implementation," "component implementation," "Principle 11," "3+ uses," "explicit user instruction," "existing project system."

- **Rule-ID duplication:** zero (grep-verified across all `references/` and `rule-catalog/` files).
- **"Implementation source" vs. "implementation repertoire":** deliberate distinction, not drift (§9 above).
- **Precedence-section format:** inconsistent across the three — `reicon.md` uses an unlabeled 4-item list; `kinetics.md` and `smoothui.md` both explicitly walk P1–P8 and name "resolved via the existing Authority Hierarchy… not a parallel… ordering." This is a real, minor, evidence-based inconsistency (Finding REICON-1), not a contradiction — Reicon's substance still resolves consistently with P0–P8, it is simply not stated in the same explicit form.
- **"Relationship to Reicon and Kinetics" section:** exists only in `smoothui.md`, not reciprocated in `reicon.md` or `kinetics.md` (they predate it). Not a contradiction — see §7, Reicon + Kinetics — but a one-directional piece of cross-integration documentation that a reader of `reicon.md` or `kinetics.md` alone would never see.
- **No stale wording found** referencing pre-Phase-7.1 rule text (e.g., the old, imprecise MOTION-004 wording) inside any of the three new files — all three cite the current, corrected rule text (confirmed by direct comparison against the live `motion.md`).

## 11. Evidence Classification

| Claim | Classification | Basis |
|---|---|---|
| None of the three answer "should this exist" | DOCUMENTED, STRUCTURALLY ENFORCED | Explicit opening-paragraph statements in all three files; no §2/§4 routing hook exists for any of them |
| Explicit user instruction always wins | STRUCTURALLY ENFORCED | Cross-referenced to `SKILL.md` §3 P2, worded unconditionally in all three files |
| Existing project systems are preserved by default | STRUCTURALLY ENFORCED (textually) / **AMBIGUOUS (detection-dependent)** | Correct textual deference to `existing-project-safety.md`, but the Inspect scan has no dedicated icon-system or component-system detection line — only motion has one (Finding INTEGRATION-1) |
| No new Anti-Slop category was created | STRUCTURALLY ENFORCED | Verified by direct read of `anti-slop-registry.md`: zero mentions of any of the three |
| No new fingerprint dimension | STRUCTURALLY ENFORCED | `SKILL.md` §6 unedited; `kinetics.md`/`smoothui.md` explicitly disclaim it |
| No new pipeline stage/routing axis/classifier | STRUCTURALLY ENFORCED | Verified directly against current `SKILL.md` §1/§2 |
| Motion decisions can't be smuggled in via a SmoothUI component | STRUCTURALLY ENFORCED | Explicit named protection in `smoothui.md`'s "Must Never Be Used to Justify" list |
| Icon decisions can't be smuggled in via a SmoothUI component | **CONTRADICTED-by-omission / AMBIGUOUS** | Same list omits iconography entirely — see Finding CROSS-1 |
| Discipline holds in real multi-project practice | **NOT VERIFIABLE from this repository** | All three integration reports explicitly state "untested in practice... no benchmark run exercised this change"; the closest available evidence (REF-009's 6/6 adoption under identical qualitative-judgment governance) points the other way |
| Reicon has a Performance consideration parallel to Kinetics/SmoothUI | CONTRADICTED | `reicon.md` has no Performance section; the other two do (Finding REICON-2) |
| SmoothUI's P2-explicit-request branch cannot be misused to bypass Principle 11 | AMBIGUOUS | Text correctly distinguishes "implement once" from "abstract," but the distinction is judgment-based with no mechanical check |

## 12. Findings

### CROSS-1 — SEVERITY: HIGH
- **Location:** `design-excellence/references/smoothui.md`, "What SmoothUI Must Never Be Used to Justify" (lines 95-101), and the Anti-Slop section (lines 59-61).
- **Concrete issue:** The list explicitly protects visual style, density, spacing, color, and motion decisions from being justified merely by SmoothUI's availability, but does not name iconography. A SmoothUI component adopted for an already-justified pattern may ship with a bundled icon (status glyph, chevron, close button) that is never independently run through `reicon.md`'s Selection test (purpose, text-alternative check, decorative-vs-functional) because it arrives as part of "the component," not as a separately-recognized "new iconography" decision.
- **Why it matters:** This is precisely the cross-integration failure mode the audit brief names as one of the most important to check ("component exists → icon exists," bypassing the "product need → design decision → justified implementation" sequence). Motion received explicit protection against exactly this same mechanism one clause earlier in the same file; icons did not, for no stated reason.
- **Evidence:** `smoothui.md:95-101` (full list, iconography absent); contrast with `smoothui.md:61` and `reicon.md:29,69` (motion is protected explicitly; icons are only protected against being *newly invented*, not against arriving *pre-bundled*).
- **Recommended action (architectural level only, not to be implemented here):** extend the existing "Must Never Be Used to Justify" list in `smoothui.md` to explicitly name iconography alongside motion — one clause, no new mechanism, consistent with how the file already handles motion.

### CROSS-2 — SEVERITY: MEDIUM
- **Location:** Systemic — `reicon.md`, `kinetics.md`, `smoothui.md` jointly, plus `visual-references.md` REF-009 as precedent evidence.
- **Concrete issue:** All three implementation sources are gated exclusively by prose Activation/Non-Activation criteria and a "qualitative, not scored" Validation section, with no VALIDATE-stage mechanical check that re-traces whether every icon/animation/component present in a finished build was independently justified versus arriving bundled through one of the other two mechanisms. The repository already has direct, in-house evidence (REF-009's 6/6 adoption across Phase 7 benchmarks, under the same "generative, considered-then-rejected is valid" governance language) that this governance shape does not reliably prevent an optional mechanism from becoming a de facto default.
- **Why it matters:** With three simultaneously-available implementation sources instead of one, the number of individually-small, individually-defensible judgment calls that can stack up in a single BUILD pass increases, while the checking mechanism (self-critique, qualitative) does not scale with that increase.
- **Evidence:** `PHASE-7-CROSS-PROJECT-ANALYSIS.md` lines 110-117, 588, 595 (REF-009 adoption data and its explicit citation as the risk model for both Kinetics and SmoothUI); all three integration reports' Residual Risks sections independently disclaiming real-world verification.
- **Recommended action (architectural level only):** none of the three files need new scoring — that would violate Principle 12 (leverage over coverage) and the task brief's own ban on new classifiers. The lower-risk architectural lever, if this is judged worth acting on, sits in `critique-protocol.md`'s existing Level 1 floor (already the mechanism that checks Craft Correctness and Technical Correctness) — a possible future scope, not something to decide or implement in this audit.

### REICON-1 — SEVERITY: LOW
- **Location:** `design-excellence/references/reicon.md`, "Precedence" section (lines 31-38).
- **Concrete issue:** Unlike `kinetics.md` and `smoothui.md`, Reicon's Precedence section does not explicitly state "resolved via the existing Authority Hierarchy (`SKILL.md` §3)" or walk the full P1–P8 ladder; it states its own 4-item order instead.
- **Why it matters:** Purely a documentation-consistency issue — the substance is not contradictory (Reicon's separate Accessibility/Anti-Slop sections cover the P1/P6 content in effect), but a reader comparing the three files side-by-side would reasonably wonder whether Reicon's precedence model is actually a strict subset of the Authority Hierarchy or a separate one, since the file itself never says.
- **Evidence:** `reicon.md:33-38` vs. `kinetics.md:34-43` and `smoothui.md:35-45`.
- **Recommended action (architectural level only):** none required to function correctly; a future editorial pass could align `reicon.md`'s Precedence section format to match its two siblings for consistency, purely cosmetic.

### REICON-2 — SEVERITY: LOW
- **Location:** `design-excellence/references/reicon.md` — entire file.
- **Concrete issue:** No Performance section, unlike `kinetics.md` and `smoothui.md`.
- **Why it matters:** Icon delivery is not performance-free (icon-font/sprite payload, per-icon inline SVG bloat at scale), and `performance-hardening.md`'s PERF-001 is stated as universal, so this is not a coverage gap in practice — but it is an asymmetry in how thoroughly each of the three implementation sources documents its own performance footprint.
- **Evidence:** `reicon.md` (no "## Performance" heading anywhere) vs. `kinetics.md:77-79` and `smoothui.md:67-69`.
- **Recommended action (architectural level only):** a future editorial pass could add a one-paragraph Performance deferral to `reicon.md`, pointing to `performance-hardening.md` generally, matching the other two files' shape.

### INTEGRATION-1 — SEVERITY: MEDIUM
- **Location:** `design-excellence/references/existing-project-safety.md` §1 (Inspect scan, lines 5-14).
- **Concrete issue:** The Inspect scan has a named, explicit line for motion-library detection (item 4) but no equivalent named line for "existing icon system" or "existing component/design-system library" — both Reicon's and SmoothUI's non-activation depend on detecting these, but must currently rely on the generic item 6 (framework/dependency detection), which will catch a named package but may miss a hand-rolled, dependency-free icon set or component layer.
- **Why it matters:** This creates an asymmetry in how reliably each of the three implementation sources' "an existing system already covers it" non-activation clause can actually be satisfied in practice — Kinetics has the strongest detection hook of the three, Reicon and SmoothUI the weakest, for no principled reason tied to their relative risk.
- **Evidence:** `existing-project-safety.md:10-14` (items 2-6, item 4 named, items for icon/component systems absent); self-disclosed for SmoothUI specifically in `PHASE-7.4-SMOOTHUI-INTEGRATION.md` Residual Risk #2, but the identical gap for Reicon was not self-disclosed in `PHASE-7.2-REICON-INTEGRATION.md`'s Residual Risks section.
- **Recommended action (architectural level only):** a future pass could add two lines to `existing-project-safety.md` §1 — "existing icon system" and "existing component/design-system library" — mirroring the existing motion-library line. This is the same architectural shape already in the file; no new mechanism.

## 13. What Should NOT Be Changed

- **The core sequencing statement** ("decide what the interface needs, then decide how it should behave and look, only then consult an implementation source") in `smoothui.md:79` — correct, load-bearing, and the clearest single expression of the intended architecture across all three files. Any future correction to CROSS-1 should extend this statement's protection list, not restate or relocate it.
- **`kinetics.md`'s explicit P1–P8 walkthrough** — the strongest precedence documentation of the three and the correct template for any future implementation-source integration.
- **The absence of a scoring/classifier system anywhere in the three files** — consistent with `SKILL.md` §9 Principle 12 and the task brief's own explicit ban; do not introduce one to address CROSS-2, which has a cheaper fix available (see §12).
- **`MOTION_INTENSITY`'s untouched authority** — the single most load-bearing sentence in `kinetics.md` given the documented Low-motion convergence baseline; nothing here suggests it needs revisiting.
- **The one-rule-one-place discipline** — zero duplicate rule-ID headers were found; this remains fully intact after all three integrations and should not be disturbed by any future correction.
- **Reicon's, Kinetics', and SmoothUI's shared refusal to fabricate technical/install/API details** — all three correctly defer this to BUILD time against the project's actual stack, consistent with `SKILL.md` §9 Principle 4 (time-bound knowledge lives in governed data, never hardcoded). This should not be "fixed" by inventing plausible-sounding package names or APIs.

## 14. Final Verdict

**PASS WITH RISKS.**

Reasoning: no BLOCKER was found — none of the three integrations contradicts the Authority Hierarchy, creates a new pipeline mechanism, or silently overrides an existing project system or explicit instruction. One HIGH finding exists (CROSS-1) and it is a real, concrete, textually-verifiable gap, not a hypothetical — but it is a narrow, one-clause omission in an otherwise-coherent document, with an available narrow fix, not a structural failure requiring a redesign of any of the three integrations. One MEDIUM systemic finding (CROSS-2) is precedented by in-repository evidence (REF-009) but is explicitly disclosed as an open risk by the architecture's own integration reports, not hidden. The remaining findings are LOW/MEDIUM documentation-consistency and detection-hook asymmetries that do not change runtime behavior.

This does not clear the bar for PASS outright, because CROSS-1 is exactly the kind of gap that produces a real defect class (unjustified icon proliferation via component adoption) rather than a merely theoretical one, and it sits in the one area (iconography inside components) the audit brief specifically asked to be checked hardest. It does not fall to REQUIRES TARGETED CORRECTION or BLOCKED, because the fix is narrow, low-risk, and does not require touching the architecture, the Authority Hierarchy, or any of the other two integrations.

## 15. Recommended Next Step

At the architectural level only, without prescribing implementation:

1. **Close CROSS-1** by extending `smoothui.md`'s existing "What SmoothUI Must Never Be Used to Justify" list to name iconography alongside the visual style/density/spacing/color/motion items already there — the same sentence shape, one more noun, no new section or mechanism.
2. **Consider closing INTEGRATION-1** by adding two named lines to `existing-project-safety.md` §1's Inspect scan (existing icon system; existing component/design-system library), mirroring the existing motion-library line — brings Reicon's and SmoothUI's detection hooks to parity with Kinetics'.
3. **Treat CROSS-2 as monitored, not fixed**, consistent with how the Phase 7 cross-project analysis already treats REF-009 ("monitor... adoption rate as a possible new default reflex") — the correct next evidence would be a future benchmark pass that exercises all three implementation sources together and checks, after the fact, whether icons/motion/components converged toward default reflexes the way REF-009 did, before deciding whether a mechanical check is actually warranted.
4. **REICON-1 and REICON-2 are optional editorial-consistency passes**, safe to defer indefinitely without functional risk.

None of the above was implemented as part of this audit, per the audit brief's explicit constraints.

---

## Audit Metadata

**Files inspected:** 20 (full read) — listed in §1.
**Files created/modified:** 1 — this report (`benchmarks/phase-7/PHASE-7.5-INTEGRATION-AUDIT.md`). No runtime skill, reference, architecture, or configuration file was modified.
**Findings by severity:** BLOCKER: 0 · HIGH: 1 (CROSS-1) · MEDIUM: 2 (CROSS-2, INTEGRATION-1) · LOW: 2 (REICON-1, REICON-2).
**Final verdict:** PASS WITH RISKS.
**Targeted correction required before next benchmark:** Not mandatory, but recommended — CROSS-1's fix is a single-sentence addition to one already-existing list in `smoothui.md`, the narrowest possible correction surface, and directly closes the one HIGH finding. CROSS-2 and INTEGRATION-1 can reasonably wait for a future benchmark pass to generate real evidence before deciding whether to act.
