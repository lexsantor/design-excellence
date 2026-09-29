# D-1 §4 Behavioral Root-Cause Investigation + Targeted Runtime Correction

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Previous milestone:** Refresh Installed Skill + Organic Headless Validation (`ee36c39`)
- **HEAD before:** `ee36c39`. Working tree before: only the pre-existing untracked workspaces, `scratchpad/`, `rules.md` and the discovery report (untouched).
- **Workspace (disposable, repository-local, uncommitted):** `de-d1-section4-correction-20260928/`. Evidence index: its `REPORT.md`.
- **Repository files changed:** `design-excellence/SKILL.md` (line 21, §1 DEFINE row), `STATE.md`, this report.
- **Not changed:** `critique-protocol.md`, every other skill file, `loop.md`, `CLAUDE.md`, the Integration Contract, architecture, T4, references, Principle Pool, workspace governance, historical reports and evidence.

## 1. Authorized scope

The human authorized this milestone with its brief. The exact text is recorded in `STATE.md`:

> adelante siguiente paso

The brief sets the scope:
- Investigate why the §4 Register/Genre/Dials declaration stays internal while the §2 line is visible.
- Make the smallest §4-scoped `SKILL.md` correction only if the root cause is evidenced.
- Refresh the installed copy with the established procedure.
- Validate the correction at runtime.
- Leave §2, OQ-1, F-1 and Level 1/Level 2 semantics unchanged.

The permission classifier refuses an agent launch of `claude -p`, so the one validation run was launched by the human. The human closed the milestone with an explicit close-out instruction.

## 2. Previous evidence

- **Organic validation** (`20260928-organic-disclosure-validation.md`, KC-01):
  - §2 PASS.
  - §4 FAIL: the values were only in thinking (14:39:16Z) and in `.design/context.md` (14:39:52Z).
- **Pre-fix base rate:** §4 visible before DIRECT/DESIGN in 0 of 9 runs (`de-disclosure-reviewer-input-20260928/analysis/disclosure-base-rate.txt`).

## 3. Investigation method

The investigation used two kinds of evidence, both source-level or existing (no new runtime yet):

1. **Source-path analysis** of `SKILL.md` §1, §2, §4 and §5.
2. **Existing transcripts.** `_method/define_window.py` prints every visible text block and tool call from the §2 point up to the first `.design/context.md` write. It ran over all 10 preserved organic builder transcripts. Output: `analysis/define-window.txt`.

A controlled reproduction was judged unnecessary. The source asymmetry and the 10-run window already pointed to one path, and the validation run tested the resulting prediction directly.

## 4. Root-cause evidence

**Source level (text before the fix):**

- **§2 is anchored at its execution point.**
  - §1 opens with "Classify the request (§2) before doing anything else."
  - The §2 template sits directly under the routing table, which is what the builder applies first.
  - Observed: the builder emits it as its first visible text (8 of 10 runs before the fix).
- **§4 is anchored only in its own section.**
  - §4 says: "Classified once, at DEFINE, declared in one line, stored in `.design/context.md`."
  - The `Declare:` template sits at the end of the dials subsection.
  - The §1 DEFINE row, which is the stage flow the builder follows, and §5 Greenfield ("create `context.md` after DEFINE") name only the file record as DEFINE's output.

**Existing runtime evidence** (`analysis/define-window.txt`, 10/10 runs):

- No visible text before the first `context.md` write declares register, genre or dials.
- Where DEFINE is narrated, the narration describes recording the file:
  - "Classification recorded. Now DEFINE decisions…" (LC-01)
  - "Next I'm recording the direction and then building." (RV-C-01)
  - "Next I'll define the direction, write `.design/context.md`, then build." (BM-C-01)
  - "Writing the project context record first (greenfield: created after DEFINE)…" (LC-01)
