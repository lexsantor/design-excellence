# Principle Pool (T3)

Accepted design principles, curated outside this repository from observed production work and promoted here one at a time after review. A sibling pool to `visual-references.md`: the same capability, the same record family, the same trigger and the same selection rule, with its own ceiling and governance. **Observe → Abstract → Adapt. Never copy.**

**Role.** An EXPLORE input for DIRECT only (`SKILL.md` §1, `layout-interaction.md` LAYOUT-010). It gives EXPLORE further externally-observed possibilities to consider beside `visual-references.md`. Entries are generative possibilities, not rules: none is ever required, and "considered, judged unnecessary" is a valid outcome. Never used by CRITIQUE or AUDIT and never a quality bar.

**Loading.** Loads together with `visual-references.md` under the identical DIRECT/DESIGN-for-a-new-visual-system trigger (`SKILL.md` §7), never on its own. Not a new load event and not a new pipeline stage. LAYOUT-010 treats both files as one combined selection source: every entry is screened, and at most 2–3 entries in total across both pools are seriously considered, and its family tie-break compares production traditions across both pools.

**Ceiling.** 15 entries is a hard ceiling for this pool; the first curation pass stops at 8. `accepted` and `stale` entries both count. No single production cluster supplies more than 2 entries. The ceiling is not a target: grow only when a genuinely new possibility justifies it.

**Freshness.** Every entry carries `freshness.last_verified_date` and `freshness.review_interval_days`. An entry whose `status` is `stale`, or whose `last_verified_date + review_interval_days` has passed when this file is consulted, is **not considered**. Stale entries are re-verified or removed through curation, never silently kept.

**Identity and provenance boundary.** No entry carries a source identity: no brand, vendor, product, marketplace, path, screenshot, measurement, code, token, colour value, typeface, copy or label from any source. Each entry's `id` is opaque and is not resolvable from this repository; it is the only provenance carried here. The external curation catalog the entries come from is never read or queried at runtime, and this file never points outside itself. The skill behaves identically where that catalog does not exist.

**Sprint-curated entries.** PRN-0101 onward were curated on 2026-09-28 under a scoped human authorization, from inspected live builds and design files rather than through the external catalog; their source evidence is kept with curation records outside this skill package, is excluded from commits, and is never read at runtime. The identity boundary above applies to them unchanged.

**Changes.** Entries change only through explicit, reviewed promotion: a re-verified entry gets a new `last_verified_date`; a withdrawn or superseded entry is removed from this file; a replacement arrives as a new entry. There is no automatic synchronization. This repository may also remove an entry under its own governance.

## Schema

```
Principle
├── id                               (opaque; the heading shows the id only, no title)
├── status                           (accepted | stale; only accepted entries are considered)
├── dimension                        (browsing metadata only, never the diversity mechanism, LAYOUT-010)
├── organizing_surface               (LAYOUT-009 organizing surfaces the principle decides)
├── observed                         (generalized, identity-stripped facts)
├── abstracted_principle             (the relationship/logic, stripped of any source identity)
├── compatible_with.registers        (Register)
├── compatible_with.genres           (Genre)
├── do_not_apply_to                  (contexts where the principle does not apply)
├── non_application_note             (explicit: what a literal copy would look like)
├── evidence_basis                   (evidence types behind the principle)
├── support_breadth.kind             (single-source | multi-source)
├── support_breadth.cluster_count    (distinct production clusters supporting it)
├── family                           (production tradition, for the LAYOUT-010 tie-break)
├── freshness.last_verified_date     (anti-slop-registry.md's shape)
├── freshness.review_interval_days
├── carrier_surfaces                 (optional: LAYOUT-009 carrier surfaces that reinforce but do not constitute it)
├── compatible_with.notes            (optional: applicability qualification)
└── confidence                       (optional: high | medium | low)
```

---

### PRN-0001

- **id:** PRN-0001
- **status:** accepted
- **dimension:** macrostructure
- **organizing_surface:**
  - macrostructure
- **observed:** One source, examined at one wide landscape frame and one narrow portrait frame. On the wide frame the entry page is exactly one frame tall and does not scroll: a text column holding a name, a display headline, a short paragraph and two actions sits beside an image panel, and a band along the bottom edge carries four labelled facts. On the narrow frame the same parts stack in one column as text, image, facts, which is their left-to-right, then top-to-bottom order on the wide frame; none is removed, and the page scrolls to about 1.2 frames tall. Display and body type sizes are defined against the smaller of a width-relative and a height-relative term; on the wide frame the height term is the one in effect, and on the narrow frame the headline sits at its minimum size.
- **abstracted_principle:** On a wide landscape frame, the entry view extends exactly as far as the frame: it is one complete unit (an identity, a statement and its actions, with any short labelled facts that fall inside the frame) that ends at the frame's edge, with nothing placed below it. Display type is sized by the smaller of a width-relative and a height-relative term, so on a wide frame where the height term is the smaller, the frame height that bounds the unit also bounds the type. On a narrow portrait frame the unit is not cut down: every part is kept and stacked in one column, in the order the parts sit on the wide frame (left to right, then top to bottom), and the view is allowed to scroll. There the display type may rest at its minimum size.
- **compatible_with.registers:**
  - brand-led
