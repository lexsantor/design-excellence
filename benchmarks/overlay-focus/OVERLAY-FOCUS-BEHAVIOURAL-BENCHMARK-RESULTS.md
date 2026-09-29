# Overlay Focus Management — Behavioural Benchmark — Results

**Status:** COMPLETED.
**Verdict:** NO OBSERVED FAILURE. Two usable overlay runs out of a target of 3; the third run built a disclosure, not an overlay.
**Level 2:** not triggered in any run.
**Independent review:** one fresh, read-only evaluator; reconciled with no disagreement.
**Repository state at start:** HEAD `46837a5`.

---

## 1. Authorization

**Human authorization (2026-09-27), recorded in `STATE.md` before any benchmark work:** "Autorizo Behavioural Benchmark: Overlay Focus Management. Scope limitado a ejecutar unas pocas DE runs independientes de tareas que incorporen overlays, en rutas donde Level 2 no se active, y evaluar los cinco comportamientos definidos en la Evidence Investigation. No autorizo cambios al Rule Catalog, Rule Authoring, Principle Pool, Integration Contract, runtime architecture, SKILL.md, loop.md ni adquisición de referencias."

**Delegation exception.** The human authorized 4 subagents for this milestone only: 3 fresh builders, one per run, and 1 fresh evaluator. `loop.md` §9 normally caps a milestone at 3 (human answer: "Allow 4 agents"). This is recorded in `STATE.md`.

## 2. Benchmark question

> Under current routes that do not trigger Level 2, how often does a Design Excellence build ship an overlay missing one or more of the five behaviours?

The five behaviours come from `benchmarks/discovery/OVERLAY-FOCUS-EVIDENCE-INVESTIGATION-RESULTS.md`:
1. Focus enters on open.
2. Focus stays contained while the overlay is modal.
3. Escape closes.
4. Focus returns to the trigger.
5. The background is inert while the overlay is open, and the overlay's content is unavailable while it is closed.

## 3. Run inventory

**Set-up.**
- Three disposable **existing** projects were seeded outside the repository, in the session scratchpad. Each had plain HTML/CSS/JS, a `.design/context.md` (register, genre, dials, constraints, breakpoints) and **no overlay** anywhere.
- Each project was snapshotted with git, so the builder's changes could be isolated.
- Each builder was a fresh general-purpose agent. It received only the user's request and was told to follow the `design-excellence` skill's pipeline exactly, and to read no files except the skill's own (`SKILL.md` and `references/`). In particular it was forbidden to read benchmarks, reports, `STATE.md`, `loop.md` or history.

