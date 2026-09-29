# Rule Candidate Evaluation — Results

**Status:** COMPLETED.
**Authorization:** AUTHORIZED FOR READ-ONLY EVALUATION ONLY (`STATE.md`, human-authorized 2026-09-27, Option 1). Rule Authoring and any Rule Catalog change are **not** authorized.
**Scope:** evaluation of Design Excellence at HEAD `451fe5a`. No file under `design-excellence/` was changed. No rule or principle was created, and no reference was acquired. The external catalog was not read in this milestone, and no behavioural benchmark was run.

**Labels.** **[DOC]** documented in a governed file or prior report. **[MEAS]** measured by a prior DE benchmark. **[STD]** public standard, verified against the W3C WCAG 2.2 Understanding documents this session. **[PRAC]** established practice. **[CAT]** catalog observation (context only; `loop.md` §4). **[INF]** inference. **[REC]** recommendation.

Identity boundary: follows Integration Contract §15. Residue items keep the labels R1–R16 from the earlier audits.

**Reading "A" in this report.** A means only that a candidate passed evaluation and may be **put to a separately authorized Rule Authoring milestone**. `loop.md` §2 requires human authorization before "adding … or changing the meaning of any runtime knowledge in `design-excellence/` (… rules …)". A does not authorize authoring.

---

## 1. Executive conclusion

| Candidate | Final classification |
|---|---|
| **U1 Narrow-viewport reflow** | Split into three parts: **U1a A (READY FOR RULE AUTHORING)**, U1b B, U1c D |
| **U2 View-state truthfulness** | **D as one rule**; split into eight sub-parts: (a), (d), (e), (h) B; (c), (f), (g) D; (b) E |
| **U3 Decision explanation** | **B** for non-failure explanation; **C** for over-limit / no-fit output (CONTENT-002) |

- **Only one candidate is ready: U1a**, a WCAG 2.2 SC 1.4.10 Reflow floor as an accessibility rule at **P5**, severity **major**. It rests on a public standard, as A11Y-001, A11Y-005 and A11Y-008 do. It is distinct from every existing rule. It carries a concrete DE-native validation hazard: root `overflow-x: clip`, which LAYOUT-004 itself recommends, lets a document-width check pass by construction. **No DE build has been observed failing it.** Its value is a verifiable floor across modes, not a behaviour correction.
- **U2 is not one rule.** "Truthfulness" is a value, not a checkable directive. Four sub-parts are rule-shaped but rest only on catalog context plus DE passes (13 of 13 assessable criteria). They need DE-native failures before authoring.
- **U3** is rule-shapeable in principle. Its only DE-evidenced part is already governed by CONTENT-002, and the rest has no demonstrated failure.
- **Subsequent milestone:** a Rule Authoring milestone is **justifiable for U1a only**, and only after a human ruling on the `loop.md` §4 taint question (§15). It is not authorized.

## 2. Governance/evidence basis

Read for this milestone:

- `loop.md`: §1–§4, §6–§9, §15–§17; §2 human-gate list verified.
- `STATE.md`.
- The Integration Contract: read in full in the previous milestone at SHA-256 `4611b171…71e56f1`. Not re-read: this milestone crosses nothing, and its relevant terms (§3 dependency direction, §8 "a principle is not a rule", §13 gates, §19 no open decisions) were already recorded. The contract has no rule crossing, so it grants no route for catalog-derived rules.
- `SKILL.md` §1 (including "Mechanical gating and capability honesty"), §3 (P0–P8 and the enumerated P1 list), §7 (T2 loading by category), and §9.
- The Rule Catalog: all seven category files, by heading index. `accessibility.md`, `layout-interaction.md`, `content-copy.md` and `performance-hardening.md` were read in full, plus the relevant `color.md` entries and `critique-protocol.md` Level 1.
- Prior reports: Residue Disposition Audit, Rejected Residue Coverage Audit, Behavioural Residue Benchmark, Responsive Reflow Replication.
- Public standards [STD], via W3C WCAG 2.2 Understanding pages:
  - **SC 1.4.10 Reflow (AA):** "Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for: Vertical scrolling content at a width equivalent to 320 CSS pixels; Horizontal scrolling content at a height equivalent to 256 CSS pixels. Except for parts of the content which require two-dimensional layout for usage or meaning."
    - Two-dimensional examples: "images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content".
    - Also: "Conforming to this success criterion doesn't mean all sections of content need to stack in a single column within smaller viewports."
  - **SC 1.4.1 Use of Color (A):** "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element."

