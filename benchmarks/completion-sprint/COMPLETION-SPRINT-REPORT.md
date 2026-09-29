# Completion Sprint Report (closed 2026-09-29)

- **Started:** 2026-09-28, under the human Completion Sprint mandate (`loop.md`, "Completion Sprint Mode").
- **Live state:** `STATE.md` (completion-gate table).
- **Workspace:** `de-completion-sprint/` (uncommitted). `reference-triage/` is git-ignored because it carries source identity.

## 1. D-1: §4 declaration not visible

**Method.**
- `run.py` launches a headless builder with the SC-01 launch configuration and brief.
- Each run stops at the first source-file write, because the disclosure outcome is decided before that point.
- `analyze.py` verdicts:
  - S2: the §2 line is visible before the first file write.
  - S4: the §4 line is visible before the first `.design/context.md` write and the first source write.
  - Thinking, tool inputs, files and the final message never count as visible.
- The analyzer reproduces SC-01's PASS on its original stream.

**Results.**

| Arm | Skill | N | S2 | S4 |
|---|---|---|---|---|
| a1–a4 | HEAD | 4 | 4/4 | 0/4 |
| b1–b4 | F1: DEFINE row anchored after INSPECT, before reference loads | 4 | 1/4 by regex (not verified; transcript read blocked) | 0/4 |

**Mechanism** (a1–a4, the same as in the earlier External Test B run):
1. The §2 line is emitted first.
2. About 13 references are loaded in one tool loop.
3. Register, genre and dials are decided in thinking.
4. The builder writes files with no visible declaration.

This reproduces under the conditions of the only earlier pass (SC-01). Session type, repository root and operator framing are therefore not the cause. Across all recorded headless runs, §4 was visible in 1 of 20.

**F1** had no effect and was reverted. The source and the installed copy were restored to HEAD bytes. The revert exposed that `git checkout` under `core.autocrlf=true` rewrites line endings, so the restore used `git show HEAD:<path>`.

**F2/F3 experiment.** Human-launched with the pre-registered rule: adopt only at S2 = 4/4 and S4 = 4/4.

| Arm | Variant | N | S2 | S4 |
|---|---|---|---|---|
| F2 | §4 line opens the turn of the first file write | 4 | 4/4 | 0/4 |
| F3 | §4 line directly under the §2 line | 4 | 4/4 | 1/4 |

- Neither is adoptable, and no further wording variant was made.
- A full read of every visible text block confirmed the S4 FAILs are real, not analyzer misses. The only visible §4 line in the sprint is f3-2's.
- The independent reviewer's read of b1–b4 shows the F1 §2 regression (1/4) is real. That read covered transcripts the classifier had earlier blocked me from reading directly; this is disclosed here.

**Decision: the contract changes, as the pre-registration allowed when no arm was adoptable.**

Evidence:
- The visible §4 line is not deliverable as a runtime guarantee. It appeared in about 2 of 36 recorded runs, across four instruction placements (`cd047ba`, F1, F2, F3).
- The classification itself is always made, and its durable record exists in 24/24 `.design/context.md` files of completed builds (register, genre and dials frontmatter).

Keeping an unmeetable guarantee would make the skill's contract false. Dropping the classification is not supported by any evidence.

`SKILL.md` changes:
- §1 DEFINE row;
- §1 HYPOTHESIS sentence;
- §4 header;
- §4 declaration paragraph.

The new contract:
- The classification stays mandatory. Its auditable record is the `context.md` frontmatter, written in the same run before SHIP. Existing-project reuse is satisfied by the existing record. A Directions-only run states the values in its delivered output.
- The visible line is still attempted but is best-effort.
- New: the visible line is never reported as stated unless it appeared. The External Test B summary had misreported it.
- The §2 requirement and the P1 override disclosure are unchanged.

**Independent review** (`loop.md` §8): PARTIALLY SUPPORTED. The core decision was supported. Six coherence defects were found and all fixed:
- record timing;
- the stale §4 header;
- HYPOTHESIS ambiguity;
- a Directions-only overclaim;
- existing-project reuse;
- "Unlike §2" implying perfect §2 compliance.

