# Rule Authoring — WCAG 2.2 SC 1.4.1 Use of Color — Results

**Status:** COMPLETED.
**Rule:** `A11Y-011 — Use of color (WCAG 2.2 SC 1.4.1)`, canonical in `design-excellence/references/rule-catalog/accessibility.md` (Always-on section).
**Provenance (Taint Ruling C1–C4):** PASS.
**Critique/review:** PASS. One blind reviewer: no blocking findings; one should-fix (this report); two minor items, one adopted and one declined (§12).
**REF-007:** UNCHANGED.
**Parent commit:** `aabe45c`.

Identity boundary: follows Integration Contract §15. No catalog id other than residue labels (R16, U2) appears.

---

## 1. Authorization

**A11Y-011 was authored under the human authorization for this milestone.**

- **Authorization message** (2026-09-27): "Autorizo Rule Authoring: WCAG 2.2 SC 1.4.1, con el scope del brief."
- **Brief scope, verbatim:** "Autorizo Rule Authoring: WCAG 2.2 SC 1.4.1. Scope limitado a convertir el candidato A11Y-0xx documentado en `A11Y-011`, incluyendo su integración en el listado Always-on/Axis 5 y el tratamiento de REF-007 que resulte estrictamente necesario. No autorizo cambios al Integration Contract, Principle Pool, runtime architecture, adquisición de referencias, otros Rule Catalog entries, ni benchmarks nuevos."
- **Gate history:**
  1. The first run found no authorization in `STATE.md` and stopped before changing anything.
  2. The authorization then arrived in the human's next message.
  3. It was recorded in `STATE.md`'s governance fields (`loop.md` §7) before any other change.
- **C4 disclosure.** It was put to the human in the previous milestone (Final Skill Completion report §10): catalog residue R16 (unit U2(h)) surfaced the topic; U2 backs only rejected principles; the gated distinctness clause is absent. The human chose "candidate only" at that point, and has now authorized authoring with that disclosure on record.

## 2. Exact scope

- Author the report §10 candidate as `A11Y-011` in `accessibility.md`.
- List it in `critique-protocol.md` Level 1 axis 5.
- Treat REF-007 only if strictly necessary.
- Validate, review, write this report, update `STATE.md`, and make one local commit.

## 3. Explicit exclusions

Not done:
- the Integration Contract and the Principle Pool;
- principle promotion or export;
- runtime architecture;
- reference acquisition;
- any other Rule Catalog entry;
- new benchmarks or fixtures;
- `loop.md` and `SKILL.md`;
- reopening the Taint Ruling or the Final Skill Completion audit;
- re-authoring A11Y-010;
- U2, U1b, U1c and U3;
- a chain B route;
- push.

## 4. Candidate source

`benchmarks/final-completion/FINAL-SKILL-COMPLETION-RESULTS.md` §10, "Candidate record" (`A11Y-0xx (candidate)`).

Changes from the candidate:

| Change | Reason |
|---|---|
| heading `A11Y-0xx (candidate)` → `A11Y-011` | the id: the next unused accessibility number (A11Y-001 to A11Y-010 exist) |
| remediation: "an underline, weight or icon (G182)" → "an underline or other text styling (G182), or an icon" | **citation precision** (reviewer MINOR). G182 names text styling (underline, bold, italics, font style or size), not icons. Icons remain supported by the principle ("a shape or icon") and by the Understanding example of required fields "with accompanying icons". The allowed cues are unchanged; only the citation is corrected |

No other wording changed. No clause was strengthened or weakened.

## 5. Final A11Y-011 rule

As committed in `accessibility.md`:

