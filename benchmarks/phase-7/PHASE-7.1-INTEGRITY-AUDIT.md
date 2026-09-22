# PHASE 7.1 — INTEGRITY AUDIT

Scope: verify whether the Phase 7.1 corrections (commits `845cf5a`, `460ed36`) are
actually wired into the skill's operational architecture. Diagnostic only — no
architecture, rule-catalog, or critique-protocol edits made during this audit.

---

## 1. Executive Summary

**PASS WITH RISKS**

Both Phase 7.1 rule edits (`MOTION-004` scoping, `A11Y-009` addition) are internally
coherent, correctly authored, and introduce no contradictions anywhere in the repo.
Repository structure and git hygiene are clean. The one real gap — `A11Y-009` not
being added to `critique-protocol.md`'s named Level 1 floor list — is genuine, but it
was already identified and disclosed by the Phase 7.1 report itself (§8, Residual
Risks) as explicitly out of scope for that pass. This audit confirms that disclosure
is accurate and quantifies exactly what it means operationally.

---

## 2. A11Y-009 Integration

**Current state:** `accessibility.md` lines 52–61. Internally coherent — the rule
states essential content/navigation, JS-independent baseline visibility, a named
legitimate-exception list (accordions/modals/drawers, decorative reveal, lazy-loaded
media with fallback, trigger-gated UI), a concrete two-path validation procedure
(rendered-capability vs. source-inspection), and a specific remediation. `layer: P5`,
`severity: critical` — matches the existing `A11Y-008` precedent for this
layer/severity combination.

