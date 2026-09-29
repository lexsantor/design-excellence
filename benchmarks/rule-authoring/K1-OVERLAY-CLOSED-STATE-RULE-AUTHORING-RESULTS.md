# Rule Authoring — K1 Overlay Closed-State Availability — Results

**Status:** COMPLETED.
**Rule:** `A11Y-012 — Closed overlays are unavailable to keyboard and assistive technologies`. It is canonical in `design-excellence/references/rule-catalog/accessibility.md`, in the Conditional section.
**Layer / severity / placement:** P5 · major · conditional (applies only when a dismissible overlay exists).
**Axis 5:** integrated as an explicitly conditional check; the axis 5 definition was adjusted in one sentence.
**Provenance:** DE-native. No catalog-derived normative support and no WCAG text.
**Independent review:** PASS. No blocking findings; 3 SHOULD-FIX and 6 MINOR adopted, 1 MINOR declined (§12).
**Parent commit:** `c24a6f0`.

Identity boundary: follows Integration Contract §15. No catalog path, record id other than PRN ids, or source material appears in this report.

---

## 1. Authorization

**Human authorization (2026-09-27), recorded in `STATE.md` before any change:**

> "Autorizo Rule Authoring: K1 Overlay Closed-State Availability. Scope limitado a convertir el candidato K1 documentado en el Rule Candidate Evaluation en una entrada del Rule Catalog, incluyendo su integración en Axis 5 como regla explícitamente condicional cuando exista un dismissible overlay, el ajuste estrictamente necesario de la definición de Axis 5 para permitir esta condición, su validación, provenance trace y el overlap check estrictamente necesario con reglas/principles existentes o rechazados. K1 debe permanecer P5, major y conditional, sin timing normativo ni prescripción de implementación. No autorizo cambios a K2, K3, K4, Principle Pool, Integration Contract, runtime architecture, adquisición de referencias, benchmarks nuevos ni cambios de arquitectura."

**Gate history.**
1. The first run found no authorization in `STATE.md` and stopped before changing anything.
2. That run also flagged two scope points. Axis 5 is defined as Always-on only, so it needed a definition change to hold a conditional entry. The overlap check needs read-only catalog access.
3. The human's authorization covers both points explicitly.

**`loop.md` §4 disclosure.** The candidate evaluation (§11, §14) records that K1's topic was surfaced by DE's own benchmarks, not by the catalog. The rejected-principle overlap check was left to this milestone; its result is in §9.

**Delegation.** One fresh, read-only, blind `loop.md` §8 reviewer, within the §9 cap.

## 2. Exact scope

- Author candidate K1 (`benchmarks/discovery/OVERLAY-FOCUS-RULE-CANDIDATE-EVALUATION-RESULTS.md` §7) as `A11Y-012`.
- Integrate it into `critique-protocol.md` axis 5 as a conditional check, adjusting the axis 5 definition only as far as strictly necessary.
- Write the validation, the provenance trace and the overlap check.
- Run the review, write this report, update `STATE.md` and make one local commit.

## 3. Explicit exclusions

Not done:
- K2 (background inert while open), K3 (behaviours 1–4) and K4 (an umbrella rule), in any form;
- the Principle Pool and the Integration Contract;
- runtime architecture, `SKILL.md` and `loop.md`;
- reference acquisition, including WCAG text;
- new benchmarks or fixtures;
- any other Rule Catalog entry;
- any change to rejected or accepted principles;
- push.

## 4. Candidate source and changes from the candidate

**Source:** the candidate evaluation §7 (the K1 proposition), §8 (layer), §9 (severity), §10 (validation) and §11 (provenance).

