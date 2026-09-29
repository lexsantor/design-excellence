# Controlled Direction Carry-Through & Distinctiveness Revalidation Benchmark

- **Date:** 2026-09-28
- **Status:** COMPLETED (behavioural evidence only; no Design Excellence file changed)
- **Previous benchmark:** `benchmarks/external-test/20260928-direction-carry-through-distinctiveness-benchmark.md` ("BM")
- **Clarification under test:** `557fc49` (`critique-protocol.md`: B1 first-generation axis 3, B2 Level 2 brief contents, C1 committed-direction carriers)

---

## 1. Objective and authorization

- **Authorization (human, verbatim, recorded in `STATE.md`):** "adelante siguiente paso", given for this milestone brief.
- **Objective:** determine whether B1, B2 and C1 change behaviour when the previous benchmark's confounds K1 (priming), K2 (engineered DETECTED) and K3 (benchmark awareness) are removed.
- **Boundary:** behavioural evidence only. The source skill, installed copy, `<external-test-a-project>`, the previous benchmark workspace and all architecture were left unchanged. Three runs are controlled behavioural evidence, not proof of general reliability.

## 2. Runtime skill and source hashes

- **Repository at start:** `365b7a8` (contains `557fc49`). The working tree held only the known untracked items.
- **Installed copy:** `C:\Users\<user>\.claude\skills\design-excellence`, 18 files, SHA-256 identical to the repository skill tree before and after the runs (§13). The installed `critique-protocol.md` contains the B1, B2 and C1 wording. The write guard was active at start (write probe DENIED) and was not touched.
- **Installed `critique-protocol.md`:** SHA-256 `525f9b33b9a05302723668a7931ff1cc2964054b7247557200cd5d0979efe970`.

## 3. Benchmark setup

| Item | Value |
|---|---|
| Workspace | `C:\Users\<user>\Desktop\design-excellence-revalidation-20260928` (new; previous workspaces not reused) |
| Method record | `_method/METHOD.md`, frozen before the first builder started |
| Builder | fresh headless session per empty folder: `claude -p "<prompt>" --model claude-opus-5-5 --permission-mode acceptEdits --allowedTools "Bash Write Edit Read Glob Grep Agent Task mcp__playwright" --mcp-config _method/mcp.json --strict-mcp-config --output-format stream-json --verbose`, three in parallel |
| Browser | Playwright MCP (Chromium), `--isolated` per session (same package as all earlier runs) |
| Evidence location | `_evidence/<case>/`, outside every project folder; the builder never saw it |
| Runs | RV-C-01 10:27:56–10:40:58; RV-C-02 10:28:02–10:39:58; RV-B-01 10:28:12–10:44:07. All exited 0. No rerun |

**Exact builder briefs.** The prompts carry over the Product Truth of BM-C-01, BM-C-02 and BM-B-01, under fresh names. Each is followed by the same common paragraph.

- **RV-C-01:** "/design-excellence We're Linden Press, a small contemporary print studio. Our work explores physical paper, ink, registration, layering and imperfect print processes. We need a landing page that introduces the studio and what we explore, and invites people to get in touch about a print project."
- **RV-C-02:** "/design-excellence We're Anvil Boxing, a boxing organization. We need a landing page that introduces us and invites visitors to find out about training. Our brand colors are black and a saturated red; please stick to them."
- **RV-B-01:** "/design-excellence We're Mudroom, a small neighborhood workshop where people learn to make things from clay: wheel throwing, hand building and glazing, in small groups, from first-timers to people returning to practice. We need a landing page that explains what happens at the workshop and who it's for, and invites visitors to ask about joining a session. It should feel welcoming to beginners without talking down to returning makers."
- **Common paragraph:** "Build it as a single static page (plain HTML, CSS and minimal JavaScript, no build step, no package dependencies) that we can host anywhere; web fonts from a public font service are fine. Keep all files inside this folder. / We haven't confirmed details like our address, prices, schedule, contact details, people's names or history yet. Don't make any of that up; leave clearly marked placeholders instead. / I won't be around to answer questions while you work, so please make the design decisions yourself."

