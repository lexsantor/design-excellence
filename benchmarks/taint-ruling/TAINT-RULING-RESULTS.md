# Taint Ruling: External Discovery vs. Governed Rule Provenance — Results

**Status:** COMPLETED. Ruling **CONDITIONAL**.
**Authorization:** AUTHORIZED FOR READ-ONLY GOVERNANCE ANALYSIS ONLY (`STATE.md`, human-authorized 2026-09-27).
**Not authorized, and not done:** Rule Authoring; any change to the Rule Catalog, `SKILL.md`, `loop.md` or the Integration Contract.
**Scope:** Design Excellence at HEAD `26d9d95`. Reading only, apart from this report and `STATE.md`'s operational fields.

**Labels.**
- **[TEXT]** existing governance wording, quoted.
- **[INT]** this milestone's interpretation of existing governance.
- **[CLAR]** recommended clarification. It is not made here; making it would be a `loop.md` §7 self-modification.
- **[CHANGE]** a conclusion that would require a future governance change.

Identity boundary: follows Integration Contract §15. No catalog id other than PRN ids is named.

---

## 1. Executive ruling

**CONDITIONAL.** The two provenance chains are treated differently:

| Chain | Ruling |
|---|---|
| **A** (catalog observation → topic → independent authoritative source establishes the norm → DE authors a native rule) | **Permitted** under current governance when four conditions hold (§11). It is subject only to the `loop.md` §2 human authorization that every rule addition already requires |
| **B** (catalog observation → abstraction or transformation → DE rule) | **Remains gated.** For the Rule Catalog it currently has **no route at all**: the Integration Contract defines a crossing for accepted principles only, so B would require a governance change [CHANGE] |

- **PROHIBITED is not supported by the text.** `loop.md` §4 is a gating clause ("without the relevant human gate"), not a ban, even for material that *is* catalog-derived.
- **PERMITTED alone is not safe.** "Independently grounded" is not testable enough to stop laundering (§8).

**U1a** (WCAG 2.2 SC 1.4.10 Reflow) meets all four conditions. It is therefore **unblocked for a future, separately authorized Rule Authoring milestone**. It is **not authored** by this milestone (§13).

**Governance text is sufficient for a defensible ruling but not self-evident.** The key terms ("derived from", "traces to", "the relevant human gate") are undefined, so the ruling rests on interpretation. A clarification is recommended (§12). No governance change is needed for U1a.

## 2. Exact governance question

Does `loop.md` §4 prohibit a DE rule from being authored from an independent authoritative source when the rule's *topic* was originally surfaced by external catalog observations?

Sub-questions:
- Is chain A permitted while chain B stays gated?
- Under what minimum conditions?
- Does the answer hold for U1a?

## 3. Relevant existing governance

| # | Source | Text [TEXT] |
|---|---|---|
| T1 | `loop.md` §4 | "A rejected catalog candidate, or anything derived from catalog material, MUST NOT be reintroduced into Design Excellence as a REF entry, principle, rule, or any other runtime knowledge without the relevant human gate (§2, §3)." · "Renaming, rewriting, reclassifying, merging, or re-abstracting rejected material does not bypass the integration gate. If an idea traces to catalog material, it is gated whatever its form." · "Rejecting a candidate as a Principle does NOT necessarily make the underlying source useless as research material. It stays in the catalog and may inform catalog research." · "If it fails Principle admission, where does it remain useful, without crossing the gate?" |
| T2 | `loop.md` §2 | STOP for human authorization before "adding, replacing, removing, or changing the meaning of any runtime knowledge in `design-excellence/` (… rules …)" and before "introducing a new permanent external source family" |
| T3 | `loop.md` §3 | Human authorization for "allowing catalog observations, evidence, captures, or products to cross into Design Excellence". Invariant: "only accepted, identity-stripped principles cross, and only through Gates 1 to 3" |
| T4 | Integration Contract §4 | Never portable, "in any field, including free text": "unaccepted principles (draft, proposed, rejected, deprecated) and any principle failing Gate 2", together with source identity, raw source material, measurements and catalog ids |
| T5 | Integration Contract §15 | "Only independently written abstract principles cross." |
| T6 | Integration Contract §3 | DE "must behave identically on a machine with neither" the catalog nor the raw library; the catalog "produces portable knowledge. DE consumes a static copy" |
| T7 | Integration Contract §1, §8, §11, §13 | The crossing is defined for "an accepted PRINCIPLE" only; "A principle is not a rule" |
| T8 | Catalog 10.2 §16 | code-only implementation patterns are "out of scope for this pool [DECISION]; they remain as external observations" |
| T9 | Rule Catalog precedent | A11Y-001 freshness: "source: WCAG 2.2 spec (external authority, not one of the six extracted sources — cite the spec directly…)"; A11Y-005, A11Y-006 cite WCAG 2.2 AA; A11Y-009 and INTX-004 cite DE's own benchmark failures |
| T10 | `loop.md` §15 | "Do not convert a known pattern into a principle merely by changing its wording." "Do not invent novelty, evidence, applicability…" |
| T11 | `SKILL.md` §3, §9.5 | P1 is narrow and enumerated; "One rule, one place" |

