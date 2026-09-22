# Phase 7.3 — Kinetics Integration

## 1. Objective

Make Kinetics available as an **implementation repertoire** for motion or microinteraction behavior that is already justified — by `motion.md`, `MOTION_INTENSITY`, explicit user instruction, or an established design direction — without letting Kinetics become a default motion layer, a reason to add animation, a replacement for an existing project's motion system, a substitute for `MOTION_INTENSITY`, a new design-direction mechanism, a new pipeline stage, a classifier, a scoring system, or a mandatory dependency. This is a capability-availability integration only; it does not claim to improve benchmark outcomes and does not claim Kinetics is technically integrated into any project.

## 2. Evidence From Phase 7

`benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10B ("Kinetics (motion and microinteraction repertoire)") states the case this phase acts on:

- Motion landed at Low `MOTION_INTENSITY` in **6 of 6** Phase 7 benchmark tests, including domains that could plausibly support more (§5.2 of that report) — a near-universal convergence, not noise.
- The analysis names this as **exactly the situation where importing a richer motion vocabulary carries real convergence risk**, if Kinetics becomes a new default reach rather than something genuinely calibrated per project.
- It states explicitly how Kinetics must stay a repertoire: "it must remain strictly gated by `MOTION_INTENSITY`'s existing dial mechanism (§3) — the same discipline that currently keeps motion Low where the brief calls for Low must keep Kinetics from becoming the default answer once it exists."
- It names the specific failure mode to guard against: "a repertoire that looks appealing in isolation could become the new reflex the same way REF-009 already shows a single structural device can dominate adoption" — i.e., Kinetics risks becoming the motion equivalent of a structurally over-adopted pattern if left ungated.
- §10D additionally flags that the `MOTION-004`/`MOTION-007` text tension (already resolved in Phase 7.1 — see §3 below) was judged relevant to Kinetics specifically, because Kinetics "will generate more motion/interaction code subject to exactly these ambiguities."

No file in this repository specifies Kinetics' install steps, package name, API surface, or pattern inventory. The only existing mention is `PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10B, which treats Kinetics purely as a candidate repertoire, evaluation-only, "not implemented here, per instructions." `kinetics.md` therefore states no technical integration details — it explicitly defers those to Kinetics' own documentation at BUILD time, against whatever stack the project uses, matching the same honesty discipline `reicon.md` already established for Reicon.

## 3. Repository Inspection

Read in full before editing: `SKILL.md`, `references/rule-catalog/motion.md`, `references/rule-catalog/accessibility.md`, `references/rule-catalog/layout-interaction.md`, `references/existing-project-safety.md`, `references/critique-protocol.md`, `references/anti-slop-registry.md`, `references/style-catalog.md`, `references/reicon.md`, `references/gesture-physics.md`, `benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md` (full), `benchmarks/phase-7/PHASE-7.2-REICON-INTEGRATION.md` (as the most recent T4-reference precedent).

Findings that shaped the integration:

