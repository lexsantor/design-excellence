# Behavioural Residue Benchmark — Results

**Status:** COMPLETED. Hypothesis **NOT SUPPORTED** by this sample (one partial failure in one of six classes).
**Authorization:** AUTHORIZED FOR READ-ONLY BENCHMARK (`STATE.md`, human-authorized 2026-09-27). Autonomous milestone under `loop.md`.
**Scope:** behavioural benchmark of Design Excellence exactly as it exists at HEAD `797170c`. No skill file, rule, principle, reference, contract, catalog or library was changed; nothing was remediated; no failure was fed back into the system. The external catalog was not used as runtime input and no catalog-derived guidance was introduced.

**Labels.** **[DOC]** measured or read in an artifact. **[INF]** inference by this benchmark.

Identity boundary: tasks were written fresh for this benchmark; they do not reuse catalog observation language, and this report carries no source identity. Residue classes refer to R1–R16 of `benchmarks/rejected-residue-coverage-audit/REJECTED-RESIDUE-COVERAGE-AUDIT-RESULTS.md`.

---

## 1. Objective

Test whether Design Excellence actually produces failures corresponding to the documented uncovered, in-remit residue identified by the completed audits.

## 2. Hypothesis

The documented gap is behaviourally meaningful: when Design Excellence is used on representative product-UI tasks, the absence of guidance for the uncovered classes will produce observable design or implementation failures.

## 3. Method

1. **Criteria fixed first.** Six tasks and 24 success criteria were written and hashed before any build, in disposable material outside both repositories.
2. **Builds.** Two fresh implementer agents each built three tasks. Each invoked the `design-excellence` skill and followed it normally. They saw only the task text: not the criteria, the residue, the expected failures or the purpose of the benchmark. Deviations from a normal run: no human was available, so the skill's questions were answered with stated assumptions; implementers were told not to spawn subagents and not to use the web.
3. **Deliverable.** One self-contained `index.html` per task (inline CSS/JS, no dependencies), plus the skill's own `.design/context.md`.
4. **Evaluation.** Scripted headless Chrome runs at 1440×900 and 390×844: overflow, off-screen elements, visibility, interaction sequences and outputs. Code reading confirmed mechanisms.
5. **Independent review.** One blind reviewer judged every criterion (§8).
6. No result was remediated.

All six skill runs routed as page-scope BUILD on an empty project: full pipeline without AUDIT (DIRECT/EXPLORE with a logged rejected direction, SHAPE, DESIGN, BUILD, VALIDATE, Level 1 critique, REFINE, SHIP). Level 2 critique did not trigger. HARDEN was skipped as prototype scope in one implementer's runs and folded into VALIDATE in the other's. [DOC: implementer reports]

## 4. Test matrix

| Test | Class (residue) | Task (fresh) | Criteria |
|---|---|---|---|
| T1 | Responsive reflow (R1, R3, R4) | bike-rental operations dashboard with persistent nav, KPI tiles, 14-day chart, rentals table | C1.1 no document overflow at 390; C1.2 nav not a side column at 390; C1.3 no KPI tile or chart clipped or cut off (scroll container allowed for the table only); C1.4 desktop sanity |
| T2 | Collection / selection state (R8, R9) | stationery inventory list with search, filter, sort, 10/page, checkboxes, select-all, bulk archive/delete | C2.1 bulk actions hidden with no selection; C2.2 hidden rows never stay selected silently; C2.3 filtering from a later page shows results; C2.4 select-all scope unambiguous |
| T3 | Conditional forms (R10, display half of R11) | home-cleaning booking with one-off/recurring, key handover, business-only invoice, free-first-cleaning promo | C3.1 frequency and concierge shown only when relevant; C3.2 hidden fields not required; C3.3 invoice not usable by non-business customers; C3.4 no card details required when nothing is due |
| T4 | Comparison display (R12, R13) | compare 1–4 of 8 scooters (data supplied, including deliberate ties) | C4.1 no marks with one model; C4.2 correct better-direction; C4.3 ties not given a sole winner; C4.4 colours unranked; C4.5 marks relative to the selection |
| T5 | Linked views (R15, R16) | warehouse bay map plus bay list with status colours, filter, search | C5.1 shared selection both ways; C5.2 map reflects filter; C5.3 no stale text when the selection is filtered out; C5.4 selection distinct from status colours |
| T6 | Recommendation explanation (R6) | cloud-backup plan picker (plans supplied) | C6.1 explained, not just named; C6.2 names the deciding constraint using the user's values; C6.3 cheapest sufficient plan (3 cases); C6.4 over-limit input handled explicitly |

Not tested, as outside the skill's remit: R5, R7, R14, and the shared-function half of R11.

## 5. Results

