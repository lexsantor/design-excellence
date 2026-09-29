# Final Skill Completion & Hardening — Results

**Status:** COMPLETED.
**Completion:** COMPLETE WITH EXPLICIT DEFERRED ITEMS.
**Independent review:** PASS after corrections. One blind reviewer ran two rounds (§15).
**Parent commit:** `5225e09`.

Identity boundary: follows Integration Contract §15. No catalog id other than PRN ids appears. Residue items keep the labels of the earlier audits (R1–R16, U1–U3).

---

## 1. Executive completion status

- **Every completion-critical item the audit found is resolved** (§3). Eight tracked files changed, and this report was added. The Integration Contract, the Principle Pool, runtime architecture and reference acquisition were not touched.
- **Two authority leaks nobody had flagged before were closed.**
  - SLOP-004 said it could override a literal "match this" instruction.
  - `smoothui.md` listed a P5 rule and a P7 rule under "P1 safety".

  Both gave rules authority that `SKILL.md` §3 does not grant them. Three other wordings that could lead a fresh session to escalate P1 were also fixed: critique axis 5, `SKILL.md`'s description of `ARCHITECTURE.md`, and the leftover scope heading in `STATE.md`.
- **A11Y-010 check (3) was stricter than WCAG** for truncation that is identical at every width. It now uses F102's comparison between the 1280 CSS px baseline and 320 CSS px. All nine validation paths the U1a report left untested were exercised on disposable fixtures (§9).
- **`loop.md` §4 now states the Taint Ruling's discovery/derivation distinction** (§5). It also closes a Principle-Pool-to-rule loophole the reviewer found in the first draft.
- **INTX-003's undefined "required floor widths" is defined** without importing A11Y-010's 320 CSS px (§11).
- **WCAG 2.2 SC 1.4.1 (Use of Color).** The rule was drafted, and every clause traced to W3C sources. Given the C4 disclosure, **the human chose "candidate only"**. The Rule Catalog therefore does not contain it. A precise candidate record is in §10.
- **What remains** is out of scope, deferred by design, a human decision, or optional (§16).

## 2. Authorization and exact scope

- **Human authorization (2026-09-27), verbatim:** "Autorizo Final Skill Completion & Hardening, con el scope completo del brief, incluyendo la modificación de loop.md §4 únicamente para la aclaración de provenance expresamente definida en el brief. No autorizo cambios al Integration Contract, Principle Pool, runtime architecture, adquisición de nuevas referencias ni push remoto."
- **Gate.** At the start of the run, `STATE.md` had no authorization for this milestone, so the run stopped before making any change. The human's authorization was then recorded in `STATE.md` (`loop.md` §7) before any other work.
- **Budget.** The 60-minute default was raised to 180 minutes for this milestone only, by a separate human answer given during the run. This is recorded in `STATE.md`. The run finished within it.
- **C4 decision.** A human answer during the run: "Candidate only" for WCAG 1.4.1 (§10).
- **Not authorized, and not done:**
  - the Integration Contract;
  - the Principle Pool;
  - promotion or export of principles;
  - new reference acquisition;
  - the licensed reference library design-file fallback;
  - runtime catalog access;
  - runtime architecture;
  - any `loop.md` change other than §4;
  - push.
- **W3C fetches.** W3C pages were fetched only to verify WCAG text. WCAG is a source family the Rule Catalog already admits (A11Y-001, A11Y-005, A11Y-006, A11Y-010). This is not reference acquisition in the `loop.md` §4/§5 sense, which concerns catalog source material. No catalog file was read.

## 3. Completion matrix

Classes: **A** completion-critical · **B** useful, non-blocking · **C** deferred by design · **D** outside authorization or human-decided.