```
### A11Y-011 — Use of color (WCAG 2.2 SC 1.4.1)
- **category:** accessibility · **layer:** P5 (UX/usability — a WCAG 2.2 Level A criterion, but not one of the four accessibility floors on the `SKILL.md` §3 enumerated P1 list; kept P5, as `A11Y-010` is. It is not the P1 "contrast" floor: contrast against the background stays with `A11Y-001`)
- **principle:** color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. Color and color coding remain fully available as design tools, as long as another visual indication complements them — for example text, a pattern, a shape or icon, or an underline or other text styling. A difference in lightness between two colors counts as that other indication when the colors reach a contrast ratio of at least 3:1 with each other; it does not when the content relies on perceiving or telling apart a particular hue.
- **severity:** major
- **applicability:** always-on for every browser-rendered interface, wherever color conveys information, indicates an action, prompts a response or distinguishes a visual element — for example links in running text, required or invalid form fields, chart series, and color-coded navigation or wayfinding (including an adaptation of `visual-references.md` REF-007). It does not apply where color carries none of these (purely decorative color). A link's visited state is not an author responsibility. Distinct from `A11Y-001` (contrast against the background; both apply), `A11Y-002` (focus indicator) and `A11Y-004` (icon text alternatives). Visual only: it does not replace the programmatic exposure of the same information to assistive technologies.
- **exceptions:** none beyond the applicability limits.
- **evidence:** public standard: WCAG 2.2 SC 1.4.1 Use of Color (Level A), its W3C Understanding document, techniques G14, G111, G182, G183, G205 and failures F13, F73, F81. DE-native: no Design Excellence rule covered this criterion, and `visual-references.md` REF-007 offers color as a navigational index, whose adaptation could make color the only cue. No DE build has yet been observed failing this criterion: the entry is a checkable floor, not a correction of observed behaviour.
- **freshness:** source: WCAG 2.2 (W3C Recommendation, 12 December 2024), SC 1.4.1 with its Understanding document and techniques — external authority; cite the spec directly, not this file. Text verified against W3C 2026-09-27. status: review_interval_days: 365.
- **validation:** manual — whether color carries information is a judgement, so this is not `mechanical-countable` and does not gate SHIP mechanically. For each place in the touched area where color conveys information, indicates an action, prompts a response or distinguishes an element, name the other visual indication or the 3:1 lightness difference that carries it too. Where rendering capability is available, viewing the area in grayscale helps find hue-only cues; it does not settle cases that depend on a particular hue. Statically, flag for review (not as failures) links in running text with `text-decoration: none`, no other non-color distinction and no 3:1 contrast against the surrounding text (G183), and form states (required, invalid) that change only color.
- **remediation:** add a non-color cue that fits the case: text that states the information (G14; for colored form labels, G205), an additional visual cue such as an underline or other text styling (G182), or an icon, or a pattern (G111). For inline links distinguished from surrounding text by color alone, a contrast ratio of at least 3:1 between link text and surrounding text is sufficient (G183), with each color still meeting `A11Y-001` against the background.
```

## 6. Rule location

- `accessibility.md`, `## Always-on` section, directly after A11Y-010 and before `## Conditional`.
- **One canonical copy.** The only other mention of the id is the pointer in `critique-protocol.md` axis 5.

## 7. Authority, layer and severity

- **P5.** SC 1.4.1 is Level A, but it is not one of the four accessibility floors on the `SKILL.md` §3 enumerated P1 list. WCAG level does not confer P1, as with A11Y-005, A11Y-008 and A11Y-010.
- **Not the P1 "contrast" floor.** The layer note states that contrast against the background stays with A11Y-001.
- **Severity major**, as in the candidate (A11Y-004 and A11Y-010 precedent).
- **Validation manual.** It is not `mechanical-countable`, so it adds no SHIP gate (`SKILL.md` §1). This matches the A11Y-009 precedent.

## 8. Always-on / axis 5 integration

- **Axis 5 edit:** one line. `A11Y-011` was added to the listed ids and to the P5 group in the existing authority sentence. Nothing else changed.
- **Membership rule honoured:** "An entry joins this list only under its own `loop.md` §2 authorization". This milestone's authorization names the listing.
- **The statement "Always-on describes when an entry is checked, not its authority … only `SKILL.md` §3 defines P1" is unchanged.**
- **No other file lists axis 5 membership.**

## 9. Clause-level provenance summary

The full clause trace is in Final Skill Completion report §10, and its W3C text was verified on 2026-09-27. It is unchanged except for the G182 citation above.

| Gate | Result |
|---|---|
| **C1 Independent support** | PASS. Every clause is supported by WCAG 2.2 SC 1.4.1 and its Note, the W3C Understanding document, the techniques G14, G111, G182, G183, G205 and failures F13, F73, F81 (all listed on the Understanding page), or existing DE entries (A11Y-001, A11Y-002, A11Y-004). No Principle Pool entry is cited |
| **C2 Specificity match** | PASS. The reviewer verified the Understanding quotes and G183's current test (3:1 link-to-text contrast, no hover/focus requirement). The only imprecision found (G182 "icon") is corrected |
| **C3 No catalog content** | PASS. No catalog observation, identifier or formulation, and no rejected-principle content. The gated Taint §8 clause ("stored status and live selection must use distinct encodings") is absent. "Form states that change only color" is a color-alone test, not a test that two states are distinct |
| **C4 Disclosed authorization** | PASS (§1) |

REF-007 appears only as an applicability example ("including an adaptation of") and as DE-native context in `evidence`. It is never normative support.

**Reviewer note (recorded).** Principle sentence 3 (the 3:1 lightness difference) rests on the Understanding document, which W3C marks informative. `loop.md` §4 requires an "authoritative" source. The Understanding document is W3C's own interpretation of the criterion and is not looser than it.

## 10. REF-007 decision

**UNCHANGED.** A11Y-011 functions correctly without modifying REF-007:
- **Reach.** A11Y-011 is always-on and checked on every task at CRITIQUE axis 5. REF-007 loads only at DIRECT/DESIGN. A color-only adaptation of REF-007 is therefore caught before SHIP.
- **Authority.** A11Y-011 (P5) outranks a distinctiveness reference (P6) under `SKILL.md` §3.
- **Wording.** REF-007's "navigate by color alone without reading every label" presupposes that labels are present ("every"), so a compliant reading exists.
- **Explicit link.** A11Y-011's applicability names REF-007 adaptations. That example is readable without loading `visual-references.md` at CRITIQUE, so `SKILL.md` §7 is respected.

