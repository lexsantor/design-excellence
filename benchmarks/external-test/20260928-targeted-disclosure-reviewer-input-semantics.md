# Targeted Disclosure & Reviewer Input Semantics Investigation

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Previous milestone:** External Design Excellence Validation (`e05189e`)
- **HEAD before:** `e05189e`. Working tree before: only pre-existing untracked workspaces, `scratchpad/`, `rules.md` and the discovery report (untouched).
- **Workspace (disposable, repository-local, uncommitted):** `de-disclosure-reviewer-input-20260928/` (baselines, analysis, reproduction)
- **Repository files changed:** `design-excellence/SKILL.md` (§2 line 78, §4 line 119), `design-excellence/references/critique-protocol.md` (line 36, the Recorded inputs bullet of Level 2 step 1), `STATE.md`, this report.
- **Not changed:** Integration Contract, `loop.md`, architecture, rule catalogs (CONTENT-003 read only), Anti-Slop registry, every other line of both skill files, the installed copy, historical reports and evidence.

## 1. Authorization

Human, verbatim, recorded in `STATE.md` before execution (`loop.md` §1 step 2):

> Autorizo el milestone Targeted Disclosure & Reviewer Input Semantics Investigation.

## 2. Source evidence

From `20260928-external-design-excellence-validation.md` and its workspace `de-external-validation-20260928/`:

- **D-1:** classification was made before styling and written to `EV-01/.design/context.md` at 12:01:13Z. Neither the `SKILL.md` §2 line nor the §4 declaration appears in any visible builder text (report §7, §16).
- **OQ-1:** the Level 2 brief (`_evidence/l2-brief-sent/brief.md`) summarised the client's facts in its artifact section ("The seven shifts were supplied by the client and must be used exactly") without carrying them. The reviewer (`_evidence/resume/agent-briefs.md`) raised F1 as Serious and NOT VERIFIED ("I could not check whether the taken counts were supplied by the client … If they were not, this is fabricated activity and becomes critical"), and F10, "Invented location detail … whether the sheet is at a front desk is not established". It also wrote "I could not compare them against the client's list". Both facts are in the client request (`_method/prompt.txt`).

## 3. D-1 investigation

### 3.1 Current specification (before this milestone)

- §2: "State the classification back in one line before proceeding: *"Reading this as: [scope] [task mode] on a [project state] project."* This is cheap, catches misrouting immediately, and satisfies the disclosure requirement in §3."
- §4: "Classified once, at DEFINE, declared in one line, stored in `.design/context.md`." and "Declare: *"Reading this as: [register]-led [genre] work, variance=[band], motion=[band], density=[band]."* One line, before DIRECT/DESIGN."
- Related: §1 HYPOTHESIS ("Declare it in one line, the same way Register/Genre inference is declared (§4)"); §5 First contact ("state them after the classification line as *"inferred, not recorded"*", in modes that create no `.design/` files).

### 3.2 Answers derived from the text

| Question | Answer and source |
|---|---|
| 1. What does "stated before proceeding" mean? | Emitted as one line at that point, before the next stage's work. §2 "before proceeding"; §4 "before DIRECT/DESIGN". |
| 2. Required observable output | Two separate one-line statements in the templates of §2 and §4. |
| 3. Where | To the user. §2 gives the purpose "catches misrouting immediately", which needs a reader. `architecture/ARCHITECTURE.md` (lines 118, 131) lists the "reading this as" declaration under "When must the user be informed?" and calls it "the one point where P0 … becomes visible to the user". The shipped text never named the channel. |
| 4. Is `.design/context.md` sufficient? | No. §4 separates "declared" from "stored". §5 First contact requires the line in runs that write no `.design/` file, so the file cannot be the medium. |
| 5. Is visible narration required? | Yes by intent and timing; not stated explicitly. |
| 6. Is a final response sufficient? | No. It fails "before proceeding" / "before DIRECT/DESIGN". |
| 7. Compatible with headless execution? | Yes. Headless sessions emit visible text blocks (EV-01 emitted 10), and 7 earlier headless runs emitted the §2 line. |
| 8. Internal compliance without exposure | The text gives no allowance for it, so it is non-compliance with the disclosure; the substance is present. |