- `SKILL.md` §7 (Progressive Disclosure) already has a T4 tier for conditionally-loaded, narrow-scope material (`gesture-physics.md`, `references/stacks/*.md`, `references/reicon.md`), gated by real evidence of need — the exact shape Kinetics' own required activation/non-activation model calls for. No new tier was needed.
- `motion.md` already states it is "the *only* motion decision system in this skill" and that "no other reference file defines a competing duration table, easing rule, or property list — they reference these ids." This is a direct, explicit constraint: `kinetics.md` must reference `motion.md`'s ids, never restate or fork them.
- `motion.md` MOTION-004 already carries the Phase 7.1 correction (paint-only carve-out, layout-affecting property restriction stated precisely) and MOTION-007 (`prefers-reduced-motion`: gentler, not zero, P1 safety) is unchanged and already fully specified. The MOTION-004/007 tension the cross-project analysis flagged as relevant to Kinetics (§10D) was already resolved in Phase 7.1, before this phase started — confirmed by reading the current file content, not assumed from the analysis document.
- `style-catalog.md` already gives each Genre a `motion_tier_default` (Low for the two most restrained catalog entries, Low–Medium/Medium–High/High for progressively more expressive ones), and MOTION-011 already gates bounce/elastic easing by genre/gesture context. This is the real, pre-existing consumer of Register/Genre for motion — `kinetics.md` references it rather than duplicating any genre-specific motion posture.
- `SKILL.md` §3's Authority Hierarchy (P1–P8) already orders exactly the precedence the task brief asked for (safety → explicit instruction → register/genre → existing-system → UX → anti-slop → performance → aesthetic). The task brief's own "Motion Precedence" list is a subset of this same ordering (it omits P6 anti-slop, which has no direct gating role here). Rather than author a second, Kinetics-specific precedence ladder, `kinetics.md` explicitly resolves via the existing hierarchy and states each relevant P-level's meaning for Kinetics inline.
- `anti-slop-registry.md` was read in full: it contains no motion-specific entry today (confirmed by grep — zero matches for "motion" in that file). This confirms the task brief's instruction not to create a new Anti-Slop category has no existing motion-adjacent entry to reconcile against; `kinetics.md`'s Anti-Slop section states the constraint in prose instead, exactly as `reicon.md` did for SLOP-007.
- `SKILL.md` §6 (Visual Fingerprint) lists five fixed dimensions, one of which is "motion tier." Kinetics sits inside that existing dimension; the fingerprint mechanism itself was not touched.
- `reicon.md` was used as the direct structural template (same T4 tier, same section shape: Purpose/Activation/Non-Activation/Precedence/…/Validation, same "qualitative, not scored" closing convention) — but its *content* differs materially from Kinetics', because Reicon is a **default source once a slot exists and no system governs it**, while Kinetics is a **repertoire consulted only once a behavior is already decided**, never a default reach. This distinction is stated explicitly in `kinetics.md` and is the core reason a Reicon-shaped file was not simply copied with terms swapped.

Conclusion: the minimum correct integration surface is one new conditionally-loaded T4 reference file plus a one-line addition to `SKILL.md` §7's existing T4 table row (no new row, no new tier) — the same shape Phase 7.2 used for Reicon, adjusted in content for motion's different risk profile.

## 4. Integration Decision

Created `design-excellence/references/kinetics.md` (T4, same tier as `gesture-physics.md` and `reicon.md`). Added `references/kinetics.md` to the existing T4 row in `SKILL.md` §7, with its load condition stated inline, pointing to `kinetics.md` for the full precedence model. No other file was modified.

## 5. Motion Need vs. Implementation

`kinetics.md` states the distinction directly in its opening paragraph and again in a dedicated "Motion Need" section: Kinetics "answers *how* an already-decided motion or microinteraction behavior gets implemented; it never answers *whether* the interface should move." That decision belongs entirely to `motion.md`'s existing canonical decision sequence (should it animate → purpose → interaction type → property → easing → duration → interruptibility → accessibility → performance) and `SKILL.md` §4's `MOTION_INTENSITY` dial — both cited by reference, neither restated.

The two "Valid" examples from the task brief (a brief-required page transition; a drag interaction needing spring response) map directly onto `kinetics.md`'s Activation section (behavior already justified by an existing UX requirement or design direction, and the band already permits it). The two "Invalid" examples (adding hover animation because Kinetics has a nice one; raising `MOTION_INTENSITY` because Kinetics is in use) map directly onto Non-Activation and the Motion Intensity section's opening sentence: "`MOTION_INTENSITY` … remains fully authoritative and is not modified, extended, or shadowed by a second scale."

## 6. Precedence Model

`kinetics.md` §"Precedence" resolves via `SKILL.md` §3's existing Authority Hierarchy rather than introducing a parallel one, stating each relevant level's meaning for Kinetics specifically:

1. P1 safety/correctness (`MOTION-007`, the P1 accessibility floor) — non-negotiable.
2. P2 explicit user instruction — followed unconditionally, never silently overridden.
3. P3 Register/Genre/established motion direction (`style-catalog.md` `motion_tier_default`, any direction already committed at DIRECT/SHAPE).
4. P4 existing project motion system (`existing-project-safety.md` §1–§2) — preserved; Kinetics applies only to a genuine gap or an explicit migration request.
5. P5 UX purpose (`MOTION-002`'s vocabulary) — the behavior's role must already be established.
6. Kinetics itself — the point actually consulted, once 1–5 clear.
7. P7 performance/production constraints (`MOTION-004`/`MOTION-005`/`MOTION-006`).
8. P8 aesthetic preference — lowest precedence.

This is not a rewrite of the existing hierarchy — `SKILL.md` §3 itself was not touched — it is Kinetics stating where it sits within the hierarchy that already exists.

## 7. Activation / Non-Activation Rules

`kinetics.md` states both explicitly:

- **Activate/consider** when a motion/microinteraction behavior is already justified (by `motion.md`'s purpose vocabulary, an explicit UX requirement, the established direction, or explicit user instruction), the already-selected `MOTION_INTENSITY` band permits it, and no existing project motion system already covers it — at BUILD, implementing a decision already made upstream, never earlier.
- **Do not load/consider** for typography-only, static-layout-only, or copy-only work; tasks with no motion requirement; pure visual polish where motion is untouched; an existing project preserving its motion system with no new behavior needed; deciding whether the interface should move or raising `MOTION_INTENSITY`; or as justification for motion that wouldn't otherwise be needed.

This reuses `SKILL.md` §7's existing T4 progressive-disclosure mechanism — no new tier, pipeline stage, or gating mechanism was introduced.

## 8. MOTION_INTENSITY Interaction

`kinetics.md` §"Motion Intensity" states the dial "remains fully authoritative and is not modified, extended, or shadowed by a second scale," then states Kinetics' conformance at each band (Low/Medium/High) individually — in every case as *conforming to* the band's existing permission, never *expanding* it. The High-band note cites `MOTION-011`'s existing bounce/elastic conditional eligibility as the actual governing rule, not a Kinetics-specific allowance. The section closes: "If `motion.md`'s existing rules restrict an effect at the currently selected band, Kinetics remains subordinate to that restriction — it carries no exemption of its own." No second intensity scale, threshold, or numeric band was introduced anywhere in the file.

## 9. Existing-System Safety

`kinetics.md` §"Existing-System Safety" is a short pointer, not a restatement: it cites `existing-project-safety.md`'s Improve-vs-Replace model directly and states Kinetics is considered only when the existing system has a genuine gap for a newly required behavior, the user explicitly requests Kinetics, or the project is explicitly migrating its motion implementation — matching the task brief's three named exception cases exactly. `existing-project-safety.md` itself was not edited; its general "reuse existing tokens/components/dependencies" principle (§3) already covers motion systems without a Kinetics-specific carve-out.

## 10. Accessibility / Reduced Motion

`kinetics.md` §"Accessibility" defers entirely to `rule-catalog/motion.md` `MOTION-007` and `rule-catalog/accessibility.md` `A11Y-003` (which itself is a pointer to `MOTION-007`, not a duplicate — confirmed by reading `accessibility.md` directly). No reduced-motion rule is restated or duplicated. The section adds one operative constraint the task brief required: "A Kinetics pattern with no meaningful reduced-motion treatment is not production-ready and must not be treated as automatically usable" until `MOTION-007`'s actual requirement is met — and explicitly declines to invent implementation details not supported by the repository's existing rules, resolving instead against `MOTION-007`'s stated requirement (keep opacity/color transitions that aid comprehension, drop movement/position changes). `accessibility.md` and `motion.md` were not modified.

## 11. Performance Interaction

`kinetics.md` §"Performance" defers to `MOTION-004` (property restriction — layout-affecting properties banned, transform/opacity/clip-path preferred, paint-only carve-out from the Phase 7.1 correction), `MOTION-005` (duration budget), `MOTION-006` (interruptibility: transitions/springs, not keyframes), and the general performance-hardening category. No Kinetics-specific performance scoring, threshold, or matrix was introduced. The section states Kinetics "must not be used to introduce unnecessary continuous animation, expensive effects, or excessive simultaneous animation beyond what the already-established UX purpose and `MOTION_INTENSITY` band justify" — directly implementing the task brief's performance constraints without adding a new mechanism to enforce them.

## 12. Anti-Slop / Fingerprint Interaction

`kinetics.md` §"Anti-Slop" explicitly declines to create a new Anti-Slop category or treat "uses Kinetics" as a quality signal, matching the task brief's constraint and the confirmed absence of any motion-related entry in `anti-slop-registry.md` today. It restates `MOTION-002`'s purpose vocabulary as the standing test any Kinetics-implemented motion must still pass, and names the specific anti-patterns the task brief called out (decoration alone, generic hover effects everywhere, gratuitous entrance animation, excessive scroll choreography, identical "premium" recipes reused across projects) as remaining exactly as ungrounded with Kinetics available as without it.

On fingerprint: `SKILL.md` §6's five dimensions (macrostructure, typography pairing, color-anchor, density band, motion tier) are unchanged — no edit was made to §6. `kinetics.md` states directly that it "does not become a fingerprint dimension" and that different Kinetics patterns do not by themselves count as fingerprint differentiation — Kinetics sits inside the existing motion-tier dimension as an implementation source, nothing more.

## 13. Files Changed

- **Created:** `design-excellence/references/kinetics.md` (new T4 reference file, ~90 lines).
- **Modified:** `design-excellence/SKILL.md` — one line changed in §7's Progressive Disclosure table (the existing T4 row), adding `references/kinetics.md` and its load condition. No other line in `SKILL.md` was touched.
- **Created:** this report, `benchmarks/phase-7/PHASE-7.3-KINETICS-INTEGRATION.md`.
- **No other files were modified.**

## 14. Validation Performed

1. Searched the full `design-excellence/` skill directory for all Kinetics references — found in exactly the two intended files (`SKILL.md`, `references/kinetics.md`).
2. Confirmed `kinetics.md` never describes Kinetics as a default motion system — its Purpose, Activation, and Motion Need sections all state it is consulted only after a motion decision already exists.
3. Confirmed every section of `kinetics.md` (Precedence, Motion Intensity, Existing-System Safety, Performance) states Kinetics as explicitly subordinate to `motion.md`, `MOTION_INTENSITY`, existing project motion systems, and `SKILL.md` §3's Authority Hierarchy — never competing with them.
4. Confirmed the Precedence section places an existing project motion system (P4) above Kinetics, and cross-references `existing-project-safety.md`'s Improve/Replace model rather than restating it.
5. Confirmed explicit user instruction (P2) is stated as followed unconditionally, "never silently substitute Kinetics."
6. Confirmed `MOTION_INTENSITY`'s definition was not altered — `SKILL.md` §4 was not edited, and `kinetics.md` states the dial "is not modified, extended, or shadowed by a second scale."
7. Confirmed reduced-motion behavior remains governed entirely by `MOTION-007`/`A11Y-003` — neither file was edited, and `kinetics.md` adds no competing reduced-motion rule.
8. Confirmed performance remains governed entirely by `MOTION-004`/`MOTION-005`/`MOTION-006` and the performance-hardening category — none edited, no Kinetics-specific scoring introduced.
9. Confirmed `kinetics.md`'s Motion Need section states Kinetics "never creates the need for motion" and that "Kinetics has a nice pattern for X" is explicitly insufficient justification.
10. Confirmed `SKILL.md` §4 (Register/Genre/Dials) and §3 (Authority Hierarchy) are byte-for-byte unchanged apart from the single §7 table-row edit — verified via `git diff`.
11. Confirmed `SKILL.md` §6 (Visual Fingerprint) is unchanged, and `kinetics.md` explicitly disclaims becoming a new fingerprint dimension.
12. Confirmed no new entry was added to `anti-slop-registry.md` (file untouched, verified via `git status`) and no motion-specific entry existed there before this phase (verified via grep, zero prior matches).
13. Confirmed no new pipeline stage, routing axis, classifier, score, or compatibility matrix exists anywhere in `kinetics.md` — Validation is stated as a qualitative checklist, matching `critique-protocol.md`'s and `reicon.md`'s existing non-scored format.
14. Confirmed `SKILL.md` was not "unnecessarily expanded" — exactly one existing table row changed; no new row, section, or tier was added.
15. Ran `git status --short` — confirmed only `design-excellence/SKILL.md` (modified) and `design-excellence/references/kinetics.md` (new, untracked) changed prior to this report's own creation; no unrelated files touched.
16. Ran `git diff --check` — no whitespace errors; the pre-existing LF→CRLF conversion notice matches the same warning seen on prior commits in this repository's history and is not a new issue introduced by this change.
17. Reviewed the complete diff for `SKILL.md` (§13 of `PHASE-7.2-REICON-INTEGRATION.md`'s equivalent step) and the full new content of `kinetics.md` (this report's §4–§12 traces every section against the task brief's required behaviors).

## 15. Residual Risks

- **Untested in practice.** This phase integrates the capability only, per the task brief's own instruction not to claim benchmark improvement or claim technical integration into any project. Whether Kinetics actually stays subordinate to `MOTION_INTENSITY` in real use, rather than becoming a de facto default the way REF-009 dominated structural adoption in Phase 7 (per the cross-project analysis's own stated risk), is unverified — no benchmark run exercised this change.
- **Kinetics' actual technical surface is unknown.** `kinetics.md` deliberately states no install/API/package/pattern-inventory details because none exist in this repository's source material. The first real BUILD-time use of Kinetics will need to resolve those details against Kinetics' own documentation; if that documentation implies patterns incompatible with `MOTION-004`'s property restriction or `MOTION-007`'s reduced-motion requirement, `kinetics.md` may need a follow-up correction pass.
- **Reduced-motion coverage is inherited, not verified against Kinetics specifically.** The accessibility deferral assumes a Kinetics pattern can be given a reduced-motion treatment using ordinary CSS media-query or JS-level `prefers-reduced-motion` handling, the same way `MOTION-007` already assumes for hand-written motion. If a specific Kinetics pattern turns out to have no meaningful reduced-motion equivalent (e.g. a physics simulation with no static analog), `kinetics.md`'s existing instruction — do not treat it as automatically usable — governs, but this has not been exercised against a real Kinetics pattern.
- **No mechanical validation exists for the Activation/Precedence rules.** Like `reicon.md` and `layout-interaction.md` LAYOUT-008/009/010, this is manual/qualitative by design (per the task brief's explicit ban on a classifier/scoring system), so correct application depends on the agent actually reading and applying `kinetics.md` at BUILD — there is no VALIDATE-stage mechanical check that would catch Kinetics being reached for before a motion decision exists, or an existing motion system being silently replaced.
- **The precedence numbering intentionally deviates from a literal reading of the task brief.** The task brief's own "Motion Precedence" list numbers P1/P2/P3/P4/P5/P7/P8 (skipping P6). `kinetics.md` follows `SKILL.md` §3's actual P1–P8 hierarchy instead of reproducing that gap, on the judgment that the task brief's own instruction ("do not blindly rewrite the existing Authority Hierarchy… inspect how motion currently resolves conflicts… integrate Kinetics into the existing model rather than creating a parallel hierarchy") takes precedence over matching the brief's illustrative list literally. This is disclosed here as a deliberate interpretation, not a silent deviation.

## 16. Verdict

**PASS.** The integration makes Kinetics available exactly where the task brief specifies — as a subordinate implementation repertoire for already-justified motion — with `MOTION_INTENSITY`, existing project motion systems, explicit user instruction, and `MOTION-007`'s accessibility floor all taking precedence, no default-motion-layer behavior, no icon-density-style incentive to animate more, no influence over Register/Genre/visual direction, no new fingerprint dimension, no new Anti-Slop category, and no new pipeline stage, routing axis, classifier, or scoring system. The change surface is minimal: one new conditionally-loaded T4 file and a one-line `SKILL.md` table edit, mirroring the Phase 7.2 Reicon integration's shape while diverging in content to reflect motion's different, more restraint-favoring risk profile. Residual risk is limited to Kinetics' real-world technical behavior, which is unverifiable from this repository alone and is correctly deferred rather than fabricated.
