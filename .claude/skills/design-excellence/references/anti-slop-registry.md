# Anti-Slop Registry (T3)

**Status: first-pass curated data requiring future review.** This registry is not permanently authoritative. It was populated once, on 2026-09-20, from `FORENSIC-EXTRACTION.md`'s merged/deduplicated anti-slop findings across Impeccable, Taste, Anthropic, and Hallmark. It is a curated subset — entries were included only where the source extraction captured a full mechanism/reason/fix, not merely a pattern name. Several named tells appear in the source taxonomies (e.g. Hallmark's "the AI nav," "card-in-card," "re-drawn UI chrome") without enough captured detail here to state a mechanism honestly; they are deliberately omitted rather than guessed at, pending a future pass back to the original sources.

**Every record below is time-bound.** These are calibrated to *current* model-generation defaults, not timeless design law. `review_interval_days: 90` on every entry — if `last_verified_date` is more than 90 days stale when this registry is consulted, treat the entry as `needs-review`, not as settled fact. No automated validator runs this check in V1 (see `SKILL.md` §9 core principle 4, and `ARCHITECTURE.md` §10/§23) — a future session or human review is required.

**Genre and Register change applicability, not the entry's existence.** A pattern flagged here as generic in one context can be a required move in another — the `applicability`/`exceptions` fields say which. Never flatten these into a single always-ban list.

---

