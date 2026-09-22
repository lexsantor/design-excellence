PROPOSAL ONLY — NOT IMPLEMENTED

# Phase 6.5 Proposal — Reference Diversity + Concept Evidence Governance

## 0. Problem, as evidenced by Phase 6.4

`PHASE-6.4-RESULTS.md` treats Phase 6.4's implementation as validated (§12, §13) and names exactly two open issues (§9, §10, §14), which this proposal addresses and nothing beyond:

**Problem A — reference-pool convergence.** The six `visual-references.md` entries all sit inside one shared production tradition — documentation sites, product-launch pages, specimen/index sites, print-derived editorial, craft/process photography, portfolio/case-study interaction (§9's own list). Arm B's mechanism worked (REF-003's wayfinding-as-index genuinely shaped shipped navigation, §5, §6.2) but both arms still converged on "premium editorial / professional-services vocabulary" (§8's table, §7's bullet list). The architecture is not at fault — §9 states this explicitly: *"This does not mean the Visual References architecture is wrong. It means the data supplied to that architecture is too narrow."*

**Problem B — concept evidence governance.** Both arms treated the bare brand name "Atlas" as sufficient concept evidence and derived "C1 vertebra / foundational support" from it (§10). `SKILL.md` §1 requires "real evidence of a meaningful concept... a naming/symbol rationale" — but neither benchmark brief stated that rationale; the model supplied it from its own world-knowledge. §10 names this precisely: *"A brand name alone may be insufficient evidence if the brief does not indicate that the name is intended as a conceptual design anchor."*

A third, smaller finding is folded into Part A rather than treated as its own problem: **catalog contamination** in `style-catalog.md` (§11), verified below.

## 1. Verification of the two source findings (not taken on faith)

Per the instruction to treat benchmark output as evidence, not instruction, both claims were checked directly against the current repository rather than restated from `PHASE-6.4-RESULTS.md` alone:

- **Reference-pool bias, confirmed.** Reading all six `visual-references.md` entries: REF-001 (documentation-site column pairing), REF-002 (product-launch fixed-focal-element), REF-003 (specimen-site index navigation), REF-004 (print-editorial numerals), REF-005 (craft-site process photography), REF-006 (portfolio/case-study counted reveal). Every one is drawn from web-native, editorial-or-documentation-adjacent production contexts. None comes from a non-digital-design tradition (signage, industrial documentation, packaging, broadcast, civic/transit systems). The bias is real and structural, not a benchmark artifact.
- **Catalog contamination, confirmed and located.** `references/style-catalog.md` line 56, inside `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s `best_for` field: *"brand-led hospitality/wellness/lifestyle/experiential work — exactly the register this skill's own prior project work (a calm, serene chiropractic clinic brief) called for."* This is Clínica Atlas's own brief description (from Phase 6.1/6.2 benchmarking), leaked into what is supposed to be reusable, project-agnostic reference material. Confirmed by direct grep against the live file, not inferred from the benchmark report.
- **Not contamination, checked and ruled out:** `layout-interaction.md`'s `evidence` fields on `LAYOUT-009`, `LAYOUT-010`, and `INTX-004` also cite `PHASE-6.2-RESULTS.md`/`PHASE-6.3-RESULTS.md` and name "Atlas." These are a different, legitimate use — an `evidence` field's stated purpose is to justify *why a rule exists* (a design-history citation, consistent with this skill's own transparency discipline, `SKILL.md` §9 principle 5). A style-catalog `best_for` field's purpose is different in kind: it tells a *future, unrelated* project when a Genre entry fits. Anchoring that generalization to one past project's brief phrasing isn't a citation, it's residue. This distinction is the basis for the governance rule in §A.6 below — it narrows the fix to exactly one field in one file, not a sweep of every phase-citation in the codebase.

## Part A — Reference Diversity

### A.1 What "diversity" means

Not entry count, not palette count, not genre count, not trend count. **Diversity is measured by whether the catalog, taken as a whole, supplies materially different *design possibilities* — different organizing or carrier logics (per `LAYOUT-010`'s own existing split, `layout-interaction.md`) that the current brief + Register + Genre would be unlikely to generate alone.** `LAYOUT-010`'s existing principle already states this correctly for *selection* ("Design Possibility > Dimension," `SKILL.md` §1's Phase 6.4 addition, my own §6 in the implementation) — Phase 6.5 extends the same test to *authoring* and *pool composition*: a catalog is diverse when its entries collectively span different production traditions, not when they're individually well-written.

Concretely, the current six entries all answer variations on "how does a considered web publication organize content." Genuinely different design possibilities live in traditions that never had to solve *that* problem in the first place:

- **Physical-world / environmental / architectural logic** — how a museum's object-label system layers information at reading distance vs. across a room; how a building's floor-plan sequences visitor movement; how a trailhead sign stacks urgent vs. reference information.
- **Civic / institutional / transit systems** — how a transit map's line-and-interchange logic differs from a menu; how a government form's field-sequencing differs from a marketing page's; how a scoreboard prioritizes glanceable state over detail.
- **Industrial / scientific documentation** — how a lab protocol sheet or an instrument's calibration card sequences steps for someone mid-task, not someone browsing; how a technical drawing layers dimensions without narrative flow at all.
- **Packaging / print ephemera** — how a ticket, receipt, or manifest compresses a lot of state into a small, non-scrolling surface; how repeated small print artifacts (labels, tags) solve hierarchy without a page metaphor at all.
- **Broadcast / kinetic graphics** — how a lower-third or scoreboard overlay handles state change over time without a "page" existing at all.

This list is illustrative of *where* to look for possibility, not a required coverage grid — per the instruction, no rule should require every entry to cover a different dimension, and no rule should require covering every family listed here. The test stays what `LAYOUT-010` already established: does this specific entry supply a possibility the brief+Register+Genre wouldn't generate alone.

### A.2 Preventing style presets

The existing schema (`id`, `dimension`, `observed`, `abstracted_principle`, `compatible_with`, `do_not_apply_to`, `non_application_note`, `freshness`) already structurally prevents this, and Phase 6.5 changes nothing about it — the fix is discipline in *authoring* new entries against the schema that already exists, not a new mechanism:

- **No entry, `id`, or `dimension` value may name an aesthetic movement or style label** ("Swiss," "Brutalist," "Japanese," "Luxury," "Minimal," "Editorial"). `dimension` names a *functional* category (composition, navigation, materiality, interaction...), never a *style* category. This is already true of all six existing entries (REF-001 through REF-006 are named for what they *do* — "Persistent asymmetric column pairing," not "Editorial" or "Swiss") — Phase 6.5's four new entries must pass the same test.
- **The authoring test, reused from `LAYOUT-010`'s own "if the principle can't be described without relying on the source's identity, the entry is not sufficiently abstracted":** apply the identical test to *style*, not just *source*. If an `abstracted_principle` cannot be stated without the word "look" or a genre/movement name, the entry is a style preset in disguise and must be rewritten or discarded before it ships.
- **No change to the schema fields themselves** — this is a writing-discipline requirement to apply during authoring, checked once at review time, not a new validation gate.

### A.3 Reference pool size

**Recommendation: grow from 6 to 10, by addition, not replacement.**

`PHASE-6.4-RESULTS.md` §12 explicitly validated REF-001, REF-003, and REF-004's real influence on the shipped design and on a rejected candidate — these are proven, working entries, and churning them out to make room for new ones would discard validated evidence to chase an unvalidated hypothesis. The problem is family clustering across the *whole pool*, not that any individual entry is wrong.

Trade-off reasoning:
- **8 entries** (2 new) is likely too few headroom — two additions can broaden the pool's average, but can't establish a second or third genuinely independent production family strong enough to reliably surface as an alternative during selection (§A.4's family tie-breaker needs more than one non-editorial candidate to choose between, or it has nothing to break a tie against).
- **10 entries** (4 new) gives enough room for at least two, ideally more, independent non-web-editorial families (per §A.1) while the total pool stays firmly below anything resembling UI UX Pro Max's 88–192-row catalog — the exact scale `ARCHITECTURE.md` §23 and `FORENSIC-EXTRACTION.md` §11 both flagged as out of scope for this skill.
- **Beyond 10** starts trading diversity for noise: `LAYOUT-010`'s selection heuristic ("consider at most 2–3 entries, never the whole file") has to work harder to find a genuinely relevant possibility inside a larger pool, and a bigger catalog re-introduces exactly the freshness-governance burden `anti-slop-registry.md`'s own scope note already warns against taking on casually.

10 is the recommended ceiling for this phase. Context cost at 10 entries is estimated in Part E; it stays inside the existing T3/DIRECT-only load trigger, not a new load event.

**Authoring constraint for the 4 new entries (concrete, not aspirational):** at least 2 of the 4 must be drawn from a tradition with no native "page" or "screen" metaphor at all (signage, packaging, print ephemera, instrumentation, broadcast) — this is the direct, checkable answer to Problem A, and prevents the new entries from quietly reconverging on "considered digital-editorial" from a different angle (see Risk in Part H, "convergence into a different meta-style").

### A.4 Reference selection

No numerical score, classifier, vector search, or quota — Phase 6.5 makes exactly one addition to `LAYOUT-010`'s existing judgment-based heuristic (`layout-interaction.md`, §6 of the Phase 6.4 implementation): a **family-level tie-breaker**, applied only after the existing "materially different possibility, not different dimension" test has already narrowed the field.

Current heuristic (unchanged): discard incompatible entries → prefer whichever introduces a possibility the brief+Register+Genre wouldn't generate alone → cap at 2–3 → proceed unaffected if nothing fits.

**Added clause:** when two or more remaining entries are comparably useful under that test, prefer the one whose overall production family (per §A.1) differs from the family the candidate(s) so far already draw from. This directly targets Problem A's actual failure mode — Phase 6.4's Arm B individually justified each reference correctly (§6 of `PHASE-6.4-RESULTS.md`) and still ended up family-homogeneous, because nothing broke ties toward family difference specifically. This is a tie-breaker on an existing test, not a new mechanism, a new field, or a numeric score.

### A.5 Source provenance

**Recommendation: remain generic pattern classes, diversified by *tradition*, not by adding named real sources.** This was a deliberate Phase 6.4 authoring decision (`visual-references.md`'s own header: *"no entry carries a recognizable source identity to begin with"*) and nothing in Phase 6.4's results argues it failed — the convergence problem is about which *traditions* are represented, not about whether sources are named.

Explicitly: **I cannot verify real, currently-accurate production sources for new entries in this proposal** — I have no live browsing capability invoked in this session, and asserting specific real sites/systems from training-data memory risks exactly the kind of unverifiable, potentially-stale factual claim `SKILL.md` §9 Core Principle 8 (no fabricated data) exists to prevent. Saying so plainly, per instruction, rather than inventing provenance.

**Hybrid path, gated, for a future phase — not this one:** a specific real, named source may be added later *only if* verified live at authoring time (a real fetch/render, with a stated verification date recorded in that entry's `freshness` field) — never asserted from memory alone. This is consistent with `anti-slop-registry.md`'s own `last_verified_date`/`review_interval_days` governance shape, extended to a new field's worth of provenance rather than just staleness. Phase 6.5 does not exercise this path; it is named here so a future author knows the bar, not left as an open question.

### A.6 Catalog contamination

Located and confirmed in §1 above. Answering the specific questions asked:

- **Where:** `references/style-catalog.md`, line 56, `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s `best_for` field.
- **Is it benchmark residue:** yes — it names "this skill's own prior project work" and describes it using Clínica Atlas's own brief language ("a calm, serene chiropractic clinic brief"), not a generic register/genre description.
- **Can it be safely removed:** yes. The field's job is to state which category of brief this Genre entry suits; that job is fully served by a generic register/genre statement with no project citation. Nothing else in the file, and no rule elsewhere in the catalog, depends on the specific clause — `style-catalog.md` is read by DIRECT/DESIGN and CRITIQUE/AUDIT (`SKILL.md` §7) as a lookup table keyed on Genre, not parsed for this specific sentence.
- **Does removing it affect the original architecture:** no. `ARCHITECTURE.md` §11 explicitly defines this file's schema as the durable contribution, populated with "one real, fully-specified entry per Genre... enough to demonstrate the pattern" — the entry's *existence* and *schema* are architectural; this one clause's *wording* is not.
- **Governance rule to prevent recurrence:** descriptive fields in `style-catalog.md` and `visual-references.md` (`best_for`, `do_not_apply_to`, `keywords`, `observed`, `compatible_with`, `non_application_note`) must never cite a specific past benchmark project, session, or brief by its content. Only `evidence` fields in the rule catalogs (`layout-interaction.md` etc.), whose explicit, existing purpose is design-history justification, may cite `PHASE-x-RESULTS.md`-style evidence. This is a one-sentence addition to `style-catalog.md`'s own header note (see Part E) plus the one-clause fix to line 56 — not a sweep or a new validation script.

**Not deleted here** — per instruction, this proposal only identifies, verifies, and specifies the fix; the actual one-clause edit is listed as a Part E file change for implementation.

## Part B — Concept Evidence Governance

### The core distinction: evidence, hypothesis, creative interpretation, user-provided intent

`SKILL.md` §1 currently produces a **binary** DEFINE outcome: concept detected / not detected. Phase 6.4's finding is that this binary conflated two genuinely different things — *the brief stating a rationale* and *the model supplying one from its own world-knowledge about the name*. The fix is not new machinery; it's replacing the binary with a **three-way classification**, applied at the exact same DEFINE step, with no new pipeline stage:

- **Evidence** — the rationale, embodiment request, or recurring reference object is *stated in the brief's own text*. This is a bright-line, literal test: can you point at the sentence. If yes → **detected (evidenced)**.
- **User-provided intent** — the user explicitly instructs the system to use a specific idea as the structural foundation (P2, `SKILL.md` §3 — wins over everything below it). Strongest possible form of evidence; also **detected**, by instruction rather than inference.
- **Hypothesis** — the model itself supplies a plausible, real, checkable association the brief does not state (an etymological fact, a well-known meaning, a real-world reference the name happens to share). Declared, never silently acted on; never logged as "detected." May still inform ordinary creative exploration (see below) but carries none of `LAYOUT-009`'s governance weight unless promoted by explicit user confirmation, at which point it becomes user-provided intent.
- **Creative interpretation** — the ordinary latitude DIRECT/EXPLORE already has to propose an interesting idea with no concept-evidence claim attached at all. Entirely unconstrained by this governance; it was never gated by Concept → Structure to begin with, and Phase 6.5 changes nothing about it.

### Case-by-case ruling

**Case 1 — brief explicitly explains the name's meaning.** *Evidence.* Detected. `LAYOUT-009` activates exactly as today — no change in behavior, this is the case Phase 6.3's mechanism was built for and worked correctly on.

**Case 2 — brief explicitly asks to use the concept as the structural foundation.** *User-provided intent (P2).* Detected, and stronger than Case 1 — an explicit instruction, not an inference. `LAYOUT-009` activates; per the Authority Hierarchy, DIRECT should treat the requirement as closer to mandatory than the ordinary "may inform zero, one, or both candidates" latitude, since declining an explicit P2 instruction with no P1 conflict would itself need disclosure (`SKILL.md` §3).

**Case 3 — brief says only "Brand: Atlas," no explanation.** *This is the case Phase 6.4 actually hit, misclassified as Case 1.* Not evidence — nothing in the brief states a rationale. The model may form a **hypothesis** ("Atlas plausibly references the C1 vertebra / the mythological titan") if it is a real, checkable fact, never invented — declare it in one line, the same transparency pattern already used for Register/Genre declaration (`SKILL.md` §4). Log as **hypothesis**, not detected. `LAYOUT-009`'s mandatory dual-candidate structural-translation requirement does **not** fire. The hypothesis may still shape one candidate's ordinary creative direction (unconstrained, per Creative Interpretation above) — but Rejected Directions logs it as hypothesis-derived exploration, never as "concept detected: yes."

**Case 4 — brand name has an obvious semantic meaning, brief silent.** *Identical ruling to Case 3.* "Obvious" is a judgment about the model's own knowledge, not brief evidence — obviousness does not upgrade a hypothesis to evidence. This is the precise, narrow correction Phase 6.4's benchmark evidence calls for.

**Case 5 — a recurring metaphor/object/spatial reference appears in the brief, not tied to the brand name.** *Evidence, unchanged.* `SKILL.md` §1's existing language already covers this ("a recurring reference object central to the identity") — Phase 6.5 makes no change here, only clarifies that "recurring" means actually appearing more than once or being given real emphasis in the brief's own text, not a single passing mention the model chooses to build significance around.

**Case 6 — the model notices a potentially interesting concept the brief doesn't support at all.** *Creative interpretation, not hypothesis.* Weaker than Cases 3/4 (no name-based hook even). If raised, treat identically to a bare hypothesis: no concept-detection status, no `LAYOUT-009` governance, no special declaration beyond ordinary Rejected Directions dimension-logging if it ends up shaping a candidate.

### What this does not do

It does not remove Concept → Structure, does not make DEFINE ask more clarifying questions (the hypothesis is *declared*, per the existing "infer and state a one-line reading" default already governing Register/Genre — `FORENSIC-EXTRACTION.md` §14.14, `SKILL.md`'s own Auto Mode alignment), and does not suppress creative interpretation — it removes exactly one failure mode: a model-supplied fact about a name being silently treated as if the brief had said it, which is what let Atlas's C1-vertebra reading acquire `LAYOUT-009`'s full mandatory-translation weight on evidence the brief never actually supplied.

## Part C — Relationship to Existing System

- **DEFINE:** gains the three-way concept-evidence classification in place of the binary; no change to how Register/Genre/Dials are classified.
- **DIRECT/EXPLORE:** mechanically unchanged. `LAYOUT-010`'s selection heuristic gains the family tie-breaker (§A.4). A hypothesis may still inform ordinary candidate creativity, unconstrained, exactly as any other unattributed creative idea already could.
- **Concept → Structure / `LAYOUT-009`:** its `applicability` field is tightened to require the "detected (evidenced)" or user-confirmed-hypothesis outcome specifically — the 3-step chain (brief concept → abstract principle → selected structural expression), the organizing/carrier surface list, and the evidence bar are all otherwise untouched.
- **Visual References / `LAYOUT-010`:** mechanism entirely unchanged, per the stated architectural constraint. Catalog grows by 4 entries; selection heuristic gains one tie-breaker clause.
- **Register / Genre, Design Dials:** untouched.
- **Anti-Slop:** untouched — explicitly a non-goal (Part I).
- **Fingerprint:** untouched. A hypothesis-derived or reference-informed candidate is fingerprinted identically to any other candidate; no special-casing.
- **Level 1 critique:** the existing structural-test sub-check under axis 1 (`critique-protocol.md`, "applied only when DEFINE... recorded a detected concept") is tightened to read specifically "detected (evidenced)" — a hypothesis-only outcome does not trigger the expectation that the concept must be structurally legible, since under the new model it was never claimed as a real concept in the first place.
- **Level 2 critique:** the parallel sentence in the dispatch-brief instructions gets the identical one-phrase tightening.
- **Rejected Directions:** gains one clarifying sentence distinguishing concept-derived logging (requires "detected") from hypothesis-derived or reference-derived logging (no `LAYOUT-009` gate, logged as ordinary distinguishing dimensions).
- **`.design/context.md`:** no schema/`schema_version` change — the concept-detection outcome is prose, not frontmatter; it now records one of three labels instead of two, in the same location it already lives.

No new pipeline stage, no new dial, no new scoring system — confirmed by the list above containing no additions to `SKILL.md` §1's Operating Model table or §4's dial list.

## Part D — Existing Projects

- **Genuinely-empty:** full three-way classification applies fresh, as described.
- **Existing project (BUILD, DIRECT reused):** a concept classification already recorded before Phase 6.5 is not retroactively re-litigated or migrated; the tightened rule only governs classifications made going forward, when DEFINE or DIRECT actually re-runs.
- **REDESIGN:** DEFINE/AUDIT-stage re-evaluate as today; the three-way classification applies the same way a fresh greenfield classification would, and Existing-Project-Safety's Constraints & Preserved Patterns continue to sit above this (P4 above P6, `SKILL.md` §3) — a hypothesis or a reference can never justify breaking a preserved pattern, unchanged from Phase 6.4.
- **POLISH:** unaffected, verified structurally — component/section POLISH has no path into DEFINE or DIRECT at all (Hard rule, `SKILL.md` §1); none of Phase 6.5's changes live anywhere but inside DEFINE/DIRECT, so none of it can leak into POLISH. This is the same guarantee Phase 6.4 relied on for Visual References, extended automatically to the concept-governance change because it's implemented at the identical boundary.
- **CRITIQUE (task mode):** the tightened structural-test wording applies whenever Level 1/2 critique runs against output carrying a concept-detection record.
- **AUDIT (task mode):** read-only; if AUDIT-stage encounters a pre-Phase-6.5 design where a hypothesis was mislabeled as "detected" under the old binary, this is a legitimate, nameable finding for the audit report — a governance-drift observation, not a new mechanism the audit itself needs to run.

## Part E — Proposed File Changes

| # | File | Why | What | Tier | Est. word delta |
|---|---|---|---|---|---|
| 1 | `SKILL.md` §1 | Replace binary concept-detection outcome with the three-way model (§Part B) | Reword the existing "Concept detection at DEFINE" paragraph | T0 | +130–170 |
| 2 | `SKILL.md` §5 | Distinguish concept-derived Rejected-Directions logging from hypothesis/reference-derived logging | One clarifying sentence added to the existing Rejected-Directions paragraph | T0 | +40–60 |
| 3 | `references/rule-catalog/layout-interaction.md` — `LAYOUT-009` | Gate mandatory activation on "detected (evidenced)" specifically, not the old binary | Tighten the `applicability` field's wording | T2 | +30–50 |
| 4 | `references/rule-catalog/layout-interaction.md` — `LAYOUT-010` | Add the family-level tie-breaker (§A.4) | One clause added to the existing selection-heuristic bullet | T2 | +40–60 |
| 5 | `references/visual-references.md` | Diversify the pool (§A.3) | Add REF-007–REF-010, same schema, ≥2 from non-page/-screen traditions; update header note per §A.6's governance rule | T3 | +520–650 |
| 6 | `references/critique-protocol.md` | Match the tightened concept-evidence wording | One phrase added at each of the two existing "recorded a detected concept" mentions (Level 1 axis-1, Level 2 dispatch instructions) | T2 | +20–30 |
| 7 | `references/style-catalog.md` | Remove the confirmed benchmark residue (§A.6) | Replace the self-referential clause in `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s `best_for` with a generic register/genre statement; add the one-sentence provenance-governance note from §A.6 to the file's header | T3 | ~0 net (removal + generic replacement + one governance sentence) |

**No new files.** No `schema_version` bump. No new rule IDs — `LAYOUT-009` and `LAYOUT-010` are reworded, not replaced; the four new catalog entries extend the existing `visual-references.md` schema, not a new rule.

**Files protected (unchanged from this proposal and from Phase 6.4's own protected set):** `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md`, every `PHASE-*.md` document, `references/anti-slop-registry.md`, `references/existing-project-safety.md`, `references/gesture-physics.md`, `references/rule-catalog/{color,typography,motion,accessibility,content-copy,performance-hardening}.md`, any `references/stacks/*`.

## Part F — Validation

**Static:**
- Exactly two rule IDs touched (`LAYOUT-009`, `LAYOUT-010`), zero new IDs; grep-confirm no duplicate IDs introduced.
- `SKILL.md` §1's Operating Model table and §2's routing table are byte-identical except for the one reworded paragraph in §1 — no new stage row, no new mode.
- `SKILL.md` §4's dial list unchanged — no fourth dial.
- No file in the diff contains a numeric relevance score, a classifier description, or a vector-database reference.
- `SKILL.md` §3's Authority Hierarchy is unchanged verbatim.
- `.design/context.md`'s YAML frontmatter schema (§5) unchanged; `schema_version` stays `1`.
- Hard rule (component/section POLISH excluded from DEFINE/DIRECT/SHAPE/DESIGN) still has zero exceptions anywhere in the diff.

**Behavioral:**
- A DEFINE run against a brief with an explicit naming rationale (Case 1) logs "detected (evidenced)" and `LAYOUT-009` fires exactly as in the original Phase 6.3 success case — a direct regression check.
- A DEFINE run against a bare "Brand: X" brief with no rationale (Case 3/4) logs "hypothesis," not "detected," and `LAYOUT-009`'s mandatory dual-candidate translation requirement does not fire.
- The Rejected Directions log for a hypothesis-shaped candidate never contains the string "concept detected: yes" or equivalent.
- Each of the 4 new `visual-references.md` entries passes the style-preset test (§A.2): its `abstracted_principle` can be read aloud without naming a style movement, a genre, or its own source.
- At least one benchmark run selects a reference from a non-editorial family (§A.1) and the resulting candidate is later logged with that entry's id, per the existing `LAYOUT-010` logging requirement.
- A POLISH-scope request, run against the same project, shows zero DEFINE/DIRECT/concept/reference activity — unchanged from Phase 6.4's own regression check.

**Benchmark (small, targeted — not another full Clínica Atlas run):**

| # | Case | Scope | What it tests |
|---|---|---|---|
| 1 | Brief with explicit concept evidence (naming rationale stated in-brief) | single page or small section | Case 1/2 — confirms "detected (evidenced)" and unchanged `LAYOUT-009` activation (regression against Phase 6.3) |
| 2 | Same subject, brand name only, rationale paragraph stripped | single page | Case 3/4 — confirms "hypothesis" classification and that `LAYOUT-009` does not mandatorily fire |
| 3 | A nameless, conceptless generic service brief | single page | Confirms clean "not detected," unchanged baseline |
| 4 | A product-led/dashboard brief (the Arm-C brief already proposed, unused, in `PHASE-6.4-PROPOSAL.md` §16) | single page or small multi-page | Tests whether the diversified 10-entry catalog surfaces a non-editorial reference and whether it visibly changes a candidate |
| 5 | An existing 2-page project: add one new section to an already-directed page, then run a component-scope POLISH | component + section | Confirms DIRECT doesn't re-fire for the section case and confirms zero DEFINE/DIRECT/concept/reference activity for the POLISH case |

Cases 1–3 can share one brief family (varying only the naming-rationale paragraph) to keep the benchmark cheap. None requires multi-page scale; the specific finding in question (evidence-vs-hypothesis classification, reference-family selection) is fully observable at single-page or component scope.

## Part G — Success Criteria

No numeric quality score. Observable pass/fail conditions:

- At least one benchmark case selects and logs a reference from a family genuinely outside the "premium editorial" cluster `PHASE-6.4-RESULTS.md` §7 names (numbered index nav, folio numerals, hairline rules, zero-radius materiality, asymmetric grid, restrained accent) — this is the named regression bar to clear.
- No candidate in any benchmark case is forced to use a reference — at least one case ships a candidate using zero references.
- Zero literal-copying findings across all five benchmark cases (Level 1/2 critique).
- Zero style-preset-named entries anywhere in the 10-entry catalog (checked by direct re-read, not inference).
- Case 3/4's benchmark run logs "hypothesis," never "detected," and `LAYOUT-009` does not mandatorily activate.
- Case 1's benchmark run reproduces the original Phase 6.3 activation behavior exactly — no regression.
- All Part F static checks pass with zero deviation.
- `style-catalog.md` no longer contains the phrase "chiropractic clinic" or any other specific past-project citation in a descriptive field.
- Net word-count delta lands within roughly 15% of Part E's ~780–1,020-word estimate.

## Part H — Risks

- **The 4 new entries could still land in adjacent "considered design" territory** even if drawn from different traditions, if authored carelessly — mitigated by the concrete authoring constraint in §A.3 (≥2 of 4 from traditions with no native page/screen metaphor), not left as aspiration.
- **The family tie-breaker in `LAYOUT-010` is itself a judgment call**, not mechanically enforced — same accepted risk class as the rest of `LAYOUT-010`'s existing selection heuristic.
- **The evidence/hypothesis distinction adds one more DEFINE-time judgment call** — mitigated by keeping the test literal and bright-line ("is it stated in the brief's own text, yes/no"), deliberately not a fuzzy confidence estimate.
- **Over-governing risk:** tightening Case 3/4 could, if misapplied, also suppress Case 5's legitimate recurring-metaphor detection — mitigated by leaving Case 5's existing criterion untouched and scoping the tightening specifically to the name-based path Phase 6.4 evidence implicates.
- **Suppressing creative interpretation:** mitigated structurally — a hypothesis can still shape a candidate under ordinary Creative Interpretation latitude; only its governance weight (mandatory `LAYOUT-009` translation, "detected" logging) is withheld, not the idea itself.
- **Benchmark contamination recurring:** the same failure that produced the `style-catalog.md` residue could recur with the new entries or during the Part F benchmark — mitigated by the explicit governance rule in §A.6, stated as a standing rule for all future benchmark sessions, not just a one-time cleanup.
- **Context cost creep:** 10 entries is stated as this phase's ceiling; any future growth should re-run this same size-vs-diversity trade-off analysis rather than accreting silently.
- **Convergence into a different meta-style:** diversifying away from "premium editorial" risks only relocating convergence (e.g., everything reads as "industrial signage kit") if the new entries are too similar to *each other* — mitigated by requiring the 4 new entries to differ from each other in production family, not just from the existing 6.
- **Provenance/freshness:** addressed by keeping entries generic for now (§A.5) rather than accepting unverifiable real-source claims — the risk is deferred, not introduced.

## Part I — Non-Goals

Phase 6.5 will not: add Reicon; add Kinetics; add SmoothUI; redesign the motion architecture; expand Anti-Slop; add a new design dial; create a vector database; create an aesthetic classifier; create a giant reference catalog (10 is the stated ceiling); add live browser editing; redesign the pipeline; solve every source of genericness. All of these remain out of scope for this phase and open for separate evaluation later, unchanged from `PHASE-6.4-RESULTS.md` §15's own list.

## Recommendation

**IMPLEMENT.**

Evidence basis: `PHASE-6.4-RESULTS.md` independently validated the Visual References mechanism (§12, §13) and named exactly these two issues as the explicit basis for a next phase (§14), with concrete supporting evidence for both (§9's reference-family list, §10's brand-name governance gap) that this proposal verified directly against the live repository (§1) rather than accepting on the report's word alone. The fixes here are proportionate to the evidence: wording tightenings to two existing rules, one small addition to a selection heuristic, four new catalog entries authored under the existing schema, and one confirmed-safe field replacement — no new mechanism, no new pipeline stage, no new dial, consistent with the explicit architectural constraint given for this phase.

The one open judgment call this proposal accepts rather than resolves further — DEFINE's evidence-vs-hypothesis classification is a bright-line but still human/model judgment, not a mechanical check — is the same class of accepted risk this skill already carries for Genre inference and `LAYOUT-010`'s own selection heuristic. Not a reason to withhold implementation.

- **Estimated net word-count impact:** ~780–1,020 words across 7 files (smaller than Phase 6.4's own ~1,747-word delta, since most of this phase is wording precision rather than new rules).
- **Files affected:** `SKILL.md`, `references/rule-catalog/layout-interaction.md`, `references/visual-references.md`, `references/critique-protocol.md`, `references/style-catalog.md`.
- **Files protected:** `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md`, every `PHASE-*.md`, `anti-slop-registry.md`, `existing-project-safety.md`, `gesture-physics.md`, `color.md`, `typography.md`, `motion.md`, `accessibility.md`, `content-copy.md`, `performance-hardening.md`, any stack file.
- **Expected context-cost impact:** no new load event — every touched T2/T3 file already loads under its existing trigger; the only size growth is `visual-references.md`'s ~520–650-word addition within the same DIRECT/DESIGN-only trigger it already has.
- **Benchmark plan:** the 5-case table in Part F — cheap, single-page/component scale, no repeat of the full Clínica Atlas multi-page benchmark.
