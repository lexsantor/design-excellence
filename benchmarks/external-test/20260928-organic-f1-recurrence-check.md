# Refresh Installed Skill Copy + Controlled Organic F-1 Recurrence Check

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Authorization (human, verbatim):** "Autorizo el milestone Refresh Installed Skill Copy + Controlled Organic F-1 Recurrence Check."
- **Previous milestone:** Autonomous Issue Resolution & Escalation Policy (`7ff5790`). Previous relevant milestone: Mechanical Level 2 Brief Transport (`30706f5`), after F-1 was recorded in `25b4e3b`.
- **Workspace (disposable, outside both repositories):** `C:\Users\<user>\Desktop\de-l1l2-organic-f1-check-20260928` (`REPORT.md` there indexes every evidence file)
- **Repository files changed:** this report and `STATE.md` (operational and milestone-record fields). No skill source file, `loop.md` or other file changed.

## 1. Executive result

| Item | Verdict |
|---|---|
| **F-1** | **PASS**: rubric block exact, no forbidden transformation, no Level 1 leakage, process verified |
| Process verification | **VERIFIED**: fresh file extraction and a mechanical diff before dispatch, both visible as executed commands with output |
| C1 (Level 1 ordering) | PASS |
| C3 (reviewer independence) | PASS |
| C4 (evidence integrity) | PASS, with one reconstruction limitation (§8) |
| O-1 | PASS: literal `.design/context.md` kept in axis 1; separate do-not-open instruction present |
| Human escalation required | **No.** No human escalation was required |

One organic run (n=1). This is behavioural evidence for one build, not a guarantee.

## 2. Source and installed copy

- Repository HEAD `7ff5790` throughout the run; source skill tree clean in git, `critique-protocol.md` blob `fd17a92…` equals HEAD.
- Pre-refresh: 18 source and 18 installed files, exactly one mismatch, `references/critique-protocol.md` (installed `c980a41…`, the `e63d7b3` text; source `ef54d20…`), as expected.
- Refresh: the root deny ACE was lifted, the one stale file was copied, and the guard was restored. `icacls /restore` failed for lack of privilege, so the identical deny ACE (`D;OICI;DCLCDTSD` for the user SID) was re-added directly (§6). The full-tree ACL dump after the refresh is byte-identical to the one before it.
- Parity: 18/18 SHA-256 identical after refresh and again after the run; installed copy unchanged during the run; source unchanged.
- Guard, tested after refresh and after the run: read OK; append, overwrite, create-file, create-directory and delete all denied.

## 3. Organic run