| Criterion | Main agent | Reviewer | Final | Evidence [DOC] |
|---|---|---|---|---|
| C1.1 | PASS | PASS | **PASS** | document scrollWidth = clientWidth at 390 and 1440 |
| C1.2 | PASS | PASS | **PASS** | at 390 the nav is a static 390×51 top bar |
| C1.3 | PASS | FAIL | **FAIL** | at 390 the 14-day chart sits in a horizontal scroll region (client width 324, content width 720; a narrow-breakpoint rule sets the chart's minimum width to 720); about 6 of 14 days are visible without scrolling |
| C1.4 | PASS | PASS | **PASS** | sticky side nav at 1440, no overflow |
| C2.1 | PASS | PASS | **PASS** | bulk bar hidden at 0 selected |
| C2.2 | PASS | PASS | **PASS** | search and filter are hidden while rows are selected; any search, filter or view change clears the selection |
| C2.3 | PASS | PASS | **PASS** | page 4 (8 rows), then a category filter, shows 7 rows; page reset and clamp in code |
| C2.4 | PASS | PASS | **PASS** | "All 10 on this page are selected. Select all 38"; header checkbox labelled for page scope |
| C3.1 | PASS | PASS | **PASS** | frequency and concierge visible only in their conditions (all four combinations, reviewer) |
| C3.2 | PASS | PASS | **PASS** | a one-off booking with the home option submits without frequency or concierge |
| C3.3 | PASS (judgement) | PASS (judgement) | **PASS** | invoice option visible but disabled for private customers, with "Business customers only" |
| C3.4 | NOT ASSESSABLE | PASS (vacuous) | **NOT ASSESSABLE** | the page never collects card details, so the tested condition cannot occur (§9) |
| C4.1–C4.5 | PASS | PASS | **PASS** (5) | one model: no marks; direction correct; 55 = 55 range tie unmarked, "Same for all"; a partial warranty tie marked "Tied best" on both; colours "Not ranked"; marks recomputed per selection |
| C5.1–C5.4 | PASS | PASS | **PASS** (4) | selection mirrored between map and list; filter dims 18 of 24 bays; a filtered-out selection shows "This bay is hidden by the current search or filter"; selection is a double ring, status is fill colour or a dashed border |
| C6.1–C6.4 | PASS | PASS | **PASS** (4) | "Why not a cheaper plan?" names each cheaper plan's shortfall beside "You need …" values; 3/3 cases correct; 60 devices gives "No single plan covers this" |

**Totals:** 22 PASS, 1 FAIL, 1 NOT ASSESSABLE. No page errors at either viewport in any test.

### Observations outside the criteria' wording (not counted as verdicts)

- **T3:** when the first cleaning is free, card is still preselected, the page promises a card step later, and the confirmation says "Paying by card". Card entry is deferred, not waived. This is close in spirit to R10's "no payment form when nothing is charged". [DOC, reviewer]
- **T3:** a promo code typed but not applied is ignored at submit (code reading only). [DOC, reviewer]
- **T2:** selections on other pages persist while paging and are reported only as "N selected". Mitigated: the delete confirmation lists item names, and archive can be undone. [DOC, reviewer]
- **T6:** the over-limit message states both values but does not say which one exceeds the largest plan. [DOC, reviewer]
- **T1:** `overflow-x: clip` on html/body could hide real overflow from a document-width check. Element scans found none. [DOC]

## 6. Answers

- **Classes tested:** all six in-remit classes, one primary task each.
- **Classes with observable failures:** **responsive reflow**, on one criterion: the chart becomes a horizontally scrolled strip at phone width instead of reflowing. It was implemented deliberately, as a labelled, focusable "scrollable" region, not as accidental clipping. Near-misses outside the criteria, in conditional forms (card still implied at €0) and explanation copy (over-limit input not named), are recorded as observations only.
- **Classes that passed:** collection/selection state, comparison display, linked views, recommendation explanation (all criteria), and conditional forms (all assessable criteria).
- **Not assessable:** C3.4 only.
- **Reproducible within the tested task:** yes, for the one failure. It follows from a fixed CSS rule, and the main agent and the reviewer measured it independently. Whether a new build of the same task would reproduce it was not tested (one build per class).
- **Behavioural gap?** The evidence does **not** support treating the documented gap as a broad behavioural gap. In five of six classes the current system produced behaviour that met every assessable criterion, without any rule covering those classes. The one failure is partial and could be judged a defensible trade-off. [INF] The documented gap looks largely like a gap in written guidance, not in model behaviour, for tasks of this kind.
- **Unknown:**
  - variance across repeated builds (n = 1 per class);
  - behaviour inside existing projects (every test was a greenfield page);
  - behaviour under POLISH or section scope, or under time pressure;
  - larger or messier data;
  - other frameworks;
  - whether skipping HARDEN in half the runs affected results.
- **Governance decision?** The evidence does not justify opening a governance decision on a new guidance path now. The strongest candidate, responsive reflow of wide content at narrow widths, rests on a single partial failure. Further evidence would be needed first; see §11.

## 7. Limitations

- One build per class, one model family, greenfield single-file pages, fresh data supplied or invented by the implementer.
- The criteria were written by the main agent and some are judgement-bearing (§9). They test the residue's failure conditions, not overall design quality.
- Implementers answered the skill's questions themselves (no human). Their runs also validated in a browser as part of the skill's own VALIDATE step, which may have caught failures a less thorough run would ship.
- **Harness defect (main agent):** the T1 off-screen scan exempted every horizontal scroll container, not only the table's as C1.3 specifies. This hid the chart failure until the reviewer caught it.
- The residue observations came from commercial templates, not from Design Excellence runs. These tasks test the same failure conditions, not the same artifacts.

## 8. Independent review (`loop.md` §8)

One fresh, blind, general-purpose reviewer. Received: the task texts, the 24 criteria, the six artifacts, and the raw measurement JSON, screenshots and scripts (measurements only, no verdicts). Withheld: the main agent's verdicts (recorded and hashed before the reviewer ran), the residue classification and the audits, rejection history, and the expected failures. Disclosure note: the criteria necessarily reveal what each test checks; the reviewer was not told why. It wrote only its own scripts and crops in a designated disposable folder and modified no artifact.

Reviewer result: 23 PASS, 1 FAIL (C1.3). It ran its own checks for C1.3, C3.1 (all four combinations), C3.2, C5.2 (a search case) and C5.4 (ring crops), and reported the observations in §5 and the ambiguities in §9.

## 9. Disagreements and reconciliation

| Criterion | Main agent | Reviewer | Reconciliation |
|---|---|---|---|
| C1.3 | PASS | FAIL | **Reviewer adopted.** Re-measured: at 390 one scroll region overflows (324 of 720) and it holds the chart, not the table. The main agent's scan wrongly exempted all scroll containers. |
| C3.4 | NOT ASSESSABLE | PASS (literal, vacuous) | **NOT ASSESSABLE kept.** The criterion tests whether card details are required at €0, but the page has no card-detail fields, so the condition cannot arise. Both agents agree nothing fails literally, and both note the deferred-card concern in §5. |
| C3.3, C6.2 | PASS (judgement) | PASS (judgement) | Same verdict. The wording leaves a judgement (a disabled but visible option; the user's value beside the deciding sentence rather than inside it), recorded as ambiguity. |

Criteria the reviewer found ambiguous: C1.3 (is a chart in a scroll container "clipped"?), C2.2 (designs that block filtering during selection), C3.3, C3.4, C4.3 (partial ties among three or more), C5.4 ("distinct" not quantified), C6.2. None changes a verdict except as reconciled above.

No material disagreement remains.

## 10. Process deviations (recorded, no governed impact)

- One implementer's browser tool briefly wrote a `.playwright-mcp/` folder into the control-plane repository root and deleted it. `git status` afterwards showed only the expected `STATE.md` change.
- The other implementer briefly wrote a file to the system temp root and deleted it.
- The `STATE.md` "Authorization scope" paragraph still describes READ-ONLY AUDIT permissions; this benchmark's permissions came from the human instruction and `loop.md` §2. The paragraph was not edited, as that is a governance field.

## 11. Next unresolved question

Is the single responsive-reflow failure an instance of a systematic tendency (wide content such as charts given a fixed minimum width and horizontal scroll at phone width), or a one-off design trade-off? And do the passing classes stay passing across repeated builds and in existing-project or POLISH contexts?

## 12. Next action (human authorization required)

No milestone is authorized. Options, unranked:

- **(a) Accept.** Treat the documented gap as largely non-behavioural for now; no further milestone.
- **(b) Authorize a bounded replication** of the responsive-reflow class only (several independent builds, same fixed criteria, the scan defect corrected) to see whether the failure recurs.
- **(c) Authorize a governance decision anyway**, on the documented gap alone. This benchmark does not supply behavioural support for it.

## 13. Files changed

- `benchmarks/behavioural-residue-benchmark/BEHAVIOURAL-RESIDUE-BENCHMARK-RESULTS.md` (added; this report).
- `STATE.md`: milestone fields set by explicit human authorization before execution; then operational fields only.

## 14. Files not changed

`loop.md`; everything under `design-excellence/` (`SKILL.md`, Rule Catalog, `principle-pool.md`, `visual-references.md`); all other benchmarks; `rules.md`; `scratchpad/`; the Integration Contract; the external catalog; every reference library. The six artifacts, criteria, scripts and measurements remain disposable material outside both repositories and are not committed.