**Level 1 floor status:** NOT included. `critique-protocol.md` line 13 (unmodified by
Phase 7.1, confirmed by `git show 845cf5a` — this file was not in that commit's diff)
still reads: *"the P1 always-on gates from `accessibility.md` (A11Y-001, A11Y-002,
A11Y-003, A11Y-004) — never skipped, regardless of scope."* `A11Y-009` is grouped under
`accessibility.md`'s own `## Always-on` section header alongside A11Y-001–004, but that
is the Rule Catalog's own internal categorization — it is not the same list the
operational Level 1 floor actually enumerates. The critical question the audit brief
flagged is confirmed: **"Always-on" (rule-catalog section) ≠ "Level 1 floor"
(critique-protocol's hardcoded id list).** They currently diverge for exactly one rule.

**Operational reachability:** conditional, not guaranteed.
- `SKILL.md` §7 (T2 tier): `accessibility.md` loads "the specific category is in scope
  for the routed task." `A11Y-009` reaches VALIDATE/Level 1's axis 4 ("craft
  correctness — spot-check against Rule Catalog categories actually in scope") and
  Level 2 (which reads the full loaded file) *only if* accessibility.md is loaded for
  that task.
- `A11Y-001–004` do not depend on that conditional load — the hardcoded id list at
  critique-protocol.md line 13 makes them run "regardless of scope," independent of
  whether accessibility.md was pulled in via T2. `A11Y-009` has no equivalent
  unconditional path.
- `SKILL.md` §7 gives its own counter-example: a "fix border radius" POLISH task loads
  `layout-interaction.md` and *maybe* `accessibility.md` — not guaranteed. A component
  POLISH that touches a JS-gated reveal pattern but isn't framed as an accessibility
  task could plausibly skip loading `accessibility.md` entirely, and therefore skip
  `A11Y-009` along with it (while still running A11Y-001–004 via the hardcoded floor).

**Evidence:** `critique-protocol.md:13` (cat'd in full, unmodified since before Phase
7.1); `SKILL.md:168` and `:170` (T2/T3 loading is conditional-on-content, not
universal); `git show --stat 845cf5a` (confirms `critique-protocol.md` was not touched
by the Phase 7.1 commit).

**Gap, reported, not fixed:** `A11Y-009` should be added to critique-protocol.md
line 13's enumerated list to close this. This exact gap is already named in
`PHASE-7.1-TARGETED-CORRECTIONS.md` §8 as a known residual risk with the correct
proposed fix ("a one-line addition to `critique-protocol.md` line 13"). The audit
confirms that self-assessment is accurate — this is not a new finding, it is
independent verification of a disclosed one.

---

## 3. MOTION-004 / MOTION-007

**Current state:** clean. `motion.md:42–51` — `MOTION-004` is explicitly semantic, not
a property allowlist. It names the actual harm (layout/reflow), lists the restricted
properties by that criterion (`width`/`height`/`margin`/`padding`/`top`/`left`/`right`/
`bottom`, or a framework transform shorthand over a non-composited property), and
states `transform`/`opacity`/`clip-path` as the preferred default for
movement/scale/reveal — not the only legal properties.

- Paint-only properties (`color`, `border-color`, `background-color`) are explicitly
  named as **outside this rule's scope** ("not a MOTION-004 finding"), with the
  reasoning stated (no layout/reflow triggered) — framed as a scope boundary, not a
  disclosed exception weakening the rule. `exceptions: none` remains accurate under
  this framing.
- `MOTION-007` (`motion.md:75–84`) owns `prefers-reduced-motion` exclusively — its
  principle explicitly keeps opacity/color transitions and drops movement/position
  changes under reduced motion. `MOTION-004`'s closing sentence points reduced-motion
  handling for *any* transition, paint-only included, back to `MOTION-007` — no
  competing statement exists anywhere else in the catalog.
- `accessibility.md:35` (`A11Y-003`) cross-references `MOTION-007` as a pointer, not a
  duplicate — consistent.

**Ambiguities found:** none. Read together, `MOTION-004` and `MOTION-007` no longer
contradict — a plain hover color transition is legal under `MOTION-004` (paint-only,
out of scope) and its reduced-motion behavior is governed by `MOTION-007` alone.

**Stale references:** none found. Repo-wide search for `MOTION-004` outside
`motion.md` returns one hit — `style-catalog.md:73`, *"more animation surface area to
keep on compositor-friendly properties (MOTION-004)"* — generic phrasing, still
accurate against the corrected rule text, requires no update. Searched for the old
unconditional-allowlist phrasing pattern ("animate only transform/opacity",
"allowlist") across every rule-catalog file — zero matches outside the corrected
`MOTION-004` entry itself.

**Evidence:** full `motion.md` read (128 lines); grep for `MOTION-004|MOTION_INTENSITY|
MOTION-007` across `design-excellence/**/*.md` (9 files matched, all reviewed, no
contradiction); grep for stale allowlist phrasing (2 matches, both inside the corrected
`MOTION-004` entry describing the new scoped rule, not stale text).

---

## 4. Rule Reference Integrity

- **Broken references:** none. Every rule id referenced anywhere in `SKILL.md` or
  `references/**/*.md` (`COLOR-*`, `CONTENT-*`, `HARDEN-*`, `INTX-*`, `LAYOUT-*`,
  `MOTION-*`, `PERF-*`, `TYPE-*`, `A11Y-*`, `SLOP-*` — 73 unique references collected)
  resolves to an id actually defined by a `###` heading in the Rule Catalog or
  Anti-Slop Registry. Set difference (referenced − defined) is empty.
- **Duplicate IDs:** none. `grep -hoE '^### [A-Z]+-[0-9]+'` across
  `references/rule-catalog/*.md` sorted and checked for duplicates — zero. `A11Y-*`
  checked separately (its digit-embedded prefix doesn't match that regex) — 9 unique
  ids, A11Y-001–009, no duplicates, matches the count `PHASE-7.1-TARGETED-
  CORRECTIONS.md` §7 claims.
- **Stale references:** none found beyond the `MOTION-004` check in §3 above.
- **File references:** every `.md` file named in `SKILL.md` or any reference file
  (`ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md`, all seven rule-catalog files,
  `critique-protocol.md`, `existing-project-safety.md`, `gesture-physics.md`,
  `style-catalog.md`, `visual-references.md`, `anti-slop-registry.md`,
  `PHASE-6.3-RESULTS.md` cited from `layout-interaction.md:91`) resolves to a file that
  actually exists in the repository. No dangling file reference found.
- **Unreachable rules:** none structurally unreachable — every rule-catalog category
  file is named in `SKILL.md` §7's T2 tier and loads conditionally on scope, which is
  the architecture's intended progressive-disclosure design, not a defect. The one
  *practically* under-reachable rule is `A11Y-009` relative to the unconditional Level
  1 floor specifically — covered in §2, not a broader Rule Catalog problem.
- **Minor, pre-existing, out of Phase 7.1's scope:** `LAYOUT-006` does not exist —
  the sequence in `layout-interaction.md` runs `LAYOUT-005` → `LAYOUT-007`. Nothing in
  the repository references `LAYOUT-006`, so this is not a broken reference, only an
  unexplained numbering gap predating this pass. Not introduced by, or related to,
  the `845cf5a`/`460ed36` commits.

**Result:** clean. No broken references, no duplicate ids, no dead file references
introduced by or exposed by Phase 7.1.

---

## 5. Architecture Coherence

- **Routing (§1–§2 of `SKILL.md`):** internally consistent — Scope × Project State ×
  Task Mode table, Hard rule for component POLISH, and the section-scope
  disambiguation all cross-reference each other without contradiction. Untouched by
  Phase 7.1 (confirmed: `SKILL.md` not in either commit's diff).
- **Authority hierarchy (§3):** `A11Y-009` (P5) and `MOTION-004` (P7) both sit at the
  layer their own content actually matches — neither was added to or silently expanded
  the P1 enumerated list (contrast / focus-visible / keyboard operability /
  reduced-motion). This is correct under the Phase 4 correction's discipline that P1
  stays narrow and enumerated. No authority-hierarchy violation introduced.
- **Pipeline (UNDERSTAND→SHIP):** no stage was added, removed, or reordered. Both
  corrections are rule-text-only, consistent with the Phase 7 analysis's Option B
  decision to avoid architectural change.
- **Critique (Level 1 / Level 2):** Level 1's structure is otherwise sound — the
  six-axis rubric, the automatic escalation trigger, and the Level 2 mechanism/honest-
  limitation language are all unchanged and self-consistent. The one point of friction
  is exactly the `A11Y-009` floor-list gap documented in §2 — not a broader coherence
  problem with the critique system itself.
- **Validation:** `SKILL.md`'s VALIDATE stage description ("always — but only the gates
  relevant to what was touched") is generic by design and doesn't enumerate specific
  rule ids anywhere — it relies on whatever was loaded via T2, same caveat as above.
- **Register/Genre, Concept Governance, Visual References, Anti-Slop, Fingerprint,
  Existing-System Safety:** none touched by Phase 7.1; spot-checked for any incidental
  cross-reference to `MOTION-004`/`A11Y-009` (style-catalog.md, layout-interaction.md)
  — all consistent, no stale wording found.

**Result:** coherent. No contradiction found across the pipeline, authority hierarchy,
routing, or critique/validation responsibilities.

---

## 6. Phase 7.1 Documentation Integrity

`PHASE-7.1-TARGETED-CORRECTIONS.md` read in full and checked against the live repo.

**Claims verified accurate:**
- Files touched: `motion.md`, `accessibility.md`, plus the report itself — matches
  `git show --stat 845cf5a` exactly (3 files, 246 insertions, 5 deletions).
- `critique-protocol.md` "inspected, not modified" — confirmed, it is absent from
  `845cf5a`'s diff.
- `SKILL.md` "read in full, inspected, left unmodified" — confirmed absent from both
  commits' diffs.
- Rule-id counts (`accessibility.md` now 9 rules, `motion.md` still 11) — confirmed by
  direct count.
- No duplicate ids, no dead `MOTION-004` references outside the generic
  `style-catalog.md:73` mention — confirmed independently in §3–§4 above.
- The self-reported residual risk ("A11Y-009 is not yet wired into
  critique-protocol.md's named Level 1 floor list... reachable... but not guaranteed to
  be treated as an unconditional Level 1 floor gate") — confirmed accurate by this
  audit's independent inspection in §2.

**Discrepancy found (minor, documentation-only):** §6 ("Non-changes") states the new
rule "is reachable through the existing T2 loading mechanism... which is true for
essentially all BUILD/REDESIGN/POLISH work touching visible UI" — a fairly confident
framing. §8 ("Residual risks") states the more precise and correct position: the rule
is "not guaranteed to be treated as an unconditional Level 1 floor gate." These two
sections of the same document sit at different confidence levels for the same
underlying fact. §8 is the accurate one (confirmed against `SKILL.md` §7's own
"fix border radius" counter-example, which shows accessibility.md loading is not
universal). §6's softer claim is not false, but it reads more reassuring than the
architecture actually guarantees.

**Residual risks (from the document) independently checked:**
- A11Y-009 floor-list gap — confirmed real (§2 above).
- Single-project evidence for the new rule — cannot be verified or falsified by static
  inspection; accurately described as unresolved by the document itself.
- No mechanical/automated check for either corrected rule — confirmed: both
  `MOTION-004` and `A11Y-009` validation fields describe grep/inspection/rendered-check
  procedures, not a single deterministic mechanical check; consistent with other
  manual-validation rules already in the catalog (`A11Y-006`, `MOTION-010`).

**Result:** the document's factual claims about what changed are accurate. Its
"complete" framing in §6 is slightly optimistic relative to §8's own more careful
language — not a false claim, but worth flagging since a reader stopping at §6 would
come away more confident about A11Y-009's reach than the architecture supports.

---

## 7. Repository Structure / Git Hygiene

- **Documentation structure:** clean. `benchmarks/phase-3.5/`, `benchmarks/phase-6.2/`
  through `phase-6.5/`, `benchmarks/phase-7/` all present and correctly scoped;
  `proposals/` holds phase proposal docs; `architecture/` holds `ARCHITECTURE.md` and
  `FORENSIC-EXTRACTION.md`; `design-excellence/` holds only the runtime skill
  (`SKILL.md` + `references/`). Repository root contains no phase/benchmark document —
  confirmed via a full top-level listing.
- **Junction:** `.claude/skills/design-excellence` exists as a symlink/junction
  pointing to `/c/Users/lexsa/Desktop/design-excellence/design-excellence/` — the local
  source, correctly targeted.
- **Ignored paths:** `git check-ignore -v` confirms both
  `.claude/skills/design-excellence` (via `.gitignore:18`) and
  `.claude/settings.local.json` (via `.gitignore:2`) are ignored. `git ls-files` returns
  no tracked paths under `.claude/skills` — the junction carries no tracked content.
- **Source-of-truth status:** confirmed single-sourced. Commit `460ed36` deleted the
  previously double-tracked copy that lived under
  `.claude/skills/design-excellence/...` (1,243 lines removed across 14 files) and
  added the junction-ignore rule to `.gitignore` in the same commit. `design-excellence/`
  is now the only versioned copy of the skill; the junction is local-only and
  untracked, exactly as intended.

**Result:** clean. No hygiene issues found.

---

## 8. Required Corrections

### INTEGRITY-1
- **Severity:** Medium
- **File:** `design-excellence/references/critique-protocol.md`, line 13
- **Exact issue:** Level 1's Accessibility axis enumerates only
  `A11Y-001, A11Y-002, A11Y-003, A11Y-004` as the "never skipped, regardless of scope"
  floor. `A11Y-009` — grouped under `accessibility.md`'s own Always-on section and
  directly motivated by the worst defect found in the Phase 7 benchmark — is absent
  from that list, so it does not share the same unconditional-reach guarantee.
- **Why it matters:** the exact failure class `A11Y-009` targets (JS-gated essential
  content, invisible/inert without JavaScript) is precisely what escaped both Level 1
  self-critique and mechanical VALIDATE in the Phase 7 MOVA benchmark, being caught
  only by a Level 2 reviewer manually tracing the JS chain. Leaving A11Y-009 off the
  hardcoded floor list means that same miss remains structurally possible on any task
  where T2 doesn't happen to load `accessibility.md` — the rule's real-world value is
  highest exactly where its current wiring is weakest.
- **Smallest viable correction:** append `, A11Y-009` to the enumerated id list on
  critique-protocol.md line 13. One clause, no rewording of the surrounding sentence
  required.

### INTEGRITY-2
- **Severity:** Low
- **File:** `benchmarks/phase-7/PHASE-7.1-TARGETED-CORRECTIONS.md`, §6 vs. §8
- **Exact issue:** §6 states A11Y-009 reachability "is true for essentially all
  BUILD/REDESIGN/POLISH work touching visible UI"; §8 more precisely states it is "not
  guaranteed... since that file was out of scope." The two framings of the same fact
  sit at different confidence levels within one document.
- **Why it matters:** a reader relying on §6 alone would overestimate how reliably
  A11Y-009 is checked today. Documentation-precision issue only — no functional impact,
  since §8 already states the accurate position and is the section explicitly
  responsible for residual risk.
- **Smallest viable correction:** none required for Phase 7.1 sign-off; if amended
  later, soften §6's claim to defer to §8 rather than asserting near-universal reach.

---

## 9. Final Verdict

**PASS WITH RISKS**

The two Phase 7.1 rule corrections are well-formed, internally coherent, and introduce
no contradictions, broken references, or architectural drift anywhere in the skill.
Repository structure and git hygiene are clean and match the documented intent exactly.
The single outstanding item — `A11Y-009` not yet added to `critique-protocol.md`'s
named Level 1 floor list — is real, but it was already correctly identified, scoped,
and disclosed as a residual risk by the Phase 7.1 report itself, with the correct fix
already named. This audit independently confirms that disclosure is accurate and finds
no additional integration gaps. Closing INTEGRITY-1 (a one-line addition) would move
this to a clean PASS; it is not a blocker discovered by this audit, but it should be
closed before treating Phase 7.1 as fully wired, and specifically before any future
pass that adds more Rule Catalog content depending on Level 1's floor being complete.
