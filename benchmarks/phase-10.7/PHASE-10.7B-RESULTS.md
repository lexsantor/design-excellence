# Phase 10.7B — Results
## Principle Pool governance hardening: regression

**Status:** Phase completed  
**Scope:** follow-ups F1–F3 from `PHASE-10.7-RESULTS.md` §3. Edits: LAYOUT-010 (`layout-interaction.md`) and one header phrase in `principle-pool.md`. `visual-references.md`, `SKILL.md`, Anti-Slop and the PRN-0001 entry are unchanged.  
**Method:** one fresh-context read-only executor confined to the skill folder, Phase 6.5 format, reasoning through LAYOUT-010 only. Observed behavior only; no scores.

---

## 1. Changes

| Follow-up | Change | Where |
|---|---|---|
| F1 family vocabulary | Step (4) states where each pool's family comes from: `family` in `principle-pool.md`; in `visual-references.md` the tradition its header assigns (REF-001–REF-006 one web/documentation/editorial-adjacent family; REF-007–REF-009 each its own named tradition). The comparison is qualitative; when it is unclear whether two traditions differ, family diversity gives no preference. No per-entry field, no new labels | LAYOUT-010 selection |
| F2 screening vs consideration | "Consider at most 2–3 entries in total across both pools, never a whole file" replaced by: steps (1)–(2) screen every entry of both pools; only survivors are weighed under (3)–(4); at most 2–3 entries in total across both pools are seriously considered for adaptation. `principle-pool.md` header aligned ("every entry is screened, and at most 2–3 … are seriously considered") | LAYOUT-010 selection; pool header |
| F3 freshness | Freshness line names both files' fields (`last_verified_date`, `review_interval_days`) and points to `principle-pool.md`'s header staleness rule | LAYOUT-010 freshness |

Selection order, the combined 2–3 limit and the tie-breaker-only status of step (4) are unchanged.

## 2. Regression

| Case | What it tests | Observed | Result |
|---|---|---|---|
| R1 brand-led studio entry page, imposed tie | F1 | Steps 1–2 screened all 10 entries; survivors REF-001 and PRN-0001; no natural tie. Under the imposed condition, the executor quoted the new family-source text, read REF-001's family from the header and PRN-0001's from its field, judged it unclear whether a commercial template tradition differs from the broad web/editorial-adjacent group, and applied "no preference"; the choice fell back to step 3 (PRN-0001). No entry that failed steps 1–3 was selectable | PASS |
| R2 brand-led maker entry page | F2 | Executor quoted the new wording, screened 10, seriously considered 3 (REF-001, REF-009, PRN-0001), found no wording suggesting that only 2–3 entries are inspected in LAYOUT-010, and confirmed the priority order (1)→(4) unchanged | PASS |
| R3 freshness | F3 | Line covers both files; consistent with the pool header rule and the Visual References fields; PRN-0001 fresh (2026-09-25 + 90 = 2026-12-24) | PASS |

The executor flagged that the pool header still read "at most 2–3 entries are considered". It was aligned in this phase (§1, F2).

## 3. Remaining ambiguity (not changed; outside this phase's scope)

- **Visual References overdue entries.** `visual-references.md` carries freshness fields but states no rule for an overdue entry; only `principle-pool.md` does. Resolving it would need a `visual-references.md` change. No entry is overdue before 2026-12-20.
- **Broad family label.** REF-001–REF-006 share one broad header tradition, so comparisons with other web-derived families will often land on "no preference". This is deliberate: it avoids false precision.
- **Step 1 vs step 2 placement.** Some `compatible_with` fields carry brief-shape conditions (REF-003, REF-009) that overlap `do_not_apply_to`; the outcome is the same either way. Predates this phase.