Repository-level facts established in this milestone [DOC]:

- No DE file names SC 1.4.10, reflow as a requirement, or a 320 CSS px width.
- **INTX-003 and TYPE-006 both validate "at the required floor widths", but no DE file defines those widths.**
- No DE file names SC 1.4.1 or a "not by colour alone" requirement. (This is observed but out of scope; see §14.)

**Taint status (`loop.md` §4).** All three candidates were surfaced by the catalog-residue audit chain, and the behavioural benchmark's test classes were designed from the residue classes. The previous milestone's reading, that rules authored from public standards or DE-run evidence are not "derived from catalog material", is **inference, not governance**. The main agent and the reviewer agree. In this report, catalog observations [CAT] never count toward a candidate's evidence sufficiency.

## 3. Candidate evaluation framework

Each candidate is scored on the ten dimensions of the milestone brief: generality, normativity, distinctness, authority, applicability, evidence, validation, remediation, cost and failure mode.

Classes:

- **A** Ready for rule authoring
- **B** Needs more evidence
- **C** Duplicates existing guidance
- **D** Too vague / not rule-shaped
- **E** Outside DE

Critical dimensions for A: normativity, distinctness, authority, evidence from a DE-admissible source (a public standard or a DE benchmark), validation, and remediation. Catalog evidence alone never satisfies the evidence dimension. Cost and failure mode are weighed but are not vetoes when a public standard supplies the norm. This follows existing precedent: A11Y-001, A11Y-005 and A11Y-008 have no DE-failure evidence.

## 4. U1 — Narrow-viewport reflow

U1 mixes three different things. They are evaluated separately.

**U1a: the WCAG 1.4.10 floor.** No document-level two-dimensional scrolling at 320 CSS px; no loss of information or function; 2D content exempt within its own container.

| # | Dimension | Assessment |
|---|---|---|
| 1 | Generality | High: every browser-rendered layout |
| 2 | Normativity | Prescriptive; the text is supplied by the standard [STD] |
| 3 | Distinctness | Not covered. INTX-003's "collapse to a menu" fires only for wrapping labels. LAYOUT-004 prevents a scrollbar but does not adapt layout. LAYOUT-005 and HARDEN-003 cover specific overflow causes. A11Y-008 forbids disabling zoom but does not require reflow. A11Y-001 names four WCAG 2.2 criteria, not 1.4.10. PRN-0001 is EXPLORE-only and excludes these contexts [DOC] |
| 4 | Authority | **P5.** Not on the §3 enumerated P1 floors (contrast, focus-visible, keyboard operability, reduced motion). WCAG AA status does not raise it: A11Y-005 (AA) and A11Y-008 are P5 by the Phase 4 correction. It must **not** be folded into A11Y-001, which is P1 only because it matches "contrast" |
| 5 | Applicability | Every browser-rendered layout, in any Task Mode that touches or evaluates layout, including AUDIT/CRITIQUE of existing pages and POLISH of a touched area. **Exempt:** only WCAG's 2D content, and only that content, never the document around it. **Not required:** a single column; side-by-side regions may stay if they fit |
| 6 | Evidence | [STD] strong (SC 1.4.10, AA). [MEAS] no DE build has failed it: document overflow was 0 in all five comparable builds (behavioural T1 plus replication B1–B3), with 0 elements past the viewport outside scroll regions. The one earlier chart strip (C1.3, a labelled, focusable region) and B3's secondary table are **probably within the 2D exemption** [INF]. [MEAS] DE-native validation hazard: every replication build used root `overflow-x: clip`, "so R2 alone could pass by construction"; the behavioural harness also exempted all scroll containers and missed C1.3 until review. [PRAC] responsive design is ubiquitous. [CAT] R1, R3, R4: context only. [INF] DE builds were measured at 390 px, not 320 px, so behaviour at 320 is untested |
| 7 | Validation | Mechanical-countable and rendered, subject to `SKILL.md` §1 capability gating (`skipped — capability unavailable` otherwise), with a static fallback. Must check element bounds and scroll containers, not document width alone (§12) |
| 8 | Remediation | Concrete: fluid tracks and `min-width: 0`; side regions leave the flow or collapse; 2D content in a labelled, focusable container or a narrow alternative; never mask with root clip |
| 9 | Cost | Low (one entry). Behavioural gain is small, because priors already handle it at 390 px. The real additions are an explicit **320 px floor** (DE currently references undefined "required floor widths"), clip-proof validation, and coverage in AUDIT, CRITIQUE and existing-project work |
| 10 | Failure mode | A real, standard-defined failure class. **Not evidenced in DE behaviour**, so the behaviour-level benefit is speculative. The validation-masking hazard **is** evidenced |

