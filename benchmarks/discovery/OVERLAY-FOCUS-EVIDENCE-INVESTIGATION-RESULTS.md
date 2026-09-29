# Overlay Focus Management — Evidence Investigation — Results

**Status:** COMPLETED.
**Verdict:** SUPPORTED (coverage gap established; how often DE actually gets overlay focus wrong is not established).
**Repository state examined:** HEAD `964f689`.
**Delegation:** none. The coverage question is answered from rule text directly, so an investigator would not have reduced uncertainty.

**Evidence labels.**
- **[OBS]** stated in a repository file.
- **[INF]** inference from observed facts.

---

## 1. Authorization

- **Human authorization (2026-09-27):** "Adelante, siguiente paso en base a la respuesta que te di antes." It was recorded in `STATE.md` (`loop.md` §7) before any other work.
- **Scope:** the read-only evidence pass proposed in `CURRENT-GAP-DISCOVERY-RESULTS.md` §5 step 1:
  - trace Phase 7 Tests 01, 04 and 05;
  - look for retained artifacts;
  - classify A11Y-002 and other current coverage of the five behaviours;
  - give a verdict.
- **Not authorized:**
  - behavioural runs and fixtures;
  - Rule Catalog changes and Rule Authoring;
  - the Principle Pool and the Integration Contract;
  - runtime architecture;
  - `SKILL.md` and `loop.md`;
  - push.
- **`STATE.md` state before this run.** `STATE.md` named the completed Rule Authoring — WCAG 2.2 SC 1.4.1 milestone, not Gap Discovery: Gap Discovery ran on the human's "report file only" instruction, without a `STATE.md` record. No milestone was active, so nothing conflicted.

## 2. Hypothesis

From `CURRENT-GAP-DISCOVERY-RESULTS.md` §4, verbatim:

> When a Design Excellence build adds an overlay surface (modal dialog, drawer, off-canvas navigation or sheet), the current skill does not reliably produce correct overlay focus management — focus moved into the overlay on open, kept within it while modal, Escape to close, focus returned to the trigger on close, and the background (or the closed overlay) removed from focus and the accessibility tree — through BUILD, VALIDATE and the Level 1 critique floor alone, because no Rule Catalog entry or critique axis names these behaviours and A11Y-002's generic keyboard-operability wording does not surface them; defects are therefore found mainly by Level 2, which does not run on POLISH, component or section scope, or BUILD without a brand-quality signal.

## 3. Evidence inventory

**Artifact availability** [OBS]:
- No Phase 7 build artifact exists in the working tree or anywhere in git history.
- `git log --all --name-only` lists no `.html`, `.js` or `.css` file under any path, only the Phase 7 reports.
- The `architecture/phase*` folders hold no retained output that mentions a dialog, drawer or `aria-modal`.
- The Phase 7 reports record no artifact paths.

**What that means.** All case evidence below comes from the Phase 7 per-test reports, which the build sessions wrote themselves. For 01 and 04 they quote the Level 2 auditor's findings. **Nothing was re-verified against code**, and no implementation detail is reconstructed beyond what the reports state.

**A11Y-002 in force during Phase 7** [OBS]:
- A11Y-002's current text, including its validation ("static: every `:hover` rule has a `:focus-visible` counterpart … rendered (Enhanced mode only: actual keyboard walk)"), is unchanged since the repository's first commit, `b4ec715` ("phase-6.5 baseline"). A pickaxe search for "actual keyboard walk" finds only that commit and two path-reorganization commits.
- The Phase 7 reports arrived in the next commit.
- The later accessibility changes (A11Y-009, A11Y-010, A11Y-011) did not touch A11Y-002.

