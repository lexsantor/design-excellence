# Layout & Interaction — Rule Catalog (T2)

Named banned layout patterns (e.g. the eyebrow/tag-left-header-right two-column tell) live in `anti-slop-registry.md`, freshness-governed. This file holds structural/technical layout and interaction rules that don't go stale.

---

## Layout

### LAYOUT-001 — Macrostructure as one atomic choice
- **category:** layout · **layer:** P6 (anti-slop/distinctiveness) · **severity:** major
- **principle:** pick page shape as a single named bundle (e.g. Bento Grid, Long Document, Marquee Hero, Specimen, Manifesto) that carries heading placement, body composition, divider language, and reveal pattern together — rather than choosing 6 independent axes from scratch, which regresses to the mean because every independent axis tends toward the same combination.
- **applicability:** page/multi-page-site scope only; not applicable to component-scope requests. `DESIGN_VARIANCE` High band raises the fingerprint distinctiveness bar for the macrostructure dimension specifically (`SKILL.md` §6) — a macrostructure repeat is close to disqualifying, not just one-of-five; Low band permits a deliberately consistent macrostructure across a project without triggering a redirect. Medium band (Phase 6 correction): standard fingerprint bar applies (`SKILL.md` §6's 2-of-5 rule), with no additional raise or exemption — Medium is the one band where the fingerprint check alone, unmodified, governs. `VISUAL_DENSITY` High band favors denser macrostructures (e.g. Bento Grid); Low band favors generously-spaced ones (e.g. Long Document) (Phase 4 correction — real consumers of both dials, not just prose mentions).
- **exceptions:** a deliberately consistent macrostructure across a multi-page site is a legitimate choice, not a violation — see the Fingerprint redirect-signal framing in `SKILL.md` §6.
- **evidence:** the mechanism behind avoiding "every generated page shares a hero→3-feature→CTA→footer rhythm."
- **freshness:** status: permanent (the mechanism); the specific catalog of named bundles is reference material, populated in `style-catalog.md`.
- **validation:** self-critique-prompt at SHAPE stage.
- **remediation:** re-pick a different bundle if the fingerprint check (SKILL.md §6) flags insufficient difference from recent output.

### LAYOUT-002 — Squint test
- **principle:** blur vision (or literally blur a screenshot in Enhanced mode) — can primary/secondary hierarchy and groupings still be identified? For a generated set of variants: write one-sentence descriptions of each side by side; if two rhyme, rework the offender.
- **category:** layout · **layer:** P5 · **severity:** moderate
- **applicability:** universal, cheap, repeatable.
- **evidence:** a well-known technique, worth preserving as a literal step rather than leaving it implicit.
- **freshness:** status: permanent.
- **validation:** self-critique-prompt (Core v1) / rendered blur comparison (Enhanced mode, `existing-project-safety.md`/`critique-protocol.md` cross-reference).
- **remediation:** strengthen the weakest hierarchy signal (size, weight, or spacing contrast).

### LAYOUT-003 — Container queries vs. viewport queries
- **principle:** viewport queries control page layout; container queries control component layout. Don't use one where the other is the semantically correct tool.
- **category:** layout · **layer:** P5 · **severity:** minor
- **applicability:** universal, increasingly load-bearing as container-query support matures.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** switch the query type to match what's actually being resized.

### LAYOUT-004 — `overflow-x: clip`, not `hidden`
- **principle:** use `clip` (not `hidden`) on `html`/`body` to prevent horizontal scroll, because `hidden` silently breaks `position: sticky`/`position: fixed` on descendants — a non-obvious CSS interaction.
- **category:** layout · **layer:** P7 (production hardening) · **severity:** major
- **applicability:** universal CSS fact.
- **evidence:** the naive fix for a common bug (horizontal scroll) has a side effect most people don't know about.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag `overflow-x: hidden` on `html`/`body` when `sticky`/`fixed` descendants exist).
- **remediation:** swap to `clip`.

### LAYOUT-005 — `minmax(0, 1fr)` for image-bearing grid tracks
- **principle:** grid tracks that contain images must use `minmax(0, 1fr)`, never bare `1fr` — a bare `1fr` resolves to `minmax(auto, 1fr)`, and a large native image's intrinsic width becomes the track's effective minimum, blowing out mobile layouts.
- **category:** layout · **layer:** P7 · **severity:** major
- **applicability:** universal CSS Grid fact, wherever a grid track contains an `<img>` or similar intrinsically-sized element.
- **evidence:** only manifests with real (large) images, so it's easy to ship and fail only in front of real users.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag bare `1fr` on image-bearing grid tracks).
- **remediation:** wrap in `minmax(0, 1fr)`.

### LAYOUT-007 — Spacing scale keyed to `VISUAL_DENSITY` band
*(Added Phase 4 — closes a gap where spacing had no rule-catalog representation, and gives `VISUAL_DENSITY` a real consumer.)*
- **category:** layout · **layer:** P8 (aesthetic) · **severity:** minor
- **principle:** Low `VISUAL_DENSITY` band → generous section rhythm (48–96px separation between major sections), tight-grouping (8–12px) reserved for closely related elements only. High band → compact rhythm throughout, smaller gaps, more content visible per viewport. Medium band sits between the two and is the default absent other signal.
- **applicability:** universal — the primary rule-catalog consumer of `VISUAL_DENSITY`.
- **exceptions:** Register caps the ceiling regardless of dial value (`SKILL.md` §6) — a product-led register won't go as tight as a High-density brand-led editorial layout might.
- **evidence:** generalizes Impeccable's tight-grouping-vs-generous-separation rhythm framing (`FORENSIC-EXTRACTION.md` §3, Spacing) into a dial-consumable rule.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (measure declared spacing values against the band's range).
- **remediation:** adjust spacing tokens to the declared band's range.

