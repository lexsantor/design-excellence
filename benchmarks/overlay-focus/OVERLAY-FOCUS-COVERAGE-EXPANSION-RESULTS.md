# Overlay Focus Management — Coverage Expansion Benchmark — Results

## 1. Status

**COMPLETED.**

- **Verdict:** ONE OBSERVED FAILURE. There were 3 usable off-canvas navigation runs out of a target of 2–3, giving 15 assessable checks. 14 passed and 1 failed: behaviour 5(b) in run 1, only during the drawer's close transition.
- **Level 2:** not triggered in any run.
- **Independent review:** one fresh, read-only evaluator. Its FAIL was reproduced independently by the main agent; the builder's self-report missed it.
- **Repository state at start:** HEAD `1aac962`.

## 2. Authorization

**Human authorization (2026-09-27), recorded in `STATE.md` before any benchmark work:** "Autorizo Coverage Expansion Benchmark: Overlay Focus Management. Scope limitado a ejecutar unas pocas DE runs independientes centradas en navegación off-canvas que use un overlay/modal navigation pattern, en rutas donde Level 2 no se active, y evaluar los cinco comportamientos definidos en the Evidence Investigation. No autorizo cambios al Rule Catalog, Rule Authoring, Principle Pool, Integration Contract, runtime architecture, SKILL.md, loop.md ni adquisición de referencias."

**Delegation exception.** The human authorized 4 subagents for this milestone only: 3 builders and 1 independent evaluator. `loop.md` §9 normally caps a milestone at 3 (human answer: "Allow 4 agents"). The authorization covers no later milestone and no Rule Authoring.

## 3. Benchmark question

> Can current Design Excellence builds, routed without Level 2, independently produce the five overlay focus behaviours for an **off-canvas navigation** pattern?

The previous benchmark could not answer this. Its two usable runs were a dialog and a filter sheet, and its navigation run built a disclosure instead of an overlay.

The five fixed behaviours come from `benchmarks/discovery/OVERLAY-FOCUS-EVIDENCE-INVESTIGATION-RESULTS.md`:
1. Focus enters the overlay on open.
2. Focus stays contained while the overlay is modal.
3. Escape closes the overlay.
4. Focus returns to the trigger after closure.
5. (a) The background is inert while the overlay is open, and (b) the overlay's content is unavailable once it is closed.

## 4. Run inventory

**Set-up.**
- Three disposable **existing** projects were seeded outside the repository, in the session scratchpad. Each had plain HTML/CSS/JS, a `.design/context.md` (register, genre, dials, Product Truth, constraints, breakpoints) and **no overlay**.
- Each project was snapshotted with git, so the builder's changes could be isolated.
- Each builder was a fresh general-purpose agent. It received only the client's request and was told to follow the `design-excellence` skill's pipeline as the skill directs.
- **What builders could read:** only the skill's own files (`SKILL.md` and `references/`).
- **What builders could not read or use:**
  - benchmarks, reports, `STATE.md`, `loop.md`, `rules.md`, proposals, scratchpad or git history;
  - memory or history tools.

**Independence.**
- No request mentioned focus, keyboard, accessibility, modality or the benchmark.
- Each request asked for a panel or drawer "sliding in … over the page". That describes the visual pattern the client wants; it does not describe any interaction behaviour.
- Builds ran one after another because they shared one browser.

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| **Context** | mobile site navigation (bike workshop marketing site) | account/settings navigation (clinic scheduling app) | secondary/utility navigation (city news magazine) |
| **Request (abridged)** | "Below 900px, replace the link row with a Menu button that opens the navigation in a drawer sliding in from the right over the page, and keep 'Book a service' easy to reach." | "Below 960px, add a 'Settings menu' button above the page title that opens the settings sections in a panel sliding in from the left over the page." | "Add an 'All sections' button to the masthead that opens a side panel sliding in from the left over the page, listing every section … plus Newsletter, Archive, About us and Log in. It should work at every screen width." |
| **Seeded context** | existing; brand-led; atmospheric-expressive; dials 6/4/4 | existing; product-led; modern-minimal; dials 3/2/6 | existing; hybrid; editorial; dials 5/3/7 |
| **Builder's routing** | "component-scope BUILD on an existing project" | "component-scope BUILD on an existing project" | "component-scope BUILD on an existing project" |
| **Overlay built** | yes: class-toggled fixed drawer with a scrim and JS `inert` on the page content | yes: native `<dialog>` opened with `showModal()` (the existing sidebar is moved into it) | yes: native `<dialog>` opened with `command="show-modal"`, with a JS fallback |
| **Usable** | yes | yes | yes |