| # | Issue | Source | State found | Risk | Class | Action | Validation | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Axis 5 labelled "the P1 always-on gates" while listing P5 entries | U1a §15.1 (reviewer M10) | inaccurate label | P5 rules read as P1 and used to override P2 | A | Relabel as always-on checks. Each entry keeps its own layer. Listing still needs its own §2 authorization | diff; review | COMPLETE |
| 2 | `loop.md` §4 "derived"/"traces to" undefined | Taint §12.5; U1a §15.6 | ruling rested on interpretation | over-blocking, or laundering | A | One §4 bullet (C1–C4); Principle Pool excluded as support | Chain A/B test; review ×2 | COMPLETE |
| 3 | A11Y-010 check (3) failed truncation identical at every width | this audit; fixture `clip-fixed` | stricter than WCAG | false FAIL on legitimate fixed truncation | A | Compare against the 1280 baseline, as F102 does; principle aligned | clip fixtures (§9) | COMPLETE |
| 4 | A11Y-010 validation paths never exercised | U1a §12, §15.4 | 9 paths untested | validation credibility | A | 20 disposable fixtures; harness for checks (1)–(6) | §9 | COMPLETE |
| 5 | INTX-003/TYPE-006 "required floor widths" undefined | U1a §15.2 | undefined since Phase 2 | a mechanical SHIP gate that cannot be reproduced | A | INTX-003 defined as the narrowest width of each layout range; 320 explicitly not implied. TYPE-006 unchanged (already bound) | review round 2 | COMPLETE |
| 6 | LAYOUT-004 readable as fixing overflow | U1a §15.3 | no pointer | root clip treated as a reflow fix | A | One-sentence pointer to A11Y-010 | diff | COMPLETE |
| 7 | WCAG 2.2 SC 1.4.1 absent | RCE §14; Taint §12.3; U1a §15.5 | no DE coverage | Level A gap; REF-007 tension | D (human-decided) | Drafted and traced; kept as candidate by human decision | W3C verified; review | DEFERRED (human decision) |
| 8 | SLOP-004 claimed override of a literal "match this" instruction | this audit | P6 entry asserting P1-style override | accidental authority | A | Explicit instruction wins | diff; review | COMPLETE |
| 9 | `smoothui.md` listed A11Y-005 (P5) and A11Y-007 (P7) under P1 | this audit (Phase 7.5 missed it) | mislabelled | accidental P1 escalation | A | Both bind at their own layers | diff; review | COMPLETE |
| 10 | `SKILL.md` called `ARCHITECTURE.md` "authoritative source", although it was later superseded ("any accessibility violation is P1 by construction") | fresh-session test | stale authority | P1 escalation through design history | A | "Original design source"; this package governs where they differ | diff; review | COMPLETE |
| 11 | `STATE.md` scope block began "READ-ONLY AUDIT permits …" | fresh-session test | residue of an earlier milestone | scope misread | A | Standing boundaries; the Integration Contract is never edited | review round 2 | COMPLETE |
| 12 | U2 (a), (d), (e) and the (h) distinctness clause | RCE; Taint §8 | blocked as chain A | — | D | none | — | OUT OF SCOPE |
| 13 | U1b, U1c, U3 | RCE | not candidates | — | D | none | — | OUT OF SCOPE |
| 14 | Chain B route for rules | Taint §10 | needs a Contract change | — | D | none | — | OUT OF SCOPE |
| 15 | A11Y-010 checks marked mechanical-countable although (1), (2) and (4) need judgement | U1a §12 | A11Y-004/INTX-003 precedent | — | C | recorded | — | DEFERRED BY DESIGN |
| 16 | REF-007 "navigate by color alone" wording | this audit | tension with WCAG 1.4.1, which DE does not yet contain | an adaptation could use color as the only cue | D | Pointer removed together with the candidate (human decision) | — | DEFERRED with #7 |
| 17 | Anti-slop / visual-reference freshness | file headers | verified 2026-09-20/21, 90-day interval | — | C | none (not stale) | dates | DEFERRED BY DESIGN |

## 4. Files changed

| File | Change |
|---|---|
| `loop.md` | §4: one bullet (provenance clarification) |
| `STATE.md` | governance fields from the human's authorization and budget answer; standing-boundaries heading; operational fields |
| `design-excellence/SKILL.md` | line 10: `ARCHITECTURE.md` described as the original design source; this package governs where they differ |
| `design-excellence/references/critique-protocol.md` | Level 1 axis 5 label and authority note |
| `design-excellence/references/rule-catalog/accessibility.md` | A11Y-010: principle loss baseline; check (3) |
| `design-excellence/references/rule-catalog/layout-interaction.md` | LAYOUT-004 pointer; INTX-003 floor widths |
| `design-excellence/references/anti-slop-registry.md` | SLOP-004 applicability and exceptions |
| `design-excellence/references/smoothui.md` | Precedence item 1 |
| `benchmarks/final-completion/FINAL-SKILL-COMPLETION-RESULTS.md` | this report (added) |

