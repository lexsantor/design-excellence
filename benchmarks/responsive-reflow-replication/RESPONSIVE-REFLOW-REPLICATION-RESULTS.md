# Responsive Reflow Replication — Results

**Status:** COMPLETED. Mechanism present in **0 of 3** builds. Hypothesis **NOT SUPPORTED**; the earlier failure is best read as **isolated**.
**Authorization:** AUTHORIZED FOR READ-ONLY BENCHMARK (`STATE.md`, human-authorized 2026-09-27). Autonomous milestone under `loop.md`.
**Scope:** behavioural replication of Design Excellence exactly as it exists at HEAD `e1733a3`. No skill file, rule, principle, reference, contract, catalog or library was changed. Nothing was remediated, and no build's outcome was fed to another. The external catalog was not used.

**Labels.** **[DOC]** measured or read in an artifact. **[INF]** inference by this milestone.

---

## 1. Objective

Determine whether the single responsive-reflow failure observed in the completed Behavioural Residue Benchmark represents a repeatable behavioural tendency of Design Excellence or was a one-off design trade-off.

## 2. Hypothesis

Design Excellence systematically tends to keep wide content (charts or similar wide visualizations) at a fixed or excessive minimum width inside a horizontal scrolling region at narrow viewports, instead of adapting it, when the task requires the content to remain meaningfully usable on a narrow viewport.

**Prior failure being replicated** [DOC, Behavioural Residue Benchmark §5, C1.3]: at 390 px a 14-day bookings chart kept a fixed minimum width of 720 px inside a labelled, focusable horizontal scroll region (324 px visible), so about 6 of 14 days were visible without scrolling. Recorded limitations: one build; the criterion wording ("clipped") was ambiguous about deliberate scroll regions; the main harness initially exempted all scroll regions.

## 3. Experimental design

- **Three fresh tasks** in different domains, each posing the same problem: a naturally wide primary visualization, an app shell with primary navigation, and an explicit statement that users rely on phones. No task mentions responsiveness, charts adapting, prior benchmarks or catalog material.
- **Frozen first:** tasks and rubric were written and hashed before any build (§4).
- **Builders:** two fresh implementer agents used the `design-excellence` skill normally and saw only their task text. `loop.md` §9 caps subagents at 3 including the reviewer, so one implementer built B1 and B2 as separate projects and the other built B3. The two equivalent chart tasks (B1, B3) therefore came from independent agents. B2 shares an agent with B1 (§14).
- **Measurement:** one generic probe at 1440×900 and 390×844, which reports every horizontal scroll region instead of exempting it (the earlier harness defect), plus targeted checks per build.
- **Independent review:** one blind reviewer (§12). One build per task, no retries; no technical failures occurred.

## 4. Frozen criteria and criteria hash

Frozen file SHA-256: **`153ba9a598a85ed73dca8b7f95d5b12b295190b4589aea73b2556edf640bc329`** (disposable, outside both repositories; recorded 2026-09-27 00:35, before any build).

| Id | Criterion |
|---|---|
| R1 | Desktop integrity at 1440: the primary visualization renders fully, no document overflow, no page errors |
| R2 | At 390: documentElement.scrollWidth ≤ clientWidth + 1 |
| R3 | At 390: primary navigation is not a desktop side column beside the content |
| R4 | At 390: ≥ 80% of the visualization's data categories are visible in the initial view or conveyed by a narrow-specific alternative; visualization text ≥ 10 px |
| R5 | FAIL if at 390 the visualization keeps a fixed or minimum width greater than the viewport that causes a horizontal scroll region, unless R6 justifies it |
| R6 | If a scroll region holds the visualization: JUSTIFIED only if (a) a genuinely continuous surface needs the width and the task makes scanning it appropriate, (b) the scroll is communicated, and (c) the rest of the page is coherent |
| R7 | No important content silently clipped or placed outside the usable viewport |

**Build classes:** PASS / FAIL / NOT ASSESSABLE / TECHNICAL FAILURE.
**Target mechanism M:** R5 fails and R6 is NOT JUSTIFIED.
**Replication rule:** M in ≥ 2 of 3 → REPEATED FAILURE; in exactly 1 → ISOLATED FAILURE; in 0 → NOT SUPPORTED; indistinguishable → UNRESOLVED.

## 5. Task summaries

