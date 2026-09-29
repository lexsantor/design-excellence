# External Design Excellence Validation

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Previous milestone:** Align Workspace Governance (`61da475`)
- **Workspace (disposable, repository-local, uncommitted):** `de-external-validation-20260928/` (`REPORT.md` there indexes every evidence file)
- **Repository files changed:** this report and `STATE.md`. No skill source, installed copy, `loop.md` or other governed file changed.

## 1. Authorization

Human, verbatim, recorded in `STATE.md` before execution (`loop.md` §1 step 2):

> Autorizo el milestone External Design Excellence Validation.

## 2. Objective

Obtain behavioural evidence about the current Design Excellence system on one fresh, realistic, unprimed external task, after the recent governance, critique, workspace and issue-resolution changes.

## 3. Hypothesis

On an unprimed, realistic greenfield page-scope BUILD, the current skill routes, directs, builds, validates and critiques according to its current specification, and any deviation is observable and recordable from preserved evidence.

## 4. Test project and setup

- **Project:** fictional "Eastgate Community Pantry" volunteer shift sign-up page. A single static page (HTML, CSS, minimal JS). The brief supplies all seven shifts and their capacities (one is full). It asks for filters by day and kind of work, a sign-up form with name, email and phone, and an honest no-backend submission that must never claim a save. The audience is older volunteers, often on a phone. Unknown facts are to be left as placeholders. It also says "We plan to give the link to our regular volunteers next month."
- **Why this project:** every earlier organic run was a brand-led studio or marketing landing page. This is a small product tool, with data display, filtering, capacity states, a form, failure paths and touch use.
- **Priming control:** the prompt contains no word about critique, review, level, axis, rubric, score, assessable, transport, verbatim, independence, benchmark, test, premium or flagship (scan recorded at setup). It says nothing about F-1, earlier tests or expected findings. The weekday/date pairs were checked against the 2026 calendar before the method was frozen.
- **Builder:** one fresh headless `claude -p` session with `claude-opus-5-5`, using the same invocation as earlier organic runs (`_method/METHOD.md`, frozen before the run). The `/design-excellence` prefix loads the installed skill. The main agent did not steer the builder.
- **Baselines:** HEAD `61da475`. Installed copy 18/18 SHA-256 identical to `design-excellence/`. Write guard active (a write probe was denied). A Desktop listing was captured before the run.

## 5. Workspace location

