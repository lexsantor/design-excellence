# Phase 10.7 — Results
## Principle Pool integration: EXPLORE behavioral benchmark

**Status:** Phase completed  
**Scope:** first entry in `references/principle-pool.md` (PRN-0001), `SKILL.md` §1 activation clause and §7 T3 row, LAYOUT-010 two-pool wording.  
**Method:** behavioral benchmark in the Phase 6.5 format. Five cases, run by three independent fresh-context executors against the working tree of this commit. Each was confined to the skill folder, read-only, reasoning through routing, loading and LAYOUT-010 selection only (no build, no render). Only observed behavior is recorded; there are no scores.

---

## 1. Result

**PASS.** All five cases pass. Both pools load together under the existing DIRECT/DESIGN trigger, LAYOUT-010 treats them as one source, at most 3 entries are ever seriously considered, PRN-0001 informs a candidate when compatible and applicable and is discarded when it is not, and neither pool loads in CRITIQUE.

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | A visual-system exploration loads both pools together | Cases 1, 2, 3, 5: both files loaded in one step via the §7 rows | PASS |
| 2 | LAYOUT-010 considers them as one source | Cases 1, 2, 3, 5: steps 1–3 screened all 10 entries of both files in one pass | PASS |
| 3 | At most 3 entries considered in total | Case 1: 3 (PRN-0001, REF-009, REF-004); Case 2: 3 (REF-009, REF-008, REF-007); Case 3: 2; Case 5: 2 | PASS |
| 4 | Family tie-break operates across both pools | Not reached naturally in Cases 1–3 (no tie). Case 5 imposed the tie condition: step 4 compared PRN-0001's `family` with REF-001's tradition from the `visual-references.md` header, preferred the differing family, and never promoted an entry that failed steps 1–3 | PASS, with follow-up F1 |
| 5 | PRN-0001 can inform a candidate | Case 1 (committed Candidate A) and Case 5 (Candidate B) | PASS |
| 6 | No source imitation | Cases 1 and 5 checked every trait named in PRN-0001's `non_application_note` and reproduced none; no "make it look like X" reasoning | PASS |
| 7 | Anti-Slop remains active | Cases 1–3 loaded `anti-slop-registry.md` and checked candidates by SLOP id; Case 4 loaded it for CRITIQUE | PASS |
| 8 | No catalog or runtime lookup | All executors report reading nothing outside the skill folder; no file in the skill folder points outside itself (static grep) | PASS |
| 9 | Incompatible brief discards PRN-0001 | Case 2 (product-led workspace): discarded at step 1, register; its `do_not_apply_to` #1 also matches. Case 3 (continuous-scroll magazine): discarded at step 2, `do_not_apply_to` "Sites whose value is the continuous scroll" | PASS |
| 10 | No convergence on the source as a whole | Case 1: the adopted candidate took only the page-extent principle; proportions, type pairing, colour, and fact placement came from the brief (facts moved into the text column, three brief-supplied facts); the rejected candidate used no reference. Case 2 committed a different entry entirely | PASS |

## 2. Cases

### Case 1 — Brand-led maker entry page (compatible)
- **Routing:** page-scope BUILD, genuinely-empty; brand-led, editorial; variance Medium, motion Low, density Low. Concept: HYPOTHESIS (LAYOUT-009 inactive).
- **Loaded:** `SKILL.md`, `style-catalog.md`, `layout-interaction.md`, `visual-references.md` + `principle-pool.md` (together), `anti-slop-registry.md`.
- **Step 1:** discarded REF-002 (motion), REF-007, REF-008 (register/genre). **Step 2:** discarded REF-003 (growing set), REF-005 (no real process material), REF-006 (Low motion, no fixed count). PRN-0001 matched none of its seven `do_not_apply_to` clauses.
- **Step 3:** PRN-0001 adopted; REF-009 judged not materially different from the Genre default; REF-004 judged unnecessary. Step 4 not invoked (no tie).
- **Candidates:** A "Frame-bounded entry unit" (PRN-0001; committed) vs B "Masthead and captioned plate" (no reference); differ on composition, imagery, typography.
- **Non-application check:** no source proportions, type pairing, emphasis, colour theme or fact-band labels/placement.
- **Result: PASS.**

### Case 2 — Product-led analytics workspace (incompatible)
- **Routing:** page-scope BUILD; product-led, modern-minimal; variance Low, motion Low, density Medium.
- **Loaded:** same set as Case 1, both pools together.
- **Step 1:** PRN-0001 discarded ("brand-led" only; notes "Brand register only"), with REF-001..006. **Step 3:** REF-009 adopted (rule-segmented chart strip), REF-008 and REF-007 considered and not adopted.
- **Result: PASS.**

### Case 3 — Brand-led long-form magazine with endless stream (register-compatible, not applicable)
- **Routing:** multi-page-site BUILD; brand-led, editorial; motion Low, density Low.
- **Step 1:** PRN-0001 passed. **Step 2:** PRN-0001 discarded by "Sites whose value is the continuous scroll, such as feeds, long-form reading or catalogues."
- **Step 3:** REF-001 adopted into Candidate B, REF-004 not adopted. 2 entries considered.
- **Result: PASS.**

### Case 4 — CRITIQUE of an existing landing page
- **Routing:** CRITIQUE mode. Loaded `existing-project-safety.md`, `critique-protocol.md`, `anti-slop-registry.md`, `style-catalog.md`.
- `visual-references.md` and `principle-pool.md` **not loaded** (§7: DIRECT/DESIGN only, never CRITIQUE/AUDIT). No critique rule refers to either pool.
- **Result: PASS.**

### Case 5 — Targeted step-4 tie-break
- Brand-led studio entry page. Steps 1–2 left PRN-0001 and REF-001. Step 3 favored PRN-0001 (no natural tie).
- Imposed condition: Candidate A already informed by a `visual-references.md` entry. Step 4 read PRN-0001's `family` field and REF-001's tradition from the `visual-references.md` header ("web/documentation/editorial-adjacent"), judged them different, and preferred PRN-0001. It never selected REF-007..009, which failed step 1.
- The executor could not read `SKILL.md` past line 120 (environment read denial); §7 behavior is covered by Cases 1–4.
- **Result: PASS**, with follow-up F1.

## 3. Follow-ups (not blockers; outside this phase's authorized edits)

- **F1.** `visual-references.md` has no `family` field; its traditions are header prose, while pool entries use a `family` value. The cross-pool comparison works by judgment and would be ambiguous for near-synonymous traditions. A shared tradition vocabulary would need a `visual-references.md` change, which this phase does not authorize.
- **F2.** LAYOUT-010 "Consider at most 2–3 entries" reads against steps 1–2, which screen every entry. Executors consistently read "considered" as weighed at step 3. This wording predates this phase.
- **F3.** LAYOUT-010's `freshness` line names only `visual-references.md`. The pool's freshness rule lives in its own header, as designed.
- **Environment:** a read hook truncated the Read tool to line 1 in all executors; they read files with read-only shell commands instead. Not a skill defect.

## 4. Not validated

- No build or render was run; this benchmark covers routing, loading and selection only, as in Phase 6.5.
- The step-4 tie-break was exercised only under an imposed condition, not a natural tie.
- PRN-0001's frames other than one wide landscape and one narrow portrait frame remain unverified, as its own `do_not_apply_to` states.
