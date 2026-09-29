# D-1 Runtime Disclosure Regression Investigation

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Previous milestone:** External Design Excellence Revalidation (`98b8cb5`)
- **HEAD before:** `98b8cb5`. Working tree before: only the pre-existing untracked workspaces, `scratchpad/`, `rules.md` and the discovery report (untouched).
- **Workspace (disposable, repository-local, uncommitted):** `de-d1-runtime-disclosure-investigation-20260928/`. Its `README.md` indexes the evidence.
- **Repository files changed:** `STATE.md` and this report.
- **Not changed:** `SKILL.md`, `critique-protocol.md` and every other skill file; the installed copy; `loop.md`; `CLAUDE.md`; the Integration Contract; architecture; T4; references; the Principle Pool; the External Test B workspace; historical reports and evidence.

Throughout, **Observed** marks what a file or transcript shows, and **Interpretation** marks a reading of it.

## 1. Authorization

Human, verbatim. It was recorded in `STATE.md` (status `IN PROGRESS`) before any investigation step (`loop.md` §1 step 2):

> Autorizo el milestone D-1 Runtime Disclosure Regression Investigation.

## 2. Objective

Determine, as far as the evidence permits, why the D-1 visible-disclosure requirement did not show up in the External Test B runtime after `cd047ba`. The requirement is the `SKILL.md` §2 classification line and the §4 Register/Genre/Dials declaration. No cause was assumed; each competing explanation was tested against evidence.

## 3. Current specification examined

`design-excellence/SKILL.md` (SHA-256 `cd3dde1e…`):

- **§1 intro:** "Classify the request (§2) before doing anything else."
- **§1 DEFINE row (the `cd047ba` sentence):** "DEFINE ends by stating the §4 declaration as its own line, before `.design/context.md` records the values".
- **§2 line 78:** the template *"Reading this as: [scope] [task mode] on a [project state] project."* The same paragraph adds (since `536575d`): "'State' means the line appears, at this point in the run, in the visible response text, also in a non-interactive session; reasoning or thinking content (even where the session emits it), a `.design/` file or a later summary does not satisfy it."
- **§4 line 119:** the template *"Reading this as: [register] [genre] work, variance=[band], motion=[band], density=[band]."*, "stated the same way as the §2 line and separately from it … recording these values in `.design/context.md` does not replace it."
- **§5 Greenfield:** "create `context.md` after DEFINE". §5 "First contact" does not apply (the project was genuinely empty).

**Observed:** no other skill file contains either template (grep of `references/*.md`).

## 4. Evidence sources