| Element | Change from the candidate | Reason |
|---|---|---|
| Principle | the §7 proposition, verbatim, plus one closing sentence: "The rule states an observable outcome only: it sets no timing value and requires no particular technique." | makes the evaluation's constraints part of the entry; the sentence adds no requirement |
| Applicability | written out from §7 and §8: dismissible overlays only; not inline disclosures or accordions; closed state only; no interface is required to contain an overlay; relationship to A11Y-002 and A11Y-009 | the evaluation's scope, stated in the entry. "Closed state only" keeps K2 and K3 out |
| Validation | §10 steps (1)–(5) with every §10 qualifier kept (open by keyboard; focus an element other than the first; close control activated by keyboard). Two changes: close paths are the ones "the overlay actually offers", and for script-driven exits the end of the exit may also be judged by the overlay's rendered state ceasing to change (reviewer SHOULD-FIX 2; still no fixed delay). The static fallback is marked "for review — not as a failure" | the brief's validation list (items 1–8), which matches §10. `getAnimations()` alone would stop sampling early for exits driven by scripts or timers |
| Remediation | §10's outcome wording, plus a pointer to existing `MOTION-005`/`MOTION-007` for the exit motion itself | a pointer, not a new requirement: motion stays governed where it already is |
| Evidence | §3, §4, §11 and §13 condensed, including §13's limits (only Escape probed during the exit, one engine, one implementation style). The overlap check is referenced to this report rather than described in the runtime entry | the disclosures the brief requires; candidate §14 item 6 carries §13 into `evidence:`; TR §11 C4 places the trace in the report |

No clause was strengthened or broadened beyond the candidate.

## 5. Final A11Y-012 rule

As authored in `accessibility.md`, after review:

### A11Y-012 — Closed overlays are unavailable to keyboard and assistive technologies
- **category:** accessibility · **layer:** P5 (UX/usability — a real accessibility defect, but not one of the four items on the `SKILL.md` §3 enumerated P1 list: its failure adds focus stops and exposure that should not exist, it does not make anything impossible to operate by keyboard, which is the test that keeps `A11Y-006` P1; kept P5, as `A11Y-004` and `A11Y-009` are)
- **principle:** when an overlay surface that is shown and dismissed (a drawer, sheet, off-canvas navigation panel or modal dialog) is closed, whether it was never opened or has been dismissed, none of its content can receive keyboard focus and none of it is exposed to assistive technologies. This holds from the moment the dismissal takes effect, including while any exit animation or transition is still running, until the overlay is opened again. The rule states an observable outcome only: it sets no timing value and requires no particular technique.
- **severity:** major
- **applicability:** only when the interface contains a dismissible overlay of the kinds named in the principle, in any Task Mode that creates, changes or evaluates one (BUILD, REDESIGN, POLISH of the touched overlay, CRITIQUE, AUDIT). It does not apply to inline disclosures or accordions that expand in place, and it requires no interface to contain an overlay. It governs the closed state only: focus handling while the overlay is open is not part of this rule. Distinct from `A11Y-002`, which requires interactive elements to be reachable and does not make closed content unreachable, and from `A11Y-009`, whose applicability presupposes closed overlays "represented accessibly and operably" without checking it; both still apply.
- **exceptions:** none once a dismissible overlay exists.
- **evidence:** DE-native only. `OVERLAY-FOCUS-COVERAGE-EXPANSION-RESULTS.md` (2026-09-27): in 1 of 3 off-canvas navigation builds routed without Level 2 — a custom drawer — the closed drawer's links stayed reachable by Shift+Tab and exposed in the accessibility tree while its exit transition ran after Escape; found by an independent evaluator, reproduced independently, and missed by the builder's own VALIDATE, which checked the settled state. The two native-dialog builds in that benchmark did not show it. This is the only independently verified failure. Supporting but weaker: Phase 7 Test 05 reported, about its own build with no retained artifact, drawers "only moved off-screen via `transform`, leaving their content focusable and AT-visible while 'closed'", caught in its own VALIDATE. An earlier benchmark's sheet used a similar delayed hide but was never probed during its exit, so it is not counted. No frequency is established. Limits: the exit window was probed through Escape only, in one browser engine (Chromium), on one implementation style (a class-toggled drawer). No WCAG or other external text was acquired for this rule; every clause rests on Design Excellence's own evidence or existing entries. Candidate record, clause trace and overlap check: `OVERLAY-FOCUS-RULE-CANDIDATE-EVALUATION-RESULTS.md` (K1) and `K1-OVERLAY-CLOSED-STATE-RULE-AUTHORING-RESULTS.md`.
- **freshness:** status: permanent.
- **validation:** mechanical-countable, subject to the capability gating in `SKILL.md` §1 — rendered, Enhanced mode only, with motion not reduced (reduced motion can shorten or remove the exit and hide the defect). For each dismissible overlay in scope: (1) before first open, a Tab sweep and a Shift+Tab sweep across the page never focus overlay content, and the accessibility tree exposes none of it; (2) open the overlay by keyboard and move focus to an element inside it other than the first; (3) close it once through each close path the overlay actually offers — Escape, its close control activated by keyboard, its backdrop or scrim, and its trigger where the trigger toggles; (4) immediately after each close, without waiting for any exit animation, press Shift+Tab and Tab several times each and sample `document.activeElement` after every press: no sample may be inside the overlay; (5) from the moment of dismissal until the overlay's own animations and transitions have finished — judged from the page (for example `getAnimations()` on the overlay or, where the exit is script-driven, until the overlay's rendered state stops changing), never from a fixed delay — sample the accessibility tree repeatedly: no sample may expose overlay content; (6) after it settles, repeat (1); then repeat (2)–(5) on a second open/close cycle. PASS only if every sample holds. A probe that waits for the close to settle before checking passes a build that fails; do not rely on it. Without rendering capability: report `skipped — capability unavailable`, and statically flag for review — not as a failure — any overlay whose closed state takes effect after a delay, or only through position or opacity, with nothing removing its content from focus and from the accessibility tree at the moment of dismissal.
- **remediation:** make the overlay's content unavailable to keyboard focus and to assistive technologies at the moment of dismissal, independent of how long the visual exit lasts, and keep it unavailable until the overlay is opened again. Any technique that achieves this outcome is acceptable; keep the exit motion itself within `motion.md` (`MOTION-005`, `MOTION-007`).

