# SmoothUI (T4)

SmoothUI is an **implementation source for already-justified components and UI patterns** — a carrier/implementation surface, not a design-direction input, the same role `reicon.md` plays for iconography and `kinetics.md` plays for motion. It answers *how* an already-decided component or interaction pattern gets implemented; it never answers *whether* the interface should have that component. That question is resolved entirely upstream — by the brief, `SHAPE`'s structural decisions, `layout-interaction.md`, and `SKILL.md` §9 Core Principle 11 (extract a reusable component only at 3+ uses with the same intent) — before this file is ever consulted.

**Scope of this document:** this file governs when SmoothUI is available as a component implementation source and how its use stays subordinate to the existing component-system, design-system, and Anti-Slop discipline. It does not specify SmoothUI's install steps, package name, API surface, or component inventory — none of that is verified from this repository's own source material (`PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10C only establishes SmoothUI as an optional component-implementation source, coexisting as "an implementation shortcut for a brief-derived pattern already decided by DIRECT, never a substitute for deciding the pattern," gated by progressive disclosure). Resolve implementation specifics against SmoothUI's own documentation at BUILD time, against whatever stack the project actually uses (`existing-project-safety.md` §1) — never fabricate them here.

---

## Purpose

Every component or UI pattern a project needs — a filter-chip set, a modal dialog, a card system, a rule-segmented list — still has to be built by something. SmoothUI supplies an implementation for a component or pattern that the brief, `SHAPE`, and the existing design system have already established as needed, instead of hand-building that layer from scratch each time. It exists to reduce genuine, repeated implementation cost for an already-decided pattern — never to decide which patterns the interface should have.

## Activation

Consider SmoothUI when:
- a component or UI pattern is already justified — by the brief, `SHAPE`'s structural decisions, an explicit UX requirement, or explicit user instruction, **and**
- either:
  - the component's existence and role have already cleared `SKILL.md` §9 Core Principle 11 (justified by repeated use with the same intent, not a one-off) when reusable component abstraction is being considered, or
  - the user has explicitly requested SmoothUI for this implementation, **and**
- no existing project component system, design system, or shared component library already covers it, or the user has explicitly requested migration to SmoothUI.

This applies once a component decision already exists — at BUILD, implementing something already decided — never earlier in the pipeline, and never as the reason a component gets added or a one-off gets abstracted. An explicit request to use SmoothUI does not by itself justify extracting a reusable component or abstracting a one-off; `SKILL.md` §9 Core Principle 11 still governs whether abstraction is warranted.

## Non-Activation

Do not load this file or consider SmoothUI for:
- typography-only, copy-only, or static-content work with no component or UI-pattern requirement;
- deciding whether a component or pattern is needed, what it should do, or whether it belongs in the design system — those decisions belong entirely upstream (brief, `SHAPE`, `SKILL.md` §9 Principle 11), before this file is ever consulted;
- a pattern that appears once and has no independent reuse justification, unless the user has explicitly requested SmoothUI for that specific implementation — even then, SmoothUI's availability is never itself a reason to componentize the one-off;
- an existing project whose component system or design system is being preserved and needs no new pattern;
- justifying the addition of a component that wouldn't otherwise be needed — SmoothUI's availability is never itself a reason to add a component.

## Precedence

Resolved via the existing Authority Hierarchy (`SKILL.md` §3), not a parallel SmoothUI-specific ordering:

1. **P1 safety/correctness** — the accessibility floor (`A11Y-002` keyboard operability + `:focus-visible`, `A11Y-005` touch target size, `A11Y-007` form-field state bugs, and the rest of the P1 list). Non-negotiable.
2. **P2 explicit user instruction** — a named component library, a specific implementation approach, or "no SmoothUI." Follow it. Never silently substitute SmoothUI.
3. **P3 Register/Genre/established design direction** — the direction already committed at DIRECT/SHAPE. SmoothUI conforms to it, never overrides it.
4. **P4 existing project component/design system** — an established component library, shared component set, or design system already in use (`existing-project-safety.md` §1–§2). Preserve it. SmoothUI applies only where a required component genuinely isn't covered by that system, or the user explicitly requests migration.
5. **P5 UX purpose and product requirements** — the component's role must already be established as genuinely needed, per `SKILL.md` §9 Core Principle 11 and the brief/`SHAPE` decisions.
6. **P6 Anti-Slop/distinctiveness** — a SmoothUI implementation still has to clear the same registry as any other implementation (see Anti-Slop below).
7. **SmoothUI, for an already-justified component with no established implementation** — the point at which this file is actually consulted, once (1)–(6) all clear.
8. **Other/custom implementation** — only when justified (SmoothUI doesn't fit the implementation constraints, a specific technical constraint rules it out, etc.), stated as a deliberate choice rather than a fallback. A specific technical constraint can include the source/package/API being genuinely unverifiable or unusable in the current build environment — this is genuine inability to verify or use the source, not absence of effort, and is never invoked merely because the source wasn't investigated, nor because the project is greenfield or has no build step. When `.design/context.md` exists, record this deliberate choice under its existing Known Exceptions section (`SKILL.md` §5).
9. **P7 performance/production hardening** — the general performance-hardening rule category binds any SmoothUI component — or its Other/custom substitute — exactly as it binds a hand-built one.
10. **P8 aesthetic preference** — lowest precedence, exactly as `SKILL.md` §3 already orders it.

## Existing Project Safety

Per `existing-project-safety.md`: an established component system or design system is preserved by default (Improve, not Replace). SmoothUI's availability is never grounds to migrate or replace it. Never replace a working component merely because SmoothUI provides an alternative. Migration requires the same explicit confirmation any Replace-classified change already requires under that file. SmoothUI is considered only for a genuine implementation gap, an explicit migration request, or explicit user instruction — never as a default swap-in for something that already works. Detected via `existing-project-safety.md` §1's Inspect scan (frontend framework and existing dependencies, item 6), the same scan step that already surfaces an established component or design-system library before any design decision is made.

## Greenfield

For a genuinely new project, the order is fixed: first determine whether a component or pattern is actually required, then determine its role and behavior, then determine whether it belongs in the design system (`SKILL.md` §9 Core Principle 11 — 3+ uses with the same intent). Only once all three are settled may SmoothUI be considered as an implementation source, and only when no existing project system or explicit user instruction already governs the implementation.

The project's stack is settled independently of SmoothUI (explicit user instruction or the project's own engineering decision) and is never selected or changed to make SmoothUI usable; if the settled stack cannot host SmoothUI, that is the "unusable in the current build environment" case under Precedence item 8, while the mere absence of a build step yet, on a stack that can host it, is not.

## Design-System Interaction

SmoothUI does not weaken, replace, or bypass `SKILL.md` §9 Core Principle 11. A pattern used once still does not get extracted into a reusable component merely because SmoothUI makes the implementation easy — the same-intent/3+-uses threshold applies identically whether the implementation source is hand-written or SmoothUI. SmoothUI must never be used to justify over-componentizing an interface: it fills an abstraction already justified by repeated use, it does not create the justification.

## Anti-Slop

SmoothUI is a tool for implementing an already-justified component — not a reason to add components, and not a "more premium" shortcut. It does not create a new Anti-Slop category, and it does not become a visual-fingerprint dimension: `SKILL.md` §6's five dimensions (macrostructure, typography pairing, color-anchor, density band, motion tier) are unchanged by SmoothUI's presence. A SmoothUI implementation is still governed by the existing registry exactly as a hand-built one is — most directly `anti-slop-registry.md` SLOP-007 (uniform "SaaS-card kit" cardification) and SLOP-008 (glassmorphism/component material reached for as an unconsidered default). SmoothUI changes an implementation's *source quality*, not whether the pattern itself, its density, or its visual treatment was warranted. Card usage, button hierarchy, page structure, spacing, typography, color, visual style, density, and interaction model all remain governed entirely by the existing skill architecture (Register/Genre/Dials, the rule catalog, Anti-Slop) — SmoothUI does not dictate any of them.

## Accessibility

Governed entirely by the existing rule catalog — most directly `rule-catalog/accessibility.md` `A11Y-002` (keyboard operability + `:focus-visible`), `A11Y-005` (touch target size), `A11Y-007` (form-field state bugs), and `A11Y-008` (never disable zoom), plus the general P1 accessibility floor in `SKILL.md` §3. This file adds no accessibility rules of its own; it defers. A SmoothUI component with unresolved keyboard operability, focus visibility, or form-state behavior is not production-ready and must not be treated as automatically usable until those requirements are met for that component specifically.

## Performance

Governed entirely by `rule-catalog/performance-hardening.md`'s existing rule category (including `PERF-002`'s LCP-lazy-loading constraint where a SmoothUI component sits above the fold). A SmoothUI component is subject to the same performance constraints as any hand-written implementation — no SmoothUI-specific performance scoring exists or is introduced. Bundle-weight and dependency-footprint tradeoffs of adopting a SmoothUI component are evaluated the same way any new dependency is evaluated under this skill's existing discipline (`SKILL.md` §9 Core Principle 12 — leverage over coverage; `existing-project-safety.md` §2's Replace threshold for introducing a new dependency).

## Relationship to Reicon and Kinetics

The three implementation sources are parallel and independent, each subordinate to the same discipline:

- **Reicon** — implementation source for new iconography, once an icon has already been justified.
- **Kinetics** — implementation repertoire for already-justified motion/microinteraction.
- **SmoothUI** — implementation source for already-justified components/UI patterns.

None of the three creates design demand. None answers whether the interface needs an icon, motion, or a component — only how an already-decided need gets implemented. The governing sequence is identical across all three: first decide what the interface needs, then decide how it should behave and look, only then consult an implementation source if useful. Never reverse that order.

## Validation

Qualitative, not scored:
- Is this component or pattern genuinely needed here, independent of SmoothUI being available?
- If reusable component abstraction is being considered: has it already cleared `SKILL.md` §9 Core Principle 11 (3+ uses, same intent — not a one-off)? If SmoothUI was explicitly requested for a specific implementation instead: does the implementation stay within that requested scope, without using SmoothUI's availability to justify abstracting it?
- Does an existing project component or design system already solve this?
- Does it fit the established Register/Genre/visual direction?
- Does it clear the Anti-Slop registry (SLOP-007, SLOP-008, and any other applicable entry) on its own merits?
- Does it meet the accessibility floor (`A11Y-002`, `A11Y-005`, `A11Y-007`, `A11Y-008`)?
- Does it introduce unnecessary performance or dependency cost beyond what the requirement justifies?
- Is the component solving a UX problem, not decorating the interface?

No numerical scoring is introduced.

## What SmoothUI Must Never Be Used to Justify

- Adding a component or pattern the brief, `SHAPE`, or the user didn't already establish as needed.
- Abstracting a one-off into a reusable component below the 3+-uses/same-intent threshold.
- Replacing an existing project's working component or design system absent a genuine gap, explicit migration request, or explicit user instruction.
- A visual style, density, spacing, color, or motion decision — those remain governed entirely by Register/Genre/Dials and the rule catalog, not by what SmoothUI ships.
- Iconography bundled inside an adopted component — an icon a SmoothUI component ships with still needs to independently clear `reicon.md`'s own need/role test, the same as any other icon; it does not bypass that test merely because it arrived as part of the component's default markup. An existing project icon system or explicit user instruction governing icons remains authoritative regardless, and a bundled icon that is already justified and appropriate does not need to be replaced.
- Motion bundled inside an adopted component (transitions, press-scale, enter/exit animation): it must independently clear `rule-catalog/motion.md` (need and purpose via MOTION-001/002; MOTION-004 through MOTION-009 at VALIDATE) exactly as hand-written motion does, which puts `motion.md` in scope whenever such a component is adopted. It does not route through `kinetics.md`, since no motion implementation is being sourced. An existing project motion system or explicit user instruction remains authoritative, and bundled motion that already clears those rules does not need to be removed.
- Treating "SmoothUI has this component" as evidence the interface should use it.
