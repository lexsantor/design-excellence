# Align Workspace Governance

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Authorization (human, verbatim):** "Autorizo el milestone Align Workspace Governance."
- **Previous milestone:** Close F-1 Record + Repository Workspace Organization (`d076aa3`), which recorded this inconsistency as its follow-up (§2.4 there)
- **Repository files changed:** `loop.md` (§0, §1 step 4, §2), `STATE.md` (milestone record and operational fields), this report

## 1. Executive result

| Item | Result |
|---|---|
| Contradiction | `loop.md` placed disposable copies "outside both repositories"; `CLAUDE.md` places every Design Excellence workspace inside this repository and ranks itself below `loop.md`, so the old rule governed |
| Sections affected | `loop.md` §1 step 4 and §2 (both amended); new "Workspace location" bullet in §0, which both now reference |
| Final policy | workspaces, disposable test projects, benchmark/evidence workspaces and temporary artifacts inside this repository, separate from governed files and uncommitted; installed user-level skill copy external; any other external location only when an operation inherently requires it or an authorization or governance rule does |
| Validation | 16/16 PASS (§6) |

## 2. Before

- §1 step 4: "Prefer read-only work; disposable copies live outside both repositories and outside governed state."
- §2: the agent may "create disposable work copies outside both repositories".

"Both repositories" meant this control-plane repository and the external reference catalog. `CLAUDE.md` ("Workspace Organization") requires all future workspaces, benchmarks, evidence, reports, temporary artifacts and disposable test projects to live inside this repository. Its "Instruction Hierarchy" puts `loop.md` first and itself last, so the `loop.md` wording was the effective rule and required the opposite of the intended organization. Every earlier Desktop-level workspace (for example the ones cited by `20260928-organic-f1-recurrence-check.md`) was created under that old rule.

## 3. After

New `loop.md` §0 bullet, **Workspace location**:

- **Project and disposable test workspaces, benchmark and evidence workspaces, temporary artifacts:** inside this repository, in subdirectories kept separate from governed files (the skill directory, `loop.md`, `STATE.md`, committed reports). Never as new folders beside this repository, and never inside the external reference catalog or a reference library.
- **Reuse:** an existing repository-local workspace may be reused when reuse cannot contaminate earlier evidence. This matches `CLAUDE.md` "Workspace Safety".
- **Commit status:** workspaces stay uncommitted. This points to the existing §14 rule and adds nothing new.
- **Installed skill:** the installed user-level copy is a runtime copy, not a workspace, and stays outside this repository. The path itself is named in `CLAUDE.md`; `loop.md` names no filesystem paths beyond its own repository (§0 identity hygiene).
- **Genuinely external resources:** allowed only when an operation inherently requires them (for example a tool's own temporary or session directory) or an authorization or governance rule requires them.

§1 step 4 now reads "disposable copies live in a repository-local workspace (§0), outside governed state". §2 now reads "create disposable work copies in a repository-local workspace (§0)". The rest of the §2 sentence was reflowed with no word changed (verified by word diff).

## 4. Occurrence classification

| Location | Text | Class | Action |
|---|---|---|---|
| `loop.md` §1 step 4 | "disposable copies live outside both repositories" | A | amended |
| `loop.md` §2 | "create disposable work copies outside both repositories" | A | amended |
| `loop.md` §2.1 | "cleaning up temporary artifacts … inside its disposable workspace" | D | unchanged (location-neutral) |
| `loop.md` §14 | "Never commit disposable captures, work copies, …" | D | unchanged; still keeps repository-local workspaces out of commits |
| `loop.md` §0, §3, §4, §18 | external reference catalog / external repository | B | unchanged |
| `loop.md` §0 identity hygiene; §5 "copies differ" | unrelated uses | D | unchanged |
| `CLAUDE.md` lines 13, 56 | scope of the project; installed copy "intentionally outside the repository" | B/D | unchanged |
| `design-excellence/SKILL.md` §7, `references/principle-pool.md` | "nothing outside this repository is read at runtime"; "curated outside this repository" | D | unchanged |
| `STATE.md` previous Next action | recommendation naming the old rule | operational | replaced by this milestone's record |
| 15 committed benchmark reports citing external workspaces | historical record | C | unchanged |

## 5. Files

**Changed:** `loop.md`, `STATE.md`, this report.

**Deliberately unchanged:**
- `CLAUDE.md`: it already states the intended policy and already lists the target hierarchy (`loop.md`, `STATE.md`, `SKILL.md`, repository documentation, `CLAUDE.md`). Its "MUST live inside" wording is stricter than `loop.md`'s narrow external exception. Its own hierarchy resolves that in `loop.md`'s favour, so no edit was needed and no `loop.md` text was duplicated into it.
- `STATE.md`: only the milestone record and operational fields changed. "Authorization scope" and "Closed branches" are unchanged.
- The rest: `design-excellence/` (including `SKILL.md`), `architecture/`, `proposals/`, every historical report, `.gitignore`, workspaces, `scratchpad/`, Desktop archives. The Integration Contract is held outside this repository and was not touched.

## 6. Validation

| # | Check | Result |
|---|---|---|
| 1 | `loop.md` defines repository-local workspaces | PASS (§0 "Workspace location") |
| 2 | Old "outside both repositories" workspace rule removed | PASS (§1 step 4, §2) |
| 3 | No unintended occurrence changed | PASS (word diff: only the three intended changes; reflow word-identical) |
| 4 | Installed skill explicitly external | PASS (`loop.md` §0; `CLAUDE.md` names the path) |
| 5 | `CLAUDE.md` and `loop.md` agree on workspace location | PASS |
| 6 | `STATE.md` consistent | PASS |
| 7 | Historical reports unchanged | PASS (`git diff HEAD -- benchmarks` empty apart from this new file) |
| 8 | `SKILL.md` unchanged | PASS (`git diff HEAD -- design-excellence` empty) |
| 9 | Architecture and Integration Contract unchanged | PASS |
| 10–11 | No new workspace; no Desktop-level folder | PASS (Desktop listing unchanged) |
| 12 | No benchmark or behavioural test run | PASS |
| 13 | No evidence deleted or moved | PASS |
| 14 | No unrelated pre-existing work modified | PASS (untracked set unchanged) |
| 15 | Diff holds only intended changes | PASS (checked on the staged diff) |
| 16 | No push | PASS |

**Targeted search after editing.** `outside both|outside (the|this) repositor` over `loop.md`, `STATE.md`, `CLAUDE.md`, `design-excellence/SKILL.md`, `architecture/` and `proposals/` returns only four lines: the new narrowed exception in `loop.md` §0, `CLAUDE.md` lines 13 and 56 (project scope and installed copy), and `SKILL.md` §7's runtime-read clause. No current normative instruction requires Design Excellence workspaces to be outside this repository. `git diff --check` is clean.

## 7. Governance preservation

The only semantic change is where workspaces live. No authorization boundary, human gate, milestone rule, `STATE.md` authority, Integration Contract clause, closed branch, acquisition rule, Principle Pool rule, runtime-catalog rule, architecture statement, agent limit, budget, validation, commit/push rule, §2.1 policy or escalation boundary was changed. No stage, mode, trigger, score or P-layer was added. The change was made to `loop.md` under this milestone's explicit authorization (§7), recorded in `STATE.md`. §8 independent review was not triggered, because the output is a wording alignment that the human specified, not a verdict on governance or strategy. No subagent was used. Iteration 1 of 5, within budget.

## 8. Limitations

- "Inherently requires" for an external location is a judgement, bounded by the examples and by `CLAUDE.md`. It is not a closed list.
- Tools launched in a milestone (for example headless sessions) may still write to their own temporary directories, as earlier runs did. The new rule permits this as an operational necessity. It does not prevent it.
- Committed historical reports still cite the old Desktop paths. The path map in `20260928-close-f1-workspace-organization.md` §2.2 remains the reference.

## 9. Recommended next action

Await human direction for the next substantive milestone. No further workspace-governance change is needed. (Recommendation only; not authorized.)