## 5. Level 2 routing evidence

Every builder classified its task as a component-scope BUILD on an existing project, and none ran Level 2. Each quoted `critique-protocol.md`: "Do not run Level 2 by default for BUILD at component/section scope, or for any POLISH task".

Each builder also reported that none of the escalation triggers applied:
- no production, brand-critical or high-traffic signal;
- not a REDESIGN;
- not an empty-project multi-page BUILD with a brand-quality bar;
- no Level 1 axis below 3.

| Run | Genericness | Hierarchy | Distinctiveness | Craft | Accessibility | Technical |
|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 4 | 4 | 5 | 5 |
| 2 | 4 | 4 | n/a | 4 | 4 | 5 |
| 3 | 4 | 4 | n/a | 4 | 5 | 5 |

The routing arose naturally. Level 2 was neither forced off nor steered.

## 6. Overlay implementation evidence

These facts come from the code diffs and were confirmed by rendered behaviour (§8).

- **Run 1.**
  - `nav.primary` becomes a fixed drawer below 900px: `transform: translateX(100%)` plus `visibility: hidden`.
  - Closing uses `transition: transform 220ms, visibility 0s 220ms`, so `visibility` becomes hidden only 220 ms after the close starts.
  - Opening sets `inert` on the logo, the header Book link, the Menu button, `main` and the footer, then focuses Close.
  - Closing removes `inert` at once, and focus returns to Menu after Escape, Close or a scrim click.
- **Run 2.**
  - Below 960px a "Settings menu" button opens a native `<dialog>` with `showModal()`. The existing `<aside>` is moved into the dialog and moved back on close.
  - Escape, inertness and focus return are left to the native dialog.
  - The dialog closes if the window widens past 960px.
- **Run 3.**
  - A native `<dialog>` opens with invoker commands (`commandfor` / `command="show-modal"`), with a JS fallback for browsers without them.
  - It contains 10 sections and 4 utility links.
  - Escape, containment and focus return are native.

## 7. Five-behaviour matrix

These are the independent evaluator's scores, reconciled in §8.
- **Run 1 and run 2:** tested at 375px.
- **Run 3:** tested at 1280px and at 375px, with identical results.
- **Every run:** tested on a first and a second open/close cycle, with no difference between them.

| Behaviour | Run 1 (drawer) | Run 2 (dialog panel) | Run 3 (dialog panel) |
|---|---|---|---|
| 1. Focus enters on open | PASS: Tab ×3 reached Menu; Enter put focus on the drawer's Close | PASS: Tab ×5 reached Settings menu; Enter put focus on Close | PASS: Tab ×3 reached All sections; Enter put focus on Close |
| 2. Focus contained while modal | PASS: 36 Tab and 36 Shift+Tab per pass (9 focusables) never focused page content | PASS: 36 Tab and 36 Shift+Tab (10 focusables) never focused page content | PASS: 36 Tab and 36 Shift+Tab (15 focusables) never focused page content |
| 3. Escape closes | PASS: Escape pressed on the 2nd drawer link closed the drawer | PASS | PASS |
| 4. Focus returns to trigger | PASS: after Escape and after Enter on Close | PASS: after Escape and after Enter on Close | PASS: after Escape and after Enter on Close, at both widths |
| 5(a). Background inert while open | PASS: only the `banner` that contains the nav stayed in the accessibility tree; all other page content was ignored | PASS: no non-ignored nodes outside the dialog | PASS: no nodes outside the dialog |
| 5(b). Closed content unavailable | **FAIL, during the close transition only.** Before first open and once the close has finished: no drawer nodes in the tree, and Tab sweeps never reached the drawer. For about 220 ms after closing starts, the drawer's links are reachable by Shift+Tab and exposed in the accessibility tree (§9) | PASS: no overlay nodes and no overlay focus before first open or after close, including Shift+Tab 6–33 ms after Escape | PASS: the same, including Shift+Tab 7–35 ms after Escape |
| **Behaviour 5 overall** | **FAIL** | PASS | PASS |

**Totals.**

| Run | Assessable checks | Failures |
|---|---|---|
| 1 | 5 | 1 (behaviour 5, part b) |
| 2 | 5 | 0 |
| 3 | 5 | 0 |

Across all three runs that is 15 checks, 14 passes and 1 failure. None were NOT ASSESSABLE.

