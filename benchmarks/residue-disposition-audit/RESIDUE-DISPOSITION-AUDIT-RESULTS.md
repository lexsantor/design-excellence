# Residue Disposition Audit — Results

**Status:** COMPLETED. Recommendation **CURRENT ARCHITECTURE SUFFICIENT**.
**Authorization:** AUTHORIZED FOR READ-ONLY AUDIT (`STATE.md`, human-authorized 2026-09-27). Autonomous milestone under `loop.md`.
**Scope:** read-only governance/architecture audit of Design Excellence at HEAD `e80bdbf`. No skill file, rule, principle, visual reference, contract, catalog record or library was changed. No reference was acquired; no principle or rule was created, promoted or exported; no behavioural benchmark was run.

**Labels.** **[DOC]** documented in a governed file, record or prior report. **[MEAS]** measured by a prior benchmark. **[INF]** inference by this audit. **[REC]** recommendation.

Identity boundary: this report follows the Phase 10.7 Integration Contract §15. It names no source, vendor, product or marketplace; no path, file name, route or measurement from any source; and no catalog id other than PRN ids. Residue items keep the labels **R1–R16** of the Rejected Residue Coverage Audit (the 16 catalog observations that support no accepted principle, in ascending catalog id order).

---

## 1. Executive conclusion