### LAYOUT-008 — Imagery / art-direction decision procedure
*(Added Phase 6 — closes a gap where no rule gave imagery any decision framework; "no imagery" was previously the only option ever considered, not a weighed choice.)*
- **category:** layout · **layer:** P8 (aesthetic) · **severity:** minor
- **principle:** before finalizing a direction, answer explicitly and record the answer in `.design/context.md`'s Visual System section: (1) does the subject/brief warrant visual weight beyond typography and color — yes/no, with reason; (2) if yes, what medium is actually appropriate given what's available — provided/original photography, illustration, an abstract graphic system, AI-generated imagery, or another purposeful treatment; reject only genuinely generic/stock-looking treatments, not the category of imagery itself; (3) what role the medium plays (hero-anchor, supporting texture, wayfinding); (4) how it interacts with the chosen macrostructure (`LAYOUT-001`).
- **applicability:** page/multi-page-site scope BUILD/REDESIGN, alongside DIRECT's candidate-direction step (`SKILL.md` §1). "No imagery, deliberately justified" is a fully valid answer to question 1 — this rule does not mandate imagery, and does not introduce an imagery catalog.
- **exceptions:** none — a generative decision procedure, not a constraint to work around, matching `TYPE-002`'s format.
- **evidence:** the prior gap wasn't a preference for or against imagery — it was the absence of any evaluated decision; "no imagery" may well be the correct answer for a given brief, but it must be reached, not defaulted to.
- **freshness:** status: permanent.
- **validation:** manual — the four questions must be answered and recorded, not mechanically checked.
- **remediation:** n/a.

