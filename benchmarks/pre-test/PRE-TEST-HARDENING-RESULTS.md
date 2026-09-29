# Pre-Test Hardening & External Test Preparation — Results

**Status:** COMPLETED. The first external test was **not** run.
**Authorization:** human authorization recorded verbatim in `STATE.md` (2026-09-28): "Autorizo Pre-Test Hardening & External Test Preparation. …". It authorizes resolving PT-01, PT-02, PT-03, PT-04, PT-05, PT-59, PT-06, PT-07, PT-09 and PT-11 from `benchmarks/audit/COMPREHENSIVE-PRE-TEST-SKILL-READINESS-AUDIT-RESULTS.md`, preparing the environment for a Greenfield BUILD test, and a final `loop.md` §8 review.
**Parent commit:** `3a29e5f`.
**Delegation:** no operational subagents were needed. The edits are small, in shared files, and made by the main agent. One `loop.md` §8 reviewer was used.

---

## 1. Changes implemented

**Skill text.** Four files changed; no stage, mode, tier, file or P-layer was added.

| File | Change | Finding |
|---|---|---|
| `design-excellence/SKILL.md` §1 DEFINE row | "Task Mode ∈ {BUILD, REDESIGN} only — never POLISH, CRITIQUE, AUDIT or DISCOVER"; BUILD-existing reuses recorded values; pointer to §5 "First contact" | PT-02 |
| `SKILL.md` §1 capability paragraph | Defines Enhanced (can render and measure in a browser) and Core v1 (cannot). Checks needing rendered geometry, laid-out text, post-render colors or runtime metrics need Enhanced even where the entry does not say so. **Color pairs declared in code are computed statically and still gate in Core v1.** When in doubt, run what is static and report the rest as `skipped — capability unavailable` | PT-06 |
| `SKILL.md` §2 POLISH row | `INSPECT(cache read; on a cache miss, the existing-project-safety.md §1 scan, not persisted)` | PT-02, PT-07 |
| `SKILL.md` §5 Per Project State | New bullet, **First contact**, which is not a separate Project State: an existing project with no `.design/context.md` (full text below the table) | PT-02, PT-07 |
| `SKILL.md` §7 T3 anti-slop row and category paragraph | The SLOP-011 entry loads for Level 1 axis 1; the CRITIQUE stage loads `accessibility.md` for axis 5. The "maybe `accessibility.md`" example is removed | PT-05, PT-59 |
| `SKILL.md` §7 Stack modules | A session never creates a stack file. The skill's own directory is read-only during any task. With stack evidence, work from the project's own configuration and record the stack under the project's Constraints & Preserved Patterns only in a run that writes `context.md`. `references/stacks/*.md` is a maintained change only. The Phase 4 note records the withdrawal | PT-03 |
| `SKILL.md` §7 T4 dependencies | New paragraph (full text below the table) | PT-11 |
| `references/critique-protocol.md` Level 1 | A new `not assessable: <reason>` status: never a pass, never an estimate, not counted for escalation. Level 1 loads what it checks. The Fingerprint History stamp is written only when `context.md` exists or is created by the run, the run writes to the project, and Fingerprint History is not excluded; otherwise it is reported in session output | PT-05, PT-06, PT-07 |
| `critique-protocol.md` axis 5 | "never skipped" clarified: a check that cannot run honestly is recorded `not assessable`, never passed | PT-06 |
| `references/existing-project-safety.md` §1 | The scan still always runs. It is cached to `.design/preflight-cache.json` only in BUILD and REDESIGN; POLISH, CRITIQUE, AUDIT, DISCOVER and bounded profiles that end before BUILD keep it in the session. Pointer to "First contact" | PT-07, PT-02 |
| `existing-project-safety.md` §5 | Where no Constraints list exists yet, the post-build diff uses the §1 preserve/introduce summary | PT-02 |
| `references/rule-catalog/content-copy.md` CONTENT-003 (P1; layer unchanged) | New clause in the principle (full text below the table); the validation also traces claims to the existing project's own content | PT-09 |