| Build | Domain | Primary wide content | Stated device context |
|---|---|---|---|
| B1 | electricity supplier customer portal | daily kWh for the last 30 days against the same 30 days last year, with total, average and highest-use note | most customers on phone, some on laptop |
| B2 | physiotherapy practice room schedule | 5 rooms × 08:00–19:00, appointments of 30 or 45 minutes with initials, therapist and treatment | reception on desktop, therapists on phone |
| B3 | café bookkeeping cash-flow report | money in vs out for 12 months with running bank balance, totals, best and worst month | owner mostly on phone, accountant on desktop |

## 6. Build matrix

| Build | Implementer | Skill route [DOC, implementer reports] | Artifact |
|---|---|---|---|
| B1 | agent 1 (first of two projects) | page BUILD, empty project: full pipeline without AUDIT; Level 1 critique; HARDEN skipped (prototype); Level 2 not triggered | single `index.html` |
| B2 | agent 1 (second project) | same | single `index.html` |
| B3 | agent 2 | same; contrast fixes and three screenshot-driven fixes during VALIDATE | single `index.html` |

## 7. Measurements

| | B1 | B2 | B3 |
|---|---|---|---|
| Document width at 1440 / 390 | 1440/1440 · 390/390 | 1440/1440 · 390/390 | 1440/1440 · 390/390 |
| Elements past the viewport, outside scroll regions (both widths) | 0 | 0 | 0 |
| Primary visualization at 390 | SVG chart in a 358 px figure, `min-width: 0`, not in a scroll region | per-room vertical slot lists (the grid layout applies only from 64rem up) | HTML column chart 298 px wide, not in a scroll region |
| Data categories visible at 390 | 30/30 days (31 bar elements all inside the figure; narrowest bar 7 px) | 53/53 appointments in view; free periods listed | 12/12 months |
| Smallest visualization text at 390 | 12 px | 13 px | 11 px |
| Horizontal scroll regions at 390 | nav strip, 390 of 442 px ("Help" initially past the edge, with an edge fade) | none | month table, 356 of 511 px (`table{min-width:440px}` below 600 px, with a swipe hint) |
| Navigation at 390 | top bar (scrolling strip) | `<details>` Menu; opens full-width | `<details>` Menu; side nav from 960 px |
| Root overflow clipping | `html{overflow-x:clip}` | `html{overflow-x:clip}` | `html,body{overflow-x:clip}` |
| Page errors | none | none | none |

The root clip in all three means R2 alone could pass by construction. Both agents therefore also scanned for any element past the viewport outside a scroll region, at both widths, and found none.

## 8. Screenshots and evidence summary

Full-page and first-viewport screenshots were taken at both widths per build, plus raw probe JSON, targeted-check output and the reviewer's own scripts. They are held as disposable material outside both repositories and are not committed. Visual reading confirmed the measured states: B1's 30 bars with last year's line and the average line at both widths; B2's 5-column grid at 1440 and "Free rooms" plus per-room lists at 390; B3's 12 bar pairs above a balance line at both widths.

## 9. Implementation mechanisms

- **B1:** the chart is width-fluid (figure at 100%, `min-width: 0`) with 30 bars scaled to the available width. The full data is also available as a "Show all 30 days as a table" disclosure.
- **B2:** a layout switch at 64rem: CSS grid of 5 room columns above it, a free-rooms summary and per-room vertical slot lists below it. This is a narrow-specific alternative representation, not a compressed grid.
- **B3:** a fluid HTML column chart with year suffixes and smaller month labels below 720 px. The secondary table keeps a 440 px minimum width inside a scroll region with a phone-only swipe hint.

## 10. Classification per build

| Build | R1 | R2 | R3 | R4 | R5 | R6 | R7 | Class | M |
|---|---|---|---|---|---|---|---|---|---|
| B1 | PASS | PASS | PASS | PASS | PASS | n/a | PASS (judgement: nav strip item reachable by scroll, edge fade shown) | **PASS** | absent |
| B2 | PASS | PASS | PASS | PASS | PASS | n/a | PASS (three short free-gap times at 1440 are deliberate screen-reader-only text) | **PASS** | absent |
| B3 | PASS | PASS | PASS | PASS | PASS | n/a for the visualization | PASS (judgement: table columns start off-screen but are announced) | **PASS** | absent |

**Counts:** 3 PASS, 0 FAIL, 0 NOT ASSESSABLE, 0 TECHNICAL FAILURE.

## 11. Replication assessment