## 4. K1 / K2 / K3 controls (and a new K4)

| Confound | Control | Held? |
|---|---|---|
| **K1** priming | No instruction to score, report status, classify axes, use "not assessable", log evidence, or reproduce anything. No RUN-LOG requested. Evidence comes from the raw transcript, builder files and analyst renders | **Yes.** A term scan of all three prompts for benchmark, experiment, fictional, axis, score, status, assessable, detected, evidenced, review and test found no match |
| **K2** engineered DETECTED | The BM-C-01 sentence about "a direction with a material distinction … carried into the rendered interface" was removed; only Product Truth remains | **Yes.** RV-C-01 recorded **HYPOTHESIS** ("Linden" = basswood), where BM-C-01 recorded DETECTED. This confirms BM's reading that the old sentence engineered DETECTED |
| **K3** awareness | Client-voice briefs; no mention of benchmark, internal, fictional, experiment, reviewer or hypotheses | **Yes, as far as observable.** No run referred to a benchmark or test. Every run treated its page as a real client deliverable ("before it goes live", "public-facing page") |
| **K4 (new)** external reference library | The method relied on omitting the Skill tool from `--allowedTools`. **That did not restrict it:** `--allowedTools` pre-approves tools, it does not deny others | **No, for RV-B-01.** RV-B-01 invoked the user-level `taste-examples` skill (a library of production landing pages), triggered by the user's global CLAUDE.md rule "For new frontend visual directions, use the taste-examples skill", and read two of its reference sheets. It disclosed this nowhere, neither in `context.md` nor in its messages. RV-C-01 and RV-C-02 did not invoke it. In BM, the prompt's "no other skills" line suppressed this. Not rerun: B1, B2 and C1 do not depend on where candidate ideas came from, and following a user-level instruction is legitimate P2 behaviour in this environment |

**Consequence of removing the "not production-facing" statement:** all three runs triggered Level 2 on their own, on the production-facing / public-facing stakes signal, and dispatched a fresh `lexia-design:visual-critic`. Level 2 was not forced.

## 5. Per-case results

| Field | RV-C-01 Linden Press | RV-C-02 Anvil Boxing | RV-B-01 Mudroom |
|---|---|---|---|
| Classification | page BUILD, genuinely-empty | same | same |
| Register / Genre / Dials | brand-led, atmospheric-expressive, variance High, motion Medium-low, density Low | brand-led, atmospheric-expressive, 7 / 3 / 4 | brand-led, atmospheric-expressive, 6 / 2 / 3 |
| DEFINE concept | HYPOTHESIS | HYPOTHESIS ("anvil" = shaped by repeated blows) | HYPOTHESIS ("mudroom" = boot room) |
| LAYOUT-009 | not activated | not activated | not activated |
| T3 internal pools | loaded; REF-009 and PRN-0001 adopted | loaded; PRN-0001 and REF-009 adopted | loaded; PRN-0001 adopted; REF-005 screened out |
| External library | none | none | **`taste-examples` (K4), undisclosed** |
| Committed direction | "Two inks, one sheet" | "Fight bill" | "The clay's own path" |
| Rejected candidate | "Job docket" (single ink on white, dense rule-segmented form grid, grotesk + mono, static) | "Corner split" (black-dominant, red as thin rules and one CTA accent, condensed grotesque, photo hero, asymmetric columns) | "Glaze test-tile board" (bento tiles, a glaze colour per tile, mono labels, tile hover/expansion) |
| Logged dimensions | composition, colour, typography, interaction | composition, imagery, typography, colour | composition, colour, typography, interaction |
| Level 1 (as recorded) | 4 / 4 / **not assessable (first Fingerprint History entry)** / 4 / "pass" / "pass" (formed before dispatch per visible thinking, transcript line 452; written after) | 3 / 4 / **not assessable: first Fingerprint History entry** / 4 / 4 / 5 (formed *after* reading Level 2; post-REFINE) | 4 / 4 / **not assessable (first Fingerprint History entry)** / 4 / 4 / 4 (written to `context.md` before the background report arrived) |
| Level 2 | triggered, executed | triggered, executed | triggered, executed (background dispatch) |
| Level 2 axis 3 | not assessable | not assessable: first Fingerprint History entry | not assessable |
| REFINE | yes (4 findings from Level 2) | yes (direction collapse below the fold plus 7 more) | yes (hero overflow at 1280×720, colour reset, equal cobalt bands, and more) |
| Second critique after REFINE | no Level 2; self-check only | Level 1 only (after REFINE and after Level 2); no second Level 2, disclosed | no second Level 2, not disclosed |
| `context.md` written before `index.html` | yes | no (after) | no (after, and after Level 2 dispatch) |
| Fingerprint History after run | 1 entry (baseline) | 1 entry (baseline), **stale after REFINE** (still lists "Archivo variable (condensed widths)", which REFINE removed) | 1 entry (baseline) |
| Final evidence | `_evidence/RV-C-01/RV-C-01-analyst-final-{1440,375}.png` | `_evidence/RV-C-02/...` | `_evidence/RV-B-01/...` |
| Pre-REFINE evidence | 11 images recovered from the transcript (builder deleted its screenshot folder) | 9 recovered images; `04-image.png` is the pre-REFINE full page Level 2 saw | 14 recovered images, plus the builder's own `.playwright-mcp/mud-*.jpg` |