Consequences read directly from the text:
- Every rule addition already passes a human gate (T2).
- §4 names two gates, "§2, §3". Only §3 adds anything beyond T2.
- For rules, §3 plus the Contract (T3, T7) currently provide no route.

## 4. Discovery vs derivation analysis

- **[INT] Discovery is not derivation.** Every verb §4 uses to extend the taint ("renaming, rewriting, reclassifying, merging, or re-abstracting") transforms *content*. None describes becoming aware of a topic. "Derived from catalog material" and "whatever its form" both presuppose that catalog content is carried into the result.
- **[INT] The "idea" of a rule is its normative content.** That content comes from its norm, scope, thresholds and exceptions. "If an idea traces to catalog material" is therefore read as: the rule's normative content traces to catalog material. It does not mean "the rule's topic was once observed in the catalog".
- **[INT] Counterfactual test.** Could every clause of the rule be written and justified exactly as it stands if the catalog had never existed? If yes, the catalog's role was discovery. If any clause could only be written from catalog material, that clause is derived.
- **[INT] A topic-level reading conflicts with the rest of governance:**
  - It would make taint depend on who looked first, not on what crosses. §3 and the Contract protect against content and identity crossing, not topics.
  - It contradicts T1's own statement that rejected material "may inform catalog research" and the §4 question "where does it remain useful, without crossing the gate?".
  - It inverts the dependency direction of T6: DE's rule evolution would become a function of the catalog's research breadth.

## 5. Evidence vs provenance analysis

