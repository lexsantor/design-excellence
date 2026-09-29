# Targeted Specification Clarification: Mechanical Level 2 Brief Transport

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Authorization (human, verbatim):** "adelante siguiente paso"
- **Previous milestone:** Refresh Installed Skill Copy + Controlled Behavioral Check (`25b4e3b`), which recorded F-1 and O-1
- **Changed:** `design-excellence/references/critique-protocol.md`, Level 2 "Implementation" step 1 only
- **Not changed:** the Level 1 section and the Order paragraph (lines 1–33, byte-identical), the no-render precedence paragraph, steps 2 and 3, the honest-limitation paragraph, "What Level 2 is not", `SKILL.md`, rule catalogs, the Anti-Slop registry, the installed skill copy, `<external-test-a-project>` and earlier benchmark workspaces

## 1. Root cause of F-1

Evidence from the previous check (`C:\Users\<user>\Desktop\de-l1l2-behavioral-check-20260928\_evidence`, session transcript). The builder's reasoning blocks are redacted, so only its actions are observable.

| Observation | Evidence |
|---|---|
| The builder read `critique-protocol.md` once, at 09:45:21Z | session JSONL |
| It wrote the brief as a single Agent tool input at 09:52:56Z: 7.5 minutes and 48 tool calls later, without re-reading the file and without any extraction command | session JSONL |
| It labelled the rubric "definitions copied as written" and the rule "as written" while editing both | `level2-brief-sent.md` |
| The edits cluster on text addressed to the builder or pointing outside the brief (citations, phase tags, `SKILL.md` §6/§7, `accessibility.md` sections, the `.design/context.md` recording parenthetical), and on qualifiers turned into their application to the run (axis 4). Anti-Slop and rule ids received improvised definitions | `brief-verification.txt` |
| When brief-building is the only task and the protocol has just been read, the **old** text produced a fully verbatim, leak-free brief, retyped in one Write (§4, R2) | micro-test R2 |

**Root cause.** The old step 1 required a verbatim *result* but left the *method* to the builder, and the builder reconstructed the text:

1. **Stale source.** Nothing required the text to be taken from the file when the brief is written. Inside a long build session, the builder regenerated the rubric from a read 48 tool calls earlier. R2 shows that the same wording is followed verbatim when the read is fresh.
2. **Mixed brief.** The rubric, recorded inputs, access rules and reviewer instructions were one prose stream. Builder-authored help (a §6 summary, a category list, id definitions) therefore landed inside or in place of rubric text.
3. **Self-containment pressure without a rule for references.** A "self-contained brief" whose definitions cite files the reviewer does not have invites resolving the citations: deleting them, or glossing them.
4. **O-1 unresolved.** Axis 1's literal `.design/context.md` collided with the no-pointer rule, and the builder removed it.
5. **No mechanical check.** Compliance relied on the builder's own reading, the same judgement that made the edits.

Items 1 and 5 are observed. Items 2–4 are inferred from the pattern of deviations; the builder's reasons are not observable.

## 2. Specification change

Step 1 keeps its opening sentence. The brief is then assembled from four separately delimited parts, plus the artifact under review with its kind in its own section, and nothing written for one part goes inside another:

- **Rubric block (literal transport).** Exactly two passages of the Level 1 section, named by anchors: the `not assessable` rule ("An axis, or an always-on check within it" through "does not count toward the escalation trigger below.") and axis items 1–6, each complete.
  - Read or extracted from the file in the same step that writes the brief. An earlier read does not count, and the block is never retyped from memory.
  - Every word, qualifier, parenthetical, citation, phase tag, cross-reference and formatting mark stays. Equivalent meaning is not enough, and each observed deviation is named as forbidden.
  - Compared mechanically before dispatch (for example, written to a scratch file outside the project and diffed). Reading it over is not a comparison, and a differing block is never sent.
  - The synthesis says literal transport was not verified only where no file-read or comparison capability exists.
- **Recorded inputs.** The inputs as before, plus in-scope Rule Catalog categories and Anti-Slop entries by id only, with no definitions. The no-conclusion rule now applies "in any part".
- **Access and inspection instructions.** The existing no-pointer and do-not-open rules, the O-1 resolution, and a rule for cited references: name the governed file, or carry the complete section or entry extracted and compared the same way. Never a partial passage, summary or improvised definition. The reviewer writes nothing.
- **Reviewer task.** Score against the block. When DEFINE recorded DETECTED / EVIDENCED, apply the structural test "as stated in axis 1 of the rubric block, without restating it". Operational requests live here and never qualify the block.
- **"Do not include"** is unchanged in substance and now reads "in any part". A blank line now separates it from the no-render paragraph.

Every clause of the old step 1 is present. The sentences that changed wording are restructured, not dropped: the old "copied as written" list is a subset of the new deviation list; the inputs, no-pointer, copy-from-`context.md`, writes-nothing, no-conclusion and "Do not include" clauses moved into their parts; the structural-test instruction now points at the block instead of asking for a second copy.

## 3. O-1 disposition

Resolved without weakening either rule. The literal `.design/context.md` inside the rubric block (axis 1) is rubric text, not a pointer or access instruction, and stays unchanged. The access part's instruction not to open `.design/context.md` governs access, and neither is edited to accommodate the other.

## 4. Validation

