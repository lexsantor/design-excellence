# Kinetics (T4)

Kinetics is an **implementation repertoire for already-justified motion and microinteraction** — a carrier/implementation surface, not a design-direction input, the same role `reicon.md` plays for iconography. It answers *how* an already-decided motion or microinteraction behavior gets implemented; it never answers *whether* the interface should move. That question belongs entirely to `rule-catalog/motion.md` (MOTION-001 through MOTION-011) and `SKILL.md` §4's `MOTION_INTENSITY` dial, and is resolved before this file is ever consulted.

**Scope of this document:** this file governs when Kinetics is available as a motion implementation source and how its use stays subordinate to the existing motion system, `MOTION_INTENSITY`, and accessibility/performance rules. It does not specify Kinetics' install steps, package name, API surface, or pattern inventory — none of that is verified from this repository's own source material (`PHASE-7-CROSS-PROJECT-ANALYSIS.md` §10B only establishes Kinetics as a candidate motion/microinteraction repertoire, subordinate to `MOTION_INTENSITY` and existing motion systems). Resolve implementation specifics against Kinetics' own documentation at BUILD time, against whatever stack the project actually uses (`existing-project-safety.md` §1) — never fabricate them here.

---

## Purpose

Kinetics supplies implementation patterns for a motion or microinteraction behavior that `motion.md` and `MOTION_INTENSITY` have already established as needed — instead of improvising an ad-hoc transition, spring, or gesture response from scratch. It exists to give an already-justified motion decision a better implementation, never to justify motion that wasn't already decided.

## Activation

Consider Kinetics when:
- a motion or microinteraction behavior is already justified — by `motion.md`'s purpose vocabulary (`MOTION-002`), an explicit UX requirement, the established design direction, or explicit user instruction, **and**
- the `MOTION_INTENSITY` band already selected (`SKILL.md` §4) permits the behavior in question, **and**
- no existing project motion system, transition language, or animation utility already covers the behavior, or the user has explicitly requested migration to Kinetics.

This applies once a motion decision already exists — at BUILD, implementing something `motion.md`/DIRECT/SHAPE already decided — never earlier in the pipeline, and never as the reason a motion decision gets made.

## Non-Activation

Do not load this file or consider Kinetics for:
- typography-only, static-layout-only, or copy-only work;
- a task with no motion or microinteraction requirement;
- pure visual polish where motion is untouched;
- an existing project whose motion system is being preserved and needs no new behavior;
- deciding whether the interface should move, or raising `MOTION_INTENSITY` — that decision belongs entirely to `motion.md`/`SKILL.md` §4, upstream of this file;
- justifying the addition of motion that wouldn't otherwise be needed — Kinetics' availability is never itself a reason to animate something.

## Precedence

Resolved via the existing Authority Hierarchy (`SKILL.md` §3), not a parallel Kinetics-specific ordering:

1. **P1 safety/correctness** — `MOTION-007`'s reduced-motion handling and the rest of the P1 accessibility floor. Non-negotiable.
2. **P2 explicit user instruction** — a named animation library, a specific motion style, or "no motion." Follow it. Never silently substitute Kinetics.
3. **P3 Register/Genre/established motion direction** — the Genre-derived motion posture (`style-catalog.md` `motion_tier_default`) and any direction already committed at DIRECT/SHAPE. Kinetics conforms to it, never overrides it.
4. **P4 existing project motion system** — an established transition language, animation utility, or motion library already in use (`existing-project-safety.md` §1–§2). Preserve it. Kinetics applies only where a required behavior genuinely isn't covered by that system, or the user explicitly requests migration.
5. **P5 UX purpose** — the specific behavior's role (feedback, state transition, spatial continuity, hierarchy/reveal, orientation, gesture response, confirmation, progressive disclosure) must already be established, per `MOTION-002`.
6. **Kinetics, for an already-justified behavior with no established implementation** — the point at which this file is actually consulted, once (1)–(5) all clear.
7. **Other/custom implementation** — only when justified (Kinetics doesn't fit the implementation constraints, a specific technical constraint rules it out, etc.), stated as a deliberate choice rather than a fallback. A specific technical constraint can include the source/package/API being genuinely unverifiable or unusable in the current build environment — this is genuine inability to verify or use the source, not absence of effort, and is never invoked merely because the source wasn't investigated. When `.design/context.md` exists, record this deliberate choice under its existing Known Exceptions section (`SKILL.md` §5).
8. **P7 performance/production constraints** — `MOTION-004`'s property restriction and the general performance-hardening rules bind any Kinetics pattern — or its Other/custom substitute — exactly as they bind hand-written motion.
9. **P8 aesthetic preference** — lowest precedence, exactly as `SKILL.md` §3 already orders it.

## Motion Need

Kinetics never creates the need for motion. The need is established entirely upstream, by `motion.md`'s decision sequence (should it animate → purpose → interaction type → property → easing → duration → interruptibility → accessibility → performance) and by `SKILL.md` §4's `MOTION_INTENSITY` band. "Kinetics has a nice pattern for X" is never sufficient justification to add X — the same discipline `reicon.md` applies to iconography applies here to motion.

## Motion Intensity

`MOTION_INTENSITY` (`SKILL.md` §4) remains fully authoritative and is not modified, extended, or shadowed by a second scale. Kinetics conforms to whichever band (Low/Medium/High) is already selected:

- **Low band** — Kinetics may supply an implementation for the single orchestrated moment or feedback/state-transition purpose the band already permits; it does not license more motion than the band would otherwise allow.
- **Medium band** — same conformance; Kinetics is a source for how a Medium-band-eligible purpose gets implemented, not a reason to reach Medium from Low.
- **High band** — Kinetics may supply richer patterns (per `MOTION-011`'s existing bounce/elastic conditional eligibility), still governed entirely by the rules that already apply at High band, not by anything specific to Kinetics.

If `motion.md`'s existing rules restrict an effect at the currently selected band, Kinetics remains subordinate to that restriction — it carries no exemption of its own.

## Selection

Select a Kinetics implementation pattern only after the motion behavior itself is already decided:
- What purpose does this motion serve, from `MOTION-002`'s fixed vocabulary?
- What band does `MOTION_INTENSITY` currently permit, and does the pattern fit inside it?
- Does an existing project motion system already solve this?
- Is a plain CSS transition/spring sufficient, without reaching for a repertoire at all?

Kinetics fills an already-decided behavior; it does not decide the behavior.

## Existing-System Safety

Per `existing-project-safety.md`: an established motion system, transition language, or animation utility is preserved by default (Improve, not Replace). Kinetics' availability is never grounds to migrate an existing system. Migration requires the same explicit confirmation any Replace-classified change already requires under that file. Kinetics is considered only when the existing system has a genuine gap for a newly required behavior, the user explicitly requests Kinetics, or the project is explicitly migrating/replacing its motion implementation.

## Accessibility

Governed entirely by `rule-catalog/motion.md` `MOTION-007` (`prefers-reduced-motion`: gentler, not zero) and `rule-catalog/accessibility.md` `A11Y-003` (which points to `MOTION-007` as its full specification). This file adds no reduced-motion rules of its own; it defers. A Kinetics pattern with no meaningful reduced-motion treatment is not production-ready and must not be treated as automatically usable until `MOTION-007`'s requirement is met for that pattern specifically — do not invent a reduced-motion behavior not supported by the repository's existing rules; resolve it against `MOTION-007`'s actual requirement (keep opacity/color transitions that aid comprehension, drop movement/position changes) at implementation time.

## Performance

Governed entirely by `rule-catalog/motion.md` `MOTION-004` (property restriction), `MOTION-005` (duration budget), `MOTION-006` (interruptibility), and the general performance-hardening rule category. A Kinetics pattern is subject to the same property/duration/interruptibility constraints as any hand-written motion — no Kinetics-specific performance scoring exists or is introduced. Kinetics must not be used to introduce unnecessary continuous animation, expensive effects, or excessive simultaneous animation beyond what the already-established UX purpose and `MOTION_INTENSITY` band justify.

## Anti-Slop

Kinetics is a tool for implementing already-justified motion — not a reason to increase animation, and not a "make it feel more premium" shortcut. It does not create a new Anti-Slop category, and it does not become a fingerprint dimension: `SKILL.md` §6's five dimensions (macrostructure, typography pairing, color-anchor, density band, motion tier) are unchanged — Kinetics is an implementation source inside the existing motion-tier dimension, not a new one. Motion implemented via Kinetics still needs a concrete UX role from `MOTION-002`'s vocabulary (feedback, state transition, spatial continuity, hierarchy/reveal, orientation, gesture response, confirmation, progressive disclosure) — decoration alone, generic hover effects everywhere, gratuitous entrance animation, excessive scroll choreography, and identical "premium" motion recipes reused across unrelated projects remain exactly as ungrounded with Kinetics available as without it.

## Validation

Qualitative, not scored:
- Is motion genuinely needed here, independent of Kinetics being available?
- What UX role does it serve, from `MOTION-002`'s vocabulary?
- Does it fit the already-selected `MOTION_INTENSITY` band?
- Does it respect `MOTION-007` reduced-motion behavior?
- Does it fit the established Register/Genre/visual direction?
- Does an existing project motion system already solve this?
- Does it introduce unnecessary performance cost beyond `MOTION-004`'s constraints?
- Is the pattern solving a UX problem, not decorating the interface?

No numerical scoring is introduced.
