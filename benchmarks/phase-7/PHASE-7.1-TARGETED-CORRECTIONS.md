# Phase 7.1 — Targeted Rule Corrections

Source: `benchmarks/phase-7/PHASE-7-CROSS-PROJECT-ANALYSIS.md` §7, §10D, §11. This is a
targeted correction pass on two concrete, textually-demonstrated rule-catalog gaps —
not a redesign, not a new stage, not a new dial, not a new Anti-Slop rule.

---

## 1. Scope

Two corrections, both recommended by the Phase 7 cross-project analysis (§7, Option B):

- **Correction A** — `MOTION-004` read as contradicting `MOTION-007` on paint-only
  color/border-color/background-color transitions. Three independent benchmark
  sessions (Tests 01, 03, 06R) hit this and resolved it identically, unprompted —
  strong convergent evidence of a textual gap, not a misreading.
- **Correction B** — no rule in the catalog named "essential content must not depend
  on JavaScript to become visible." This gap let the single most severe defect in the
  whole benchmark (Test 01/MOVA: hero content and the mobile nav toggle both
  invisible/inert without JS, no fallback) pass Level 1 critique and mechanical
  VALIDATE; it was caught only by a Level 2 reviewer manually tracing the JS chain.

Both are rule-text fixes inside the existing architecture, per the analysis's Option B
decision (§11): the architecture itself produced no failures across six domains, so a
structural change would be unjustified overfitting to one benchmark.

---

## 2. Pre-change findings

**MOTION-004 (before):** stated an unconditional allowlist — "animate only `transform`
and `opacity`; `clip-path` is a sanctioned fourth" — framing every other property as a
performance finding, full stop. `MOTION-007` separately presupposes color/opacity
transitions are legitimate under `prefers-reduced-motion`. Read alone, MOTION-004 gave
no textual room for a plain hover `color`/`border-color`/`background-color` transition,
which is not layout-affecting and was never the harm the rule's own evidence field
names ("layout thrash and jank"). Three sessions independently judged such transitions
out of scope and kept them as a disclosed exception — correct in outcome, but only
recoverable by inference, not by reading the rule itself.

**Progressive enhancement (before):** confirmed absent. Searched the full rule catalog
(`motion.md`, `accessibility.md`, `performance-hardening.md`, `layout-interaction.md`,
`content-copy.md`, `color.md`, `typography.md`) and `SKILL.md` for progressive
enhancement, JS-independent visibility, `opacity: 0` defaults, JS-only reveal, or
`<noscript>` handling — zero matches. `accessibility.md`'s P1 always-on list
(A11Y-001–004) covers contrast, keyboard operability, reduced motion, and icon roles —
none of which name content existing/being visible at all as a precondition. This is
exactly the gap the Phase 7 analysis identifies (§7, §10D): a real, addressable rule
absence, not a misapplication of an existing rule.

---

## 3. Changes made

Two files edited, both inside `design-excellence/references/rule-catalog/` (also
reachable at the symlinked `.claude/skills/design-excellence/...` path — same file):

- `motion.md` — `MOTION-004` rewritten (principle, evidence, validation, remediation
  fields; title changed to match the corrected scope).
- `accessibility.md` — new rule `A11Y-009` added to the Always-on section, after
  `A11Y-004`, before the Conditional section header.

No other file touched. `SKILL.md` inspected and left unmodified (§4 below).

---

## 4. MOTION-004 / MOTION-007

**Before:** "animate only `transform`/`opacity`/`clip-path`; anything else is a
performance finding." No scoping to *why* — read alone, a plain color hover transition
was technically a violation, contradicted only by inference from MOTION-007.