- **compatible_with.genres:**
  - editorial
  - modern-minimal
  - atmospheric-expressive
  - playful
- **do_not_apply_to:**
  - Product-led or application entry views whose first job is to let the user work: the entry there is a workspace, not a bounded presentational unit.
  - Entry content that cannot fit one wide frame without cutting parts, hiding them, or pushing type or touch targets below usable size; the unit must fit as a whole or the principle does not apply.
  - Forcing the one-frame bound on narrow frames: the supporting evidence lets the narrow layout scroll. Frames other than one wide landscape and one narrow portrait frame, including short landscape windows, are unverified.
  - Sites whose value is the continuous scroll, such as feeds, long-form reading or catalogues.
  - As a rule for reaching deeper content: the principle is silent on navigation and routing. Where the rest of the content lives and how it is reached must be decided on its own evidence.
  - As a content-selection or ranking rule: it bounds how much the entry view holds and where it ends, not which facts belong in it or in what priority. The supporting evidence does not show that the facts inside the frame were chosen specifically for the entry view.
  - Other pages of the same site: the principle covers the entry view only, not a page model for a whole site, and keeping every part on narrow frames is claimed for the entry view only.
- **non_application_note:** A literal copy would reproduce the source's proportions between a text column and an image panel, its pairing of display and body typefaces and its emphasis treatment, its colour theme, and the particular labels and placement of its fact band. None of these is the principle: the principle is an entry view whose extent is bounded by the frame, with display type bound to the smaller of a width-relative and a height-relative term, and a narrow-frame fallback that keeps every part in the wide frame's order and scrolls.
- **evidence_basis:**
  - RENDERED
  - CODE
- **support_breadth.kind:** single-source
- **support_breadth.cluster_count:** 1
- **family:** commercial-ui-template
- **freshness.last_verified_date:** 2026-09-25
- **freshness.review_interval_days:** 90
- **carrier_surfaces:**
  - typography
  - responsive-behavior
- **compatible_with.notes:** Brand register only, the register of the source. Genre-neutral by curator judgment: no clause depends on a genre's default posture, so all four genres are listed as target applicability. This is not a statement about the source's genre.
- **confidence:** medium

### PRN-0003

- **id:** PRN-0003
- **status:** accepted
- **dimension:** content-architecture
- **organizing_surface:**
  - content-architecture
- **observed:** One source, read in code and rendered at one wide and one narrow frame. A claims section makes three claims, each closing with a short list of what it says is recorded. Each example item on the same page carries a small field list holding the values the first claim says are recorded, with an action on one of them; an example derived from another shows a value taken from its parent in place of its own. A second page lists a larger set of examples with the same fields; some are labelled as derived from a named earlier example and reference it, which is the derivation claim made on the first page. Of the other two claims, one (a capacity claim) has no field on any example, and the other is carried only in part: one of the record fields it names appears on the examples. On the narrow frame the first page keeps every example's field list; the second page drops the per-example fields from its list, keeps each example's derivation label, and shows the full field list of the selected example, including its parent reference, in a detail view placed above the list.
- **abstracted_principle:** Structure a presentational page's examples by its claims: couple the section that makes claims with the section that shows examples, so that each claim that can be traced to an item is carried as a field every example exposes, and a claim about deriving one thing from another is carried by an example that names the one it came from. Claims that no item can carry stay stated claims and are not dressed up as fields. The examples section then takes its structure from the claims section instead of running beside it as an independent gallery. Where space is short, the fields may move into a detail view of the selected item; the coupling holds only while every item's fields remain reachable there.
- **compatible_with.registers:**
  - brand-led
  - hybrid
- **compatible_with.genres:**
  - editorial
  - modern-minimal
  - atmospheric-expressive
  - playful