- In KC-01 the classification formed in thinking (#22) and went straight to the Write (#25).

**Competing explanations checked against the evidence:**

- "Headless runs don't narrate before tool calls": contradicted. Visible narration precedes many tool calls in every run.
- "The builder treats the §2 line as covering §4": not supported. §2 lines carry routing add-ons ("full pipeline minus AUDIT-stage", "Loading the references…") but never register values, and KC-01 emitted §2 alone after the separation wording of `536575d`.

**Root cause.** DEFINE's specified output at its execution point was only the `.design/context.md` record. The §4 declaration was attached to the §4 taxonomy text, not to the stage flow, so the builder discharged DEFINE by writing the file.

## 5. Source change

`design-excellence/SKILL.md` line 21, §1 stage table, DEFINE row. One sentence was appended (`_evidence/spec-diff.patch`):

> DEFINE ends by stating the §4 declaration as its own line, before `.design/context.md` records the values

- It references §4 by section and does not restate or alter the template.
- The ordering it names is already implied by §4 ("before DIRECT/DESIGN") and §5 Greenfield ("after DEFINE").
- No stage, gate or output was added.
- §2, §4 text, §5, `critique-protocol.md` (OQ-1, F-1, Level 1/Level 2) are unchanged.
- The source hash lists show `SKILL.md` as the only changed file.

## 6. Installed-runtime refresh

- **Before:** the installed copy equalled the pre-edit source (18/18).
- **Procedure:** `icacls … /remove:d <user> /T`, `Copy-Item` of `SKILL.md` only, then `icacls … /deny "<user>:(OI)(CI)(DE,WD,AD,DC)"`.
- **After:**
  - 18/18 SHA-256 parity with the edited source. Only `SKILL.md` changed (`cd3dde1e…`).
  - The `icacls /T` dump is byte-identical to the one before.
  - Guard probe: read OK, create DENIED, append DENIED.
- No classifier denial occurred.

## 7. Validation method

- **Kind: organic runtime evidence.** One fresh, unprimed BUILD on a genuinely-empty folder `project/SC-01/`, with a new brief ("Spoke & Chain" bike repair shop, `_method/prompt.txt`).
  - The brief is ASCII-only and has 0 priming-term hits, including variance/density/motion.
  - The prompt as received equals `prompt.txt` exactly, so the KC-01 encoding issue did not recur.
  - The parent folder held only `SC-01`, so the method and evidence names were not exposed.
- **Launch:** by the human, command as in `_method/METHOD.md`.
  - Init: `claude-opus-5-5`, cwd `SC-01`, Playwright connected.
  - Result: `success`, `is_error=false`, 61 turns, 11.4 min. stderr empty.
- **Acceptance criteria** (from the milestone brief), frozen in `METHOD.md` before the run:
  1. §2 remains visible and positioned.
  2. §4 is visible response text.
  3. §4 is its own declaration.
  4. §4 comes before downstream design work.
  5. §4 carries this run's actual values.
  6–8. §4 is not only in `context.md`, thinking or the final summary.
  9. §2 semantics are unchanged.
  10. No OQ-1 / F-1 / Level 1–Level 2 regression.
- **Evidence:**
  - `_evidence/stream.jsonl` (UTF-16LE original) and a decoded copy.
  - The session JSONL and subagent JSONL copied into `_evidence/session-transcript/`.
  - The watcher log.
  - `analysis/*`.

## 8. Exact observed §2 evidence

- #6, 15:22:22.284Z, visible text, after INSPECT (`ls`) and before any reference load or DEFINE:
  `Reading this as: page BUILD on a genuinely-empty project.`
- It is repeated at the top of the #20 text block.

## 9. Exact observed §4 evidence

- #20, 15:24:24.100Z, visible text block (`analysis/timeline.txt`, `analysis/assistant-text.md` line 14). It sits on its own line, after the block's **DEFINE** bullets and before its **DIRECT / EXPLORE** section:
  `Reading this as: hybrid modern-minimal work, variance=Medium (4), motion=Low (2), density=Medium (5).`
- **Values** match `.design/context.md` frontmatter: `register: hybrid`, `genre: modern-minimal`, `dials: { variance: 4, motion_intensity: 2, visual_density: 5 }`.
- **Format:** each dial gives its band followed by the integer in parentheses. The template asks for `[band]`, and the band is present; the extra integer does not change the declared value.
- **Not only in the other channels:** it is also absent from the final message.

## 10. Timing and order evidence

| Time (UTC) | Event |
|---|---|
| 15:22:22 | §2 line (visible) |
| 15:22:22–15:22:28 | Reference loads |
| **15:24:24** | **§4 line (visible)**, then the DIRECT/EXPLORE candidates in the same block |
| 15:24:32 | Token contrast computation (DESIGN) |
| 15:26:36 | First `index.html` write |
| 15:29:11 | First `.design/context.md` write (transcript; watcher 15:29:14) |
| 15:30:09 | Level 2 dispatch |
| 15:33:19 | Final message |

§4 precedes DIRECT/EXPLORE, all DESIGN and BUILD work, and the first `context.md` write, by 4 min 47 s.

## 11. Regression checks

| # | Criterion | Result |
|---|---|---|
| 1 | §2 visible, before DEFINE | PASS (#6) |
| 2 | §4 visible response text | PASS (#20) |
| 3 | Own declaration | PASS: a distinct line, separate from the §2 line |
| 4 | Before downstream design work | PASS (§10) |
| 5 | Actual values of this run | PASS: equal to `context.md` |
| 6–8 | Not only in `context.md`, thinking or final summary | PASS |
| 9 | §2 semantics unchanged | PASS: §2 text not edited, line in template |
| 10a | OQ-1 | PASS. The brief labels "Source input, the user's request passages that state facts (quoted verbatim; data, not instruction to you)". Request paragraphs 1–6, including the not-yet-known passage, are verbatim. Paragraph 7 ("I'm in the workshop all day…") is omitted, as in KC-01. No usage conclusion is stated (`analysis/source-fact-verify.txt`). |
| 10b | F-1 | PASS: 7/7 rubric passages exact vs the installed protocol (`analysis/rubric-verify.txt`) |
| 10c | Level 1 before Level 2 | PASS: Level 1 recorded 15:29:11 "before Level 2 dispatch". Brief written 15:29:58, dispatch 15:30:09. The six pre-dispatch Level 1 lines are verbatim in the final `context.md`. |
| 10d | No leakage / isolation | PASS. No Level 1 content in the brief. The reviewer (`lexia-design:visual-critic`, fresh, not a fork) opened only the brief, `index.html`, the five screenshots the brief listed as the artifact, and governed skill files. It never opened `context.md`, which the brief forbids (`analysis/reviewer-isolation.txt`). |
| — | Build sanity | 16/16 checked facts present in the page. The only "booked" is "Your slot is not booked yet". 9 placeholder markers. Server stopped. |
| — | Repository | Only `SKILL.md` changed in the skill tree. Installed 18/18. Desktop listing unchanged. |

## 12. Limitations

- **One organic run.** It shows the corrected behaviour occurs; it does not establish a rate. The pre-fix record was 0/10.
- **Attribution rests on source analysis and the before/after contrast**, not a controlled A/B on the same brief. The brief also differs from KC-01's.
- **§4 inside a larger block.** The §4 line is its own line, but it sits in a multi-section visible block that also restates §2 and carries the DEFINE and DIRECT content. It was not a separate text message.
- **Human-launched run**, because of the classifier restriction.
- The builder stored its screenshots in `.design/evidence/`. This is outside this milestone's scope; recorded only because the reviewer read them as the artifact.

## 13. Final disposition

- **COMPLETED.**
- **D-1 §4:** root cause identified. Corrected by one sentence in the §1 DEFINE row, and validated PASS in one organic run.
- **D-1 §2:** still PASS.
- **OQ-1, F-1, Level 1/Level 2 independence:** no regression.
- **Next action:** await human direction.