| | Test 01 (MOVA) | Test 04 (FORMA) | Test 05 |
|---|---|---|---|
| **Overlay** | full-screen mobile navigation disclosure (01 l.121–122, 154–155) | mobile filter sheet `role="dialog"`; mobile navigation (04 l.54, 67) | mobile navigation drawer, "Crear tarea" slide-over drawer, client-detail drawer (05 l.51, 58, 91) |
| **Available evidence** | the report: design claim (l.155 "a real full-screen disclosure with a focus trap"), Level 2 ux-auditor findings (l.263–266), refinement (l.329–331) | the report: design claim (l.54 "with a real focus trap"), Level 1 list (l.59–60), Level 2 ux-auditor findings (l.67), refinement (l.75) | the report: Level 1 (l.67–78), Level 2 not triggered (l.82–83), VALIDATE/CRITIQUE fixes (l.88–93), summary (l.124, 130) |
| **Missing evidence** | build artifact; whether focus moved in on open, Escape handling, and focus return (not stated) | build artifact; the mobile nav's exact gaps ("better, still incomplete") | build artifact; initial focus, containment, Escape and focus return for the drawers (not stated) |
| **Verified behaviour (per report)** | focus contained (a trap existed; the auditor refers to "the keyboard focus trap", l.265) | none of behaviours 1–4 on the filter sheet: "no initial focus, no Tab trap, no Escape handler, no focus restore" | after the fix, closed drawers are `inert` |
| **Defect** | behaviour 5: background `<main>` not `inert` while the overlay was open, so screen-reader virtual-cursor navigation could reach occluded content. Graded MODERATE | behaviours 1–4 absent on the filter sheet. Graded CRITICAL. It contradicted the build's own "real focus trap" claim | behaviour 5 (closed overlay): drawers only moved off-screen with `transform`, "leaving their content focusable and AT-visible while 'closed'" |
| **Detection stage** | Level 2 ux-auditor. Level 1 and VALIDATE did not report it; the builder's summary (l.559–560) names only the JS-dependency miss explicitly | Level 2 ux-auditor. Level 1's list of pre-Level 2 catches (l.59–60) does not include it | VALIDATE/CRITIQUE by the builder itself ("rendered-output inspection with Playwright", l.88). Level 2 did not run |
| **A11Y-002 active** | yes | yes | yes |
| **Level 1 identified** | no (not in the reported Level 1 findings) | no | yes, in combined VALIDATE/CRITIQUE (the report does not separate them) |
| **Level 2 identified** | yes | yes | not run |
| **VALIDATE identified** | no | no | yes (see above) |
| **Complete enough to support the claim?** | partial: the defect and its stage are stated; three behaviours are unknown | yes for the filter sheet (four behaviours named absent) | partial: the defect and its stage are stated; four behaviours unknown |
| **Confidence** | moderate | moderate-high | moderate |

**Case summary** [OBS]:
- 3 of 3 builds shipped an overlay-focus defect out of BUILD.
- Two were detected only by Level 2; one by the builder's own rendered VALIDATE, with no Level 2.
- Of the 15 case-behaviour pairs (3 cases × 5 behaviours), 5 are documented defects, 2 are documented as correct, and 8 are not assessable.

## 4. Five-behaviour coverage matrix

Classification is about whether the current protocol tells the agent or reviewer to check the behaviour. It is not about whether a keyboard walk might happen to meet it.

| Behaviour | A11Y-002 | Other current coverage | Classification | Evidence |
|---|---|---|---|---|
| 1. Focus moves into the overlay on open | Not named. The principle is "every interactive element reachable and operable by keyboard alone"; the rendered validation is an unspecified "actual keyboard walk" | none. MOTION-009 governs focus-ring timing; A11Y-010 check (5) opens overlays for reflow only | **NOT COVERED** | `accessibility.md` A11Y-002; `motion.md` MOTION-009; A11Y-010 validation (5) |
| 2. Focus stays contained while modal | Not named. "Reachable and operable" does not require containment | none | **NOT COVERED** | as above |
| 3. Escape closes the overlay | Not named. An overlay with a keyboard-operable close button meets A11Y-002's wording without Escape | none. MOTION-010 uses focus but not Escape | **NOT COVERED** | as above |
| 4. Focus returns to the trigger on close | Not named | none | **NOT COVERED** | as above |
| 5. Background (while open) or the closed overlay is inert | Not named. A11Y-002's "every interactive element reachable" points toward reachability, and does not address hidden or occluded content | A11Y-009's applicability *presupposes* closed modals and drawers "whose collapsed state is represented accessibly and operably" but states no requirement. A11Y-010 *ignores* closed menus and drawers for measurement. SmoothUI defers to A11Y-002 ("unresolved keyboard operability, focus visibility, or form-state behavior … not production-ready") | **NOT COVERED** | `accessibility.md` A11Y-009 applicability; A11Y-010 validation; `smoothui.md` Accessibility |

**Would the Phase 7 defects escape A11Y-002 under the current protocol?** [INF] Yes, realistically:
- **04:** a filter sheet whose Close button is keyboard-operable satisfies A11Y-002's text while lacking behaviours 1–4. That is the observed case.
- **01:** the defect concerned assistive-technology exposure (virtual cursor) while keyboard focus was trapped. That is outside A11Y-002's keyboard scope by construction.
- **05:** off-screen focusable drawer content is "reachable". A11Y-002 names reachability as a goal, not a defect.