### LAYOUT-009 — Concept → structural-expression decision procedure
*(Added Phase 6.3 — closes a gap where a brief's specific concept could remain fully decorative (copy, motif, color, imagery) without ever shaping macrostructure, navigation, content architecture, section transitions, or interaction. See `PHASE-6.2-RESULTS.md`'s Clínica Atlas finding: every other Phase 6 mechanism — EXPLORE, Genre inference, the imagery procedure, mechanical validation, Level 2 critique — functioned correctly in that run, and this gap still occurred, because none of them asks this question.)*
- **category:** layout · **layer:** P6 (distinctiveness) · **severity:** minor
- **principle:** when DEFINE (`SKILL.md` §1) has recorded a detected concept, translate it in three steps, during DIRECT's existing EXPLORE comparison (`SKILL.md` §1), before either candidate is committed to: (1) **brief concept** — the specific idea/metaphor as stated or evidenced in the brief, never invented; (2) **abstract structural principle** — the concept stripped of its literal imagery, restated as a relationship or organizing logic that could organize content, not something that could be drawn (e.g. a concept built around a foundational reference object might abstract to "a single reference point the rest of the content orients around" — never to "add [object]-shaped decoration"); (3) **selected structural expression** — which organizing surface (below) the principle actually manifests on in each of the two EXPLORE candidates, recorded via the existing Rejected Directions mechanism (`SKILL.md` §5) alongside the candidate's other distinguishing dimensions.
- **organizing surfaces** (capable of carrying a structural decision — at least one must carry a decision traceable to the abstract structural principle; one is sufficient, never require more): macrostructure, content architecture, navigation, section transitions, interaction.
- **carrier surfaces** (reinforce but do not by themselves constitute structural expression): typography, color, spacing, imagery, iconography, motion, grid, responsive behavior.
- **not an Anti-Slop rule:** lives in the rule catalog, not `anti-slop-registry.md`, and is not a ban-list check. Anti-Slop is subtractive — it flags known-bad patterns (e.g. SLOP-011's self-tell clusters, SLOP-013's category-reflex palettes). This rule is generative — it derives a structural choice from this specific brief. A direction can pass every Anti-Slop entry cleanly while still being conceptually arbitrary; the two mechanisms are orthogonal, and this rule neither modifies nor duplicates any Anti-Slop entry.
- **applicability:** page/multi-page-site scope BUILD/REDESIGN only, and only when DEFINE's concept-detection step (`SKILL.md` §1) recorded **DETECTED / EVIDENCED** specifically (Phase 6.5 tightening) — component/section POLISH has no path into DIRECT at all (Hard rule, `SKILL.md` §1), so this rule cannot activate there regardless. A **HYPOTHESIS** outcome does not activate this rule's mandatory translation requirement, though the hypothesis may still inform ordinary DIRECT/EXPLORE creativity outside this rule's governance (`SKILL.md` §1). Operates entirely within whatever `DESIGN_VARIANCE`/`MOTION_INTENSITY`/`VISUAL_DENSITY` band and Register/Genre posture (`SKILL.md` §4) are already set — never a reason to raise a dial or override Register or Genre.
- **exceptions:** "NOT DETECTED" and "HYPOTHESIS" are both fully valid DEFINE outcomes, not a violation of this rule — matching `LAYOUT-008`'s own "no imagery, deliberately justified" pattern. Not every brand-led or editorial brief needs to be metaphorical, and a plausible but brief-unstated association is not grounds to treat one as if it were.
- **evidence:** `PHASE-6.2-RESULTS.md` — the Atlas concept (a vertebra + cartographic reference) was fully argued in copy and rendered as one decorative motif, but an independent reviewer found the nav, hero pattern, alternating-band sections, numbered list, CTA band, and footer "could serve another premium professional-services brand with only the copy swapped."
- **freshness:** status: permanent.
- **validation:** manual — the three steps and the organizing surface used must be answered and recorded (`SKILL.md` §5); not `mechanical-countable`, and not scored numerically.
- **remediation:** n/a — generative, not a constraint to work around, matching `TYPE-002`'s and `LAYOUT-008`'s format.

