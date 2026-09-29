# Close F-1 Record + Repository Workspace Organization

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Authorization (human, verbatim):** "Autorizo el milestone Close F-1 Record + Repository Workspace Organization."
- **Previous milestone:** Refresh Installed Skill Copy + Controlled Organic F-1 Recurrence Check (`6f2c37c`)
- **Repository files changed:** this report, `STATE.md` (milestone record and operational fields), `.gitignore` (narrow additions, §3), and `CLAUDE.md` (pre-existing untracked root instruction file, committed unchanged, §2.4). No skill source, `loop.md`, historical report or evidence changed.

## 1. F-1 closure

**Previous state.** F-1 was recorded in `25b4e3b` (`STATE.md`, "Unresolved findings"). In a controlled build, the builder did not transport the Level 2 axis definitions verbatim, even though the protocol text was unambiguous. `30706f5` made the transport mechanical: extraction at brief-writing time plus a mechanical comparison (`20260928-level2-brief-transport-clarification.md`). Its micro-test did not reproduce F-1's long-session condition, so recurrence in an organic build stayed untested.

**Organic recurrence evidence.** `benchmarks/external-test/20260928-organic-f1-recurrence-check.md` (`6f2c37c`):

- F-1 PASS; process VERIFIED; C1 PASS; C3 PASS; C4 PASS with a reconstruction limitation; O-1 PASS; no human escalation.
- One organic three-page build dispatched the brief 48 tool calls and 8 min 41 s after the only session read of the protocol. That matches the F-1 timing condition, which arose without being forced.
- The builder extracted the rubric from the file by command, inserted it by file concatenation and diffed it before dispatch ("RUBRIC IDENTICAL"). The received block is byte-exact against an independent extraction, with no Level 1 leakage.
- Installed/source parity 18/18; write guard restored; no source skill change.

**Closure status.** F-1 is closed under the current mechanical Level 2 brief-transport specification after one organic recurrence check. The rubric was transported exactly, and the extraction/comparison process was directly verified. This does not establish universal non-recurrence. Reopen only if a later organic run produces a deviation; until then, no further Level 2 transport work is warranted.

**Limitations carried forward unchanged** (from the organic report §8): n=1; the sent brief was reconstructed deterministically, not captured; extraction preceded the brief write by 40 s and five tool calls; the builder's diff compares against its own extraction; reviewer isolation from `context.md` rests on instruction (O-3); the run does not isolate the specification change as the only cause.

**Where recorded.** There is no separate F-1 record file. F-1's history is the `25b4e3b` `STATE.md`, the clarification report and the organic report. None of these was edited. The closure is recorded here, and `STATE.md` points to this report.

## 2. Repository organization

### 2.1 Root structure

Before and after are identical: no file or directory was moved, created or deleted at the root. The only root-level change is to the contents of `.gitignore` and `STATE.md`.

| Item | Class | Git | Decision |
|---|---|---|---|
| `design-excellence/` | A governed source | tracked | untouched |
| `loop.md`, `STATE.md` | B governance/state | tracked | `loop.md` untouched; `STATE.md` operational/milestone record |
| `CLAUDE.md` | B repository instructions | untracked → committed | committed unchanged (§2.4) |
| `benchmarks/`, `architecture/`, `proposals/` | C formal reports / design history | tracked | untouched; this report added under `benchmarks/external-test/` |
| `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md` | C, deliberately untracked | untracked | untouched: `OVERLAY-FOCUS-EVIDENCE-INVESTIGATION-RESULTS.md` records that it stays untracked "as the human instructed" |
| `de-l1l2-behavioral-check-20260928/` | D disposable workspace | untracked | kept in place (F-1 origin evidence) |
| `de-l2-transport-microtest-20260928/` | D | untracked | kept in place (clarification micro-test) |
| `de-l1l2-organic-f1-check-20260928/` | D | untracked | kept in place (F-1 closure evidence; index in its `REPORT.md` verified present) |
| `design-excellence-benchmark/` | D | untracked | kept in place (carry-through benchmark) |
| `design-excellence-revalidation-20260928/` | D | untracked | kept in place (revalidation benchmark) |
| `scratchpad/` | E historical/experimental | untracked | untouched |
| `.claude/` | F configuration | ignored (`settings.local.json`, skill junction) | untouched |
| `.gitignore` | F | tracked | narrow additions (§3) |
| `ruvector.db` | G local tool database | ignored (`*.db`) | untouched: not tracked, not referenced by governed files (only by historical phase-7 and scratchpad reports) |
| `rules.md` | H generated/unknown | untracked | untouched: generic browser-tool rules, unrelated to Design Excellence; earlier observed to appear from a session hook. Its purpose is not established by repository evidence |