**First contact** (the new `SKILL.md` §5 bullet), in full:
- INSPECT still runs the safety scan; a missing context or cache is never a reason to skip it.
- BUILD and REDESIGN run DEFINE and create `context.md`. Under a bounded profile, Choose / prepare creates it with the prepared direction; Directions only creates none.
- POLISH, CRITIQUE, AUDIT and DISCOVER do not enter DEFINE. They derive provisional register, genre, dials and Product Truth from the code and the request, and state them as *"inferred, not recorded"*.
- Those modes create no `.design/` files unless the user asks.

**T4 dependencies** (the new `SKILL.md` §7 paragraph), in full:
- The T4 files decide when a source fits. They do not verify package names, install commands or APIs.
- Before adding any T4 source, whether as a package or by copying its source in through a registry or CLI, state the exact package and its origin, and get the user's explicit confirmation.
- Never install a guessed or unverified package.
- If the user declines or cannot confirm, treat the source as unusable and follow that file's Other/custom implementation item.

**CONTENT-003's new clause:**
- Content already in an existing project (its figures, names, testimonials) counts as supplied. This rule never replaces it with a placeholder or changes its facts.
- Reusing that content does not verify it, and never licenses new or derived claims.
- Edits the user asks for, and copy edits that keep its facts, are outside this rule.

**Environment** (outside the repository; not committed):
- **PT-01:** a real **copy** of `design-excellence/` is installed at user level: `C:\Users\<user>\.claude\skills\design-excellence`. It holds 18 files, identical to the repository by SHA-256. A copy, rather than a link, was chosen so that no test-session write can reach this governed repository.
- **Write guard:** an NTFS **deny** rule on that folder for the current user, inherited by all children, denies WriteData, AppendData, Delete and DeleteSubdirectoriesAndFiles. Read access is unaffected. The first attempt, using `icacls` generic `W`, also blocked reads because W includes SYNCHRONIZE. It was removed and replaced with the exact rights above.
- **PT-04:** the first real test is defined as a **Greenfield BUILD on a new, empty project folder outside this repository**. No existing project is touched.

## 2. Audit findings resolved

| Finding | Resolution |
|---|---|
| PT-01 (P) | Installed at user level and verified loading from an external folder, both through the Skill tool and by explicit `/design-excellence` invocation (§4) |
| PT-02 (A) | First-contact behaviour specified for every mode. The DEFINE row is unambiguous. POLISH's cache-miss path is defined. The safety §5 fallback is added |
| PT-03 (A) | Runtime stack-file creation withdrawn. The skill directory is declared read-only during tasks, and the installed copy is write-guarded |
| PT-04 (P) | The first test is fixed as a Greenfield BUILD on a new project (setup in §6). The execution milestone still needs its own authorization |
| PT-05 (A) | SLOP-011 loads for Level 1 axis 1 |
| PT-59 (B) | `accessibility.md` loads for Level 1 axis 5 |
| PT-06 (B) | Level 1 `not assessable` status; Enhanced/Core v1 defined; general capability-dependence rule, with static color pairs kept as a Core v1 gate |
| PT-07 (B) | No `.design/` writes (cache or Fingerprint stamp) in POLISH first contact, CRITIQUE, AUDIT, DISCOVER or bounded pre-BUILD profiles |
| PT-09 (B) | CONTENT-003 preserves existing project content without verifying it or licensing new claims |
| PT-11 (B) | Confirmation required before any T4 addition, with a defined fallback |
| PT-60 (B), mitigated | Not a text change. The test setup requires explicit `/design-excellence` invocation, and verification listed 11 competing design skills (§4) |

## 3. Audit findings intentionally deferred

Not authorized for this milestone. They remain as recorded in the audit.
- **A:** PT-10, PT-12, PT-13, PT-14, PT-15, PT-16, PT-17.
- **B:** PT-08, PT-18 to PT-30.
- **C:** PT-31 to PT-58. PT-38 (directions-only vs the Greenfield `context.md` write) is only partly settled, for first contact.
- **Not done:**
  - per-rule capability tags: replaced by the general rule in `SKILL.md` §1;
  - an AUDIT/DISCOVER accessibility path (PT-29);
  - a REFINE loop definition (PT-20);
  - a BUILD vs REDESIGN decision rule (PT-18).

## 4. Verification performed