`C:\Users\<user>\Desktop\design-excellence\de-external-validation-20260928\`, inside the repository and separate from governed files. The installed skill stayed at `C:\Users\<user>\.claude\skills\design-excellence\`. See §12 for the governance checks.

## 6. Execution summary

| Segment | Time (UTC) | Result |
|---|---|---|
| Run 1 | 11:58:24 to 12:12:44 | 71 turns. Ended by an account API session limit (HTTP 429, `terminal_reason: api_error`) while the Level 2 reviewer was running. The reviewer was also cut off and returned only partial output ("Need full index.html.") |
| Interruption | 12:12 to 13:10 | No work possible, because the account limit applied to all sessions |
| Resume | 13:10:11 to 13:19:00 | Same session, `--resume` with the neutral prompt "Please continue." (`loop.md` §2.1 case E). 32 turns, exit 0 |
| Main-agent validation | 13:20 to 13:30 | Independent Playwright checks (§10) |

The resume prompt is the only input the main agent gave the builder after the initial brief. It carries no design or critique content.

## 7. Pipeline behaviour

- **Classification before styling: held.** `.design/context.md` was written at 12:01:13Z with register/genre/dials, Product Truth and routing rationale, before any page file (`index.html` first written at 12:03:01Z).
- **One-line disclosure: not emitted (D-1).** Neither the `SKILL.md` §2 line ("Reading this as: [scope] [task mode] on a [project state] project.") nor the §4 declaration line appears in any visible builder text in either segment. The transcript search only matches the skill file's own text. Classification exists only inside `context.md`.
- **INSPECT:** the builder listed its folder (empty) and the parent folder names first. It never opened `_method/` or `_evidence/` (tool-call scan).
- **Routing:** page-scope BUILD, genuinely-empty, unbounded profile (the brief asks for implementation). All runtime evidence is consistent with this: DEFINE, DIRECT, then design tokens, BUILD, VALIDATE, CRITIQUE, REFINE and SHIP all ran. There was no AUDIT stage, as specified for greenfield BUILD.
- **DEFINE:** product-led register; modern-minimal genre, justified from the brief's language ("easy to use", older users, phone) and cross-checked against STYLE-MODERN-MINIMAL-01 `best_for`/`do_not_use_for`. Dials variance 3, motion 2, density 3. Stakes recorded as production-facing.
- **Concept:** HYPOTHESIS (the page read as the paper sheet's successor). It was declared as not evidenced, informed only the places gauge, and was explicitly recorded as not activating LAYOUT-009. This is consistent with the §1 three-state model.
- **Loads:** `SKILL.md` §7 T2 and T3 files for a new visual system: all seven rule categories, `critique-protocol.md`, `anti-slop-registry.md`, `style-catalog.md`, `visual-references.md` and `principle-pool.md` together. `existing-project-safety.md` was not loaded, which is correct for genuinely-empty. No T4 file was loaded (§12).
- **Preservation of existing systems:** not exercised (greenfield).
- **HARDEN:** there is no stage-labelled HARDEN pass in the narration. The builder did test failure paths (unreachable, HTTP 409, HTTP 500, mocked 200), double submit and 200% text. Whether this constitutes the HARDEN stage is not assessable from labels (§18).

## 8. Direction / distinctiveness behaviour

- **DIRECT:** two candidates. Committed: "The week's roster" (one overview list grouped by day, filters in place, form disclosed under the row). Rejected: "One question at a time" (a step flow). The rejection names 2 distinguishing dimensions (composition, interaction) and a brief-traceable reason ("see the upcoming shifts"), cross-checked against the style catalog. It does not rest on a genre stereotype.
- **Visual references (LAYOUT-010):** REF-008 informed the rejected candidate and, in lighter form, the committed one. REF-007 was judged unnecessary, with the reason stated (it would add an A11Y-011 risk). REF-009 was not applied because its `do_not_apply_to` matched. A reference was not treated as a quota.
- **Carriers (main-agent check on the render):** composition is carried, since all seven shifts are visible in one grouped list at every width (`full-*.png`). Interaction is carried, since the form opens in place under the chosen row (`form-errors-390.png`). Both are observable, and neither is decoration.
- **Fingerprint:** first entry. All five dimensions were recorded. Level 1 and Level 2 both recorded axis 3 as `not assessable: first Fingerprint History entry`, as `critique-protocol.md` axis 3 specifies.
- **Concept → Structure:** not activated, correctly (HYPOTHESIS only).

## 9. Critique behaviour

- **Level 1:** six axes recorded in Fingerprint History at 12:09:29.746Z, marked "recorded before any Level 2 dispatch": Genericness 4 (including the SLOP-011 gestalt check and a check of the committed-direction carriers), Hierarchy 4, Distinctiveness not assessable (first entry), Craft 4, Accessibility 4 (every always-on entry by id; A11Y-012 n/a, no overlay), Technical 5.
- **Trigger:** "production-facing (the page will be shared with real volunteers next month)". This is the first `critique-protocol.md` trigger condition, taken from a real-use statement in the brief, not a word like "premium".
- **Transport:** at 12:09:53Z (#66) a script read the installed `critique-protocol.md`, sliced the two passages, independently re-extracted them and printed `IDENTICAL`. Assembly (#67) printed "rubric present verbatim in brief: True". The main agent's independent `verify_block.py` against the installed file found the not-assessable rule and all six axes exact (`ALL EXACT`). O-1 held: the literal `.design/context.md` stays in axis 1, and a separate instruction forbids opening `.design/`.
- **Leakage:** no Level 1 score, finding or outcome appears outside the rubric block (`analysis/leakage-scan.txt`). The only near hit, "REF-008's principle carried in lighter form", is DIRECT's own logged line, which the protocol allows as a recorded input. The brief states "Prior Fingerprint History entries … none" as an input and leaves the axis 3 outcome to the reviewer. Categories and Anti-Slop entries were passed by id.
- **Order:** Level 1 was on disk 70 s before dispatch 1 (12:10:39Z). The file changed append-only across both segments (the pre-resume vs final diff adds lines only), so the pre-dispatch Level 1 was never revised.
- **Dispatch:** fresh `lexia-design:ux-auditor` (a preferred specialised critic, not a fork). Dispatch 1 was cut off by the 429. After the resume, the builder re-dispatched a fresh reviewer with the same brief file (byte-identical to the preserved copy) and added one operational sentence to the prompt. Neither reviewer transcript shows access to `.design/` or any Write/Edit.
- **Level 2 result:** Genericness 4, Hierarchy 4, Distinctiveness not assessable (first entry), Craft 4, Accessibility 4, Technical 4. There were 12 findings with file:line, several marked "NOT VERIFIED" where a browser was needed.
- **Synthesis:** appended and labelled "synthesis outcomes, not revisions of the L1 result". The disagreement (Technical 5 vs 4) was surfaced to the user in the final message ("The independent reviewer gave it 4 and was right"). 8 findings were adopted and fixed. Two were rejected with evidence from the source brief, and two were noted without change (Google Fonts render-blocking and privacy, which the brief allowed; the raw endpoint response without JS).
- **Evidence honesty:** the reviewer did not assert fabrication. It marked F1 ("taken counts") and F10 ("front desk") as unverifiable from its inputs. The builder rejected both because the client brief states them. See OQ-1.
- **What Level 2 caught that Level 1 and the builder's VALIDATE missed:** focus dropped during sending; a server rejection reported as unreachable; stale errors in a reopened form; a filter hiding the open form; no spacing between fields; chips not wrapping at large text sizes.

## 10. Accessibility / quality behaviour (main-agent validation, final state)

| Check | Result |
|---|---|
| Horizontal overflow at 320/375/768/1024/1440 | 0 px at all widths |
| Shift data vs brief | all 7 exact (4/6, full, 2/3, 1/6, 3/4, 2/2, 2/5 open); the full shift has no Sign up control, and "Full. No places left." is stated in text |
| Keyboard walk | skip link, both radio groups (one stop each), then 6 Sign up controls in order; every stop has a 3px solid outline |
| Form | focus moves to the first field on open; an empty submit gives 3 linked text errors, with focus on the first invalid field |
| Honest submission | against the placeholder `.invalid` endpoint: "Your sign-up was not saved…", input kept, no "signed up" text anywhere |
| Contrast (A11Y-001) | minimum rendered text pair 7.10:1 |
| Reduced motion (A11Y-003) | 0 running animations; only colour/background/border transitions |
| No-JS (A11Y-009) | 7/7 shifts visible; the sign-up form is visible, with a shift select, posting to the placeholder; filters (an enhancement) hidden |
| A11Y-008 | `width=device-width, initial-scale=1`; inputs 18px |
| A11Y-012 | not applicable (inline disclosure, no overlay), as both levels recorded |
| Console | only the expected failed request to the placeholder endpoint |
| Placeholders | 5 visible "To be confirmed" fields; no invented contact, address, hours or names |

The builder's own VALIDATE matched these results (320/390/640/1280, no-JS, 200% text, contrast pairs, keyboard walk). Screen-reader testing was not done, by either the builder or the main agent.

## 11. Anti-slop behaviour

No hero, stock imagery, gradients, icon set, card grid or persuasion block. The only graphic is the places gauge, which is driven by the data and hidden from assistive technology (the same information is in text). The accent colour was derived from the brief's pen-on-paper sheet (SLOP-013). The single typeface, Atkinson Hyperlegible Next, was chosen for low-vision readers and the reflex UI sans set was explicitly rejected. The SLOP-011 gestalt check was recorded with no cluster match. The page repeats one row structure, which is dictated by its content. No content-relevance trigger arose (the brief does not raise genericness).

## 12. T4 behaviour

Not activated. No new iconography, motion-library need or component library was established, so `reicon.md`, `kinetics.md` and `smoothui.md` were neither loaded nor used, and no package was installed. This is consistent with the §7 T4 triggers. Source/fallback handling was not exercised.

## 13. Autonomous issue resolution events (`loop.md` §2.1)

| Issue | Class | Resolution | Validation |
|---|---|---|---|
| Run 1 ended by the API session limit (HTTP 429) | technical, case E | resumed the same session with "Please continue." instead of a fresh rerun, so there was no reroll of the design | resume exit 0; the flow completed |
| The sent Level 2 brief lived only in the builder's temp folder | evidence | copied to `_evidence/l2-brief-sent/` before the resume | `cmp` identical to the file dispatch 2 read |
| My interim `STATE.md` blocker said the reviewer "had returned"; it had not | own error | corrected in `STATE.md`; recorded here | transcript shows partial output only |
| The main agent's Playwright tool wrote `.playwright-mcp/` in the repository root (git-ignored) | workspace hygiene | moved into `_evidence/main-agent-validation/` | root folder removed |
| An auto-mode classifier failed transiently on two Bash calls | tool, case E | read files directly, then retried | succeeded |

No case B or D arose. No escalation question was asked.

## 14. Independent review

No `loop.md` §8 reviewer was required. This milestone's output is behavioural evidence about one design run, not a verdict on architecture, governance, source-family viability, reference admission, integration or strategic direction, and no such verdict is made here. Design critique followed the Design Excellence protocol inside the run (§9). Agents: the main agent spawned none. The run involved the builder session plus two reviewer dispatches, the first of which was aborted by the 429. That makes 3 including the builder, within the `loop.md` §9 cap.

## 15. Evidence index

`de-external-validation-20260928/REPORT.md` lists every artifact. Key items: `_method/METHOD.md`, `_method/prompt.txt`, `_evidence/stream*.jsonl`, `_evidence/session-transcript/`, `_evidence/l2-brief-sent/brief.md`, `_evidence/analysis/{expected-block.md,leakage-scan.txt,timeline.txt,toolcalls.txt}`, `_evidence/resume/agent-briefs.md` (full reviewer report), `_evidence/main-agent-validation/`, `EV-01/.design/context.md`.

## 16. Defects

- **D-1: classification disclosure not stated.** `SKILL.md` §2 requires the one-line classification to be stated before proceeding, and §4 requires the one-line Register/Genre/Dials declaration before DIRECT/DESIGN. Neither appears in the builder's visible output. The substance was classified and recorded before styling, so the deviation is in disclosure only. This is n=1, in a headless session whose only reader is the final message. Visible text blocks were searched; any thinking content could not be inspected.

No other deviation from the current specification was found.

## 17. Corrections

- **Builder REFINE (inside the run):** 8 adopted Level 2 findings fixed, plus two overflow issues found during re-verification (h1 and skip link at 320px and 200% text). The pre-fix state is preserved in `_evidence/pre-resume-EV-01/`; the post-fix state is in `EV-01/`. The main-agent validation (§10) was run on the post-fix state only.
- **Main agent:** the §13 items only. No project or governed file was changed to improve a result.

## 18. Limitations

- **n=1**, one model, one browser engine (Chromium), in the harness environment and global settings of earlier runs.
- **Interrupted run.** The resume continued the same session. Its context shows the builder lost its local server and reviewer, but the design decisions and Level 1 were all made before the interruption. The re-dispatch reused a brief written about an hour earlier (OQ-2).
- **Wall-clock budget.** Active work was about 45 minutes; including the hour when the account limit blocked all sessions, elapsed time was about 95 minutes. I count the blocked hour as an interruption (`loop.md` §6), not as budget consumed. A stricter reading would call this over the 60-minute default.
- **Not measured:** Core Web Vitals / Lighthouse, screen readers, real touch devices, Firefox and Safari. PERF-001 (render-blocking web font) was flagged by Level 2 and left unchanged, because the brief allowed public font services.
- **HARDEN** could not be identified as a labelled stage (§7).
- **Reviewer isolation from `.design/`** rests on instruction; it was complied with, not enforced.
- **Builder side effect:** the brief's temp folder remains outside the repository at `AppData\Local\Temp\tmp.1wLMly9dPq` (copied into the workspace).

## 19. Open questions

- **OQ-1: Level 2 brief and client-supplied facts.** The brief summarised the Product Truth ("the seven shifts were supplied by the client") but did not carry the client's shift list or wording. The reviewer therefore could not verify CONTENT-003 for the capacities or the "front desk" sheet and raised two unverifiable concerns, which the builder rejected. `critique-protocol.md` does not state whether source facts needed to check fabrication belong in the brief. This needs future investigation, not a change here.
- **OQ-2: re-dispatch after an aborted reviewer.** The protocol ties extraction to "the same step that writes the brief" but is silent on reusing an already verified brief for a re-dispatch. Here the content stayed byte-exact against the unchanged installed file.
- **OQ-3: production-facing threshold.** "Give the link to our regular volunteers next month" was read as production-facing, which is consistent with the trigger text. Whether a small internal-audience tool should reach Level 2 is the threshold question previously listed, and it remains a human policy question.

## 20. Final milestone outcome

**COMPLETED.** The hypothesis is accepted with one recorded deviation (D-1). On this unprimed product-led page BUILD, the following behaved per current specification:
- routing;
- classification before styling;
- DEFINE with the three-state concept model;
- DIRECT with evidence-traceable rejection;
- visual-reference judgement;
- carrier-bearing output;
- first-entry fingerprint handling;
- Level 1 before Level 2;
- exact mechanical rubric transport, with no leakage;
- reviewer independence;
- labelled synthesis;
- honest no-backend behaviour;
- absence of fabrication;
- the always-on accessibility floor;
- correct non-activation of T4.

The one-line classification and declaration disclosures were not stated. Previously closed behaviours showed no regression: F-1 transport, the Level 1/Level 2 order, O-1, and A11Y-012 applicability.

**Autonomous fixes:** see §13. **Regressions:** none observed.

## 21. Recommended next action

Human decision on whether D-1 warrants a targeted look at how the §2/§4 disclosure lines survive in long or headless sessions, and whether OQ-1 should be investigated. This is a recommendation only; no milestone is authorized.