| Item | Value |
|---|---|
| Project | `OB-01/`, empty at start |
| Builder | one fresh headless `claude -p` session, `claude-opus-5-5`, same invocation as `25b4e3b` (`_method/METHOD.md`, frozen before the run) |
| Prompt | fictional "Fernhollow Community Print Workshop", three static pages sharing one header and footer, "our live public website, the first thing most people will ever see of us" (production-facing / brand-critical trigger); all facts as placeholders. No word about critique, review, level, axis, rubric, score, transport, verbatim, independence, ordering, F-1 or earlier tests. The `/design-excellence` prefix loads the skill in the subject session, as in the earlier checks; the main agent did not invoke the skill |
| Run | 10:41:32Z to 10:55:40Z, exit 0, 74 builder tool calls, no rerun |
| Initial protocol read | 10:42:02Z (#06), installed path, complete (19,516 chars) |
| Level 1 recorded | 10:49:45.7Z tool call; on disk 10:49:48.1Z (independent watcher) |
| Rubric extraction | 10:49:54.5Z (#48), 7 min 52 s and 41 tool calls after the protocol read |
| Brief assembled + diffed | 10:50:34.9Z (#54) |
| Level 2 dispatch | 10:50:43.1Z (#55), 8 min 41 s and 48 tool calls after the protocol read |
| Reviewer report returned | 10:52:56.3Z |
| Post-report Level 1 activity | 10:55:08.7Z, appended and labelled non-independent (§5) |

**Condition match with F-1.** In the F-1 run the brief was written 7.5 min and 48 tool calls after the only protocol read. Here dispatch came 8 min 41 s and 48 tool calls after it, with the whole three-page build, rendering and fixes in between. The long-session condition was reproduced without forcing it.

## 4. Transport evidence

**Extraction (#48).** A `node` script read `C:/Users/<user>/.claude/skills/design-excellence/references/critique-protocol.md` from disk. It sliced the `not assessable` rule from line 7 between its two anchors, and took lines 9–14 as the axis list, with bound checks that line 9 starts `1. **Genericness**` and line 14 starts `6. **Technical`. It wrote both passages to `/tmp/l2/rubric.txt`. The earlier session read (#06) was not the source.

**Assembly and comparison (#54).** `brief.md` was built by shell concatenation, with `cat rubric.txt` placed between `<<<RUBRIC` / `RUBRIC>>>` delimiters. The block was never retyped. The same command then extracted the delimited block back out of `brief.md`, ran `diff rubric.txt extracted.txt`, and printed `RUBRIC IDENTICAL` before the Agent call. The builder's text before dispatch reads "Rubric block matches the source byte-for-byte."

**Timing nuance.** Five tool calls (screenshots for the brief, 40 s) separate the extraction from the brief write. I read these as one brief-construction step. The rule targets regeneration from an earlier read, and here the text went file to file. If read more strictly, that is the only point open to question.

**Dispatch form.** The Agent prompt (333 chars) points the reviewer to `C:/Users/<user>/AppData/Local/Temp/l2/brief.md`. The reviewer's first tool call read it whole (no offset or limit).

**Sent vs received.** The builder deleted `/tmp/l2` in its final cleanup, so no copy of the written file exists. The sent file was reproduced deterministically: the logged #48 script was re-run on the unchanged installed protocol, and the #54 template was rendered with its logged variables. The reconstruction is byte-identical (11,291 bytes) to what the reviewer received (its Read result, line-number prefixes stripped).

**Independent comparison.** Performed after the run by the main agent (`_method/verify_block.py`), against passages extracted anew from the installed file:

| Passage | Exact match | Changed | Omitted | Inserted |
|---|---|---|---|---|
| `not assessable` rule | yes | none | none | none |
| Axis 1 Genericness | yes | none | none | none |
| Axis 2 Hierarchy | yes | none | none | none |
| Axis 3 Distinctiveness | yes | none | none | none |
| Axis 4 Craft correctness | yes | none | none | none |
| Axis 5 Accessibility | yes | none | none | none |
| Axis 6 Technical correctness | yes | none | none | none |

- The delimited block equals the expected block byte for byte (`diff` empty): it contains nothing else, is contiguous and is in the specified order. All citations, phase tags, parentheticals, cross-references, qualifiers (axis 4's "not all seven — only the ones loaded per `SKILL.md` §7") and formatting marks are present. No paraphrase or substitution.
- The builder's extraction equals the independent extraction byte for byte.
- **IDs:** Rule Catalog categories and Anti-Slop entries appear in Recorded inputs as ids only ("ids only"), with no definitions. For normative text, the access part names the governed files for the reviewer to read (`SKILL.md` including §6, `anti-slop-registry.md`, `rule-catalog/*.md`, `principle-pool.md`, `visual-references.md`), a form the specification allows. There is no partial excerpt or gloss.
- **Level 1 leakage:** none. Outside the block, no Level 1 score, finding, failing axis, dispatch-reason axis, or axis outcome appears. The scan found 0 hits for Level 1 terms, the recorded scores, `not assessable: first`, carried/carrier, baseline, mitigat, weakness, `/5` and failing. "score" and "context.md" each occur once, in the task and access instructions. "Prior Fingerprint History entries: none exist" is stated as an input, and axis 3's outcome is left to the reviewer. The trigger named is "production-facing / brand-critical work", as permitted.

**O-1.** The literal "(in `.design/context.md` only where this run may write it, as above; otherwise in the run's own report)" is inside the transported axis 1, unchanged. Separately, the access part says: "Do not open …/OB-01/.design/context.md, anything under …/.design/ …". Neither was edited to fit the other.

## 5. Independence

- **Level 1:** complete and on disk (Fingerprint History, marked "recorded before Level 2 dispatch") 6 s before the extraction, 47 s before the brief and 55 s before dispatch.
- **Not revised:** the diff of the pre-report and final `context.md` is append-only. All six pre-dispatch Level 1 lines are unchanged.
- **Post-report Level 1:** one pass exists, explicitly labelled "formed after Level 2, not independent of it". The synthesis compares Level 2 with the pre-dispatch values ("Disagreement on Craft (L2 3 vs L1 4)"), and the adopted finding is recorded as a synthesis outcome. The post-report pass is not used as the independent comparison.
- **Reviewer:** fresh `lexia-design:visual-critic` (the protocol's preferred specialised critic). Not a fork: its first event is the dispatch prompt, and meta shows `foreground`, spawn depth 1.
- **Reviewer inputs:** the dispatch prompt; `brief.md`; the four project code files plus `favicon.svg`; five screenshot copies in `/tmp/l2/shots`; Grep and Read on the governed `anti-slop-registry.md`, `rule-catalog/*` and `motion.md` (as the brief directed); one `node -e` contrast calculation (stdout only). It opened nothing under `.design/`, nor `README.md` or `.playwright-mcp/`.
- **No project writes:** the reviewer used no Write or Edit, and the watcher shows no project file change between 10:50:43Z and 10:53:52Z (first builder REFINE write).
- **Report integrity:** the reviewer's final text (`level2-report-raw.md`) equals, after de-indentation, the report inside the harness hand-back wrapper the builder received.

## 6. Autonomous issue resolution (`loop.md` §2.1, first real use)

| Issue | Why in scope | Correction | Validation | Interrupted? |
|---|---|---|---|---|
| `icacls /restore` of the saved ACL failed (missing restore privilege), leaving the guard lifted after the copy | restoring the guard is required by the milestone; reversible | re-added the identical deny ACE with `icacls /deny` | ACL dump byte-identical to pre-refresh; six guard behaviours tested | No |
| The builder deleted the written `brief.md`, so no sent copy survived | evidence gathering for this milestone | recovered the received text from the reviewer's Read result and reproduced the sent file from the logged commands | byte-identical | No |
| My own conversion of the Read result added an extra final newline, giving a false 1-byte mismatch | own analysis error | fixed the conversion | `cmp` identical | No |
| A validation command timed out on a recursive scan of the large untracked `scratchpad/` (case E) | validation of untouched untracked items | stopped it; bounded depth-3 freshness check plus directory mtimes | nothing newer than the run start | No |

No case B or D arose, so no escalation question was asked. **No human escalation required.** No fix touched a governed file.

## 7. Validation

1. Repository HEAD `7ff5790` before commit; tracked changes only `STATE.md` and this report.
2. Installed/source parity 18/18 after refresh and after the run.
3. Write guard re-tested after the run: read OK, other five operations denied.
4. No source skill modification (source hash lists pre/post identical).
5. Pre-existing untracked `rules.md`, `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md` and `scratchpad/` untouched (mtimes 2026-09-23 / 2026-09-27; nothing under `scratchpad/` newer than the run start at depth ≤ 3).
6. Workspace holds the complete evidence (index in its `REPORT.md`).
7. Items 8 to 15 of the brief: §4 to §6 above. No push.

## 8. Limitations

- **Sent brief reconstructed, not captured.** The builder deleted `/tmp/l2`. The sent file is a deterministic reproduction from the logged commands and the unchanged protocol. The direct evidence that the embedded block equalled the extraction at send time is the builder's own `diff` output ("RUBRIC IDENTICAL") within the command that wrote the file. The received text is captured directly.
- **Extraction precedes the brief write by 40 s and five screenshot calls** (§4). I judge this compliant; a stricter reading of "the same step" could dispute it.
- **The builder's diff checks the block against its own extraction,** as specified, not against a second read. That the extraction itself was correct is established only by the independent check here.
- **Reviewer isolation from `context.md` rests on instruction** (earlier O-3): the reviewer had Read, Grep and Bash. It complied; access control did not enforce it.
- **Causality.** n=1, and the site, brand and page count differ from the F-1 run. The run shows the prescribed method executed and produced exact transport under F-1's timing conditions. It does not isolate the specification change as the only cause, and it does not show the method is always followed.
- **Harness environment.** The headless builder inherits the user's global settings and hooks, the same as in earlier checks.
- **Side effect.** The builder left `C:\Users\<user>\AppData\Local\Temp\contrast.mjs` (copied to the workspace), outside every governed location.

## 9. Agents

The main agent spawned no subagent. Operationally, the run involved the headless builder session plus the one reviewer it dispatched: 2 if the builder counts, within the cap of 3. No parallel writes to governed artifacts. No §8 reviewer was required, because this milestone's output is a behavioural verdict on a check, not a verdict on architecture or governance. The Level 2 reviewer inside the run is the subject's own.

## 10. Final interpretation

**What the evidence proves.** In one organic three-page build, the Level 2 brief was written 48 tool calls and nearly nine minutes after the only session read of the protocol, the condition under which F-1 occurred. The builder did not rely on that read. It extracted the two passages from the file with a command, inserted them by file concatenation, and mechanically diffed the result before dispatch. The block the reviewer received is byte-exact against an independent extraction, and no Level 1 content leaked. C1, C3, C4 and O-1 held as well.

**What it does not prove.** That F-1 cannot recur, that every builder or model will follow the method, or that the specification change alone caused the difference. It is one run.

## 11. Recommended next action

Treat F-1 as not recurring under the current specification and close it in the record. Take no further specification or benchmark action on Level 2 transport unless a later organic run shows a deviation. (Recommendation only; not authorized.)
