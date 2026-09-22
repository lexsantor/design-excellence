PROPOSAL ONLY — NOT IMPLEMENTED

# Phase 6.4 Proposal — Visual References

## 1. Problem

Phase 6.3 closed a real gap (a brief's concept staying decorative instead of shaping structure — `LAYOUT-009`) and the fix held up under independent critique. But the Clínica Atlas benchmark surfaced a different, narrower problem that Concept → Structure cannot solve because it isn't the kind of gap Concept → Structure targets:

**DIRECT's EXPLORE step compares two candidates, but both candidates are drawn from the same visual-language family.** Genre (`SKILL.md` §4) sets a default posture, and EXPLORE's two candidates — even when they differ meaningfully in composition, interaction, and (per `LAYOUT-009`) structural interpretation of a concept — are generated from inside that one posture's own gravity well. Nothing in the current pipeline ever asks EXPLORE to consider a candidate that draws on a genuinely different visual register than Genre's own default. The result, stated plainly in `PHASE-6.3-RESULTS.md` §F: *"the underlying pattern family... is still a competently-executed instance of a broader editorial-services vocabulary, not a wholly novel one."* That is not a defect in any existing mechanism — it is the boundary of what those mechanisms were built to do.

A second, smaller and genuinely separate problem surfaced in the same benchmark: primary CTAs and the form's submit CTA received different responsive width treatment on mobile (intrinsic-width vs. full-width) with no rule anywhere governing which is correct. This is addressed narrowly in §13, kept decoupled from the Visual References architecture proper.

Five things this proposal is careful not to conflate (the same discipline `PHASE-6.3-PROPOSAL.md` used to scope Concept → Structure correctly):

- **Generic high-quality design** — Anti-Slop's problem.
- **AI slop** (current-model tells) — Anti-Slop's problem.
- **Visual repetition across a project's own history** — Fingerprint's problem.
- **Conceptual distinctiveness / structural expression** — Concept → Structure's problem (`LAYOUT-009`), closed in 6.3.
- **Narrowness of the possibility space explored before committing to a direction** — nothing's problem yet. This is what Visual References targets.

## 2. Evidence from Phase 6.3

Direct citations, not paraphrase:

- `PHASE-6.3-RESULTS.md` §C: Candidate A ("Anchored Datum") and Candidate B ("Ascending Path") differ on composition, interaction, and color — enough to pass the ≥2-of-6-dimensions distinctness check — but both are structural variations *within* editorial genre's own default posture. Candidate B was rejected for a `MOTION_INTENSITY` conflict, not for being a different visual language; Candidate A was never compared against anything outside that family in the first place.
- `PHASE-6.3-RESULTS.md` §E: *"the honest claim is narrower: the structure is consistent with and derived from the concept... not that the structure alone would make a stranger guess the brand name unaided."*
- `PHASE-6.3-RESULTS.md` §F: *"Would this swap into another premium professional-services site? Less easily than before the Level 2 fixes, but not zero... a competently-executed instance of a broader editorial-services vocabulary, not a wholly novel one."*
- `PHASE-6.3-RESULTS.md` §G Gaps: *"Visual quality is improving, but the exploration space needs to widen before selecting a direction. DIRECT generated two candidates and picked between them; it did not range widely enough to test whether a materially different visual language... could have served this brief as well or better."*
- `PHASE-6.3-RESULTS.md` §D/§G, CTA gap: *"Primary CTAs frequently remain intrinsic-width on mobile while the form-submit CTA is full-width... CTA/action hierarchy on mobile is not sufficiently defined."*

Every existing distinctiveness mechanism (Anti-Slop, Fingerprint, Genre inference, Concept → Structure) functioned correctly in that run. The gap still occurred, because none of them ever asks "what does a genuinely different visual register look like for this brief, and did EXPLORE actually consider one?" — that is a missing question, the same shape of finding that justified `LAYOUT-009` in the first place.

## 3. Objective

Build **Visual References**: a lightweight evidence layer that gives DIRECT's EXPLORE step material to draw on when generating its two candidates, so the comparison spans a genuinely wider slice of the possible visual space before commitment — without turning the skill into a copying engine, without adding a pipeline stage, and without the cost of a large reference database.

Core mechanism, stated once and enforced everywhere it applies: **Observe → Abstract → Adapt. Never Copy.**

## 4. Architectural placement

**Proof this doesn't need a new stage.** DIRECT already contains a sub-step — EXPLORE (`SKILL.md` §1, the Phase 6 "Creative exploration inside DIRECT" correction) — whose entire job is: generate two candidates, compare them on named dimensions, commit to one, log the rejected one. `LAYOUT-009` already extended this same sub-step with an additional input (the concept's abstract structural principle) without adding a stage, an Operating Model row, or a cost tier. Visual References is architecturally identical in shape: one more input to a comparison step that already exists and already runs at the right cost (page/multi-page-site scope, BUILD/REDESIGN only, per the Hard rule in `SKILL.md` §1). No case exists in this proposal, in `PHASE-6.3-RESULTS.md`, or in `ARCHITECTURE.md` where the gap requires a new stage rather than a better-informed existing one. New stage: rejected.

