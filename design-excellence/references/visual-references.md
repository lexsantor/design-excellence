# Visual References (T3)

Nine demonstration entries, not a catalog — same restraint `style-catalog.md` applies to itself. **10 entries is a hard ceiling for this pool (Phase 6.5); grow only when a genuinely new design possibility justifies it, never to fill a round number.** Gives DIRECT's EXPLORE step (`SKILL.md` §1, `layout-interaction.md` LAYOUT-010) a small set of externally-observed design possibilities to consider, so candidates aren't generated only from Genre's own default posture. **Observe → Abstract → Adapt. Never copy.**

REF-001–REF-006 (Phase 6.4) are web/documentation/editorial-adjacent production traditions. REF-007–REF-009 (Phase 6.5) deliberately draw from traditions with no native page/screen metaphor — transit/civic wayfinding, laboratory instrumentation, packaging/print ephemera — added because benchmarking found the original six, while each individually valid, shared one production family closely enough to still converge on a "premium editorial" visual language as a pool (`PHASE-6.4-RESULTS.md` §9). A fourth candidate (civic/government form field-sequencing) was considered and set aside for this pass — its distinguishing feature overlaps enough with ordinary form UX already covered elsewhere in this skill's own rules that it was a weaker addition than the three shipped here; revisit only if future evidence shows a real gap.

Entries describe a real, commonly-observed production pattern generically (a class of site, not a named brand) — no entry carries a recognizable source identity to begin with. Loads under the identical DIRECT/DESIGN-for-a-new-visual-system trigger `style-catalog.md` already uses (`SKILL.md` §7) — not a new load event.

## Schema

```
VisualReference
├── id
├── dimension              (browsing metadata only — never the diversity mechanism, LAYOUT-010)
├── observed               (2–4 concrete, checkable facts)
├── abstracted_principle   (the relationship/logic, stripped of any source identity)
├── compatible_with        (Register × Genre)
├── do_not_apply_to        (Register × Genre / brief-signal mismatches)
├── non_application_note   (explicit: what a literal copy would look like)
└── freshness              (last_verified_date, review_interval_days — anti-slop-registry.md's shape)
```

---