**Limits:**
- §2 compliance is high but not perfect: 12/12 on the current wording, 1/4 under F1, 7/9 pre-fix, and a miss in External Test B.
- The first-contact "inferred, not recorded" statement uses the same visible mechanism and is untested.
- The record's reliability rests on completed builds. `validate.py` checks it on full runs: its D1_CONTRACT criterion requires S2 PASS plus the frontmatter record. This criterion was amended before any `validate.py` run.

## 2. Reference inventories (`themes-links.md`, `figma-links.md`)

**Authorization.** A human reopening of the licensed library for this sprint only, quoted verbatim in `loop.md` §5. Each new entry waits for the human's review before commit.

**Access.**
- **Live demos:** 61 URLs; 60 reachable, 1 returns 404.
  - **Product UI (27):**
    - 19 viewable: 12 directly, 7 through a demo path the login page itself offered.
    - 4 gated; 1 broken; 3 of the viewable are not product UI.
  - **Marketing (34):** 30 fully rendered, 4 partial.
    - The partial cases are headless rendering limits.
    - Scroll-reveal sections were re-captured frame by frame.
- **Design files:** 43 of 43 opened, 51 frames captured.
  - The page lists returned by the design-file tool are incomplete, so pages were opened directly by id.

**Finding.** Most of both inventories are generic:
- dashboards: sidebar, KPI row, charts and table;
- landing pages: hero, logos, features, pricing, FAQ, CTA.

**Curation.**
- Three inspectors produced 7 candidates. I checked the key claims against screenshots myself.
- An independent reviewer checked every observed clause against the cited evidence, looked for identity leaks, and checked overlap with the existing entries:
  - 1 ACCEPT and 3 REVISE, all revisions applied;
  - overstated clauses removed, verbatim labels generalized, provenance citations fixed.

**Result: 4 entries proposed; human review (2026-09-28) kept PRN-0101, PRN-0103 and PRN-0104 (committed and installed) and dropped PRN-0102 (research evidence only, not installed).**

| Id | Principle | Support | Confidence |
|---|---|---|---|
| PRN-0101 | Delegated actions shown against the authority they acted under | 3 sources / 2 clusters | medium |
| PRN-0102 | A figure's reference point is the target the user steers toward | 3 / 2 | low |
| PRN-0103 | Figures carry their denominator (population, window, admission) | 2 / 1 | medium |
| PRN-0104 | Price as an inverse calculation in the buyer's own unit | 3 / 2 | medium |

**Not promoted:**
- scope-rebuilt shell (thin support);
- receiver-view preview (folded into PRN-0101);
- every-state kits (process, already covered by existing rules);
- two single-source ideas.

**Where they fit.** The pool had no product-led entries. PRN-0101 gives product-led and hybrid EXPLORE its first pool option. PRN-0103 and PRN-0104 give brand-led pages generative alternatives to unexplained statistics and to fixed-tier pricing. Each entry carries anti-fabrication exclusions and a literal-copy note.

## 3. Governance and tooling

- **`loop.md`:** one execution model. Completion Sprint Mode states its precedence section by section; safety, provenance, the Integration Contract and anti-gaming are unchanged.
- **`tools/install-skill.ps1`:**
  - mirrors the source, or a variant tree via `-Source`, onto the installed copy;
  - verifies full parity;
  - re-applies the runtime write guard.
- **`tools/check-references.py`:** checks both pools for:
  - schema;
  - ceilings (visual references ≤ 10, pool first pass ≤ 8, ceiling 15);
  - freshness;
  - identity leaks (URLs, marketplace names, hex values, pixel measurements, image files, and product/host names derived from the inventories).

  Current result: PASS.

## 4. Validation status

