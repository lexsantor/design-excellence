# Rejected Residue Coverage Audit — Results

**Status:** COMPLETED. Hypothesis **REJECTED**.
**Authorization:** AUTHORIZED FOR READ-ONLY AUDIT (`STATE.md`, human-authorized 2026-09-26). Autonomous milestone under `loop.md`.
**Scope:** read-only. No file in the skill (`design-excellence/`), the Rule Catalog, the Principle Pool, the Integration Contract, the external reference catalog or any reference library was changed. No reference was acquired or curated; no principle was created or promoted; no integration path was designed.

**Labels.** **[DOC]** documented in a governed file or record. **[INF]** inference by this audit.

Identity boundary: this report follows the Phase 10.7 Integration Contract §15. It names no source, vendor, product or marketplace, no path, file name, route or measurement from any source, and no catalog id other than PRN ids. Residue items are labelled **R1–R16**: the 16 catalog observations that support no accepted principle, taken in ascending catalog id order. That ordering rule reproduces the set from the catalog without carrying its ids here.

---

## 1. Objective

Measure how much of the evidence-backed catalog residue that currently has no route into Design Excellence is already covered by existing Design Excellence rules and runtime knowledge.

## 2. Hypothesis

The apparent architectural gap may be materially smaller than the Reference Architecture Audit suggests because some rejected or otherwise non-exported knowledge is already covered by existing Design Excellence rules.

## 3. Evidence examined

- Starting evidence: `benchmarks/reference-architecture-audit/REFERENCE-ARCHITECTURE-AUDIT-RESULTS.md` (COMPLETED, closed).
- Residue set re-derived from the authoritative catalog records by a read-only script: 26 observations, 10 supporting the 2 accepted principles, **16 residue items** (12 backing only rejected principles, 4 backing none). Matches the prior audit exactly. [DOC]
- The 16 observation statements, polarity, dimension and limitations, read in full.
- Design Excellence runtime knowledge, read in full: Rule Catalog `layout-interaction.md`, `accessibility.md`, `content-copy.md`, `performance-hardening.md`, `color.md`; `visual-references.md` (REF-001, REF-006, REF-008 in full, others by header and entry list); `principle-pool.md` (both entries, including `do_not_apply_to`); `SKILL.md` §7, §9; searches of `SKILL.md`, `critique-protocol.md`, `anti-slop-registry.md`, `style-catalog.md`, `existing-project-safety.md` for responsive, overflow and composition coverage. The independent reviewer additionally read `typography.md`, `motion.md`, `anti-slop-registry.md`, `style-catalog.md` and `existing-project-safety.md` in full.
- Governing files verified unchanged by hash: `loop.md`, the Integration Contract.

Residue dimensions [DOC]: interaction-states 9, component-architecture 3, responsive-behavior 3, composition 1. Polarity: 3 negative (defects), 13 positive. Evidence: 12 code-reading only, 1 vendor-shipped output, 3 rendered.

## 4. Classification rule

- **CLEARLY COVERED:** an existing DE entry states a directive that, if followed, would produce the observed behaviour or prevent the observed defect.
- **PARTIALLY COVERED:** a DE entry's directive genuinely reaches part of the observation's transferable content.
- **NOT COVERED:** no DE entry's directive reaches it. Shared vocabulary or a rule in the same area is not coverage.
- **NOT ASSESSABLE:** no transferable claim to compare, or insufficient evidence.

Rejected principles and catalog rejection reasons were not used as coverage. Only knowledge present in DE counts.

## 5. Coverage map