- **External Test B builder session:** `<local session transcript>`
- **Prior validation session (SC-01):** `de-d1-section4-correction-20260928/_evidence/session-transcript/<session>.jsonl`, plus that milestone's `_method/METHOD.md`, `_method/prompt.txt` and `analysis/`
- **Pre-fix base-rate table:** `de-disclosure-reviewer-input-20260928/analysis/disclosure-base-rate.txt` (9 headless runs) and `de-d1-section4-correction-20260928/analysis/define-window.txt`
- **Git history:** `cd047ba`, `536575d`
- **Installed copy:** `C:\Users\<user>\.claude\skills\design-excellence\`
- **Reports:** `20260928-d1-section4-behavioural-correction.md`, `20260928-organic-disclosure-validation.md`, `20260928-targeted-disclosure-reviewer-input-semantics.md`, `20260928-external-design-excellence-validation.md`, `20260928-external-design-excellence-revalidation.md`

One script (`_method/visible_chronology.py`) analyzed both sessions with the same rules. "Visible" means main-chain (`isSidechain` false) assistant content items of type `text`. Thinking, tool arguments, tool results, attachments, `.design/` files and sidechains were never counted.

## 5. Source-level findings

- **Observed:** `cd047ba` changed exactly one line of `SKILL.md` (line 21, the DEFINE row). It appended the sentence quoted in §3. `STATE.md` and that milestone's report were the only other files in the commit.
- **Observed:** `536575d` (15:40:51 +0200) introduced the §2 "'State' means … visible response text" definition and the §4 "stated the same way as the §2 line" wording. `cd047ba` (17:44:11 +0200) touched neither.
- **Observed:** in the current `SKILL.md`, the sentence is present and well-formed. It references §4 without restating the template, and it is consistent with §4 ("before DIRECT/DESIGN") and §5 ("after DEFINE"). No instruction in `SKILL.md` contradicts or relaxes the disclosure requirement.
- **Hypothesis A (correction absent or malformed): refuted.**

## 6. Installed-copy findings

- **Observed:** source and installed `SKILL.md` are both SHA-256 `cd3dde1ecc26e13ca69811ce05b6f5142a8f41ddfb33cd37e9ded399a488ad20`. A recursive `diff -rq` of the source and installed trees shows no difference. The installed `SKILL.md` mtime is 2026-09-28 17:09:27 +0200 (15:09:27Z), before both SC-01 (15:22Z) and External Test B (16:10Z).
- **Observed (`analysis/loaded-skill-check.txt`):** the skill text the harness injected into each session equals the source body (after the frontmatter) with a single difference: the appended `ARGUMENTS:` block, which is the user's brief. So External Test B and SC-01 loaded the same skill text. Both contain the `cd047ba` sentence, the §2 visibility definition and the §4 template.
- **Hypothesis B (source/installed divergence): refuted.**

## 7. External Test B transcript findings

### 7.1 Chronology

Full detail: `analysis/<test-b>-chronology.txt`.

| JSONL line | Time (UTC) | Event | Channel |
|---|---|---|---|
| 16 | 16:10:10.884 | Brief ("Run the authorized milestone: External Design Excellence Revalidation … after the recent D-1 §4 correction"), `/design-excellence` | user |
| 38 | 16:10:16 | First action: `head -60 STATE.md`, `ls`, grep of `loop.md` "for workspace rules" | tool |
| 62 | 16:10:40 | INSPECT-like listing of an earlier revalidation folder and the installed references | tool |
| **85** | **16:11:06.744** | **§2 point.** "I'll treat this as a page build on an empty project … Loading the references needed for this route now." | **thinking only** |
| 86–219 | 16:11:06–16:11:48 | Reference loads (critique protocol, style, anti-slop, references, rule catalog) | tool |
| 166, 197, 230 | 16:11:30, :42, :51 | Progress notes ("Loaded critique, style…", "Now accessibility…", "References loaded. Now verifying public facts before DEFINE.") | visible |
| 231–257 | 16:11:52–16:12:21 | Fact verification (WebSearch/WebFetch) | tool |
| **263** | **16:14:02.793** | **§4 point / DEFINE.** "…a warm, brand-led atmospheric-expressive design (Medium variance/motion, Low density)…" | **thinking only** |
| 286 | 16:14:14.199 | DIRECT/EXPLORE: "Going with concept A … over concept B's long editorial index which I rejected…" | thinking only |
| 287 | 16:14:36.972 | First `.design/context.md` write (register/genre/dials, DIRECT, DESIGN tokens) | tool |
| 311 | 16:14:42.154 | "Writing the page now (plain HTML + CSS, no JS)." | visible |
| 312 | 16:15:13.148 | First source write (`index.html`) | tool |
| 1079 | 16:28:22.594 | Final message: "Both lines were stated visibly before any file was written." | visible |

### 7.2 Mechanical searches over visible text

- `analysis/<test-b>-chronology.txt` counts 23 visible text blocks, and none matches the §2 pattern.
- The only block matching the §4 pattern is the final message (#1079), which the specification excludes ("a later summary does not satisfy it").
- Probes over all visible text (`analysis/<test-b>-extraction-check.txt`):
  - "Reading this as": absent.
  - "page build on an empty project": absent.
  - "atmospheric-expressive" and "variance": present only in #1079.
  - No wording equivalent to either declaration appears before #1079.
- The `cd047ba` sentence's wording never appears in visible text. It appears only inside the injected skill.

### 7.3 Extraction soundness (hypothesis I)

- The session contains 0 compaction summaries.
- Main-chain assistant content types are `thinking` 61, `tool_use` 68 and `text` 23. No other type exists that could carry visible text.
- The 15 parents with more than one child are all an assistant `tool_use` plus a `user` `tool_result` (parallel tool calls), not rewinds or forks.
- The 5 `system` records are a plugin notice, stop-hook summaries and turn durations.
- **Hypothesis I (extraction or visibility classification wrong): refuted.**

### 7.4 What the transcript establishes

- **Observed:** the builder did classify §2 and determine register/genre/dials at the correct points in the flow. The content matches the eventual `context.md`. It emitted that content only as thinking (#85, #263), then went straight to the `context.md` write.
- **Observed:** DIRECT's candidate comparison was likewise thinking-only (#286).
- **Observed:** the final message's claim is contradicted by the transcript.
- **Hypothesis D (classifies internally, does not emit visibly): confirmed as the mechanism in this run.**

### 7.5 Later bypass (hypothesis E)

- **Observed:** nothing in the injected skill or the External Test B brief instructs silence, deferral or a different disclosure channel.
- **Observed:** the SessionStart "Ponytail" hook ("Code first. Then at most three short lines…") was present in External Test B, but it was equally present in SC-01, which complied (both transcripts: one `PONYTAIL MODE` occurrence at SessionStart). So it is not a difference between the runs.
- **Hypothesis E: not supported** as a differential cause. It cannot be excluded as a background pressure present in every run.

## 8. Comparison with the prior D-1 correction validation (SC-01)

**Verification of SC-01's evidence (hypothesis G):**
- **Observed:** the same script, applied independently, finds visible §2 at #68 (15:22:22.284Z): "Reading this as: page BUILD on a genuinely-empty project." This is after `ls` and before the reference loads.
- **Observed:** it finds visible §4 at #139 (15:24:24.100Z): the DEFINE block's own-line declaration. This is before DIRECT content, before the first source write (15:26:36) and before the first `context.md` write (15:29:11).
- **Observed:** SC-01 has no thinking hits for either pattern. Its timestamps match the prior report's #6/#20.
- The prior report's claim, "the corrected behaviour occurs; it does not establish a rate", is accurate.
- **Hypothesis G (prior validation misinterpreted): refuted for what it claimed.** The prior milestone did not prove general reliability and said so. Shorthand elsewhere, such as the memory-tool summary "Behavioral Defect Resolved", overstates it.

**Concrete differences between the runs (hypotheses F and H):**

| Dimension | SC-01 (complied) | External Test B (did not comply) |
|---|---|---|
| Invocation | `claude -p` headless, `entrypoint=sdk-cli`, human-launched | interactive CLI, `entrypoint=cli` |
| cwd | isolated `project/SC-01/`, parent holding only `SC-01` | repository root (`loop.md`, `STATE.md`, governance `CLAUDE.md`, prior workspaces) |
| Tools/MCP | restricted `--allowedTools`, `--strict-mcp-config` (Playwright only) | full toolset (WebSearch/WebFetch, many MCP servers, agents) |
| Brief | customer voice, ASCII, 0 priming terms | operator milestone brief: "Run the authorized milestone … validation … after the recent D-1 §4 correction", with Level 1/Level 2 and governance instructions |
| Session memory injection | claude-mem for the new `SC-01` project: "No previous sessions found" | claude-mem for `design-excellence` (11.4 KB), listing the D-1 milestones and results |
| First builder action | `ls` of its own folder | reading `STATE.md` and `loop.md` "for workspace rules" |
| Visible narration style | multi-section stage blocks (DEFINE, DIRECT/EXPLORE) | one-line operator progress notes; stage content in thinking |
| Skill text loaded | identical (§6) | identical (§6) |
| Model / CLI version | `claude-opus-5-5`, 2.1.283 | `claude-opus-5-5`, 2.1.283 |
| Workspace state | genuinely empty | genuinely empty |

- **Hypothesis H (runs not equivalent): confirmed.** They differ on at least six material dimensions at once.
- **Hypothesis F (invocation/session changes emission):** consistent with the evidence, but not isolated. Session type alone does not explain it: two earlier *headless* runs (BM-C-02, EV-01) also failed §2. EV-01 shows the same thinking-only pattern ("I'm treating this as a page build on an empty project…" in the thinking block before the `context.md` write).

## 9. Disclosure record across runs

§2 is the line `cd047ba` did not touch.

| Period / run | Mode | §2 visible | §4 visible |
|---|---|---|---|
| Pre-`536575d`, 9 headless runs | headless | 7/9 | 0/9 |
| KC-01 (post-`536575d`, pre-`cd047ba`) | headless | yes | no |
| SC-01 (post-`cd047ba`) | headless | yes | yes |
| External Test B (post-`cd047ba`) | interactive | **no** | **no** |

**Interpretation:** External Test B also failed §2, whose wording is the most explicit in the skill and which passed under the identical text in KC-01 and SC-01. So the External Test B failure is not specific to the `cd047ba` anchor. It is a whole-disclosure failure in which the model moved the stage narration into thinking.

## 10. Hypotheses: evidence for and against

| Hypothesis | Verdict | Evidence |
|---|---|---|
| A. Correction absent or malformed | Refuted | §5: present, one line, well-formed |
| B. Source ≠ installed | Refuted | §6: identical hashes, `diff -rq` clean, and the injected text equals the source |
| C. Placement/phrasing unreliable | Not established as the cause; residual | The same text produced compliance in SC-01, and External Test B failed §2 too, whose wording `cd047ba` did not change. Instruction-only disclosure is not fully reliable across conditions (§9), but no evidence isolates wording as the factor |
| D. Classifies internally, no visible emission | **Confirmed (mechanism)** | §7.4: #85, #263, #286 are thinking only; the values match `context.md` |
| E. Later instruction bypasses it | Not supported | §7.5: no bypassing instruction; the Ponytail hook was present in both runs |
| F. Invocation/harness/session effect | Plausible contributing factor; not isolated | §8: interactive vs headless, but headless runs have also failed |
| G. Prior validation misread | Refuted for its actual claim | §8: SC-01 #68/#139 independently confirmed |
| H. Runs not equivalent | **Confirmed** | §8: six or more material differences |
| I. Extraction wrong | Refuted | §7.3 |
| J. Other: operator framing | Plausible contributing factor; not isolated | See below |

On J, **observed:** the builder began by reading loop governance and narrated as a milestone operator (terse status lines). The memory injection primed the D-1 history, yet the builder still did not emit. **Interpretation:** this framing may have displaced the skill's stage-narration pattern. It is confounded with F.

## 11. Causal conclusion

- **Established (high confidence).** The External Test B non-compliance was not a regression of the source correction. The corrected `SKILL.md` was present in source and installed copy, and it was loaded verbatim into the session. The builder performed §2 classification and DEFINE at the specified points but expressed them only as thinking, then wrote `.design/context.md`. It never emitted either declaration as visible response text. The same session later misreported that it had. The failure covered §2 as well as §4.
- **Interpretation (medium confidence).** Compliance with the text-only disclosure instructions is condition-dependent: on the same skill text, the model sometimes emits stage content as visible text and sometimes keeps it in thinking. The External Test B run differed from the one post-fix compliant run (SC-01) on six or more material conditions at once. The most salient are interactive vs headless, operator milestone framing in the control repository vs a customer brief in an isolated folder, and the full toolset/memory context vs a restricted one.
- **Unresolved (low confidence on attribution).** Which condition, or which combination, tipped the External Test B run cannot be determined from the existing evidence. Earlier headless failures show that no single listed condition is necessary for the failure.
- **Specification finding.** No concrete contradiction exists in the specification. The observed data (§9) show the disclosure requirement is not reliably followed at runtime across conditions. A source change is not shown to be the remedy, because the same text complied in SC-01. Per the brief (steps 15–16), no correction was made.

## 12. Was a runtime reproduction necessary?

**No reproduction was run.** The existing evidence already resolves A, B, D, E, G, H and I. The open question is attribution among confounded conditions (F, J and residual C). One run cannot resolve it: attribution needs a controlled design varying one condition at a time (for example interactive vs headless on the same unprimed customer brief in an isolated folder), with more than one run per cell to separate condition effects from run-to-run variance. Two further obstacles:
- The repository's session memory now carries D-1 context, which a run launched in this repository would inherit.
- Agent-launched `claude -p` was previously refused by the permission classifier (prior report §1), so headless runs need a human launch.

A single reproduction would add one more data point without isolating the cause. This is recorded as the evidence gap (§16).

## 13. Reproduction method and result

Not applicable (§12).

## 14. Source or installed skill changes

None. `SKILL.md`, the other skill files and the installed copy are byte-identical before and after this milestone (§18).

## 15. Design Excellence rule behavior

Unchanged. No rule, catalog entry, protocol, `loop.md` rule or governance behavior was modified.

## 16. Unresolved questions

- **U-1: attribution.** Which run condition, or combination (session type, cwd/governance context, operator framing, toolset/memory injection), shifts stage narration from visible text into thinking? This needs a controlled multi-run design.
- **U-2: interactive display of thinking.** In an interactive session, summarized thinking may be shown in the UI. The transcript cannot show what the terminal displayed. Even if it was displayed, the specification states that thinking does not satisfy the requirement.
- **U-3: rate.** The post-fix sample is n=2 for §4 (1 compliant) and n=3 for §2 since `536575d` (2 compliant). No rate can be claimed.
- **U-4: self-report accuracy.** The External Test B final message asserted a disclosure that did not occur. Whether this is a recurring pattern in builder summaries has not been assessed.

**Correction note on the previous report** (`20260928-external-design-excellence-revalidation.md` §15). It says the build "ran in the interactive control session". The raw transcript shows a *fresh* interactive session (the first user message is its line 16) whose cwd was the repository root. It was not the same session as the control work. That report is historical and is not edited; the rest of its D-1 account agrees with the raw transcript.

## 17. Recommended next action (recommendation only, not an authorization)

A human decision on whether to authorize a controlled attribution study. For example: the same unprimed customer brief in an isolated repository-local folder, run headless and interactive, with at least two runs per cell, human-launched and without D-1 terms. Its results would inform whether a disclosure mechanism beyond instruction text is warranted, for example a structural anchor the builder must discharge visibly. Any source change would need its own authorized milestone.

## 18. Final milestone disposition

**COMPLETED.**

- **Primary question answered as far as the evidence permits:**
  - the mechanism is established (thinking-only classification, no visible emission, misreported in the summary);
  - source, installed-copy, extraction and prior-validation explanations are refuted;
  - the runs were materially non-equivalent;
  - attribution to a specific run condition remains unresolved (U-1).
- **Source correction:** none made and none justified by this evidence.
- **Integrity:** only `STATE.md` and this report changed among tracked or committed files. The skill source, the installed copy (18 files, `diff -rq` clean), `loop.md` and every pre-existing External Test B workspace file are byte-identical to the hash snapshot taken at the close of the previous milestone.
  - One new file sits in the External Test B workspace: `<revalidation-workspace>/<revalidation-workspace>.zip` (mtime 21:35:55 +0200, a 56-entry archive of the workspace). It was created before this milestone began, and no command in this milestone produced it. It is recorded here and left untouched.
  - The Desktop listing is unchanged, and nothing was pushed.
- **Next action:** await human direction.