- **Mechanism M observed in 0 of 3 builds** → **NOT SUPPORTED** by this replication.
- Across all four comparable chart or wide-visualization builds (the earlier bookings chart plus B1–B3), a primary visualization was kept at a fixed minimum width in a scroll region once. [INF] That fits an isolated design trade-off better than a systematic tendency.
- **Strongest counter-evidence:** B2, the task where a scroll region would most plausibly have been justified (a time grid), was solved with a narrow-specific alternative representation instead.
- **Adjacent observation, outside M:** B3 applies the same technique (fixed minimum width plus a communicated scroll region) to its secondary data table. Together with the earlier chart, this shows Design Excellence does use fixed-minimum-width scroll regions for wide content at phone width, but in this sample only once for a primary visualization. Whether that is acceptable for secondary tables was not a question of this milestone.

## 12. Independent reviewer findings

One fresh, read-only, blind general-purpose reviewer received the three task texts, the frozen rubric, the three artifacts, the raw probe JSON and the screenshots. Withheld: the main agent's verdicts (hashed before review: `ee5f487e…`), the previous benchmark and its verdict, the residue audits, the expected failure and the hypothesis wording. The rubric necessarily defines M; the reviewer was not told it had occurred before.

Reviewer result: B1 PASS, B2 PASS, B3 PASS; M absent in all three; 0 of 3, NOT SUPPORTED.

Beyond the main measurements, the reviewer:
- confirmed that the root `overflow-x: clip` hides no overflow;
- opened the collapsed menus (all items inside the viewport);
- identified B2's hidden 1440 text as deliberate screen-reader-only content;
- corrected the probe's mis-picked elements (B2's viz, B3's hidden mobile nav);
- stated that B3's table would likely be NOT JUSTIFIED under R6(a) if R5/R6 applied to secondary content, which they do not as written.

## 13. Disagreements and reconciliation

None on any build class or criterion. Both agents flagged the same two judgement points under R7 (B1's scrolling nav strip, B3's table columns) and reached the same PASS reading. Rubric ambiguities raised by the reviewer and accepted as limitations (§14):
- R2 can be defeated by root clipping;
- R5/R6 cover only the primary visualization;
- R1's "renders fully" for tall content;
- R4's SVG text scaling (moot here: all labels are HTML);
- R3 does not require the collapsed nav to work (checked anyway).

## 14. Limitations

- Three builds; one per task; one model family; greenfield single-file pages with sample data.
- **Agent sharing.** B1 and B2 were built by the same implementer as separate projects, so they are not fully independent. B1 and B3, the two equivalent chart tasks, are independent.
- **Device statement.** Each task states that phone use is common, which is realistic product information but may prime responsive care more than the original bookings task did (it gave no device context). This could partly explain the difference from the earlier failure and is not separable with this design.
- **Builders' own checks.** Both builders checked their pages at narrow widths during VALIDATE, as the skill's process directs. The result reflects the full pipeline, not a first draft.
- **Rubric scope.** The rubric measures the target mechanism only, not overall design quality; R7 judgements are qualitative.
- **Harness.** The generic probe's visualization heuristic mis-picked elements in two builds. Targeted checks and the reviewer corrected for this; no verdict rested on the heuristic alone.

## 15. Whether the hypothesis is supported

**No.** The mechanism did not recur in any of three fresh, independent builds that posed the same responsive challenge.

## 16. Systematic, isolated or absent

**Isolated.** The earlier failure is not reproduced (0 of 3 here; 1 of 4 across comparable builds). It is not "absent" overall, because it did occur once, and the related technique appears on secondary tabular content (B3).

## 17. Should this line of investigation close?

**Yes, for the question asked.** Under the frozen replication rule the chart-reflow failure is not a repeatable tendency in this evidence, and the behavioural chain started by the audits (documented gap → behavioural benchmark → replication) has not produced support for a behavioural gap in responsive reflow. This report proposes no rule, architecture or governance change. Anything further would be a new, separately authorized question (§20).

## 18. Files changed

- `benchmarks/responsive-reflow-replication/RESPONSIVE-REFLOW-REPLICATION-RESULTS.md` (added; this report).
- `STATE.md`: milestone fields set by explicit human authorization before execution; then operational fields only.

## 19. Files not changed

`loop.md`; everything under `design-excellence/` (`SKILL.md`, Rule Catalog, `principle-pool.md`, `visual-references.md`, anti-slop, style, motion, accessibility and all other runtime knowledge); all other benchmarks, including the Behavioural Residue Benchmark report; `rules.md`; `scratchpad/`; the Integration Contract; the external catalog; every reference library. The three artifacts, frozen criteria, probe, measurements, screenshots and reviewer scripts are disposable material outside both repositories and are not committed.

## 20. Next unresolved question

No open question remains on the replicated mechanism. One adjacent question was observed but not tested: whether fixed-minimum-width scroll regions for **secondary** wide content (tables) at phone width are acceptable or a usability cost. It lies outside this milestone and would need its own authorization.