A pointer on REF-007 would change a REF entry's meaning, and it is not strictly necessary. It was therefore not added. The reviewer agreed that leaving REF-007 unchanged is defensible.

## 11. Validation performed

Structural and textual only. No browser or visual validation was performed, and no fixtures or benchmarks were created.

| Check | Result |
|---|---|
| A11Y-011 read completely in context | done |
| Fidelity to the candidate | identical except the heading, before the G182 correction (scripted line comparison); after it, one remediation phrase differs (§4) |
| Schema | fields and order match A11Y-010: category · layer, principle, severity, applicability, exceptions, evidence, freshness, validation, remediation |
| Duplicate rule ids | none |
| Unrelated Rule Catalog entries | unchanged: the diff touches only the added block and the axis 5 line |
| Layer | P5; no P1 layer text in the entry |
| Axis 5 membership | correct (§8) |
| No new P1 authority | confirmed (`SKILL.md` §3 unchanged) |
| Provenance | unchanged from the traced candidate (§9) |
| Principle Pool / catalog content | none |
| REF-007 | `visual-references.md` unchanged (no diff) |
| Cross-references | every rule id referenced under `design-excellence/` resolves to a definition |
| `git diff --check` | clean |
| Scope | only `STATE.md`, `accessibility.md`, `critique-protocol.md` and this report changed |
| `STATE.md` consistency | governance fields per the human's authorization; operational fields updated at completion |

## 12. Independent review

One fresh, blind, read-only general-purpose reviewer (`loop.md` §8; `loop.md` §4 requires the reviewer to check the clause trace).
- **Received:** the diff, the candidate and its trace, the governance files, the provenance model, the U1a precedent, and w3.org access.
- **Withheld:** the main agent's verdict, frozen and hashed before dispatch (SHA-256 `b4ba21ab…5f024cd1793`).
- **Changes made by the reviewer:** none. It read the Understanding page for 1.4.1, G183, G182 and F73.

**Result: PASS.**

| Question | Verdict |
|---|---|
| Fidelity | PASS (only the heading differed) |
| WCAG specificity | PASS, one MINOR citation issue |
| Authority | PASS |
| Always-on / axis 5 | PASS |
| Provenance | PASS |
| REF-007 | NOTE (unchanged is defensible) |
| Unrelated rules | PASS |
| Validation honesty | PASS |
| Scope and STATE | PASS, NOTE |

Reconciliation:

| Finding | Class | Reconciliation |
|---|---|---|
| The milestone report and trace do not yet exist; `STATE.md` Next action is stale | SHOULD-FIX | **Adopted:** this report; `STATE.md` updated |
| G182 does not name icons | MINOR | **Adopted** (§4). Citation precision only |
| F73: cues shown only on hover or focus do not count; the static check could say so | MINOR | **Declined.** It would add a validation requirement the approved candidate does not have, and the brief directs not to strengthen the candidate. The rule already cites F73, and its principle requires another visual indication; this milestone makes no further claim |
| The Understanding document is informative | NOTE | recorded (§9) |
| REF-007 unchanged | NOTE | agreed (§10) |

No disagreement remains, and none of the findings requires an out-of-scope change.

## 13. Files changed

- `design-excellence/references/rule-catalog/accessibility.md`: A11Y-011 added (11 lines).
- `design-excellence/references/critique-protocol.md`: axis 5 lists A11Y-011 among the always-on checks and in the P5 group (one line).
- `STATE.md`: governance fields from the human's authorization; operational fields.
- `benchmarks/rule-authoring/A11Y-011-RULE-AUTHORING-RESULTS.md`: added (this report).

## 14. Files intentionally unchanged

- `design-excellence/references/visual-references.md` (REF-007, §10).
- `design-excellence/references/principle-pool.md`.
- `design-excellence/SKILL.md`: no integration inconsistency required a change.
- `loop.md`.
- Every other Rule Catalog entry and file, including A11Y-001 to A11Y-010, `color.md` and `layout-interaction.md`.
- The Integration Contract and every catalog file.
- All earlier reports, including the Final Skill Completion report and its §10 candidate record, which stays as that milestone's history.
- `rules.md` and `scratchpad/` (untracked, not this milestone's).

## 15. Deferred / out-of-scope findings

- **REF-007 pointer.** A sentence such as "Color stays a complement to labels or shapes, never the only cue" was offered by the reviewer as an optional follow-up. It would change a REF entry's meaning, so it would need its own §2 authorization. It is not needed for A11Y-011 to function (§10).

## 16. Final commit SHA

This report is part of the milestone's single local commit, and a file cannot contain its own commit hash. The SHA is given in the final response and is visible with `git log -1`. Parent: `aabe45c`. Nothing was pushed.
