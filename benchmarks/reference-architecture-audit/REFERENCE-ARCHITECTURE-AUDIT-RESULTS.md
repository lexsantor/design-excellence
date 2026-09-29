# Reference Architecture Audit — Results

**Status:** COMPLETED. Hypothesis **PARTIALLY SUPPORTED**.
**Authorization:** AUTHORIZED FOR READ-ONLY AUDIT (`STATE.md`). Autonomous milestone under `loop.md`.
**Scope:** read-only. No file in the skill (`design-excellence/`), the Integration Contract, the external reference catalog or any reference library was changed. No reference was acquired or curated; no Principle Pool entry was created, promoted or exported.

**Labels.** **[DOC]** documented in a governed file or record. **[INF]** inference by this audit. **[UNK]** unknown.

Identity boundary: this report follows the Phase 10.7 Integration Contract §15. It names no source, vendor, product or marketplace, no path into the catalog or any library, and no catalog id other than PRN ids. Catalog documents are cited by phase and section only.

---

## 1. Objective

Determine whether the current architecture preserves and exposes the practical value of concrete references from the licensed reference library during design work independently of Principle Pool promotion.

## 2. Hypothesis

The current architecture may discard practical value from concrete references from the licensed reference library because only accepted, identity-stripped principles cross into Design Excellence runtime.

## 3. Evidence examined

Design Excellence (HEAD `99e8d9a`, read in full where governing):

- `SKILL.md` §1 (Visual Reference Evidence inside EXPLORE), §5 (Rejected Directions), §7 (progressive-disclosure table).
- `references/rule-catalog/layout-interaction.md` LAYOUT-010.
- `references/principle-pool.md` (header and both entries), `references/visual-references.md` (header, freshness), headers of `references/smoothui.md`, `references/kinetics.md`, `references/reicon.md`, `references/style-catalog.md`.
- `loop.md`, `STATE.md` (read completely; line counts 458 and 39 confirmed).

External reference catalog (read-only):

- Phase 10.7 Integration Contract, read completely (291 lines).
- Phase 10.2 architecture decision §2, §4, §12, §13, §15, §16.
- Catalog README; observation and principle schemas.
- All observation and principle records, tabulated by a read-only script: 26 observations, 7 principles (2 accepted, 5 rejected); product, artifact and evidence counts 8 / 9 / 61 (evidence types: 41 CODE, 16 RENDERED, 4 SHIPPED-OUTPUT).
- Phase 14 corpus gap analysis §1, §5, §9, §10.

Not opened: the licensed reference library, capture files, evidence records' excerpts, catalog Phases 15–19 beyond what earlier control-plane runs already recorded.

**Location note.** The human-supplied catalog location did not resolve as typed; the evident intended location, differing by one path separator, was used and was confirmed by the contract's content hash matching the version read in the previous governance run. Neither location is recorded in this repository.

## 4. Current architecture map

| Hop | What crosses | What stays behind | Basis |
|---|---|---|---|
| Licensed library → catalog | PRODUCT, ARTIFACT, EVIDENCE records; captures stored outside Git and referenced by hash | every library file | [DOC] catalog README; 10.2 §12 |
| Evidence → OBSERVATION | concrete, checkable facts (may name product, routes, values); positive and negative | nothing is abstracted yet; observations are never exported | [DOC] observation schema; 10.2 §12.2 |
| OBSERVATION → PRINCIPLE (Gate 1) | generalized `observed` facts, the abstraction, `do_not_apply_to`, `non_application_note`, trust signals | review records, provenance ids, rejection reasons (catalog-only) | [DOC] Contract §4, §13 |
| Accepted PRINCIPLE → DE (Gates 2, 3) | projection of the portable fields only, verbatim, PRN id as sole provenance | everything else | [DOC] Contract §4, §5, §11 |
| DE runtime | `principle-pool.md` at T3, only for DIRECT/DESIGN of a new visual system, only with `visual-references.md`, consumed only through LAYOUT-010 (at most 2–3 entries across both pools; "judged unnecessary" valid) | never used in CRITIQUE, AUDIT, component/section POLISH or implementation | [DOC] SKILL §1, §7; LAYOUT-010 |

Parallel channels with **no catalog relationship**: `visual-references.md` REF entries (authored under DE governance, own ceiling of 10), T4 implementation sources (component, motion, icon), `style-catalog.md`. [DOC] Contract §8.

## 5. Distinctions