## 6. Rule location

- **Placement:** `accessibility.md`, Conditional section, after A11Y-008. It is the next unused id, since A11Y-001 to A11Y-011 already exist.
- **Why Conditional.** It follows A11Y-005, -006 and -007: the rule is scoped to an interaction that may be absent.
- **No pointer entries elsewhere.** `smoothui.md` l.92 lists an accessibility floor for adopted components (A11Y-002, -005, -007, -008). Adding A11Y-012 there is not strictly necessary: that list is a quick check, and adopted overlays remain governed by the whole Rule Catalog (`smoothui.md` l.68, "Governed entirely by the existing rule catalog"). It was left unchanged, and the question is recorded in §15.

## 7. Authority, layer and severity

- **P5.** `SKILL.md` §3 enumerates the only P1 accessibility floors and says "Do not add 'best practice' items to this list".
  - K1's failure adds focus stops and exposure; it does not prevent keyboard operation. A11Y-006 is P1 only because a drag-only interaction cannot be operated by keyboard at all.
  - A11Y-004 (misexposure in the accessibility tree) and A11Y-009 (a critical defect kept P5) are the precedents.
  - The layer note in the entry states this.
- **Severity: major.** Content becomes over-reachable rather than unavailable. The demonstrated case is transient and narrow in reach. A11Y-004 and the RCE §8 reasoning on U1a are the precedents (candidate evaluation §9).
- **Validation: `mechanical-countable`, rendered, capability-gated,** as for A11Y-010. The probe is deterministic, with `activeElement` and accessibility-tree samples. Under `SKILL.md` §1 it can therefore gate SHIP when rendering capability exists; without rendering it is skipped, and the static flag is review-only.
- **No P1 text is added anywhere.** `SKILL.md` §3 is unchanged.

## 8. Axis 5 integration

**Decision: integrate, conditionally.**
- **Why integrate.** The gap arose because overlay defects escape BUILD, VALIDATE and Level 1 on routes where Level 2 does not run:
  - Evidence Investigation §5;
  - coverage-expansion run 1, whose builder's own VALIDATE missed the defect;
  - the candidate evaluation §8 tradeoff.

  A conditional rule that is absent from axis 5 would leave that route open.
- **Why conditional.** Making it Always-on would imply that every interface is checked for overlays it does not have. The brief and the authorization require it to stay conditional.