Workspaces are not tracked, and this milestone does not start tracking them. `loop.md` §14 forbids committing disposable captures and work copies. No workspace is redundant: each holds the evidence a committed report cites. None was deleted, and none was ignored wholesale.

### 2.2 Workspace path map

Committed reports and workspace `REPORT.md` files cite the workspaces at their earlier Desktop-level paths. The files are unchanged: reports are cited, never rewritten (`loop.md` §0), and the workspace files are evidence. The canonical locations are:

| Cited path | Canonical path |
|---|---|
| `C:\Users\<user>\Desktop\de-l1l2-behavioral-check-20260928` | `<repo>\de-l1l2-behavioral-check-20260928` |
| `C:\Users\<user>\Desktop\de-l2-transport-microtest-20260928` | `<repo>\de-l2-transport-microtest-20260928` |
| `C:\Users\<user>\Desktop\de-l1l2-organic-f1-check-20260928` | `<repo>\de-l1l2-organic-f1-check-20260928` |
| `C:\Users\<user>\Desktop\design-excellence-benchmark` (and date-suffixed variants) | `<repo>\design-excellence-benchmark` |
| `C:\Users\<user>\Desktop\design-excellence-revalidation-20260928` | `<repo>\design-excellence-revalidation-20260928` |

`<repo>` is `C:\Users\<user>\Desktop\design-excellence`. `STATE.md` no longer names any Desktop-level workspace path.

### 2.3 Ambiguous items outside the repository (recorded, not touched)

The Desktop has no Design Excellence workspace folder left. Two Desktop-level archives remain: `design-excellence-benchmark-20260928.zip` (26,071,874 B, SHA-256 `8f791f93…`) and `design-excellence-revalidation-20260928.zip` (22,140,246 B, 96 entries, `RV-*` projects). Neither is byte-identical to an in-repository file: the in-repository `design-excellence-benchmark.zip` is `5c8831dd…`, 26,065,680 B, and the revalidation workspace has no archive. They are outside the audited repository, the right destination is not unambiguous, and moving or removing them is a human decision. `<external-test-a-project>/` on the Desktop is the external test's subject project, not a Design Excellence workspace, and was not touched.

### 2.4 Governance inconsistency found (recorded, not fixed)

`loop.md` §1 step 4 ("disposable copies live outside both repositories") and §2 ("create disposable work copies outside both repositories") conflict with the root `CLAUDE.md` workspace rule, which puts every workspace inside the repository. `CLAUDE.md` places itself below `loop.md`. Taken literally, the old rule would therefore govern future milestones. Editing `loop.md` requires explicit human authorization (§7), this milestone's brief requires `loop.md` to stay intact, and no step of this milestone creates a workspace. It is not needed to complete the milestone (`loop.md` §2.1 case C), so it is recorded as the follow-up in §7.

`CLAUDE.md` was untracked. It is committed here unchanged, because it is the repository-level workspace rule this milestone is organizing around, and the brief names it the permanent instruction file. It contains only repository and installed-skill paths, with no catalog or library identifiers.

## 3. Git