- **[INT] Provenance attaches to content, not to topics.** A topic can appear both in catalog observations and in a pre-existing public standard without the standard becoming catalog-derived. WCAG 2.2 SC 1.4.10 exists, is normative and is citable independently of the catalog and of anything DE did.
- **[INT] Caveat: application can be derived even when the citation is independent.** If catalog material shapes how a standard is applied (which specifics, which exceptions, which examples), those parts are derived even though the headline citation is independent. That is why condition C2 (§11) exists.
- **[INT] What makes a source independent enough.** No general whitelist is supported by governance. By existing precedent (T9), a source qualifies when:
  - (a) its content exists independently of the catalog and its products;
  - (b) it is normative (a published standard's own text), or it measures DE's own behaviour;
  - (c) it can be checked by citation;
  - (d) its family is already admitted to the Rule Catalog. W3C/WCAG is admitted by A11Y-001, A11Y-005 and A11Y-006, and DE benchmarks by A11Y-009 and INTX-004. A family not yet admitted goes through T2's "new permanent external source family" gate.
- **[INT] DE benchmarks whose criteria were written from catalog residue** (as the Behavioural Residue Benchmark's were) can show that DE has a failure. They cannot supply the norm, because the norm would then be the catalog criterion restated. This is interpretation, and it is the point most likely to over-block (§12).
- **[INT] DE-native with an external norm.** A rule can be DE-native when its normative source is external but its layer, applicability, validation, remediation and freshness are set under DE governance. A11Y-001 is exactly this model. "DE-native" means authored and governed by DE and independently written (T5's own wording), not that the norm originated in DE.

## 6. U1a provenance analysis

- **History.** Catalog observations (the three responsive residue items) were consolidated into unit U1. The WCAG gap was identified while seeking authority for that unit. U1a is the split of U1 whose content is WCAG's. U1b (a DE-stricter bar) and U1c (composition prescriptions) were separated out as B and D because their content is not WCAG's. [TEXT, prior reports]
- **Rejection integrity.** The responsive residue items back **no** principle, accepted or rejected. U1a therefore has no rejected-principle lineage. [TEXT, Reference Architecture Audit §6; Rejected Residue Coverage Audit §5]

Clause-by-clause trace of the proposed entry (Rule Candidate Evaluation §12):

| Clause | Supported by | Catalog content? | Result |
|---|---|---|---|
| principle: 320 CSS px; 256 px height clause; no loss of information or function; no two-dimensional scrolling; listed 2D exemptions; "does not require a single column" | WCAG 2.2 SC 1.4.10 and its Understanding text, verified against W3C in the Rule Candidate Evaluation | none | pass |
| principle: page as a whole never scrolls horizontally; nothing silently clipped | follows from "without requiring scrolling in two dimensions" and "without loss of information" | none | pass |
| applicability: always-on across layout-touching/evaluating modes | DE authority over its own modes (`SKILL.md` §1, §7) | none | pass |
| exceptions: WCAG 2D list; keyboard reach | WCAG; A11Y-002 | none | pass |
| exceptions: "identifiable as scrollable" | defensible under "without loss of information", but no explicit citation | none | pass, **authoring must record this basis or drop the phrase** |
| evidence: WCAG; DE harness and root-clip hazard | WCAG; measurements of DE's own output | none; states no catalog evidence | pass |
| freshness | A11Y-001 precedent | none | pass |
| validation | derived from the standard plus DE-native harness lessons | none | pass |
| remediation: fluid tracks, `min-width: 0`, no clip masking | LAYOUT-005, HARDEN-003, LAYOUT-004 | none | pass |
| remediation: side regions leave the flow or collapse behind a control | existing DE entry INTX-003 ("collapse to a menu") | close to catalog observations; D as a mandate (U1c) | pass **only as an option**; turning it into a directive would re-import U1c |
| layer P5, severity major | `SKILL.md` §3; A11Y-005 and A11Y-008 precedent | none | pass |

**Verdict [INT]:** U1a's provenance is chain A. The catalog's role was discovery only.

## 7. Rejection-integrity test

Invariant: rejected catalog-derived principles cannot bypass Gates 1–3 by being rewritten as rules.

- **Held by existing text.** T4 bars unaccepted principles "in any field, including free text". T1 bars reshaping them ("rewriting, reclassifying, merging, or re-abstracting"). T3 and T7 give catalog content no route into the Rule Catalog. [TEXT]
- **Held by the ruling.** Condition C3 (§11) makes reproducing a rejected or unaccepted principle's normative content, in any wording, a disqualifier from chain A, which sends it to chain B. Chain B has no route to the Rule Catalog. Conditions C1 and C2 stop a generic citation carrying that content in at a higher specificity than the source. [INT]
- **Engagement in practice.** Rejection integrity is directly engaged for all of U2: its 12 interaction-state and component observations back only rejected principles. It is not engaged for U1a. [TEXT, prior reports]

## 8. Anti-gaming test

**Loophole to test:** catalog observation → cite a generic public standard → rewrite the rejected observation → insert it into the Rule Catalog.

| Case | Attempt | Result under the conditions |
|---|---|---|
| U2(a) selection scope | cite generic "visibility of system status" advice, or WCAG 3.3.x | **Blocked.** No independent source states "a selection's reach across filter and paging; hidden items never silently stay selected" (fails C2). The content matches the rejected PRN-0004 abstraction (fails C3). The residue-designed DE benchmark cannot supply the norm and passed anyway |
| U2(e) comparison marks | cite CONTENT-003 or a generic "do not mislead" norm | **Blocked.** No standard supports "best mark only with two or more items and a unique best; ties as ties" (fails C2). Borrowing CONTENT-003 would also contaminate P1. The content matches the rejected PRN-0006 abstraction (fails C3). A generic rule stripped of the specifics adds nothing (T10) |
| U2(h) selected vs status colour | cite WCAG 1.4.1 Use of Color | **Split correctly.** A general "not by colour alone" rule at 1.4.1's own specificity passes C1–C3 and is permitted, even though a catalog defect observation surfaced it. "Stored status and live selection must use distinct encodings" goes beyond 1.4.1, which requires a non-colour means, not distinctness between two states. That clause fails C2 and stays gated |
| U2(d) conditional forms | cite A11Y-001's redundant-entry (WCAG 3.3.7) | **Blocked.** Redundant entry concerns information the user already entered. "A hidden field is never required" and "no payment form when nothing is due" have no source at that specificity (fail C2) and match the rejected PRN-0005 abstraction (fail C3) |

The loophole does not open. C2 (specificity) and C3 (no rejected content in any wording) are the conditions that close it.

**Opposite failure** (blocking legitimate standards). Under a topic-level reading:
- WCAG 1.4.10 and 1.4.1 are both broadly applicable and both absent from DE. They would be frozen permanently because a catalog observation looked at them first, even though A11Y-001 already adopts WCAG 2.2 as an authority and DE could have added either at any time without the catalog.
- The catalog's observations span layout, responsive, component, token and typography dimensions, so taint would spread across much of the Rule Catalog's future. [INT]

The CONDITIONAL ruling avoids this: the standard's own criteria pass; only catalog-shaped specifics are held back.

## 9. Independent reviewer findings (`loop.md` §8)

One fresh, blind, read-only general-purpose reviewer. It received the governance question, the two chains, the decision model, `loop.md`, `STATE.md`, the full Integration Contract, 10.2 §12, §13 and §16, `SKILL.md` §3 and §9, the Rule Catalog, and the four relevant reports. Withheld: the main agent's ruling and conditions, frozen and hashed before the reviewer ran (SHA-256 `9a105dbf…a410ba535`). It modified no file.

Reviewer result: **CONDITIONAL**, with four minimum conditions:
- clause-level independent support;
- specificity match;
- no carriage of catalog content;
- disclosed human authorization.

It found U1a meets all four and is unblocked for a future authorized authoring milestone. Chain B has no Rule Catalog route and would need a governance change. PROHIBITED has no textual support. It recommended a clarification of §4 and listed five points where the text is insufficient.

Reconciliation:

| Point | Main agent (frozen) | Reviewer | Reconciliation |
|---|---|---|---|
| Ruling | CONDITIONAL | CONDITIONAL | agreed |
| Norm test | "subtraction" test: delete catalog material and the rule text is unchanged | **specificity match:** no clause more specific than its supporting source | **Reviewer's C2 adopted.** It is sharper and directly testable. The subtraction test survives as the counterfactual in §4 |
| Admissible support | independent source or DE benchmark failures | also existing DE entries | **Adopted.** Remediation clauses legitimately rest on existing entries (for example INTX-003, LAYOUT-005) |
| Rejected-principle equivalence | separate condition (C4) | folded into "no carriage of catalog content" | **Merged into C3**, with the explicit words "normative content … in any wording" kept from the main draft |
| Human gate | §2 authorization recording the checks | §2 authorization with **disclosure** of catalog surfacing, rejected-principle overlap and the clause trace | **Reviewer's C4 adopted** (disclosure is the substantive protection) |
| Residue-designed DE benchmarks | not addressed | may show failure, not the norm | **Adopted as [INT]**, flagged as the likeliest over-block (§12) |
| "Identifiable as scrollable"; remediation as option only | not addressed | authoring notes | **Adopted** (§6) |

No unreconciled disagreement remains.

## 10. Final ruling

**CONDITIONAL.** [INT, grounded in T1–T11]

- **Chain A** is permitted when conditions C1–C4 (§11) all hold. The only gate is the `loop.md` §2 human authorization that every rule addition already requires. The §3 crossing gate is not engaged, because no catalog content crosses.
- **Chain B** remains gated. For the Rule Catalog it has no route under the current Integration Contract (principles only). Enabling it would require changing Contract §1, §4, §11 and §13 and the `loop.md` §3 invariant [CHANGE]. This ruling does not recommend that.
- **A mixed case is split clause by clause.** A candidate that fails any condition for some clause is not a chain A candidate for that clause. The clause is dropped or treated as chain B.

## 11. Conditions

All four are required, applied **clause by clause** to the proposed entry: principle, applicability, exceptions, thresholds, examples, validation and remediation.

- **C1. Independent support.** Every normative clause is supported by one of:
  - (a) the text of an independent authoritative source, meaning a source whose content exists independently of the catalog, is normative, is citable, and belongs to a family already admitted to the Rule Catalog or admitted through the §2 source-family gate;
  - (b) DE-native evidence measuring DE's own behaviour; or
  - (c) an existing DE entry.

  Catalog material counts for nothing. It is context only.
- **C2. Specificity match.** No clause is more specific than its supporting source. Specifics beyond the independent source must come from DE-native evidence whose criteria were not written from catalog material. Otherwise the clause is derived and falls under chain B.
- **C3. No carriage of catalog content.** The entry carries no catalog observation, evidence, identifier, or catalog-specific formulation. It must not reproduce the **normative content of a rejected or unaccepted principle, in any wording** (Contract §4 "in any field, including free text"; `loop.md` §4 "rewriting … re-abstracting").
- **C4. Disclosed human authorization.** The `loop.md` §2 authorization request states:
  - that the topic was surfaced by catalog material;
  - any overlap with rejected principles;
  - the C1–C3 clause trace.

  The authoring milestone's §8 reviewer checks that trace. The trace lives in the authoring report, never in the runtime entry, because of the identity boundary.

No other condition is added. Each condition closes a specific failure: C1 closes catalog-only support, C2 closes generic-citation laundering, C3 closes rejected-content re-entry, and C4 closes an uninformed human gate.

## 12. Explicit implications for future Rule Authoring

1. **U1a is eligible** for a Rule Authoring milestone if the human separately authorizes one. That milestone must:
   - include the C4 disclosure and clause trace;
   - re-verify the WCAG quotations against W3C;
   - keep "side regions leave the flow or collapse" as a remediation option, never a directive;
   - record the basis for "identifiable as scrollable" or drop it;
   - decide separately, each under its own §2 authorization, whether to list the rule in `critique-protocol.md` Level 1, whether to add a `layout-interaction.md` pointer, and whether 320 CSS px becomes the definition of INTX-003's and TYPE-006's "required floor widths" (which changes their meaning).
2. **U2** candidates (a), (d) and (e), and the selected-vs-status clause of (h), remain **blocked** as chain A. No independent source reaches their specificity, and all of U2 overlaps rejected principles. They could enter only through DE-native failures found with criteria not written from catalog material, or through a chain B route that does not exist.
3. **A general WCAG 1.4.1 "Use of Color" rule is eligible** for evaluation as chain A, at 1.4.1's own specificity. This is recorded only; no such candidate was evaluated.
4. **Repeatability.** Future cases apply C1–C4 clause by clause and record the trace. The topic-origin question does not need reopening.
5. **Recommended clarification [CLAR]** (not made; a `loop.md` §7 change needing human authorization). Add to `loop.md` §4:

   > "Learning of a topic through catalog material is not derivation. Content is derived when any normative clause is supported only by catalog material or is more specific than its independent support. A rule whose every clause is supported by an independent authoritative source, DE-native evidence or existing DE entries, and which carries no catalog content or rejected-principle content in any wording, is DE-native and subject only to §2, with disclosure of the catalog surfacing."

6. **Where current text is genuinely insufficient** (recorded, not resolved by changing governance):
   - "derived from" and "traces to" are undefined;
   - "the relevant human gate (§2, §3)" does not say which gate applies when;
   - the Rule Catalog has no mandatory provenance or source field, so independence criteria exist only by precedent;
   - the status of DE benchmarks designed from catalog residue is undefined; this ruling limits them to evidence of failure, which may over-block;
   - chain B for rules would need a Contract change [CHANGE].

## 13. U1a is NOT authored by this milestone

No rule was written or changed. The following were not touched:
- `accessibility.md`, `layout-interaction.md` and every other Rule Catalog file;
- `critique-protocol.md`;
- `SKILL.md`;
- INTX-003 and TYPE-006.

"Unblocked" means only that the taint question no longer blocks U1a. Authoring it still requires a separate, explicit human authorization under `loop.md` §2. No milestone is authorized after this one.

## 14. Files changed / files not changed

**Changed:**
- `benchmarks/taint-ruling/TAINT-RULING-RESULTS.md` (added; this report).
- `STATE.md`: governance fields set to this milestone by explicit human authorization before execution; then operational fields only (Iteration, Status, Blockers, Pending human gate, Next action).

**Not changed:**
- `loop.md`.
- The Integration Contract and every other catalog file.
- Everything under `design-excellence/`: `SKILL.md`, all Rule Catalog files, `critique-protocol.md`, `principle-pool.md`, `visual-references.md`.
- All other benchmarks and reports.
- `rules.md`; `scratchpad/`.

The frozen draft and reviewer material are disposable and are not committed.
