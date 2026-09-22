READY FOR IMPLEMENTATION

  Problem definition

  Five distinct things, easy to conflate:

  - Generic high-quality design — technically correct, accessible, well-classified (Register/Genre/Dials fit the brief's category), but the specific choices made are the ones any
    competent execution of that category would make. Not wrong, just unearned.
  - AI slop — recognizable generation artifacts: current-model tells (italic emphasis, eyebrow labels, arrow-on-every-CTA, gradient text, specific hex clusters). This is a
    negative/ban-list problem. anti-slop-registry.md targets it directly and well (SLOP-001 through SLOP-019).
  - Visual distinctiveness — the output differs from this system's own prior output on the same project, across sessions. A self-comparison problem. The Visual Fingerprint (SKILL.md §6, 5
    mandatory dimensions, 2-of-5 threshold) targets it directly.
  - Conceptual distinctiveness — the output's specific character is traceable to this brief's actual meaning, not swappable for another brief in the same category. Nothing in the current
    architecture measures this.
  - Structural expression — a concept is legible in the page's organizing logic (macrostructure, navigation, content architecture, section transitions, interaction), not only in its
    decoration (motif, copy, color, imagery). This is the specific, narrow thing PHASE-6.2 found missing.

  The current skill handles the first three well because each has a purpose-built mechanism: Anti-Slop (ban-list against known-bad patterns), Fingerprint (self-comparison against project
  history), Genre/Register/Dials (category-level posture classification). None of the three asks whether the macrostructure/navigation/content-architecture choice was derived from the
  brief's specific idea versus from Genre's default posture. LAYOUT-001 governs how to commit to a macrostructure as one atomic bundle; it has no requirement that the bundle be
  concept-derived. LAYOUT-008 (imagery) and CD-1 (EXPLORE) are both Phase 6 additions aimed at distinctiveness, but neither requires the distinguishing content to be brief-specific rather
  than aesthetic-preference-specific.

  PHASE-6.2-RESULTS.md is precise evidence for this, not a hypothetical: EXPLORE ran correctly (two genuinely distinct candidates, cross-checked against style-catalog.md), Genre inference
  resisted a self-reference shortcut, LAYOUT-008's imagery procedure ran as a real recorded decision, mechanical validation caught real defects, Level 2 critique genuinely dispatched and
  found real bugs — every existing mechanism functioned as designed, and the concept still ended up "well-argued in copy and rendered as one decorative SVG motif" while "the nav, hero
  pattern, alternating-band sections, numbered list, anchor CTA band, and footer could serve another premium professional-services brand with only the copy swapped." That is a missing
  decision, not a broken one — nothing in the current pipeline ever asks the question this gap requires.

  Proposed Concept → Expression model

  Reject the prompt's own literal example ("concept = cartography" → "add contour lines") as the failure mode to design against — it skips the one step that matters. Minimum useful chain,
  three steps, each a recorded artifact rather than an internal jump:

  1. Brief concept — the specific idea/metaphor as stated or evidenced in the brief (not invented).
  2. Abstract structural principle — the concept stripped of its literal imagery, restated as a relationship or logic that could organize content, not something that could be drawn.
     ("Atlas: a vertebra everything balances on, a map that orients before it details" → candidate: "a single fixed reference point the rest of the content orients around" — a structural
     claim, not a visual one.)
  3. Selected structural expression — which surface (§ below) the principle actually manifests on, chosen during DIRECT's existing EXPLORE comparison, recorded with the surface named and
     the rejected alternative's surface named too.

  This is deliberately the same shape as TYPE-002's font-selection procedure and LAYOUT-008's imagery procedure — a generative decision sequence, not a constraint, not a catalog, reusing
  the existing Rejected Directions mechanism rather than creating a new record type.

  Recommended name: Concept → Structure, not Concept → Expression. "Expression" is ambiguous with decorative expression (the exact failure mode being corrected); "Structure" states the
  required destination explicitly.

  Activation criteria

  Fires only when the brief itself supplies real evidence of a concept: the brief spends real space explaining why a name/symbol/idea was chosen, explicitly asks for an idea to be
  "felt"/"embodied"/"woven through," or gives a recurring reference object central to identity (not just a logo asset to place). This is a DEFINE-stage reading judgment, the same kind of
  call Genre inference already makes — not a keyword scanner.

  Does not activate: Register = product-led generally (Register already caps expressiveness; forcing concept-translation onto a utility interface is exactly the risk the prompt names);
  briefs with no stated concept at all (inventing one would violate Core Principle 8 / the P1 no-fabrication gate); any task with no path into DIRECT (component/section POLISH — Hard
  rule, §1, untouched).

  Pipeline integration

  Two touch points, no new stage:

  - DEFINE — detection only. One sub-question folded into the existing register/genre declaration moment: does the brief supply real concept evidence, yes/no with reason. Cheap,
    T0/T1-tier.
  - DIRECT — translation and selection, folded into the existing CD-1 EXPLORE step (SKILL.md §1). When DEFINE flagged a concept, the abstract structural principle becomes an additional
    input to the 2-candidate comparison already happening there.

  Primarily a DIRECT concern with a DEFINE trigger. Not DESIGN — DESIGN generates the token/visual system, which is exactly the layer PHASE-6.2 showed already carries the concept fine
  (copy, motif, color). Not SHAPE — SHAPE builds whatever DIRECT already committed to; it needs no new logic, only a better-specified input.

  Relationship to other mechanisms: Register/Genre/Dials set posture and ceiling, unchanged, evaluated as normal — concept operates within them. Fingerprint is unaffected
  (self-comparison, orthogonal axis). Anti-Slop is unaffected (ban-list, orthogonal axis). Design System generation (tokens/components, ARCHITECTURE.md §19) is unaffected — only the
  macrostructure/content-architecture choice that LAYOUT-001 already requires gets a concept-derived reason when one exists. Content architecture is one of the surfaces this feeds into,
  not a separate concern.

  Relationship to EXPLORE

  Option C — concept defines a constraint/abstract principle; EXPLORE produces different structural interpretations of it.

  Option A (concept before EXPLORE, informing both candidates) risks both candidates converging on the same structural translation of the concept, reducing EXPLORE to aesthetic-only
  variants — the exact convergence PHASE-6-PLAN-FINAL.md's own guardrail warns against ("must not trade one unconsidered convergence for another"). Option B (concept after candidate
  selection) risks the Atlas failure exactly reproduced: pick a direction for aesthetic reasons, retrofit a motif on top afterward.

  Option C keeps EXPLORE's existing job intact and extends it minimally: DEFINE's detection produces the concept + a candidate abstract principle before DIRECT, as an input alongside
  Register/Genre/Dials/Product Truth (same status as those, not a new authority layer). EXPLORE's two candidates are then required, only when a concept was detected, to propose different
  structural interpretations of that principle — meaning at least one of CD-1's already-required ≥2 distinguishing dimensions (composition, interaction, or a structural axis named
  alongside them) is where the two candidates diverge on how the concept manifests structurally. No new dimension list — CD-1's existing six dimensions already include the structural ones
  needed (composition, interaction); this just points the existing naming discipline at structure when a concept exists.

  Relationship to Register / Genre

  Unchanged as classification mechanisms. Concept detection is Product-Truth-adjacent (subject-specific, captured at DEFINE alongside subject/audience/primary job) but does not alter
  Register's ceiling or Genre's default posture — it operates within whatever they set. A brand-led/editorial classification and a concept-derived macrostructure choice are independent
  decisions; the concept never overrides what Register/Genre already license.

  Relationship to Design Dials

  No new dial, none proposed. Concept-expression is dial-neutral by design: it operates within whatever DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY bands Register/Genre/brief-language
  already set. It must never be used to justify raising a dial band ("we have a concept, so more motion/color is warranted") — that would smuggle in exactly the visual-complexity default
  the prompt explicitly rules out. It informs what structural logic is chosen, never how much visual intensity is licensed.

  Relationship to Anti-Slop

  Architecturally distinct, not overlapping, on two axes at once:

  - Direction: Anti-Slop is subtractive (a ban-list against known-bad patterns — SLOP-011's self-tell clusters, SLOP-013's category-reflex palette). Concept-expression is generative
    (derive a structural choice from this specific brief). A palette can cleanly pass SLOP-013 (not category-stereotyped) while still being conceptually arbitrary — has nothing to do with
    the brief's actual idea. Passing the ban-list says nothing about brief-derivation.
  - Surface: the entire Anti-Slop Registry, by its own scope note, is populated from typography/color/layout-decoration tells (italics, eyebrows, gradients, card kits). None of it
    evaluates macrostructure/content-architecture/navigation derivation — which is exactly the class of surface PHASE-6.2's gap lived on, and exactly why a ban-list mechanism couldn't
    have caught it regardless of how complete the registry is.

  Fingerprint compares this project's output against its own history (repetition, cross-session). Concept-expression compares this output against this brief's own meaning (derivation,
  single-session). Four genuinely separate axes — Anti-Slop, Fingerprint, Register/Genre, Concept-Structure — none of which subsumes another, confirmed empirically by PHASE-6.2: all three
  existing axes functioned correctly and the gap still occurred.

  Expression surfaces

  From the prompt's list, split by what can organize versus what can only carry:

  Organizing surfaces (capable of structural expression): macrostructure, content architecture, navigation, section transitions, interaction.
  Carrier surfaces (reinforce but rarely constitute structure alone): typography, color, spacing, imagery, iconography, motion, grid, responsive behavior.

  Structural = the concept determines an organizing decision — something that, if changed, requires re-deriving how content is grouped, sequenced, navigated, or transitioned. Decorative =
  the concept appears in an element that could be deleted without changing how a user moves through or organizes the content (a motif SVG, an "evocative" color, a themed icon set).

  Minimum evidence bar: at least one of the five organizing surfaces carries a decision traceable to the abstract structural principle, not just to the concept's literal imagery. One
  surface is sufficient — do not require more; requiring multiple risks forcing decoration onto surfaces just to hit a quota, which is the prompt's own explicit non-goal.

  Structural test

  "Would the concept still be perceptible if the logo, color palette, imagery, and copy were removed?" — this is literally the test PHASE-6.2's Level 2 reviewer already applied unprompted
  ("cover the logo").

  Useful: yes — cheap, qualitative (matches the explicit instruction against a numeric score), and it's exactly what caught the real, only-known instance of this gap.

  When applied: best suited to Level 2 (independent, fresh-context critique), not Level 1. Mentally subtracting logo/color/copy requires not being anchored on the choices that were just
  made — a self-critique pass authored by the same context that made the decorative choices is structurally poorly positioned to apply it objectively. This is the same reasoning
  critique-protocol.md already gives for why Level 2 exists at all.

  Reveals: whether the concept lives in organizing decisions or decoration only.

  Limitations: (1) qualitative, reviewer-judgment-dependent, not mechanically verifiable; (2) a "no" is not automatically a failure — many legitimate designs are concept-in-voice-only by
  deliberate choice (a product-led interface should often fail this test, and forcing a "yes" there violates the "not every project needs to be metaphorical" non-goal); (3) gameable
  post-hoc if used alone — pairs with the recorded Concept→Principle→Surface chain (§ above) so the reasoning is auditable, not just a pass/fail vibe check.

  Validation / Critique integration

  Level 1 — one-line addendum to axis 1 (Genericness), parallel to how AS-1 already added the SLOP-011 gestalt sub-check to the same axis: when DEFINE flagged a concept, Genericness's
  existing question ("would this be produced for any similar brief") is sharpened by the structural test. No new axis.

  Level 2 — when Level 2's existing trigger conditions fire (this is exactly Atlas's own trigger class: genuinely-empty, multi-page-site BUILD, explicit brand-quality bar), the dispatched
  reviewer's brief explicitly includes the structural test as one instruction. This formalizes behavior PHASE-6.2's reviewer already produced organically — documenting a
  demonstrated-good pattern, not inventing a new one.

  VALIDATE/HARDEN — no new mechanical gate. This is a qualitative judgment by construction (explicit instruction against a numeric score); it stays in the critique layer.

  Is existing critique architecture sufficient? Mostly — one small addition needed. LAYOUT-001 (bundle-commitment mechanics), LAYOUT-008 (imagery medium), and the
  accessibility/motion/color/typography catalogs never touch macrostructure/content-architecture derivation, so a net-new rule is justified. It should be the smallest possible one: a
  critique-protocol.md addendum sentence (AS-1's exact precedent) plus one rule-catalog entry (§ below) — not a new numbered critique axis, not a new file.

  Clínica Atlas retrospective

  What Concept→Structure would have extracted: "Atlas" — the C1 vertebra everything above balances on, plus a cartographic/orientation reference.

  Plausible abstract structural principles it might have produced (illustrative, not the answer): "a single fixed reference point the rest of the content orients around";
  "position/orientation established before detail"; "a load-bearing hierarchy — one foundational element other sections visibly relate back to." Several readings are legitimate; which one
  gets picked is DIRECT's job, not this retrospective's.

  Structural surfaces it could plausibly have influenced (illustrative, not prescribed): macrostructure (one anchor element other sections relate back to, versus an undifferentiated
  alternating-band stack); navigation (orientation-style wayfinding rather than a generic top nav); content architecture (position-before-detail sequencing rather than generic
  feature-list order); section transitions (movement between reference points rather than a cut). Which of these — if any — is correct is exactly what this proposal does not decide.

  What would have remained optional: which specific surface carries it, whether more than one surface is used at all (one is sufficient per the evidence bar above), and whether the
  selected direction ends up looking dramatically different from what shipped — a concept-derived macrostructure could plausibly still resemble an alternating-band editorial layout; the
  requirement is traceability, not novelty.

  How this makes Atlas more ownable: the reviewer's own "cover the logo" finding is that the current structure is generic-premium-professional-services-swappable. Concept→Structure's
  DEFINE-stage detection would have flagged "Atlas" as strong concept evidence (the brief spends real space on naming rationale), and DIRECT's EXPLORE would then have been required to
  make the concept part of what distinguishes candidate A from candidate B — so whichever direction was ultimately selected would carry a structural rationale traceable to "Atlas"
  specifically, not only to Genre=editorial generically. Whether that rationale ends up expressed through navigation, content architecture, or another surface is not something this
  retrospective settles.

  Complexity / context-cost impact

  - T0 (SKILL.md) growth: ~3–5 sentences across §1 (DEFINE detection trigger, DIRECT/EXPLORE extension) and §5 (Rejected Directions requirement extension) — comparable in size to Phase
    6's CD-1/CD-3 additions. No new Operating Model row, no new stage.
  - No new catalog: the five organizing/seven carrier surfaces are a checklist reused from this proposal, not a populated catalog needing entries or freshness governance.
  - No new T3/T4 file: precedent from TYPE-002 and LAYOUT-008 — both generative decision procedures live as a single rule-catalog entry, not a separate file. Concept→Structure fits the
    same shape and size.
  - T2 growth: one new rule in layout-interaction.md (~250–350 words, comparable to LAYOUT-008's own length) + 1–2 sentences in critique-protocol.md (comparable to AS-1's addition). Both
    files already load whenever DIRECT/CRITIQUE run for page-scope work — zero new load trigger.
  - Net new content: roughly 400–550 words across 3 files, smaller than any single Phase 6 rule-addition category, and it is exactly one new rule ID.
  - No forced metaphor: activation criteria (§ above) gates on real brief evidence; no evidence → no activation → no fabrication risk.

  Files that would change

  1. design-excellence/SKILL.md — §1 (DEFINE row: one detection-trigger sentence; DIRECT/CD-1 paragraph: one sentence tying concept detection to CD-1's existing distinctness dimensions),
     §5 (Rejected-Directions paragraph: extend to name which structural surface each candidate uses, when a concept was detected). No change to §4 — Register/Genre/Dial mechanics stay
     untouched.
  2. design-excellence/references/rule-catalog/layout-interaction.md — one new rule (see below).
  3. design-excellence/references/critique-protocol.md — one addendum sentence to Level 1 axis 1 (parallel to AS-1's existing pattern) + one sentence added to the Level 2 dispatch-brief
     instructions (step 1) noting the structural test is included when a concept was flagged.

  No change to ARCHITECTURE.md, style-catalog.md, anti-slop-registry.md (content unchanged; possibly one optional cross-reference, matching AS-1's own optional-cross-reference precedent,
  but not required), color.md, typography.md, existing-project-safety.md, gesture-physics.md, or any of motion.md/accessibility.md/content-copy.md/performance-hardening.md
  (content-copy.md was not part of this proposal's required reading and is flagged here, honestly, as unverified — if content architecture work turns out to need copy-level rules, that's
  a separate, later question, not assumed here).

  Existing rules that can be reused

  LAYOUT-001 (macrostructure-as-one-atomic-choice) is the natural downstream consumer — Concept→Structure supplies it a reason, doesn't replace its mechanics. CD-1's EXPLORE step
  (SKILL.md §1) is extended, not duplicated. The Rejected Directions mechanism (SKILL.md §5) is reused as-is for recording. AS-1's critique-protocol.md addendum pattern is reused as the
  template for how the structural test gets folded into axis 1, rather than becoming a new axis.

  New rule IDs proposed

  One: LAYOUT-009 — Concept → structural-expression decision procedure (next available id in layout-interaction.md's Layout section, following LAYOUT-008's own numbering and format — a
  generative procedure, layer P6 anti-slop/distinctiveness, matching LAYOUT-001's layer since both are distinctiveness mechanisms). Considered and rejected: folding this into LAYOUT-001
  directly (different question — LAYOUT-001 governs how to commit to a bundle, this governs why; LAYOUT-001 is already dense with Phase 4/6 corrections layered in) or into LAYOUT-008
  (scoped specifically to imagery medium, a different surface).

  Future library compatibility

  Reicon, Kinetics, SmoothUI all sit downstream of DIRECT, where Concept→Structure resolves. Once a structural expression is selected, these libraries supply implementation of it — an
  icon (Reicon), a transition (Kinetics), a component (SmoothUI) — never the decision of what the structure should be. Concretely: if DIRECT selects a structural principle around
  orientation/reference-points, Kinetics is where an implementation of a transition satisfying that already-decided requirement gets sourced — not browsed first and reverse-justified as
  conceptual. No change to Concept→Structure's own architecture is implied by these libraries' eventual arrival; they slot into BUILD/DESIGN, strictly after DIRECT has already committed.

  Risks

  - The DEFINE-stage detection ("does the brief carry a meaningful concept") is a judgment call, not mechanically checkable — same category of risk Genre inference already carries, not a
    new kind of ambiguity introduced.
  - "Meaningfully distinct structural interpretation" in EXPLORE, like CD-1's existing distinctness requirement, is auditable after the fact (named surfaces, recorded reasoning) but not
    mechanically enforced at generation time — same risk profile CD-1 already accepted.
  - A team could over-apply this to briefs with weak concept evidence, forcing structure onto content that doesn't warrant it — mitigated by the activation criteria's explicit "no
    evidence → no activation" gate and by LAYOUT-008's own precedent that "no imagery, deliberately" is a valid answer (here: "no meaningful concept, deliberately" is equally valid).
  - Structural test at Level 2 only fires when Level 2's existing trigger conditions fire — a concept-heavy brief that doesn't meet Level 2's stakes bar (small BUILD, no brand-quality-bar
    language) never gets the test applied by an independent reviewer, only Level 1's lighter self-check. This is an accepted cost-proportionality tradeoff, consistent with the whole
    skill's cost-proportional-to-stakes principle, not an oversight.

  Recommendation

  Implement as scoped: one new rule (LAYOUT-009) in layout-interaction.md, a handful of sentences across SKILL.md §1/§5, and a two-sentence addendum to critique-protocol.md — no new
  pipeline stage, no new file, no new dial, no numeric score. This is the smallest mechanism that closes the specific, evidence-demonstrated gap: none of Anti-Slop, Fingerprint, or
  Register/Genre would organically produce concept-to-structure derivation, confirmed by a benchmark run where all three functioned correctly and the gap still occurred. Treat this
  proposal as ready to schedule as Phase 6.4 implementation; no further research or exploration is needed before writing the actual diff.