| Item | Dimension | Transferable content (generalized) | Class | Nearest DE entry and why it does not reach |
|---|---|---|---|---|
| R1 (defect) | responsive | layout with no narrow-viewport adaptation: persistent side navigation stays in flow, page overflows, content clips and overlaps | NOT COVERED | LAYOUT-005 and HARDEN-003 fix other overflow causes; LAYOUT-004 would hide the overflow, not adapt the layout; no DE directive requires narrow-viewport reflow |
| R2 | composition | one editorial home composition: masthead, uneven lead row, main feed beside a narrower rail of mixed modules | NOT ASSESSABLE | descriptive, single variant, one viewport; no stated claim. Compared against REF-001 and LAYOUT-001, it is not covered either |
| R3 | responsive | persistent sidebar leaves the canvas below a breakpoint; header reduces to a menu control; secondary cards drop below the main list | NOT COVERED | INTX-003's "collapse to a menu" is a remedy for wrapping link labels only; nothing governs sidebar or column reflow |
| R4 | responsive | narrow view keeps every module, stacked below the main feed; cards change orientation; no overflow | NOT COVERED | PRN-0001 states the keep-every-part, stack-in-order logic, but its `do_not_apply_to` excludes "Sites whose value is the continuous scroll, such as feeds" and "Other pages of the same site"; it is also an optional EXPLORE input, not a rule |
| R5 | interaction | two forms of one calculation agree at shared inputs; the deeper form only narrows | NOT COVERED | CONTENT-001 keeps wording identical through a flow, not computed results |
| R6 | interaction | show the working with the user's own numbers and name what decided the recommendation | NOT COVERED | CONTENT-002's what/why/how formula is scoped to error, failure and empty states |
| R7 | component | shared limits duplicated across two screens; agreement kept only by comment | NOT COVERED | §9 Principle 5 governs DE's own rule files; Principle 11 is a 3+ reuse threshold |
| R8 | interaction | selection pruned to the filtered set, kept across pages; page reset and clamped on filter change; bulk bar only with a selection | NOT COVERED | INTX-001's eight states are per-component; INTX-002 governs recovery from destructive actions, not what a selection reaches |
| R9 (defect) | interaction | selection never reduced on filter change; hidden rows stay selected and counted | NOT COVERED | nothing would prevent it |
| R10 | interaction | a one-option choice replaced by a statement; fields shown only when relevant; payment form omitted when nothing is charged | NOT COVERED | A11Y-007 covers field-state rendering bugs; A11Y-001's redundant-entry criterion concerns information the user already entered, not options derived from other data |
| R11 | interaction | validation uses the same condition as display, but the two are written separately | NOT COVERED | nothing |
| R12 | component | comparison rows declare their kind; a win mark only with two or more columns and a unique best; ties unmarked; legend scopes marks to the compared set | NOT COVERED | CONTENT-003 names comparison rows but governs fabricated values only |
| R13 | interaction | "differences only" control carrying a count, shown only when matches exist; emptied groups lose their heading | NOT COVERED | nothing |
| R14 | component | one stored structure from which lists and counts are derived; overview reuses the component read-only | NOT COVERED | Principle 11 is a reuse threshold, not single-source derivation |
| R15 | interaction | one shared selection across a map and a list; second click clears; map sticky beside the list on wide screens | NOT COVERED | INTX-001 has no selected or linked state; REF-002 concerns scroll hierarchy |
| R16 (defect) | interaction | filter not passed to the linked view; helper text claims a highlight that cannot exist; one colour for a stored status and the live selection | NOT COVERED | REF-007 is an optional navigation reference, not a state-distinctness rule; CONTENT-003 does not govern inaccurate UI copy of this kind |

## 6. Measured coverage

| Class | Count | Share of 16 |
|---|---|---|
| Clearly covered | **0** | 0% |
| Partially covered | **0** | 0% |
| Not covered | **15** | 94% |
| Not assessable | **1** | 6% |

Of the 15 assessable items, **0 are covered in any degree**. The gap identified by the Reference Architecture Audit is not reduced by existing DE knowledge.

Remit split of the 15 uncovered items [INF, agreed by both agents]:

- **Within DE's remit (11):** responsive reflow (R1, R3, R4; R1 is a defect DE would not catch); collection state (R8, R9); conditional forms (R10, and the display half of R11); comparison display (R12, R13); linked views (R15, R16); recommendation explanation copy (R6).
- **Outside or borderline (4):** R5 (calculation business logic), R7 and R14 (single source of truth, data modelling), and the shared-function half of R11 (engineering).

All three negative observations (R1, R9, R16) fall inside the remit and record defects that no DE entry would prevent.

## 7. Additional finding: rejection-time coverage claims

Two catalog rejection reasons (PRN-0005, PRN-0006) stated or implied that the rejected content was already covered by, or sat on the ground of, DE entries, citing A11Y-001, A11Y-007, INTX-001 and CONTENT-003. Checked against the DE text, none of those entries' directives reaches the corresponding residue items (R10–R13). The rejections themselves rested on pool fit and material difference, which this audit does not revisit. The narrower point is factual: "already covered by DE" was not borne out by DE's text. [DOC: rejection reasons read in part, first ~420 characters each; DE entries read in full.]