### REF-001 — Persistent asymmetric column pairing
- **dimension:** composition / macrostructure
- **observed:** long-form technical documentation sites often run a narrow, fixed nav/index column beside a wider, independently-scrolling content column, at a constant ratio across every page.
- **abstracted_principle:** a persistent, unequal split where one region orients (fixed, low-content) and the other delivers (scrolls, high-content) — orientation and content spatially separated rather than layered.
- **compatible_with:** brand-led/hybrid; editorial or modern-minimal.
- **do_not_apply_to:** product-led, dense high-frequency-interaction UI — a fixed column steals working screen area.
- **non_application_note:** don't copy the exact column ratio, nav typography, or imply "documentation site" as the subject.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-002 — Single dominant focal element across a scroll transition
- **dimension:** spatial hierarchy
- **observed:** some product-launch pages hold one large visual fixed in place while surrounding content scrolls past and around it.
- **abstracted_principle:** hierarchy through what doesn't move, not what's largest — a stationary anchor reads everything scrolling past as subordinate, regardless of its own size.
- **compatible_with:** brand-led; atmospheric-expressive/editorial; Medium–High `MOTION_INTENSITY`.
- **do_not_apply_to:** Low `MOTION_INTENSITY` or any scroll-motion-averse brief — the technique is inherently motion-dependent.
- **non_application_note:** don't copy the specific anchor asset, its exact fixed position, or the source's imagery.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-003 — Wayfinding as index, not menu
- **dimension:** navigation
- **observed:** some specimen-style sites present navigation as a literal enumerated index a user scans, current position highlighted within it rather than in a separate breadcrumb.
- **abstracted_principle:** navigation framed as "where am I in a bounded set," not "where can I go" — apt only when content is genuinely finite and countable.
- **compatible_with:** editorial; brand-led/hybrid; a closed, countable content set.
- **do_not_apply_to:** product-led, or any content set that grows/changes — an index implies a completeness the content doesn't have.
- **non_application_note:** don't copy the numbering typography, or use the index decoratively when content isn't actually enumerable.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-004 — Oversized numerals as structural dividers
- **dimension:** typography
- **observed:** some print-derived editorial sites use large running numerals (a folio, a section count) as the divider language instead of a rule or border.
- **abstracted_principle:** typography doing structural work (marking a boundary) rather than only communicative work — division through scale contrast inside the type system itself.
- **compatible_with:** editorial; brand-led; Medium–High `DESIGN_VARIANCE`.
- **do_not_apply_to:** modern-minimal/product-led, where the numeral competes with functional hierarchy instead of serving it.
- **non_application_note:** don't copy the specific numeral typeface or scale ratio — the principle is the divider logic, not that appearance.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-005 — Process imagery instead of polished hero photography
- **dimension:** imagery / art direction
- **observed:** some craft/maker sites use unstaged process photography (materials, hands, partial states) as hero imagery instead of one polished finished-product shot.
- **abstracted_principle:** credibility signaled through visible process rather than an idealized result — showing how something is made, not only its finished look.
- **compatible_with:** brand-led; editorial/atmospheric-expressive; briefs where craft/authenticity is a stated value.
- **do_not_apply_to:** any brief with no real process to show — fabricating "process" imagery is a fabrication risk (`SKILL.md` §9 #8), not a style choice.
- **non_application_note:** don't copy the subject matter, materials, or framing shown — the principle is process-over-polish, not any particular process.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-006 — Reveal tied to a persistent counted index, not a scroll-fade
- **dimension:** interaction / transition
- **observed:** some case-study/portfolio sites advance via a visible counter ("02/08") incrementing per section, each transition a discrete state change, not a continuous scroll-fade.
- **abstracted_principle:** progress made legible as a finite, countable sequence the user can watch themselves move through, not an open-ended scroll of unstated length.
- **compatible_with:** brand-led; editorial/playful; a genuinely finite content sequence.
- **do_not_apply_to:** Low `MOTION_INTENSITY` (discrete transitions still carry motion weight), or content with no real fixed count.
- **non_application_note:** don't copy the counter's typography/placement or exact transition timing — the principle is visible countable progress, not that implementation.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-007 — Color as the wayfinding system itself, not an accent on top of one
*(Phase 6.5 addition — non-page/screen tradition: transit/civic wayfinding.)*
- **dimension:** navigation
- **observed:** metro/rail network maps assign each line a distinct color that functions as the primary identification and navigation cue — platform signage, vehicle livery, and the map itself all key off the same color, and it means the same thing everywhere it appears, independent of medium (printed, backlit, handheld).
- **abstracted_principle:** color used as the navigational index itself, not a decorative accent layered on top of a separately-labeled system — the same color always denotes the same path, so a user can navigate by color alone without reading every label.
- **compatible_with:** hybrid/product-led register; modern-minimal or playful genre; content with a genuinely bounded, nameable set of parallel paths or sections (distinct product lines, service tiers, content tracks).
- **do_not_apply_to:** a brief with only one primary path/section, or a Low `DESIGN_VARIANCE` product-led context where a second color-coded system would compete with an existing token-based accent scheme.
- **non_application_note:** don't copy specific line colors, a map's geometric-distortion technique, or transit-specific iconography — the principle is color-as-index, not "look like a transit map."
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-008 — Hierarchy for someone mid-task, not someone deciding whether to proceed
*(Phase 6.5 addition — non-page/screen tradition: instrumentation / laboratory protocol documentation.)*
- **dimension:** information hierarchy / interaction
- **observed:** an instrument calibration card or lab protocol sheet sequences numbered steps meant to be followed while performing a task, not browsed for persuasion; state is tracked via checkboxes and tolerance fields rather than narrative copy, and there is no introductory framing — the first visible content is step one.
- **abstracted_principle:** content organized for someone already committed to a task ("what do I check next"), not someone deciding whether to proceed ("why should I") — hierarchy optimized for glanceable task-state rather than for persuasion or scanning.
- **compatible_with:** product-led register; modern-minimal genre; task-driven flows already underway (onboarding steps, checklists, setup wizards) where the user has already committed to completing the flow.
- **do_not_apply_to:** brand-led marketing/landing content whose entire job is persuasion before commitment — a no-persuasion structure there removes the exact thing the page needs to do.
- **non_application_note:** don't copy specific tolerance/measurement units or instrument-specific iconography — the principle is task-state-first hierarchy, not "look like lab equipment."
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90

### REF-009 — Segmentation by rule on a fixed canvas, not elevation
*(Phase 6.5 addition — non-page/screen tradition: packaging / print ephemera.)*
- **dimension:** composition / information hierarchy
- **observed:** a boarding pass or receipt compresses several independent facts (confirmation code, seat, time, amount) onto one small, fixed-size, non-scrolling surface, isolating each field with a rule or perforation rather than a card, shadow, or background-color block.
- **abstracted_principle:** hierarchy achieved through spatial segmentation on a bounded canvas (a rule or gap separating fields) rather than through elevation/shadow/card treatment — useful wherever a surface has a genuinely fixed size and must communicate several independent, equally-weighted facts at once.
- **compatible_with:** any register/genre, for a bounded summary surface (an order confirmation, a status card, a compact dashboard tile) where the content is a small set of independent facts, not a scrolling narrative.
- **do_not_apply_to:** primary scrolling page content — this principle is for bounded, fixed-size summary surfaces specifically, not general page layout.
- **non_application_note:** don't copy perforation/ticket-stub ornamentation itself as decoration — the principle is segmentation-by-rule for genuinely independent fields, not a ticket motif.
- **freshness:** last_verified_date: 2026-09-21 · review_interval_days: 90