**Confirmed flow:**

```
Brief
→ Register / Genre / Dials (DEFINE)
→ Concept → Structure, when applicable (DEFINE detection, DIRECT translation — LAYOUT-009)
→ Visual Reference Evidence (DIRECT, before EXPLORE generates its candidates — new, this proposal)
→ EXPLORE (2 candidates, now informed by both concept translation and reference evidence)
→ selection
→ SHAPE
→ DESIGN
```

Visual Reference Evidence sits at the *opening* of DIRECT, before EXPLORE's two candidates are drafted — not after selection (that would just retrofit a motif onto an already-chosen direction, the exact "Option B" failure mode `PHASE-6.3-PROPOSAL.md` already rejected for Concept → Structure, and the same reasoning applies here without modification).

**Secondary use — CRITIQUE quality bar. Evaluated, not assumed, and rejected for 6.4.** The prompt asks whether the same reference system should also seed a quality bar during CRITIQUE. Three reasons this doesn't earn its cost right now:

1. `LAYOUT-009`'s structural test ("would the concept still be perceptible if logo/color/copy were removed?") already gives Level 2 a concrete, evidence-backed quality bar for exactly the failure mode Atlas exhibited, and it worked — `PHASE-6.3-RESULTS.md` §D shows the independent reviewer catching the gap unprompted, before the mechanism was even formalized.
2. A "does this measure up to reference X" critique bar requires the *same* reviewer to hold the *same* references in mind that DIRECT used — either re-loading the catalog at Level 2 (doubling its context cost inside a stage that is supposed to stay isolated and cheap-floor-first) or trusting the generating session's own selection, which defeats the independence Level 2 exists for (`critique-protocol.md`'s dual-blind isolation principle).
3. No benchmark evidence shows CRITIQUE specifically under-detects genericness when references aren't in play — 6.2 and 6.3's Level 2 passes both caught real, specific defects using only the rubric and the rule catalog already in scope.

Recommendation: Visual References is a **DIRECT/EXPLORE-only** capability for 6.4. Revisit CRITIQUE-side use only if a future benchmark shows Level 2 missing a genericness finding that a reference-bar check would have caught — don't build it speculatively now.

## 5. Reference model

**What a "visual reference" is, precisely: a distilled, pre-abstracted written observation about a real production design — not a stored image, not a template, not a layout to fill in.** The abstraction work (Observe → Abstract, §7) happens once, when an entry is authored, not re-derived live from an image at every DIRECT run. This is the single most important design decision in this proposal for both context cost (§19) and copying safety (§7): if abstraction happened at generation time, every DIRECT run would need to inspect an image and reason about it fresh, at real token cost, with real risk of the abstraction sliding back toward literal description under time pressure. A pre-authored, already-abstracted entry avoids both.