### LAYOUT-010 — Visual Reference Observe → Abstract → Adapt
*(Added Phase 6.4 — closes a gap `LAYOUT-009` doesn't: `PHASE-6.3-RESULTS.md` found both EXPLORE candidates staying inside one visual-language family even with a concept correctly translated into structure, because nothing asked EXPLORE to consider a genuinely different, externally-observed possibility.)*
- **category:** layout · **layer:** P6 (distinctiveness) · **severity:** minor
- **principle:** when `references/visual-references.md` or `references/principle-pool.md` (T3, §7; loaded together and treated as one combined source) yields an entry compatible with the current Register/Genre, DIRECT's EXPLORE step (`SKILL.md` §1) considers whether it meaningfully broadens either candidate. Observe and Abstract are already done at authoring time — DIRECT only reads the entry's stored `observed` facts and `abstracted_principle` (already stripped of source brand/subject/copy/color/typeface/imagery), never re-derives them. Adapt happens live: apply the principle to this brief's own Product Truth, Register, Genre, dials, and (when present) Concept → Structure's principle — never pasted in as a template, never applied merely because it exists.
- **selection (judgment, not a classifier), in strict priority order (Phase 6.5 clarification):** (1) **compatibility** — discard entries incompatible with Register/Genre/brief; (2) **applicability** — among what's left, discard any whose `do_not_apply_to` matches this brief's actual context; (3) **materially different design possibility** — among what remains, prefer whichever introduces a possibility this brief + Register + Genre would be unlikely to generate alone; `dimension` is browsing metadata, not the diversity mechanism, so a same-dimension entry with a genuinely different possibility outranks a different-dimension entry that doesn't; (4) **family diversity, strictly a tie-breaker** — only when two or more entries are otherwise comparably useful under (3), prefer the one whose production family/tradition differs from the family already favored by the candidate(s) so far, comparing families across both pools. An entry's family is its `family` value in `principle-pool.md`; in `visual-references.md` it is the production tradition the file header assigns to the entry (REF-001–REF-006 one web/documentation/editorial-adjacent family; REF-007–REF-009 each its own named tradition). The comparison is qualitative: when it is unclear whether two traditions differ, family diversity gives no preference. Family diversity is never grounds to select a reference on its own, and never justifies forcing a reference from a different family into a candidate it doesn't actually fit — priorities (1)–(3) always come first. Steps (1)–(2) screen every entry of both pools against its stored fields; only the survivors are weighed under (3)–(4), and at most 2–3 entries in total across both pools are seriously considered for adaptation. Nothing useful → proceed exactly as EXPLORE runs without this rule.
- **not a quota:** a reference may inform zero, one, or both candidates. "Considered, judged unnecessary" and "no compatible entry" are as valid as "adopted" — never require a candidate to use one merely because it was available, and never require each candidate to anchor to a different entry (that manufactures distinctness instead of testing for it). Both candidates must still independently pass the existing ≥2-of-6 distinctness requirement (`SKILL.md` §5).
- **copying boundary:** never reason as "make it look like [the reference]" — it supplies a possibility, not a target identity, template, or component recipe. Honor the entry's own `non_application_note`, not just this general rule.
- **applicability:** page/multi-page-site BUILD/REDESIGN only — no path for component/section POLISH (Hard rule, §1). Operates inside whatever dial band, Register, and Genre are already set (§4); never grounds to raise a dial or override Register/Genre/explicit instruction/preserved patterns (§3, §5). Independent of `LAYOUT-009`: a concept determines what the brief's meaning requires, a reference informs how a candidate could express that or something unrelated — neither needs the other present. Orthogonal to Anti-Slop for the same reason `LAYOUT-009` already states: subtractive vs. generative; a reference-informed candidate still clears every Anti-Slop entry unchanged.
- **exceptions:** none — generative, matching `LAYOUT-008`/`LAYOUT-009`'s format. "No compatible reference" is a fully valid outcome.
- **evidence:** `PHASE-6.3-RESULTS.md` §F/§G — every existing distinctiveness mechanism functioned correctly and candidates still stayed inside one visual-language family, because none of them asks this question.
- **freshness:** status: permanent (the mechanism); entries carry their own freshness fields (`last_verified_date`, `review_interval_days`) in `visual-references.md` and `principle-pool.md`; `principle-pool.md` states its own staleness rule in its header.
- **validation:** manual — which entry informed which candidate, and the principle applied, recorded when used (§5); not `mechanical-countable`, not scored.
- **remediation:** n/a.

## Interaction

### INTX-001 — 8-state coverage + demo-wrapper QA
- **principle:** every interactive component covers default/hover/`:focus-visible`/active/disabled/loading/error/success. QA technique: mirror real pseudo-classes onto force-classes (`.is-hover`/`.is-focus`/`.is-active`) on the same selectors so all 8 states render simultaneously on one throwaway preview, instead of manually forcing each pseudo-class in devtools.
- **category:** interaction · **layer:** P5 · **severity:** major
- **applicability:** universal for any interactive-component workflow; near-exact consensus across every source in the research.
- **evidence:** components routinely ship only default+hover; the other 6 states are either missing or invisible to a reviewer without this technique.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (presence of all 8 state selectors) + the demo-wrapper as the actual QA method.
- **remediation:** add the missing state(s); build the demo-wrapper preview for review.

### INTX-002 — Undo over confirm
- **principle:** default to undo-after-action for destructive operations; reserve confirm dialogs for truly irreversible, high-cost, or batch operations.
- **category:** interaction · **layer:** P5 · **severity:** moderate
- **applicability:** universal.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** replace a confirm-dialog with an undo toast where the action is reversible.

### INTX-003 — Clickable text never wraps to two lines
- **principle:** buttons, primary nav links, footer links, tabs, breadcrumbs, and CTAs never wrap. Fix priority: shorten the label first (preferred) → `white-space: nowrap` + reflow → drop non-essential items → collapse to a menu. Never let a CTA or nav link wrap — that's the hard floor.
- **category:** interaction · **layer:** P7 · **severity:** major
- **applicability:** universal, especially at narrow responsive widths.
- **evidence:** a visually obvious "wasn't tested at this width" tell, common because responsive testing usually eyeballs body copy, not button labels.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (rendered, Enhanced mode: check for wrapped clickable text at the required floor widths).
- **remediation:** apply the fix-priority order above.

### INTX-004 — Responsive action hierarchy depends on competing-action count, not viewport width alone
*(Added Phase 6.4 — Atlas's primary CTAs stayed intrinsic-width on mobile while its form's submit button went full-width, `PHASE-6.3-RESULTS.md`, with no rule governing which is right. Independent of Visual References; bundled only because the same benchmark evidenced both.)*
- **principle:** width/weight treatment follows how many competing actions share a region at a breakpoint, not a fixed mobile-width default either way. One action alone in its region going full-width is often correct — no sibling to differentiate from. Multiple competing actions (primary + secondary CTA, a card's several actions) collapsing to identical treatment erases their hierarchy: the primary should read dominant through width, weight, or position; a secondary shrinks toward intrinsic width or a quieter treatment instead of also going full-width. Width is one hierarchy tool among several (weight, position, order), never the only one.
- **category:** interaction · **layer:** P5 · **severity:** moderate
- **applicability:** universal, any region with 2+ visible actions at a breakpoint; exactly one action is the named exception where full-width is frequently correct.
- **exceptions:** none beyond the single-action case — a contextual judgment rule, not a threshold to work around.
- **evidence:** `PHASE-6.3-RESULTS.md` — the Atlas intrinsic-vs-full-width inconsistency existed because nothing asked the hierarchy question in either case.
- **freshness:** status: permanent.
- **validation:** manual — deliberately not `mechanical-countable`; a countable check here would recreate the blanket-rule failure mode this entry avoids.
- **remediation:** re-derive width/weight/position from the actual competing-action count, not viewport width alone.