Not changed:
- the Integration Contract and every catalog file;
- `principle-pool.md` and `visual-references.md` (the REF-007 pointer was added and then removed with the candidate);
- `typography.md` (TYPE-006);
- `color.md`, `motion.md`, `content-copy.md` and `performance-hardening.md`;
- `existing-project-safety.md`, `reicon.md`, `kinetics.md`, `style-catalog.md` and `gesture-physics.md`;
- every earlier report;
- `rules.md` and `scratchpad/` (untracked, not this milestone's).

## 5. Governance changes

**`loop.md` §4.** One bullet was added after "If an idea traces to catalog material, it is gated whatever its form." The existing text is unchanged. The bullet:
- says that learning of a topic through catalog material is not derivation;
- defines "traces to" clause by clause: supported only by catalog material, more specific than its independent support, or reproducing a rejected or unaccepted principle's normative content in any wording;
- names the admissible independent support: an admitted authoritative source family, DE-native evidence, or an existing DE entry **other than a Principle Pool entry**;
- limits evidence gathered with residue-designed criteria to showing failure;
- sends independently supported knowledge through the ordinary §2 authorization, with disclosure of the catalog surfacing and rejected-principle overlap, and a clause trace in the report that the §8 reviewer checks;
- drops or gates any failing clause;
- states that it "creates no route for catalog material itself to cross".

The Taint Ruling's §12 wording was the starting point.

Chain test (confirmed independently by the reviewer in both rounds):

| Case | Result |
|---|---|
| **Chain A**: the catalog surfaces a topic; WCAG supplies every clause | not derived; §2 with disclosure (the A11Y-010 case) |
| **Chain B**: a catalog observation is abstracted into a rule | its normative content is supported only by catalog material, so it traces and stays gated; the Contract still provides no rule route |
| **Laundering** (Taint §8 U2(a), (d), (e), and the (h) distinctness clause) | the over-specific or rejected-content clause traces |
| **Principle Pool → rule** | closed: Pool entries cannot serve as support (found by the reviewer in the first draft, fixed) |
| **Human gate** | unchanged; no second route |

**`STATE.md`.**
- Governance fields set from the human's authorization and budget answer.
- The standing block no longer opens with "READ-ONLY AUDIT permits …". It now reads as standing boundaries: the actions of `loop.md` §2 inside an authorized milestone, and the listed exclusions, which hold unless an Authorization field names one "and never where `loop.md` forbids it (the loop never edits the Integration Contract, §3)". The exclusion list is unchanged.
- Operational fields updated. An earlier draft of the scope text cited the Taint Ruling by commit hash, which `loop.md` §0 does not allow; it now cites the report.

## 6. Rule Catalog changes

- **A11Y-010:**
  - **Principle:** "information that is hidden, clipped or truncated at that width counts as lost" now reads "information that is visible at 1280 CSS px but hidden, clipped or truncated at 320 CSS px counts as lost". This follows F102, which compares against the 1280 baseline.
  - **Check (3):** clipping or truncation fails when "text or a control visible at the 1280 CSS px baseline of (4) is no longer visible", unless a mechanism reveals the rest. Before the change, it also failed truncation that is identical at every width (fixture `clip-fixed`). The first correction draft ("not equally clipped … at the baseline") compared elements rather than content, and was too loose for width-dependent clamps. The reviewer caught this (§15), and the final wording and re-run fixed it (§9).
  - Nothing else in A11Y-010 changed.
- **LAYOUT-004.** One sentence added: `clip`/`hidden` only removes the scrollbar and does not fix the overflow; content it cuts off is still checked by `A11Y-010`.
- **INTX-003 validation.** "At the required floor widths" is now defined as "the narrowest width of each layout range, meaning each declared responsive breakpoint (`SKILL.md` §5 Responsive Notes) or, where none are declared, each width breakpoint the stylesheets define, plus the narrowest width the project declares it supports, if any. `A11Y-010`'s 320 CSS px reflow floor is checked separately and is not implied here" (§11).
- **SLOP-004.**
  - **Before:** the entry claimed to override even a literal "match this" instruction, with disclosure.
  - **Why that was wrong:** SLOP-004 is Anti-Slop (P6) and not on the P1 list. `SKILL.md` §3 allows overriding P2 only for P1 items, "never for subjective style disagreement". The Phase 2 architecture had rejected exactly this source stance as "too permissive" (`ARCHITECTURE.md` §4, Conflict Map #5).
  - **Now:** an explicit instruction to keep or match the layout wins, and naming the tell once is enough. The statement, severity and remediation are unchanged.
- **`smoothui.md` Precedence item 1.** The P1 floor is now `A11Y-002` plus the rest of the `SKILL.md` §3 list. `A11Y-005` (P5) and `A11Y-007` (P7) still bind SmoothUI components, at their own layers. No obligation was dropped.
- **No rule was added.** A11Y-011 was drafted and then withdrawn by human decision (§10).

## 7. Critique protocol changes

- **Axis 5.** "The P1 always-on gates" now reads "the always-on accessibility checks listed here, each an entry of `accessibility.md`'s Always-on section (A11Y-001, A11Y-002, A11Y-003, A11Y-004, A11Y-009, A11Y-010)". The axis also states:
  - "An entry joins this list only under its own `loop.md` §2 authorization" (Taint §12.1);
  - always-on sets when an entry is checked, not its authority;
  - A11Y-001–003 are P1, and A11Y-004, A11Y-009 and A11Y-010 are P5;
  - only `SKILL.md` §3 defines P1.
- **Membership is unchanged.** Level 1 and Level 2 mechanics are unchanged.

## 8. A11Y-010 integrity result

A11Y-010 was audited as an existing rule. Rewording for style was out of scope, and nothing was changed on that basis.

| Aspect | Result |
|---|---|
| WCAG fidelity | Principle, exceptions and the 256 px clause match SC 1.4.10, Notes 1 and 2 and the Understanding document (verified in U1a). One over-strict step, check (3), is corrected, and the principle's loss clause now names the F102 baseline explicitly (§6). The reviewer judged the result "neither stricter nor looser than the criterion" |
| Authority | P5; not raised. Axis 5 now says so explicitly |
| Severity | major; unchanged |
| Always-on placement; critique floor | correct; listed in axis 5 |
| Exceptions | WCAG Note 2 examples, grids and cells, preformatted text. Legitimate 2D content is not prohibited |
| "320 CSS px" | not a single-column mandate ("This does not require a single column") |
| Remediation | options only ("any presentation that keeps it available is acceptable — for example …") |
| Provenance | no catalog wording or rejected-principle content; the changes only align the rule with F102 |
| Consistency with layout rules | LAYOUT-004 points to A11Y-010. INTX-003 now states that 320 is not implied. LAYOUT-005 and HARDEN-003 are consistent |
| Independently understandable | yes |

## 9. A11Y-010 validation coverage

**Method.** 20 disposable fixture pages were built outside the repository: pass/fail pairs per path, plus one extra truncation case. The expected verdict for each was fixed from WCAG before any run. A harness implementing checks (1)–(6) as written ran in Chromium through the Playwright MCP browser:
- baseline at 1280×800, with menus and dialogs opened;
- 320×800 closed, then opened (check (5));
- 1280×256 with the axes swapped for vertical-text pages (check (6)).

Check (3) was re-run with a word-level comparison of hidden content at 320 against 1280.

**Limits (read before the table):**
- The evidence is synthetic, author-built and author-harnessed.
- Classification was simulated by fixture attributes rather than performed by a design agent: `data-excepted` marks content needing 2D layout, and `data-reveal` marks a reveal mechanism.
- Only one engine was used.
- The fixtures and harness are disposable and are not committed (`loop.md` §14), so the results cannot be reproduced from this repository. They were provided to the human with this report.
- A PASS below means the rule's check procedure classified the fixture as WCAG does. It is not evidence about any DE build.
- No real DE build was re-run, because the three existing builds contain none of these paths (U1a §12).
- The usable width at 320 was 320 here (overlay scrollbar), against 305 in the U1a dry-run.

| Validation path | Result | Evidence |
|---|---|---|
| decoration bleed | **PASS** | aria-hidden decoration past the edge is ignored; a 420 px text line fails check (1) |
| carousels | **PASS** | 260 px panels pass (G225); 420 px panels fail check (2) |
| code blocks | **PASS** | an excepted `pre` passes. `nowrap` prose in a scroller fails check (2) when the harness measures content width. Run 1 measured the block box and missed it; that was a harness defect, since the rule already says "fully visible" |
| non-table grids | **PASS** | an excepted grid passes; a cell whose own content exceeds the visible width fails (cell clause) |
| dialogs | **PASS** | a 480 px dialog fails, and only at check (5), which shows the open-state step is needed |
| vertical clipping | **PASS** | a fixed-height box whose text wraps at 320 fails check (3); a clamp with a reveal link passes |
| truncation identical at every width (`clip-fixed`) | **PASS** after correction | the pre-milestone check (3) failed it (stricter than WCAG); the corrected rule passes it (5 words hidden at both widths, 0 lost) |
| width-dependent clamp (`clip-same`) | **PASS** | the corrected rule fails it, as F102 requires (46 words visible at 1280 are hidden at 320). The first correction draft passed it wrongly; the reviewer caught this before commit |
| excepted content under root clip | **PASS** | an SVG diagram under `html{overflow-x:clip}` fails check (1) because the real page cannot scroll it into view; in its own scroller it passes |
| horizontally scrolling content / 256 px height | **PASS** | vertical-rl text passes at 256 px height; `inline-size: 400px` fails check (6) |
| corrected checks (5) and (6) | **PASS** | exercised above (dialogs; vertical text) |
| 1280 CSS px baseline | **PASS** | used for checks (3) and (4). The rule already specified 1280; U1a's dry-run had used 1440 |
| full content availability | **PASS** | hiding an aside at 320 fails check (4), with its heading and text reported missing (content, not only controls); navigation behind a Menu disclosure passes |

No path was NOT ASSESSABLE. No environment limitation blocked a path, beyond the limits above.

## 10. WCAG 1.4.1 decision

**Decision: candidate only (human decision under Taint C4). The Rule Catalog is unchanged for 1.4.1.**

- **Investigation:**
  - **Existing coverage: none.** A11Y-001 covers contrast against the background, A11Y-004 icon text alternatives, INTX-001 state coverage, and the COLOR rules construction and aesthetics.
  - **Material usefulness.** Level A, applicable to every interface. `visual-references.md` REF-007 offers "color used as the navigational index itself … a user can navigate by color alone without reading every label"; adapting it with no second cue would fail 1.4.1.
  - **Overlap.** The topic was surfaced by catalog residue R16 (unit U2(h)). U2's observations back only rejected principles. Taint §8 permits a general rule at 1.4.1's specificity and keeps "stored status and live selection must use distinct encodings" gated. The draft contained no selection, status or state-distinctness wording.
  - **Gates.** C1–C3 passed, confirmed by the reviewer clause by clause against the W3C Understanding page and G183.
  - **C4.** The reviewer noted that the human's authorization preceded the disclosure, so C4 could not be self-certified. The disclosure was put to the human, who chose "Candidate only".
- **Candidate record** (not in the Rule Catalog; for a future, separately authorized Rule Authoring milestone):

```
### A11Y-0xx (candidate) — Use of color (WCAG 2.2 SC 1.4.1)
- **category:** accessibility · **layer:** P5 (UX/usability — a WCAG 2.2 Level A criterion, but not one of the four accessibility floors on the `SKILL.md` §3 enumerated P1 list; kept P5, as `A11Y-010` is. It is not the P1 "contrast" floor: contrast against the background stays with `A11Y-001`)
- **principle:** color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. Color and color coding remain fully available as design tools, as long as another visual indication complements them — for example text, a pattern, a shape or icon, or an underline or other text styling. A difference in lightness between two colors counts as that other indication when the colors reach a contrast ratio of at least 3:1 with each other; it does not when the content relies on perceiving or telling apart a particular hue.
- **severity:** major
- **applicability:** always-on for every browser-rendered interface, wherever color conveys information, indicates an action, prompts a response or distinguishes a visual element — for example links in running text, required or invalid form fields, chart series, and color-coded navigation or wayfinding (including an adaptation of `visual-references.md` REF-007). It does not apply where color carries none of these (purely decorative color). A link's visited state is not an author responsibility. Distinct from `A11Y-001` (contrast against the background; both apply), `A11Y-002` (focus indicator) and `A11Y-004` (icon text alternatives). Visual only: it does not replace the programmatic exposure of the same information to assistive technologies.
- **exceptions:** none beyond the applicability limits.
- **evidence:** public standard: WCAG 2.2 SC 1.4.1 Use of Color (Level A), its W3C Understanding document, techniques G14, G111, G182, G183, G205 and failures F13, F73, F81. DE-native: no Design Excellence rule covered this criterion, and `visual-references.md` REF-007 offers color as a navigational index, whose adaptation could make color the only cue. No DE build has yet been observed failing this criterion: the entry is a checkable floor, not a correction of observed behaviour.
- **freshness:** source: WCAG 2.2 (W3C Recommendation, 12 December 2024), SC 1.4.1 with its Understanding document and techniques — external authority; cite the spec directly, not this file. Text verified against W3C 2026-09-27. status: review_interval_days: 365.
- **validation:** manual — whether color carries information is a judgement, so this is not `mechanical-countable` and does not gate SHIP mechanically. For each place in the touched area where color conveys information, indicates an action, prompts a response or distinguishes an element, name the other visual indication or the 3:1 lightness difference that carries it too. Where rendering capability is available, viewing the area in grayscale helps find hue-only cues; it does not settle cases that depend on a particular hue. Statically, flag for review (not as failures) links in running text with `text-decoration: none`, no other non-color distinction and no 3:1 contrast against the surrounding text (G183), and form states (required, invalid) that change only color.
- **remediation:** add a non-color cue that fits the case: text that states the information (G14; for colored form labels, G205), an additional visual cue such as an underline, weight or icon (G182), or a pattern (G111). For inline links distinguished from surrounding text by color alone, a contrast ratio of at least 3:1 between link text and surrounding text is sufficient (G183), with each color still meeting `A11Y-001` against the background.
```

- **Clause trace** (W3C text verified 2026-09-27: WCAG 2.2 Recommendation of 12 December 2024, the Understanding document for SC 1.4.1, technique G183):

| Clause | Support |
|---|---|
| principle, sentence 1 | SC 1.4.1, verbatim |
| principle, sentence 2 | Understanding: "This should not in any way discourage the use of color on a page, or even color coding if it is complemented by other visual indication."; G14, G111, G182 |
| principle, sentence 3 | Understanding Intent: lightness difference counts "as long as … a contrast ratio of 3:1 or greater"; "if content relies on the user's ability to accurately perceive or differentiate a particular color an additional visual indicator will be required regardless of the contrast ratio" |
| applicability, examples | F73/G183 (links); F81 and Intent "required fields are red", "error is shown in red"; Situation B/G111 and the Intent sales example (charts); SC "distinguishing a visual element" plus DE REF-007 |
| applicability, limits | Understanding: "does not apply to situations where color has not been used to convey information…"; visited-link notes; "does not directly address the needs of users with assistive technologies"; SC Note (Guideline 1.3) |
| layer, severity, validation | `SKILL.md` §3; DE precedent (A11Y-004, A11Y-010); judgement needed, so manual |
| remediation | G14, G205, G182, G111, G183 (current test: link text at least 3:1 against surrounding text); A11Y-001 |

- **Notes for a future authoring milestone:**
  - The reviewer's MINOR edit to the static check ("flag for review (not as failures) … and no 3:1 contrast against the surrounding text (G183)") is already included above.
  - If authored, the milestone would also decide the axis 5 listing and a REF-007 pointer. The draft note was "Color stays a complement to labels or shapes, never the only cue", and the reviewer flagged it as a meaning change to a REF entry that must be disclosed.

## 11. INTX-003 / TYPE-006 decision

- **Main agent's first decision:** leave both unchanged as intentionally contextual. The phrase comes from `ARCHITECTURE.md` §19 ("responsive-width checks at the required floor widths") and was never defined.
- **The reviewer's objection, accepted.** INTX-003 is a `mechanical-countable` SHIP gate whose parameter is undefined and whose applicability names no widths, so two sessions cannot run it the same way. The class changed from C to A.
- **INTX-003 is now defined** as the narrowest width of each layout range: declared breakpoints (`SKILL.md` §5 Responsive Notes), or the stylesheets' width breakpoints where none are declared, plus the narrowest width the project declares it supports.
  - This is where labels wrap, consistent with INTX-003's own "especially at narrow responsive widths".
  - The reviewer's round-2 fix replaced a first wording that checked only the breakpoints themselves. That would have missed phone widths on a mobile-first site with only `min-width: 768px`.
- **A11Y-010's 320 CSS px is stated as not implied.** This keeps the Taint §12.1 condition that 320 must not silently redefine these rules.
- **TYPE-006 is unchanged.** Its applicability already names "every declared responsive breakpoint", and its validation borrows INTX-003's technique.
- **The residual semantic change is disclosed:** INTX-003 goes from undefined to a defined parameter. It gains no new norm and no fixed width.

## 12. LAYOUT-004 decision

- **Functional test.** An agent loading only `layout-interaction.md` (for example for a navigation POLISH) reads "use `clip` … to prevent horizontal scroll" and could conclude the overflow is solved.
- **Evidence.** Every Responsive Reflow Replication build set a root clip.
- **Decision.** Answer: yes. A one-sentence canonical pointer was added. No A11Y-010 content was duplicated.

## 13. Taint/provenance integrity

- No catalog observation, evidence, identifier, formulation, product, vendor, path or measurement entered any changed file.
- No catalog-derived material entered the Rule Catalog. A11Y-010's changes only align it with F102. LAYOUT-004's pointer and INTX-003's definition rest on existing DE entries (`SKILL.md` §5, TYPE-006) and CSS mechanics.
- The 1.4.1 candidate's catalog surfacing and rejected-principle context are disclosed in §10. It is not in runtime knowledge.
- `loop.md` and `STATE.md` carry no commit hashes, catalog identifiers or source names (`loop.md` §0).

## 14. Fresh-session test

Key governance files were read cold: `STATE.md`, `loop.md`, `SKILL.md` §1–§3 and §7, `critique-protocol.md`, `accessibility.md`.

| Risk | Found | Resolution |
|---|---|---|
| Unauthorized milestone execution | `STATE.md` "READ-ONLY AUDIT permits …" contradicted modifying milestones; the first rewrite implied an Authorization field could permit editing the Integration Contract (reviewer) | final wording: `loop.md` §2 actions inside an authorized milestone; exclusions hold "never where `loop.md` forbids it" |
| Accidental P1 escalation | axis 5 label; SLOP-004; `smoothui.md`; `SKILL.md` calling `ARCHITECTURE.md` authoritative | all corrected (§6, §7). The reviewer found no P1 escalation in the final diff |
| Catalog taint | "derived" undefined; Principle Pool as support (first draft) | `loop.md` §4 bullet, with the Pool excluded |
| Duplicated rules | none | pointers only |
| Incorrect critique routing | an axis 5 membership rule could have added entries automatically (first draft) | listing requires its own §2 authorization |
| Incorrect pipeline routing | none | `SKILL.md` §1 and §2 unchanged |
| False Level 2 independence | none | protocol unchanged |
| Fabricated validation | none | validation limits stated (§9); nothing is claimed as run that was not run |
| Accidental architecture change | none | no stage, tier, profile or source family added |

## 15. Independent review

One fresh, blind, read-only general-purpose reviewer (`loop.md` §8).
- **Received:** the diff, the completion matrix, the validation evidence, fixtures and harness, the governance files, the relevant reports, and W3C access.
- **Withheld:** the main agent's verdict, frozen and hashed before dispatch (SHA-256 `a290b643…d06b757`).
- **Changes made by the reviewer:** none.

**Round 1: ISSUE**

| Finding | Reviewer | Reconciliation |
|---|---|---|
| B1 check (3) correction too loose (element-level "equally clipped"; `clip-same` is a width-dependent clamp) | BLOCKING | **Adopted.** Reviewer's wording; principle aligned; word-level re-run; `clip-fixed` added (§9) |
| B2 report and trace unwritten; C4 disclosure not given to the human | BLOCKING | **Adopted.** The report was mid-draft at review time. The disclosure was put to the human, who chose candidate only |
| S1 `loop.md` §4: Principle Pool entries could "independently support" a rule; §8 trace check dropped | SHOULD-FIX | **Adopted**, with wording adapted to keep REF entries (DE-authored), which the reviewer accepted in round 2 |
| S2 `STATE.md` wording dropped "within the authorized milestone" and implied the Contract could be authorized | SHOULD-FIX | **Adopted verbatim** |
| S3 axis 5 membership rule would bypass the §2 listing decision | SHOULD-FIX | **Adopted** |
| S4 INTX-003 undefined parameter | SHOULD-FIX | **Adopted** (§11) |
| S5 REF-007 pointer | SHOULD-FIX | Applied, then **removed** with the candidate (human decision) |
| M1 static-check qualifier; M2 `SKILL.md` "authoritative"; M3 evidence limits | MINOR | **Adopted** (M1 in the candidate record) |

**Round 2 (same reviewer, after corrections): PASS, with one SHOULD-FIX and minor items**
- Check (3) and principle: "neither stricter nor looser than the criterion".
- `loop.md` §4: PASS; "Pool-to-rule laundering is now closed"; no second route; gate not weakened.
- INTX-003: SHOULD-FIX (breakpoints are not the narrowest widths; the "not 320" phrasing read as excluding narrow widths). **Adopted verbatim.**
- Principle "that width" is ambiguous: **adopted** ("at 320 CSS px").
- `loop.md` re-wrap: **done**.
- `STATE.md` gate fields: **done**. The pending C4 gate was resolved by the human before commit.
- "I found no P1 escalation anywhere in the new diff."

No unreconciled disagreement remains. Round 2 wording changes made after the round were the reviewer's own proposals.

## 16. Remaining work

Every item has a reason. None is unfinished core work.

| Item | Class | Reason |
|---|---|---|
| WCAG 1.4.1 rule (§10 candidate), with its axis 5 listing and REF-007 pointer | DEFERRED (human decision) | C4: the human chose candidate only. It needs a separately authorized Rule Authoring milestone |
| U2 (a), (d), (e) and the (h) distinctness clause | OUT OF SCOPE | blocked as chain A (Taint §8); no independent source reaches their specificity |
| U1b (a DE-stricter reflow bar), U1c (composition prescriptions), U3 | OUT OF SCOPE | not chain A candidates (RCE) |
| Chain B route for rules | OUT OF SCOPE | would require an Integration Contract change (not authorized) |
| A11Y-010 checks (1), (2) and (4) marked mechanical-countable although they need judgement | DEFERRED BY DESIGN | same precedent as A11Y-004 and INTX-003; recorded in U1a §12 |
| Validating A11Y-010 on a real DE build containing these paths | OPTIONAL | no existing build has them; creating one would be benchmark hunting (`loop.md` §15) |
| Anti-slop registry and visual references re-verification | DEFERRED BY DESIGN | fresh until about 2026-12-19 (90-day interval); runs on its own schedule |

## 17. Status of every item

- **COMPLETE:** matrix items 1, 2, 3, 4, 5, 6, 8, 9, 10, 11.
- **DEFERRED BY DESIGN:** 15, 17.
- **DEFERRED (human decision):** 7, 16.
- **OPTIONAL:** validation on a real DE build containing the new paths.
- **OUT OF SCOPE:** 12, 13, 14.

## 18. Commit SHA

This report is part of the milestone's single local commit, and a file cannot contain its own commit hash. The SHA is given in the final response and is visible with `git log -1`. Parent: `5225e09`. Nothing was pushed.
