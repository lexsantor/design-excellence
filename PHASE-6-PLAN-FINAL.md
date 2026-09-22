# PHASE 6.0 — Creative Direction Correction Plan (FINAL)

Status: **PLAN ONLY.** No file inside the skill package (`design-excellence/design-excellence/`) has been modified. This document revises `PHASE-6-PLAN.md` per the review corrections below. Full evidence citations (file:line, benchmark artifacts) live in `PHASE-6-PLAN.md` §2 and are not restated here except where a correction changes what the evidence is taken to mean.

**Corrections applied from `PHASE-6-PLAN.md`:** CD-1 now requires candidates be meaningfully distinct on ≥2 of {composition, imagery, typography, color, materiality, interaction} — not label-only variants. Atmospheric-Expressive is no longer framed as the required or "correct" outcome anywhere in this plan — Genre selection is judged on evidence-use, not on which Genre gets picked. AS-1 explicitly creates no new catalog. VAL-1 now respects the existing Core-v1/Enhanced capability split and requires explicit "skipped — capability unavailable" reporting instead of silent pass. HERO-1 no longer prescribes a default fix. CRIT-1 is a routing trigger only — it must never claim Level 2 ran if it didn't. DENS-1 is deferred out of this phase entirely.

---

## 1. Executive diagnosis

The benchmark exposed two distinct failure classes, and Phase 6 corrects the process, not the output:

1. **A process gap at DIRECT.** DIRECT commits to a single direction without generating and comparing genuine alternatives. The one alternative that was logged (Atmospheric-Expressive, in `.design/context.md`'s Rejected Directions) was rejected on a premise not actually present in `style-catalog.md`'s own definition of that Genre. This is evidence of weak evidence-use in the rejection, not evidence that Atmospheric-Expressive was the "right" answer — Phase 6 does not correct this by pointing the system at a preferred Genre. It corrects it by requiring that (a) at least one real, meaningfully-distinct alternative is considered, and (b) any rejection is checked against what the cited reference material actually says, whichever Genre that leaves standing.

2. **A gestalt/enforcement gap at Anti-Slop and VALIDATE.** `anti-slop-registry.md`'s SLOP-011 already names the exact color/type/accent cluster the benchmark produced as a documented model self-tell, and a separately mechanically-countable rule (SLOP-003, eyebrow-label ratio) was violated in a way its own stated check would have caught. Both rules already exist correctly specified. The gap is that no step compares a finished direction against SLOP-011 as a *combination*, and mechanically-countable rules across the catalog aren't guaranteed to actually gate SHIP.

**Explicit guardrail for this phase (per review correction 14):** success is measured by whether the *decision process* used real evidence and real comparison — not by whether the output becomes more atmospheric, more image-heavy, or more experimental. A re-test that lands on Editorial again, with a real second candidate genuinely compared and a rejection reason that correctly cites the style catalog, is a **pass**. A re-test that lands on Atmospheric-Expressive without that comparison having happened is a **fail**. Phase 6 must not trade one unconsidered convergence for another.

---

## 2. Confirmed gaps (condensed — full evidence in `PHASE-6-PLAN.md` §2)

| Gap | Evidence | Status |
|---|---|---|
| DIRECT has no candidate-generation/comparison step | Rejected Directions logged only anti-pattern avoidances the brief already banned + one alternative rejected on a premise absent from its own catalog entry | CONFIRMED |
| Genre-inference in `SKILL.md` §4 has no concrete anchor for weighing brief emotional-register language against category/vertical defaults | `ARCHITECTURE.md` §24 Scenario A contains a worked example that didn't survive compression into T0 | CONFIRMED |
| Anti-Slop has no gestalt/cluster-level check | SLOP-011 is written as a combination; every element of the reproduced cluster individually passed its own atomic rule | CONFIRMED |
| A mechanically-countable Anti-Slop rule (SLOP-003) was not enforced before SHIP | Eyebrow count (6) exceeded the rule's own stated ceiling (3) | CONFIRMED — execution gap, not a rule-content gap |
| No decision framework exists for imagery/art direction | Single grep hit across the entire package, explicitly excluding imagery from any tracked criteria | CONFIRMED |
| `DESIGN_VARIANCE`'s two real consumers (`COLOR-001`, `LAYOUT-001`) leave Medium band unspecified | Both rules define High/Low behavior only | CONFIRMED |
| No rule detects headline orphan/widow/awkward wrap | Zero hits for orphan/widow/rag across the package; `INTX-003` covers clickable text only | CONFIRMED |
| Level 2 (independent) critique has no trigger for a brand-critical greenfield BUILD | `ARCHITECTURE.md`'s own Scenario A for this exact brief recommends it; `critique-protocol.md`'s trigger list doesn't cover this case | CONFIRMED |
| `LAYOUT-001` references a macrostructure-bundle catalog that is never populated anywhere | Bundle names appear only in `LAYOUT-001`'s own prose | CONFIRMED — deferred, not fixed, this phase (see DENS-1 below) |

---

## 3. Proposed changes (corrected)

### CD-1 — Lightweight EXPLORE step inside DIRECT
- **Correction applied:** candidates must be meaningfully distinct on **at least 2** of {composition, imagery, typography, color, materiality, interaction} — not two labels for the same aesthetic (e.g. "editorial-light" vs. "editorial-dark" does not qualify).
- **Change:** for page/multi-page-site BUILD/REDESIGN only, DIRECT states 2 candidate directions before committing — one line each, naming which ≥2 dimensions distinguish them from each other. This reuses the existing Rejected Directions mechanism in `.design/context.md`; it does not generate full designs, mockups, or a style catalog.
- **Files:** `SKILL.md` §1 (DIRECT row), `SKILL.md` §5 (Rejected Directions requirement).
- **Risk:** low — additive, two sentences of reasoning, no P1/accessibility interaction.

### CD-2 — Cross-check rejection rationale against the cited reference's actual text
- **Change (unchanged from `PHASE-6-PLAN.md`, approved as-is):** when a Genre or direction is rejected and `style-catalog.md` is already loaded (T3, DIRECT/DESIGN per `SKILL.md` §7), the stated rejection reason must be checked against that entry's own `best_for`/`keywords`/`do_not_use_for` fields. If the rejection reason isn't actually in the entry, that's a signal to re-examine, not proceed on the assumption.
- **Explicit non-goal:** this does not mean the check must conclude in favor of the entry being reconsidered — it means the reasoning must be traceable to real text, whatever conclusion follows.
- **Files:** `SKILL.md` §5.

### CD-3 — Genre-inference anchor, reframed as process not outcome
- **Correction applied:** the anchor illustrates that brief emotional/register language deserves the same concrete weight as category/vertical defaults — it does **not** instruct "calm → Atmospheric-Expressive" as a rule to follow. The one-line addition to `SKILL.md` §4 states the *failure mode* to avoid (defaulting to a category stereotype like "healthcare brief → editorial-premium" without weighing the brief's actual register language against it), not a preferred answer.
- **Files:** `SKILL.md` §4.
- **Risk:** low.

### AS-1 — Gestalt/cluster check for combination-style Anti-Slop entries
- **Change (approved, with explicit constraint honored):** at CRITIQUE Level 1's Genericness axis (`critique-protocol.md`), add one explicit sub-check comparing the finished direction's color/type/accent combination against SLOP-011's existing named clusters as a whole. **No new catalog, no new entries, no new visual reference data** — this reuses SLOP-011's existing text verbatim as the comparison target.
- **Files:** `critique-protocol.md` (Level 1 axis 1), optional one-line cross-reference in `anti-slop-registry.md` SLOP-011 pointing at where the check now lives (content of the entry itself unchanged).
- **Risk:** low.

### VAL-1 — Mechanically-countable rules gate SHIP, proportional to available validation capability
- **Correction applied:** the original proposal risked implying every mechanically-countable rule always gates SHIP regardless of environment. Corrected: gating applies **only when the required validation capability is actually available** — this reuses the existing Core-v1 (no-browser-required, text/DOM-countable) vs. Enhanced (rendered, browser-tooling) distinction already present in `SKILL.md`/`ARCHITECTURE.md`. Rules checkable without rendering (e.g. SLOP-003's eyebrow count, TYPE-001's font-family count) gate in Core v1. Rules requiring rendered output (e.g. INTX-003's wrap detection, the new HERO-1) gate only when Enhanced mode/rendering is available.
- **New requirement:** when a mechanically-countable check cannot run because the capability is unavailable, VALIDATE must explicitly report it as **skipped — capability unavailable**, not silently treat it as passed. This is a reporting requirement, not a new mechanism — `critique-protocol.md`'s Level 2 already models this exact honesty pattern ("state plainly that Level 2 was not available... rather than presenting a self-review as if it were independent"); VAL-1 applies the same principle to mechanical gates.
- **Files:** `SKILL.md` §1 (VALIDATE row).
- **Risk:** low-medium — real per-task cost when capability is available, but explicitly proportional (§1's existing cost model), and never fabricates a pass.

### VAR-1 — Medium-band behavior for DESIGN_VARIANCE's existing consumers
- **Change (approved, unchanged):** one line each in `COLOR-001` and `LAYOUT-001` stating Medium-band behavior explicitly, so a Medium-declared variance can't land at the genre's most conservative option on every axis simultaneously. **No new dial consumers added** — only the two existing ones (`COLOR-001`, `LAYOUT-001`) are touched.
- **Files:** `color.md`, `layout-interaction.md`.
- **Risk:** low.

### IMG-1 — Imagery/art-direction decision procedure
- **Correction applied:** explicitly a decision *procedure*, not a requirement to use imagery. "No imagery, deliberately justified" remains a fully valid outcome. The procedure must let the answer distinguish generic stock imagery (avoid) from purposeful art direction, original photography, illustration, abstract visual systems, or other appropriate media (all legitimate, decided case-by-case) — not default to "no imagery" as the only option ever considered, which was the actual gap.
- **Change:** one new rule in `layout-interaction.md`, matching `TYPE-002`'s existing generative-procedure format (a sequence of questions, not a constraint): (1) does the subject/brief warrant visual weight beyond type+color, state yes/no with reason; (2) if yes, what medium is actually appropriate given what's available (provided/original photography, illustration, abstract graphic system, AI-generated imagery) — reject only genuinely generic/stock-looking treatments, not the category of imagery itself; (3) what role it plays; (4) how it interacts with the chosen macrostructure.
- **Files:** `layout-interaction.md` (new rule).
- **Risk:** low.

### HERO-1 — Responsive headline/hero integrity check
- **Correction applied:** removed the prescribed default fix (non-breaking space). The rule now only specifies **detection** — orphaned single words, widows, or awkward rag on a display/hero headline at a declared breakpoint — and lists multiple legitimate remediation strategies without ranking one as default: container/measure width adjustment, type-scale/font-size adjustment, explicit line-break placement, copy adjustment, or non-breaking grouping where genuinely appropriate. Which strategy applies is a per-case judgment, same as other P5/P8-layer rules in this catalog.
- **Change:** new rule `TYPE-006` in `typography.md`, using `INTX-003`'s existing validation pattern (mechanical-countable, rendered, Enhanced mode, checked at declared breakpoints) applied to one additional element class.
- **Files:** `typography.md` (new rule).
- **Risk:** low — subject to VAL-1's capability gating (requires rendering; reports as skipped if Enhanced mode is unavailable).

### CRIT-1 — Level 2 trigger only, never a fabricated outcome
- **Correction applied:** this change adds **one routing trigger condition** to `critique-protocol.md`'s existing Level 2 trigger list — a genuinely-empty, multi-page-site BUILD where the brief states an explicit brand-quality bar escalates to Level 2 by default, matching how REDESIGN already escalates. It does **not** change what Level 2 *is* or guarantee it produces a result. `critique-protocol.md`'s existing honesty clause already governs this ("if a future environment... does not provide [isolated dispatch]... state plainly that Level 2 was not available... rather than presenting a self-review as if it were independent") — CRIT-1 relies on that existing clause rather than adding new fabrication-prevention logic. The output must state, explicitly, whether Level 2 actually ran, and if not, why.
- **Files:** `critique-protocol.md` (Level 2 trigger conditions).
- **Risk:** low-medium — real dispatch cost when the trigger fires and the mechanism is available; zero risk of a false claim, since the existing honesty clause already covers the unavailable case.

### DENS-1 — DEFERRED, not in scope for this phase
- **Correction applied:** per review correction 10, do not populate `LAYOUT-001`'s referenced macrostructure-bundle catalog in this phase. The broken cross-reference in `LAYOUT-001` (naming Bento Grid/Long Document/Marquee Hero/Specimen/Manifesto without defining them) remains a known, documented gap, deferred to a future phase. This also keeps Phase 6 aligned with review correction 12 (prefer modifying existing rules over creating new catalog content) — populating that catalog is the one item in the original plan that was genuinely new content rather than a correction to existing content.
- **Files:** none this phase.
- **Note:** `VISUAL_DENSITY`'s scope is not otherwise expanded this phase either — VAR-1 only touches `DESIGN_VARIANCE`'s two consumers. No density-scope change is proposed.

---

## 4. Files affected

- `SKILL.md` — §1 (DIRECT row: CD-1; VALIDATE row: VAL-1), §4 (Genre-inference process anchor: CD-3), §5 (Rejected Directions requirement: CD-1, CD-2).
- `references/rule-catalog/typography.md` — new rule `TYPE-006` (HERO-1).
- `references/rule-catalog/layout-interaction.md` — new rule for imagery decision procedure (IMG-1); `LAYOUT-001` Medium-band clarification (VAR-1).
- `references/rule-catalog/color.md` — `COLOR-001` Medium-band clarification (VAR-1).
- `references/critique-protocol.md` — one new Level 2 trigger condition (CRIT-1); one sub-check added to Level 1 axis 1 (AS-1).
- `references/anti-slop-registry.md` — optional one-line cross-reference on SLOP-011 (AS-1); no content change to the entry itself.

## 5. Files not affected

- `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md` — historical, not runtime dependencies.
- `references/style-catalog.md` — **no changes this phase** (DENS-1 deferred; CD-2 reads this file but does not modify it).
- `references/existing-project-safety.md`, `references/gesture-physics.md` — untouched, no finding implicates them.
- `references/rule-catalog/motion.md`, `references/rule-catalog/accessibility.md`, `references/rule-catalog/content-copy.md`, `references/rule-catalog/performance-hardening.md` — no finding implicates any rule in these four files.
- `AUDIT-3.5.md`, `PHASE-6-PLAN.md` — prior-phase historical records.
- Everything inside `design-excellence-benchmark/` — evidence, not something corrected in place; any re-test runs as a fresh generation.

---

## 6. Implementation order

1. **HERO-1** (`typography.md`) — isolated, reuses `INTX-003`'s existing validation pattern, no dependency on any other change.
2. **VAL-1** (`SKILL.md` VALIDATE row) — enforcement + capability-gating + honest-reporting requirement; makes HERO-1 and every existing mechanically-countable rule actually gate output where capability allows.
3. **CD-3** (`SKILL.md` §4) — single-sentence process anchor, independent of the others.
4. **CD-1 + CD-2** (`SKILL.md` §1, §5) — shipped together; CD-2 is what makes CD-1's rejection reasoning trustworthy.
5. **AS-1** (`critique-protocol.md` Level 1) — more meaningful once CD-1/CD-2 exist (DIRECT is actually producing/rejecting real alternatives), but independently shippable.
6. **CRIT-1** (`critique-protocol.md` Level 2 trigger) — independent; grouped with AS-1 for one consolidated edit to `critique-protocol.md`.
7. **VAR-1** (`color.md`, `layout-interaction.md`) — independent, low-risk.
8. **IMG-1** (`layout-interaction.md` new rule) — ships after CD-1 exists, since the imagery decision is naturally exercised during the same DIRECT pass now producing real alternatives.
9. **DENS-1** — explicitly not scheduled this phase.

Each item ships and is independently testable before the next lands — no batched single edit pass, consistent with `SKILL.md` Core Principle 12 (leverage over coverage) and review correction 12 (keep the implementation small).

---

## 7. Risks

- **CD-1 risk:** a "meaningfully distinct on ≥2 dimensions" requirement is a judgment call, not a mechanical check — risk of the two candidates still being superficially different rather than genuinely distinct. Mitigation: the requirement to *name* which dimensions differ, logged in Rejected Directions, makes the judgment call auditable after the fact, even if not mechanically enforced at generation time.
- **VAL-1 risk:** the capability-gating requirement adds a new failure mode — a task that silently never has Enhanced mode available would never get HERO-1/INTX-003 gating, and could ship the same class of defect indefinitely if nobody notices the "skipped — capability unavailable" report. Mitigation: this is a known, disclosed limitation, not a silent one — the report itself is the safeguard, consistent with the existing honesty pattern in `critique-protocol.md`.
- **CRIT-1 risk:** the new trigger increases dispatch cost for a specific class of task (brand-critical greenfield BUILD). Mitigation: this is a narrow, already-precedented trigger class (REDESIGN already escalates by default for analogous reasons).
- **General risk:** any of these changes could be interpreted, in a future pass, as license to add more rules over time, re-approaching the "more rules" trap the original benchmark diagnosis warned against. Mitigation: implementation order (§6) and the explicit files-not-affected list (§5) are the guardrail — nothing here creates a new reference file, and DENS-1 (the one item that would have required new catalog content) is deferred.
- **Guardrail risk (review correction 14):** the risk this whole phase most needs to watch is over-correcting toward a different convergence (more atmospheric-expressive, more imagery, more experimental layouts by default). None of the nine changes above set a directional default — CD-1/CD-2/CD-3 are process requirements with no preferred outcome, IMG-1 explicitly preserves "no imagery" as valid, and VAR-1 only fills an unspecified band, it doesn't raise variance's floor.

---

## 8. Success criteria

A Phase 6 re-test succeeds on **process**, not on a preferred output:

1. **Genre inference is evidence-traceable** — whatever Genre `.design/context.md` records, its selection (and the rejection of at least one real alternative) cites actual text from `style-catalog.md`, not an assumed stereotype. The Genre itself is not judged — the reasoning is.
2. **Rejected Directions contains a genuine alternative** — meaningfully distinct from the chosen direction on ≥2 of {composition, imagery, typography, color, materiality, interaction}, named explicitly, not only brief-mandated anti-pattern avoidances.
3. **SLOP-011 gestalt check runs** — the finished direction's color/type/accent combination is explicitly compared against SLOP-011's named clusters, with the result (match/no-match, and any declared exception) recorded.
4. **Mechanically-countable rules report their status honestly** — each gate either ran and passed/failed, or is explicitly reported as skipped with the reason (capability unavailable), never silently assumed passed.
5. **Mobile hero headline has no orphan/widow defect** where rendering capability was available to check it; if unavailable, this is explicitly reported as unchecked, not claimed as passing.
6. **Imagery decision is recorded** — `.design/context.md` shows an explicit answer to IMG-1's questions, even if the answer is "no imagery, because X."
7. **Level 2 critique status is honestly reported** — either it ran (with the trigger condition that fired named) or it's explicitly reported as not run / not available, never silently omitted or implied.
8. **No new directional default was introduced** — a fresh reviewer comparing this re-test's process against the original benchmark's process should see more genuine comparison and evidence-use, not simply a different aesthetic default substituted for the old one.

---

## 9. Benchmark re-test procedure

1. Re-create a fresh working directory — do not edit `design-excellence-benchmark/` in place. Symlink the corrected skill package the same way the original benchmark did.
2. Re-run `brief.md` verbatim, unchanged, so the comparison isolates the skill's behavior, not a changed brief.
3. Capture: `.design/context.md` in full (register/genre/dials, Rejected Directions with named distinguishing dimensions, imagery decision record, any Level 2 critique record or explicit unavailability note), plus rendered screenshots at 1440px and 390px for the home page at minimum.
4. Score against §8's 8 criteria. Criteria 1–4 and 6–7 are process/record checks — verifiable directly from `.design/context.md`. Criterion 5 depends on rendering capability being available; report honestly if it wasn't. Criterion 8 requires a qualitative comparison.
5. For criterion 8, dispatch a fresh-context reviewer (genuinely new agent, not a fork — matching `critique-protocol.md`'s own isolation mechanism) with only the brief and the rendered screenshots, blind to Phase 6's specific changes, and ask: does the visible design process show real comparison and evidence-use, or does it read like a single default was picked and rationalized after the fact (regardless of which aesthetic that default happens to be)?
6. Report per-criterion, not as a single pass/fail. A result that lands on the same Genre as the original benchmark, but with a real second candidate genuinely compared and a rejection reason that correctly cites the style catalog, is a full pass — the objective is stronger evidence-based decision-making, not a different decision.

Plan is ready for review. Stopping here — no implementation performed.
