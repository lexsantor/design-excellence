# Rule Candidate Evaluation — Overlay Closed-State Availability — Results

**Labels.**
- **[DOC]** stated in a governed file or prior report.
- **[MEAS]** measured by a DE benchmark and independently verified.
- **[SELF]** reported by a DE build session about its own work, with no retained artifact.
- **[INF]** inference.

**Reading "A" in this report.** A means only that a candidate may be put to a separately authorized Rule Authoring milestone. `loop.md` §2 requires human authorization before "adding … or changing the meaning of any runtime knowledge in `design-excellence/` (… rules …)". An A classification authorizes nothing.

---

## 1. Status

**COMPLETED.** Evaluation only.

- **One candidate is classified A:** K1, the narrow closed-state availability proposition.
- **Every other candidate is B, D or F.**
- **Rule Authoring is not authorized.**
- **Repository state at start:** HEAD `7c7d8a7`.
- **No change to:** any file under `design-excellence/`, `loop.md`, the Principle Pool or the Integration Contract.
- **Not done:** no reference acquisition, no benchmark, no behavioural run.

## 2. Authorization

**Human authorization (2026-09-27), recorded in `STATE.md` before any evaluation work:** "Autorizo Rule Candidate Evaluation: Overlay Closed-State Availability. Scope limitado a evaluar la evidencia existente sobre el fallo observado en comportamiento 5(b) del Overlay Focus Management benchmark, determinar si constituye un Rule Catalog candidate y evaluar su relación con A11Y-002, A11Y-009 y las cinco behaviours documentadas en the Evidence Investigation. No autorizo Rule Authoring, cambios al Rule Catalog, Principle Pool, Integration Contract, runtime architecture, SKILL.md, loop.md, adquisición de referencias ni benchmarks nuevos."

**Delegation.** One fresh, read-only, blind reviewer, as `loop.md` §8 requires for a governance verdict. It is within the §9 cap of 0–1 subagents for ordinary work, and follows the precedent of `RULE-CANDIDATE-EVALUATION-RESULTS.md` §10.

**Correction disclosed.** Before authorization, the main agent told the human that it did not plan to use subagents. When the authorization was recorded, the main agent's own annotation in `STATE.md` said "no subagents". That was an error: `loop.md` §8 requires a reviewer for this verdict. The annotation, which is not part of the human's authorization text, was corrected before the reviewer ran.

## 3. Evidence base

**Read for this milestone:**
- `benchmarks/overlay-focus/OVERLAY-FOCUS-COVERAGE-EXPANSION-RESULTS.md` (CE)
- `benchmarks/overlay-focus/OVERLAY-FOCUS-BEHAVIOURAL-BENCHMARK-RESULTS.md` (BB)
- `benchmarks/discovery/OVERLAY-FOCUS-EVIDENCE-INVESTIGATION-RESULTS.md` (EI)
- `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md` (GD): the untracked file, read-only
- `benchmarks/phase-7/PHASE-7-05-RESULTS.md` §6
- `design-excellence/references/rule-catalog/accessibility.md` (in full), plus overlay-related searches of `motion.md`, `layout-interaction.md`, `performance-hardening.md`, `smoothui.md` and `existing-project-safety.md`
- `design-excellence/references/critique-protocol.md` (axis 5)
- `design-excellence/SKILL.md` §3
- `loop.md` §2, §4, §8, §9, §15, §16
- `STATE.md`
- Precedent: `benchmarks/rule-candidate-evaluation/RULE-CANDIDATE-EVALUATION-RESULTS.md` (RCE), `benchmarks/taint-ruling/TAINT-RULING-RESULTS.md` (TR), and `benchmarks/phase-7/PHASE-7.1-TARGETED-CORRECTIONS.md` (how A11Y-009 was admitted)

**Evidence on the five behaviours:**