| Check | Result |
|---|---|
| Exact-match edit scripts (every target string matched once) | pass |
| `git diff --check` | clean |
| Stale-phrase search across `design-excellence/` ("stack file is created", "maybe `accessibility.md`", "cache read only", "skip if POLISH") | none remain |
| Scope | only `SKILL.md`, `critique-protocol.md`, `existing-project-safety.md` and `content-copy.md` (plus `STATE.md` and this report) changed. `principle-pool.md`, `loop.md`, the T4 files, P-layers and the §3 P1 list are unchanged |
| Installed copy vs repository | 18 files, identical SHA-256 (after the final edits) |
| Write guard | create file DENIED; edit `SKILL.md` DENIED; create `references/stacks` DENIED; delete file DENIED; read `SKILL.md` OK |
| External load, Skill tool (headless `claude -p` in an empty folder outside the repo, before the guard) | loaded `# Design Excellence` from `C:\Users\<user>\.claude\skills\design-excellence`; folder still empty afterwards |
| External load, explicit `/design-excellence` invocation (after the guard) | same heading and path; folder still empty afterwards |
| Competing skills visible in an external session | design-taste-frontend, frontend-design, high-end-visual-design, impeccable, redesign-existing-projects, taste-examples, frontend-design:frontend-design, ui-ux-pro-max:ui-ux-pro-max, impeccable:impeccable, lexia-design:lexia-design, anthropic-skills:ui-ux-pro-max |
| Independent review (`loop.md` §8) | see below |

**Independent review.**
- **Reviewer.** One fresh, read-only reviewer. It received the diff and the audit, not `STATE.md` or the git log, and it changed nothing.
- **Result.** No BLOCKING findings. Every authorized finding was assessed PASS, with 3 SHOULD-FIX, 5 MINOR and 5 NOTE. It confirmed scope, unchanged P-layers, no remaining stack-creation text, and no damage to the greenfield BUILD path.

| Finding | Class | Reconciliation |
|---|---|---|
| S1: the CONTENT-003 clause was broader than PT-09 needs ("copy … preserve it as it is") and, at P1, could block requested fact updates and copy work; also, reuse must not verify content or license new claims | SHOULD-FIX | **Adopted:** clause narrowed to figures, names and testimonials; no verification; no new or derived claims; user-requested edits and fact-keeping copy edits excluded |
| S2: "contrast of rendered color pairs" plus "when in doubt, rendering-dependent" let Core v1 skip the P1 contrast check | SHOULD-FIX | **Adopted:** declared color pairs computed statically and still gating in Core v1; only post-render colors need Enhanced; "when in doubt" now runs static checks and reports the rest as skipped |
| S3: T4 confirmation had no fallback, and the scope of "adding a dependency" was unclear | SHOULD-FIX | **Adopted:** declined or unavailable confirmation → source unusable → the file's Other/custom item; registry/CLI copy-in counts as adding it |
| M1: axis 5 "never skipped" next to not assessable | MINOR | **Adopted:** clarified in axis 5 |
| M2: the Fingerprint stamp could create `context.md` in a first-contact POLISH | MINOR | **Adopted:** stamp only when `context.md` exists or the run creates it under §5 |
| M3: directions-only on first contact could create `context.md` | MINOR | **Adopted:** Directions only creates none; Choose / prepare creates it with the prepared direction |
| M4: no schema section for the detected stack | MINOR | **Adopted:** recorded under Constraints & Preserved Patterns |
| M5: "First contact" might read as a fifth Project State | MINOR | **Adopted:** "not a separate Project State" |
| NOTES (always-on loading cost, REDESIGN compatibility, general capability clause in place of per-rule tags, scope, HARDEN-002 unaffected) | NOTE | agreed |

No disagreement remains. The reconciliation edits were applied with exact-match scripts, re-checked with `git diff --check` and the stale-phrase search, and the installed copy was re-synced before the guard went on.

## 5. Remaining test risks