**Criterion 2, fixed wording.** The criterion is applied exactly as in the previous benchmark: PASS means focus never reaches page content behind the overlay. In all three runs, `activeElement` was BODY with `document.hasFocus() === false` at the wrap point of each Tab cycle. That means focus had left the document for the browser's own interface. No page element was ever focused.

| Run | BODY steps, pass 1 | BODY steps, pass 2 |
|---|---|---|
| 1 | Tab #18, #28; Shift+Tab #8, #27 | Tab #9, #19, #29; Shift+Tab #7, #17, #27 |
| 2 | Tab #10, #21; Shift+Tab #5, #16, #27 | Tab #20, #31; Shift+Tab #5, #26 |
| 3 | Tab #15, #31; Shift+Tab #5, #21 | Tab #30; Shift+Tab #21 |

These steps are recorded as observations. They do not change the score.

## 8. Independent review

- **Evaluator.** One fresh, read-only general-purpose agent.
- **What it could read:**
  - `index.html`, `styles.css` and `app.js` in each project;
  - `git diff HEAD` for those files.
- **What it could not read:**
  - `.design/` (which holds the builders' own critique scores);
  - the builders' reports, which were moved to a withheld folder;
  - the repository;
  - memory tools.
- **Method.** It drove Chrome 154 through playwright-core with real `page.keyboard.press` input: Tab from a fresh page load, then Enter to open. It sampled `document.activeElement` after every key, and read the accessibility tree through CDP (`Accessibility.getFullAXTree`), resolving each node to its DOM element.
- **Clean-up.** It modified no project file; `git status --short` was identical before and after in all three projects. It created no `.playwright-mcp` folder and stopped its servers.

**Reconciliation with the builders' self-reports.**
- **Runs 2 and 3:** the builders reported the same passing behaviours. There is no disagreement.
- **Run 1:** the builder reported that Esc closed the drawer "and re-hides the drawer". The evaluator found the closed drawer still reachable during the close transition.
  - The main agent reproduced this with its own script. At 375px it opened the drawer by keyboard, pressed Tab twice, pressed Escape, then Shift+Tab three times with no wait.
  - Result: +4 ms, the header "Book a service" (page); +7 ms, the drawer's "Book a service" (**overlay**); +8 ms, the drawer's "Visit us" (**overlay**).
  - With a 400 ms wait before the Shift+Tabs, focus went only to page elements.
  - The same probe with no wait never reached overlay content in runs 2 and 3.
  - The code shows the cause (§9). The FAIL is confirmed, and the evaluator's score stands.
- **Criterion 2 BODY steps:** the evaluator's PASS is kept, under the fixed wording.

## 9. Observed failures

**Run 1, behaviour 5(b): the closed drawer's content stays available during the close transition.**

**Cause.** When the drawer closes:
- the `is-open` class and `aria-expanded="false"` change at once;
- `inert` is removed from the page at once;
- the drawer itself was never made inert;
- `visibility: hidden` is applied only after a 220 ms delay (`transition: … visibility 0s 220ms`).

So for about 220 ms the "closed" drawer is still visible, focusable and in the accessibility tree.

**Evidence (evaluator).**
- Escape, then Shift+Tab at +7 ms, reached the header Book link. A second Shift+Tab at +10 ms landed on the drawer's "Book a service", then "Visit us", then "Journal".
- With about 90 ms between presses, the second Shift+Tab, at +199 ms, still landed in the drawer. With 120 ms between presses it did not, because the second press came at +278 ms.
- When the window ends, whatever is focused inside the drawer is hidden, and focus drops to BODY.
- 32 ms after Escape, the accessibility tree still exposed Close, the drawer's "Book a service" and all 7 drawer links.

**Reach.** Triggering it takes two quick Shift+Tabs, or an assistive technology reading the tree, within about 220 ms of closing. The normal, slower keyboard flow does not hit it. It is still a real, reproducible failure under the fixed wording: after closing, the drawer's content is reachable by Tab and exposed in the accessibility tree.

**Observed-but-not-scored edges.**
- **Run 1:**
  - Following a drawer link by keyboard closes the drawer but leaves focus on BODY; the code closes it without restoring focus.
  - Clicking empty space inside the open drawer drops focus to BODY.
  - Widening the window past the breakpoint while the drawer is open closes it and leaves focus on BODY.
- **Run 2:** widening past 960px closes the dialog. Focus ends on BODY because the trigger is hidden at that width.
- **Runs 2 and 3:** activating a link (href="#") leaves the dialog open. This is not one of the five behaviours.
- **Runs 1–3:** Escape pressed while focus was on BODY during the open state also closed the overlay and returned focus to the trigger.

## 10. Evidence limitations

- **Sample size.** 3 runs and 15 assessable checks: one small sample, one model family, and builders working without a human.
- **Browser.** One engine, Chromium (Chrome 154). Run 3 relies on native invoker commands. Its JS fallback, used by browsers without invoker commands, was not exercised.
- **Seed projects.** Small plain-HTML projects. The requests named the visual pattern (a panel "over the page"). That was needed to get genuine off-canvas overlays, but it makes overlays more likely than a free choice would.
- **Timing-dependent failure.** The run 1 failure appears only in a timing window. Whether a test finds it depends on probing during the close transition.
- **Builders' own VALIDATE.** Every builder tested its overlay by keyboard, unprompted, as part of the skill's VALIDATE stage. The run 1 builder's checks did not cover the close-transition window.
- **No population claim.** Three runs support an observed signal, not a frequency estimate.

## 11. Comparison with the previous two-run benchmark

| | Previous (`OVERLAY-FOCUS-BEHAVIOURAL-BENCHMARK-RESULTS.md`) | This benchmark |
|---|---|---|
| Usable overlay runs | 2 of 3 (dialog, filter sheet) | 3 of 3 (all off-canvas navigation) |
| Off-canvas navigation covered | no (run 3 built a disclosure) | yes |
| Assessable checks | 10 | 15 |
| Failures | 0 | 1 (run 1, 5(b), close transition) |
| Level 2 triggered | no | no |
| Criterion 2 wording | fixed; BODY steps observed | same fixed wording; BODY steps observed |

**Method asymmetry.** This evaluator probed the close-transition window; the previous one did not.
- The previous run 2 filter sheet used the same pattern as run 1 here: `visibility: hidden` delayed by 250 ms on close, with `inert` removed at once.
- It may therefore have had the same latent transition-window exposure. It was not probed, and it is **not** re-scored here: the previous results stand as recorded.
- As a result, "0 failures before, 1 failure now" should not be read as a regression. The difference may come partly or wholly from the deeper probe.

## 12. Frequency signal

**A weak signal exists, but it is not a frequency estimate.**
- Across the two benchmarks there are 5 usable overlay runs and 25 assessable checks, with 1 observed failure.
- That failure is confined to one sub-part (5(b)), one implementation style (a class-toggled drawer with delayed `visibility`) and a timing window of about 220 ms.
- The four other behaviours passed in all 5 runs.
- Native-`<dialog>` implementations passed every check in both benchmarks: 1 run before and 2 here.

The data can support one bounded statement: current builds routed without Level 2 reliably produce behaviours 1–4, and can ship a transient closed-state exposure when a custom drawer animates `visibility`. The sample cannot say how often that happens.

## 13. Rule Authoring question

**It remains open and unauthorized.**
- The coverage gap still stands: no Rule Catalog entry names the five behaviours (Evidence Investigation §4).
- This benchmark adds one confirmed, narrow failure mode: closed-state availability during an exit transition.
- Whether that justifies Rule Authoring, a wider benchmark, or accepting the current state is a human decision.
- No rule is authored or proposed in the repository by this milestone.

## 14. Scope compliance

- **No changes to:**
  - the Rule Catalog (A11Y-002 included);
  - `critique-protocol.md`, `SKILL.md`, `loop.md` or the Principle Pool;
  - the Integration Contract;
  - runtime architecture.
- **No Rule Authoring and no reference acquisition.**
- **No benchmark rule and no permanent harness.**
- **Builders and the evaluator did not see:** the five behaviours (builders only), benchmark reports, `STATE.md`, `loop.md` or previous findings.
- **Disposable and not committed:** seed projects, builds, builder reports, evaluator scratch and the main agent's reconciliation probe. All of these stay in the session scratchpad, outside the repository.
- **`.playwright-mcp`.** Builders 1 and 3 reported that their browser tools created a `.playwright-mcp` folder in the repository root, and that they removed it. Repository `git status` shows no such folder.
- **Pre-existing untracked files are not included:** `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md`, `rules.md` and `scratchpad/`.

## 15. Files changed

- `STATE.md`: modified (milestone, authorization, objective, hypothesis, iteration, status, blockers, pending gate, next action).
- `benchmarks/overlay-focus/OVERLAY-FOCUS-COVERAGE-EXPANSION-RESULTS.md`: created (this report).

## 16. Commit hash

The hash is reported in the milestone's final response, since a commit cannot contain its own hash. The commit contains only the two files above. Nothing was pushed.