| Check | Result |
|---|---|
| Installed copy = HEAD, 18/18, write guard | PASS (install script) |
| Variant install and restore path | PASS (dry test, byte-exact both ways) |
| Reference pools static check | PASS |
| Independent evidence review of new entries | Done; revisions applied |
| Human entry review | KEEP 0101, 0103, 0104; DROP 0102 |
| Approved entries installed, parity | PASS (18/18, guard; entries byte-identical to reviewed text) |
| D-1 fix runs (`experiment.py`, human-launched) | F2 S4 0/4, F3 S4 1/4: neither adoptable → contract change |
| Contract change: installed, parity | PASS (installed skill = committed tree + new `SKILL.md`, 18/18, guard; pending pool entries not installed) |
| Final end-to-end builds (`validate.py`: two neutral briefs, D-1 plus pool use plus literal-copy guard) | PASS: human-launched 2026-09-29, 2/2 runs (§5) |

## 5. End-to-end validation (2026-09-29)

Human-launched `validate.py`: one full build per neutral brief, with the installed skill (D-1 contract change and approved entries PRN-0101, PRN-0103, PRN-0104). Result file: `de-completion-sprint/validation-result-20260929T081225.txt`.

| Run | Brief | BUILD_COMPLETED | termination | SHIP | S2 | S4 | D1_CONTRACT | pools read before build | pool ids in context.md | literal_copy_hits |
|---|---|---|---|---|---|---|---|---|---|---|
| `v-ops-20260929T081225` | ops (back-office screen) | true | completed | true | PASS | FAIL | PASS | both | PRN-0101 | [] |
| `v-solar-20260929T081225` | solar (one-page co-op site) | true | completed | true | PASS | FAIL | PASS | both | PRN-0103, PRN-0104 | [] |

- **Completion:** in both runs the last `result` event has terminal_reason `completed` and is_error false, run.py exit code is 0, and the session-limit text does not appear. Ops: 63 turns. Solar: 69 turns.
- **D-1:** S4 is FAIL in both runs; the visible §4 line did not appear, and it is not reported as passed. This is compatible with the current contract (§1): the visible §4 line is best-effort; D1_CONTRACT requires S2 PASS plus the durable `context.md` frontmatter record (register, genre, dials), and both runs meet it.
- **Principle use:** each run logs the entries it used in `.design/context.md` and adapts them to its brief without the entries' literal-copy markers.
  - Ops (PRN-0101): each automated action names the rule it ran under, sits in one explicit state and, when held, shows its evidence and "Not sent"; the rules are editable in one place; the waiting count stays visible.
  - Solar (PRN-0103): the figures are shown with their population and window. PRN-0104: the share cost is a visible per-kW calculation. Neither run invents a figure the brief does not supply: there is no "2 of 412" and no monthly instalment.
- **Post-validation evidence review (qualitative, read-only):** both runs genuinely reached SHIP and were not truncated.

**Non-blocking observations** (recorded, not new requirements):
- **Solar, JS-off claim:** the final report says the form "also works if the phone blocks JavaScript". The JS-off check only confirmed that the content is visible. Without JS, the "not connected" notice (inserted by `script.js`) does not appear, and a submit goes to the placeholder `.invalid` address. The claim is broader than the evidence until the real address is in place.
- **Solar, figures band:** the three figures sit in a large-numeral band that is somewhat generic and interchangeable, and the scope line sits above the figures rather than beside each one. The run's own independent reviewer said the same (genericness 3/5).
- **Parallel runs share local ports:** Solar's first navigation to `127.0.0.1:8765` loaded the Ops page. The builder noticed and switched to its own port, and the deliverable was not contaminated. Parallel runs can still collide this way.
- **Ops visual evidence is limited:** its screenshots were deleted by the run's own cleanup, and one screenshot write outside the site folder was blocked. Its functional and layout claims are backed by recorded browser results, but the visual result cannot be re-inspected.

None of these observations blocks closure of the Completion Sprint. N=1 per brief: this is workflow evidence, not a rate.

`runs/v-ops-20260929T123456` and `runs/v-solar-20260929T123456` are not part of this validation. A harness unit test launched them by accident; they were not analyzed, and they were deleted during final workspace cleanup on 2026-09-29.