## 8. Verdict

**REJECTED.** Existing DE rules and runtime knowledge cover none of the 16 residue items clearly and none partially. The apparent gap is not materially smaller than the Reference Architecture Audit indicated. Most of the uncovered material (11 items) is product-UI state logic and responsive reflow, which falls within a design skill's remit; DE's runtime knowledge concentrates on visual direction, anti-slop, accessibility floors, motion and specific CSS failure modes.

## 9. Independent review (`loop.md` §8)

One fresh, read-only, blind general-purpose reviewer. It received the coverage question, the four-class rule, the 16 observation records and the DE runtime files. Withheld: the main agent's classifications (recorded in disposable material before the reviewer ran), the principle records and their rejection reasons, catalog reports, earlier benchmark reports, and `loop.md`/`STATE.md`. It modified no file.

Reviewer result: 0 clearly covered, 0 partial, 16 not covered, 0 not assessable. It listed five items where it hesitated between two classes (R1, R2, R4, R6, R16) and resolved each to NOT COVERED with quoted reasons.

## 10. Disagreements and reconciliation

| Item | Main agent (provisional) | Reviewer | Reconciliation |
|---|---|---|---|
| R3 | PARTIAL (INTX-003 "collapse to a menu") | NOT COVERED | Reviewer adopted. INTX-003's directive fires only when link labels would wrap and would not produce the observed sidebar or column reflow; counting it was vocabulary overlap |
| R4 | PARTIAL (PRN-0001 narrow-frame clause) | NOT COVERED | Reviewer adopted, verified in `principle-pool.md`: PRN-0001's `do_not_apply_to` explicitly excludes feed-based sites and non-entry pages. The provisional call missed that exclusion |
| R2 | NOT ASSESSABLE | NOT COVERED (hesitated) | Main agent kept: the observation states no claim, so by §4's rule it is not assessable. Both agree nothing in DE covers it; the coverage measure is unaffected |
| all others | NOT COVERED | NOT COVERED | agreement |

Both provisional disagreements moved toward less coverage. No material disagreement remains: the headline measure (0 covered of 15 assessable) is identical under either agent's classification.

## 11. Limitations

- **Documented coverage only.** The audit measures what DE's files state, not what the model does. Several residue items were rejected from the pool as ordinary practice; a model may already apply some of them without a rule. Whether their absence causes actual design failures is unmeasured.
- 12 of 16 items rest on code reading only, one on vendor-shipped output; no behaviour was executed.
- Remit classification is judgment, agreed by both agents but not governed anywhere.
- Rejection reasons were read in part (§7).
- One reviewer, same model family.
- The human-supplied catalog location again differed from the actual one by one path separator; the location was resolved as in the previous audit and is not recorded here.

## 12. Files changed

- `benchmarks/rejected-residue-coverage-audit/REJECTED-RESIDUE-COVERAGE-AUDIT-RESULTS.md` (added; this report).
- `STATE.md`: governance fields set to this milestone by explicit human authorization before execution; then operational fields only (Iteration, Status, Blockers, Pending human gate, Next action).

## 13. Files not changed

`loop.md`; everything under `design-excellence/` (including `SKILL.md`, the Rule Catalog, `principle-pool.md`, `visual-references.md`); all other benchmarks, including the Reference Architecture Audit report; `rules.md`; `scratchpad/`; the Integration Contract; every catalog record, schema, config and report; the licensed reference library; the public-sector libraries.

## 14. Next unresolved question

The documented gap is real and unreduced. Does it matter in practice? That is: does DE actually produce the uncovered defects (for example no narrow-viewport reflow, or selection state inconsistent with filters) when building product UI? And if it does, where may the missing guidance legitimately come from: independently authored DE rules, or catalog-derived knowledge through a gate that does not yet exist? The second part is a governance question under the Integration Contract and `loop.md` §4.

## 15. Next action (human authorization required)

No milestone is authorized. Options, unranked:

- **(a) Accept the gap.** Record it; no further milestone.
- **(b) Authorize a behavioural benchmark.** Test whether DE fails on the in-remit uncovered classes (responsive reflow, collection state, conditional forms, comparison display, linked views) without adding any rule, to separate documented from behavioural gaps.
- **(c) Authorize a governance decision** on the permitted source for any future guidance in these classes (independent authoring vs a new catalog crossing gate), which touches the Integration Contract and requires explicit authorization at every gate.