The protocol text has not changed since Phase 7, so the same routes remain.

## 5. Pipeline analysis

- **BUILD.** No catalog entry names any of the five behaviours, so BUILD has no instruction to produce them. 01 and 04 claimed a focus trap in their design and delivered one partially (01) or not at all (04) [OBS].
- **VALIDATE.** It runs "only the gates relevant to what was touched" (`SKILL.md` §1). For keyboard the relevant gate is A11Y-002, whose rendered check is an unspecified walk. VALIDATE caught behaviour 5 in 05 through the builder's own Playwright inspection, and missed it in 01 [OBS]. It has no instruction that would make the 05 result repeatable [INF].
- **Level 1 CRITIQUE.** Axis 5 lists A11Y-002 as an always-on check, and the self-critique scores it. It carries no overlay-specific question. In 01 and 04 Level 1 did not report the defects [OBS].
- **Level 2 CRITIQUE.** It found the 01 and 04 defects [OBS]. The findings came from the dispatched auditor's own expertise under the generic six-axis rubric (`critique-protocol.md` step 1), not from a DE instruction [INF].
- **Level 2 routing.** Level 2 runs only on its triggers: production/brand-critical signals, page-scope REDESIGN, greenfield multi-page BUILD with a brand-quality bar, or two failing Level 1 passes. It explicitly does not run "for BUILD at component/section scope, or for any POLISH task" [OBS]. Overlay additions to existing products typically arrive through those non-Level-2 routes [INF].

## 6. Hypothesis verdict

**SUPPORTED.** Each criterion of the milestone's decision logic is met:
- **Retained evidence supports the Phase 7 pattern** [OBS]. All three overlay builds shipped an overlay-focus defect out of BUILD, and two were detected only by Level 2.
- **All five behaviours are NOT COVERED** by current A11Y-002 validation or any other current mechanism (§4). This is established directly from rule text that has been unchanged since Phase 7.
- **The gap remains meaningful under the current pipeline.** Level 2 is stakes-gated and absent from POLISH and component/section BUILD, and nothing else names the behaviours.

**Limits of the verdict:**
- **Reliability is not measured.** Behaviour frequency rests on n = 3 self-reported builds from one benchmark, with no retained artifacts; 8 of 15 case-behaviour pairs are not assessable.
- **VALIDATE can sometimes catch it.** Test 05 shows the builder's VALIDATE catching behaviour 5 without Level 2.
- **What the verdict does and does not establish.** "Not covered" is established. "Not reliably produced" is supported but unquantified.

## 7. Next investigation

**Remaining question.** Under current routes that do not trigger Level 2, how often does a DE build ship an overlay missing one or more of the five behaviours?

**No read-only evidence remains.** No artifacts are retained, and no other retained DE run contains overlays (§3). The question can therefore only be answered by behavioural runs.

**Smallest shape:**
- a few independent DE runs of tasks that add an overlay;
- routed so that Level 2 does not trigger (for example section-scope BUILD, or POLISH in an existing project);
- scored by an independent reviewer against the five behaviours as fixed criteria;
- verdicts recorded per behaviour.

**Separate benchmark authorization required.** This milestone does not authorize it. Rule Authoring would need its own, later authorization.

## 8. Explicit non-actions

- no Rule Catalog changes;
- no Rule Authoring;
- no benchmarks or behavioural runs;
- no fixtures;
- no Principle Pool changes;
- no Integration Contract changes;
- no runtime architecture changes;
- no `SKILL.md` changes;
- no `loop.md` changes;
- no internet access or external references.

## 9. Files

**Changed by this milestone:**
- `STATE.md`: governance fields from the human's authorization; operational fields.
- `benchmarks/discovery/OVERLAY-FOCUS-EVIDENCE-INVESTIGATION-RESULTS.md`: added (this report).

**Not changed:** everything else, including `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md`, which remains untracked from the previous run, as the human instructed there.

**Commit.** The brief asked for no commit unless `loop.md` requires one. `loop.md` §1 makes COMMIT step 10 of the core cycle, and §14 says "Commit once per completed milestone … containing only that milestone's intended files". This milestone is therefore committed locally, with exactly the two files above. Nothing was pushed.