**After:** the restriction is explicitly scoped to properties that trigger
layout/reflow (`width`/`height`/`margin`/`padding`/`top`/`left`/`right`/`bottom`, or a
framework's `x`/`y`/`scale` shorthand over a non-composited property) — that is named
as the specific harm the rule exists to prevent. `transform`/`opacity`/`clip-path`
remain the preferred, stated-first choice for movement/scale/reveal. Paint-only
properties (`color`/`border-color`/`background-color`) are named explicitly as outside
this rule's scope, not as an exception weakening it — they don't cause layout thrash,
so they were never the harm MOTION-004 targets. The rule closes by pointing
`prefers-reduced-motion` handling back to MOTION-007 for any transition, paint-only
included, so the two rules no longer read as contradictory when either is read alone.
`exceptions: none` is unchanged and still true: the carve-out is a scope boundary, not
an exception to the restriction. MOTION-001/002/003 (frequency, purpose, decorative
restraint) are referenced explicitly so the carve-out cannot be misread as blanket
permission for gratuitous color animation.

---

## 5. Progressive enhancement

**Before:** no rule existed. The MOVA defect was catchable only by a Level 2 reviewer's
manual JS-trace, with no mechanical or self-critique-prompt path to it.

**After:** `A11Y-009` — "Essential content must not depend on JavaScript to exist or
become visible" — added to `accessibility.md`'s Always-on section.

- **Core principle:** essential content and essential interaction (primary content,
  navigation, its own toggle) must be visible/operable in HTML+CSS alone before any JS
  runs; JS may enhance, never gate existence. States the preferred order (HTML visible
  → CSS presentation → JS enhancement) against the pattern that failed in MOVA (HTML →
  hidden CSS state → JS required to reveal).
- **Named failure patterns:** `opacity: 0` defaults, `visibility: hidden` defaults,
  off-screen positioning, JS-only reveal classes — the exact shape of the MOVA defect.
- **Explicit non-scope, so it can't overreach:** closed accordions/modals/drawers with
  an accessible collapsed state, decorative/non-essential reveal choreography,
  lazy-loaded media with a fallback, and interaction-only UI gated behind its own
  trigger are all named as legitimate and outside this rule. Scroll-reveal motion on
  non-essential content is explicitly left to `MOTION-003`/`MOTION_INTENSITY`, not this
  rule — the failure targeted is permanent inaccessibility without JS, not the
  existence of a reveal animation.
- **Validation:** concrete two-path procedure — rendered capability available →
  disable/simulate no-JS on critical pages and verify essential content/nav still
  works; rendered capability unavailable → inspect source for the named default-hidden
  shapes with no CSS-visible fallback and no `<noscript>`/equivalent. No external tool
  required, per instructions.
- **Layer/severity:** `layer: P5`, `severity: critical`. Deliberately **not** added to
  the P1 enumerated list in `SKILL.md` §3 (contrast / focus-visible / keyboard
  operability / reduced-motion) — that list is narrow and enumerated by design (Phase 4
  correction), and this rule doesn't literally match any of the four items. `severity:
  critical` carries the real-world stakes (this was the worst defect in the benchmark)
  without silently broadening P1's override authority. This mirrors the existing
  precedent `A11Y-008` (Never disable zoom) already sets: P5 layer, critical severity.

---

## 6. Non-changes

Explicitly confirmed **not** touched in this pass:

- Architecture / pipeline stages / routing — untouched.
- Concept Governance (three-state model, LAYOUT-009) — untouched.
- Visual References (LAYOUT-010, `visual-references.md`) — untouched.
- Anti-Slop registry — no new rule added, no existing entry modified.
- DESIGN_VARIANCE architecture — untouched (its Medium-band operationalization gap
  from §7 of the analysis is explicitly out of scope for this pass, per instructions).
- Register / Genre — untouched.
- Reicon, Kinetics, SmoothUI — not integrated, not referenced.
- `SKILL.md` — read in full, inspected for stale references to `MOTION-004`'s old
  wording or to any `A11Y-00x` id; none found (`SKILL.md` never restates rule text
  inline, only ids by cross-reference, and it references no accessibility/motion rule
  ids directly). No factual inconsistency was introduced and the new rule is reachable
  through the existing T2 loading mechanism (§7 of `SKILL.md`: `accessibility.md` loads
  whenever the accessibility category is in scope, which is true for essentially all
  BUILD/REDESIGN/POLISH work touching visible UI). Left unmodified.
- `critique-protocol.md` — **inspected, not modified** (out of scope per the hard
  constraints). Its Level 1 floor list at line 13 enumerates `accessibility.md`'s
  always-on gates by id: "A11Y-001, A11Y-002, A11Y-003, A11Y-004." The new `A11Y-009`
  is not added to that named list, since editing that file is outside this pass's
  hard-constrained file set. See Residual Risks (§8).

---

## 7. Validation

**Structural:**
- Unique rule IDs: `grep -hoE '^### [A-Z]+-[0-9]+' *.md | sort | uniq -d` in
  `rule-catalog/` returns no output — no duplicates. `accessibility.md` now has 9
  rules (A11Y-001–009, was 8); `motion.md` still has 11 (MOTION-001–011, content of
  MOTION-004 changed, count unchanged).
- No dead references: searched the full repo for `MOTION-004` outside `motion.md` —
  one hit (`style-catalog.md:73`, "compositor-friendly properties (MOTION-004)"),
  generic phrasing, still accurate against the corrected text. Searched for `A11Y-009`
  — only the new definition itself, as expected for a brand-new id with no consumers
  yet.
- No unnecessary new files — only this report was created, as instructed.
- P-level authority coherence: `A11Y-009` follows the same layer/severity separation
  the file's Phase 4 correction already established (P5 layer with critical severity,
  matching `A11Y-008`'s precedent) rather than inventing a new severity scale or
  quietly expanding the enumerated P1 list.
- Reachability: confirmed via `SKILL.md` §7's existing T2 gate (category-based
  loading) — no new loading path was needed or added.

**Content:**
- MOTION-004 read alone now states: what harm it prevents (layout/reflow), which
  properties are restricted (the layout-affecting list), that paint-only
  color/border/background transitions are out of scope (not a violation), that
  transform/opacity/clip-path remain preferred for movement/reveal, and that
  MOTION-007 owns `prefers-reduced-motion` handling for any transition.
- A11Y-009 read alone now states: what "essential" means (primary content, nav, nav's
  toggle), what failure looks like (default-hidden + JS-only reveal, named CSS
  patterns), what JS-disabled validation should do (two-path procedure), what
  legitimate exceptions exist (accordions/modals/lazy-media/trigger-gated UI, motion
  choreography on non-essential content), and why it's a correctness/progressive-
  enhancement rule rather than a motion ban (explicit cross-reference to
  MOTION-003/MOTION_INTENSITY for the non-essential case).

**Diff:**
- `git diff --check` — no errors (only pre-existing LF/CRLF line-ending warnings
  unrelated to content).
- `git diff --stat` — 4 paths changed (2 real files, each also visible at its
  `.claude/skills/design-excellence/...` symlink target), 32 insertions, 10 deletions.
  Reviewed the full `git diff` — changes are confined to the two intended rule bodies;
  no unrelated file touched.

**Remaining ambiguity:** none identified in the two corrected rules themselves. One
adjacent gap named by the source analysis (DESIGN_VARIANCE's Medium-band spacing/color
thresholds, `LAYOUT-007`/`COLOR-001`) remains genuinely unresolved — correctly, since
it was explicitly out of scope for this pass.

---

## 8. Residual risks

- **A11Y-009 is not yet wired into `critique-protocol.md`'s named Level 1 floor list**
  (currently "A11Y-001, A11Y-002, A11Y-003, A11Y-004"). The rule is still reachable —
  it loads with the rest of `accessibility.md` under the existing T2 mechanism, and
  VALIDATE/Level 2 review both read the full loaded file, not just that named subset —
  but it is not guaranteed to be treated as an unconditional Level 1 floor gate the way
  A11Y-001–004 explicitly are, since that file was out of scope for this pass. In the
  original MOVA case this defect was caught by Level 2, not Level 1 — so this residual
  risk reflects the same coverage shape the benchmark already showed, not a new one
  introduced here. Closing it cleanly requires a one-line addition to
  `critique-protocol.md` line 13 in a future pass.
- **Single-project evidence.** The progressive-enhancement rule is motivated by one
  concrete defect (Test 01/MOVA), though its causal shape (opacity-0 default + JS-only
  reveal) is named in the source analysis as a plausible recurring pattern given how
  this skill's brand-led builds use scroll/load-in reveal motion. Not yet
  cross-validated by a second occurrence.
- **No mechanical/automated check.** Both corrected rules remain
  self-critique-prompt/manual-inspection or rendered-verification procedures, not a
  fully mechanical grep-and-flag check — consistent with the rest of the catalog's
  existing validation styles for rules of this shape (e.g. `A11Y-006`, `MOTION-010`
  are also manual), not a new gap introduced by this pass.

---

## 9. Decision

**PASS**