## 6. B1 evidence

- **All six critique records** (three Level 1, three Level 2) recorded axis 3 as not assessable. None scored, passed, estimated or inferred it. Each run wrote exactly one Fingerprint History entry, labelled as baseline or "generation 1".
- **Exact form:** RV-C-02 Level 1 used the exact string `not assessable: first Fingerprint History entry`. RV-C-01 and RV-B-01 used "not assessable (first Fingerprint History entry)", with the same reason in parentheses rather than after a colon. The three Level 2 reviewers wrote "not assessable", one of them with the full reason.
- **Later-comparison semantics:** untouched. No run had prior entries, so nothing was compared. BM already confirmed the §6 text is unchanged; no evidence here bears on later generations.
- **Unprimed:** no prompt mentioned status, scoring or axes (K1).
- **Result:** **RESOLVED** for the behaviour (6 of 6 not assessable, unprimed). Exact string formatting varies in 2 of 3 Level 1 records, which is cosmetic.

## 7. B2 evidence

The exact dispatch prompts are preserved in `_evidence/<case>/level2-brief-prompt.md`.

| Required content | RV-C-01 | RV-C-02 | RV-B-01 |
|---|---|---|---|
| Complete Level 1 definition of every axis | **paraphrased and condensed**; axis 1 carrier clause omits the absence and "never presumed carried" parts; axis 5 without A11Y ids or the conditional A11Y-012 | **paraphrased**; axis 4/5 turned into checklists; axis 1 includes the full carrier clause | **nearly complete in substance**; full carrier clause incl. absence; conditional A11Y check; "Do not substitute a judgement of how distinct it looks"; mild pre-framing (its absence example is the assessed dimension) |
| `not assessable` rule | yes ("never a pass or estimate") | partial ("never estimate") | yes ("never a pass and never replaced by an estimate") |
| DEFINE concept outcome | yes | yes | yes |
| Committed direction, logged dimensions, rejected candidate | yes | yes (details by pointer to `context.md`) | yes |
| Prior Fingerprint History (none) | yes | yes | yes |
| Current run's entry excluded | yes (none passed) | yes ("Ignore its Fingerprint History entry … this run wrote it") | yes |
| Level 1 scores/findings withheld | yes | Level 1 scores yes (`context.md` at dispatch held "Level 1 critique: see entry below"); **but the brief pointed the reviewer at `context.md`, whose Known Exceptions carried the builder's own genericness judgement** ("SLOP-011 cluster 2 … Mitigated by using red as drenched surface") | yes |
| Anything pre-decided | no | **axis 3 outcome dictated** ("must be recorded `not assessable: …`") | **axis 3 outcome dictated** (same) |