- **Branch:** `main`. **HEAD before:** `6f2c37c`.
- **Intended changed files:** `STATE.md`, `.gitignore`, `CLAUDE.md` (new to tracking), this report.
- **`.gitignore` assessment.** The existing rules (local settings, `*.db`, OS/editor files, skill junction) were correct but incomplete. Before this change, `node_modules/` and `.next/` were ignored only by nested project `.gitignore` files under `scratchpad/`, so a new disposable project without one would expose them. `.playwright-mcp/` output inside `design-excellence-benchmark/BM-*` was not ignored at all. Added: `node_modules/`, `.next/`, `.playwright-mcp/`, `__pycache__/`, `.env`, `.env.*` with `!.env.example`. Not added: `de-*`, `scratchpad/`, `benchmarks/`, `*.md`, `*.zip`, `*.log`, `dist/`, because they could hide evidence or legitimate files. Check: `git ls-files -ci --exclude-standard` is empty (no tracked file became ignored); `.env.example` stays visible; the untracked top-level set is unchanged.
- **Tracked/untracked.** Tracked: governed source, governance, reports, design history. Intentional untracked: the five workspaces, `scratchpad/`, the discovery report and `rules.md`. Ignored: `.claude/` contents, `*.db`, nested dependency/build output. Nothing accidental was staged.
- **Commit:** this milestone's single local commit, `chore: close F-1 and organize project workspaces`. A commit cannot contain its own hash. Not pushed.

## 4. Safety

- No folder created under `C:\Users\<user>\Desktop\` (Desktop listing before and after: no `de-*` or workspace folder).
- No evidence moved, deleted or rewritten; historical reports and workspace files byte-unchanged.
- Installed skill `C:\Users\<user>\.claude\skills\design-excellence\` untouched and external: 18/18 SHA-256 parity with `design-excellence/`, read-only check.
- No unrelated change staged. `rules.md`, the discovery report and `scratchpad/` stay untracked and untouched.

## 5. Validation

| # | Check | Result |
|---|---|---|
| 1 | No new Desktop-level folder | PASS |
| 2 | All Design Excellence workspaces inside the repository | PASS (five, listed in §2.1) |
| 3 | Root `CLAUDE.md` exists with the workspace rule | PASS |
| 4 | `loop.md` intact | PASS (`git diff HEAD -- loop.md` empty) |
| 5 | `STATE.md` operationally consistent | PASS (COMPLETED; points to this report; closed branches unchanged) |
| 6 | F-1 closure points to the organic report | PASS (§1) |
| 7 | Historical evidence available | PASS (workspace indexes present) |
| 8 | No evidence deleted | PASS |
| 9 | No governed skill source change | PASS (`git diff HEAD -- design-excellence` empty) |
| 10 | Installed skill external | PASS (18/18 parity) |
| 11 | `.gitignore` narrow and justified | PASS (§3) |
| 12 | No unrelated pre-existing work modified | PASS |
| 13 | Staging holds only intended files | PASS (checked before commit) |
| 14 | No push | PASS |

§8 independent review was not required, because this milestone's output is a record closure and a repository organization, not a verdict on architecture, governance, sources, integration or strategy. No subagent was used. Iteration 1 of 5, within the 60-minute budget.

## 6. Issues resolved in scope (`loop.md` §2.1)

| Issue | Case | Resolution |
|---|---|---|
| `STATE.md` pointed to the organic workspace's former Desktop path | A | replaced by the current record, which cites no Desktop workspace path |
| Committed reports cite former Desktop paths | A (record) | path map in §2.2; reports not rewritten |
| Dependency/tool-output ignore gaps | A | narrow `.gitignore` rules (§3) |
| `loop.md` vs `CLAUDE.md` workspace location | C | recorded; follow-up (§7) |

No case B or D arose, so no escalation question was asked.

## 7. Recommended next action

Authorize a targeted `loop.md` amendment aligning §1 step 4 and §2 ("outside both repositories") with the in-repository workspace rule in `CLAUDE.md`. (Recommendation only; not authorized.)