1. **Competing skills (PT-60).** Mitigated only by explicit invocation. Record which skill actually ran.
2. **Stale installed copy.** The copy does not follow repository changes, and the guard blocks overwriting it. After any future skill edit, remove the guard, re-copy and re-apply (§6). Check the hash before the test. Git reports that it will rewrite these files with CRLF line endings the next time it checks them out; that changes the hash without changing content, so a mismatch after a checkout also calls for a re-copy.
3. **Capability path (PT-06).** If the test session has no browser, rendering-dependent checks will be `skipped` and Level 1 may carry `not assessable`. That is correct behaviour, but it limits evidence. Decide in advance whether the test provides a browser.
4. **T4 confirmation (PT-11).** A greenfield BUILD needing icons, motion or components will now ask before installing Reicon, Kinetics or SmoothUI. The tester should decide how to answer; declining exercises the Other/custom path.
5. **Deferred risks that a greenfield BUILD can still hit:**
   - PT-20 (no defined REFINE loop or cap);
   - PT-21 (the "production-facing" Level 2 threshold);
   - PT-35 (HARDEN depends on the undefined "ship-readiness"/"prototype");
   - PT-08 (mechanical gates vs user instructions);
   - PT-10 (A11Y-001 P1 target-size leakage);
   - PT-12 to PT-14 (motion and color rule defects).
6. **Stack choice.** Every earlier run was plain HTML. If the test uses a framework (PT-26), stack detection and T4 paths run for the first time.
7. **Guard scope.** The guard protects only the installed copy. The repository's own project-level junction (`.claude/skills/design-excellence` → `design-excellence/`) still exists, but it applies only to sessions opened inside this repository.
8. **Reverting the guard requires a command** (§6). Any tool that needs to update the copy will fail until the guard is removed.

## 6. Exact setup required for the first external test

Performed by the separately authorized test milestone, not here.

1. **Authorize** the test milestone. Name the new project folder, which must be new, empty and outside this repository, for example `C:\Users\<user>\Desktop\<test-project>`, and state that it is a Greenfield BUILD (PT-04).
2. **Confirm the installed copy is current.** In PowerShell:
   ```powershell
   (Get-FileHash "$env:USERPROFILE\.claude\skills\design-excellence\SKILL.md").Hash -eq (Get-FileHash "C:\Users\<user>\Desktop\design-excellence\design-excellence\SKILL.md").Hash
   ```
   It must print `True`, and the repository should be at the commit this milestone produces.
3. **Create the empty folder** and open Claude Code **in that folder** (`cd <folder>; claude`), not in this repository.
4. **Decide capabilities in advance and record them:** whether a browser tool (Playwright or Chrome) is available (Enhanced vs Core v1), and how T4 install confirmations will be answered.
5. **Invoke explicitly.** The first message starts with `/design-excellence ` followed by the greenfield brief, for example a landing page for a named product with its audience and job. Do not rely on automatic skill selection.
6. **Instrument the run and record:**
   - which skill loaded;
   - the classification line;
   - stages run;
   - reference files read;
   - every file written (all must be inside the test folder);
   - `skipped — capability unavailable` and `not assessable` entries;
   - T4 confirmation prompts;
   - Level 1 scores.
7. **After the run:**
   - re-check the hash from step 2;
   - run `git status` in this repository (must be unchanged apart from untracked residue);
   - confirm nothing was written outside the test folder.
8. **To update or remove the guard later** (Bash, with path conversion off):
   ```bash
   MSYS_NO_PATHCONV=1 icacls 'C:\Users\<user>\.claude\skills\design-excellence' /remove:d <user> /T
   ```
   To re-apply it, add a deny rule for WriteData, AppendData, Delete and DeleteSubdirectoriesAndFiles with container and object inheritance, as done in this milestone. Do not use the generic `W` right, which also blocks reads.

## 7. Files created or modified

**In the repository (committed):**
- CREATED: `benchmarks/pre-test/PRE-TEST-HARDENING-RESULTS.md` (this report)
- MODIFIED: `STATE.md`
- MODIFIED: `design-excellence/SKILL.md`
- MODIFIED: `design-excellence/references/critique-protocol.md`
- MODIFIED: `design-excellence/references/existing-project-safety.md`
- MODIFIED: `design-excellence/references/rule-catalog/content-copy.md`

**Outside the repository (not committed):**
- CREATED: `C:\Users\<user>\.claude\skills\design-excellence\` (installed copy, 18 files, write-guarded)
- Disposable verification folders `ext-load-check` and `ext-load-check2` in the session scratchpad (empty)

**Commit:** reported in the final response. Nothing was pushed.