- **Result: PARTIALLY RESOLVED.** Every brief carried the recorded inputs B2 requires, and no Level 1 score leaked. RV-C-02 did expose builder judgement recorded in `context.md` by pointing the reviewer at the whole file instead of passing the recorded inputs alone. No reviewer scored axis 3 against a label. But no brief carried the verbatim Level 1 definitions: all three were reconstructed. One omitted C1's absence clause, and two dictated the axis-3 outcome instead of passing the rule. Dictating it is harmless here, since it follows mechanically from "no prior entries". Still, it is a conclusion handed to the reviewer, which the clarified text neither asks for nor forbids.

## 8. C1 carry-through evidence

Classification by the analyst from final renders and source, checked against each Level 2 reviewer's per-dimension report.

| Case | Dimension | Final render | Notes |
|---|---|---|---|
| RV-C-01 | composition | carrier present | Overlapping-ink hero art and a staggered specimen grid. The rule-segmented studio details sheet is a device shared with the rejected "Job docket" (REF-009), isolated to one section; Level 2 flagged it the same way |
| | colour | carrier present | Two inks plus a multiplied third colour on paper; drenched blue enquiry band |
| | typography | carrier present | Clarendon display (Besley) + grotesk; no mono |
| | interaction | carrier present in code, thin; not assessable from a static render | One-shot `register-text`/`register-art` keyframes into register; removed under reduced motion. Level 2: "held, but thin". Its separate finding, that the headline offset read as a drop shadow rather than misregistration, was answered by a real change to the offset |
| RV-C-02 | composition | **pre-REFINE absent → present** | Level 2: "DRIFTED … left-aligned, asymmetric 1.3fr/1fr About section … close to B". Final: centred bill composition throughout (`recovered-screenshots/04` vs `07`, analyst render) |
| | colour | **pre-REFINE absent → partial** | Level 2: "From About to Contact … black with red only as the particulars sheet and a 6px rule … B's device". Final: contact is now a drenched red slab; About and Training remain black with a red sheet |
| | typography | **pre-REFINE partial → present** | Level 2: labels in condensed Archivo = B's "industrial condensed grotesque". Final: buttons and labels in Alfa Slab |
| | imagery | carried by intentional absence | No photography versus B's photo hero; one marked photo slot |
| RV-B-01 | composition | carrier present | Six full-width numbered bands in an ordered list, not tiles |
| | colour | carrier present (repaired) | Level 2: "carried, weakened", since B also used a colour per unit; the distinguishing ramp reset after the path. REFINE fixed the reset. Final: ordered clay-state ramp, then deeper cobalt |
| | typography | carrier present | Wide grotesk display (Anybody) + serif body; no mono |
| | interaction | carried by intentional absence | No tile hover/expansion; paint-only gated hover. Level 2 noted FAQ `<details>` is native disclosure, not tile expansion |

**How carry-through failures were handled:**
- **Exposure:** in 2 of 3 runs a declared dimension was not (RV-C-02) or only weakly (RV-B-01) carried in the first build. **Both were exposed**, in both cases by the Level 2 reviewer, which was briefed with the C1 carrier question.
- **Response:** each was answered by **genuine design revision** in REFINE (recomposition, colour surfaces, label typeface, ramp order). None was answered by decoration. RV-C-02 also appended a dated note to `context.md` recording that the first build carried the direction only in the hero and that the design, not the claim, was revised. That is the appended-note form the clarified text asks for.
- **Record:** RV-B-01 recorded the per-dimension outcome in `context.md` ("Direction carriers per Level 2: composition carried; color carried (weakened until the post-path surface fix); typography carried; interaction carried by absence").
- **Level 1 made no carrier assessment of its own.** In all three runs every carrier finding comes from Level 2. RV-C-01's visible pre-dispatch Level 1 summary mentions genericness, clusters and the fingerprint, but not carriers.
- **Result: RESOLVED for exposure when Level 2 runs; NOT ASSESSABLE for Level 1 alone.** The previous silent failure (BM-C-02: a dimension with no carrier, unflagged) did not recur: the same failure shape appeared (RV-C-02 below the fold) and was caught. But it was caught by Level 2, and all three runs triggered Level 2. Whether Level 1 alone would catch it, the path BM tested, is not shown by this benchmark.

