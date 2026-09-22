# Phase 7.2 — Reicon Integration

## 1. Objective

Establish Reicon as the **default implementation source for new iconography** when a project has no established icon system and no explicit user instruction governs the choice — without making Reicon mandatory, without letting it define visual direction, and without adding a new pipeline stage, routing axis, classifier, or scoring system. This is a default-capability integration only; it does not claim to improve benchmark outcomes.

## 2. Evidence From Phase 7

`benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10A ("Reicon (default iconography system)") states the case this phase acts on:

- Every Phase 7 benchmark test hand-built its own icons ad hoc.
- A meaningful share of the accessibility findings across the benchmark were icon-related (`aria-hidden` on decorative SVGs, `aria-label` on icon-only buttons, PHASE-7-06R's `✕`-glyph → SVG swap for reliable assistive-technology exposure).
- The same section names the risk this phase treats as a hard constraint: Reicon "must not override an existing project's icon language" — PHASE-7-06R (ORBIT) explicitly preserved its existing stroke language, and Reicon must yield to that kind of instruction, not compete with it.
- Interaction with explicit user instructions is stated as **subordinate** — brief/existing-system instructions win.
- Progressive disclosure is stated as: load only when a project needs new iconography, never bundled by default.

`architecture/ARCHITECTURE.md` §13/§16 area (icon accessibility) independently confirms `A11Y-004`'s existing role-conditional icon accessibility rule (decorative-beside-text hidden from the a11y tree; standalone needs alt; interactive needs accessible name+state) predates this phase and already governs icon accessibility — this phase does not touch it.

No file in the repository specifies Reicon's install steps, package name, API surface, or icon inventory. Every existing mention (`PHASE-6.3-PROPOSAL.md`, `PHASE-6.5-PROPOSAL.md`, `PHASE-6.4-RESULTS.md`, `PHASE-7-CROSS-PROJECT-ANALYSIS.md`, `PHASE-7.1-TARGETED-CORRECTIONS.md`) treats Reicon only as a named candidate icon library, consistently deferred as out of scope until this phase. `reicon.md` therefore states no technical integration details — it explicitly defers those to Reicon's own documentation at BUILD time, against whatever stack the project uses.

## 3. Repository Inspection

Read in full before editing: `SKILL.md`, `references/style-catalog.md`, `references/anti-slop-registry.md`, `references/visual-references.md`, `references/existing-project-safety.md`, `references/critique-protocol.md`, `references/gesture-physics.md`, `references/rule-catalog/accessibility.md`, `references/rule-catalog/layout-interaction.md`, `references/rule-catalog/content-copy.md`, `architecture/ARCHITECTURE.md` (icon-related sections), and all Phase 7 benchmark/analysis files.

Findings that shaped the integration:

- `SKILL.md` §7 (Progressive Disclosure) already has a T4 tier for conditionally-loaded, narrow-scope material (`gesture-physics.md`, `references/stacks/*.md`), gated by real evidence of need — the exact shape Reicon's own stated progressive-disclosure requirement calls for. No new tier was needed.
- `existing-project-safety.md` already establishes the Improve-vs-Replace model and "reuse existing tokens/components/dependencies over introducing new ones for the same purpose" — this already covers preserving an existing icon system; no edit to this file was required.
- `rule-catalog/accessibility.md` A11Y-004 already fully specifies icon accessibility as role-conditional; no new or duplicate accessibility rule was needed.
- `rule-catalog/layout-interaction.md` LAYOUT-008 (imagery decision procedure) was reviewed as a possible template/location — its "decision procedure" format (answer explicit questions, record the answer, no mandate either way) was used as the structural model for `reicon.md`'s Selection section, but iconography is not imagery and LAYOUT-008 itself was left untouched; a new rule-catalog ID was judged unnecessary because the full decision belongs in one self-contained, conditionally-loaded file per the task's own instructions.
- No existing reference file was a correct home for Reicon-specific precedence/activation rules — none of the six inspected files are scoped to iconography, and cramming this into e.g. `layout-interaction.md` or `anti-slop-registry.md` would have miscategorized it (Reicon is neither a structural/technical layout rule nor a banned-pattern entry).

Conclusion: the minimum correct integration surface is one new conditionally-loaded T4 reference file plus a one-line addition to `SKILL.md` §7's existing T4 table row (no new row, no new tier).

## 4. Integration Decision

Created `design-excellence/references/reicon.md` (T4, same tier as `gesture-physics.md`). Added `references/reicon.md` to the existing T4 row in `SKILL.md` §7, with its load condition stated inline, pointing to `reicon.md` for the full model. No other file was modified.

## 5. Precedence Model

`reicon.md` §"Precedence" states, in order:

1. Explicit user instruction (named library, custom iconography, specific style, "no icons") — followed unconditionally, never silently overridden.
2. Existing project icon system (`existing-project-safety.md` §1–§2) — preserved; Reicon applies only where a required icon genuinely doesn't exist in that system, new functionality needs iconography the system doesn't cover, or the user explicitly requests migration.
3. Reicon, for new iconography with no established system — the default once (1) and (2) don't apply.
4. Other/custom implementation, only when justified and stated as deliberate.

This exactly mirrors the precedence order specified in the task brief and in `PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10A's "subordinate" framing.

## 6. Default-New-Iconography Behavior

`reicon.md` §"Default Behavior" states the operative rule directly: a greenfield project, or a project with no established icon system, that genuinely needs new iconography defaults to Reicon as the source, with no additional user instruction required to reach that default. This is the mechanism that prevents the failure mode named in the task brief (generate generic icons → finish → replace with Reicon later) — the default is reached at DESIGN/BUILD, the first time an icon requirement exists, not after the fact.

Iconography need itself is gated upstream of this file, per `reicon.md` §"Selection": an icon's UX/content purpose (comprehension, navigation, action recognition, information density) must already be established, text must be preferred when clearer, and decorative iconography needs the brief to actually call for it. Reicon fills an already-real slot; it does not create one. This directly implements the task brief's "Reicon must NOT create a demand for icons" requirement.

## 7. Activation / Non-Activation Rules

`reicon.md` states both explicitly:

- **Activate/consider** when new iconography is genuinely needed, no established project icon system covers it, and no explicit user instruction names a different library/style/"no icons" — always at DESIGN/BUILD, after the icon's UX role is established.
- **Do not load/consider** for typography-only, layout-only, or copy-only work; tasks with no iconography requirement; pure visual polish where icons are untouched; an existing project preserving its icon system; or as a justification for adding an icon that wouldn't otherwise be needed.

This uses `SKILL.md` §7's existing progressive-disclosure mechanism (T4, evidence-gated) — no new pipeline stage or gating mechanism was introduced.

## 8. Existing-System Safety

`reicon.md` §"Existing-System Safety" is a one-paragraph pointer, not a restatement: it cites `existing-project-safety.md`'s Improve-vs-Replace model directly and states that Reicon's availability is never grounds to migrate an existing icon system, and that migration requires the same explicit confirmation any Replace-classified change already requires under that file. `existing-project-safety.md` itself was not edited — its general "reuse existing tokens/components/dependencies" principle (§3) already covers icon systems without a Reicon-specific carve-out.

## 9. Anti-Slop / Fingerprint Interaction

`reicon.md` §"Anti-Slop" explicitly declines to create a new Anti-Slop category or turn "uses Reicon" into a quality signal, per the task brief's constraint. It cross-references `anti-slop-registry.md` SLOP-007 (SaaS-card-kit, where icon-per-card is often part of the tell) only to clarify the boundary: Reicon changes an icon's *source quality* when one is already warranted, it does not license the icon-card pattern SLOP-007 already flags, and it does not touch SLOP-007's own applicability or remediation.

Reicon is explicitly kept subordinate to Register/Genre/visual fingerprint/visual references/existing project context/UX requirements/explicit user direction (`reicon.md` opening paragraph and §"Purpose") — it answers *how* an already-needed icon gets implemented, never *whether* one is needed, what role it plays, or what the visual direction is. No change was made to `SKILL.md` §4 (Register/Genre/Dials), §6 (Visual Fingerprint), or `visual-references.md`.

## 10. Accessibility Interaction

`reicon.md` §"Accessibility" is a single-sentence deferral to `rule-catalog/accessibility.md` A11Y-004, restating none of its content. `accessibility.md` was not modified. This satisfies the task brief's explicit instruction not to duplicate the accessibility system.

## 11. Files Changed

- **Created:** `design-excellence/references/reicon.md` (new T4 reference file, ~95 lines).
- **Modified:** `design-excellence/SKILL.md` — one line changed in §7's Progressive Disclosure table (the existing T4 row), adding `references/reicon.md` and its load condition. No other line in `SKILL.md` was touched.
- **No other files were modified.**

## 12. Validation Performed

1. Searched the full `design-excellence/` skill directory for all Reicon references — found in exactly the two intended files (`SKILL.md`, `references/reicon.md`).
2. Confirmed `reicon.md`'s Default Behavior section establishes Reicon as the default for new iconography where no existing system exists, with no additional instruction required.
3. Confirmed the Precedence section places explicit user instruction above Reicon, worded as an unconditional override ("Follow it. Never silently substitute Reicon.").
4. Confirmed the Precedence section places an existing project icon system above Reicon, and cross-references `existing-project-safety.md`'s Improve/Replace model rather than restating it.
5. Confirmed Reicon is never stated as mandatory — Non-Activation explicitly lists cases where it must not be loaded or considered, and Precedence's item 4 (other/custom) remains available when Reicon doesn't fit.
6. Confirmed the Selection section requires an icon's UX role to be established before Reicon is consulted, and states plainly that Reicon's availability is never sufficient justification for adding an icon.
7. Confirmed the opening paragraph and Purpose section explicitly subordinate Reicon to Register/Genre/visual fingerprint/visual references/existing context/UX/explicit instruction, and that no edits were made to any of those mechanisms.
8. Confirmed no new pipeline stage, routing axis, classifier, score, or compatibility matrix was introduced — the only mechanism used is `SKILL.md` §7's pre-existing T4 progressive-disclosure tier.
9. Confirmed no new routing axis was introduced — Task Mode/Scope/Project State (`SKILL.md` §2) are unchanged.
10. Confirmed no numerical scoring or classifier exists anywhere in `reicon.md` — Validation is stated as a qualitative checklist, matching `critique-protocol.md`'s and `layout-interaction.md` LAYOUT-008/009/010's existing non-scored format.
11. Confirmed `SKILL.md` changed by exactly one line, and no other section of that file was expanded.
12. Confirmed via `git status --short` that no unrelated files changed — only `SKILL.md` (modified) and `references/reicon.md` (new, untracked) appear.
13. Ran `git diff --check` — no whitespace errors; the pre-existing LF→CRLF conversion notice matches the same warning seen on prior commits in this repository's history and is not a new issue introduced by this change.
14. Reviewed `git status --short` output directly (above).
15. Reviewed the complete diff for `SKILL.md` and the full new content of `reicon.md` (this report's §4–§10 traces every section against the task brief's required behaviors).

## 13. Residual Risks

- **Untested in practice.** This phase integrates the default capability only, per the task brief's own instruction not to claim benchmark improvement. Whether Reicon actually produces better outcomes than the Phase 7 ad-hoc icon baseline is unverified — no benchmark run exercised this change.
- **Reicon's actual technical surface is unknown.** `reicon.md` deliberately states no install/API/package details because none exist in this repository's source material. The first real BUILD-time use of Reicon will need to resolve those details against Reicon's own documentation; if that documentation conflicts with any assumption implicit in this file's framing (e.g. if Reicon turns out to be genre/register-restrictive itself), `reicon.md` may need a follow-up correction pass.
- **A11Y-004 coverage is inherited, not verified against Reicon specifically.** The accessibility deferral assumes Reicon's icons are implemented as ordinary SVG/icon-font/component output that A11Y-004's three cases (decorative/standalone/interactive) already cover correctly. If Reicon ships a non-standard delivery mechanism (e.g. an icon web component with its own shadow-DOM labeling behavior), this assumption should be re-checked at first real use.
- **No mechanical validation exists for the Precedence/Default Behavior rules.** Like `LAYOUT-008`/`LAYOUT-009`/`LAYOUT-010`, this is manual/qualitative by design (per the task brief's explicit ban on a classifier/scoring system), so correct application depends on the agent actually reading and applying `reicon.md` at DESIGN/BUILD — there is no VALIDATE-stage mechanical check that would catch a missed default or a wrongly-overridden existing system.

## 14. Verdict

**PASS.** The integration establishes Reicon as the default source for new iconography exactly where the task brief specifies, with explicit user instruction and existing project icon systems both taking precedence, no mandatory-everywhere rule, no icon-density incentive, no influence over Register/Genre/visual direction, and no new pipeline stage, routing axis, classifier, or scoring system. The change surface is minimal: one new conditionally-loaded T4 file and a one-line `SKILL.md` table edit. Residual risk is limited to Reicon's real-world technical behavior, which is unverifiable from this repository alone and is correctly deferred rather than fabricated.
