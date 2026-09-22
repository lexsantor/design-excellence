# AUDIT-3.5.md

Record of the Phase 3.5 independent behavioral audit and the Phase 4 correction pass it drove. Source of truth for both phases: `ARCHITECTURE.md` and `FORENSIC-EXTRACTION.md`.

---

## Phase 3.5 Findings (recap)

Conducted by a fresh, non-fork subagent with zero prior context on this project — dispatched specifically to avoid auditing the implementation from the same context that built it. Full report was delivered in-session; summarized here for continuity.

**Verdict at the time: PASS WITH CORRECTIONS.**

Critical findings: (1) `accessibility.md` blanket-declared every rule P1 "by construction," violating the Authority Hierarchy's narrow-enumerated-P1 rule; (2) `SKILL.md §7`'s T3 loading condition was mode/stage-only, giving Scenario F ("make this hero less generic") no structural path to `anti-slop-registry.md`; (3) `DESIGN_VARIANCE` and `VISUAL_DENSITY` were defined but never consumed by any rule's `applicability` field — only `MOTION_INTENSITY` was; (4) `HARDEN-002` restated `existing-project-safety.md` §3 near-verbatim instead of pointing to it; (5) the `stacks/` V1 commitment from `ARCHITECTURE.md §22/§23` was silently reversed. Also flagged: a DIRECT/SHAPE routing contradiction (Scenario H), an AUDIT critique-exemption stated only in prose not in the routing table, and a misleading "genre-sliced loading" claim in `style-catalog.md` that the single-file implementation can't actually deliver.

The three "honesty" tests (fingerprint-as-redirect-not-blocker, independent-critique-limits, freshness-automation-absence) all passed with direct textual confirmation and were preserved unchanged in this correction pass.

---

## Phase 4 Correction Report

### Corrected

1. **P1 scope creep in `accessibility.md`** — removed the blanket "all rules are P1" header claim. Each of the 8 rules now carries its own `category`/`layer` field, classified individually against `SKILL.md §3`'s narrow enumerated list (contrast, focus-visible, keyboard operability, reduced-motion, plus fabrication/untrusted-content/destructive-editing). Result: A11Y-001, A11Y-002, A11Y-003, A11Y-006 remain P1 (each traces to a specific enumerated item — dragging-alternative is kept P1 because a drag-only interaction with no keyboard alternative is literally a keyboard-operability failure). A11Y-004 (icon accessibility) and A11Y-008 (never disable zoom) moved to P5. A11Y-005 (touch target size) moved to P5. A11Y-007 (form-field implementation bugs) moved to P7. Guidance content was preserved in full; only authority/severity changed, per the correction brief's explicit instruction not to solve this by moving the whole file to P2.
2. **Content-relevance loading path for `anti-slop-registry.md`** — `SKILL.md §7`'s T3 row now has a third loading path alongside mode/stage: a request whose content itself names genericness, distinctiveness, or "AI-generated" appearance triggers the load regardless of Task Mode or Scope. Explicitly worded as a judgment call (the same kind DEFINE-stage register/genre inference already makes), not a keyword-matcher, with paired positive/negative examples taken directly from the correction brief ("make this hero less generic" triggers it; "fix border radius," "fix mobile navigation" don't).
3. **`HARDEN-002` de-duplicated** — stripped the restated non-destructive-editing text; it is now a bare pointer to `existing-project-safety.md`, which remains the sole canonical location. The rule got shorter (571 → 546 words for the whole file, net).
4. **`DESIGN_VARIANCE` and `VISUAL_DENSITY` wired into real rules.** `DESIGN_VARIANCE`: `COLOR-001` (High band pushes the commitment ladder toward its higher tiers even against a lower genre default) and `LAYOUT-001` (High band raises the fingerprint distinctiveness bar specifically on the macrostructure dimension). `VISUAL_DENSITY`: `LAYOUT-001` (density band favors denser vs. more generously-spaced macrostructures) and a new rule, `LAYOUT-007` (spacing scale keyed directly to density band — closes a real content gap, since spacing had no rule-catalog representation at all before this). Two strong consumers per dial, not broad artificial wiring across dozens of rules. `SKILL.md §4` now names the actual consuming rule ids rather than leaving the "every rule consumes a band" claim unqualified.
5. **DIRECT/SHAPE routing contradiction resolved.** `SKILL.md §1`'s stage table now explicitly states: SHAPE runs for page/site-scope BUILD/REDESIGN, *or* for section scope specifically when a genuinely new section is being added to an existing page (not when polishing one). DIRECT stays page/site-scope only and does not re-run for a new section on an already-directed page. A new "Section-scope disambiguation" paragraph makes the improve-existing vs. add-new distinction explicit, and §2's BUILD-existing-project row was rewritten to match (the old `[DIRECT/SHAPE if new surface]` bracket, the source of the contradiction, is gone).
6. **AUDIT critique-exemption made explicit in the routing table**, not just in `critique-protocol.md`'s prose. `SKILL.md §1`'s CRITIQUE row now states "except Task Mode = AUDIT" directly, with the reasoning (no newly generated output exists to critique; the audit findings pass is itself the deliverable).
7. **`style-catalog.md`'s genre-slicing claim fixed.** No file split was created (four entries, ~700 words doesn't warrant fragmentation). The claim was rewritten to state honestly that the whole file loads in one read at its current size, "sliced to Genre" means attention, not a smaller read, and a real split becomes worth it only if the catalog grows substantially.
8. **Provenance citation added** to Core Principle 8 (`SKILL.md §9`) — now cites `content-copy.md` CONTENT-003, matching the citation style already used by principles 3, 9, and 10.
9. **`stacks/` decision documented explicitly** in `SKILL.md §7` — a short note states this diverges from `ARCHITECTURE.md`'s stated 1–2-by-default V1 scope, explains why (no repository this skill has run against has supplied real stack evidence, so a default file would have been fabricated content), and marks it a deliberate refinement, not an accidental omission.