| Source | Runs | Quality | Result |
|---|---|---|---|
| CE (off-canvas navigation) | 3 | [MEAS]: independent evaluator plus independent reproduction by the main agent | 15 checks; 14 PASS; 1 FAIL (run 1, 5(b)) |
| BB (dialog, filter sheet) | 2 usable | [MEAS]: independent evaluator; the close-transition window was **not** probed | 10 checks; 10 PASS. Not rescored |
| Phase 7-01, 7-04, 7-05 (via EI §3) | 3 | [SELF]: the build sessions' own reports, quoting Level 2 findings for 01 and 04; no artifacts | 5 documented defects, 2 correct, 8 not assessable |

**Source of the five behaviours.** They were written in GD from Phase 7 DE-native evidence. GD states: "All evidence is DE-native: Design Excellence's own benchmark runs. No catalog material is involved" [DOC].

## 4. Observed failure

This restates CE §8–§9 and adds no new evidence.

- **Run 1:** a class-toggled off-canvas drawer.
- **What happens on close.** Closing sets the closed state at once and removes `inert` from the page at once. The drawer is hidden only after a delayed `visibility` transition, of about 220 ms in this build.
- **In that window:**
  - Shift+Tab reached the drawer's links (evaluator: +10 ms and later; main agent: +7 and +8 ms).
  - The accessibility tree still exposed the Close button and all drawer links (32 ms after Escape).
  - When the window ends, focus inside the drawer drops to BODY.
  - After a 400 ms wait, nothing in the drawer was reachable.
