# Direction Carry-Through & Distinctiveness Semantics Benchmark

- **Date:** 2026-09-28
- **Status:** COMPLETED (behavioural evidence only; no Design Excellence file changed)
- **Parent milestone:** External Test Analysis & Behavioral Gap Audit (`benchmarks/external-test/20260928-external-test-a-gap-audit.md`, "the audit")

---

## 1. Scope and authorization

- **Authorization (human, verbatim, recorded in `STATE.md`):** "Autorizo el milestone Direction Carry-Through & Distinctiveness Semantics Benchmark."
- **In scope:** BM-C (direction-to-build carry-through) and BM-B (first-project distinctiveness semantics) as defined in the audit §12. That means three greenfield page BUILDs (BM-C-01, BM-C-02, BM-B-01) against the unchanged installed skill, and a read-only re-score of `<external-test-a-project>`.
- **Out of scope, and not done:** any change to the skill, its installed copy, `loop.md` or governance. The audit's proposed wordings (C1 diagnostic, B1 first-entry clause, B2 Level 2 axis definitions, D1 re-check, E1, F1, H2) were **not** implemented. They are treated here only as hypotheses to test.
- **Governance:**
  - Each build was run by its own main agent, a fresh headless Claude Code session in its own empty folder.
  - Two read-only subagents were used: the BM-B re-score critic and the `loop.md` §8 reviewer. Both briefs and raw outputs are preserved.
  - No agent wrote to another agent's project.

## 2. Skill revision tested

- **Repository:** `HEAD` `21e579f`. The skill tree `design-excellence/` is unchanged since `9c719a7`; `git diff --stat 9c719a7 HEAD -- design-excellence` is empty.
- **Installed copy:** `C:\Users\<user>\.claude\skills\design-excellence`, 18 files, SHA-256 identical to the repository before the runs and re-checked after them (§13). Still write-guarded; not touched.
- **How the skill loaded:** every build prompt began with `/design-excellence`. The slash-command expansion of SKILL.md is not echoed in `stream-json` output, so it cannot be quoted from the transcripts. Skill use is evidenced by three things:
  - every session read references only from the installed path;
  - every session used the skill's classification-line format;
  - every session used the skill's stage and section vocabulary.
- **Correction to the milestone brief:** `layout-interaction.md` lives at `references/rule-catalog/layout-interaction.md`, not at `references/`.

## 3. Benchmark environment