### Deliberately unchanged

Per the correction brief's explicit preservation list — none of the following were touched:
- **Fingerprint** — still 5 dimensions, still explicitly "experimental — not settled fact," still a redirect signal never a hard blocker.
- **Independent critique** — the honest limitation language in `critique-protocol.md` is untouched; still refuses to treat a `fork` as genuine isolation, still states the Level-1-only fallback plainly if isolation isn't available.
- **Freshness** — `anti-slop-registry.md` still explicitly discloses no automated validator exists in V1.
- **Motion** — Emil's framework in `motion.md` remains the sole canonical motion decision system, untouched.
- **Stack detection approach** — kept exactly as implemented (on-demand, evidence-gated); only the *documentation* of that choice changed (item 9 above), not the behavior.
- **Existing-project safety** — non-destructive editing and Improve-vs-Replace in `existing-project-safety.md` untouched (it was the correct canonical version all along; `HARDEN-002` was the file with the problem).
- **Context schema** — `.design/context.md`'s schema in `SKILL.md §5` untouched.

### Before / After

| Metric | Before | After |
|---|---|---|
| `SKILL.md` word count | 1,917 | 2,439 (+522, +27%) |
| `accessibility.md` word count | 866 | 1,149 (+283 — per-rule layer justification text) |
| `performance-hardening.md` word count | 571 | 546 (**−25**, net reduction from de-duplicating HARDEN-002) |
| `color.md` / `layout-interaction.md` word count | 894 / 849 | 931 / 1,071 (+37 / +222 — dial wiring + new LAYOUT-007) |
| `style-catalog.md` word count | 706 | 777 (+71 — honest loading-claim rewrite) |
| Number of reference files | 13 | 13 (no new files; one new rule inside an existing file) |
| Number of rule-catalog entries | 47 | 48 (+`LAYOUT-007`) |
| P1-layer rules across the whole catalog | ~12 (several not on the enumerated list) | 9, every one traceable to a specific `SKILL.md §3` enumerated item |

**On the `SKILL.md` growth specifically:** re-measured per item 10's instruction. The +522 words are load-bearing corrections (a genuinely new routing mechanism, a genuinely new disambiguation rule, explicit table statements replacing ambiguous prose) — not padding. No "obvious reference material" was found that could move out of T0 without either losing routing-critical information or restructuring the file tree, which was out of scope for this pass. T0 still reads as router + decision engine + safety contract, not a reference manual — nothing added was catalog/example content, all of it is decision logic. This is reported honestly as an assessment, not forced toward a lower number for its own sake, per the brief's own "do not optimize merely for an arbitrary number" instruction.

### Critical Scenario Results