**Edit to `critique-protocol.md` axis 5 (one sentence).**
- **Added after "never skipped, regardless of scope":**
  > "plus the conditional checks listed here, each an entry of `accessibility.md`'s Conditional section, checked only when that entry's own applicability holds (A11Y-012, only when a dismissible overlay is in the scope being critiqued; no interface is required to contain one)"
- **Why "its own applicability".** Axis 5 defers to the entry's applicability, so a POLISH limited to a touched overlay and a CRITIQUE of a whole interface do not contradict it (reviewer MINOR 2).
- **Changed:** "Always-on describes when an entry is checked, not its authority" → "Always-on or conditional describes when an entry is checked, not its authority".
- **Changed:** A11Y-012 added to the P5 group.
- **Unchanged:**
  - the Always-on list and its "never skipped, regardless of scope" wording;
  - the membership rule ("An entry joins this list only under its own `loop.md` §2 authorization"), which this authorization satisfies;
  - "only `SKILL.md` §3 defines P1".
- **No other file lists axis 5 membership.**

## 9. Overlap check (`loop.md` §4)

**Existing DE entries.** The whole Rule Catalog, `principle-pool.md`, `visual-references.md`, `anti-slop-registry.md`, `style-catalog.md`, the T4 sources, `gesture-physics.md` and `existing-project-safety.md` were searched for overlay-related material (inert, off-canvas, drawer, dialog, overlay, aria-hidden, focus trap).
- **Hits:**
  - A11Y-009's presupposition (applicability);
  - A11Y-010 check (5);
  - INTX-002 (confirm dialogs);
  - MOTION-005 (modal durations);
  - `gesture-physics.md` (drag-to-dismiss applicability);
  - `smoothui.md` (example list, accessibility deferral).
- **None states K1's requirement.** A11Y-002 and A11Y-009 are analysed in candidate evaluation §5, and A11Y-012's applicability records both relationships. Nothing in the Principle Pool concerns focus, keyboard, modals or sheets.
- **No existing entry was changed.**

**Catalog principle records (read-only).**
- **Records scanned:** all 7 principle records in the external reference catalog's principle store: PRN-0001 and PRN-0003 accepted; PRN-0002, PRN-0004, PRN-0005, PRN-0006 and PRN-0007 rejected.
- **Method.** A scripted keyword scan of every string field of every record for: inert, focus, keyboard, overlay, drawer, dialog, modal, sheet, off-canvas, dismiss, closed, hidden, aria, assistive, screen reader, accessib, tab order, exit, transition.
- **Result:** no record contains focus, keyboard, overlay, drawer, dialog, modal, sheet, off-canvas, dismiss, inert, aria, assistive or tab-order content. The hits were incidental:
  - PRN-0004 (rejected): "hidden selections" in a selection-scope principle;
  - PRN-0005 (rejected): a "hidden question is never required" form-requiredness principle;
  - review-note text ("accessib…", "closed for this principle", reviewer notes) in PRN-0001, -0002, -0003, -0006 and -0007.
- **Conclusion.** No accepted or rejected principle states or approaches K1's norm, scope, boundary, validation or remediation. No overlap was found, so no principle was changed and no clarification was needed.
- **Where the result is recorded.** Only in this report. The runtime entry refers to this report for the overlap check and names no catalog material (reviewer MINOR 5; TR §11 C4).
- **Limitation, disclosed.** A follow-up command to print each record's principle text in full was **denied by the session's permission classifier**, and was not pursued by other means. The keyword scan had already covered every field of every record, so the conclusion rests on it rather than on a full read. The milestone's reviewer was not given catalog access.

## 10. Clause-level provenance trace

