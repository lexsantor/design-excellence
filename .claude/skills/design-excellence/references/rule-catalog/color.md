# Color — Rule Catalog (T2)

Five complementary layers merged per `FORENSIC-EXTRACTION.md` §9 (not five competing answers): commitment ladder (how much color), construction recipe (how it's generated), token schema (how it's implemented), anti-convergence rotation (how repetition is avoided), and the contrast-failure catalog (what breaks in practice). AI-tell-flavored content (specific converged hex families, model-self-tell hex codes) lives in `anti-slop-registry.md`, freshness-governed — not duplicated here.

---

### COLOR-001 — Commitment ladder
- **category:** color · **layer:** P8
- **principle:** Restrained (tinted neutrals + ≤10% accent) → Committed (one color, 30–60% coverage) → Full palette (3–4 deliberate roles) → Drenched (surface IS the color). The "≤10% accent" rule applies only at the Restrained tier — a direct fix to the common over-generalized 60-30-10 rule.
- **severity:** moderate
- **applicability:** `genre: atmospheric-expressive` and `playful` default toward Committed/Drenched; `modern-minimal` and `product-led` register default toward Restrained/Committed. `DESIGN_VARIANCE` High band pushes toward the ladder's higher tiers even within a genre whose own default sits lower; Low band holds at Restrained/Committed regardless of genre default (Phase 4 correction — first real rule-catalog consumer of this dial). Medium band (Phase 6 correction): the genre's own default tier applies, but the direction must visibly move at least one rung off that default's most conservative edge — a Medium-declared variance may not land at the same minimum-commitment result a Low band would produce.
- **exceptions:** a deliberate brand accent-as-background (e.g. a solid CTA band) can exceed the tier's default ceiling — declare it explicitly in `.design/context.md` Known Exceptions.
- **evidence:** names the actual failure mode (overusing "the brand color" because it's the brand color) instead of a vague "don't overdo it."
- **freshness:** status: permanent.
- **validation:** mechanical-countable (compute accent color's viewport-area coverage against the declared tier's ceiling).
- **remediation:** pull the coverage back to the declared tier, or explicitly re-declare a higher tier with rationale.

### COLOR-002 — 60-30-10 reframed as visual weight
- **principle:** the ratio is about *visual weight* (size × saturation × contrast), not literal pixel/area count.
- **category:** color · **layer:** P8 · **severity:** minor
- **applicability:** universal wherever the 60-30-10 heuristic is invoked.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** re-balance by weight, not by measuring pixels.

### COLOR-003 — On-color token requirement + audit trail
- **principle:** every color role ships its paired `on-<role>` foreground token (primary/on-primary, accent/on-accent, etc.), not just background swatches. Deliberate contrast-driven adjustments to a token's "natural" brand-adjacent value are documented with a note (e.g. "accent adjusted from #F97316 — failed 4.5:1, corrected"), not silently lost.
- **category:** color · **layer:** P5 · **severity:** major
- **applicability:** universal wherever CSS custom-property theming is used.
- **evidence:** on/foreground pairing is where generated color systems most often break contrast silently; recording *why* a value was adjusted makes the palette auditable instead of a black box.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (every background-bearing role has a paired on-token; overrides logged in `.design/context.md` Known Exceptions).
- **remediation:** add the missing on-token; verify it meets A11Y-001.

### COLOR-004 — OKLCH 4-layer construction recipe
- **principle:** build palettes in OKLCH as paper / ink / neutrals / accent. Neutrals are tinted toward the anchor hue at low chroma — never zero-chroma "flat grey." Accent capped at ~3–5% of viewport area by default (genre may raise this explicitly — atmospheric-expressive can go to ~20–30%). Dark mode transforms lightness/chroma only, never inverts hue, with a stated body-text weight reduction (~50 units) to compensate for the optical weight of light-on-dark text.
- **category:** color · **layer:** P8 · **severity:** moderate
- **applicability:** universal for token-based color systems; the OKLCH-specific mechanics are implementation detail, portable to any perceptually-uniform color space.
- **exceptions:** accent-area ceiling is a default, not a law — genre/brief can explicitly raise it (see COLOR-001 exceptions).
- **evidence:** the *generator function* rather than a pre-baked palette list — complements catalog-style references (`style-catalog.md`) rather than competing with them.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (accent viewport-area %; neutral chroma > 0 check; dark-mode hue-preservation check).
- **remediation:** re-run the construction recipe rather than hand-patching individual swatches.

### COLOR-005 — Dark mode is not inverted light mode
- **principle:** depth via lighter surfaces, not shadows (shadows read as flat/invisible on dark). Desaturate accents slightly. Never pure black — use a dark tinted neutral.
- **category:** color · **layer:** P8 · **severity:** minor
- **applicability:** any interface shipping a dark theme.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag `#000`/`#fff` literal usage; flag box-shadow-only elevation in dark theme).
- **remediation:** replace pure black/white with tinted neutrals; add a surface-lightness elevation step.

### COLOR-006 — Anti-convergence rotation mechanism
- **principle:** when a project's category/vertical has a known converged default (the pool of current defaults lives in `anti-slop-registry.md`, freshness-governed), detect it, avoid it, and rotate through a small set of named alternatives — never repeating the same alternative twice in a row for the same project.
- **category:** color · **layer:** P6 (anti-slop) · **severity:** major
- **applicability:** universal mechanism; the specific converged-default pool per vertical is time-bound (see the registry, not this rule).
- **evidence:** the *mechanism* (detect convergence → ban → rotate → no-repeat) generalizes past any one vertical's current palette monoculture.
- **freshness:** status: permanent (mechanism); the pool of what's currently converged is in `anti-slop-registry.md` with its own freshness fields.
- **validation:** mechanical-countable, checked against Fingerprint History (`.design/context.md`).
- **remediation:** pick the next unused alternative in rotation.

### COLOR-007 — Background-lightness-flip contrast bug
- **principle:** any section whose background lightness drops below 50% must flip its text-color token in the *same* rule that sets the background — a color token surviving a background-color change is a real, recurring bug (button-text-vs-fill within 5% lightness and 0.05 chroma auto-fails; catches literal near-invisible text).
- **category:** color · **layer:** P1 (safety — this is a contrast/accessibility bug, cross-reference A11Y-001)
- **severity:** critical
- **applicability:** universal wherever CSS custom-property theming is used.
- **evidence:** reads as mined from an actual production incident, not derived in the abstract.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (pair every background-lightness rule with its text-token rule; flag mismatches).
- **remediation:** add the paired text-token flip to the same selector.