### SLOP-001 — Italic on display/heading type
- **category:** typography · **severity:** major
- **statement:** italic on any heading/display type — including a single italicized word for emphasis inside an otherwise-roman headline — reads as one of the most recognizable current AI tells. Emphasis should come from weight, accent color, or a drawn underline instead; italic survives only inside running body copy.
- **applicability:** `genre: modern-minimal, product-led` — treat as a hard fail. `genre: editorial` — may have narrower legitimate exceptions (a literary/publishing-adjacent brief); declare explicitly if used.
- **exceptions:** declared editorial use, stated in `.design/context.md` Known Exceptions.
- **remediation:** replace the italic emphasis with a weight, color, or underline treatment.
- **source:** Hallmark (typography discipline gates 37–38) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-002 — Accented single word in a headline
- **category:** typography · **severity:** moderate
- **statement:** italic/bold/color applied to exactly one word inside an otherwise-plain headline, for emphasis, is a named generation-artifact tell.
- **applicability:** universal default-ban; no strong genre exception found in the source material.
- **remediation:** remove the single-word accent; if emphasis is genuinely needed, restructure the sentence or use scale/color at the phrase level, not one isolated word.
- **source:** Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-003 — Unnecessary eyebrow labels
- **category:** layout · **severity:** moderate
- **statement:** tracked-out ALL-CAPS labels above content, used reflexively rather than because the content needs a category label. Mechanically checkable: count instances, fail if count exceeds `ceil(sectionCount / 3)`.
- **applicability:** universal; the ratio itself is a tunable default, not a hard law.
- **remediation:** remove eyebrows that don't add real category information; if kept, ensure the count stays within the ratio.
- **source:** Anthropic Frontend Design (upstream) + Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-004 — Eyebrow/tag-left-header-right hanging layout
- **category:** layout · **severity:** critical
- **statement:** any wrapper containing both a section label/number and a heading, laid out as two columns (label left, heading right), is one of the most-recognized templated-editorial-SaaS tells. Must resolve to single-column.
- **applicability:** universal — deliberately non-negotiable, per the source, even under an instruction to "preserve structural parity with a reference build" (the reference build predates the rule).
- **exceptions:** none stated in source material — this is the one entry in this registry explicitly flagged as overriding even a literal "match this" instruction. Cross-reference `SKILL.md` §3 (P1 override, disclosed) before applying that override in practice — this registry entry alone does not grant silent-override authority; the disclosure requirement still applies.
- **remediation:** collapse to block/flex-column/grid-1fr.
- **source:** Hallmark · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-005 — Middle-dot meta strings and em-dash fragment labels
- **category:** content-copy · **severity:** minor
- **statement:** meta strings joined with middle dots ("A · B · C") and "WORD — fragment" em-dash labels are template-chrome tells independent of color choice.
- **applicability:** universal.
- **remediation:** rewrite as plain prose or a simple list.
- **source:** Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-006 — Arrow appended to every link/button
- **category:** content-copy · **severity:** minor
- **statement:** a `→` glyph appended reflexively to every link/button label, regardless of whether it communicates anything.
- **applicability:** universal; a single, deliberate use (e.g. one primary CTA) is not a violation — the tell is doing it *everywhere*.
- **remediation:** reserve the arrow for genuine directional/navigational cues.
- **source:** Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-007 — "SaaS-card kit" uniform cardification
- **category:** layout · **severity:** major
- **statement:** identical rounded cards, one border-radius value everywhere, uniform `rgba(0,0,0,.1)` shadow on every surface, gradient-wash decoration — a default reached for regardless of whether the content is "truly distinct and actionable." Includes nesting cards inside cards.
- **applicability:** `genre: modern-minimal, product-led` — high risk. Cards remain legitimate when content is genuinely distinct/actionable and radius/shadow are deliberately varied for hierarchy, not uniform by default.
- **remediation:** use cards only where content is truly distinct and actionable; vary radius/shadow/elevation to encode hierarchy, never apply one flat treatment everywhere.
- **source:** Anthropic Frontend Design (upstream) + Impeccable · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-008 — Glassmorphism as unconsidered default
- **category:** components · **severity:** moderate
- **statement:** translucent/blurred surfaces reached for reflexively rather than as a deliberate material-language choice.
- **applicability:** `genre: atmospheric-expressive` — legitimate when chosen deliberately as the visual language, with layer weight (blur+shadow) encoding hierarchy and light translucent surfaces never stacked on each other (legibility collapse). `genre: modern-minimal, product-led` — treat as a default-avoidance flag.
- **remediation:** either commit to it as a stated material-language decision (in `.design/context.md`) or remove it.
- **source:** Impeccable · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-009 — Gradient text on headlines/metrics
- **category:** typography/color · **severity:** moderate
- **statement:** gradient-filled text applied to hero headlines or stat/metric numbers by default.
- **applicability:** universal default-avoidance; a deliberate, register/genre-declared brand treatment is not automatically a violation but should be a stated choice, not a reflex.
- **remediation:** use solid color + weight/scale for emphasis instead.
- **source:** Impeccable + Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-010 — Near-black standing in for true black
- **category:** color · **severity:** minor
- **statement:** `#0B0B0B`/`#111` used as a "sophisticated" substitute for true black, applied reflexively rather than as part of a considered dark-neutral scale (cross-reference COLOR-005 for the correct construction).
- **applicability:** universal.
- **remediation:** derive dark neutrals from the OKLCH construction recipe (COLOR-004) instead of reaching for one specific hex.
- **source:** Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-011 — Model-specific self-tell accent clusters
- **category:** color · **severity:** major
- **statement:** four named generation clusters observed for the current model generation: (1) warm cream `#F4F1EA` + high-contrast serif + terracotta accent near `#D97757`; (2) near-black background + single bright acid-green/vermilion accent; (3) broadsheet layout, hairline rules, zero border-radius, dense newspaper columns; (4) the "SaaS-card kit" (see SLOP-007). None of these patterns are bad — they are defaults rather than choices, and the problem is using one *regardless of subject*, not the pattern itself.
- **applicability:** flag when a cluster appears without a stated reason tied to the actual brief/subject; not a violation when deliberately chosen and declared.
- **exceptions:** any of the four, explicitly chosen and stated in `.design/context.md` Known Exceptions with a subject-specific rationale.
- **remediation:** if unconsidered, pick a direction actually derived from the subject/register/genre instead.
- **gestalt check (Phase 6 correction):** validated as a combination, not per-element, at CRITIQUE Level 1 axis 1 (`critique-protocol.md`) — closes a gap where each element of a cluster could individually pass its own atomic rule elsewhere in this registry while the combination still matched one of the four clusters above. This entry's cluster definitions are unchanged; only where the comparison happens is new.
- **source:** Anthropic Frontend Design (upstream) — **highest-priority entry for review**, since it names one specific model family's own output tendencies and will go stale fastest of anything in this registry. · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-012 — Broadsheet newspaper layout as unconsidered default
- **category:** layout · **severity:** minor
- **statement:** hairline rules, zero border-radius, dense newspaper columns, reached for reflexively.
- **applicability:** `genre: editorial` — this is a legitimate, often-correct genre choice, not a violation, when deliberately selected. `genre: modern-minimal, playful, atmospheric-expressive` — flag as a default-avoidance signal.
- **remediation:** confirm the layout was chosen for the brief's editorial genre, not defaulted into.
- **source:** Anthropic Frontend Design (upstream) · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-013 — Category-reflex palette
- **category:** color · **severity:** major
- **statement:** if the palette is guessable from the domain/category name alone (a "wellness brand" palette, a "fintech" palette), it has failed — the palette should come from the specific brief, not the vertical stereotype.
- **applicability:** universal.
- **remediation:** re-derive color anchor from a subject-specific reference (a physical object, a real detail from the brief), not the category default.
- **source:** Impeccable · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-014 — Reflex-default typeface list
- **category:** typography · **severity:** moderate
- **statement:** a rotating set of currently-overused "training-data default" typefaces reached for reflexively rather than chosen via the font-selection procedure (TYPE-002). The specific current list is intentionally not hardcoded here — it changes faster than this registry's review interval warrants embedding literal names; consult the most recent review pass.
- **applicability:** universal; the *procedure* (TYPE-002) is the durable defense, this entry exists to flag that reflex-picking without running the procedure is itself the violation.
- **remediation:** run TYPE-002's font-selection procedure before finalizing a typeface choice.
- **source:** Impeccable + Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-015 — Loading-message clichés
- **category:** content-copy · **severity:** minor
- **statement:** whimsical loading-state copy that has itself become a recognizable AI-generated-copy tell ("Herding pixels," "Teaching robots to dance," "Consulting the magic 8-ball").
- **applicability:** universal.
- **remediation:** use a plain, functional loading message, or a genuinely brand-specific voice — not a generic "clever" placeholder.
- **source:** Impeccable · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-016 — Performative-craftsman copy register
- **category:** content-copy · **severity:** minor
- **statement:** phrases like "quietly trusted by," "field notes," or similarly affected artisan-voice copy, reached for reflexively regardless of whether the brand actually has that register.
- **applicability:** `genre: editorial, atmospheric-expressive` with an explicitly craft-oriented brief — may be legitimate. `genre: modern-minimal, product-led` — near-always a mismatch.
- **remediation:** replace with plain, direct copy matched to the brief's actual register.
- **source:** Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-017 — Em-dash as a stylistic separator
- **category:** content-copy · **severity:** minor
- **statement:** the em-dash used as a clause separator is currently a well-known model tell. Stated as an absolute ban (no "use sparingly" exception) because the source that originated this rule documented that a softer "sparingly" version was empirically ignored by the model it was written for.
- **applicability:** universal, but explicitly flagged as the most model-generation-specific, fastest-aging entry in this registry after SLOP-011 — re-verify this one first at the next review pass.
- **remediation:** rewrite with a period, comma, or restructured sentence.
- **source:** Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-018 — Version-label and section-numbering eyebrows
- **category:** layout/content-copy · **severity:** moderate
- **statement:** labels like "V0.6," "BETA," "00/INDEX," or "001 · Capabilities" used as decorative eyebrows with no real versioning/indexing meaning behind them.
- **applicability:** universal — legitimate only when the label is factually true (an actual version number, an actual index the user can navigate).
- **remediation:** remove if decorative; keep only if functionally accurate.
- **source:** Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90

### SLOP-019 — Purple/generic-gradient hero as unconsidered default
- **category:** layout/color · **severity:** major
- **statement:** a purple (or purple-to-cyan) gradient hero background, reached for as a default rather than derived from the subject.
- **applicability:** universal default-avoidance; a genuinely brief-derived purple palette (the subject's actual brand color happens to be purple) is not a violation.
- **remediation:** re-derive the hero treatment from COLOR-004's construction recipe and the subject's actual anchor color, not a generic gradient.
- **source:** Hallmark + Taste · **created_date:** 2026-09-20 · **last_verified_date:** 2026-09-20 · **confidence:** first-pass · **status:** active · **replacement_id:** — · **review_interval_days:** 90