- **do_not_apply_to:**
  - Claims with no item-level trace (speed, support, reliability, scale): they stay stated claims, and adding fields for them puts values on items that no claim needs. The supporting source leaves one such claim without any field and carries another only in part.
  - Shipping the structure with placeholder values: example fields must hold real items' values, otherwise they give the form of proof without its substance and fall under the rule against fabricated data.
  - Items whose properties cannot be shown (private, sensitive or proprietary data).
  - Working views in a product the user operates: the principle concerns examples on presentational pages, not how records are shown in a tool.
  - Items that carry only a name or a caption: without at least one claim an item can actually carry, there is nothing to couple.
  - Dropping the fields on constrained frames with no other way to reach them; the supporting evidence examined only one wide and one narrow frame.
  - As a metadata-display rule: where showing item fields is already the default for the genre, the principle adds only the choice of fields by the claims and the parent reference; showing fields alone is not an application.
- **non_application_note:** A literal copy would reproduce the source's particular field set, its value formats, its per-field actions, the split between a short example set and a full list, and its labels for derived items; the fields are also not meant to be rendered as middle-dot meta strings or as a uniform card grid. None of these is the principle: the principle is that the examples section is structured by the claims section, so each traceable claim is carried by a field on every example and a derivation claim by an example that names its parent.
- **evidence_basis:**
  - RENDERED
  - CODE
- **support_breadth.kind:** single-source
- **support_breadth.cluster_count:** 1
- **family:** commercial-ui-template
- **freshness.last_verified_date:** 2026-09-25
- **freshness.review_interval_days:** 90
- **carrier_surfaces:**
  - responsive-behavior
- **compatible_with.notes:** Useful where the product produces or keeps inspectable items (records, orders, submissions, versions, requests). Genre-neutral by curator judgment: the principle couples two sections of a page through the item fields the claims determine, not a presentation. Hybrid is an extrapolation from a brand-led source page.
- **confidence:** medium

### PRN-0101

- **id:** PRN-0101
- **status:** accepted
- **dimension:** interaction
- **organizing_surface:**
  - interaction
  - content-architecture
- **observed:** Three sources from two production clusters, examined as rendered screens of a live build and design files. In an operations console, an automated agent's proposed reallocation is shown as held: one panel gives the evidence, names the admin-set threshold the change exceeds and says that nothing has executed, beside two exits (accept the change, or leave things as they are); the governing limits are listed read-only in a panel beside the proposal, with a sentence that the agent acts freely below them and stops at them, and they are edited on the agent's own detail screen. That detail screen's decision log records the agent's discarded outputs next to its executed steps. In a second product of the same cluster, a settings screen assigns each kind of action one of three autonomy levels, from acting and logging, through acting after a notice period unless stopped, to waiting for approval, and an activity stream present on every inspected screen attributes each automated entry to the acting agent with a line naming its basis, and pins the number of items waiting for a person and the age of the oldest. A queue in the first product states its admission rule once at the top, and each item carries the gate that rule assigns it. In a writing tool from a different cluster, the assistant answers a request with alternatives to insert instead of editing the document, and the version history lists the assistant as an author beside the human authors.
- **abstracted_principle:** When the product acts on the user's behalf, the unit of the interface is the action in relation to the authority it acted under, not the action alone. Every automated change is attributed the way a human change is (who acted, on what basis) and sits in one explicit state: done and logged, held at a limit, waiting for a decision, or discarded. A held action shows its evidence, the limit it crossed and the fact that nothing has happened yet, with the decision beside it. The governing limits and the autonomy level of each kind of action are visible beside the actions they govern and editable in one known place, and the number of actions waiting for a person stays visible wherever the user is.
- **compatible_with.registers:**
  - product-led
  - hybrid
- **compatible_with.genres:**
  - editorial
  - modern-minimal
  - atmospheric-expressive
  - playful
- **do_not_apply_to:**
  - Products with no delegated or automated actions: adding agent attribution or autonomy settings to them invents a system that does not exist.
  - Brand and marketing pages.
  - Single-shot generators whose output is the whole point and where nothing waits for approval, and inline completion, where an approval step adds friction without reducing risk.
  - Limits the user cannot change: then show attribution and state only; a displayed limit nobody can edit is noise.
  - Narrow frames: unverified. The supporting evidence was examined at wide frames; one narrow capture overflowed.
- **non_application_note:** A literal copy would reproduce a side column of named agents with a monospace provenance footer, confidence rings, a three-way segmented autonomy control, paired approve and keep buttons, rule identifiers in labels, or "AI" styling applied to a product that delegates nothing. None of these is the principle: the principle is attribution, one explicit state per automated action, and the governing limit placed beside the action it constrains.
- **evidence_basis:**
  - RENDERED
  - DESIGN-FILE
- **support_breadth.kind:** multi-source
- **support_breadth.cluster_count:** 2
- **family:** commercial-product-ui-kit
- **freshness.last_verified_date:** 2026-09-28
- **freshness.review_interval_days:** 90
- **carrier_surfaces:**
  - responsive-behavior