| Item | Value |
|---|---|
| Workspace | `C:\Users\<user>\Desktop\design-excellence-benchmark` (created for this milestone; outside the repository) |
| Builder | `claude -p` (Claude Code 2.1.283), `--model claude-opus-5-5`, `--permission-mode acceptEdits`, tools `Bash Write Edit Read Glob Grep Skill mcp__playwright`, one session per folder, run in parallel |
| Browser | Enhanced: Playwright MCP (Chromium) via `npx @playwright/mcp@latest --isolated`, one isolated instance per session (`--strict-mcp-config`). This is the same package the External Test A test used; `--isolated` only stops the three parallel sessions sharing one browser profile. No new browser infrastructure was installed |
| Session environment | User-level plugins and hooks load in headless sessions, as they did in the External Test A test (ponytail, superpowers, vercel context; a lexia detector hook ran on writes). Runs report not using them for design decisions |
| Stack instruction | Single static HTML page, no dependencies (a stack instruction, not a visual one; it differs from External Test A's Astro) |
| Reference instruction | "Do not acquire or consult external visual references (Figma, the licensed library, the web, reference catalogs, or other skills). The skill's own internal reference pools may be used as the skill specifies." No "reference-free" wording |
| Level 2 control | Each brief states the page is an internal benchmark, not production-facing, not brand-critical, not high-traffic, and will not be deployed. Nothing else disables Level 2 |
| Evidence | Each project has `test-evidence/` with `BRIEF.md`, `INVOCATION.md` (exact command and verbatim prompt), `RUN-LOG.md` (builder's own log), `transcript.jsonl` (raw session log), `transcript-summary.txt` (tool calls, files read and written), `pre-refine-*.png` and `final-*.png` |
| Durations | BM-B-01 8.8 min, BM-C-01 10.5 min, BM-C-02 10.4 min |

**Benchmark-design confounds (disclosed up front; they limit every conclusion below):**
1. **K1, priming by the evidence instruction.** The common instruction asked the builder to log "every axis with its score **or status** and reason". The word "status" may have nudged builders toward `not assessable` on axis 3.
2. **K2, BM-C-01's brief.** The brief (as specified by the milestone) says it "deliberately asks for a direction with a material distinction that can be carried into the rendered interface". The builder read that as an explicit request to embody an idea, recorded **DETECTED / EVIDENCED**, and ran LAYOUT-009. BM-C-01 therefore tested the concept path, not the pure direction path C1 is about.
3. **K3, awareness.** Every builder knew it was a benchmark and was asked to log the committed and rejected directions. The External Test A builder was an external test framed as a client project. Carry-through may be better when the builder knows it is observed.
4. **K4, re-score build state.** The External Test A re-score saw the final (post-REFINE) build, while the original Level 2 saw the pre-REFINE build.

## 4. BM-C-01

| Field | Record |
|---|---|
| Path | `C:\Users\<user>\Desktop\design-excellence-benchmark\BM-C-01` |
| Brief | `test-evidence/BRIEF.md` (verbatim): internal design benchmark landing page for fictional analog print studio "Morrow Press"; physical paper, ink, registration, layering and imperfect print; direction with a material distinction to be carried into the rendered interface; no invented facts |
| Classification | "Reading this as: page BUILD on a genuinely-empty project." |
| Register / Genre / Dials | brand-led, atmospheric-expressive, variance 8 (High), motion 4, density 3 |
| Concept detection | **DETECTED / EVIDENCED**, citing the two brief sentences (see K2) |
| T3 internal pools | Loaded (`visual-references.md`, `principle-pool.md`); all entries screened (LAYOUT-010); **PRN-0001 and REF-005 adopted** into the committed candidate; REF-009 considered and set aside |
| External references | None (transcript: no web, Figma or the licensed library tools; reads limited to the skill and the project) |
| Committed direction | "Two-plate overprint sheet": blue key plate carries all type; yellow multiplied plate slightly off register; overprint green where they cross; a page-wide "In register" toggle; explorations shown as live-drawn test prints |
| Rejected direction | "Letterpress impression sheet" (one ink, cotton stock, locked-up column, deboss, type-case index nav) |
| Distinguishing dimensions (as logged) | composition, color, typography, materiality, interaction (5 of 6) |
| LAYOUT-009 organizing surfaces | interaction (register toggle), content architecture (live specimens) |
| Level 1 (pass 1 → pass 2) | Genericness 4 → 4; Hierarchy 4 → 4; **Distinctiveness `not assessable` → `not assessable`**; Craft 3 → 4; Accessibility 3 → 4; Technical 4 → 4 |
| Level 2 | Not triggered (reasons logged: not production-facing, not REDESIGN, page scope, no escalation) |
| REFINE | Yes (hero exceeded one frame, A11Y-010 overflow at 320 px, yellow plate over notice copy, mobile header rows). Pre-REFINE screenshots exist |
| Fingerprint History | First entry recorded; the log says the check "ran, trivially: no prior entries" |
| Skipped / not assessable | axis 3; HARDEN (declared non-ship-readiness); CWV; emulated reduced-motion render (CSS-verified only); screen reader; cross-browser; A11Y-005 measurement |
| Final evidence | `test-evidence/final-desktop-1440.png`, `final-mobile-375.png` |

**Rendered carriers (from `final-desktop-1440.png` and source):**

| Dimension | Carrier | Verdict |
|---|---|---|
| Color | Two spot inks multiplied on grey-warm stock across every section; overprint green where plates cross (`mix-blend-mode` ×3 in source) | yes |
| Materiality | Rough plate edges and ink spread (`feTurbulence` SVG filters ×5), paper swatches, mottled "imperfect print" specimen | yes |
| Interaction | Page-wide register toggle (header and specimen) moving every yellow plate; verified in RUN-LOG §8 | yes |
| Composition | Poster hero → specimen sheet under crop marks → job docket → colophon | yes |
| Typography | Archivo condensed heavy with Courier Prime docket type | yes |

**Box-ticking check:** the independent reviewer (§14) judged the swatch legend strip under the hero and the "Paper" specimen (three plain rectangles) to be label-like, as is the small yellow patch behind "Job docket". None of them is load-bearing: every dimension also has a page-wide carrier. Minor label-like elements, with real core carriers.

## 5. BM-C-02

| Field | Record |
|---|---|
| Path | `C:\Users\<user>\Desktop\design-excellence-benchmark\BM-C-02` |
| Brief | `test-evidence/BRIEF.md` (verbatim): internal design benchmark landing page for fictional boxing organization "Iron Form"; mandated palette black and saturated red; no other visual direction; no invented facts |
| Classification | "Reading this as: page BUILD on a genuinely-empty project." |
| Register / Genre / Dials | brand-led, atmospheric-expressive, variance 7, motion 4, density 3 |
| Concept detection | **HYPOTHESIS** ("Form" as technique; name only); LAYOUT-009 not activated; tone only, no motif |
| T3 internal pools | Loaded; screened; **PRN-0001 adopted** in the committed candidate; REF-009 informed the rejected candidate; REF-002 considered and judged unnecessary |
| External references | None |
| Committed direction | "Fight Bill": red is the paper and black the ink (letterpress fight bill on red stock); one-frame entry view with facts band; fundamentals as a descending "billing" where size encodes learning order |
| Rejected direction | "Wall Board": black ground, red as ruled segmentation (Committed tier), mono + grotesk, long document. Rejected partly because black ground + single red accent is SLOP-011 cluster 2 |
| Distinguishing dimensions (as logged) | composition, color, typography, materiality |
| Level 1 (pass 1 → pass 2) | Genericness 3 → 3; Hierarchy 4 → 4; **Distinctiveness `not assessable` → `not assessable`**; Craft 2 → 4; Accessibility 2 → 4; Technical 4 → 4 |
| Level 2 | Not triggered. Craft and Accessibility were 2 on pass 1, but not on two consecutive passes |
| REFINE | Yes (h2 and button overflow at 375/320, placeholder overflow, TYPE-006 orphan, `main` landmark and skip-link failure, billing proximity). Pre-REFINE screenshots exist. Two interim tuning screenshots taken before pass 1 were deleted by the builder "as non-evidence" |
| Fingerprint History | First entry recorded; axis 3 stamped "n/a" in `context.md`, `not assessable` in RUN-LOG |
| Skipped / not assessable | axis 3; HARDEN; CWV; cross-browser; screen reader; A11Y-005 measurement |
| Final evidence | `test-evidence/final-desktop-1440.png`, `final-mobile-375.png` |

**Rendered carriers:**

| Dimension | Carrier | Verdict |
|---|---|---|
| Color (Drenched red paper, not a black ground) | Hero and training section are red stock with black ink. The black middle section with red display words is the rejected candidate's own combination, which the builder flagged as a local SLOP-011 cluster 2 match | **partial** |
| Composition | One-frame poster entry with facts band; descending billing (STANCE → DEFENCE by size); ruled particulars table | yes |
| Typography | Mixed widths (extended IRON, condensed FORM) plus IBM Plex Mono are rendered. But the logged contrast with the rejected "mono + grotesk" barely exists, because the committed pairing is also grotesk + mono | **partial**: carried, but hardly a distinction |
| Materiality ("printed bill with rules") | Flat red fill and heavy rules only; no paper, ink or press texture in source (`feTurbulence` 0). Rules were also the rejected candidate's device ("ruled segments"), so they cannot carry a distinction from it | **no carrier** (draft said "partial"; revised after independent review, §14) |

**Box-ticking check:** none observed. The run did not add decoration to prove the direction. The materiality claim was simply left without a carrier, and no step noticed it: Level 1 axis 1 pass 1 and pass 2 did not mention materiality.

## 6. BM-B-01

| Field | Record |
|---|---|
| Path | `C:\Users\<user>\Desktop\design-excellence-benchmark\BM-B-01` (created empty; `ls -A` empty before launch; no `.design/`) |
| Brief | `test-evidence/BRIEF.md` (verbatim): internal design benchmark landing page for fictional neighborhood ceramics workshop "Fieldwork"; wheel throwing, hand building, glazing, small groups; welcoming to beginners without talking down to returning makers; no invented facts; no visual direction given |
| Classification | "Reading this as: page BUILD on a genuinely-empty project." |
| Register / Genre / Dials | brand-led, atmospheric-expressive, variance 6, motion 4, density 3 |
| Concept detection | HYPOTHESIS ("Fieldwork" = hands-on practical work); LAYOUT-009 not activated |
| T3 internal pools | Loaded; **PRN-0001 and REF-005 adopted**; REF-002 informed the rejected candidate; PRN-0003 screened out (placeholder values) |
| External references | None |
| Committed direction | "Shape, then glaze": long-document route of the clay; one-frame entry with a technique fact band; wheel and hand as two parallel paths converging on a drenched glaze band |
| Rejected direction | "Glaze test-tile board" (bento tiles, full palette, rounded sans, scroll-anchored wheel) |
| Distinguishing dimensions | composition, color, typography, interaction |
| Level 1 (pre-REFINE only) | Genericness 3; Hierarchy 4; **Distinctiveness `not assessable`**; Craft 3; Accessibility 5; Technical 4 |
| Level 2 | Not triggered |
| REFINE | Yes (TYPE-006 orphan, MOTION-008 bare hover, placeholder mass). Level 1 was **not** re-run after REFINE ("narrow fixes … re-verified mechanically"). Pre-REFINE screenshots exist |
| Skipped / not assessable | axis 3; HARDEN (declared prototype/benchmark); cross-browser; A11Y-005 measurement; offline font fallback |
| Final evidence | `test-evidence/final-desktop-1440.png`, `final-mobile-375.png` |

**First-project Fingerprint History evidence (§8 of the brief), verbatim from the run:**
- **Fingerprint History created:** yes. `context.md` "## Fingerprint History": "2026-09-28, page v1: macrostructure = one-frame entry + process-ordered long document (parallel paths converging); typography = Young Serif + Hanken Grotesk; color-anchor = raw-clay grey paper with drenched deep glaze teal; density = Low; motion = Medium-low (single CSS load moment). Distinctiveness check: first entry, nothing to compare against."
- **Axis 3 numeric?** No.
- **Axis 3 status and reason:** "**Distinctiveness: not assessable.** Fingerprint History has no prior entries, so there is nothing to test 2-of-5 against. This run created the first entry." (RUN-LOG §5)
- **First entry stored as baseline:** yes, as above.
- **How the empty comparison was treated:** not assessable. It was not treated as satisfied, failed or skipped. RUN-LOG §9 lists it under "Skipped or not assessable".
- **Stamp in `context.md`:** "distinctiveness not assessable (no prior entries)".

**Rendered carriers (supplementary; this is not a BM-C run, but Level 2 did not run here either):**
- **Composition:** yes. There are two staggered shaping paths, then a full-width drenched band.
- **Color:** yes. The page uses raw-clay grey with drenched teal.
- **Typography:** yes. It pairs a heavy low-contrast serif with a grotesk.
- **Interaction:** "static page with one load moment" versus the rejected scroll-anchored wheel. This dimension is defined by an **absence**, and its carrier is the lack of scroll choreography (source: 2 one-shot keyframes, no script). It is satisfied, but a "name the element that carries it" test does not fit it well (§8).

## 7. External Test A read-only re-score

- **Method:** a fresh `lexia-design:visual-critic`, the same critic type as the original Level 2, reviewed the final External Test A screenshots, `context.md`, SLOP-011/013 and SKILL §6. It was given the **verbatim current six axis definitions** from `critique-protocol.md` l.9 to l.14. It was not given any prior scores, the audit or a hypothesis. `<external-test-a-project>` was only read.
- **Evidence:** `design-excellence-benchmark\BM-B-rescore\test-evidence\REVIEWER-BRIEF.md`, `axis-definitions-verbatim.md`, `REVIEWER-RAW-OUTPUT.md`.

| Axis | Original Level 1 | Original Level 2 | Re-score with verbatim definitions |
|---|---|---|---|
| 1 Genericness | 3 | 3 | 3 |
| 2 Hierarchy | 4 | 4 | 4 |
| 3 Distinctiveness | 3 | **2** | **`not assessable`**: the Fingerprint History holds no prior entry |
| 4 Craft | 4 | 4 | 4 (partial, screenshots only) |
| 5 Accessibility | 4 | 4 | `not assessable` (no computed checks possible from screenshots) |
| 6 Technical | 5 | 5 | `not assessable` (no code or runtime) |

Answers to the milestone's five questions:
1. **What axis 3 means under the current text:** the §6 intra-project fingerprint comparison (2 of 5 dimensions against the last 5 entries), "where in scope". The re-score critic reached this reading unaided: "The fingerprint check measures sameness between generations of one project, not how the page looks against competitors. I judge the market-level question under axis 1."
2. **What the External Test A Fingerprint History supports:** one entry, the build itself. That is a baseline, and nothing about divergence.
3. **Is a first-generation numeric score defensible?** Only under the "trivially satisfied" reading. The re-score critic: "Turning a trivial pass into a 1–5 score would be estimating." `critique-protocol.md` l.7 forbids estimates for an axis that cannot be evaluated honestly. The number is not defensible as an assessment. The text still does not name this case, so it is not forbidden in terms.
4. **Does the label create ambiguity?** Yes. The critic listed axis 3 among "unclear" definitions and resolved it only because the definition was in front of it. The original Level 2, whose brief is not preserved, scored perceived identity on the same label.
5. **With the definitions given:**
   - the axis-3 disagreement disappears;
   - the category concern moves to axis 1;
   - axis 1 lands at 3, the same value as both original levels.
   The category-default finding (condensed heavy caps with black and red) was reproduced verbatim in substance, tagged [Genericness].
   n = 1, with confound K4.

## 8. Direction carry-through findings

1. **Is there a check? No, for HYPOTHESIS / NOT DETECTED runs.**
   - **Text:** `critique-protocol.md` axis 1 asks a brief-level question; the structural test runs only for DETECTED. `SKILL.md` §5 compares candidates on paper; §6 compares against project history.
   - **Behaviour:** in BM-C-02 and BM-B-01 no step walked the declared dimensions against the render. BM-C-02's axis 1 did name "subject-derived choices" (mixed-width name, descending billing) and "generic parts", which is a partial, unprompted self-check. It never reached the materiality dimension, which had no carrier.
   - **Disposition:** the absence of a per-dimension check reproduces, a **CONFIRMED GAP** in coverage.
2. **When a concept is DETECTED, an existing mechanism does cover it.** In BM-C-01 the Level 1 structural test ("would the concept still be perceptible if … removed") was run and explicitly confirmed the concept lives in interaction and content architecture. That functioned as a carry-through check for the organizing surfaces. It did not cover the carrier dimensions (color, typography, materiality), but all of those had strong carriers anyway. **EXPECTED BEHAVIOR.**
3. **Silent carry-through failure recurred, in a milder form, in a second project.**
   - **BM-C-02:** one of its four logged dimensions (materiality) had no rendered carrier. Two more (color, typography) were only partially carried, one of them because the claimed distinction from the rejected candidate barely existed on paper. Nothing in the run flagged any of this, and it shipped.
   - **BM-B-01:** every dimension was carried.
   - **Combined with External Test A:** 2 of 3 HYPOTHESIS-path generations without a Level 2 check on the final build had at least one declared dimension without a carrier. (External Test A's Level 2 caught it pre-REFINE; BM-C-02 had no Level 2.)
   - **Caveats:** n is small, and confounds K2/K3 would, if anything, favour carry-through. **Disposition for recurrence: CONFIRMED GAP** (the failure occurs across more than one project and is silent without Level 2).
   - **Note:** in BM-C-02 part of the failure sits at DIRECT (a claimed distinction that the committed and rejected candidates barely differ on), not only at BUILD. A per-dimension check after BUILD would expose both.
   - **Draft reversal:** the draft of this section said the failure did not recur. That was revised after the independent review (§14): the draft had counted rules as a materiality carrier without noticing that the rejected candidate used rules too.
4. **Decorative box-ticking:** no run added decoration to prove its direction, but there was no incentive to, because the diagnostic does not exist yet. The reviewer notes the risk is real if the check is self-administered: BM-C-02 could have cited "rules" and BM-C-01 its legend strip as carriers. **EVIDENCE INSUFFICIENT** for the size of the risk.
5. **Fit of the proposed diagnostic ("name the rendered element that carries each dimension"), judged on these runs:**
   - **Useful where a dimension is positive and material.** It would have pointed at BM-C-02's partial materiality, and at External Test A's pre-REFINE tape.
   - **Redundant in the DETECTED path** for organizing surfaces, where the structural test already asks the question.
   - **Ill-posed for dimensions defined by absence** (BM-B-01's "static, one load moment" versus a scroll-anchored rejected candidate). There the carrier is the lack of something.
   - **Subjective at the margin** ("partial" in BM-C-02 was a judgement call for this audit and needs the reviewer's agreement, §14).
   - **Not redundant on the HYPOTHESIS path,** where nothing else applies (reviewer).
   - **Guards the evidence supports:**
     - the carrier must distinguish the committed direction from the rejected one (a device both candidates share does not count);
     - dimensions defined by absence are satisfied by the absence of the rejected treatment;
     - the outcome of "no carrier" is to revise or **retract the claimed dimension**, never to bolt on decoration. Retraction is the reviewer's guard against box-ticking; bolting on decoration after commitment would contradict the DIRECT order that LAYOUT-009 also relies on;
     - it stays non-blocking, like the structural test;
     - it is also carried into any Level 2 brief.
   - **Net:** useful, not redundant, and now motivated by recurrence. But its box-ticking risk is unmeasured and its wording needs the guards above. **DEFERRED INVESTIGATION** for the wording; see §19.

## 9. First-project Fingerprint History findings

| Run | Skill text | Axis 3 recorded | First entry stored |
|---|---|---|---|
| External Test A (external test) | `9c719a7` | **3** ("2-of-5 check is trivially satisfied") | yes |
| BM-C-01 | same | `not assessable` (both passes) | yes |
| BM-C-02 | same | `not assessable` (both passes; "n/a" in `context.md`) | yes |
| BM-B-01 | same | `not assessable` ("nothing to test 2-of-5 against") | yes |
| Re-score critic (verbatim definitions) | same | `not assessable` | n/a |

- **The ambiguity reproduces as inconsistency across runs:** the same text produced a score once and `not assessable` four times. That is what the audit classified as B1 SPECIFICATION AMBIGUITY, and the benchmark supports that disposition. It also contradicts nothing in it.
- **The majority reading already matches the audit's proposed first-entry clause.** So the clause would codify existing behaviour rather than change it. That lowers its regression risk.
- **Caveats:**
  - **B1 is not "fixed":** the text is unchanged and one run in five read it the other way.
  - **Priming:** confound K1 may have inflated the `not assessable` count in the three builds. The re-score critic, whose brief allowed `not assessable` explicitly for any axis, is subject to the same caveat.
- **Axis 1 as the home of category/model genericness:** confirmed in every run that discussed it. BM-C-02 axis 1 ran the SLOP-011 gestalt and named the generic patterns. The re-score placed the category concern under [Genericness].
- **Baseline recorded:** yes in all four builds.
- **Disposition:** SPECIFICATION AMBIGUITY (reproduced).

## 10. Level 1 / Level 2 axis-definition findings

- **Did Level 2 receive the same axis definitions as Level 1?** Not observable in any benchmark run, because Level 2 did not trigger (by design). External Test A's Level 2 brief was not preserved. **EVIDENCE INSUFFICIENT** for what Level 2 actually receives.
- **Does passing the definitions reduce ambiguity?** In the single controlled comparison (§7), yes, materially. The axis-3 split (3 vs 2) became `not assessable`, and the substantive concern moved to axis 1, where all three readings agree at 3. **SPECIFICATION AMBIGUITY (B2), supported;** n = 1, with confound K4.
- The re-score also marked axes 5 and 6 `not assessable` from screenshots, correctly under l.7. The original Level 2 had scored them 4 and 5, apparently from the same kind of artifact (brief not preserved). That suggests the definitions affect more than axis 3 and strengthens the case for carrying them into any Level 2 brief. **EVIDENCE INSUFFICIENT** (the original reviewer's inputs are unknown).

## 11. Category-convention findings

- **BM-C-02 changed, beyond palette:**
  - **Color application:** red became the ground (Drenched stock), not a black ground with a red accent. The builder explicitly rejected the black-ground candidate as SLOP-011 cluster 2.
  - **Composition:** a one-frame poster entry with a facts band, a descending billing encoding learning order, and ruled particulars.
  - **Typography:** mixed widths, with mono for labels.
- **Category-conventional elements that remained:**
  - condensed heavy uppercase display type for the billing and headings;
  - one black section with red display words, which the builder itself flagged as a local cluster-2 match.
- **Cross-run observation:** Archivo condensed heavy appeared in three of four generations (External Test A, BM-C-01, BM-C-02), in two unrelated subjects. The fingerprint is per-project by design (`SKILL.md` §6: "No cross-project or cross-user storage exists or is proposed"), so no mechanism can see this. **Recorded as an observation only (DEFERRED INVESTIGATION); see §18.**
- **Does a mandated category palette systematically increase the need for carry-through?** Suggestive but unsupported. Both black-and-red builds (External Test A and BM-C-02) claimed a material dimension that did not reach the render, and BM-B-01 (unconstrained palette) carried everything. But palette and subject are confounded (both boxing), and there is no non-mandated boxing control. **EVIDENCE INSUFFICIENT.**

## 12. LAYOUT-009 separation findings

- **Activation:**
  - **HYPOTHESIS path, 2 runs (BM-C-02, BM-B-01):** LAYOUT-009 did not activate. Neither a direction's metaphorical name ("Fight Bill", "Shape, then glaze") nor its material language activated it. **EXPECTED BEHAVIOR.**
  - **BM-C-01:** LAYOUT-009 activated naturally, from the brief's own sentence (K2).
- **Was BM-C-01's activation correct?** Under `SKILL.md` l.38, DETECTED includes a brief that "explicitly asks for an idea to be embodied or felt". A sentence asking for "a direction with a material distinction that can be carried into the rendered interface", beside a list of the studio's subjects, can reasonably be read that way. It can also be read as a request about the *direction's* properties, which the audit deliberately kept separate from a brief concept.
  - The skill does not say whether a brief-requested direction property counts as an "idea to be embodied". The reviewer adds that the sentence names no specific idea; the model chose registration and layering itself.
  - **Disposition: EXPECTED BEHAVIOR under the current text,** with a benchmark-design confound (K2): the sentence was written by the benchmark and effectively engineered DETECTED. The draft classified this as a new SPECIFICATION AMBIGUITY. That was withdrawn after independent review (§14), because a single benchmark-engineered sentence is not evidence of ambiguity in real briefs. The direction/concept boundary is recorded as **DEFERRED INVESTIGATION**, to watch in real briefs.
- **Can carry-through be evaluated without expanding Concept → Structure?** Yes. In this benchmark it was evaluated (by this audit and the reviewer) directly against the §5-logged dimensions, with no need for LAYOUT-009 on the HYPOTHESIS runs.

## 13. Evidence matrix

| Question | BM-C-01 | BM-C-02 | BM-B-01 | Test A re-score | Result |
|---|---|---|---|---|---|
| Level 2 triggered | no | no | no | n/a | benchmark control worked |
| Concept outcome | DETECTED (K2) | HYPOTHESIS | HYPOTHESIS | (HYPOTHESIS) | n/a |
| LAYOUT-009 active | yes, naturally | no | no | no | separation held on the HYPOTHESIS path |
| T3 pools loaded / used | yes / PRN-0001, REF-005 | yes / PRN-0001 | yes / PRN-0001, REF-005 | n/a | used in 3/3; PRN-0001 adopted 3/3 |
| External references | none | none | none | none | n/a |
| Per-dimension carry-through check performed | via structural test (organizing surfaces only) | no | no | n/a | gap in coverage on the HYPOTHESIS path |
| All declared dimensions carried | yes (5/5; minor label-like elements) | **no**: materiality none; color and typography partial | yes (4/4; interaction by absence) | n/a | silent partial failure in BM-C-02 |
| Box-ticking observed | no | no | no | n/a | n/a |
| Axis 3 on first generation | not assessable | not assessable | not assessable | not assessable | vs Test A original: 3 |
| First fingerprint entry stored | yes | yes | yes | (yes, original) | n/a |
| Axis 1 holds category judgement | yes | yes | yes | yes | n/a |
| Level 1 re-run after REFINE | yes | yes | **no** | n/a | inconsistent (audit D1 / PT-20) |
| Pre-REFINE screenshots | yes | yes | yes | no (original) | H5 evidence gap closed for these runs |
| `context.md` written before `index.html` | yes | **no** | **no** | (n/a) | observation |
| HARDEN | skipped (non-ship) | skipped | skipped | n/a | consistent with briefs |
| Level 1 scores stamped in Fingerprint History | **no** (entry omits them) | yes | yes (pre-REFINE only) | n/a | observation (reviewer) |

**Post-run integrity checks:**

| Check | Result |
|---|---|
| Skill tree | `git diff --stat -- design-excellence` empty; `loop.md` unchanged |
| Installed copy | 18/18 files SHA-256 identical to the repository after the runs |
| `<external-test-a-project>` | no file newer than 09:00 (milestone start 09:2x) |
| Benchmark projects | not modified by the review subagents; the main agent added only `test-evidence/BRIEF.md`, `INVOCATION.md`, `transcript.jsonl` and `transcript-summary.txt` after each run |
| Out-of-folder writes | Builder transcripts show `Write`/`Edit` only inside their own project folders |

## 14. Independent review and reconciliation

One fresh, read-only, blind reviewer (general-purpose subagent). It was given the evidence paths, the skill text and seven questions (`design-excellence-benchmark\REVIEW\REVIEWER-BRIEF.md`), not this report's conclusions or the audit's verdicts. It changed nothing. Its raw output is preserved verbatim in `design-excellence-benchmark\REVIEW\REVIEWER-RAW-OUTPUT.md`.

| Question | Reviewer | Draft of this report | Reconciliation |
|---|---|---|---|
| 1 Carriers | BM-C-01: all 5 yes; swatch legend and "Paper" specimen label-like. BM-C-02: composition yes; color partial (black middle section is the rejected combination); typography partial (committed and rejected are both grotesk + mono); **materiality no** (flat fill + rules, and rules were the rejected candidate's device). CONFIRMED GAP | BM-C-02: color yes (exception noted), typography yes, materiality partial | **Adopted in full.** The draft missed that rules and grotesk + mono were shared with the rejected candidate, so they cannot carry a distinction. §5, §8, §13, §15 and §16 revised; the draft's "no silent failure" conclusion reversed |
| 2 Existing check | CONFIRMED GAP: structural test DETECTED-only and about the concept; LAYOUT-009 validation is a planning record; nothing re-checks §5 dimensions; nothing applies on HYPOTHESIS | Same | **Agreed** |
| 3 LAYOUT-009 | EXPECTED BEHAVIOR with confound: the brief sentence is a benchmark-written meta-instruction naming no specific idea | SPECIFICATION AMBIGUITY (new) | **Adopted.** Downgraded to EXPECTED BEHAVIOR; boundary kept as a DEFERRED observation (§12) |
| 4 Axis 3 first generation | SPECIFICATION AMBIGUITY: 3 runs `not assessable`, Test A 3; first entry recorded in all; BM-C-01 omits Level 1 scores in Fingerprint History; BM-B-01 has pre-REFINE only | Same | **Agreed;** the two observations added to §13 |
| 5 Re-score | SPECIFICATION AMBIGUITY: axis 1 stable at 3; axis 3 `not assessable`; the label invites a perceived-identity reading; carry-through concern belongs under axis 1; caveats n = 1 and pre/post-REFINE | Same | **Agreed** |
| 6 Mandated palette | EVIDENCE INSUFFICIENT; both black-and-red boxing cases left a material claim without a carrier: suggestive, confounded with subject | EVIDENCE INSUFFICIENT | **Agreed;** the suggestive pattern added to §11 |
| 7 Diagnostic | DEFERRED INVESTIGATION: useful and not redundant on HYPOTHESIS; moderate subjectivity; box-ticking risk real if self-administered; outcome should be retract-or-revise, non-blocking, carrier definition excluding stickers, also in Level 2 briefs | DEFERRED; "not yet justified by recurrence" | **Adopted:** the guards are added to §8 item 5 and §19; "not yet justified by recurrence" withdrawn, since recurrence is now shown |
| Confounds | BM-C-01 brief engineers DETECTED; non-production framing removes the only mechanism that caught Test A's failure; all three runs chose atmospheric-expressive, motion 4, density 3, and PRN-0001; Archivo convergence | K1 to K4; PRN-0001 and Archivo noted | **Agreed.** Also recorded: 3/3 atmospheric-expressive with identical motion/density bands (a convergence the per-project fingerprint cannot see), and that removing Level 2 is the design of BM-C, not a defect |

No disagreement remains unreconciled, so the outcome is not `UNRESOLVED` (`loop.md` §8). The reconciliation reversed one of the draft's central conclusions (C1 impact); that reversal is recorded in §8 item 3.

## 15. Conclusions

1. **C1 is two claims, and the benchmark confirms both, with limits:**
   - **(a) Coverage.** No step checks that a committed direction's declared dimensions reach the render on the HYPOTHESIS / NOT DETECTED path. Reproduced in text and in 2 of 2 runs on that path: CONFIRMED GAP.
   - **(b) Impact.** A declared dimension without a rendered carrier ships unnoticed when Level 2 does not run. Reproduced in a second project (BM-C-02: materiality with no carrier, color and typography partial). That makes 2 of 3 HYPOTHESIS-path generations overall: CONFIRMED GAP. The failure is milder than External Test A's, and n is small.
   - **Relation to the audit:** the audit's C1 stands. Its priority (MUST INVESTIGATE NEXT) is supported. Its phrase "the common case" remains a small-n claim.
2. **B1 (first-entry axis 3) is confirmed as a SPECIFICATION AMBIGUITY** that produces inconsistent behaviour (1 numeric of 5 readings). The majority behaviour already matches the proposed clause, so the clarification is low-risk and codifies practice.
3. **B2 (axis-3 label) is supported as a SPECIFICATION AMBIGUITY.** Giving the critic the verbatim definitions removed the External Test A axis-3 disagreement and placed the category concern in axis 1 (n = 1).
4. **LAYOUT-009 separation held on the HYPOTHESIS path.** Its one activation came from a benchmark-engineered sentence (EXPECTED BEHAVIOR; the direction/concept boundary is a DEFERRED observation).
5. **A mandated category palette:** suggestive (both black-and-red builds left a material claim without a carrier) but confounded with subject. No systematic conclusion.
6. **The proposed carrier diagnostic is useful and not redundant,** but needs the guards in §8 item 5 before any wording is authorized; the most important is that a missing carrier leads to retraction or revision, never to added decoration.

## 16. Confirmed recurrence / non-recurrence

| Audit finding | Result in this benchmark |
|---|---|
| C1 coverage (no carry-through check) | **Recurs** (HYPOTHESIS path, 2/2) |
| C1 impact (silent carry-through failure) | **Recurs** in a second project, milder (BM-C-02: 1 dimension with no carrier, 2 partial; BM-B-01 none) |
| B1 first-entry axis 3 scored | **Does not recur in behaviour** (0/3 builds); the ambiguity recurs as inconsistency across runs (1/5 overall; K1) |
| B2 axis-3 label ambiguity | **Recurs** when a critic works from the label; **resolved** when the critic has the definitions (n = 1) |
| H1 category pressure under mandated palette | Not testable at n = 1; builder avoided the cluster-2 ground but kept condensed heavy caps |
| D1 / PT-20 (what runs after REFINE) | **Recurs** as inconsistency: Level 1 re-run in 2/3 builds, not in BM-B-01 |
| G1 heuristic false positives | **Recurs** (BM-B-01 INTX-003 heuristic flagged padded pill buttons; verified false positive) and is handled per case: consistent with EXPECTED BEHAVIOR |
| H5 evidence loss | **Closed for these runs** (brief, invocation, raw transcript, pre-REFINE screenshots preserved) |

## 17. What remains evidence-insufficient

1. **C1 impact frequency** without K2/K3, and with more than one subject under a mandated palette. This needs briefs that do not ask for carry-through and builders that do not know which dimensions will be inspected.
2. **Box-ticking risk of the diagnostic.** Measurable only with the diagnostic in the protocol. Out of scope; it would need an authorized trial on a disposable copy.
3. **What Level 2 actually receives.** No Level 2 ran; External Test A's Level 2 brief is lost.
4. **Mandated-palette effect.** One run.
5. **B1 interpretation rate without K1.** The builders' `not assessable` may be partly primed.
6. **Cross-project typeface convergence** (Archivo in 3 of 4 generations). Observation only; the causes (model default, TYPE-002 procedure, reference-free pools) are not separable here.
7. **PRN-0001 adopted in 3 of 3 builds.** Whether one pool entry is becoming a default is not assessable from three runs.

## 18. Explicit non-changes

Based on this evidence, the following **should not** be changed:
1. **No implementation of C1 in this milestone,** and no new rule. Any wording needs its own authorization and must carry the §8 guards (distinguishing carrier, retraction not decoration, non-blocking).
2. **No change to LAYOUT-009's activation or to the DETECTED definition** from this benchmark alone. The one activation came from a benchmark-engineered sentence.
3. **No cross-project fingerprint or typeface tracking.** §6's per-project scope is a deliberate design decision, and one observation does not justify revisiting it.
4. **No change to the principle pool or visual references** because PRN-0001 was adopted 3/3.
5. **No new anti-slop entry** for combat-sports conventions or condensed display type.
6. **No new score semantics.** Neither B1 nor B2 needs any; both reuse `not assessable` and existing definitions.
7. **No change to Level 2 triggers.** The explicit non-production framing worked as a control, with no need for a mechanism change.
8. **No change to the skill or its installed copy.** None was made.

## 19. Recommended next milestone

**Recommendation (requires human authorization; not authorized here):** *Targeted Specification Clarification: critique semantics*, text-only, in `critique-protocol.md`:
- **B1:** a first-generation axis-3 clause (`not assessable: first Fingerprint History entry`) codifying the majority behaviour.
- **B2:** Level 2 briefs carry each axis's definition.
- **C1:** the carrier question in axis 1, with the §8 guards:
  - the carrier must distinguish the committed direction from the rejected one;
  - an absence-defined dimension is satisfied by the absent treatment;
  - the outcome of "no carrier" is revise or retract, never decorate;
  - it stays non-blocking;
  - it is also carried into Level 2 briefs.

All three sit in the same file, reuse existing statuses and vocabulary, and need no new rule id, score or stage. That milestone should then re-run the three benchmark briefs (with K1 and K2 removed) against the clarified text on a disposable skill copy, to measure box-ticking before the change is installed.

**Alternative:** a neutral-brief C1 benchmark first (no carry-through request, no dimension-logging instruction, a real-business framing, a second mandated-palette subject), then the clarification.

**Deferred:** A2, D1/PT-20 (inconsistency recurred here: Level 1 re-run in 2 of 3 builds), E1, F1, H2, the direction/concept boundary, cross-project typeface convergence.
