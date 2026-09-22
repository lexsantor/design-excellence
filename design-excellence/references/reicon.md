# Reicon (T4)

Reicon is the **default implementation source for new iconography** — a carrier/implementation surface, not a design-direction input. It answers *how* a required icon gets implemented once an icon is already needed; it never answers *whether* an icon is needed or *what role* it should play. Those questions belong to `layout-interaction.md`/`SKILL.md` §4 (Register/Genre/Dials) and are resolved before this file is ever consulted.

**Scope of this document:** this file governs the decision of *when Reicon is the default source* and how the resulting iconography stays coherent with the rest of the design. It does not specify Reicon's install steps, package name, API surface, or icon inventory — none of that is verified from this repository's own source material (`ARCHITECTURE.md` §10A only establishes that Reicon is a candidate default icon library, subordinate to explicit instructions and existing systems). Resolve implementation specifics against Reicon's own documentation at BUILD time, against whatever stack the project actually uses (`existing-project-safety.md` §1) — never fabricate them here.

---

## Purpose

When new iconography is genuinely required and no established icon system or explicit instruction already governs it, Reicon is the default source Claude reaches for — instead of hand-drawing generic SVGs, improvising outline icons, or reflexively pulling from another generic icon set. This exists to prevent the failure mode of shipping generic icons first and replacing them with Reicon later, by making the correct default the first move.

## Activation

Consider Reicon when:
- new iconography is genuinely needed (an icon improves comprehension, navigation, action recognition, or information density — per Selection below), **and**
- no established project icon system already covers it (`existing-project-safety.md` §1 Inspect), **and**
- the user has not named a specific icon library, custom iconography, or "no icons."

This applies at DESIGN/BUILD, once an icon's UX role has already been established — never earlier in the pipeline.

## Non-Activation

Do not load this file or consider Reicon for:
- typography-only, layout-only, or copy-only work;
- a task with no iconography requirement at all;
- pure visual polish where icons are untouched;
- an existing project whose icon system is being preserved, not extended;
- justifying the addition of an icon that wouldn't otherwise be needed — Reicon's availability is never itself a reason to add an icon.

## Precedence

In order:

1. **Explicit user instruction** — a named icon library, a specific icon style, custom iconography, or "no icons." Follow it. Never silently substitute Reicon.
2. **Existing project icon system** — an established icon language already in use (`existing-project-safety.md` §1–§2). Preserve it. Reicon applies only where a required icon genuinely doesn't exist in that system, new functionality needs new iconography the existing system doesn't cover, or the user explicitly requests migration/replacement.
3. **Reicon, for new iconography with no established system** — the default once (1) and (2) don't apply.
4. **Other/custom implementation** — only when justified (Reicon doesn't fit the visual direction, a specific technical constraint rules it out — e.g., the source's package/API cannot be verified or installed in the current build environment — etc.), stated as a deliberate choice rather than a fallback. This is genuine inability to verify or use the source, not absence of effort — never invoked merely because the source wasn't investigated. When `.design/context.md` exists, record this deliberate choice under its existing Known Exceptions section (`SKILL.md` §5).

## Default Behavior

Greenfield project, or a project with no established icon system, genuinely needs new iconography → Reicon is the default source. No additional user instruction is required to reach this default; it is the first move, not a later correction.

## Selection

Select an icon only after its UX/design role is already established:
- What is the icon's purpose — comprehension, navigation, action recognition, information density?
- Would text communicate this more clearly? Prefer text when it does.
- Is this decorative rather than functional? Decorative iconography needs the brief to actually call for it — Reicon's availability is not sufficient justification on its own.

Reicon fills the slot once that role is real. It does not create the slot.

## Consistency

Within a chosen icon set, keep coherent:
- visual weight and stroke/shape language
- optical size and alignment
- semantic clarity (the icon reads as its meaning, not merely "an icon")
- consistent treatment across repeated actions

Don't mix icon families without a stated reason, and don't manually redraw or modify an icon for cosmetic reasons absent a concrete requirement.

## Accessibility

Governed entirely by `rule-catalog/accessibility.md` A11Y-004 (icon accessibility is role-conditional) — decorative-beside-text hidden from the accessibility tree, standalone-meaningful needs a text alternative, interactive-control needs an accessible name and state. This file adds no accessibility rules of its own; it defers.

## Anti-Slop

Reicon is a tool for avoiding generic/basic icon implementation when an icon is already needed — not a reason to increase icon density or make icon use a visible feature of the design. It does not create a new Anti-Slop category. Icon-heavy patterns reached for without a concrete UX reason remain governed by the existing registry (e.g. `anti-slop-registry.md` SLOP-007's card-kit pattern, where icon-per-card is often part of the tell) — Reicon changes the icon's *source quality*, not whether the pattern itself was warranted.

## Existing-System Safety

Per `existing-project-safety.md`: an established icon system is preserved by default (Improve, not Replace). Reicon's availability is never grounds to migrate an existing system. Migration requires the same explicit confirmation any Replace-classified change requires.

## Validation

Qualitative, not scored:
- Is an icon actually needed here?
- Is its meaning clear at the size/context it's used?
- Is the chosen icon appropriate to the specific action/content, not a generic stand-in?
- Does it belong to a coherent icon language with the rest of the interface?
- Does it support the established Register/Genre/visual direction, or conflict with it?
- Is accessibility preserved (A11Y-004)?
- Is the icon solving a UX problem, not decorating the interface?

No numerical scoring is introduced.