- **compatible_with.notes:** Hybrid applies only where a product surface with delegated actions is embedded. Genre-neutral by curator judgment: every clause is structural. The full pattern (attribution, per-action autonomy levels, limit beside the action) was seen in one cluster; the other cluster shows attribution and proposal-instead-of-edit.
- **confidence:** medium

### PRN-0103

- **id:** PRN-0103
- **status:** accepted
- **dimension:** content-architecture
- **organizing_surface:**
  - content-architecture
- **observed:** Two sources from one production cluster, examined as rendered live builds at one wide and one narrow frame. An outcomes section presents three figures, each followed by the population it was measured on and the time window, under a statement of which populations the figures exclude, with a closing line that restates population, window and update cadence. A second site states the population its figures are drawn from, and introduces a shown sample as a count out of the whole set it was drawn from. On the narrow frame every figure keeps its definition next to it.
- **abstracted_principle:** Show a figure on a presentational page with its denominator: the population it was measured on, the window, and the rule that admitted items into it; introduce a shown sample with its share of the whole, and say what the figures do not represent. The definition travels with the figure at every frame size instead of sitting in a footnote, so the figure reads as a measurement rather than a slogan.
- **compatible_with.registers:**
  - brand-led
  - hybrid
- **compatible_with.genres:**
  - editorial
  - modern-minimal
  - atmospheric-expressive
  - playful
- **do_not_apply_to:**
  - Figures whose population, window or admission rule the brief does not supply: never invent them (anti-fabrication); state the figure as supplied, or leave a marked placeholder.
  - Briefs that supply no figures: do not create a figures section in order to apply this.
  - Values that are not measurements, such as prices, hours or specifications.
- **non_application_note:** A literal copy would reproduce oversized dotted numerals, a three-figure column, the wording of the disclaimer line or a grid background. The principle is that every figure carries its denominator and scope beside it.
- **evidence_basis:**
  - RENDERED
- **support_breadth.kind:** multi-source
- **support_breadth.cluster_count:** 1
- **family:** commercial-ui-template
- **freshness.last_verified_date:** 2026-09-28
- **freshness.review_interval_days:** 90
- **carrier_surfaces:**
  - typography
  - responsive-behavior
- **compatible_with.notes:** Both sources look like one producer, so the breadth is one cluster. Genre-neutral by curator judgment.
- **confidence:** medium

### PRN-0104

- **id:** PRN-0104
- **status:** accepted
- **dimension:** interaction
- **organizing_surface:**
  - interaction
  - content-architecture
- **observed:** Three sources from two production clusters, examined as rendered live builds and operated. A property site asks for the amount the buyer can pay each month, works the purchase ceiling out from it with deposit and rate controls, prints its assumptions in one sentence, and counts how many of the listed homes fall under the result; moving the amount changed both the ceiling and the count. A tutoring site recomputes its median price and the monthly total when a level is chosen, and, as weaker corroboration, its booking step keeps a running cost summary that ends with what is charged at booking. A software pricing page shows its pricing formula and the reason for its plan recommendation; raising usage to the maximum switched the recommended plan.
- **abstracted_principle:** Present price as a calculation that starts from a quantity the buyer already knows (a budget, a usage level, a level of need) and returns the answer in the buyer's own unit (what it buys, what it costs each month, which plan fits and why). The arithmetic and its assumptions stay visible, and the result is tied back to the actual offer: how many real items fit, or which plan and why. The buyer changes inputs, alongside or ahead of any fixed tiers.
- **compatible_with.registers:**
  - brand-led
  - hybrid
- **compatible_with.genres:**
  - editorial
  - modern-minimal
  - atmospheric-expressive
  - playful
- **do_not_apply_to:**
  - A single flat price: there is nothing to compute.
  - Prices that depend on a quote the page cannot compute honestly.
  - Any rate, formula or input range the brief does not supply: never invent one (anti-fabrication).
  - Contexts where a computed "what you can afford" answer needs regulatory disclosures the brief does not provide.
- **non_application_note:** A literal copy would reproduce a circular dial with tick marks, a slider trio, a large headline announcing the reverse calculation, or a receipt line stating a zero charge. The principle is the direction of the calculation (from what the buyer knows to what it gets them) with visible arithmetic tied to the real offer.
- **evidence_basis:**
  - RENDERED
- **support_breadth.kind:** multi-source
- **support_breadth.cluster_count:** 2
- **family:** commercial-ui-template
- **freshness.last_verified_date:** 2026-09-28
- **freshness.review_interval_days:** 90
- **compatible_with.notes:** Genre-neutral by curator judgment.
- **confidence:** medium
