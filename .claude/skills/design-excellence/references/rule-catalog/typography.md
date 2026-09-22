# Typography — Rule Catalog (T2)

AI-tell-flavored typography patterns (e.g. italic-on-display-type, accented single word in a headline) live in `anti-slop-registry.md` as freshness-governed entries, not here — this file holds structural/procedural typography rules that don't go stale the way "current AI tells" do.

---

### TYPE-001 — Font family count: cap 2, conditional 3rd
- **category:** typography · **layer:** P8 (aesthetic)
- **principle:** default cap of 2 families. A documented 3rd "outlier" face (display/wordmark/pull-quote accent) is allowed only under a usage-slot discipline — capped at ≤2 usage slots; a 3rd use demotes it to "now it's a body font, collapse it."
- **severity:** moderate
- **applicability:** `applicability: {product-led: cap=2 hard; brand-led+editorial: cap=3 with outlier-demotion; hybrid: cap=2 default, 3 by explicit brief signal}`.
- **exceptions:** genuinely maximalist/editorial directions may justify a documented 3rd family — never a 4th.
- **evidence:** resolves a direct cross-source conflict (one source capped at 2 absolutely, another allowed 3 with discipline) — see `FORENSIC-EXTRACTION.md` Conflict Map #2. The discipline (usage-slot demotion) is what makes 3 safe.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (count distinct font-family declarations; check outlier usage-slot count).
- **remediation:** demote or remove the excess family.

### TYPE-002 — Font selection procedure
- **category:** typography · **layer:** P8
- **principle:** write 3 physical-object brand-voice words → list the reflex fonts that come to mind → reject any that are training-data defaults (see anti-slop registry for the current list) → browse real foundries with the voice words in mind, framing the choice as a physical object ("a 1970s terminal manual," "a receipt from a mid-century diner") → cross-check the final pick doesn't trivially match the category stereotype.
- **severity:** minor
- **applicability:** brand-led/editorial work primarily; product-led register may substitute "use the existing system font stack" as a legitimate terminus of this procedure.
- **exceptions:** none — this is a generative procedure, not a constraint to work around.
- **evidence:** a durable *method* survives even as which fonts count as "reflex defaults" changes; more valuable than any specific font list.
- **freshness:** status: permanent (the procedure); the reflex-reject list itself lives in `anti-slop-registry.md` with review dates.
- **validation:** manual.
- **remediation:** n/a — this is generative, not a check.

### TYPE-003 — Line length
- **principle:** under 80 characters by default for running body text; serif body can run slightly longer with more line-height than sans-serif.
- **category:** typography · **layer:** P5 (UX/readability)
- **severity:** moderate
- **applicability:** prose/article/body-copy contexts. Does not apply to dashboards, data tables, or wide UI where content legitimately needs the width.
- **exceptions:** dense/tabular/dashboard content.
- **evidence:** long measure is a well-established readability finding; the hard-number version breaks legitimately for non-prose UI, hence the applicability scope.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (measure computed line length against character count at target viewport).
- **remediation:** constrain the text column width, not the font size.

### TYPE-004 — Size-specific tracking and leading
- **principle:** letter-spacing and line-height are not single fixed values — negative tracking as text grows, positive/near-zero tracking at small sizes; leading tightens as size increases.
- **category:** typography · **layer:** P5
- **severity:** minor
- **applicability:** universal typographic principle, consistent with type-design consensus generally.
- **exceptions:** none.
- **evidence:** a single fixed `letter-spacing`/`line-height` across all sizes is a common generated-CSS tell and a real legibility issue at scale extremes.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** define tracking/leading per type-scale step, not globally.

### TYPE-005 — Register-conditioned scale strategy
- **principle:** product register: fixed rem scale (1.125–1.2 ratio), system fonts legitimate, single-family often correct. Brand register: fluid `clamp()` scale (≥1.25 ratio), more typographic expression licensed.
- **category:** typography · **layer:** P8
- **severity:** minor
- **applicability:** `applicability: {register}` — this rule's whole point is register-conditioning; do not apply the brand-register scale to a product-register interface or vice versa.
- **exceptions:** hybrid register uses judgment scoped between the two.
- **evidence:** most sources don't distinguish product vs. brand typography scale strategy this explicitly; a genuinely useful contrast to preserve.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** n/a.

### TYPE-006 — Responsive display/hero headline integrity
*(Added Phase 6 — closes a gap where no rule checked orphan/widow/awkward rag on display type; `INTX-003` (`layout-interaction.md`) covers clickable text only, `TYPE-003` covers running body prose only.)*
- **category:** typography · **layer:** P5 (UX/readability) · **severity:** moderate
- **principle:** display/hero headlines are checked at each declared responsive breakpoint for orphaned single words, widows, or awkward rag on the final line. Detection only — no single fix is prescribed by default; legitimate remediation strategies include container/measure width adjustment, type-scale or font-size adjustment, explicit line-break placement, copy adjustment, or non-breaking grouping between the last two words where genuinely appropriate. Which strategy applies is a per-case judgment, not a mechanical default.
- **applicability:** any display/hero-level heading, at every declared responsive breakpoint (`SKILL.md` §5 Responsive Notes).
- **exceptions:** none.
- **evidence:** the benchmark that motivated this rule shipped a mobile hero headline with an orphaned word at its breakpoint — a defect no existing rule in this catalog was scoped to catch.
- **freshness:** status: permanent.
- **validation:** mechanical-countable, subject to the capability gating in `SKILL.md` §1 — rendered, Enhanced mode only, using the same "check at required floor widths" technique `INTX-003` already uses; reports `skipped — capability unavailable` when rendering capability isn't available, never silently treated as passed.
- **remediation:** apply whichever strategy above fits the specific case; do not default to one mechanically.