**Independence.**
- No brief mentioned focus, keyboard, accessibility, overlays as a subject, or the benchmark.
- No temporary rule or context was added.
- The builds ran one after another because they shared one browser.

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| **Scenario** | project workspace page: "the Share button doesn't do anything yet. Add the share flow: clicking Share should open a dialog …" | shop listing: "on phones and tablets the filters … disappear completely. Add a Filters button … that opens the filter options in a panel sliding in from the side, with Apply and Clear actions" | library site: "our header navigation doesn't fit on phones anymore. Add a mobile menu …" |
| **Project state** | existing (product-led, modern-minimal) | existing (hybrid, editorial) | existing (hybrid, modern-minimal) |
| **Routing (the builder's own classification)** | "component BUILD on an existing project" | "section BUILD on an existing project" | "component-scope POLISH on an existing-requiring-polish project" |
| **Why Level 2 did not trigger** | component-scope BUILD, with no stakes signal and no Level 1 axis below 3 | section-scope BUILD (protocol: "Do not run Level 2 by default for BUILD at component/section scope") and no axis below 3 | POLISH ("or for any POLISH task") and no axis below 3 |
| **Level 2 absent** | yes | yes | yes |
| **Overlay implemented** | yes: native `<dialog>` opened with `showModal()`; modal | yes: off-canvas panel below 1024px with a scrim, `role="dialog"`, `aria-modal="true"`, and `inert` on the page content; modal | **no:** a disclosure (`aria-expanded`, `display:none`/`flex`, `position:static`) that pushes content down; not modal |
| **Usable for the benchmark question** | yes | yes | **no overlay.** The request did not prescribe one and the builder chose a disclosure, a legitimate design choice. Its applicable checks are reported separately and not counted as overlay evidence |

## 4. Behaviour matrix

These are the fresh evaluator's scores (§6), from real keyboard input, `document.activeElement` samples and the Chrome DevTools Protocol (CDP) accessibility tree.

| Behaviour | Run 1 (modal dialog) | Run 2 (off-canvas sheet) | Run 3 (disclosure; not an overlay) |
|---|---|---|---|
| Focus enters on open | PASS: Enter on Share put focus on the dialog's Close button | PASS: Enter on Filters put focus on the panel's close button | NOT ASSESSABLE (not applicable: a disclosure keeps focus on its toggle) |
| Focus contained while modal | PASS: 12 Tab and 12 Shift+Tab presses never reached page content (see the note) | PASS: Tab and Shift+Tab cycled panel controls only; background `inert` | NOT ASSESSABLE (not applicable: not modal) |
| Escape closes | PASS | PASS | PASS |
| Focus returns to trigger | PASS: after Escape and after the close control | PASS: after Escape, the close control and Apply | PASS |
| Background / closed overlay inert | PASS: (a) accessibility tree held dialog nodes only while open; (b) `display:none` when closed | PASS: (a) only the dialog was exposed while open; (b) `visibility:hidden` when closed, and Tab skipped it | PASS: (a) not applicable; (b) `display:none` when closed |

**Totals:**

| Run | Assessable checks | Failures | Failed behaviours |
|---|---|---|---|
| 1 | 5 | 0 | none |
| 2 | 5 | 0 | none |
| 3 (not an overlay) | 3 | 0 | none |

Across the usable overlay runs: 10 assessable checks, 0 failures.

**Note on criterion 2.** In runs 1 and 2, `activeElement` was BODY once per Tab cycle; no page element was ever focused. The criterion's own wording is "never reaching page content behind it", so this is PASS. The evaluator attributes the BODY step to the native `<dialog>` and to the headless browser letting focus leave the document, where a real browser would move it to its own toolbar. A stricter reading ("focus is always on an overlay element") would score both runs FAIL. The criterion was fixed before the runs, and its fixed wording is applied here.

## 5. Detection analysis

**No failures were observed, so no defect has a detection stage.**

For context only (from the builders' self-reports, which the evaluator did not see):
- Builders 1 and 2 checked focus behaviours themselves during VALIDATE.
  - Builder 1: initial focus, Escape, focus return.
  - Builder 2: focus in, Tab containment, Escape, focus return, page locked.
  - Neither was prompted to.
- Builder 3 explicitly chose a disclosure over "a full-screen overlay with focus trapping", reasoning that a six-link header does not need one.
- No behaviour was caught incidentally by another mechanism, because none failed.

**Observed-but-not-failing edges** (the evaluator's observations):
- **Run 2:** Escape is handled only when focus is inside the panel. With focus blurred to BODY, Escape did not close it. The normal keyboard flow never reaches that state, so criterion 3 stays PASS.
- **Run 3:** Escape on a disclosure is optional. If criterion 3 is treated as not applicable, run 3 has 2 assessable checks and 0 failures.

## 6. Independent review

- **Evaluator.** One fresh, read-only general-purpose agent.
- **Received:**
  - the three project folders (rendered by serving them locally);
  - `git diff` against the seeded state (the relevant code);
  - the five fixed criteria, with an instruction to score only what is observable and to use NOT ASSESSABLE where a behaviour cannot be established or does not apply.
- **Withheld:**
  - the builders' self-reports (moved to a separate folder the evaluator was told not to read);
  - their VALIDATE findings and self-critique;
  - the main agent's view.
- **What it did.** It modified no project file; `git status` was unchanged in all three runs. It deleted the `.playwright-mcp` folder its browser tool created.

**Reconciliation:**
- **Criterion 2 BODY step:** the evaluator's PASS is kept, under the fixed wording (§4 note).
- **Run 3 not an overlay:** agreed. It is reported as outside the overlay evidence (§3).
- **Run 2 blurred-focus Escape:** recorded as an observation, not a failure.

No disagreement remains.

## 7. Evidence limitations

- **Sample size.** 3 runs, of which **2 contained an overlay**. That gives 10 assessable overlay checks.
- **Unusable run.** Run 3 built no overlay, and no replacement run was made: the brief allows extra runs only after an execution failure, and the human authorized 4 agents. The three overlay forms the brief preferred are therefore covered only as dialog and sheet; off-canvas navigation is not.
- **NOT ASSESSABLE.** Two checks in run 3 (criteria 1 and 2), as not applicable.
- **Environment.** One model family, one browser engine (headless Chromium), small plain-HTML seed projects, and builders working without a human.
- **Builders' own VALIDATE.** Builders validated in a browser as the skill directs. That may catch issues a less thorough run would ship; it is part of the current pipeline being measured.
- **Not the Phase 7 condition.** The skill now includes A11Y-009, A11Y-010 (whose check (5) opens menus, drawers and dialogs) and A11Y-011. These may draw attention to overlays without naming the five behaviours. The model and session conditions also differ from Phase 7. This benchmark does not separate these factors.
- **No population claim.** This is an observed signal from two overlay builds, not a frequency estimate.

## 8. Benchmark verdict

**NO OBSERVED FAILURE.** All assessable behaviours passed across all usable runs: 10 of 10 overlay checks, plus 3 of 3 applicable checks in the non-overlay run.

## 9. Consequence

- **No frequency signal.** This benchmark provides no frequency signal supporting a later Rule Authoring investigation.
- **The coverage gap still stands.** No rule names the five behaviours (Evidence Investigation §4).
- **The two findings together.** Current builds produced the behaviours unprompted in both overlay runs, even though no rule names them. The three self-reported Phase 7 failures are not reproduced under current conditions in this sample.
- **Any decision now rests with the human.** Examples: accept the uncovered-but-unobserved state, or seek more evidence (for example off-canvas navigation). This milestone makes no rule and no recommendation to author one.

## 10. Scope compliance

- **No changes to:**
  - the Rule Catalog (A11Y-002 and axis 5 included);
  - the critique protocol;
  - `SKILL.md`, `loop.md` or the Principle Pool;
  - the Integration Contract;
  - runtime architecture.
- **No Rule Authoring and no reference acquisition.**
- **Disposable artifacts stay outside the repository and are not committed:** seed projects, builds, builder reports and evaluator scratch.
- **`.playwright-mcp`.** The builders' and evaluator's browser tools twice created an empty `.playwright-mcp` folder in the repository root. The tools deleted it, and the one empty remnant was removed by the main agent.
- **Committed files:** `STATE.md` and this report. Nothing was pushed.