**U1a: A (READY FOR RULE AUTHORING), subject to the taint ruling (§15).**

**Formulation (answer to the milestone's U1 question).** An **accessibility rule**, not a responsive-layout rule and not both: the norm comes from WCAG, and "one rule, one place" (§9.5) forbids two copies. Canonical entry in `accessibility.md`, always-on. An optional pointer id in `layout-interaction.md` would follow the A11Y-003 → MOTION-007 pointer pattern, because a responsive POLISH may load only the layout category (§7). Whether to add that pointer is an authoring decision.

How the rule handles the distinctions the brief asked for:

| Case | Treatment |
|---|---|
| Document overflow | Fail |
| Component-level horizontal scrolling | Allowed only for 2D-exempt content, contained, labelled and keyboard-reachable (A11Y-002) |
| Genuinely continuous/2D data surfaces | The exemption |
| Narrow-specific alternative representations | A remediation option, not a mandate |
| Silent clipping | Fail |

**No blanket "never scroll horizontally."**

**U1b: DE-stricter bar.** Primary visualizations and wide tables should reflow or use a narrow alternative rather than a fixed-minimum-width scroll strip, even where WCAG exempts them. There is no public authority for this. DE evidence: 1 of 4 primary-visualization builds (isolated, **not replicated**) and 1 secondary table not tested against that criterion. Validation would be judgement-bearing (the replication rubric's R6).

**U1b: B.** Smallest evidence is in §13.

**U1c: composition prescriptions.** Sidebar collapses to a menu; secondary regions stack after primary; every module is kept. WCAG explicitly does not require stacking. These are layout choices whose only source is [CAT] or PRN-0001, which excludes these contexts.

**U1c: D.** Not a floor, and taint-exposed.

## 5. U2 — View-state truthfulness

**As one rule: D.** Main agent and reviewer agree. The sub-parts differ in:
- **Validation method:** interaction script, form-submission test, recomputing marks against data, or visual-encoding inspection.
- **Category:** interaction, form, content, or colour/accessibility.
- **Evidence.**

A single "truthful UI" rule would have no observable validation.

Evidence common to all sub-parts:
- [CAT] code reading of one product per sub-part. Context only.
- [MEAS] 13 of 13 assessable criteria passed across Behavioural T2–T5 (greenfield page BUILD, full pipeline, n = 1 per class).
- [STD] none, except for (h).

| Sub-part | Normativity / distinctness | Authority | Validation / remediation | Evidence and failure mode | Class |
|---|---|---|---|---|---|
| (a) Selection scope: what a selection reaches across filter and paging; hidden items never stay selected silently; select-all scope explicit; count labels its scope | Prescriptive; no DE entry (INTX-001 has no selected state; INTX-002 is undo) | P5 | Scriptable: select, filter or page, then compare count, visible set and bulk-action target. Concrete remediation | [MEAS] C2.1–C2.4 passed; one non-verdict observation (off-page selections reported only as "N selected", mitigated by named confirmation and undo). Failure is speculative for DE | **B** |
| (b) Filtered sets: page reset and clamp on filter change | Logic correctness; the symptom (a false empty page) is a bug | – | – | [MEAS] C2.3 passed | **E** |
| (c) Counts as a standalone rule | "Counts must be correct" is engineering (E). The design part, scope labelling, belongs in (a). CONTENT-003 does not apply: a mis-derived count is not a fabricated number, and must not inherit P1 | – | – | – | **D** |
| (d) Conditional forms: fields only when relevant; a hidden field never required; no payment collection when nothing is due | Partly prescriptive; not in A11Y-007 (rendering bugs only) or A11Y-001's redundant-entry. "One-option choice shown as a statement" is a refinement, not rule-grade (D fragment) | P5 | "Hidden never required" is testable by submitting under each condition; the rest is judgement | [MEAS] C3.1–C3.3 passed; C3.4 not assessable; one near-miss (card preselected and "Paying by card" at €0, entry deferred) | **B** |
| (e) Comparison marks: a "best" mark only with 2+ items and a unique best; ties shown as ties; marks scoped to the compared set; correct better-direction | Prescriptive; CONTENT-003 covers only fabricated values. It must stay P5, **not** under CONTENT-003's P1 | P5 | Recompute marks from the data. Concrete remediation | [MEAS] C4.1–C4.5 passed | **B** |
| (f) Linked views: views must share selection and filter | Linking is a product/interaction choice, not a floor. The normative core ("a view presented as linked must not contradict the other's state") folds into (a) | – | – | [MEAS] C5.1–C5.2 passed | **D** |
| (g) Helper/status copy stays true after state changes | As framed, a generic truth claim; its sharp form overlaps (a), (d) and CONTENT-001 | – | – | [MEAS] C5.3 passed | **D** |
| (h) Selected state vs status encoding distinctness | Not really a U2 rule. The strongest form is WCAG 1.4.1 "not by colour alone" (absent from DE), plus a "selected/current" state in INTX-001's state list | P5 | Checkable: non-colour visual difference plus ARIA state attribute | [MEAS] C5.4 passed (ring vs fill). [STD] 1.4.1 verified this session | **B** (reframed; see §14) |

## 6. U3 — Decision explanation

| # | Dimension | Assessment |
|---|---|---|
| 1 | Generality | Moderate: recommenders, calculators, plan pickers, prioritizers. For prioritization or ranking the deciding logic may be opaque or inappropriate to reveal (for example fraud or credit scoring). Those exceptions are unmapped |
| 2 | Normativity | Can be stated prescriptively: when the UI outputs a derived choice, state the deciding input(s) in the user's own values and name the binding constraint |
| 3 | Distinctness | CONTENT-002 governs "error, failure and empty states". The only DE-evidenced shortfall (T6: an over-limit message not saying which input exceeds) is a failure state, **already governed by CONTENT-002** (what happened / why / how to fix). The non-failure explanation is not covered |
| 4 | Authority | P5 |
| 5 | Applicability | Only UIs that output a derived choice. Not trivially obvious choices, and not where disclosure of logic is inappropriate |
| 6 | Evidence | [MEAS] T6 passed 4 of 4, with the explanation copy already present unprompted. [STD] none. [PRAC] explanation of automated decisions is widely advised. [CAT] R6 context only |
| 7 | Validation | Mostly `self-critique-prompt`. A scripted check needs boundary inputs the agent invents |
| 8 | Remediation | A copy template; concrete enough |
| 9 | Cost | Largely duplicates model priors; risk of generic UX advice |
| 10 | Failure mode | Speculative in DE |

**U3: B** for the non-failure explanation (rule-shapeable, not evidenced). **C** for the over-limit / no-fit part (CONTENT-002).

Category, if ever adopted: `content-copy.md`, as a **scope widening of CONTENT-002** rather than a new id [INF, reviewer agrees].

## 7. Existing-rule overlap analysis

| Existing entry | What it governs | Overlap with candidates |
|---|---|---|
| INTX-003 | Clickable text never wraps; "collapse to a menu" as its last remedy; validates "at the required floor widths" | Adjacent to U1. It does not require reflow, and its floor width is undefined. U1a would supply a defined 320 px floor. Whether INTX-003 and TYPE-006 adopt it changes their meaning and is a separate authoring decision |
| TYPE-006 | Headline integrity at "required floor widths" | Same undefined floor |
| LAYOUT-004 | Root `overflow-x: clip`, not `hidden` | **Interaction hazard:** it hides overflow, and every replication build used it. U1a's validation must neutralise it. U1a does not contradict it (clip stays correct for sticky), but "clip is not a fix" belongs in U1a's remediation |
| LAYOUT-003 / LAYOUT-005 / HARDEN-003 | Query type; grid-track and flex overflow causes | Remediation techniques for U1a; no duplication |
| A11Y-001 | P1 contrast plus four named WCAG 2.2 criteria | Must not absorb U1a (P1 contamination) |
| A11Y-002 | Keyboard operability | Governs the keyboard reachability of exempt scroll containers; referenced, not restated |
| A11Y-007 | Form-field rendering-state bugs (P7) | Adjacent to U2(d); does not cover conditional requiredness |
| A11Y-008 | Never disable zoom (P5, critical) | Adjacent to U1a (zoom); distinct requirement |
| INTX-001 | 8 per-component states, no selected state | Adjacent to U2(a) and (h) |
| INTX-002 | Undo over confirm | Adjacent to U2(a) (bulk actions); distinct |
| CONTENT-001 | Vocabulary constant through a flow | Overlaps U2(g) |
| CONTENT-002 | Error/failure/empty formula | **Covers** U3's failure part |
| CONTENT-003 | P1 no fabricated data | Must not absorb U2(c) or (e) |

## 8. Authority/severity analysis

- **No candidate belongs at P1.** `SKILL.md` §3: "Do not add 'best practice' items to this list". WCAG status does not confer P1 (A11Y-005, A11Y-008 precedent).
- **U1a: P5, severity major.**
  - Critical (as A11Y-008 is) was considered and rejected. A11Y-008's failure is total for the affected user. Reflow failures range from minor to severe, and DE shows none. [INF; the reviewer hesitated here]
  - Always-on rather than conditional, because every browser-rendered layout has a narrow case.
- **B candidates** would be P5 (U2 a, d, e, h; U3), with severity to be set at authoring if ever evidenced.
- Level 1 critique (`critique-protocol.md` axis 5) lists specific always-on accessibility ids (A11Y-001, -002, -003, -004, -009). Adding U1a there is an authoring-time edit to a governed file, not implied by this evaluation.

## 9. Validation/remediation analysis

| Candidate | Validation observable? | Remediation concrete? |
|---|---|---|
| U1a | Yes: rendered element-bounds and scroll-container checks at 320 CSS px, clip neutralised; static fallback; capability-gated | Yes |
| U1b | Judgement-bearing (continuous surface? communicated? coherent?) | Partly |
| U1c | No floor to check | – |
| U2 umbrella | No | No |
| U2(a), (e) | Yes: interaction script; recompute marks | Yes |
| U2(d) | Partly: submission tests for requiredness | Yes for requiredness |
| U2(h) | Yes: non-colour difference plus ARIA state | Yes |
| U2(b), (c), (f), (g) | Engineering tests or none | – |
| U3 | Mostly self-critique-prompt | Template |

DE-native lesson for any reflow validation [MEAS]:
- Document width alone is insufficient under root clip.
- Scroll containers must be enumerated and classified, never blanket-exempted.

Both errors occurred in DE's own benchmark harnesses.

## 10. Independent reviewer findings (`loop.md` §8)

One fresh, blind, read-only general-purpose reviewer. It received the three candidates, the ten dimensions, the decision model, the WCAG 1.4.10 text, `loop.md`, `SKILL.md`, the full Rule Catalog, `critique-protocol.md` and the four reports. Withheld: the main agent's classifications, frozen and hashed before the reviewer ran (SHA-256 `2d27fd4a…aaf48209`). It changed no file and read nothing on the catalog drive.

Reviewer results:
- **U1:** split into U1a **A** (with a full draft), U1b **B**, U1c **D**. Accessibility rule, P5, major.
- **U2:** **D** as one rule; sub-parts (a), (d), (e), (h) B; (b) E; (c), (f), (g) D.
- **U3:** B, with the failure part C.

It also contributed:
- the "C1.3 and B3 are probably WCAG-exempt" finding;
- the WCAG 1.4.1 reframing of (h), which the main agent then verified;
- the note that authoring U1a would imply a separate `critique-protocol.md` edit;
- two warnings: U2 B labels may invite a benchmark hunt (`loop.md` §15), and U1a's A depends on the taint ruling.

Disagreements and reconciliation:

| Point | Main agent (frozen) | Reviewer | Reconciliation |
|---|---|---|---|
| U1 structure | one A candidate; "narrow alternative preferred, not mandated"; 2D-exempt scroll allowed | U1a A / U1b B / U1c D | **Reviewer adopted.** The substance was the same; the split makes the non-A parts explicit |
| U2(b) filtered sets, (c) counts | inside (a) | (b) E, (c) D standalone | **Reviewer adopted.** Pagination clamp and count correctness are logic correctness; scope labelling stays in (a) |
| U2(f) linked views | B (coherence) | D (linking mandate), core folds into (a) | **Reviewer adopted.** Linking is a product choice; the normative residue is already (a) |
| U2(h) | B as an INTX-001 addendum | B reframed as WCAG 1.4.1 | **Reviewer adopted and verified:** SC 1.4.1 text confirmed; absent from DE. Class unchanged |
| U3 | D (generic), failure part C | B, failure part C | **Reviewer adopted.** The reviewer showed a prescriptive, partly scriptable formulation, so "not rule-shaped" was too strong. It is unevidenced, not unshapeable. No evidence action is recommended (§13) |
| U1a severity, layer, placement, category | major, P5, always-on, `accessibility.md` | same (hesitated on critical) | no disagreement |

No unreconciled disagreement remains.

## 11. Final classification of every candidate

| Candidate | Class |
|---|---|
| U1a WCAG 1.4.10 reflow floor | **A** |
| U1b DE-stricter no-scroll-strip bar for primary visualizations and wide tables | **B** |
| U1c composition prescriptions (collapse, stack order, keep every module) | **D** |
| U2 as one rule ("view-state truthfulness") | **D** |
| U2(a) selection scope | **B** |
| U2(b) filtered-set pagination reset and clamp | **E** |
| U2(c) counts, standalone | **D** |
| U2(d) conditional forms (relevance, hidden never required, no payment when nothing due) | **B** |
| U2(e) comparison marks | **B** |
| U2(f) linked-view mandate | **D** |
| U2(g) helper/status copy truthfulness | **D** |
| U2(h) selected vs status distinctness (reframed as Use of Color) | **B** |
| U3 decision explanation, non-failure outputs | **B** |
| U3 over-limit / no-fit output | **C** (CONTENT-002) |

## 12. Proposed rule entries for A candidates only

**Not written into the Rule Catalog.** Proposal for a separately authorized authoring milestone.

```
### A11Y-0xx — Reflow at 320 CSS px (WCAG 2.2 SC 1.4.10)
- **category:** accessibility · **layer:** P5 (UX/usability — a WCAG AA criterion, but not one of the four accessibility floors on the `SKILL.md` §3 enumerated P1 list; kept P5 consistent with A11Y-005/A11Y-008 and the Phase 4 correction) · **severity:** major
- **principle:** at a viewport width equivalent to 320 CSS px, content is presented without loss of information or functionality and without requiring scrolling in two dimensions (for content that scrolls horizontally, the equivalent is a height of 256 CSS px). The page as a whole never requires horizontal scrolling. Parts of the content that require two-dimensional layout for usage or meaning — maps, diagrams and images required for understanding, video, games, presentations, data tables as a whole (not their individual cells), interfaces that must keep a toolbar in view while content is manipulated — may scroll in two dimensions within their own container; nothing else may. This does not require a single column: regions may stay side by side where they fit. Content is never silently clipped or pushed outside the usable viewport.
- **applicability:** always-on for every browser-rendered layout, in any Task Mode that creates, touches or evaluates layout (BUILD, REDESIGN, POLISH of the touched area, CRITIQUE, AUDIT). Distinct from `INTX-003` (label wrapping), `LAYOUT-005`/`HARDEN-003` (specific overflow causes) and `A11Y-008` (zoom must not be disabled).
- **exceptions:** only the two-dimensional content listed in the principle, and only that content, never the document around it. An exempt container must still be reachable and operable by keyboard (`A11Y-002`) and identifiable as scrollable. A narrow-specific alternative representation is always an acceptable substitute, never a requirement.
- **evidence:** public standard: WCAG 2.2 SC 1.4.10 Reflow (Level AA). DE-native: in DE's own benchmarks every responsive build applied a root `overflow-x: clip` (`LAYOUT-004`), which makes a document-width check pass by construction, and one benchmark harness exempted every scroll container and missed a fixed-width scroll strip until independent review — so validation must not rest on document width alone. No DE build has yet been observed failing this criterion; its value is a verifiable floor across modes, not a correction of observed behaviour.
- **freshness:** source: WCAG 2.2 spec (external authority — cite the spec directly, not this file). status: review_interval_days: 365.
- **validation:** mechanical-countable, rendered, subject to the capability gating in `SKILL.md` §1. At 320 CSS px width: (1) with any root `overflow-x: clip/hidden` neutralised for the check, `documentElement.scrollWidth ≤ clientWidth + 1`; (2) no rendered element lies wholly or partly beyond the viewport's horizontal bounds unless it is inside a scroll container; (3) every horizontal scroll container is listed and classified either as exempt (naming its two-dimensional content type) or as a FAIL — never blanket-exempted; (4) no element with `overflow: hidden/clip` clips text or controls (its scrollWidth > clientWidth); (5) primary navigation and every control available at desktop width remain reachable (collapsed menus opened). Without rendering capability: report `skipped — capability unavailable`, and statically flag fixed `width`/`min-width` above 320 px on non-exempt layout elements and a root clip used as the only overflow control.
- **remediation:** replace fixed widths with fluid ones (`minmax(0, 1fr)`, `min-width: 0`, `max-width: 100%`); let persistent side regions leave the flow or collapse behind a control; place exempt two-dimensional content in a labelled, keyboard-focusable scroll container or provide a narrow-specific alternative; never use `overflow: clip/hidden` to mask overflow — `LAYOUT-004` prevents the scrollbar, it does not fix the layout.
```

Authoring-time decisions this entry implies, **not decided here**:
1. Its id and position (always-on section).
2. Whether `critique-protocol.md` Level 1 axis 5 lists it.
3. Whether to add a pointer id in `layout-interaction.md`.
4. Whether 320 CSS px becomes the definition of "required floor widths" for INTX-003 and TYPE-006. That changes their meaning and needs its own `loop.md` §2 authorization.

## 13. Evidence required for B candidates only

A common condition applies (`loop.md` §15): these benchmarks should run only if a human wants the question answered. They are not to be run to manufacture failures. A zero-failure result closes the candidate.

| Candidate | Smallest future evidence |
|---|---|
| U1b | One frozen-criteria DE benchmark on **existing-project or POLISH** work with a wide table or chart at 320–390 px and an **unprimed** brief (no phone-use statement). Needs a repeated (≥ 2 of 3), independently reviewed, clearly unjustified fixed-width strip with measurable task loss (a required comparison not visible without two-direction scrolling) |
| U2(a), (d), (e) | One frozen-criteria DE benchmark in existing-project/POLISH contexts: add bulk actions to an existing filtered, paginated list; add a zero-charge path to an existing checkout; add tied values to an existing comparison. Needs repeated, reviewed failures that existing rules would not catch. Greenfield BUILD already passes 13 of 13 |
| U2(h) | No benchmark. The evidence is the verified public standard (SC 1.4.1). The open question is scope: whether a general "not by colour alone" accessibility candidate should be evaluated in its own right (§14). The selected-state addition to INTX-001 would follow from that evaluation |
| U3 (non-failure) | DE runs in which a recommendation or calculator output gives a name or number with no deciding reason, reproduced in ≥ 2 independent builds or existing-project contexts. **No evidence action is recommended:** T6 shows the behaviour is already present |

## 14. Explicit list of candidates rejected as C/D/E

- **C:** U3 over-limit / no-fit output. Governed by CONTENT-002.
- **D:**
  - U1c composition prescriptions;
  - U2 as one rule;
  - U2(c) counts standalone;
  - U2(f) linked-view mandate;
  - U2(g) helper/status copy truthfulness;
  - the "one-option choice shown as a statement" fragment of U2(d).
- **E:** U2(b) pagination reset and clamp. The earlier E items R5, R7, R11 and R14 stay outside DE.
- **Also not to become rules:**
  - a blanket "never scroll horizontally" rule;
  - any candidate at P1;
  - any candidate folded into A11Y-001 or CONTENT-003;
  - anything grounded only in catalog observations.

**Out-of-scope observation.** WCAG 2.2 SC 1.4.1 Use of Color (Level A) is absent from DE's Rule Catalog [DOC, STD]. It is not one of U1–U3 and is **not evaluated** here. It is recorded so a human can decide whether to open it as its own candidate.

## 15. Whether a subsequent Rule Authoring milestone is justified

**Justifiable for U1a only**, as a narrow, separately authorized milestone. It is **not authorized** by this evaluation (`loop.md` §2).

Two human decisions come first:

1. **Taint ruling (`loop.md` §4).** Decide whether a rule whose norm comes from a public standard (WCAG 1.4.10), with DE-native validation evidence, may be authored even though the catalog-residue audits surfaced its topic.
   - **If no:** U1a is blocked, and the correct outcome is no rule.
   - **If yes:** the ruling should be recorded in governance so the question does not recur per candidate.
2. **Authoring scope.** Decide whether the milestone also covers:
   - the `critique-protocol.md` Level 1 listing;
   - an optional `layout-interaction.md` pointer;
   - defining "required floor widths" for INTX-003 and TYPE-006, which changes their meaning.

**No milestone is justified for the B candidates** unless the human specifically wants the §13 questions answered. On current evidence (13 of 13 passes, and 0 of 3 replication for U1b) the expected result is no rule.

**Files changed:**
- `benchmarks/rule-candidate-evaluation/RULE-CANDIDATE-EVALUATION-RESULTS.md` (added; this report).
- `STATE.md`: governance fields set by explicit human authorization before execution; then operational fields only.

**Files not changed:**
- `loop.md`.
- Everything under `design-excellence/`: `SKILL.md`, all seven Rule Catalog files, `critique-protocol.md`, `principle-pool.md`, `visual-references.md`.
- All other benchmarks.
- `rules.md`; `scratchpad/`.
- The Integration Contract and the external catalog.

The frozen draft and reviewer material are disposable and are not committed.