| Clause | Support | Class |
|---|---|---|
| Principle: closed overlay content is not focusable and not exposed | coverage-expansion run 1 (independently verified, reproduced) [DE-native]; Phase 7 Test 05 (self-reported) [DE-native]; A11Y-009 applicability presupposition [existing DE entry] | DE-native + existing DE entry |
| Principle: kinds of overlay | fixed five-behaviour definition, written from Phase 7 DE evidence (Gap Discovery §4; Evidence Investigation §2) | DE-native |
| Principle: from dismissal, including the exit transition | coverage-expansion run 1 | DE-native |
| Principle: outcome only, no timing and no technique | candidate evaluation §7 constraints | DE-native (governance) |
| Layer P5 | `SKILL.md` §3; `accessibility.md` Phase 4 note; A11Y-004/-006/-009 precedent | existing DE entries |
| Severity major | candidate evaluation §9; A11Y-004 precedent | existing DE entries |
| Applicability, including the exclusions | candidate evaluation §7–§8 (no evidence on disclosures; closed state only) | DE-native |
| Applicability: Task Mode list | A11Y-010 applicability pattern (BUILD, REDESIGN, POLISH of the touched area, CRITIQUE, AUDIT) | existing DE entry |
| Exceptions: none once a dismissible overlay exists | candidate evaluation §7 (no exception is evidenced); A11Y-006 pattern ("none once drag exists") | DE-native + existing DE entry |
| Validation (1)–(6), including the settle-wait hazard | candidate evaluation §10; coverage-expansion §8 reproduction (400 ms wait passes, no wait fails) | DE-native |
| Static fallback, review-only | candidate evaluation §10 | DE-native |
| Remediation (outcome) and motion pointer | derived from the principle; MOTION-005/-007 | existing DE entries |

**Taint gates** (Taint Ruling C1–C4; the chain is DE-native, not chain A):

| Gate | Result |
|---|---|
| **C1 Independent support** | PASS. Every clause rests on DE-native evidence measuring DE's own behaviour or on existing DE entries. No Principle Pool entry is cited |
| **C2 Specificity** | PASS. No clause is more specific than its support. Only "from dismissal … during exit" has a demonstrated transition failure behind it, and that is exactly what it states. No timing value is set |
| **C3 No catalog content** | PASS. There is no catalog observation, identifier, formulation or rejected-principle content, and the overlap check found none on this topic (§9) |
| **C4 Disclosed authorization** | PASS, with a timing note. The topic's DE-native origin was disclosed before authorization (candidate evaluation §11, §14). The overlap-check *result* could only be produced inside this milestone, so it reaches the human through this report, after authorization (reviewer MINOR 4) |

**External text:** none. WCAG 2.2 SC 2.4.3 and SC 2.1.2 were named in Gap Discovery as possible support but were not acquired (not authorized), and nothing in A11Y-012 depends on them.

## 11. Validation performed

Structural and textual only. No browser, benchmark or fixture was run (not authorized).

| Check | Result |
|---|---|
| Fidelity to candidate evaluation §7 | principle is the §7 proposition verbatim, plus one non-normative closing sentence (§4); validation keeps every §10 qualifier |
| Schema | fields and order match A11Y-010/A11Y-011: category · layer, principle, severity, applicability, exceptions, evidence, freshness, validation, remediation |
| Duplicate ids | none; one `### A11Y-012` heading |
| Cross-references | every id in the added text resolves (A11Y-001, -002, -003, -004, -006, -009, -010, -011, -012; MOTION-005, -007) |
| No normative timing | no millisecond or duration value in the added text |
| No required technique | the added text names no `inert`, `visibility`, `display`, `hidden`, `<dialog>` or focus-trap library. `transform` appears only inside the quoted Phase 7 evidence; `getAnimations()` appears only as an example of how a *validator* detects the end of the exit |
| No WCAG text | the only mention of WCAG is the disclosure that none was acquired |
| No K2/K3/K4 | applicability limits the rule to the closed state; no open-state focus, containment, Escape or return requirement |
| Unrelated entries | unchanged: the `accessibility.md` diff is only the appended block; the `critique-protocol.md` diff is one line |
| P1 | no new P1; `SKILL.md` unchanged |
| `git diff --check` | clean |
| Scope | only `STATE.md`, `accessibility.md`, `critique-protocol.md` and this report are changed |

## 12. Independent review

One fresh, read-only general-purpose reviewer (`loop.md` §8; `loop.md` §4 requires this reviewer to check the clause trace).
- **Received:** the diff, this report in its pre-review draft, the candidate evaluation, the benchmark reports, the governance files and the precedents.
- **Blindness.** It was **not fully blind**. It received this report, which contains the main agent's conclusions, because `loop.md` §4 requires the milestone's reviewer to check the report's clause-by-clause trace. It was told to verify independently rather than adopt them. Both were hashed before dispatch: diff SHA-256 `ddc94f82…5089aea`; pre-review report SHA-256 `cb1a1856…efc3f5a`.
- **Not given:** `STATE.md`, git log messages, the catalog, the web or memory tools.
- **Changes made by the reviewer:** none.

