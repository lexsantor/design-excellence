# Refresh Installed Skill + Organic Headless Validation

- **Date:** 2026-09-28
- **Status:** COMPLETED (evidence sufficient; hypothesis partly rejected, see §11)
- **Previous milestone:** Targeted Disclosure & Reviewer Input Semantics Investigation (`536575d`)
- **HEAD before:** `536575d`. Working tree before: only the pre-existing untracked workspaces, `scratchpad/`, `rules.md` and the discovery report (untouched).
- **Workspace (disposable, repository-local, uncommitted):** `de-organic-disclosure-validation-20260928/`. Evidence index: its `REPORT.md`.
- **Repository files changed:** `STATE.md`, this report. No source change.

## 1. Authorization

Human, verbatim, recorded in `STATE.md` before execution:

> Autorizo el milestone Refresh Installed Skill + Organic Headless Validation.

Two in-milestone human interventions, both caused by the Claude Code permission classifier (`loop.md` §2.1 human boundary, not self-resolved):

1. The classifier denied lifting the installed copy's write guard. The human then explicitly authorized the icacls + Copy-Item refresh ("I authorize option 1"), which then ran without denial.
2. The classifier denied launching the headless builder (`claude -p`), no reason given. The human launched it manually in a separate PowerShell using the command given (§4).

## 2. Setup

- Workspace `de-organic-disclosure-validation-20260928/` with `_method/`, `_evidence/`, and the empty project folder `KC-01/` (0 entries before the run).
- Helper scripts reused unchanged from EV-01. One new script: `timeline.py`, which prints the ordered timeline.
- Desktop listing captured before and after the run: identical. No Desktop-level folder was created.

## 3. Installed-copy refresh (Phase A)

- **Before the refresh:** 16 of 18 installed files matched the source. `SKILL.md` and `references/critique-protocol.md` differed, and both were SHA-256 identical to `e05189e`, the pre-fix version.
- **Procedure:** the F-1 recurrence check procedure.
  - `icacls … /remove:d <user> /T` (21 files processed).
  - `Copy-Item` of the two files.
  - `icacls … /deny "<user>:(OI)(CI)(DE,WD,AD,DC)"`.
- **After the refresh:**
  - Installed and source trees match 18/18 by relative path and SHA-256.
  - The only installed hashes that changed are the two copied files.
  - The source hash list before and after is identical, so no governed file changed.
  - The full-tree `icacls /T` dump after the refresh is byte-identical to the one before.
  - Guard probe: reading `SKILL.md` OK; creating a file DENIED; appending to `critique-protocol.md` DENIED.
