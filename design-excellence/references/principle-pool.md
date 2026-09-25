# Principle Pool (T3)

Accepted design principles, curated outside this repository from observed production work and promoted here one at a time after review. A sibling pool to `visual-references.md`: the same capability, the same record family, the same trigger and the same selection rule, with its own ceiling and governance. **Observe → Abstract → Adapt. Never copy.**

**Role.** An EXPLORE input for DIRECT only (`SKILL.md` §1, `layout-interaction.md` LAYOUT-010). It gives EXPLORE further externally-observed possibilities to consider beside `visual-references.md`. Entries are generative possibilities, not rules: none is ever required, and "considered, judged unnecessary" is a valid outcome. Never used by CRITIQUE or AUDIT and never a quality bar.

**Loading.** Loads together with `visual-references.md` under the identical DIRECT/DESIGN-for-a-new-visual-system trigger (`SKILL.md` §7), never on its own. Not a new load event and not a new pipeline stage. LAYOUT-010 treats both files as one combined selection source: at most 2–3 entries are considered in total across both pools, and its family tie-break compares production traditions across both pools.

**Ceiling.** 15 entries is a hard ceiling for this pool; the first curation pass stops at 8. `accepted` and `stale` entries both count. No single production cluster supplies more than 2 entries. The ceiling is not a target: grow only when a genuinely new possibility justifies it.

**Freshness.** Every entry carries `freshness.last_verified_date` and `freshness.review_interval_days`. An entry whose `status` is `stale`, or whose `last_verified_date + review_interval_days` has passed when this file is consulted, is **not considered**. Stale entries are re-verified or removed through curation, never silently kept.

**Identity and provenance boundary.** No entry carries a source identity: no brand, vendor, product, marketplace, path, screenshot, measurement, code, token, colour value, typeface, copy or label from any source. Each entry's `id` is opaque and is not resolvable from this repository; it is the only provenance carried here. The external curation catalog the entries come from is never read or queried at runtime, and this file never points outside itself. The skill behaves identically where that catalog does not exist.

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