**Result: no BLOCKING findings.** Every check passed: wording, scope, conditional applicability, P5, major, validation, provenance, overlap, axis 5, no unintended changes, and no K2/K3/K4. There were 3 SHOULD-FIX, 7 MINOR and 4 NOTE findings.

| Finding | Class | Reconciliation |
|---|---|---|
| Validation dropped three §10 qualifiers (open by keyboard; an element other than the first; close control by keyboard) while §4 claimed "as listed" | SHOULD-FIX | **Adopted.** Qualifiers restored; §4 updated |
| `getAnimations()` misses script- or timer-driven exits, so sampling could stop early | SHOULD-FIX | **Adopted.** "or, where the exit is script-driven, until the overlay's rendered state stops changing", still with no fixed delay |
| `evidence:` omits §13 limits | SHOULD-FIX | **Adopted.** Escape-only, one engine and one implementation style now stated |
| DISCOVER missing from the Task Mode list | MINOR | **Declined.** A11Y-010's list, the precedent used, also omits it; DISCOVER is a read-only findings pass. Adding a mode would widen the entry beyond that precedent |
| Axis 5 "interface being critiqued" vs the entry's "touched overlay" for POLISH | MINOR | **Adopted.** Axis 5 now defers to "that entry's own applicability" |
| No trace rows for `exceptions:` and the Task Mode list | MINOR | **Adopted** (§10) |
| C4 marked clean although the overlap result reaches the human after authorization | MINOR | **Adopted.** Timing note in §10 |
| The runtime entry mentioned the catalog overlap check | MINOR | **Adopted.** The entry now refers to this report and names no catalog material |
| "its Conditional section" is ambiguous | MINOR | **Adopted.** Axis 5 names `accessibility.md` |
| §5 said "As committed" before any commit | MINOR | **Adopted.** "As authored … after review" |
| Overlap scan is keyword-only | NOTE | Already disclosed (§9) |
| `STATE.md` not reviewed | NOTE | By design; `STATE.md` holds only the human's authorization text and operational fields |
| The MOTION-005/-007 pointer ties a duration rule to A11Y-012 | NOTE | Kept. It points to where the exit motion is already governed and adds no timing to A11Y-012 |
| Review not fully blind | NOTE | Recorded above |

No disagreement remains. The one declined item is a MINOR precedent choice, and no finding required an out-of-scope change.

## 13. Files changed

- `design-excellence/references/rule-catalog/accessibility.md`: A11Y-012 added to the Conditional section (11 lines).
- `design-excellence/references/critique-protocol.md`: axis 5 sentence adjusted to list A11Y-012 as a conditional check and in the P5 group (one line).
- `STATE.md`: governance fields from the human's authorization; operational fields.
- `benchmarks/rule-authoring/K1-OVERLAY-CLOSED-STATE-RULE-AUTHORING-RESULTS.md`: created (this report).

## 14. Files intentionally unchanged

- `SKILL.md`, `loop.md`, `principle-pool.md` and `visual-references.md`;
- `smoothui.md` (§6);
- `motion.md` and every other Rule Catalog entry, including A11Y-001 to A11Y-011;
- the Integration Contract and every catalog file (read-only scan only);
- all earlier reports, including the candidate evaluation;
- `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md`, `rules.md` and `scratchpad/` (untracked, not this milestone's).

## 15. Deferred / out-of-scope findings

- **`smoothui.md` accessibility floor list (l.92).** Adding A11Y-012 there would be a convenience pointer that changes a T4 source's checklist. It is not strictly necessary (§6), so it would need its own §2 authorization.
- **K2 and K3.** They remain class B in the candidate evaluation. They are not authored and no benchmark is recommended for them.
- **WCAG mapping.** Optional future grounding (SC 2.4.3, SC 2.1.2) would need reference authorization.

## 16. Final commit SHA

The hash is reported in the milestone's final response, since a commit cannot contain its own hash. Nothing was pushed.