**Deterministic checks**
- Lines 1–33 are byte-identical to `25b4e3b`.
- Everything from step 2 to the end of the file, and the no-render paragraph, is byte-identical.
- Both anchors and axis 4's quoted qualifier each occur exactly once in the Level 1 section, and axis items 1–6 are present.
- `git diff --check` is clean.
- No other skill file describes the brief: a search of `SKILL.md`, the rule catalog and the Anti-Slop registry found none.
- No new rule id, stage, mode, score, trigger or P-layer. Level 1 remains the only normative rubric source; the block is per-dispatch transport "not kept anywhere else".

**Bounded micro-test** (brief construction only; no build, no dispatch)
- Workspace: `C:\Users\<user>\Desktop\de-l2-transport-microtest-20260928`; method frozen in `_method/METHOD.md`.
- Fixture: the previous check's artifact plus its pre-dispatch `context.md`, which contains the recorded Level 1 line, used as the leakage probe.
- Each run was a fresh `claude -p` with no Agent tool. The condition names seen by the subject were neutral.

| Run | Protocol | Method used | Axes 1–6 + rule verbatim | Level 1 leak | O-1 | IDs |
|---|---|---|---|---|---|---|
| R2 | old step 1 (`25b4e3b`) | retyped in one Write | 7/7 exact | none | literal kept; reviewer told the recording clause does not apply to it | ids only |
| R1 | new step 1, pre-review draft | Python extraction script | 7/7 exact | none (grep-checked by the subject) | literal kept; stated as not an access instruction | ids only |
| R3 | new step 1, final | extraction script + mechanical `diff` ("no differences") | 7/7 exact | none | literal kept; stated as rubric text | ids only |

All fixtures were unchanged (SHA-256). Side effect: R1 and R3 wrote scratch files to `C:\Users\<user>\AppData\Local\Temp` (`brief_template.md`, `build_brief.py`, `r3_brief/`), copied to `_evidence/temp-side-effects/`. They are outside every governed location.

**Reading.** The micro-test does not discriminate between old and new text, because R2 passed too. It does not reproduce F-1's condition (a brief written late inside a long build). It shows that the final text executes as intended: extraction plus a mechanical diff, and it changed the method the builder chose. It does not show that F-1 cannot recur in an organic run.

## 5. Independent review and reconciliation

One fresh read-only general-purpose reviewer (blind to the main agent's assessment; given the F-1 evidence, both protocol versions and the questions). No BLOCKING.

| Finding | Class | Disposition |
|---|---|---|
| "as read when the brief is written" allows reuse of an earlier read, which was the main cause | SHOULD-FIX | adopted: "in the same step that writes the brief; an earlier read in the session does not count" |
| The comparison is unspecified; a visual self-check is the check that already failed | SHOULD-FIX | adopted: mechanical comparison, example diff, "reading it over is not a comparison" |
| A reference excerpt could be shortened into a summary | SHOULD-FIX | adopted: complete section or entry, extracted and compared as the block is |
| The structural-test instruction invites a second, paraphrased copy | SHOULD-FIX | adopted: apply it "as stated in axis 1 of the rubric block, without restating it" |
| The artifact under review fits none of the four parts | SHOULD-FIX | adopted: "plus the artifact under review, stated with its kind, in its own delimited section" |
| The no-conclusion rule's placement could limit it to one part | MINOR | adopted: "In any part" |
| The capability escape hatch is too broad | MINOR | adopted: "Only where the environment has no file-read or comparison capability" |
| "Do not include" and the no-render paragraph merge in Markdown | MINOR | adopted: blank line |
| Builder-facing cross-references in the block may confuse the reviewer | MINOR | adopted: the reviewer task says they point to the source protocol and that the reviewer records nothing |
| "(by id, not restated)" vs the literal-excerpt allowance | MINOR | adopted: "(a literal excerpt is not a restatement)" |
| Step 1 quotes axis 4's qualifier, which could go stale if axis 4 changes | MINOR | accepted residual: an example, not a definition; a mismatch is detectable by search |
| A rebuild that keeps failing has no stated end | MINOR | residual: "never sent" holds; not observed |
| Alternative: let the reviewer read the protocol file directly | suggestion | not adopted: it drops the self-contained brief and exposes the builder-facing Level 2 instructions to the reviewer, which is a larger architectural change than this milestone allows. Recorded as an option if F-1 recurs |

No disagreement left unreconciled.

## 6. Limitations

- **No mechanical guarantee.** The builder still assembles the brief itself. The text now requires extraction at write time and a mechanical diff, and removes the reasons observed for editing, but compliance with those steps is itself behaviour. The honest-limitation clause covers only missing capability, not a skipped check.
- **The micro-test is not the failure condition.** n=1 per condition. The old text also passed when brief-building was the only task, so F-1's recurrence in a full build is untested.
- **Unobservable reasons.** The builder's reasoning in the original run was redacted, so causes 2–4 (§1) are inferences.
- **The installed copy is now stale.** `C:\Users\<user>\.claude\skills\design-excellence\references\critique-protocol.md` still holds the `e63d7b3` text, by scope. Real runs use the old step 1 until a refresh is authorized.

## 7. Agents

One read-only reviewer. The three micro-test subject sessions were headless `claude -p` runs without the Agent tool and wrote only to their evidence folders and user temp. No parallel writes to governed files. **Deviation:** if the subject sessions count as operational agents, this milestone used 4 (1 reviewer + 3 subjects) against a cap of 3. R3 was added after reconciliation so that the committed text itself was exercised.
