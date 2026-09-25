# Phase 11 — Results
## Principle Pool: second entry (PRN-0003), EXPLORE behavioral benchmark

**Status:** PASS
**Scope:** one new entry appended to `references/principle-pool.md` (PRN-0003). No other file in the skill changed: `SKILL.md`, LAYOUT-009/010, `visual-references.md`, Anti-Slop, routing, T4 files and the PRN-0001 entry are untouched. The pool header is unchanged: ceiling 15, first pass 8, at most 2 per production cluster, the freshness rule, and the identity boundary.
**Method:** behavioral benchmark in the Phase 6.5 / 10.7 format. One fresh-context read-only executor was confined to the skill folder and ran against the working tree containing the new entry. It reasoned through routing, §7 loading and LAYOUT-010 selection only, with no build and no render. Only observed behavior is recorded; there are no scores.

---

## 1. Result

| # | Check | Evidence | Result |
|---|---|---|---|
| a | Both pools load together only under the DIRECT/DESIGN trigger, never in CRITIQUE/AUDIT | §7 T3 rows; Case 4 loaded neither pool | PASS |
| b | LAYOUT-010 treats both pools as one source and screens every entry | Cases 1, 2, 3, 5 screened all 11 entries at steps 1–2 | PASS |
| c | At most 3 entries seriously considered | 3 / 1 / 3 / 0 / 3; Cases 3 and 5 cut 4 step-2 survivors to 3 | PASS |
| d | PRN-0003 can inform a candidate | Case 1 (deployment-record launch page), Case 5 (recipe publisher) | PASS |
| e | PRN-0003 discarded when incompatible or not applicable | Case 2: register, plus "Working views in a product the user operates". Case 3: "Items that carry only a name or a caption" | PASS |
| f | PRN-0003 never mandatory and never a CRITIQUE/AUDIT bar | Pool header "none is ever required … never a quality bar"; Case 4 | PASS |
| g | No `non_application_note` trait reproduced | Checked trait by trait for PRN-0003 (Cases 1, 5) and PRN-0001 (Cases 3, 5) | PASS |
| h | Anti-Slop active | T3 loads it at DIRECT/DESIGN; SLOP-005/007 cited when shaping PRN-0003's fields | PASS |
| i | No file points outside the skill folder | No absolute paths, curation-record ids or URLs; "catalog" appears only as "never read or queried at runtime" | PASS |
| j | PRN-0001 behaves as before | Adopted in Cases 3 and 5 (bounded brand-led entry); discarded in Case 1 (content cannot fit one frame) and Case 2 (register) | PASS |

## 2. Cases

### Case 1 — Brand-led launch page for a service that keeps versioned deployment records
- **Routing and survivors:** brand-led, modern-minimal, variance Medium, motion Low. After steps 1–2 the survivors were REF-001, REF-009 and PRN-0003.
  - PRN-0001 was discarded at step 2 ("Entry content that cannot fit one wide frame…").
  - REF-002..008 were discarded at step 1 or 2 by quoted clauses.
- **Step 3:** 3 entries seriously considered; step 4 not reached.
- **Candidate A (PRN-0003):**
  - The "every deploy is recorded" claim becomes fields on every example.
  - The "any deploy can be restored" claim becomes a rollback example naming the deployment it restores.
  - The "fast" claim stays a stated claim ("Claims that no item can carry stay stated claims").
  - Fields are laid out as labelled rows in a ledger, not middle-dot strings or a card grid.
- **Result: PASS.**

### Case 2 — Product-led analytics workspace
- PRN-0001 and PRN-0003 were both discarded at step 1 (register), and PRN-0003 also by "Working views in a product the user operates".
- REF-009 was the only survivor (1 entry considered).
- **Result: PASS.**

### Case 3 — Brand-led consultancy entry page with no inspectable records
- PRN-0003 was discarded at step 2 ("Items that carry only a name or a caption").
- Four entries survived; three were seriously considered (PRN-0001, REF-003, REF-004).
- Step 4 was reached between REF-003 and REF-004, which share one header tradition, so it gave no preference.
- Candidate A used PRN-0001, with none of its traits reproduced.
- **Result: PASS.**

### Case 4 — CRITIQUE of an existing landing page
- Neither pool loaded.
- `critique-protocol.md` does not refer to either pool, and no PRN acted as a criterion.
- **Result: PASS.**

### Case 5 — Brand-led recipe publisher, single bounded home requested
- **Survivors:** REF-004, REF-009, PRN-0001 and PRN-0003. Three were seriously considered (PRN-0001, PRN-0003, REF-009). **Both PRN entries reached step 3.**
- **Step 4:** the two PRN entries have identical `family` values, so family gave no preference between them. They are not rivals: one decides macrostructure, the other content architecture, and both informed Candidate A.
- **Candidate B:** REF-009, a different production tradition, preferred only as a tie-break between comparably useful entries.
- **Convergence:** the candidates did not converge on one production tradition. No traits of either PRN entry were reproduced.
- **Result: PASS.**

## 3. Ambiguities reported by the executor (non-blocking, not changed)

1. **PRN-0003 first `do_not_apply_to` clause.** It reads as guidance for part of a brief (claims with no item trace stay stated). A strict step-2 reader could discard the whole entry when a brief has one such claim. The failure is safe: the entry is simply not used. Rewording would be a new curation review.
2. **"At most 2–3".** The text does not say how to cut when 4 entries survive steps 1–2 (Cases 3, 5). The executor cut on step-3 usefulness. This predates this phase.
3. **PRN-0001 and PRN-0003 on one page.** PRN-0001 excludes entry content that needs "cutting parts, hiding them"; PRN-0003 lets item fields move into a detail view on constrained frames. They govern different scopes (entry-view extent vs item fields). Worth watching if both are adopted for one entry view.
4. **PRN-0001's "catalogues" clause vs an explicit user request for a bounded home.** P2 already governs this. Predates this phase.
5. **Visual References.** No `family` field; the header tradition is plural prose. The header does not restate the combined source. Predates this phase (10.7 follow-up F1).
6. **Shared `family`.** Both PRN entries share one production tradition. The pool header's cluster limit is enforced at curation time; the entries come from different production clusters, and cluster keys are deliberately not carried here.
7. **§5 logging.** It names "a Visual Reference"; LAYOUT-010's validation covers any entry. Predates this phase.
8. **§7 trigger on a DESIGN-only run.** The pools can load where no EXPLORE step consumes them. Harmless: nothing reads them. Predates this phase.
9. **History citations.** Phase results citations are not marked as non-shipped. Predates this phase.

None contradicts the integration contract. No skill text was changed in response.

## 4. Integrity

- **Changed:** `design-excellence/references/principle-pool.md` (one entry appended; every prior byte unchanged) and this report.
- **Unchanged:** all other skill files and the pre-existing untracked `rules.md` and `scratchpad/`.
- **Pool after this phase:** 2 entries (PRN-0001, PRN-0003), both accepted and fresh until 2026-12-24.