**Storage: one file, skill-provided, schema-templated — same shape as `style-catalog.md`, not the folder tree sketched in the prompt.** The proposed `.design/visual-references/{structural,typography,composition,imagery,interaction}/` tree is rejected for the same reason `style-catalog.md` itself already rejected a per-genre file split: *"premature fragmentation for a ~700-word file with no real token savings"* — and this catalog starts smaller than that. One file: `design-excellence/references/visual-references.md` (T3), a handful of demonstration entries (6–10 to start, matching `style-catalog.md`'s "one real entry per Genre, not a second catalog" restraint), each tagged by its **primary dimension** (composition / typography / color / imagery / materiality / interaction / spatial-hierarchy / navigation) rather than filed into a dimension-named folder. Tagging inside one file gets the same selection value as a folder split without the fragmentation cost.

**Entry schema:**

```
VisualReference
├── id
├── dimension          (primary — composition | typography | color | imagery |
│                        materiality | interaction | spatial-hierarchy | navigation)
├── observed           (2–4 concrete, checkable facts about the reference —
│                       what it actually does, stated plainly)
├── abstracted_principle (the observation restated as a relationship/logic,
│                        stripped of the reference's own subject/brand/color/copy —
│                        never something that could be drawn or named after the source)
├── compatible_with    (Register × Genre bands where this principle is a legitimate
│                       fit — references style-catalog.md's genre entries, doesn't
│                       duplicate them)
├── do_not_apply_to    (Register × Genre or brief-signal combinations where forcing
│                       this principle would be a mismatch, not a universal fit)
├── non_application_note (explicit: what NOT to copy — the reference's own literal
│                        color/typeface/copy/asset, named, so the boundary is stated
│                        rather than implied)
└── freshness          (last_verified_date, review_interval_days — same field
                        shape as anti-slop-registry.md, because a cited production
                        site can itself redesign and go stale)
```

No `accessibility_risk_tier`/`performance_cost_tier` fields (unlike `style-catalog.md`'s style entries) — a visual reference isn't a style commitment the skill is licensing, it's a possibility being surfaced for comparison; those fields belong to whichever candidate direction actually gets built, already covered by existing rule-catalog categories once a candidate is selected.

**Where entries come from.** Two sources, not mutually exclusive:

1. **Skill-provided (default, ships with the skill, same tier as `style-catalog.md`/`anti-slop-registry.md`).** A small, curated demonstration set populated at implementation time. Worth noting as prior art already in this environment, not something to invent from scratch: the installed `taste-examples` skill already maintains a curated corpus of production sites paired with a design-direction skill for exactly this "ground direction in real references instead of generic defaults" purpose. Its existence is evidence this pattern already works in this toolkit — but its internal format hasn't been inspected here and shouldn't be assumed compatible; at implementation time, evaluate whether entries can be *derived from* that corpus (running each candidate reference through this proposal's own Observe → Abstract → Adapt authoring discipline) rather than assuming its format ports directly.
2. **Project-provided (optional, project-local, mirrors `.design/context.md`'s own placement).** A single optional `.design/visual-references.md` file, same entry schema, for project-specific references the user explicitly wants considered. Not a folder, not a place to dump raw images — if the user supplies an image or URL, the distillation into the schema above happens once, when it's added, and the file stores the distilled entry, not the raw asset.

Neither source is a large database: the skill-provided set stays in the single-digit-to-low-teens entry range by design (matching `style-catalog.md`'s explicit "enough to demonstrate the pattern, not a second catalog" restraint), and the project-provided file is opt-in and expected to stay small.

## 6. Reference selection

**Lightweight, reusing context already computed at DEFINE — no new classifier, no vector search, no scoring system.** At the point DIRECT opens (§4), Register, Genre, the three dials, and (when applicable) the detected concept are already known. Selection is a reading judgment against that existing context, the same class of judgment DEFINE's own Genre inference and concept detection already make (`SKILL.md` §4, §1) — not a keyword scanner, not a similarity metric.

**Heuristic, in order:**
1. Filter to entries whose `compatible_with` includes the current Register/Genre (or that don't name it in `do_not_apply_to`) — never surface a reference that would require breaking Register's ceiling or Genre's posture to use.
2. Among compatible entries, prefer the one(s) whose primary `dimension` is **not** the dimension Genre's own default posture (`style-catalog.md`) would already emphasize — deliberately pulling toward what the brief's own gravity well would otherwise never surface, which is the entire point of this system (§1).
3. Cap at **2–3 entries considered per DIRECT run**, never the whole catalog — "load every image" and "treat every reference equally" are explicit non-goals (§20); a handful is enough to inform two candidates.

No automatic visual-style classification, no new numeric dial, no relevance score attached to entries. If nothing in the catalog is compatible with the current Register/Genre, that's a valid outcome — proceed with EXPLORE exactly as it runs today, unaffected. Absence of a fitting reference is not a gap to force-fill.

## 7. Observe → Abstract → Adapt mechanism

Same three-step shape as `LAYOUT-009`'s concept procedure and `TYPE-002`'s font-selection procedure — a generative decision sequence, not a constraint:

1. **Observe** — already done at authoring time (§5); DIRECT reads the entry's `observed` facts, doesn't re-derive them.
2. **Abstract** — already done at authoring time; DIRECT reads the `abstracted_principle`, stated at the level of a relationship or organizing logic, never at the level of the reference's own literal subject/brand/color/copy. An entry whose principle can't be stated without naming its source has failed authoring and shouldn't ship.
3. **Adapt** — happens live, at DIRECT: the abstracted principle becomes one more input to EXPLORE's already-required distinctness dimensions (`SKILL.md` §5's ≥2-of-6 requirement), applied to *this* brief's own Product Truth, Register, Genre, and (when present) concept — never pasted in as a template. The candidate that draws on it must still pass every rule that already governs a candidate (Register ceiling, Genre posture, Anti-Slop, accessibility) unchanged.

**Explicit ban, stated once and enforced at both authoring and application:** never "make it look like X." Neither an entry's own text nor DIRECT's use of it may instruct toward the reference's literal identity — only toward the abstracted relationship it demonstrates. This is the literal enforcement point for "Observe → Abstract → Adapt, never Copy," not a slogan left unimplemented.

## 8. Relationship to Concept → Structure

Two independent inputs to the same EXPLORE step, not a sequential dependency and not a merge:

- **Concept → Structure** (`LAYOUT-009`) derives a structural principle **from the brief's own meaning** — internal, brief-specific, and only present when the brief itself supplies real concept evidence.
- **Visual References** supplies structural/compositional **possibilities observed externally**, present whenever a compatible entry exists, independent of whether the brief carries a detectable concept at all.

**When both are active** (a concept is detected *and* a compatible reference exists): DEFINE produces the concept's abstract structural principle; DIRECT selects 1–2 reference entries; EXPLORE's two candidates each combine (a) which organizing surface carries the concept (`LAYOUT-009`'s existing requirement, unchanged) with (b) which reference-informed possibility they draw from — meaning the two candidates can now diverge not only in *which surface* carries the concept, but in *which broader visual register* the whole candidate inhabits. This directly targets the 6.3 gap: Atlas's two candidates differed in structural interpretation of the concept but stayed inside the same visual-language family, because nothing was pushing candidate generation to consider a materially different register in the first place.

**When only a concept is detected, no compatible reference exists:** DIRECT behaves exactly as it does today post-6.3 — unaffected, no degradation.

**When only a compatible reference exists, no concept is detected:** EXPLORE's two candidates draw on reference-informed possibilities without a concept-translation requirement — this is `LAYOUT-009`'s own precedent ("no meaningful concept detected" is a fully valid DEFINE outcome) applied symmetrically to this new mechanism.

Concept → Structure answers *why this structure, given what the brief means*. Visual References answers *what other structures or visual registers this brief could legitimately wear, given what's been observed elsewhere*. Neither substitutes for the other; both feed the same comparison.

## 9. Relationship to Anti-Slop

Distinct on the same two axes `PHASE-6.3-PROPOSAL.md` already established for Concept → Structure, and Visual References sits on the same side of both:

- **Direction:** Anti-Slop is subtractive — a ban-list against known-bad, currently-overused patterns (`anti-slop-registry.md`'s SLOP-001 through SLOP-019). Visual References is generative — it surfaces a possibility, it doesn't ban one. A candidate can pass every Anti-Slop entry cleanly while still being narrow (stuck in Genre's default posture); passing the ban-list says nothing about the breadth of what was considered.
- **Surface:** Anti-Slop's registry, by its own scope note, is populated from typography/color/layout-decoration tells. Visual References operates on macrostructure/composition/typography-pairing/color-anchor/interaction possibilities at the candidate-generation level, before those choices are even made — a different point in the pipeline than where Anti-Slop checks fire (VALIDATE/CRITIQUE, post-generation).

**Four genuinely separate axes, none subsuming another** (extending `PHASE-6.3-PROPOSAL.md`'s own framing): Anti-Slop (ban-list against known-bad patterns) · Fingerprint (compares this project's output against its own history) · Concept → Structure (derives structure from this brief's own meaning) · Visual References (expands the possibility space considered before commitment, from evidence external to both the brief and the project's history). A reference-informed candidate still has to clear Anti-Slop and still gets fingerprint-compared like any other candidate — this system adds an input earlier in the pipeline, it doesn't relax anything downstream.

## 10. Progressive disclosure

| Tier | Content | Load trigger |
|---|---|---|
| T0 | One paragraph in `SKILL.md` §1 (DIRECT/EXPLORE extension) — the system exists, pointer only | Always |
| T1 | None — reuses Register/Genre/dial/concept context already computed at DEFINE | N/A, no new T1 content |
| T2 | One new rule, `LAYOUT-010`, in `layout-interaction.md` (already loads whenever DIRECT runs for layout-in-scope work — zero new load trigger) | Same as existing `layout-interaction.md` trigger |
| T3 | `references/visual-references.md` | **Identical trigger to `style-catalog.md`'s existing one** (`SKILL.md` §7): DIRECT/DESIGN stage for a new visual system, page/multi-page-site scope — not a new load event, an addition to one that already fires |

**Image inspection is never mandatory.** The skill-provided catalog is pre-distilled text (§5) — there is no image inspection at generation time in the default case at all. The only case requiring inspection is a user adding a *new* project-level reference to `.design/visual-references.md` for the first time, and even then the distillation happens once, at the point it's added, cached as a written entry from then on — not re-inspected on every subsequent DIRECT run.

**Component/section POLISH has no path here, structurally, unchanged.** The Hard rule in `SKILL.md` §1 already blocks POLISH from reaching DIRECT at all; Visual References adds nothing to that boundary and cannot circumvent it, because it is only ever consulted *inside* DIRECT.

## 11. Routing

| Scope × Mode | Fires? | Why |
|---|---|---|
| component BUILD | No | No path into DIRECT (component scope is state/layout only, `ARCHITECTURE.md` §2) |
| component POLISH | No | Hard rule, `SKILL.md` §1 |
| section BUILD (new section on an already-directed page) | No | DIRECT does not re-run to add a section to an already-directed page (`SKILL.md` §1); the page's existing direction stands |
| section BUILD (first section establishing a page's direction) | Yes, as page-scope | Falls under page BUILD rules below |
| section POLISH | No | Hard rule, §1 |
| page BUILD (genuinely-empty) | **Yes** | Full mechanism — DIRECT establishes the direction fresh |
| page REDESIGN | **Yes**, gated | Fires, but every candidate is checked against Constraints & Preserved Patterns (§12) before being offered |
| multi-page BUILD | **Yes, once** | Fires when DIRECT establishes the site-wide direction, not per-page — matches DIRECT's existing non-re-run behavior across pages of one site |
| existing-product REDESIGN | **Yes**, gated | Same gating as page REDESIGN, at wider scope |

No routing table entry needed beyond what `SKILL.md` §1/§2 already define — Visual References activates exactly where DIRECT/EXPLORE already activates, never adds a case where DIRECT didn't already fire.

## 12. Existing-project behavior

Existing-system patterns remain authoritative by default (`SKILL.md` §3, P4) unless the user explicitly asks for a new direction — Visual References does not change this. Concretely:

- **Greenfield:** full mechanism, nothing to preserve, no gating needed.
- **Existing project, BUILD (extending, not redirecting):** DIRECT doesn't re-run (§11), so Visual References doesn't fire — the established direction is reused, exactly as today.
- **REDESIGN (page or whole-product):** fires, but per the Authority Hierarchy (`SKILL.md` §3), P4 (Existing-System Context) sits above P6 (Anti-Slop/Distinctiveness) — and Visual References operates at the same P6 layer as Concept → Structure (`LAYOUT-009`, itself layer P6). A reference-informed candidate that would silently break something on the Constraints & Preserved Patterns list (URL slugs, form field names, nav labels, analytics-relevant markup — `SKILL.md` §5) is never offered as a candidate at all; it fails before EXPLORE presents it, the same way any other P6-layer suggestion already yields to P4 in this hierarchy.
- **Polish:** never — no path into DIRECT, unchanged (§10, §11).

## 13. CTA/action hierarchy assessment

Evaluated as instructed, kept out of the Visual References architecture, and not over-scoped into it.

**This is not a Visual References problem.** It's a missing contextual principle for responsive action hierarchy — orthogonal to possibility-expansion, closer in shape to an accessibility/interaction correctness gap than a distinctiveness gap. Forcing it into this proposal's mechanism would misfile it the same way folding it into Concept → Structure would have.

**Recommendation: a small, fully decoupled rule addition, safe to implement in the same pass as Visual References but tracked as a separate diff item** (§14) — because it's cheap (one rule, no pipeline touch) and evidence-backed (Atlas's actual inconsistency), but its correctness has nothing to do with reference evidence and shouldn't be gated behind this proposal's approval.

**Draft principle** (ready to write as `INTX-004`, not implemented here): responsive action-hierarchy width is a function of **how many competing actions occupy the same region at the same breakpoint**, not a fixed mobile-width rule. A single action alone in its region (a form's own submit button, a hero's lone CTA) going full-width on narrow viewports is often correct — there is no sibling action to differentiate it from. Multiple competing actions in the same region (a primary + secondary CTA pair) collapsing to the same full-width treatment erases the hierarchy between them; the primary action should read as dominant through width, weight, or position, while the secondary shrinks toward intrinsic width or a visually quieter treatment. The failure Atlas exhibited — one region's solo submit button reflexively generalized into "mobile CTAs are full-width" applied inconsistently elsewhere — is the exact unconsidered-default pattern Anti-Slop's own philosophy already names (`SKILL.md` §9's anchor principle, `anti-slop-registry.md`'s framing): the fix is asking the hierarchy question each time a region is built, not adding a blanket width rule in either direction.

Validation: manual, matching `LAYOUT-008`/`LAYOUT-009`'s own precedent — this is a judgment about hierarchy, not a countable pattern.

## 14. Proposed file changes

1. **`design-excellence/SKILL.md`** — §1's existing "Creative exploration inside DIRECT" paragraph gets one additional sentence: when `visual-references.md` is loaded and yields a compatible entry, EXPLORE's two candidates are also required to draw on at least one distinct abstracted principle from a selected entry, so the candidates can differ in visual-language register, not only in structural interpretation of a detected concept. §7's T3 row gains `references/visual-references.md` alongside the two files already listed there, under the identical existing trigger — no new trigger condition written. Estimated delta: 3–4 sentences, comparable to or smaller than `LAYOUT-009`'s own 6.3 SKILL.md footprint.
2. **New file: `design-excellence/references/visual-references.md` (T3)** — the schema in §5 plus 6–10 demonstration entries. Estimated size: comparable to `style-catalog.md`'s ~700 words for its 4 entries; entries here carry fewer fields (no accessibility/performance tiers, §5), so total size should land near or below that per-entry average even with more entries.
3. **`design-excellence/references/rule-catalog/layout-interaction.md`** — one new rule, `LAYOUT-010` (Visual Reference Observe → Abstract → Adapt procedure + selection heuristic + the explicit copying-safety ban), sized like `LAYOUT-008`/`LAYOUT-009` (~250–350 words).
4. **`design-excellence/references/rule-catalog/layout-interaction.md`, Interaction section** — one further new rule, `INTX-004` (§13's responsive action-hierarchy principle), ~150–200 words. Architecturally unrelated to items 1–3; bundled only for implementation convenience.
5. **`.design/context.md` (project-level, no schema-version change)** — no new section needed. DIRECT's existing Rejected Directions entry (`SKILL.md` §5) gains, when a reference informed a candidate, the entry id and its abstracted principle alongside the candidate's other named distinguishing dimensions — reusing the existing append-only mechanism, not a new one.
6. **Optional, project-local: `.design/visual-references.md`** — created only if a user explicitly supplies project-specific references (§5); same schema as item 2, empty/absent by default.

**No change to:** `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md`, `anti-slop-registry.md`, `critique-protocol.md` (secondary CRITIQUE use rejected, §4), `color.md`, `typography.md`, `motion.md`, `accessibility.md`, `content-copy.md`, `performance-hardening.md`, `existing-project-safety.md`, `gesture-physics.md`, any `stacks/*.md`. `style-catalog.md` itself is read, not edited — Visual References references it (for the "not Genre's own default" selection heuristic, §6) without duplicating its content.

## 15. Validation strategy

Qualitative by construction, matching `LAYOUT-008`/`LAYOUT-009`'s own precedent — this is a possibility-expansion judgment, not a countable pattern, and forcing a numeric score onto it would misrepresent what's actually being checked. Two checks:

1. **Recorded, not mechanically scored:** did DIRECT's logged reasoning (Rejected Directions, §14 item 5) name which entry id and abstracted principle informed a candidate, stated at the abstraction level (never the reference's own subject/brand/color/copy)? Reviewed the same way `LAYOUT-009`'s three-step chain is reviewed today — auditable after the fact, not enforced at generation time.
2. **Optional, genuinely mechanical, cheap:** a string-match guard — does the shipped output contain any literal color hex, named product/brand string, or copy phrase drawn verbatim from an entry's `observed` facts? This is the one piece of this proposal that *is* `mechanical-countable` in the rule-catalog's own sense (a literal string comparison), and worth adding at VALIDATE if implementation time allows — but it's a safety net behind the Observe → Abstract → Adapt discipline (§7), not a substitute for it.

## 16. Benchmark design

**Reusing Atlas alone would not test the actual claim.** Atlas already has a committed direction from 6.3; re-running it identically doesn't test whether references broaden the space, it tests whether the skill reproduces its own prior output. Two changes to the benchmark design:

**Arm A — Atlas, fresh DEFINE, Visual References unavailable (control).** Re-run Clínica Atlas from a clean DEFINE (not reusing 6.3's committed direction), with no reference catalog loaded. Establishes a fair current-state baseline: does EXPLORE, unaided, converge to the same editorial-premium family again, or does it vary run-to-run regardless? Either result is informative and neither invalidates the test — this arm's only job is being the comparison point for Arm B.

**Arm B — Atlas, fresh DEFINE, Visual References available (test).** Identical brief and starting conditions as Arm A, catalog loaded per §6's selection heuristic. Compare against Arm A: do the two EXPLORE candidates in this arm span a genuinely different dimension-family than Arm A's candidates did (not just a different composition within the same family)? Is at least one candidate's macrostructure/color-anchor/typography combination traceable to a specific entry id + abstracted principle, logged and auditable?

**Arm C — a second, deliberately different brief.** Atlas is a brand-led editorial-prone subject; testing only there risks confirming the mechanism works for exactly the one convergence failure already observed and nothing else. Recommend a **product-led SaaS/dashboard brief** — weak-to-no concept evidence (tests §8's "reference-only, no concept" path) and a different convergence risk entirely (SLOP-007's "SaaS-card kit," not editorial-premium). This tests whether the mechanism generalizes past the one failure mode that motivated it, not just whether it patches that one case.

**Distinguishing the four evidentiary outcomes the prompt requires**, per arm:

- **A. No references** — Arm A's own result, the baseline every other outcome is measured against.
- **B. References available but not useful** — catalog loaded in Arm B/C, but DIRECT's logged reasoning cites no entry id/principle for either candidate, and the resulting candidates are not distinguishable in dimension-family from Arm A's. Evidence: absence in the Rejected Directions log despite entries being available and compatible.
- **C. References influencing decisions constructively** — at least one candidate's logged reasoning names a specific entry id and states its principle at the abstraction level, and that candidate's dimension-family (macrostructure/color-anchor/typography combination) differs from what Arm A produced and from what `style-catalog.md`'s own Genre-default entry alone would predict. Evidence: the log citation plus a concrete side-by-side dimension-family comparison against Arm A.
- **D. Literal copying/convergence** — the shipped output in Arm B/C contains a literal string/hex/asset match against an entry's `observed` facts (§15's mechanical guard), or a candidate's abstracted-principle field, if inspected, turns out to restate the reference's own subject/brand rather than a stripped relationship (an authoring failure, §7). Evidence: direct string comparison, or a manual re-check of the entry's own abstraction quality.

## 17. Success criteria

- Visual Reference Evidence changes at least one meaningful design decision in the test arm(s) versus the control arm, traceable to a specific entry id and abstracted principle — not asserted, logged.
- Recorded abstracted principles are relationships/logics, never literal restatements of a reference's own subject, brand, color, or copy.
- No candidate produced under this mechanism overrides Register, Genre, Product Truth, explicit user instruction, or (in REDESIGN) existing Constraints & Preserved Patterns — checked against `SKILL.md` §3's Authority Hierarchy with zero P3/P4 violations logged.
- Test-arm candidate directions are measurably more diverse than control-arm candidates: at minimum, one candidate's macrostructure/color-anchor/typography-pairing combination differs from what Genre's own `style-catalog.md` default entry would predict absent references.
- No genericness regression — Level 1/Level 2 Genericness axis score does not fall versus the control arm; `SLOP-011`'s gestalt check still passes on whichever candidate is selected.
- No increase in unnecessary complexity — implementation matches §14's footprint exactly: no new pipeline stage, no new dial, no new scoring system, no folder-tree storage.
- Context cost lands within roughly 15% of §19's estimate.
- Existing-project preservation intact — the REDESIGN benchmark arm (if run) shows zero Constraints & Preserved Patterns violations.

## 18. Risks

- **Selection is a judgment call, not mechanically enforced** (§6) — same risk class as Genre inference and concept detection already carry today, not a new kind of ambiguity.
- **A small skill-provided catalog could itself become a convergence source** if the same 2–3 entries get reused unreflectively across many unrelated projects. Mitigated by Fingerprint (`SKILL.md` §6) already catching repeated macrostructure/color-anchor choices within one project's own history, and by the §6 cap (2–3 entries per run, never the whole catalog) limiting any single entry's reach per run.
- **Literal-copying risk is real** given entries are distilled from real production designs. Mitigated by the Observe → Abstract → Adapt authoring discipline (§7) plus the optional mechanical string-match guard (§15); residual risk is judgment-dependent, the same honest limitation `LAYOUT-008`/`LAYOUT-009` already carry for their own qualitative checks.
- **Freshness** — a cited production site can itself redesign, making an entry's `observed` facts stale. Mitigated identically to `anti-slop-registry.md`'s own approach: `last_verified_date`/`review_interval_days` fields, `needs-review` past interval, no automated validator in V1 (matches existing precedent exactly, not a new governance burden).
- **Project-level reference file could balloon** if not bounded. Mitigated by capping it to the same distilled-entry schema (§5) — never raw image dumps — and by it being fully opt-in.
- **The bundled CTA rule (§13) risks over-hardening into a rigid width mandate**, defeating its own point. Mitigated by keeping its validation manual/qualitative (§13), matching `LAYOUT-008`/`LAYOUT-009`'s precedent rather than making it `mechanical-countable`.

## 19. Context-cost estimate

- **T0 (`SKILL.md`) growth:** 3–4 sentences across §1 (DIRECT/EXPLORE extension) and §7 (T3 row addition) — at or below `LAYOUT-009`'s own 6.3 footprint.
- **New T3 file:** `visual-references.md`, estimated 650–850 words for 6–10 entries (each entry carries fewer fields than a `style-catalog.md` style entry, §5, keeping per-entry size down even with more entries).
- **T2 growth:** `LAYOUT-010` (~250–350 words) + `INTX-004` (~150–200 words) in `layout-interaction.md` — comparable to `LAYOUT-008`/`LAYOUT-009`'s own individual sizes.
- **No change to `critique-protocol.md`** — secondary CRITIQUE use rejected (§4), zero cost there.
- **Load-event cost:** `visual-references.md` piggybacks on `style-catalog.md`'s existing T3/DIRECT trigger (§10) — this is not a new load event added to a request's cost profile, it's additional content within an event that already fires for exactly the scope where this matters (page/multi-page BUILD/REDESIGN with a new visual system).
- **Total net-new content:** roughly 1,050–1,400 words across three files (`visual-references.md`, two rule-catalog additions, SKILL.md pointer sentences) — comparable to or smaller than Phase 6.3's own measured ~920–930-word actual delta (`PHASE-6.3-RESULTS.md` audit findings), despite covering two independent concerns (Visual References + the decoupled CTA rule).

## 20. Explicit non-goals

- No giant reference database — capped at single-digit-to-low-teens skill-provided entries by design, not by an enforced limit that will need revisiting.
- No new pipeline stage, no new Operating Model row, no new cost tier.
- No large tagging taxonomy — one dimension field per entry, reusing Register/Genre/dial values already defined elsewhere.
- No vector database, no similarity scoring, no automatic visual-style classification.
- No new numeric dial — this system is dial-neutral, exactly as `LAYOUT-009` is required to be for Concept → Structure; it never justifies raising `DESIGN_VARIANCE`/`MOTION_INTENSITY`/`VISUAL_DENSITY`.
- No second scoring system alongside the existing six-axis critique rubric.
- No mandatory reference inspection for every task — component/section work has no path here at all (§10, §11), and even qualifying page/site work only triggers the mechanism when a compatible entry exists (§6).
- No folder-tree storage structure (`.design/visual-references/{dimension}/`) — one file, schema-tagged, matching `style-catalog.md`'s own anti-fragmentation precedent.
- No CRITIQUE-side use in this phase — evaluated and explicitly deferred (§4), not built speculatively.
- No forced structural/visual translation on a brief that doesn't warrant it — "no compatible reference, proceed unaffected" is a fully valid outcome (§6), matching `LAYOUT-008`'s "no imagery, deliberately" and `LAYOUT-009`'s "no meaningful concept detected" precedents.

## 21. Recommendation

Implement as scoped: one new T3 file (`visual-references.md`, 6–10 demonstration entries, schema in §5), one new rule (`LAYOUT-010`) describing Observe → Abstract → Adapt plus the selection heuristic and the explicit copying-safety ban, a handful of sentences in `SKILL.md` §1/§7, zero pipeline stages, zero new dials, zero change to `critique-protocol.md`. Bundle the fully decoupled `INTX-004` (responsive action-hierarchy principle, §13) in the same implementation pass since it costs almost nothing and touches none of the Visual References machinery — but track it as a separate diff item, since its correctness stands or falls independently of everything else in this proposal.

Benchmark with a fresh Atlas re-run split into a no-references control arm and a references-available test arm (§16, Arms A/B), plus one new product-led/dashboard brief (Arm C) to test whether the mechanism generalizes beyond the one editorial-premium convergence case that motivated it. This is the smallest architecture that could plausibly close the specific, evidence-demonstrated gap from `PHASE-6.3-RESULTS.md` §G: none of Anti-Slop, Fingerprint, Genre inference, or Concept → Structure would organically produce a wider EXPLORE comparison, confirmed by a benchmark where all four functioned correctly and the gap still occurred. Ready to schedule as Phase 6.4 implementation pending review of this proposal.