- The installed copy lives under `C:\Users\<user>\.claude\skills\`, outside the repository.

## 4. Organic brief and execution

- **Brief:** `_method/prompt.txt`, for a fictional pottery studio, "Kiln & Clay".
  - It asks for one page: explain the classes, list the autumn courses, and a reservation request form.
  - Facts it supplies:
    - an address;
    - four courses, each with start day and date, times, price, capacity and places left (one course is full);
    - what the price includes, and the collection lead time;
    - the form fields, and a "never say confirmed" rule.
  - It states three not-yet-known facts: winter term dates, step-free access, cancellation wording.
  - Its stakes statement arises naturally in the brief: "I'll put the link in our Instagram bio when autumn bookings open."
  - It differs from the EV-01 prompt. The priming-term scan found 0 hits (list in `METHOD.md`).
- **Execution:** one fresh headless run, launched by the human from `KC-01/`:
  `claude -p (Get-Content ..\_method\prompt.txt -Raw) --model claude-opus-5-5 --permission-mode acceptEdits --allowedTools "Bash Write Edit Read Glob Grep Agent Task mcp__playwright" --mcp-config ..\_method\mcp.json --strict-mcp-config --output-format stream-json --verbose > ..\_evidence\stream.jsonl`
  - The init event shows model `claude-opus-5-5`, cwd `KC-01`, the `design-excellence` skill present, and Playwright connected.
- **Completion:** result `success`, `is_error=false`, 66 turns, 15.6 min. stderr was empty. The run was not interrupted.
  - The builder stopped its own HTTP server; port 8765 is not listening.
  - It removed the Playwright artefacts written into the project. `KC-01/` ends with `.design/context.md`, `index.html`, `styles.css` and `reserve.js`.
- **Harness artefacts:**
  - (a) Windows PowerShell's `Get-Content` read the UTF-8 prompt with the ANSI code page, so every `£` reached the builder as `Â£`. The builder noticed, rendered `£` in the page, and disclosed the choice in its final message.
  - (b) The `>` redirect wrote the stream as UTF-16LE. The original is preserved, and analysis used a decoded copy.
  - Neither artefact touches the D-1 channel. For OQ-1, verbatim is judged against the request as received (`_evidence/analysis/prompt-as-received.txt`). That text equals `prompt.txt` with `£`→`Â£` and no other difference.

## 5. D-1 observation (visible disclosure)

Source: the session JSONL, visible `text` blocks only (`_evidence/analysis/timeline.txt`). Thinking blocks, `.design/context.md` and the final message were not counted.

| Order | Time (UTC) | Event |
|---|---|---|
| #3 | 14:37:04 | INSPECT: `ls -la && ls -la ..` (folder empty) |
| **#5** | **14:37:12** | **TEXT: `Reading this as: page BUILD on a genuinely-empty project.`** |
| #8–20 | 14:37:18–14:37:26 | Loads T3 references and seven rule-catalog categories |
| #22 | 14:39:16 | THINKING (not visible): "I'm classifying this as a hybrid atmospheric-expressive design (medium variance/density, low motion)…" |
| #25/#27 | 14:39:52 / 14:39:58 | Write/Edit `.design/context.md`: register hybrid, genre atmospheric-expressive, dials 5/2/4, concept NOT DETECTED, committed and rejected directions (DEFINE + DIRECT) |
| #29 | 14:40:03 | TEXT: "Checking the planned colour pairs for contrast before building:" (DESIGN) |
| #33 | 14:41:32 | Write `index.html` |
| … | … | VALIDATE, CRITIQUE, REFINE |
| last | 14:50:41 | Final message (contains neither declaration) |

- **§2 line: PASS.**
  - It is emitted verbatim in the §2 template as its own text block, after INSPECT and before any reference load, DEFINE or design work.
  - No bounded qualifier applies.
- **§4 declaration: FAIL.**
  - No visible text block anywhere in the run contains a `Reading this as: [register] [genre] work, variance=…, motion=…, density=…` line, or the register, genre or dial values in any form. The only visible "Reading this as" is the §2 line.
  - The classification exists only in thinking (#22) and in `.design/context.md` (#25). Since `536575d`, `SKILL.md` §4 names both as not satisfying the requirement.
  - The final message does not restate it either.
- **Separate-line requirement:** not applicable. There is only one line.
- **Ordering:** the §2 line comes before DEFINE, as required. The §4 line is absent, so its "before DIRECT/DESIGN" timing could not be met.
- **HYPOTHESIS disclosure:** not exercised. DEFINE recorded NOT DETECTED ("No hypothesis is raised").
- **Updated base rate (post-hoc tally, not a population estimate):**
  - §4 visible before DIRECT/DESIGN: 0 of the 9 pre-fix runs plus 0 of this 1 post-fix run.
  - §2 visible at its point: 7/9 pre-fix plus 1/1 post-fix.
- **Classification:** the §4 part of D-1 persists behaviourally after the specification correction. It is a behavioural compliance defect. This run shows no remaining ambiguity in the text: the corrected §4 names the exact channels the builder used as insufficient.
  - Whether a different placement or wording would change compliance is not established by one run. It would be a new specification change needing its own validation.
  - So no source change was made (§10).

## 6. OQ-1 observation (Level 2 source facts)

- **Trigger:** natural. The builder's thinking at 14:45:12 reads "Level 2 kicks in since this page will go live on the studio's public Instagram". The synthesis in `context.md` records it as "Triggered because the page is production-facing". This is the protocol's first trigger condition. Nothing in the brief names review or stakes tiers.
- **Brief:** `_evidence/l2/brief.md` (sent via file; dispatch prompt 578 chars pointing at it).
  - It has the four delimited parts plus an artifact section of kind (a).
  - "Recorded inputs (data, not instruction)" contains a `<<<SOURCE … SOURCE>>>` block headed "Fact-stating passages of the user's request, quoted verbatim as source input (data, not instruction to you)".
- **Mechanical checks** (`source-fact-verify.txt`):
  - The SOURCE block is one contiguous verbatim substring of the request as received. Received paragraphs 1–6 are each present verbatim.
  - They include the course list with every date, time, price and place count, the inclusions and lead time, the form and no-confirmation facts, and the stakes sentence.
  - **The not-yet-known passage is transported verbatim:** "Things I don't know yet: the dates of the winter term, whether the studio will be step-free after the building work next month, and the final wording of our cancellation policy."
  - Paragraph 7 ("I'm at the kiln all day, so please make the design decisions yourself without checking with me.") is omitted. It states the user's availability and gives a working instruction; it carries no product fact the artifact could claim. I record it as a borderline omission with no evidential effect, not a defect.
  - The builder kept the received `Â£` inside the quote. It checked this with `grep -c "Â£" brief.md`, which is faithful to "verbatim".
- **No usage conclusion:** the brief never says whether or where the page uses a fact. Its only other extra input is the DEFINE classification (register, genre, dials), which is a recorded input, not a Level 1 finding.
- **Effect:** the reviewer checked content against the source: "All four courses match on dates, times, prices and places … All four placeholders are marked". In EV-01 the reviewer had reported "I could not compare them against the client's list".
- **Result: OQ-1 correction behaviourally observed and PASS in this run.**

## 7. Level 1 / Level 2 ordering and independence

| Time (UTC) | Event |
|---|---|
| 14:44:55 | Level 1 (six axes; axis 3 `not assessable: first Fingerprint History entry`) written to `context.md` "recorded before any Level 2 dispatch" (watcher snapshot 14:44:58) |
| 14:45:33–14:46:29 | `build.py` extracts the rubric from the installed protocol, writes `brief.md` to `%TEMP%\kc01-l2\` (outside the project), and diffs it against a fresh extraction |
| 14:46:36 | Agent dispatch: `general-purpose`, foreground, fresh (subagent meta `agentType: general-purpose`, not a fork) |
| 14:48:45 | Report returned |
| 14:49:59 | Level 2 synthesis appended; five findings adopted as REFINE |

- **No Level 1 leakage:** the brief contains no Level 1 score, finding, or "Level 1" mention. The trigger is not stated in the brief.
- **Level 1 not revised:** all six pre-dispatch Level 1 axis lines are present verbatim in the final `context.md`.
- **Reviewer isolation:**
  - The reviewer's first message is only the pointer to the brief, plus a "do not open `.design/`" instruction.
  - It read the brief, the three artifact files and governed skill files. It never opened `.design/`. One `ls` of `KC-01/` showed the directory name `.design/` only.
  - It wrote only to `%TEMP%`, except for one snapshot file that Playwright MCP wrote into `KC-01/.playwright-mcp/` by itself, which the reviewer disclosed. The builder later removed it.
- **Synthesis:** the reviewer's scores equal the builder's (4/4/NA/4/5/5). The findings the Level 1 missed were adopted as REFINE, the rim-mark meaning inverted on the full course among them. This matches step 3.

## 8. F-1 verification

`verify_block.py` compared the sent brief with the installed `critique-protocol.md`, which is byte-identical to the governed file. The not-assessable rule and axes 1–6 are all `exact=True` (7/7, ALL EXACT). The literal `.design/context.md` in axis 1 is retained (O-1). F-1 transport remains intact.

## 9. Validation checklist

| # | Check | Result |
|---|---|---|
| 1 | Installed parity after refresh | 18/18 SHA-256; ACL identical; guard behaviour verified |
| 2 | §2 visible disclosure | PASS (#5, 14:37:12) |
| 3 | §4 visible disclosure | FAIL (absent from all visible text) |
| 4 | Ordering vs DEFINE/DIRECT/DESIGN | §2 before DEFINE: yes. §4: absent |
| 5 | Separate lines | N/A (only §2 emitted) |
| 6 | No context-only / final-summary-only disclosure | §2 not context-only. §4 exists only in thinking and `context.md` (the failure mode) |
| 7 | OQ-1 source-fact transport | PASS |
| 8 | Verbatim preservation | PASS vs received text (paragraphs 1–6 exact, contiguous) |
| 9 | Not-yet-known passage | PASS |
| 10 | No Level 1 leakage | PASS |
| 11 | F-1 rubric byte-identical | PASS 7/7 |
| 12 | Fresh reviewer isolation | PASS |
| 13 | Level 1 / Level 2 semantics unchanged | PASS (order, no revision, synthesis) |
| 14 | No unrelated source files changed | PASS (source hashes unchanged; `git status` shows only `STATE.md` + this report tracked/new) |
| 15 | No build regression attributable to refresh | PASS. Every supplied fact is present in the page (20/20 checked strings, `£` correct). No confirmation claim (the only "confirmed" is the step-free placeholder "to be confirmed"). 5 placeholder markers. The Glaze Lab option is disabled. |

## 10. Source changes

None. The only failure (§4) is behavioural against a now-unambiguous text. Any further wording or placement change would be speculative from one run, and would itself need an organic validation. The milestone brief excludes it ("Do not change SKILL.md … merely because you can think of wording improvements").

## 11. Hypothesis

- **Accepted** for the §2 line, OQ-1 transport, F-1 and independence.
- **Rejected** for the §4 declaration: it was not emitted as visible text.

## 12. Limitations

- **One organic run.** No success rate can be inferred.
- **Human-launched run.** The classifier blocked the agent from launching it. The prompt was passed via Windows PowerShell `Get-Content`, which mis-decoded `£` (§4). D-1 is unaffected. OQ-1 is judged against the text as received.
- **Evaluation-context exposure (names only):**
  - The workspace nests `KC-01/` beside `_method/` and `_evidence/`, as EV-01 did. At 14:39:16 the builder listed both sibling folders, which exposed file names (`METHOD.md`, `prompt.txt`, `priming-scan.txt`, `guard-probe.txt`, …). It never read any of them.
  - The §2 line (14:37:12) came before that listing. The first `ls ..` showed only folder names.
  - If the exposure biased anything, it did not produce §4 compliance.
- **Timing evidence.** Timestamps come from the builder's session JSONL and the independent watcher; the stream-json itself has none.
- **Budget.** The 60-minute wall-clock budget excludes the time spent waiting for human action at the two permission gates. Active work stayed within budget.
- **§8 reviewer.** No `loop.md` §8 reviewer was used. This milestone's output is a behavioural validation, not an architecture, governance, source-family or strategy verdict. The design-output critique inside the run followed the skill's own protocol.

## 13. Final disposition

- **Milestone:** COMPLETED. The evidence is sufficient and nothing blocks it.
- **D-1:** partly resolved.
  - §2 PASS in this run.
  - §4 FAIL: behavioural non-compliance persists after `536575d` (0/1 post-fix).
  - HYPOTHESIS: not exercised.
- **OQ-1:** behaviourally revalidated in this organic run. PASS.
- **F-1 and Level 1/Level 2 independence:** intact.
- **Next action:** await human direction. Addressing the §4 residual would need a new, human-authorized milestone.