## 9. Level 1 / Level 2 evidence

- **Level 2 triggered in 3 of 3** once "not production-facing" was removed. Builders cited the production-facing / public-facing stakes signal. This is consistent with the External Test A reading and with audit F1 / PT-21: at page scope, a real client's landing page reads as production-facing.
- **Mechanism:** each run dispatched a fresh `lexia-design:visual-critic` (a preferred type), not a fork. RV-B-01 dispatched it in the background and received its report later.
- **Ordering (NEW, 1 of 3):**
  - **RV-C-02** records "Level 1 critique (after refinement; formed after the Level 2 report was read, so not independent of it)".
  - **RV-C-01** formed Level 1 before dispatch (visible thinking, transcript line 452; dispatch at line 453) and wrote it down afterwards.
  - **RV-B-01** wrote Level 1 to `context.md` (line 509) after the background dispatch (line 483) but before the report arrived.
  - The draft of this report said RV-C-01's order could not be established; the independent review located the evidence, and the count is now 1 of 3.
  - The protocol assumes both exist independently ("compare … after both exist") but never says Level 1 must be fixed before the Level 2 report is read.
- **Synthesis:** RV-B-01 stated the disagreement (hierarchy 4 vs 3) and resolved it in the reviewer's favour with a reason. That is disclosed, not silent. No run re-dispatched Level 2 after REFINE (audit D1 / PT-20, unchanged).
- **Score semantics:** RV-C-01 Level 1 recorded axes 5 and 6 as "pass" rather than a 1–5 score. That contradicts "Score six axes 1–5" and may be a minor regression in interpretation (observed once).

## 10. Box-ticking

- No carrier in any final render is an isolated label or ornament added to satisfy a claim.
- The only borderline device is RV-C-01's ruled studio sheet, and it runs the other way: a device shared with the rejected candidate, which Level 2 flagged as not distinguishing. It is not a proof ornament.
- All exposed gaps were answered by recomposition or re-colouring, not decoration.
- **Result:** not observed.

## 11. Comparison with the previous benchmark

| Finding (BM) | BM result | This revalidation | Status |
|---|---|---|---|
| B1: first-generation axis 3 scored inconsistently | 1 numeric of 5 readings; K1 may have primed the 3 builds | 6 of 6 not assessable, unprimed, under clarified text; exact string in 1 of 3 Level 1 records | **RESOLVED** (format variance only) |
| B2: Level 2 scored a label without its definition | 1 controlled re-score; no benchmark Level 2 ran | 3 real Level 2 runs; no label-only scoring of axis 3; inputs carried; definitions paraphrased, not complete; axis 3 dictated in 2 | **PARTIALLY RESOLVED** |
| C1: declared dimension shipped without a carrier, unflagged | BM-C-02 materiality, no Level 2 | Same failure shape in RV-C-02 (and a weak one in RV-B-01) exposed by Level 2 using the carrier question, fixed by genuine revision | **RESOLVED when Level 2 runs; NOT ASSESSABLE for Level 1 alone** |
| Box-ticking risk | unmeasurable (no diagnostic) | diagnostic in text and in use; not observed | not observed (3 runs) |
| K2 engineered DETECTED | BM-C-01 DETECTED | RV-C-01 HYPOTHESIS | confound **confirmed and removed** |
| D1 / PT-20 (after REFINE) | Level 1 re-run 2/3 | no second Level 2 in 3/3; Level 1 re-run 1/3 | **REPRODUCED** |
| `context.md` before build | 1 of 3 | 1 of 3 | **REPRODUCED** (observation) |
| PRN-0001 adoption | 3 of 3 | 3 of 3 | **REPRODUCED** (observation) |
| Level 1 formed after Level 2 read | not observable | RV-C-02 explicit; RV-C-01 unknown | **NEW** |
| External reference library use undisclosed | suppressed by prompt | RV-B-01 `taste-examples`, undisclosed (K4) | **NEW** |
| Axes 5/6 recorded "pass" | not seen | RV-C-01 | **NEW** (minor) |