| Kind | Where it lives | Reaches design work? |
|---|---|---|
| Source identity | catalog only | never (Contract §15) |
| Concrete design evidence (captures, code excerpts, measurements) | catalog only | never (10.2 §12.2) |
| Observations (concrete facts) | catalog only | only as generalized `observed` text inside an accepted principle |
| Abstract principles | catalog PRINCIPLE records | accepted ones only, via Gates 1–3 |
| DE runtime knowledge | `design-excellence/` | yes, per §7 load rules |
| Visual-reference abstractions (REF) | `visual-references.md` | yes, EXPLORE only; not catalog-derived |
| Implementation guidance | T4 files | yes, implementation stage; not catalog-derived |
| Examples | no channel | no: records are title-free; LAYOUT-010 forbids templates and "component recipes" |
| Provenance | PRN id only | carried, not resolvable from DE (valid state, Contract §5) |

## 6. Value preservation and loss points

Counts are over the 26 observations present. [DOC]

1. **Preserved.** All 26 observations, all 7 principles and every rejection reason remain in the catalog. The schema keeps rejection reasons so an abstraction is not re-proposed without new evidence.
2. **Abstracted.** 10 observations support the 2 accepted principles (dimensions: macrostructure 3, component-architecture 3, responsive-behavior 2, tokens 1, typography-in-use 1), including guard observations whose failure evidence crosses as `do_not_apply_to`.
3. **Discarded.** Nothing is deleted. At the DE boundary, 12 observations back only rejected principles (interaction-states 9, component-architecture 3).
4. **Inaccessible.** 16 of 26 observations (62%) have no route into DE: the 12 above plus 4 supporting no principle (responsive-behavior 3, composition 1). By design DE cannot read the catalog (Contract §3).
5. **Deliberately excluded by governance.** Identity, concrete evidence, measurements, tokens, typefaces and copy (Contract §4, §15); observations (10.2 §12.2); code-only implementation patterns, "out of scope for this pool [DECISION]; they remain as external observations" (10.2 §16).
6. **Potentially recoverable without violating the contract.** Only through the existing route: a principle, new or re-abstracted on new evidence, that passes Gates 1–3. The rule-catalog route recorded by catalog Phase 14 §9 is **not** an existing mechanism: the contract defines a crossing for principles only, and `loop.md` §4 gates any catalog-derived runtime knowledge. Phase 14 §9 assessed the rejected residue as: two plausible rule extensions (selection/filter policy; comparison honesty), one partly covered already (A11Y-001), and the rest insufficiently defined.

Additional finding [DOC → INF]: 10.2 §13.1 justified the catalog pool by a product-led coverage gap in the REF pool. Both accepted principles exclude product-led working views (PRN-0001 brand-led only; PRN-0003 brand-led/hybrid with working views in `do_not_apply_to`). The stated product-led motivation is so far unmet, and the product-led material (interaction states, component architecture) is exactly the material without a destination.

## 7. Legitimate mechanism today

Yes, one, and it is narrow. Concrete references influence design work only after abstraction: generalized facts in `observed`, concrete failures in `do_not_apply_to`, the copying boundary in `non_application_note`, and trust in `evidence_basis`/`support_breadth`. It acts at one point, LAYOUT-010 in DIRECT/EXPLORE of page/multi-page BUILD/REDESIGN. It exposes no identity, creates no runtime dependency, copies nothing, bypasses no gate and does not lower the admission bar. There is no second legitimate path: none for CRITIQUE, AUDIT, POLISH or implementation, and none for evidence-backed knowledge that is valid but not a materially different EXPLORE possibility.

## 8. Verdict

**PARTIALLY SUPPORTED.**

- **Supported:** only accepted, identity-stripped principles cross, and nothing else in the catalog can reach design work. 16 of 26 observations, and all of the interaction-state material, have no route into DE.
- **Not supported as worded:** "discard". Nothing is destroyed; concrete value partly crosses in abstracted form; and most of what stays out is deliberately excluded by ratified governance (identity, concrete evidence, examples) or judged by review to duplicate existing DE rules.
- **Architectural gap (evidence-backed):** the architecture has one admission route (Gates 1–3) and one consumption point (LAYOUT-010 in EXPLORE). Evidence-backed knowledge that is valid but not EXPLORE-shaped has no governed destination. 10.2 §16 recognized and deferred exactly this question; catalog Phase 14 §9 recorded candidates for it without a route. The gap is a missing governed path, not a defect in the existing path.
- **Constraints on any response to the gap:** no source identity; no runtime catalog dependency; no copying; no bypass of acceptance gates; no lowering of the admission bar; DE must behave identically without the catalog (10.2 §15.1); one-way, manual, reviewed export (Contract §11); Rule Catalog governance of its own; licence terms of the library unread (10.2 §15.3), which does not bite for abstract knowledge but would for anything more concrete.
- **Net practical size of the gap is unmeasured.** Rejection reasons cite existing entries (A11Y-001, A11Y-007, INTX-001, CONTENT-003); how much of the residue those already cover was not verified in this audit.