- **D** ("Fix the mobile navigation") — **unaffected, still lightweight.** Content-relevance check for anti-slop correctly does not fire (not about genericness/distinctiveness). No DEFINE/DIRECT/SHAPE/DESIGN/HARDEN/fingerprint. Loads `SKILL.md` + `layout-interaction.md` + `accessibility.md` (now correctly non-P1 for the touch-target-adjacent guidance it might cite) + `existing-project-safety.md` + `critique-protocol.md`. **PASS.**
- **F** ("Make this hero less generic") — **fixed.** The exact phrase now matches the content-relevance trigger's own worked example; `anti-slop-registry.md` loads. Still no DEFINE/DIRECT/SHAPE/DESIGN/fingerprint (routes as POLISH-of-an-existing-section per the new disambiguation, not BUILD). **PASS (was FAIL in Phase 3.5).**
- **G** ("Change the button border radius from 8px to 10px") — **unaffected, minimal.** Content-relevance check correctly does not fire — this exact phrase is the negative worked example in the fix itself. No DESIGN/SHAPE/typography/color/anti-slop/style-catalog/fingerprint. **PASS.**
- **H** ("Add a testimonial section to the homepage") — **fixed.** Now routes explicitly as BUILD-at-section-scope via the new disambiguation: SHAPE fires narrowly for the new section's own structure, DIRECT does not re-run (direction already established), DESIGN extends only if needed. Whether anti-slop's content-relevance path fires here is a genuine borderline judgment call (testimonials carry inherent fabrication/genericness risk per `SLOP-016`/`CONTENT-003`, but the request text itself doesn't name genericness) — left to agent judgment as designed, not forced either way. **PASS** (contradiction resolved; the borderline anti-slop question is a legitimate open judgment call, not a defect).
- **I** ("Make all animations feel more premium") — `motion.md` loads unambiguously; unrelated categories (color/typography/layout) correctly stay excluded. Level 2 critique correctly does not auto-trigger (no REDESIGN, no explicit stakes signal). **PASS**, with one known gap carried forward unchanged (see Remaining Issues — no explicit routing row exists for broad-but-narrow-category POLISH; this was flagged in Phase 3.5, was not in the P0–P2 correction list, and per the brief's own instruction ("if a new issue is minor, report it instead of expanding correction scope") was left alone rather than scope-expanded).
- **J** ("Use this exact screenshot as the visual reference") — **fixed.** P2 still correctly wins for subjective style. P1 override authority is now genuinely narrow: only A11Y-001/002/003/006 can trigger a disclosed override. A 20×20px tap target or a zoom-lock in the reference screenshot can be *noted* as P5 guidance but can no longer silently or authoritatively override the explicit "match exactly" instruction — exactly the scope-creep failure mode this scenario exists to catch, now closed. **PASS (was the exact failure mode in Phase 3.5).**

### Secondary Static Audit (post-correction)

- **Duplicate rule IDs:** none — every id across all 13 files is unique (verified via full-corpus grep).
- **New duplication introduced by these corrections:** none found. `A11Y-003` is a pointer to `MOTION-007`, not a restatement (explicitly labeled as such). `HARDEN-002` is now a bare pointer.
- **Dead dials:** resolved — `DESIGN_VARIANCE` and `VISUAL_DENSITY` each have two real rule-catalog consumers now (`COLOR-001`/`LAYOUT-001` and `LAYOUT-001`/`LAYOUT-007` respectively); `MOTION_INTENSITY` unchanged at one (`MOTION-002`).
- **P1 scope creep:** resolved for `accessibility.md`; a full-corpus grep for every `layer:** P1` occurrence (9 total, down from a blanket ~12) confirms each one traces to a specific `SKILL.md §3` enumerated item. No new P1 scope creep introduced elsewhere by this pass.
- **Unexplained architecture drift:** the `stacks/` divergence is no longer *unexplained* — it's now documented in `SKILL.md §7` as an intentional refinement, matching how every other V1.1/Future deferral in this skill is already disclosed.
- **Contradictory routing statements:** the DIRECT/SHAPE contradiction and the AUDIT critique-exemption inconsistency are both resolved — each concept now has exactly one authoritative statement (in the `SKILL.md` table itself), not a table-vs-prose split.
- **Misleading loading claims:** `style-catalog.md`'s genre-slicing claim corrected to describe what the implementation can actually deliver.
- **Unnecessary T0 content:** none identified as removable without restructuring the file tree (see Before/After discussion above) — reported, not forced.

### Remaining Issues

Only what genuinely remains, none of it introduced by this correction pass:

1. **No explicit routing row for broad-scope, single-category POLISH** (Scenario I's residual gap — "make all animations feel more premium" spans the whole product but only touches one rule category). Not in the P0–P2 list for this pass; carried forward as a known, reported gap.
2. **Genre/register inference mechanism is still underspecified** — `SKILL.md §5` states the declare-and-let-the-user-correct surface behavior but gives no keyword/signal table the way Taste's original source did. Noted in Phase 3.5, not part of this correction's scope, carried forward.
3. **T2 rule-catalog category selection has no hard boundary** (Scenario G's residual note — nothing mechanically prevents an over-cautious application of the skill from pulling in an unnecessary category "just in case"). This is inherent to a prompt-driven router rather than an executable one; flagged, not solved, consistent with this being a judgment-call system by design.
4. **The `Read` tool truncation issue** (a claude-mem hook silently returning only line 1 of files with prior observations) is an environment/tooling issue, not a skill defect — both this correction pass and the Phase 3.5 audit worked around it via `Bash cat`, but it's worth the user's attention separately since it's a silent-corruption risk for any future work in this environment that trusts `Read`'s output uncritically.

None of the above were expanded into new corrections, per the brief's explicit instruction to report rather than scope-creep on newly noticed minor issues.

### Recommendation

**READY FOR REAL-WORLD TESTING.**

D, F, G, and J — the four scenarios the brief specifically requires to behave correctly before this recommendation can be made — all pass, verified against the actual corrected routing table and rule content, not asserted. The remaining issues listed above are genuine but minor, none of them reopen a P0/P1 finding, and none of them were papered over — they're named specifically so a future pass can address them deliberately rather than them surfacing as a surprise.