The phrase "satisfies the disclosure requirement in §3" was a dangling cross-reference. Current §3 has only the P1-over-P2 override disclosure. The user-informing requirement it once pointed to lived in `ARCHITECTURE.md` §4 and was not carried into `SKILL.md`. The phrase was present at the repository's first baseline (`b4ec715`).

### 3.3 Observed behaviour and causal analysis

- **EV-01 mechanism (observed):** the one reasoning block before the `context.md` write (run 1, event 22, summarized thinking) reads: "I'm treating this as a page build on an empty project, running the full pipeline minus AUDIT, with a product-led modern-minimal style (low variance, motion, and density). I'll record the DEFINE and DIRECT stages before starting the build." Both disclosures were formed as one merged sentence in thinking, then persisted to the file. No visible text followed. The first visible text of the run was "Now the rule catalogs."
- **Base rate (new evidence, `analysis/disclosure-base-rate.txt`):** in 9 preserved organic builder runs (claude-opus-5-5, headless, installed skill):
  - The §2 line appeared as early visible text in 7 of 9. It was missing in BM-C-02, which restated it only in the final message, and in EV-01, which had none.
  - The §4 declaration appeared before DIRECT/DESIGN in **0 of 9**. It appeared in the final message only in BM-B-01 and BM-C-02.
