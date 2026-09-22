# Phase 7.4 — SmoothUI Integration

## Objective

Integrate SmoothUI as a governed **implementation source** for components and UI patterns already decided to exist — never a design-direction engine. SmoothUI must answer *how* an already-justified component or interaction pattern gets implemented; it must never answer *whether* the product should have that component or pattern. The existence of a SmoothUI component must never itself create a reason to introduce that component.

This mirrors Phase 7.2 (Reicon, iconography) and Phase 7.3 (Kinetics, motion) — the third and final implementation-source integration named in `PHASE-7-CROSS-PROJECT-ANALYSIS.md` §12.

## Inspected Architecture

- `design-excellence/SKILL.md` — full read. §3 Authority Hierarchy (P0–P8), §7 Progressive Disclosure T4 row (the existing Reicon/Kinetics integration pattern), §9 Core Principle 11 ("Extract a reusable component only at 3+ uses with the same intent — never abstract for a one-off") and Principle 12 ("Leverage over coverage").
- `design-excellence/references/existing-project-safety.md` — full read. §1 Inspect scan item 6 (framework/dependency detection) is the hook point for detecting an existing component/design-system library; §2 Improve vs. Replace governs migration; §3 non-destructive editing rules.
- `design-excellence/references/reicon.md` and `design-excellence/references/kinetics.md` — full read, used as the direct structural and precedence template (kinetics.md's explicit P1–P8 authority-hierarchy walkthrough is the closest existing precedent to what this phase requires).
- `design-excellence/references/rule-catalog/layout-interaction.md` — searched for existing component-abstraction governance; confirmed no separate component rule exists beyond `SKILL.md` §9 Principle 11, and confirmed component-scope POLISH has no path into DEFINE/DIRECT/SHAPE (§2 Hard rule, cross-referenced).
- `design-excellence/references/rule-catalog/accessibility.md` — rule IDs enumerated (`A11Y-001` through `A11Y-009`). `A11Y-002` (keyboard operability + `:focus-visible`), `A11Y-005` (touch target size), `A11Y-007` (form-field state bugs), and `A11Y-008` (never disable zoom) identified as the rules directly governing interactive-component implementation.
- `design-excellence/references/rule-catalog/performance-hardening.md` — searched for dependency/bundle-specific rules; none exist beyond `PERF-002` (LCP lazy-loading). No new rule invented; SmoothUI deferred to the existing category generically, consistent with how `kinetics.md` defers to `motion.md`'s performance rules.
- `design-excellence/references/style-catalog.md` — checked for SmoothUI references; none found requiring reconciliation.
- `design-excellence/references/anti-slop-registry.md` — searched for `category: components` entries. Found `SLOP-007` ("SaaS-card kit" uniform cardification, major) and `SLOP-008` (glassmorphism as unconsidered default, moderate) — both directly applicable to a SmoothUI-implemented component and cited in the new reference file.
- `architecture/ARCHITECTURE.md`, `architecture/FORENSIC-EXTRACTION.md` — checked for SmoothUI mentions; none found. No architectural precedent to reconcile beyond what Phase 7's own benchmark analysis already established.
- `benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md` — §10C ("SmoothUI — optional component implementation source") read in full: identifies real, repeated component-implementation cost across all six benchmark tests, explicitly warns that layering a shared component source on top "without discipline could accelerate visual sameness," and states the required coexistence model verbatim: *"as an implementation shortcut for a brief-derived pattern already decided by DIRECT, never a substitute for deciding the pattern"* with progressive disclosure gating. §11–§12 confirm SmoothUI as one of three integrations approved to proceed, explicitly conditioned on staying "gated by progressive disclosure and by the existing dial mechanisms... exactly as strictly as current rules are gated," and explicitly forbidding it from becoming "defaults that override an explicit brief or existing-system instruction."
- `benchmarks/phase-7/PHASE-7.1-TARGETED-CORRECTIONS.md` — confirmed SmoothUI was, before this phase, "not integrated, not referenced" (line 138).
- `proposals/PHASE-6.3-PROPOSAL.md` §224–225 — earlier design note confirming SmoothUI was always intended to sit downstream of DIRECT, supplying "a component" as implementation once "a structural expression is selected," never the decision of what the structure should be.

No existing safeguard against replacing an established component system was found beyond the general `existing-project-safety.md` Improve/Replace model — the same model Reicon and Kinetics already rely on. No dedicated "component system detection" step exists in the Inspect scan; item 6 (framework/dependency detection via `package.json`, config files) is the closest existing hook and is what `smoothui.md` cites.

## Integration Decision

Created `design-excellence/references/smoothui.md` as a T4 reference file, structurally modeled on `kinetics.md` (whose explicit P1–P8 walkthrough most closely matches what this phase's precedence requirement needed). Added one pointer entry to the existing T4 row in `SKILL.md` §7. No new pipeline stage, routing axis, classifier, or scoring mechanism was created.

## Activation / Non-Activation Rules

**Activates** only when all three hold: (1) a component or UI pattern is already justified by the brief, `SHAPE`, or explicit user instruction; (2) it has already cleared `SKILL.md` §9 Principle 11's 3+-uses/same-intent threshold; (3) no existing project component/design system already covers it, or the user explicitly requested migration.

**Does not activate** for: typography/copy-only work; deciding whether a component is needed; a one-off pattern below the componentization threshold; an existing project whose component system is being preserved unchanged; using SmoothUI's availability as a reason to add or abstract anything.

## Precedence

Resolved entirely through the existing `SKILL.md` §3 Authority Hierarchy — no parallel SmoothUI-specific ordering was created. `smoothui.md`'s Precedence section walks P1 (accessibility floor) → P2 (explicit instruction) → P3 (Register/Genre/direction) → P4 (existing component/design system) → P5 (UX purpose, gated by Principle 11) → P6 (Anti-Slop) → SmoothUI itself (only once P1–P6 clear) → P7 (performance) → P8 (aesthetic), matching the ordering the task specified.

## Existing-Project Safety

`smoothui.md` states explicitly: existing project component systems take precedence over SmoothUI; a working component is never replaced merely because SmoothUI offers an alternative; SmoothUI fills only a genuine implementation gap unless the user explicitly requests migration or replacement — enforced via `existing-project-safety.md`'s Improve/Replace confirmation gate, the same mechanism Reicon and Kinetics already use.

## Design-System Interaction

`smoothui.md` states explicitly that it does not weaken, replace, or bypass `SKILL.md` §9 Core Principle 11: a pattern used once is not extracted into a component merely because SmoothUI makes the implementation easy. The 3+-uses/same-intent threshold applies identically regardless of implementation source.

## Anti-Slop Interaction

`smoothui.md` explicitly disclaims becoming a new Anti-Slop category or a sixth fingerprint dimension. It cites `SLOP-007` and `SLOP-008` as the existing registry entries that already govern a SmoothUI-implemented component's visual treatment, and states plainly that SmoothUI changes an implementation's source quality, not whether the pattern, its density, or its visual treatment was warranted. Card usage, button hierarchy, page structure, spacing, typography, color, visual style, density, and interaction model remain governed entirely by Register/Genre/Dials and the rule catalog.

## Relationship to Reicon and Kinetics

`smoothui.md` includes a dedicated section stating the three implementation sources are parallel and independent, restates each one's role in one line, and states the cross-cutting sequencing rule verbatim: decide what the interface needs, then decide how it should behave and look, only then consult an implementation source — never reversed.

## Files Changed

1. **`design-excellence/references/smoothui.md`** (new) — T4 reference file defining SmoothUI's purpose, activation/non-activation, precedence, existing-project safety, greenfield ordering, design-system interaction, Anti-Slop interaction, accessibility deferral, performance deferral, relationship to Reicon/Kinetics, validation checklist, and an explicit "must never be used to justify" list.
2. **`design-excellence/SKILL.md`** (modified) — §7 Progressive Disclosure T4 row: added `references/smoothui.md` to the file list and one clause describing its load condition, matching the existing Reicon/Kinetics clause style. No other line changed.

No other file was modified. Nothing was committed.

## Validation Performed

- Full diff reviewed (`git status --short`, `git diff --check`) — one modified file (`SKILL.md`, single-row edit), one new file (`smoothui.md`). `git diff --check` reports only a pre-existing LF/CRLF line-ending advisory on `SKILL.md`, identical in kind to the one Phase 7.1's own validation logged — not a whitespace error.
- Duplicate rule-ID scan: searched all `### RULE-ID` definition headers under `design-excellence/references/` — zero duplicates. (A broader scan of all rule-ID *mentions*, including legitimate cross-references from `smoothui.md` to `A11Y-002`/`A11Y-005`/`A11Y-007`/`A11Y-008`/`PERF-002`/`SLOP-007`/`SLOP-008`, correctly shows repeat counts >1; this is expected reference behavior, not duplication, and matches how `reicon.md`/`kinetics.md` already reference existing rules.)
- Confirmed no new pipeline stage, routing axis, classifier, or scoring mechanism was introduced — `smoothui.md`'s Validation section is qualitative checklist prose, matching `reicon.md`/`kinetics.md`'s existing "No numerical scoring is introduced" pattern.
- Confirmed SmoothUI is T4 only — added to the existing T4 table row, no new row or tier created.
- Confirmed existing project component systems take precedence (Existing Project Safety section, Precedence P4).
- Confirmed explicit user instruction remains authoritative (Precedence P2, stated before P4).
- Confirmed SmoothUI cannot become a design-direction input — Non-Activation section explicitly excludes deciding whether/what a component should be; Purpose and "What SmoothUI Must Never Be Used to Justify" sections both restate this.
- Confirmed no technical claims (package names, APIs, install commands, component inventories, framework integrations) were invented — the file's own Scope note states this constraint and cites `PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10C as the only verified source material, exactly as `reicon.md`/`kinetics.md` already do for their respective libraries.
- Confirmed documentation lands at the exact required path: `benchmarks/phase-7/PHASE-7.4-SMOOTHUI-INTEGRATION.md`. No Phase 7.4 directory was created. Nothing was left in the repository root.

## Residual Risks

1. **No verified SmoothUI technical detail exists in this repository.** Exactly as with Reicon and Kinetics, `smoothui.md` cannot specify install steps, package name, or component inventory because none is evidenced in the repo's own source material. This is intentional (per the task's Technical Honesty requirement) but means the file is purely architectural until a future phase supplies verified technical detail.
2. **No dedicated "existing component system" detection step exists in `existing-project-safety.md` §1's Inspect scan** — item 6 (framework/dependency detection) is the closest existing hook, reused here as it's the only one available, but it's more general-purpose than the "motion-library presence" line Kinetics could hook into directly. A future correction could add an explicit component/design-system-library detection line to §1, mirroring the motion-library line, if this proves insufficient in practice.
3. **`SKILL.md` §9 Principle 11's 3+-uses/same-intent threshold is judgment-based, not mechanically checkable** — `smoothui.md` reinforces rather than changes this, so the same pre-existing ambiguity about what counts as "same intent" carries forward unchanged.
4. **Convergence risk flagged by the Phase 7 benchmark itself** (§10C: "layering a shared component-implementation source on top without discipline could accelerate visual sameness") is a real, named risk this integration does not eliminate — it is mitigated only by the same discipline (Anti-Slop registry, Register/Genre/Dials, Principle 11) already governing every other implementation choice, not by anything SmoothUI-specific.

## Final Verdict

**PASS.** SmoothUI is integrated as a T4 implementation source, structurally parallel to Reicon and Kinetics, fully subordinate to the existing Authority Hierarchy, Existing-Project Safety, and Anti-Slop discipline. No parallel authority system, new pipeline stage, routing axis, classifier, or scoring mechanism was introduced. No technical claims were fabricated. Minimal-change requirement met: exactly the three files named in the task were touched.