- **Detection.** The builder's own VALIDATE reported the drawer re-hidden after Escape. It did not detect the defect.
- **Native `<dialog>` runs 2 and 3:** not reproduced, including Shift+Tab 6–35 ms after Escape.
- **Close paths probed during the window:** only Escape (reviewer's note). Close-control and scrim closes were verified only in their settled state.
- **A second, earlier occurrence** of the same observable proposition, by a different mechanism: Phase 7-05 §6 item 2 [SELF]. Three drawers "were only moved off-screen via `transform`, leaving their content focusable and AT-visible while 'closed.'" That was a steady-state failure, found by the builder's own VALIDATE and fixed in the run.
- **Not evidence:** the BB filter sheet used a structurally similar delayed-`visibility` close but was never probed in the window. It is not counted and not rescored.

## 5. Existing-rule coverage analysis

**A11Y-002 (keyboard operability and `:focus-visible`; P1): does not govern the failure.**
- **Principle.** "every interactive element reachable and operable by keyboard alone" (`accessibility.md` l.24). It sets a floor on **reachability**. Nothing in it requires closed or hidden content to be **unreachable**. The failure is excess reachability, which the rule treats as the goal, not a defect (EI §4, cases 01 and 05).
- **Accessibility tree.** Exposure there is outside its keyboard-only scope.
- **Validation.** "static: every `:hover` rule has a `:focus-visible` counterpart" plus "rendered (Enhanced mode only: actual keyboard walk)" (l.30). The walk is unspecified and has no transition probe. The run 1 builder performed such a walk and missed the defect. A settled-state probe also misses it (CE §8).
- **Conclusion.** Treating "keyboard operability" as implying closed-state unavailability would add a requirement the text does not establish.

**A11Y-009 (essential content without JavaScript; P5): does not govern the failure.**
- **Checkable requirement.** Essential content and navigation must be visible and operable before JavaScript runs (l.54, validation l.60). Its failure runs the other way: content that is **unavailable**.
- **Presupposition, not a requirement.** Its applicability excludes "closed accordions/disclosures/modals/drawers whose collapsed state is represented accessibly and operably" (l.56). That is a scope carve-out: it names no check and no remediation.
  - Read in reverse, a drawer whose collapsed state is *not* represented accessibly falls back into A11Y-009's scope.
  - Even then, only the no-JavaScript test applies, and run 1 passes it: its no-JS fallback shows every link (CE §6).
- **Implementation guidance.** The remediation (l.61) addresses JavaScript-gated reveals and says nothing about exit states.
- **What the presupposition is good for.** It is an existing DE entry that assumes closed overlays are represented accessibly. It can therefore serve as supporting context for a norm (TR §11, C1(c)). It does not govern.

**Other entries considered: none governs.**

| Entry | Why it does not govern |
|---|---|
| A11Y-001 | Names "focus-not-obscured" as a WCAG 2.2 criterion (l.13), but gives no text or check. The defect is the focused element itself being hidden, not obscured by other content. It is not stretched to cover this |
| A11Y-010 check (5) | Opens closed menus and drawers for reflow only, and otherwise ignores them |
| INTX-001 | Covers component states, not overlay availability |
| MOTION-005 and MOTION-006 | MOTION-005 sets modal budgets of 200–500 ms; MOTION-006 prefers CSS transitions (reviewer [INF]). Neither governs availability, but both make timed exits normal, which is where this defect appears |
| MOTION-009 | Focus-ring timing |
| SmoothUI | Defers accessibility to A11Y-002 |

## 6. Five-behaviour coverage matrix

The Coverage column describes whether any current rule tells an agent or reviewer to produce or check the behaviour. That remains as EI §4 established; no governing text has changed since.

| Behaviour | Coverage | Failure evidence | Current independent results (CE + BB) | Bucket |
|---|---|---|---|---|
| 1. Focus enters on open | none | Phase 7-04 [SELF, Level 2] | 5/5 PASS | uncovered; not observed failing now (historical self-reported failure only) |
| 2. Focus contained while modal | none | Phase 7-04 [SELF, Level 2] | 5/5 PASS | same |
| 3. Escape closes | none | Phase 7-04 [SELF, Level 2] | 5/5 PASS | same |
| 4. Focus returns to trigger | none | Phase 7-04 [SELF, Level 2] | 5/5 PASS | same |
| 5(a). Background inert while open | none | Phase 7-01 [SELF, Level 2: virtual-cursor reach] | 5/5 PASS | same |
| 5(b). Closed overlay unavailable | none (A11Y-009 only presupposes it) | **CE run 1 [MEAS]**, plus Phase 7-05 [SELF] | 4/5 PASS, 1 FAIL | **evidence of failure under the current skill** |

**Adequately governed elsewhere:** none of the six.

**What the matrix supports.** One failure does not show that all five behaviours need a rule. Under current conditions:
- behaviours 1–4 passed 20 of 20 independent checks;
- 5(a) passed 5 of 5.

Their only failure evidence is self-reported, from Phase 7 builds that retained no artifacts.

## 7. Candidate rule proposition

Candidates are evaluated separately.

**K1: closed-state availability (behaviour 5(b)).** The narrowest proposition the evidence supports:

> When an overlay surface that is shown and dismissed (a drawer, sheet, off-canvas navigation panel or modal dialog) is closed, whether it was never opened or has been dismissed, none of its content can receive keyboard focus and none of it is exposed to assistive technologies. This holds from the moment the dismissal takes effect, including while any exit animation or transition is still running, until the overlay is opened again.

- **Observable behaviour only.** It sets no timing value and prescribes no technique:
  - no `inert`, `visibility`, `display` or `hidden`;
  - no JavaScript or CSS mechanism;
  - no `<dialog>` requirement;
  - no focus-trap library.

  Native `<dialog>` passed in every run, but no evidence *requires* it. A custom drawer can meet the proposition.
- **Scope.**
  - The failure evidence comes from drawers and off-canvas panels (CE run 1; Phase 7-05).
  - Modal dialogs are included because the proposition is identical and the fixed five-behaviour definition covers them. That adds no requirement, since native dialogs already meet it.
  - Inline disclosures and accordions are out of scope: there is no evidence about them.
- **Transition boundary.** "From the moment the dismissal takes effect" is what captures the demonstrated defect. A settled-state wording would restate what the Phase 7-05 fix already achieved, and would miss CE run 1.

**K2: background inert while the overlay is open (5(a)).** The proposition is rule-shaped: while a modal overlay is open, page content behind it cannot receive keyboard focus and is not exposed to assistive technologies. It is evaluated in §12.

**K3: the focus lifecycle (behaviours 1–4).** The proposition is rule-shaped: focus enters on open, stays contained while modal, Escape closes, and focus returns to the trigger. It is evaluated in §12.

**K4: one rule covering all five behaviours.** It is evaluated in §12.

**K5: implementation prescriptions** (reviewer's "K1-M" and similar). Examples:
- "apply `inert` to the overlay at the moment of closing";
- "never delay `visibility` on exit";
- "use `<dialog>`";
- a normative millisecond bound.

These are evaluated in §12.

## 8. Authority/layer analysis

**K1: P5 (UX/usability).**
- **`SKILL.md` §3.** It enumerates the only P1 accessibility floors (contrast, focus-visible, keyboard operability, reduced motion) and says "Do not add 'best practice' items to this list".
- **Why not the keyboard-operability floor.** K1's defect is extra reachability and phantom exposure. Nothing becomes impossible to operate by keyboard. A11Y-006 is P1 only because a drag-only interaction cannot be operated by keyboard at all (l.99); K1 does not meet that test.
- **Precedent.** The Phase 4 correction note (l.3) and A11Y-009's own layer note (l.53) keep a critical accessibility defect at P5 rather than expanding the list. A11Y-004, which governs exposure in the accessibility tree, is P5.
- **K2 and K3: P5 if ever authored**, for the same reason. The Phase 7-04 absence of all four behaviours was graded CRITICAL by its auditor, but that grades severity, not layer.

**Placement: conditional**, applying only when the interface contains a dismissible overlay. This follows A11Y-005, -006 and -007, which are scoped to the interaction they govern.

**Tradeoff (reviewer's point, adopted).**
- `critique-protocol.md` axis 5 lists only Always-on entries (l.13), so a conditional K1 would not appear on the Level 1 critique floor. That is the route by which the original gap escaped.
- Making K1 Always-on, or listing it in axis 5, is a separate authoring decision needing its own `loop.md` §2 authorization ("An entry joins this list only under its own `loop.md` §2 authorization").
- This evaluation does not decide it.

## 9. Severity analysis

**K1: major.**
- **Why not critical.** A11Y-008 and A11Y-009 are critical because their failure makes content or zoom unavailable to the affected user. K1's failure adds reachability and exposure; it removes nothing.
- **The demonstrated case is narrow.** It lasts only a transition window and is reached only by fast keyboard input or an assistive technology reading the tree during it (CE §9).
- **The steady-state case is worse.** In the Phase 7-05 shape [SELF], content is permanently focusable while hidden. It is still an addition of phantom focus stops rather than a loss of function.
- **Precedent.** A11Y-004 (misexposure in the accessibility tree) is major. RCE §8 rejected critical for U1a on the same "range of harm" reasoning.

**K2 and K3:** severity is set at authoring only if they are evidenced.

## 10. Validation proposal

This is the smallest behavioural check that would have detected CE run 1. It is written as a proposed rule `validation:` field, not as a benchmark or harness.

**Setup.** Rendered, Enhanced mode only, subject to the capability gating in `SKILL.md` §1. Run it with motion **not** reduced: reduced motion can shorten or remove the exit and hide the defect.

**For each dismissible overlay in the touched area:**
1. **Before first open.** A Tab sweep and a Shift+Tab sweep across the page never focus overlay content. The accessibility tree contains no overlay content.
2. **Open by keyboard.** Move focus to an element inside the overlay other than the first. Then close it, **once for each close path the overlay offers**:
   - Escape;
   - the close control, activated by keyboard;
   - a backdrop or scrim, if present;
   - the trigger, if it toggles.
3. **Immediately after each close, with no wait for the animation to settle,** press Shift+Tab and Tab several times each. Sample `document.activeElement` after every press. No sample may be inside the overlay.
4. **During the exit.** From the moment of closing until the overlay's own animations have finished, sample the accessibility tree repeatedly. Judge "finished" from the page (for example `getAnimations()` on the overlay), not from a fixed delay. No sample may contain overlay content.
5. **After the exit settles,** repeat check 1. Then repeat 2–4 on a second open/close cycle.

**Result.** PASS only if every sample in 1–5 holds.

**Validation hazard (DE-native, [MEAS]).** A probe that waits for the close to settle passes a build that fails. CE's main-agent probe passed run 1 after a 400 ms wait and failed it with no wait. This parallels the root-clip hazard recorded in A11Y-010's evidence.

**Without rendering capability.** Report `skipped — capability unavailable`. Statically flag **for review, not as failure** any overlay whose closed state takes effect after a delay, or only through position or opacity, with nothing removing its content from focus and the accessibility tree at the moment of dismissal. These are detection heuristics, not required techniques.

**Remediation (for authoring, stated as outcomes).** Make the overlay's content unavailable to focus and to assistive technologies at the moment of dismissal, independent of how long the visual exit lasts. Any technique that achieves this is acceptable.

## 11. Provenance/taint analysis

**K1 is DE-native and not tainted.**

| K1 clause | Support | Class |
|---|---|---|
| Norm: closed overlay content is not focusable and not exposed | CE run 1 [MEAS], Phase 7-05 [SELF]; A11Y-009 l.56 presupposes it (existing DE entry) | DE-native evidence plus existing DE entry (`loop.md` §4 independent support; TR §11 C1(b), C1(c)) |
| Scope: drawers, sheets, off-canvas navigation, modal dialogs | GD §4 / EI §2 fixed definition, written from Phase 7 DE evidence | DE-native |
| Boundary: from dismissal, including the exit transition | CE run 1 [MEAS] | DE-native |
| Validation, including the settle-wait hazard | CE §8 reproduction [MEAS] | DE-native |
| Remediation (outcome only) | derived from the norm; no source-specific technique | DE-native |

**What that means:**
- **No catalog material.** GD states that none is involved, and no clause is supported only by catalog material, so this is not catalog-derived.
- **Criteria.** The benchmark criteria were written from DE evidence, not from catalog material, so `loop.md` §4's "criteria written from catalog material … cannot supply a norm" does not apply.
- **Not WCAG-derived.** GD §5 names WCAG 2.2 SC 2.4.3 (Focus Order) and SC 2.1.2 (No Keyboard Trap) as possible independent support. Their text is not in the repository and was not acquired (not authorized). Nothing in K1 depends on WCAG. Verifying a WCAG mapping would be an optional authoring-time step that needs reference authorization.
- **Not checked.** Overlap with rejected catalog principles was not checked: the catalog was outside this milestone's reads. `loop.md` §4 requires any authoring request to disclose such overlap, so it must be stated at authoring.
- **Normative weight of Phase 7 findings.** The Phase 7 Level 2 auditor findings are DE-run output, not catalog material. They are treated as evidence of failure, not as a normative source.
- **Precedent.** A11Y-009 was admitted on DE-native evidence alone (`PHASE-7.1-TARGETED-CORRECTIONS.md`).

**K2 and K3:** DE-native by the same trace. Their limit is evidence strength, not provenance.

## 12. Candidate classification

| Candidate | Class | Layer | Severity | Placement |
|---|---|---|---|---|
| **K1** closed-state availability from dismissal onward, including during exit | **A — READY FOR RULE AUTHORING** | P5 | major | conditional (axis-5 listing is a separate §2 decision) |
| **K2** background inert while open (5(a)) | **B — RULE-SHAPED BUT INSUFFICIENT EVIDENCE** | P5 | set only if evidenced | conditional |
| **K3** focus lifecycle (behaviours 1–4) | **B — RULE-SHAPED BUT INSUFFICIENT EVIDENCE** | P5 | set only if evidenced | conditional |
| **K4** one rule for all five behaviours | **B** (only 5(b) is evidenced under the current skill; author K1 alone) | P5 | – | – |
| **K5** implementation prescriptions (`inert` on close, no delayed `visibility`, `<dialog>`, a millisecond bound) | **D — NOT RULE-SHAPED / IMPLEMENTATION-SPECIFIC**; a motion-side restatement of K1 would be **F** | – | – | at most remediation examples or a pointer at authoring |

**Why K1 is A.**
- **Normativity:** observable, with no technique or timing value.
- **Distinctness:** no rule governs it (§5).
- **Authority:** P5 by precedent.
- **Validation:** concrete and behavioural (§10).
- **Remediation:** concrete as an outcome.
- **Provenance:** clean (§11).
- **Evidence:** it meets the precedent by which A11Y-009 was admitted, a single DE-native Phase 7 defect caught only by independent review and admitted with its limit disclosed. It exceeds that precedent:
  - the failure was independently verified;
  - it was reproduced independently;
  - its code cause was identified;
  - it occurred under the current skill;
  - the skill's own VALIDATE missed it;
  - a second, self-reported occurrence exists (Phase 7-05).

**Counter-precedent, recorded (reviewer).** RCE §13 required U1b to fail in at least 2 of 3 runs. Under that repetition bar K1 would be B: 1 of 3 runs here, 1 of 5 across both benchmarks. U1b is not the governing precedent here, for three reasons:
- it was a DE-*stricter* design bar beyond a public standard;
- its validation was judgement-based;
- its topic was surfaced by the catalog.

K1 is a floor-type defect with mechanical validation and clean DE-native provenance, which is the A11Y-009 route. The human may still apply the stricter bar; if so, K1 becomes B.

**Why K2 and K3 are B.**
- **Rule-shaped:** they are observable, DE-native and uncovered.
- **Not enough evidence:**
  - their only failure evidence is self-reported, from Phase 7 builds with no artifacts;
  - they passed every one of 25 current independent checks (1–4: 20/20; 5(a): 5/5).
- **Not a benchmark hunt.** `loop.md` §15 says zero-yield results are valid outcomes, and RCE l.271 says benchmarks should not "manufacture failures". No further benchmark is recommended for them.

## 13. Evidence limitations

- **One independently verified failure.** It comes from one build, one implementation style (a class-toggled drawer with a delayed hide) and one close path probed in the window (Escape). The other close paths share the same code (`setOpen(false, true)`), so they probably fail too [INF], but they were not probed.
- **The second occurrence is weak.** Phase 7-05 is self-reported, with no artifact.
- **Environment.** One browser engine (Chromium), one model family, small plain-HTML seed projects.
- **No frequency estimate.** The five overlay runs across both benchmarks do not estimate frequency.
- **Probe-depth asymmetry.** BB's filter sheet may have had the same latent exposure. Because it was not probed, BB's 10/10 cannot be read as evidence against K1, and it is not rescored.
- **No WCAG verification.** No WCAG text is in the repository. K1's norm rests on DE-native evidence and an existing DE presupposition, not on a public standard. That is weaker external grounding than A11Y-010 and A11Y-011 have.
- **No catalog overlap check.** Overlap with rejected catalog principles was not checked (§11).

## 14. Exact conditions required before Rule Authoring

1. **Human authorization.** A separate, explicit human authorization for a Rule Authoring milestone naming K1 (`loop.md` §2). This evaluation does not grant it.
2. **Disclosure in the authorization request** (`loop.md` §4):
   - that the topic was surfaced by DE's own benchmarks, not the catalog;
   - a check for any overlap with rejected catalog principles;
   - a clause-by-clause provenance trace (the §11 table), checked by that milestone's §8 reviewer.
3. **Human decisions on authoring scope:**
   - **Placement:** conditional (as evaluated) or always-on.
   - **Critique floor:** whether `critique-protocol.md` axis 5 lists K1. This is a separate governed edit needing its own authorization.
   - **Relationship to A11Y-009:** whether A11Y-002 or A11Y-009 gets a cross-reference to K1. A pointer is not a duplicate, but a wording change to A11Y-009's applicability would change its meaning.
4. **Evidence bar.** Whether the human accepts the A11Y-009 admission precedent for K1, or applies RCE §13's repetition bar, which would make K1 B.
5. **Optional: WCAG support.** If the human wants WCAG grounding (SC 2.4.3 or 2.1.2), reference acquisition must be authorized to verify the text. K1 does not depend on it.
6. **Authoring constraints.** The authored rule stays within §7 K1's observable wording, with no timing value and no required technique. It carries §13's limitations into its `evidence:` field.

## 15. Explicit non-actions

- no Rule Authoring, and no draft entry written into any governed file;
- no change to:
  - the Rule Catalog (A11Y-002 and A11Y-009 unchanged);
  - `critique-protocol.md`, `SKILL.md` or `loop.md`;
  - the Principle Pool or the Integration Contract;
  - runtime architecture;
- no reference acquisition, no web access, no catalog reads;
- no new benchmark, behavioural run or harness;
- no rescoring of BB or CE;
- no authorization of any later milestone;
- pre-existing untracked files left untouched: `benchmarks/discovery/CURRENT-GAP-DISCOVERY-RESULTS.md` (read only), `rules.md`, `scratchpad/`.

**Independent review (`loop.md` §8).**
- **Reviewer.** One fresh, read-only, blind general-purpose agent.
- **What it received:** the question, the evidence reports, the Rule Catalog, `critique-protocol.md`, `smoothui.md`, `SKILL.md`, `loop.md` and the RCE/TR precedents.
- **What it did not receive:** the main agent's verdict, frozen before the reviewer ran (SHA-256 `5d8e491b…c36db6c`), and `STATE.md`.
- **What it wrote:** only its own output file in the session scratchpad.

**Agreement.** It reached the same conclusions on:
- A11Y-002 and A11Y-009 (neither governs);
- K1's shape and its A classification;
- P5, major and conditional placement;
- DE-native provenance;
- K2 and K3 as B.

**Reconciliation:**

| Point | Main agent (frozen) | Reviewer | Reconciliation |
|---|---|---|---|
| Bucket for 1–4 and 5(a) | "failure evidence" (historical) and "not observed failing" | "only 5(b) has evidence of failure"; the others are uncovered, not failing now, with self-reported Phase 7 failures | Same facts, different labels. §6 records both: historical [SELF] failures, and not failing under the current skill |
| Validation detail | immediate probes; accessibility tree after close | sample until the overlay's own animations finish (`getAnimations`), not a fixed delay; add a trigger-toggle close path; only Escape was probed in the window | **Adopted** (§10, §13) |
| Umbrella rule | not separated | K4: B | **Adopted** (§12) |
| Motion-side variant | prescriptions: D | K1-M: F as a requirement, D as technique guidance | **Adopted** (§12, K5) |
| Evidence bar | A by the A11Y-009 precedent | A, but B under RCE's U1b repetition bar | **Recorded** as a human decision (§12, §14 item 4) |
| Critique-floor tradeoff | not stated | conditional placement keeps K1 off axis 5 | **Adopted** (§8, §14 item 3) |
| A11Y-009 presupposition | supporting context | usable as C1(c) support | agreed |

No unreconciled disagreement remains.

## 16. Files changed

- `STATE.md`: modified. Governance fields from the human's authorization text; operational fields (iteration, status, blockers, pending gate, next action). The main agent's own annotation in the Authorization field was corrected as disclosed in §2.
- `benchmarks/discovery/OVERLAY-FOCUS-RULE-CANDIDATE-EVALUATION-RESULTS.md`: created (this report).

## 17. Commit hash

The hash is reported in the milestone's final response, since a commit cannot contain its own hash. The commit contains only the two files above. Nothing was pushed.