**Did removing K1/K2/K3 change the interpretation?**
- **K1:** yes. BM's B1 result may have been primed; this one is not, so B1 is now resolved on stronger evidence.
- **K2:** yes. The concept-bearing case now takes the HYPOTHESIS path, so all three runs exercised C1 on the path C1 was written for.
- **K3 together with the removed production-facing line:** it changed the Level 2 condition entirely (0/3 → 3/3). That is why C1 is now observed through Level 2 rather than Level 1. This benchmark therefore answers a different question for C1 than BM did.

## 12. Findings

| ID | Finding | Status |
|---|---|---|
| RV-1 | B1 behaviour: axis 3 not assessable on first generation, baseline recorded, unprimed, 6/6 | RESOLVED |
| RV-2 | B1 string format varies (colon vs parenthesis) | RESOLVED in substance; format NOTE |
| RV-3 | B2: recorded inputs carried and Level 1 withheld in 3/3 Level 2 briefs | RESOLVED |
| RV-4 | B2: "complete Level 1 definition" not delivered verbatim in any brief; one omits C1's absence clause | PARTIALLY RESOLVED |
| RV-5 | B2: axis-3 outcome dictated to the reviewer in 2/3 | NEW (minor) |
| RV-6 | C1: carry-through failure exposed and genuinely revised when Level 2 runs (2 cases) | RESOLVED |
| RV-7 | C1 via Level 1 alone | NOT ASSESSABLE (Level 2 ran in every case) |
| RV-8 | Box-ticking | not observed |
| RV-9 | Level 1 formed after reading the Level 2 report (RV-C-02; 1 of 3) | NEW |
| RV-10 | Level 2 triggers for any real-client landing page (3/3) | REPRODUCED (audit F1 / PT-21) |
| RV-11 | No second Level 2 after REFINE on the axis Level 2 flagged | REPRODUCED (audit D1 / PT-20) |
| RV-12 | Undisclosed use of an external reference library via a user-level rule | NEW (environment; relates to audit A2) |
| RV-13 | Axes 5/6 recorded as "pass" | NEW (minor, n = 1) |
| RV-14 | Level 2 pointed at the whole `context.md`, exposing builder judgement in Known Exceptions (RV-C-02) | NEW (minor) |
| RV-15 | Fingerprint baseline left stale after REFINE changed a fingerprint dimension (RV-C-02 typography) | NEW (minor; affects later comparisons) |

## 13. Integrity checks

- The installed copy stayed identical to the repository (18/18 SHA-256) before and after the runs. No write to it was attempted by this milestone.
- No repository skill file changed.
- `<external-test-a-project>` and the previous benchmark workspace are unmodified.
- Builders wrote only inside their own project folders (transcript `Write`/`Edit` paths).
- Analyst renders were produced by the plugin Playwright MCP, whose save root is the repository. They were written to its `.playwright-mcp/` scratch folder, moved to the evidence folder, and the folder was deleted, so nothing was left in the repository.

## 14. Confounds and limitations

1. **n = 3,** one run per case.
2. **Level 2 ran everywhere,** so C1's behaviour through Level 1 alone was not tested here (RV-7). The previous benchmark tested only that path, and this one only the other.
3. **K4:** RV-B-01 consulted an external reference library. It does not affect B1, B2 or C1 directly, but its direction's origin is not comparable with BM-B-01.
4. **Lost screenshots:** builders deleted their own screenshot folders (RV-C-01, RV-C-02). Pre-REFINE images were recovered from the transcripts, but their exact capture moments are inferred from order.
5. **Level 1 is only partly visible:** the transcripts show no visible reasoning, so Level 1 is observable only where the builder wrote it down. Ordering claims rest on the builders' own statements (RV-9).
6. **Carrier judgements** are qualitative (analyst plus Level 2 reviewers plus the §8 reviewer).