No implementation change is proposed. The gap is recorded, not solved.

## 9. Independent review (`loop.md` §8)

One fresh, read-only, blind general-purpose reviewer. It received the audit question, the hypothesis, the contract, 10.2 sections, the catalog README, schemas and records, and the DE runtime files. Withheld: the main agent's verdict, catalog Phase 11+ reports (curation and rejection history), and `loop.md`/`STATE.md` (closed-branch history). It modified no file.

Reviewer findings, summarized: same flow map; same counts (10 abstracted, 12 rejected-only, 4 no principle); one legitimate mechanism acting only at DIRECT/EXPLORE; a structural, evidence-backed gap for valid non-EXPLORE knowledge, recognized and deferred in 10.2 §16; the product-led expectation of 10.2 §13.1 unmet; verdict **PARTIALLY SUPPORTED**, with "discard" rejected as inaccurate. It flagged two catalog documentation inconsistencies (§11).

## 10. Disagreements and reconciliation

| Point | Main agent | Reviewer | Reconciliation |
|---|---|---|---|
| Verdict | supported with qualification | PARTIALLY SUPPORTED | agreed; the report uses PARTIALLY SUPPORTED |
| Counts and flow | as §4, §6 | identical | no disagreement |
| Recoverable value (f) | Gates 1–3 only; rule-catalog route exists only as a recorded, ungated proposal | Gates 1–3 only | consistent; the main agent's addition comes from Phase 14 §9, withheld from the reviewer, and does not change the conclusion |
| Product-led coverage | not initially weighted | raised | verified against `principle-pool.md` and adopted (§6) |
| Net size of gap | Phase 14 §9 gives a partial assessment | unmeasured | both hold: partial catalog-side assessment exists, coverage by existing DE rules is unverified |

No material disagreement remains.

## 11. Limitations

- Observation-level analysis only; evidence excerpts and captures were not opened, so "practical value" is judged from observation statements and review reasons, not from re-inspecting sources.
- Rejection reasons were read in part (first ~400–420 characters each) by both agents.
- Coverage of the rejected residue by existing DE rules was not verified.
- One reviewer, same model family: independent of the main agent's reasoning, not of the model.
- Catalog documentation drift noted by the reviewer, not acted on (outside scope): the catalog README and the principle schema's top-level description still describe portable provenance as observation ids, while Contract R4 makes the PRN id the only portable provenance; 10.2 §14.2 "accept writes to the pool" is superseded by Contract §13/§18.
- Pre-existing, outside scope: `benchmarks/phase-10.7/PHASE-10.7C-RESULTS.md` is tracked and names the source and a catalog location, contrary to Contract §3/§15. Not changed.

## 12. Files changed

- `benchmarks/reference-architecture-audit/REFERENCE-ARCHITECTURE-AUDIT-RESULTS.md` (added; this report).
- `STATE.md` (operational fields only: Iteration, Status, Blockers, Pending human gate, Next action).

## 13. Files not changed

`loop.md`; the governance fields of `STATE.md`; everything under `design-excellence/` (including `SKILL.md`, `principle-pool.md`, `visual-references.md`, the Rule Catalog); all other benchmarks; `rules.md`; `scratchpad/`; the Integration Contract; every catalog record, schema, config and report; the licensed reference library; the public-sector libraries.

## 14. Next unresolved question

Should evidence-backed knowledge that is valid but not an EXPLORE possibility (interaction-state policy, component architecture, correctness residue) have a governed path into Design Excellence, and if so under which gate, given the constraints in §8? Or should the current single-route architecture be accepted as final, with that material remaining catalog-only research?

## 15. Next action (human authorization required)

This milestone does not choose. Options, unranked:

- **(a) Accept the current architecture.** Record the gap as deliberate; no further milestone on this question.
- **(b) Authorize a read-only follow-up** measuring how much of the rejected residue existing DE rules already cover (the unmeasured net size in §8), before any design decision.
- **(c) Authorize a governance-design milestone** for a second governed crossing (for example rule-level knowledge), which would touch the Integration Contract and the Rule Catalog and therefore needs explicit authorization at every gate.

Each requires explicit human authorization in `STATE.md` before any run.