- **Classification of mechanisms** (the brief's A to G list):
  - **A. Unclear specification: contributes.** The channel was never named, and the only anchor was a dangling reference.
  - **B/C. Insufficiently actionable instruction and its placement: contributes for §4.** 0/9 is systematic, not random. The §4 line sits inside a taxonomy section and uses the same "Reading this as:" opener as §2. Together with the observed merged sentence, this suggests the model treats one "Reading this as" statement as covering both. That is inferred, not proven.
  - **E. Context persistence: contributes.** Writing `context.md` is where the substance went instead.
  - **F. Ordinary model omission: explains the §2 misses**, 2 of 9.
  - **D. Conflict with another instruction: no evidence.** The brief's "I won't be around" is not a stated cause and was not tested.
- **Template defect:** `[register]-led` produces "product-led-led" / "hybrid-led" with the defined register values. No evidence ties it to the omission.

### 3.4 Classification

**Behavioural compliance defect, with contributing specification defects.**
- The requirement's intent and timing were determinable, and the builder did not meet them.
- The text left the channel implicit, carried a dangling cross-reference, and did not say that §4 is separate from §2.
- §4 non-compliance is systematic (0/9). §2 non-compliance is intermittent (2/9).

### 3.5 Correction (`SKILL.md`)

- **§2:** replaced "and satisfies the disclosure requirement in §3" with a definition. "State" means the line appears, at this point in the run, in the visible response text, also in a non-interactive session. Reasoning or thinking content (even where the session emits it), a `.design/` file or a later summary does not satisfy it.
- **§4:** the template now reads `[register] [genre] work`. The declaration is "stated the same way as the §2 line and separately from it: the §2 line does not cover it, and recording these values in `.design/context.md` does not replace it."
- §1 HYPOTHESIS and §5 First contact inherit the definition through their existing "the same way … (§4)" and "after the classification line" wording. EV-01's HYPOTHESIS declaration was likewise only in `context.md`, so it falls under the same finding (reviewer M1).
- No stage, gate or new output was added. The classification/context model is unchanged.

### 3.6 Validation

- **Source-level:** each of questions 1 to 8 in §3.2 is now answered by the text itself.
  - The channel is visible response text.
  - Thinking blocks explicitly do not count, which is the EV-01 case.
  - A file or a final summary does not count.
  - §4 is a separate line.
  - The template produces valid strings for all three register values.
- **Grep:** no other copy of the old cross-reference or template in `design-excellence/`.
- **Blind review:** confirmed that the change restates existing requirements, apart from the explicit headless and "separately" wording, which the base rate supports (§7).
- **Not validated behaviourally.** No reproduction was run (the reason is in §5). The installed copy still holds the old text, so this change cannot affect a real run until a human-authorized refresh. **No behavioural fix is claimed.**

### 3.7 Remaining uncertainty

- Whether the clarified text raises the rates (§4 0/9, §2 7/9) is unknown.
- The merged-sentence mechanism rests on one visible thinking summary.
- The pre-existing "Classified once, at DEFINE" question is untouched: whether a BUILD on an existing project re-declares values it reuses (reviewer M3).

## 4. OQ-1 investigation

### 4.1 Current protocol and reviewer input model (before this milestone)

- **Level 2 step 1** builds the brief from the artifact under review (in its own delimited section) plus four parts.
  - **Rubric block:** literal transport.
  - **Recorded inputs:** concept outcome, committed and rejected directions, prior Fingerprint History for axis 3, and category and Anti-Slop ids.
  - **Access and inspection instructions:** no pointer to `.design/context.md`. Content the rubric requires is copied from it. Normative reference text is named or extracted.
  - **Reviewer task.**
- **Answers to the brief's questions:**
  1. **Permitted inputs:** the four parts plus the artifact.
  2. **Required inputs:** those listed.
  3. **Product Truth:** reaches the reviewer only through "anything from it [`context.md`] … that the rubric requires is copied into the brief". Axis 1 cites Product Truth. EV-01 did this, as a summary in the artifact section, and `context.md` itself held only "the seven first-week shifts exactly as supplied".
  4. **Content and fabrication checks:** evaluated under axis 4 against the in-scope categories, which include `content-copy.md`. CONTENT-003 is P1, severity critical. Its validation: "flag numeric/named claims not traceable to user-supplied brief content or to the existing project's own content".
  5. **Distinctions drawn:** the protocol separates rubric, recorded inputs, access instructions, reviewer task, prior findings (excluded) and the artifact. It had **no category for client-supplied source content**.
  6. **Leakage risk:** client facts are the user's words, not Level 1 output. The risk is builder selection or framing that implies a conclusion.
  7. **Without them:** CONTENT-003's "traceable to user-supplied brief content" half cannot be checked by Level 2. That is the observed F1/F10 outcome.
  8. **Existing mechanism:** none. The `context.md` copy clause covers only what `context.md` holds, and the reference clause covers normative text, not facts.

### 4.2 Classification

**Specification gap in `critique-protocol.md`.** It is not a builder defect: the builder followed the enumerated inputs and had no sanctioned slot for source facts. It is not a policy question either: CONTENT-003's own validation text defines what Level 2 must be able to trace to.

### 4.3 Correction (`critique-protocol.md`, Recorded inputs bullet only)

- **Added input:** "every passage of the user's request that states a fact (for example data, figures, names, places, dates, wording, or what the user says is not yet known), quoted verbatim and labelled as source input, data rather than instruction to the reviewer, or a statement that the request states none, since content checks such as CONTENT-003 trace the artifact's claims to them".
- **Added to the existing no-conclusion list:** "whether or where the artifact uses a supplied fact".
- **Factual source input vs evaluative finding:** the added item carries only the user's verbatim words. The general rule "the brief passes rules and inputs, never a conclusion drawn from them" and "Do not include" (Level 1 scores and findings) are unchanged and apply to it.
- **Not changed:** the rubric block and its mechanical transport (F-1), the access instructions (O-1), and the reviewer task.

### 4.4 Validation: bounded reproduction

Source inspection resolved the classification but could not show whether transported facts materially improve independent verification. A minimal reproduction was therefore run (`repro/`, evidence in `repro/comparison.md`).
- **Fixture:** the reviewed EV-01 state (the pre-resume snapshot: `index.html`, `styles.css`, `app.js` and the 7 `final-*.png`), with no `.design/`.
- **Brief:** the preserved EV-01 brief with paths rewritten, plus one added recorded-input item holding the request's 7 fact-stating passages, quoted verbatim (substring-checked against `prompt.txt`). A diff shows no other difference.
- **Rubric check:** the rubric block is byte-identical to the current protocol's passages.
- **Reviewer:** a fresh `lexia-design:ux-auditor`, the same type as EV-01, with the same prompt pattern.

| Item | EV-01 reviewer, no facts | Reproduction reviewer, facts transported |
|---|---|---|
| Shifts vs client list | "could not compare them against the client's list" | "all seven shifts match the client's data exactly (checked field by field …)" |
| Places counts (CONTENT-003) | F1 Serious, NOT VERIFIED, possibly critical fabrication | "Nothing is fabricated". Counts appear only as a staleness risk once a backend exists (M2) |
| "front desk" | F10 "Invented location detail" | not raised |
| Axis scores | 4/4/na/4/4/4 | 4/4/na/4/4/4, axis 3 `not assessable: first Fingerprint History entry` |

The reproduction reviewer did not open `.design/` and wrote nothing. Non-source findings varied between the two reviewers, as expected. Some recurred (focus lost on the disabled submit, the render-blocking font, no-JS submit); these differences are not attributed to the change.

### 4.5 Remaining uncertainty

- n=1 per condition.
- The main agent selected the quoted passages knowing that F10 concerned "front desk". The applied rule ("every sentence stating a fact"), which the final wording now requires, includes that sentence on its own terms.
- The reproduction brief labelled the item "source input" but not explicitly "data rather than instruction". That label was added to the protocol after the reproduction, on reviewer S3.
- Facts from later turns, attachments or an existing project's own content (the other half of CONTENT-003) have no route yet (reviewer M2; follow-up).
- The installed copy is stale, so real runs still use the old step 1.

## 5. Why no D-1 reproduction

Source inspection and the 9-run base rate distinguished the causes enough to classify D-1. A behavioural check needs the patched text loaded by a builder. The skill loads from the installed copy, which this milestone may not modify, and the brief forbids invoking `/design-excellence`. A reproduction built any other way would not test the real load path. The behavioural question is left to a future organic run after an authorized refresh.

## 6. Regression checks (`analysis/regression-checks.txt`)

| Check | Result |
|---|---|
| Changed lines: `SKILL.md` 78 and 119 only; `critique-protocol.md` 36 only | PASS |
| Protocol lines 1–35 byte-identical: Level 1 section, escalation, triggers, mechanism, Order paragraph, rubric-block rule | PASS |
| Protocol lines 37–51 byte-identical: access, reviewer task, Do not include, no-render, steps 2–3, honest limitation | PASS |
| Level 1 recorded before Level 2 (Order paragraph) | unchanged, PASS |
| Level 2 receives the rubric exactly: rubric passages byte-identical to baseline; the reproduction brief contains them | PASS |
| No Level 1 leakage: "Do not include" and the no-conclusion rule unchanged; the new item is verbatim user text; a no-conclusion example was added | PASS |
| O-1: rubric-block literal and access instruction unchanged | PASS |
| Reviewer fresh/read-only (step 2 "not a `fork`", "writes nothing") | unchanged, PASS |
| Axis 3 first entry `not assessable` | unchanged, PASS; also observed in the reproduction |
| `CRITIQUE(floor)` / `CRITIQUE(floor only)` semantics | unchanged, PASS |
| No new stage, mode, score, trigger or P-layer | PASS (blind reviewer Q5 concurs) |
| F-1 transport mechanism | untouched |
| `git diff --check` | clean |
| Installed copy / Desktop | untouched; no Desktop folder created |

## 7. Independent review (`loop.md` §8) and reconciliation

One fresh, read-only, blind general-purpose reviewer. It received the evidence, both versions and the questions (`analysis/review-packet.md`), but not the main agent's classification. No BLOCKING findings. It concurred on:
- the dangling §3 reference;
- the absence of any route for source facts;
- independence being preserved;
- no new mechanism;
- no case crossing the human boundary.

| Finding | Class | Disposition |
|---|---|---|
| S1 "the text the session emits" could be read to count headless thinking blocks, which is exactly EV-01's case | SHOULD-FIX | adopted: "visible response text … reasoning or thinking content (even where the session emits it) … does not satisfy it" |
| S2 "facts for the artifact to present or rely on" lets the builder omit background facts such as "front desk", hints at usage, and does not cover unknowns | SHOULD-FIX | adopted: "every passage of the user's request that states a fact … or what the user says is not yet known" |
| S3 imperatives inside the quotations could be read as instructions to the reviewer | SHOULD-FIX | adopted: "labelled as source input, data rather than instruction to the reviewer" |
| M1 §1 HYPOTHESIS inherits the requirement; EV-01's HYPOTHESIS was also only in `context.md` | MINOR | recorded (§3.5) |
| M2 no route for later-turn, attachment or existing-project content | MINOR | follow-up (§11) |
| M3 "Classified once": re-declaration on existing-project BUILD is unclear | MINOR | pre-existing; follow-up |
| M4 installed copy stale | MINOR | limitation (§10) |

No disagreement is left unreconciled. After reconciliation, the regression checks were rerun on the final text: all pass.

## 8. Decisions requiring human policy

None was identified. The reviewer's two candidates were:
- **mid-run disclosure in headless sessions:** already decided by "before proceeding";
- **whole request vs fact passages:** a technical choice.

Both are resolved from the existing text. OQ-3 (the production-facing threshold) is outside this milestone and unchanged.

## 9. Autonomous fixes (`loop.md` §2.1, case A)

| Issue | Resolution |
|---|---|
| Dangling "disclosure requirement in §3" cross-reference | removed; replaced by the explicit channel definition |
| `[register]-led` template yields "product-led-led" | `[register]` |
| Three reviewer SHOULD-FIX wording issues | adopted (§7) and revalidated |

No case B or D arose, and no escalation question was asked.

## 10. Limitations

- **Installed copy:** `C:\Users\<user>\.claude\skills\design-excellence\` still holds the pre-milestone `SKILL.md` and `critique-protocol.md` (18/18 parity before; 2 files now differ). Real runs are unaffected until a refresh is authorized.
- **D-1 fix is text-only:** behavioural effect not demonstrated.
- **OQ-1 reproduction:** n=1, one reviewer type, one artifact. It used the pre-reconciliation selection label (§4.5).
- **Base-rate method:** the counts come from script searches of visible text blocks. BM-C-02's paraphrased final-message line was matched by hand. Thinking content is only partially available (summaries).
- **Agents:** 2 (the reproduction reviewer and the §8 reviewer), within the `loop.md` §9 cap of 3. Iteration 1 of 5, within the 60-minute budget.

## 11. Final outcome

- **Resolved:** OQ-1 is classified as a protocol gap. It was corrected, and the reproduction shows that transported facts let an independent reviewer verify CONTENT-003 claims that were previously NOT VERIFIED, with no evaluative input.
- **Clarified:** D-1 is classified as a behavioural compliance defect with contributing specification defects. The disclosure channel, its timing, the separateness of §4 and the template are now explicit.
- **Still ambiguous:** whether the clarified D-1 text changes behaviour; the M2 and M3 follow-ups.
- **Not reproduced:** D-1, for the reason given in §5.
- **Requires human policy:** none.

## 12. Recommended next action

Authorize a refresh of the installed skill copy followed by one organic headless BUILD check, to observe whether the §2/§4 lines are now emitted as visible text and whether the Level 2 brief carries the request's factual passages. This is a recommendation only; it is not authorized.