## 15. Independent review and reconciliation

One fresh, read-only reviewer (general-purpose subagent) received the evidence, the installed criteria and seven questions (`_method/REVIEWER-BRIEF.md`), not the draft. Raw output: `_method/REVIEWER-RAW-OUTPUT.md`.

**Process note:** the reviewer disclosed that it wrote one extraction file (`c01.txt`) into the main agent's session scratchpad, outside every project and the repository, in breach of its read-only instruction. The file was removed by the main agent. No project, evidence or skill file was affected.

| Question | Reviewer | Draft | Reconciliation |
|---|---|---|---|
| 1 B1 | RESOLVED; C-01 "pass" on axes 5/6; C-02 baseline fingerprint stale after REFINE | RESOLVED; "pass" noted | **Agreed;** stale baseline adopted as RV-15 (verified: `context.md` l.25 vs l.53) |
| 2 B2 | PARTIALLY RESOLVED; C-01 carrier clause omits absence and never-presumed parts; C-02 pointed reviewer at `context.md` containing builder genericness conclusions; B-01 mild pre-framing | PARTIALLY RESOLVED | **Agreed;** the `context.md` exposure adopted as RV-14, details added to §7 |
| 3 C1 | RESOLVED; C-01 interaction not assessable from a static render (present in code); C-02 appended "design revised, not the claim" note | RESOLVED when Level 2 runs | **Agreed;** appended note verified (`context.md` l.47) and added to §8; interaction wording adjusted |
| 4 Ordering | PARTIALLY RESOLVED; C-01 Level 1 formed before dispatch (visible thinking); B-01 clean; only C-02 after | C-01 order "cannot be established" | **Adopted** after verifying transcript lines 452/453 (C-01) and 483/509 (B-01); RV-9 narrowed to 1 of 3 |
| 5 Box-ticking | RESOLVED (none) | not observed | **Agreed** |
| 6 Contradictions | NEW minor items; B-01 did not disclose the missing re-review | same items, less detail | **Agreed;** §5 row updated |
| 7 taste-examples | NEW confound; undisclosed; limits attribution of B-01's direction, not B1/B2/C1 | K4, same | **Agreed** |

No disagreement remains unreconciled, so the outcome is not `UNRESOLVED` (`loop.md` §8).

## 16. Is additional specification work justified?

- **Not for B1.** It behaves as clarified.
- **Possibly, narrowly, for B2 and ordering (RV-4, RV-5, RV-9, RV-14).** A sentence could say that Level 1 is recorded before the Level 2 brief is written, and that the brief carries the axis text rather than a paraphrase or a pre-applied outcome. Both are small, text-only and in the same file. They rest on 3 runs.
- **Not yet for C1.** It worked when used. What remains unknown is Level 1 alone, which needs evidence, not wording.
- **RV-10, RV-11 and RV-12** belong to already-recorded clarification candidates (F1/PT-21, D1/PT-20, A2) and should be handled there, not here.

## 17. Recommendation

**Recommended (requires human authorization; not authorized here):** *Targeted Specification Clarification: Level 1/Level 2 independence*, text-only in `critique-protocol.md`:
- (a) Level 1 is formed and recorded before the Level 2 brief is written or its report read (RV-9).
- (b) The brief carries each axis's Level 1 text as written rather than a paraphrase, passes rules rather than pre-applied outcomes, and passes the recorded inputs rather than a pointer to the whole `context.md` (RV-4, RV-5, RV-14).
- RV-15 (refresh the fingerprint entry when REFINE changes a fingerprint dimension) belongs with the existing fingerprint-hygiene candidate (PT-30), not this clarification.

**Alternatives:**
- a Level-1-only C1 benchmark, with runs that do not trigger Level 2 through their own brief, to settle RV-7;
- the already-recommended F1/PT-21 trigger clarification, which RV-10 reinforces.

## 18. Explicit statement

No Design Excellence source file and no installed skill file was modified in this milestone. Nothing was pushed.