- **Disposition of the 16 items:** A 0, **B 11**, C 0, D 0, **E 4**, **F 1** (§3). The 11 B items reduce to **three distinct knowledge units**: narrow-viewport reflow, view-state truthfulness, and decision explanation (§5).
- **Every B unit is rule-shaped** (prescriptive, with a layer, severity and validation), not EXPLORE-shaped. Its fitting destination is the existing, DE-governed **Rule Catalog** (T2), not the Principle Pool or Visual References (§6).
- **The architectural gap reported earlier is real, but it is a provenance-route gap, not a missing knowledge home.** DE already has a governed, non-EXPLORE runtime knowledge path: the Rule Catalog. What does not exist is a crossing from the *external catalog* into it. The residue does not justify building one: it fails all five conditions for a second path (§7).
- **The key question.** The limitation is not merely that useful knowledge "is not represented as an EXPLORE-time Principle". That knowledge should never be a Principle. Where it has value, it is ordinary Rule Catalog material, and it can come from DE-native sources (public authorities such as WCAG, and DE's own benchmark failures), as existing rules already do. No materially justified need for a second governed runtime path is shown.
- **Behaviour.** DE produced no broad failure in these classes (22 of 24 criteria passed; the one failure did not replicate, 0 of 3). This does **not** prove the guidance is useless. It means no runtime value has been demonstrated that could justify new architecture (§4).

## 2. Evidence base and study boundaries

Read in full for this audit:

- `loop.md` (§1–§4, §6–§9, §15–§17), `STATE.md`.
- Phase 10.7 Integration Contract, read completely. SHA-256 `4611b171…71e56f1`, the version the previous governance runs read.
- Catalog Phase 10.2 architecture decision §13 and §16; catalog Phase 14 corpus gap analysis §4–§9.
- The 16 residue observation records (statement, dimension, polarity, limitations) and the 5 rejected PRINCIPLE records (abstraction and **full** rejection reason; the earlier audits read only ~400–420 characters). Extracted by a read-only script.
- The four prior reports: Reference Architecture Audit, Rejected Residue Coverage Audit, Behavioural Residue Benchmark, Responsive Reflow Replication.
- DE runtime: `SKILL.md` §1, §3, §5, §7, §9; Rule Catalog `layout-interaction.md`, `accessibility.md`, `content-copy.md`, `performance-hardening.md`, and the rule index of all seven categories; `principle-pool.md`; `visual-references.md`. A repository-wide search confirmed that no DE file names WCAG 1.4.10 Reflow or states a narrow-viewport reflow directive.

What each study can and cannot establish (main agent and reviewer agree):

| Study | Result | Can establish | Cannot establish |
|---|---|---|---|
| Reference Architecture Audit | 16 of 26 observations have no route into DE | The routes: one admission path (Gates 1–3), one consumption point (LAYOUT-010 in EXPLORE); the product-led motivation of 10.2 §13.1 is unmet | Whether the unrouted material is valuable, already covered, or behaviourally needed ("net practical size of the gap is unmeasured") |
| Rejected Residue Coverage Audit | 15 of 16 not covered, 1 not assessable, 0 covered | **Documented** coverage: no DE directive reaches any item; rejection-time "already covered" claims were not borne out by DE's text | Model behaviour ("measures what DE's files state, not what the model does") |
| Behavioural Residue Benchmark | 22 PASS, 1 FAIL, 1 NOT ASSESSABLE over six in-remit classes | On greenfield page BUILDs through the full pipeline, DE meets these classes without any rule | Variance (n = 1 per class); existing-project, POLISH, HARDEN-skipped or time-pressured contexts; criteria were written by the main agent |
| Responsive Reflow Replication | Mechanism in 0 of 3; 1 of 4 comparable builds overall | The chart-reflow failure is isolated, not systematic | Other classes; secondary tables (the same technique appeared on one); unprimed briefs (the tasks stated phone use) |

These results do not contradict each other. They measure different things: routes, written guidance, and behaviour. Together they separate **absence of guidance** (confirmed) from **presence of failure** (not supported by the sample).

## 3. Complete 16-item disposition matrix

Disposition model: **A** adequately covered by existing runtime knowledge · **B** potentially useful reusable knowledge outside runtime coverage · **C** contextual technique with insufficient generality · **D** product/data/domain-specific · **E** correctness or engineering detail better handled outside DE · **F** insufficient evidence to classify.

| Item | Dim. / polarity | Transferable content (generalized) | Disp. | Value type (B) | Unit | Reason and nearest DE entry checked |
|---|---|---|---|---|---|---|
| R1 | responsive / defect | no narrow-viewport adaptation: side navigation stays in flow, page overflows, content clips | **B** | responsive/compositional (normative floor) | U1 | No directive requires narrow-viewport reflow. INTX-003's "collapse to a menu" fires only for wrapping labels. LAYOUT-005 and HARDEN-003 cover other overflow causes. LAYOUT-004 hides overflow rather than adapting. A11Y-001 does not include WCAG 1.4.10 Reflow |
| R2 | composition / positive | one editorial home composition at one viewport | **F** | – | – | Descriptive, a single variant, and states no claim, so it cannot be judged reusable or specific. Nothing in DE covers it either |
| R3 | responsive / positive | sidebar leaves the canvas below a breakpoint; header reduces to a menu; secondary cards stack below the main list | **B** | responsive/compositional | U1 | No DE entry beyond INTX-003's label-wrap remedy. Weak evidence (non-reproducible shipped output), corroborated by R4 |
| R4 | responsive / positive | narrow view keeps every module, stacked after the main feed; cards change orientation | **B** | responsive/compositional | U1 | PRN-0001 has the keep-and-stack logic, but its `do_not_apply_to` excludes feed-based sites and non-entry pages, and it is an optional EXPLORE input, not a rule |
| R5 | interaction / positive | two forms of one calculation agree at shared inputs | **E** | – | – | Business-logic consistency. CONTENT-001 governs wording, not computed results |
| R6 | interaction / positive | show the working with the user's values; name what decided the recommendation | **B** | content/copy | U3 | CONTENT-002's formula is scoped to error, failure and empty states |
| R7 | component / positive | shared limits duplicated across screens, kept equal only by comments | **E** | – | – | Single-source-of-truth engineering. `SKILL.md` §9 Principle 5 governs DE's own files; Principle 11 is a reuse threshold |
| R8 | interaction / positive | selection pruned to the filtered set, kept across pages; page reset and clamped on filter change; bulk bar only with a selection | **B** | interaction/state | U2 | INTX-001 lists per-component visual states; INTX-002 governs recovery. Neither says what a selection reaches |
| R9 | interaction / defect | selection never reduced on filter change; hidden rows stay selected and counted | **B** | interaction/state | U2 | The user-visible failure counterpart of R8. Nothing in DE would prevent it |
| R10 | interaction / positive | a determined answer stated instead of a one-option control; fields only when relevant; no payment form when nothing is charged | **B** | interaction/state (forms) | U2 | A11Y-007 covers field-state rendering. A11Y-001's redundant-entry concerns data the user already entered, not options derived from other data. The domain specifics are D fragments |
| R11 | interaction / positive | validation uses the same condition as display, written separately in two places | **E** | – | – | The item's core claim is code structure. Its user-visible half (a hidden field is never required) is carried by U2 through R10 |
| R12 | component / positive | rows declare their kind; a mark only with two or more columns and a unique best; ties unmarked; marks scoped to the compared set | **B** | normative display integrity (comparison honesty) | U2 | CONTENT-003 names comparison rows but forbids fabricated values only. Which rows rank, and the direction judgements, are D fragments |
| R13 | interaction / positive | "differences only" control shown only when it would have an effect, carrying its count; emptied groups lose their heading | **B** | interaction/state | U2 | No DE entry. Generalizes as "a control or mark appears only when true or effective" |
| R14 | component / positive | one stored structure from which list and counts derive; overview reuses the component read-only | **E** | – | – | Data modelling. Principle 11 is a reuse threshold, not single-source derivation |
| R15 | interaction / positive | one selection shared across a map and a list; second click clears | **B** | interaction/state | U2 | INTX-001 has no selected or linked state; REF-008 is task-state hierarchy |
| R16 | interaction / defect | filter not passed to the linked view; helper text claims a highlight that cannot exist; one colour for stored status and live selection | **B** | interaction/state + copy | U2 | No state-distinctness rule; REF-007 is optional colour-as-wayfinding. Sample-data aspects are D fragments |

**Counts:** A **0** · B **11** (R1, R3, R4, R6, R8, R9, R10, R12, R13, R15, R16) · C **0** · D **0** as a primary disposition (D fragments inside R10, R12, R16) · E **4** (R5, R7, R11, R14) · F **1** (R2).

## 4. Coverage reconciliation

1. **Routes vs coverage.** The Reference Architecture Audit's 16 unrouted observations are exactly R1–R16. Being unrouted says nothing about coverage. The Coverage Audit then showed that none of them is covered by DE's written guidance. This audit re-checked every near-miss (INTX-003, PRN-0001, CONTENT-002, CONTENT-003, A11Y-001, A11Y-007, INTX-001, REF-007, REF-008) and found no directive that reaches any item. **Disposition A = 0 confirms that coverage result.** [DOC]
2. **Coverage vs behaviour.** "Not covered" describes the files, not the model. The Behavioural Benchmark tested the six in-remit classes that correspond to the B units and found them met in five classes and partly failed in one. [MEAS] The Replication showed that partial failure is isolated. [MEAS] Together: the guidance is missing and the behaviour is largely present. The model's priors appear to supply what the files do not, for greenfield page BUILDs. [INF]
3. **Rejection-time coverage claims.** With the full rejection reasons now read, the finding of the Coverage Audit §7 stands. The rejections of PRN-0005 and PRN-0006 rested on pool fit and material difference (ordinary form UX, correctness hygiene). Their mentions of A11Y-001, A11Y-007, INTX-001 and CONTENT-003 describe adjacent ground, not coverage. The rejections were correct for the **Principle Pool**; they do not show the content is covered **elsewhere in DE**. [DOC]
4. **Non-failure is not absence of value.** Behavioural non-failure cannot show that the guidance is useless in untested contexts: existing projects, POLISH scope, repeated builds, or messier data. The main agent and the reviewer agree on this. It does show that no runtime value has been **demonstrated**, which is what an architectural change would need. [INF]

## 5. Reusable-knowledge assessment

The 11 B items consolidate into three units:

| Unit | Items | Value type | Generality | Evidence strength |
|---|---|---|---|---|
| **U1 Narrow-viewport reflow**: persistent side regions leave the flow or collapse at narrow widths; secondary regions stack after primary; nothing is silently lost; no document overflow | R1, R3, R4 | responsive/compositional, normative floor | High. It is also a public accessibility criterion (WCAG 2.x 1.4.10 Reflow), which DE does not currently name | Catalog: 1 rendered defect, 1 shipped-output, 1 rendered positive. DE: 4 of 5 comparable builds adapted; 1 isolated chart failure [MEAS] |
| **U2 View-state truthfulness**: selections, counts, marks, controls and helper text stay true of the set currently shown and the options actually open; a control or mark appears only when it is true or has an effect; stored state and live selection are distinct | R8, R9, R10, R12, R13, R15, R16 (+ user-visible half of R11) | interaction/state knowledge, with a comparison-honesty and conditional-form sub-part | Moderate to high across collection, form, comparison and linked-view UI. It is standard product-UI practice, not a new discovery | Catalog: code reading only, one product per sub-part, two defects [DOC]. DE: all assessable criteria in T2–T5 passed; one near-miss outside the criteria (card implied at zero charge) [MEAS] |
| **U3 Decision explanation**: explain a recommendation with the user's own values and name the deciding constraint | R6 | content/copy guidance | Moderate. It applies to recommenders, calculators and plan pickers | Catalog: code reading only, string templates, one product. DE: T6 passed 4 of 4; one near-miss on over-limit wording [MEAS] |

None of the three is a **distinct class of knowledge** that DE's existing forms cannot express. U1 is a layout/accessibility rule. U2 is interaction rules of the INTX kind. U3 is a content-copy rule. [INF, reviewer agrees]

Items outside DE (E): calculation consistency, single-source constants, shared validation functions, and derived data models. These belong to engineering practice, not to a design decision engine. R2 (F) would need a stated claim and more than one variant before it could be judged at all.

## 6. Runtime-destination analysis

| Unit | Principle Pool | Visual References | Rule Catalog | Enters without a second quality system? |
|---|---|---|---|---|
| U1 | **No** for the floor. It is prescriptive, and it would need to apply in POLISH, CRITIQUE and AUDIT, where the pool is never loaded (Contract §9). Only R4's keep-and-stack idea is EXPLORE-shaped, and it would need new evidence through Gates 1–3 | No | **Yes**: `layout-interaction.md` (LAYOUT-0xx) or `accessibility.md` as a WCAG 1.4.10 criterion, authored from the public standard as A11Y-001 is | Yes, as ordinary Rule Catalog authoring at P5/P7 |
| U2 | **No.** These are "state policy" and "correctness" content, which the pool's bar rightly excludes (catalog Phase 14 §8: lowering the bar "would turn the pool into a second rule catalog") | No | **Yes**: one or more INTX entries in `layout-interaction.md` (for example a "selected/linked" state beside INTX-001), with a form addendum beside A11Y-007 | Yes, if kept at P5. Must **not** inherit CONTENT-003's P1 status; `SKILL.md` §3 forbids adding "best practice" items to P1 |
| U3 | No | No | **Yes**: widen CONTENT-002's scope or add a CONTENT entry | Yes |

**Finding.** Every unit has a legitimate existing destination: the Rule Catalog. It is DE-governed, has its own record shape (category, layer, severity, applicability, evidence, freshness, validation, remediation), loads at T2 by category in every mode, and already takes rules from DE's own evidence (INTX-004 from a Phase 6.3 benchmark; A11Y-009 from the Phase 7 benchmark) and from public authorities (A11Y-001 from WCAG). [DOC] No unit needs a new pool, load event, stage or authority.

**The real constraint is provenance, not destination.** The Integration Contract defines a crossing for accepted PRINCIPLES only (§1, §13; §19 "Open Decisions: None"). `loop.md` §3 keeps the invariant "only accepted, identity-stripped principles cross, and only through Gates 1 to 3". `loop.md` §4 gates anything "derived from catalog material", in whatever form. A Rule Catalog entry **derived from these catalog observations** therefore cannot enter without a human gate and, if made a standing route, a Contract change. A Rule Catalog entry **authored from DE-native sources** (WCAG, DE benchmark failures, established public practice) is ordinary DE governance. [DOC → INF]

## 7. Case for and against a second knowledge path

**For** (the strongest form, raised by the reviewer as its main counter-argument):

- The architecture has one crossing and one consumption point. Useful, rule-shaped catalog knowledge (11 items) has no governed route, and DE's Rule Catalog is thin exactly where the residue sits: product-UI state and reflow. [DOC]
- The `loop.md` §4 taint rule ("If an idea traces to catalog material, it is gated whatever its form") may close even the DE-native route for these topics now that the audits have discussed them. Without a defined path, the knowledge could become unreachable. [INF]
- The behavioural tests used the conditions least likely to produce R9/R16-style defects (greenfield, full pipeline, fresh data), so "no failure" is weak comfort. [INF]

**Against:**

- The five conditions for a justified second path are **not met (0 of 5)**. Main agent and reviewer agree:

  | Condition | Result | Reason |
  |---|---|---|
  | (a) Not expressible through Principle Pool or Rule Catalog | **FAIL** | Every unit fits an existing Rule Catalog file and record shape (§6) |
  | (b) Legitimate runtime value | **FAIL (not demonstrated)** | 22 of 24 criteria passed without rules; the one failure did not replicate. Value is plausible but unmeasured |
  | (c) Sufficient evidence | **FAIL** | 12 of 16 items rest on code reading only and 1 on non-reproducible shipped output; each unit rests on a single product; parts rest on sample data and template judgement. This is weaker than the DE-run evidence behind existing rules |
  | (d) Clear authority and lifecycle | **FAIL** | None exists. The Contract has no non-principle crossing, and 10.2 §16 deferred it ("out of scope for this pool [DECISION]; they remain as external observations"). Rules are `status: permanent`, with no counterpart to catalog re-verification, staleness or deprecation. A lifecycle would have to be invented |
  | (e) No duplication or bypass | **FAIL** | It would give the Rule Catalog a second authoring authority beside DE's own. 10.2 §13 already rejected a "separate governed source with its own consumption path". It would also become the channel through which rejected principles re-enter as rules, which `loop.md` §4 names as the risk to guard against |

- **Anti-gaming (`loop.md` §15, milestone rule).** The residue is not a distinct class of knowledge. It is ordinary rule-shaped practice (responsive floors, state truthfulness, explanatory copy). Creating a path to give it a destination would be the prohibited move.
- **The taint concern is answered without a path.** These topics are widely documented public knowledge (WCAG 1.4.10; standard collection, form and comparison practice). DE can author rules from those sources and from its own evidence. Where origin is genuinely in doubt, a single human decision under `loop.md` §3/§4 resolves it. A standing crossing is not needed. [INF, reviewer agrees]

**Net:** the case against is decisive on current evidence.

## 8. Independent reviewer findings (`loop.md` §8)

One fresh, blind, read-only general-purpose reviewer. It received the question, the disposition model, the five-condition test, the 16 observation statements (with principle linkage and rejection reasons removed), the four prior reports, `loop.md`, the Integration Contract, 10.2 §13 and §16, and the DE runtime files. Withheld: the main agent's classifications and conclusions (frozen before the reviewer ran, SHA-256 `f6f47d30…a7d4c1`), the rejected PRINCIPLE records and their full rejection reasons, and catalog Phase 14. Disclosure: the prior reports necessarily summarize parts of the rejection history. They were supplied because the question requires reconciling them. The reviewer wrote no file and modified nothing.

Reviewer result: A 0, B 11, C 0, D 0, E 4, F 1. It found three units, consolidating U2 as "view-state truthfulness". Every unit's destination is the Rule Catalog. The second-path test scored 0 of 5. Recommendation: **CURRENT ARCHITECTURE SUFFICIENT**. It also identified the absence of WCAG 1.4.10 Reflow from DE, which the main agent then verified.

Disagreements and reconciliation:

| Item | Main agent (frozen draft) | Reviewer | Reconciliation |
|---|---|---|---|
| R2 | D (product-specific description) | F | **Reviewer adopted.** The observation states no claim and covers one variant, so it cannot be judged reusable or specific. Either letter gives the same outcome: no destination |
| R13 | C (contextual component feature) | B | **Reviewer adopted.** "A control appears only when it has an effect" generalizes beyond comparison tables and belongs to the U2 idea. Being common is not the same as insufficient generality |
| R15 | C (known technique) | B | **Reviewer adopted.** A known technique is not a contextual one: shared selection across linked views is general multi-view state knowledge (U2) |
| Units | six units (reflow, selection scope, forms, comparison honesty, explanation, state distinctness) | three units | **Reviewer adopted.** Selection, form, comparison and linked-view items share one idea; the finer split was presentation, not substance |
| Recommendation, destinations, five conditions | CURRENT ARCHITECTURE SUFFICIENT; Rule Catalog; not justified | identical | no disagreement |

All adopted changes moved items from C to B, which **strengthens** the case for a second path. The recommendation is unchanged, because B items still fit the existing Rule Catalog. No material disagreement remains.

## 9. Remaining uncertainty

- **Untested contexts.** Existing-project, POLISH, HARDEN-skipped and time-pressured runs; repeated builds for the non-reflow classes; secondary wide tables at phone width (B3 used a fixed-minimum-width scroll region). A failure there would justify a DE-native Rule Catalog entry. It would not justify a second catalog path.
- **Taint-rule interpretation.** Whether a DE-authored rule on a topic the catalog also observed "traces to catalog material" under `loop.md` §4 is not defined anywhere. This audit reads it as no, when the rule is authored from public or DE-run sources. That reading is an inference, not governance.
- **Remit boundary.** The E versus B line (for example R9, R11) is judgement. Both agents agree on it, but no governed text defines it.
- **Single model family.** Main agent and reviewer share it.
- **Catalog location.** As in the earlier audits, the catalog was resolved to its evident location; the location is not recorded here.

## 10. Explicit architectural recommendation

**CURRENT ARCHITECTURE SUFFICIENT.** [REC]

- Keep the single Principle crossing (Gates 1–3) and LAYOUT-010 as its only consumption point.
- Record the gap from the Reference Architecture Audit as **deliberate and adequate**. It is a provenance-route gap. The non-EXPLORE knowledge it concerns already has a governed home in the Rule Catalog, reachable from DE-native sources.
- Do not design a catalog → Rule Catalog crossing on the current residue.
- The R1–R16 observations remain catalog research material (`loop.md` §4).

Nothing is implemented by this milestone.

## 11. Proposed future milestone

**None is proposed.** No finding requires one.

If the human later wishes to test the only evidence that could change this conclusion, that would be a DE behavioural benchmark in existing-project or POLISH contexts for U1/U2. It would be a separately authorized milestone, and any resulting rule would be authored under DE governance, not through the catalog. This is recorded as information, not as a recommendation to proceed.

## 12. Files changed / files not changed

**Changed:**

- `benchmarks/residue-disposition-audit/RESIDUE-DISPOSITION-AUDIT-RESULTS.md` (added; this report).
- `STATE.md`: governance fields set to this milestone by explicit human authorization before execution; then operational fields only (Iteration, Status, Blockers, Pending human gate, Next action).

**Not changed:** `loop.md`; everything under `design-excellence/` (`SKILL.md`, the Rule Catalog, `principle-pool.md`, `visual-references.md`, and all other runtime knowledge); all other benchmarks, including the four prior reports; `rules.md`; `scratchpad/`; the Integration Contract; every catalog record, schema, config and report; the licensed reference library; the public-sector libraries. The frozen draft, extraction output and reviewer inputs are disposable material outside both repositories and are not committed.
