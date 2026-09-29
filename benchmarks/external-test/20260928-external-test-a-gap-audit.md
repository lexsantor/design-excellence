# External Test A Gap Audit

- **Milestone:** External Test Analysis & Behavioral Gap Audit (analysis only)
- **Authorization:** "adelante siguiente paso" (human, 2026-09-28), recorded in `STATE.md`
- **Date:** 2026-09-28
- **Skill state audited:** repository `HEAD` `9c719a7` ("fix: harden skill for first external test"), the same text the test ran against (installed copy made from it in the Pre-Test Hardening milestone)
- **Outcome:** COMPLETED. No Design Excellence file was changed. Every proposed correction below is a recommendation that needs its own human authorization.

---

## 1. Scope and evidence

### 1.1 Primary evidence (external project, read-only)

`<external-test-a-project>`, inspected without modification:

| Evidence | How used |
|---|---|
| `TEST-RESULTS.md` (304 lines, read in full) | The test agent's own run record. Treated as a claim to verify, not as fact |
| `.design/context.md` (113 lines, read in full) | The committed direction, Known Exceptions, Rejected Directions, Fingerprint History |
| `test-evidence/01-desktop-1440-full.png`, `02-mobile-375-full.png`, `07-desktop-1440-hero-viewport.png` | Viewed directly; regions of 01 and 02 were cropped into the session scratchpad (outside both repositories) for legibility |
| `src/styles/global.css`, `src/components/*.astro` | `grep` only, to locate the tape treatment (`.tape`, `.tape-torn`, `.tape-strip`) |

**Missing primary evidence.** The verbatim test brief is not on disk. `TEST-RESULTS.md` §1 gives only a summary ("no external visual references, Figma or the licensed library (a reference-free baseline)"). The Level 2 subagent's brief and raw output are also not preserved; only the test agent's summary of them is (§21). Findings that depend on exact wording are qualified accordingly.

### 1.2 Design Excellence sources (read in full at `9c719a7`)

`design-excellence/SKILL.md` (209 lines); `references/critique-protocol.md`, `anti-slop-registry.md`, `style-catalog.md`, `visual-references.md`, `principle-pool.md`, `existing-project-safety.md`; rule catalog `layout-interaction.md`, `typography.md`, `color.md`, `accessibility.md`, `motion.md`, `content-copy.md`, `performance-hardening.md`; `loop.md`; `STATE.md`; `benchmarks/pre-test/PRE-TEST-HARDENING-RESULTS.md`; the PT-20, PT-21, PT-35 and PT-52 rows of `benchmarks/audit/COMPREHENSIVE-PRE-TEST-SKILL-READINESS-AUDIT-RESULTS.md`.

### 1.3 Method and limits

- Every observation in `TEST-RESULTS.md` §20 to §27 was traced to the governing skill text, then to the rendered evidence where the claim is visual.
- No site was rendered, rebuilt or re-tested. Visual claims rest on the seven final-build screenshots.
- The audit does not score the site. Visual observations are recorded only to reconcile the independent critique with the evidence.
- n = 1. One external run cannot establish frequency. Where a finding rests on one run, it says so.

### 1.4 Independent review (`loop.md` §8)

One fresh, read-only, blind reviewer received the evidence paths, the skill paths and the seven questions, without this audit's verdicts. Its dispositions and the reconciliation are in §5.4.

---

## 2. External test summary

| Item | Observed |
|---|---|
| Routing | "page-scope BUILD on a genuinely-empty project (full pipeline minus AUDIT-stage)"; correct per `SKILL.md` §2 l.70 |
| Register / Genre / Dials | brand-led, editorial, variance 6, motion 3, density 4 |
| Concept detection | HYPOTHESIS (an ordinary meaning of the business name); LAYOUT-009 correctly not activated |
| Direction | committed "Canvas, tape and ink"; rejected "Round clock" logged with 4 distinguishing dimensions and a style-catalog cross-check |
| T3 references | `anti-slop-registry.md`, `style-catalog.md` loaded; `visual-references.md` and `principle-pool.md` deliberately not used (P2 reading) |
| Stack | Astro 7.3.5, plain CSS; first framework run (PT-26 path) |
| Capability | Enhanced (Playwright/Chromium) |
| Level 1 | 3 / 4 / 3 / 4 / 4 / 5 |
| Level 2 | fresh `lexia-design:visual-critic`, no Level 1 scores given: 3 / 4 / **2** / 4 / 4 / 5 |
| REFINE | 7 changes; rendered gates re-run; Level 2 not re-run |
| HARDEN | partial |
| Ship status | "shippable as a front end, with placeholders" |
| Safety | no fabricated facts found in the screenshots; placeholders labelled ("To be confirmed by the business") |

Behaviour that worked as specified and is not re-examined below: routing and the classification line, DEFINE concept three-state outcome, the HYPOTHESIS literal-motif ban (no kanji, enso or brush motif), LAYOUT-008 imagery decision (no stock imagery, fabrication risk named), CONTENT-003 (no invented timetable, prices, coaches), the Rejected Directions distinctness log, SLOP-011 Known Exception with a subject-specific rationale, capability honesty in reporting, INTX-004 on mobile (primary full-width, secondary intrinsic, visible in `02`), A11Y-012 applied after Level 2 flagged the overlay, and no writes outside the test folder.

---

## 3. Finding matrix

| ID | Finding | Disposition | Priority |
|---|---|---|---|
| A1 | "Reference-free baseline" in the test brief did not say whether it covered the skill's internal T3 pools | TEST-PROMPT AMBIGUITY | MUST INVESTIGATE NEXT (cheap; affects the next test) |
| A2 | The skill does not say whether an instruction excluding "external references" reaches `visual-references.md` / `principle-pool.md`, whose own headers describe their content as externally observed | SPECIFICATION AMBIGUITY | SHOULD INVESTIGATE |
| B1 | Level 1 axis 3 produced a numeric score (3) from a vacuous first-entry fingerprint comparison | SPECIFICATION AMBIGUITY | MUST INVESTIGATE NEXT |
| B2 | The Level 1 vs Level 2 "Distinctiveness" disagreement compared two different definitions of axis 3 | SPECIFICATION AMBIGUITY | MUST INVESTIGATE NEXT (with B1) |
| C1 | No check verifies that a committed DIRECT direction's declared distinguishing dimensions reach the rendered output | CONFIRMED GAP | MUST INVESTIGATE NEXT |
| C2 | LAYOUT-009 not applied to "Canvas, tape and ink" | EXPECTED BEHAVIOR | none |
| D1 | Whether CRITIQUE (and so Level 2) re-runs after REFINE is not specified | SPECIFICATION AMBIGUITY | SHOULD INVESTIGATE |
| E1 | HARDEN ran partially; HARDEN's trigger and HARDEN-001's per-item applicability are unspecified | SPECIFICATION AMBIGUITY | DEFER |
| E2 | PERF-001 rendered CWV not measured although a browser was available, with no reason given | DEFERRED INVESTIGATION | DEFER (watch) |
| E3 | Screen reader, cross-browser and `astro check` not run | ACCEPTABLE / NOT A GAP | none |
| E4 | Keyboard walk with a visual check at every stop not completed | ACCEPTABLE / NOT A GAP | none |
| F1 | Level 2 activated on "production-quality" + "brand credibility" | SPECIFICATION AMBIGUITY (confirms PT-21 in practice) | SHOULD INVESTIGATE |
| G1 | INTX-003 and TYPE-006 heuristic false positives | EXPECTED BEHAVIOR | DEFER |
| H1 | Category-convention pressure when P2 fixes the palette to the category default | DEFERRED INVESTIGATION | SHOULD INVESTIGATE (as part of the C1 benchmark) |
| H2 | A11Y-012 applicability does not name a disclosure panel that overlays content | SPECIFICATION AMBIGUITY | SHOULD INVESTIGATE |
| H3 | DIRECT candidates were logged, not shown to the user, before commit | ACCEPTABLE / NOT A GAP | none |
| H4 | `accessibility.md` read through a condensed extraction | EVIDENCE INSUFFICIENT | DEFER |
| H5 | The external test left no record in this repository (no report, `STATE.md` not advanced, verbatim brief not preserved) | TEST-PROMPT AMBIGUITY (test-protocol instruction) | MUST INVESTIGATE NEXT (next test's setup) |

---

## 4. Detailed findings A-G

### A. T3 internal references vs a reference-free test

**What happened.** `TEST-RESULTS.md` §10 and `context.md` l.94: the agent read the user's "no external visual references, Figma or the licensed library (a reference-free baseline)" as P2 covering `visual-references.md` and `principle-pool.md` too. Their headers and REF-001 were read incidentally; no entry informed either candidate. The choice was disclosed in both files.

**Governing text.**
- `SKILL.md` §7 l.178 to l.179: both files load at "DIRECT/DESIGN stage for a new visual system **only**". This run met that trigger.
- `SKILL.md` §3 l.87: P2 "wins over P3–P8 unconditionally". LAYOUT-010 is P6.
- `principle-pool.md` l.13: "nothing outside this repository is read at runtime"; the pool is skill-internal data.
- `visual-references.md` l.3: the pool gives EXPLORE "a small set of **externally-observed** design possibilities"; `principle-pool.md` l.3: principles "curated **outside this repository** from observed production work".

**Analysis.**
- Under current P0 to P8 authority the agent's behaviour is valid *if* the instruction covered the pools. P2 outranks LAYOUT-010, and LAYOUT-010 itself says "considered, judged unnecessary" and "no compatible entry" are valid outcomes (`layout-interaction.md` l.93 to l.94). No P1 item depends on the pools. So nothing was violated.
- Whether the instruction covered them is the open question, and it has two sources:
  - **A1, the prompt.** "Reference-free baseline" is broader than "no external visual references". A baseline that is free of *acquired* references and a baseline free of *any* reference input are both natural readings. The prompt's list (Figma, the licensed library) names acquisition channels, which points to the first reading; the word "reference-free" points to the second. The agent took the second, stricter reading, which is the safe side of P2.
  - **A2, the skill.** The skill has no statement that its T3 pools are governed skill knowledge (like the anti-slop registry) rather than "external references", and the pools' own headers call their content externally observed. A reader who wants to honour a "no external references" instruction therefore has textual support for excluding them.
- A1 is resolved in the next test prompt without any skill change. A2 is a wording question only; it does not justify overriding P2 to force T3 use.

**Rule that should govern the distinction (proposal, not implemented).** An explicit instruction excluding external or third-party visual references bounds *runtime acquisition*: fetching or consulting sources outside the skill (Figma, the licensed library, the web, the external reference catalog, other skills' libraries). It does not by itself exclude the skill's governed T3 pools, which are part of the skill's own runtime knowledge and are never read from outside the repository. An instruction that names those pools, or asks for a run without any reference input, excludes them under P2. When the wording allows both, follow the instruction's stated purpose (here a "baseline", which supports excluding the pools, as the agent did) and state the reading in one line after the Design Read, the same way Register/Genre inference is declared (`SKILL.md` §4 l.119). The purpose clause is adopted from the independent review.

**What the omission cost (bounded).** Screening the pools against this run's stored fields (brand-led, editorial, variance Medium, motion Low, no real imagery, no inspectable items):
- plausibly compatible: REF-001, REF-003 (only if the three programs are treated as a closed set), REF-004, REF-009 (bounded summary surfaces only), PRN-0001;
- excluded by their own fields: REF-002 and REF-006 (motion Low), REF-005 (no real process imagery; fabrication risk), REF-007 and REF-008 (register), PRN-0003 (no real items; placeholder values are in its `do_not_apply_to`).

So the pools would not have been empty for this brief. Whether any entry would have changed the Level 2 outcome is **not knowable** from this run (§10).

**Disposition.** A1 TEST-PROMPT AMBIGUITY. A2 SPECIFICATION AMBIGUITY.

- A1 corrected test instruction: "Do not acquire or consult external visual references (Figma, the licensed library, web, reference catalogs, other skills). The skill's own internal reference pools may be used as the skill specifies." For a deliberate no-pool baseline, say so explicitly: "Also do not use `visual-references.md` or `principle-pool.md`."
- A2 wording clarification (for a later milestone): one sentence at `SKILL.md` §7 T3 (or §3 "P2 and pipeline extent") stating the rule above.

### B. First-project Distinctiveness

**What happened.**
- Level 1 axis 3 = 3, noted as "the 2-of-5 check is trivially satisfied because there is nothing to compare against" (`TEST-RESULTS.md` §20; `context.md` l.102).
- Level 2 axis 3 = 2, based on perceived identity close to the combat-sports category default (§21).
- The test agent itself concluded "the two scores measure different things" (§21, §27).

**Governing text.**
- `critique-protocol.md` l.11: "**Distinctiveness** — fingerprint check (`SKILL.md` §6), where in scope."
- `SKILL.md` §6 l.161: difference on at least 2 of 5 dimensions "against each of the last 5 recorded entries in the same project"; l.163: per-project only.
- `critique-protocol.md` l.9: axis 1 **Genericness** asks "would this be produced for any similar brief" and runs the SLOP-011 gestalt check. This is where category-level and model-default genericness is judged.
- `critique-protocol.md` l.7: an axis that "cannot be evaluated honestly in this run" is recorded `not assessable: <reason>`; the listed examples (nothing built, screenshot only, capability unavailable) do not include "no prior entry".
- Level 2 uses "the same six axes as Level 1" (l.31) but the protocol does not require the axis definitions to be passed to the reviewer.

**Analysis.**
- The architecture does **not** conflate the two concepts in its definitions: category/brief-level genericness is axis 1, intra-project divergence is axis 3. The conflation happens in two places:
  1. **B1, scoring a vacuous comparison.** With zero prior entries the 2-of-5 test has no comparison set. It cannot pass or fail, yet the run recorded a number (3). That number carries no information and entered Fingerprint History looking like a mid-range judgement. This is the same class of problem the Pre-Test Hardening milestone fixed for capability (PT-06): a check that cannot be evaluated honestly must not produce a score.
  2. **B2, the label "Distinctiveness".** The Level 2 reviewer (a lexia-design critic with its own distinctiveness notion) evidently scored perceived identity on axis 3. Whether it received the DE axis definitions is not recorded (§10). Either way the "disagreement" compared a fingerprint check with a perceptual judgement.
- The decisive observation: **on axis 1, the axis that actually measures category genericness, Level 1 and Level 2 agreed (3 and 3).** The only disagreement is on the axis whose definition differs. What looks like a perception conflict is mostly a definitional one.
- The first entry should therefore be treated differently only on axis 3, and only by using the existing `not assessable` status. No new score, tier or dimension is needed, and the fingerprint system itself (5 dimensions, 2-of-5, redirect-not-refusal, per-project) is untouched.

**B1: SPECIFICATION AMBIGUITY** (downgraded from CONFIRMED GAP after independent review, §5.4).
- **Evidence:** `TEST-RESULTS.md` §20 row 3; `context.md` l.100 to l.102; `critique-protocol.md` l.7, l.11; `SKILL.md` §6 l.161.
- **Current behaviour:** a first-generation run scores axis 3 numerically from an empty comparison.
- **Expected behaviour:** axis 3 is `not assessable: no prior Fingerprint History entry` on the first generation in a project; category-level distinctiveness is judged, as now, under axis 1.
- **Why it is ambiguous rather than missing:** l.7's general clause ("cannot be evaluated honestly in this run") arguably already covers an empty comparison set, and axis 3 is qualified "where in scope". But the clause's examples are all run-level causes (nothing built, screenshot only, capability unavailable), and axis 3 has no first-entry clause, so an agent can read an empty comparison as "trivially satisfied", as this one did. Interpretation 1: vacuous means satisfied (the test followed this). Interpretation 2: vacuous means not assessable (l.7's intent).
- **Affected file:** `references/critique-protocol.md` (axis 3 line, and possibly the l.7 examples).
- **Smallest wording clarification:** one clause on axis 3: "On the first recorded generation in a project there is nothing to compare against: record `not assessable: first Fingerprint History entry`." Fingerprint History still records the entry (it is the baseline for later checks).
- **Regression risk:** low. `not assessable` does not count toward the automatic escalation trigger (l.7), and a first generation cannot have "two consecutive revision passes" on axis 3 anyway. Watch that the change is not read as skipping the fingerprint *record*.
- **Later benchmark:** not strictly needed (text-verifiable); covered cheaply by BM-B in §12.

**B2: SPECIFICATION AMBIGUITY.**
- **Unclear semantics:** axis 3 is named "Distinctiveness" but defined as a fingerprint check; Level 2 receives "the same six axes" without a requirement to carry the definitions.
- **Interpretation 1:** axis 3 means intra-project divergence (the text). **Interpretation 2:** axis 3 means perceived distinctiveness of the identity (the ordinary meaning, and what an external critic applies).
- **The test followed:** interpretation 1 at Level 1, interpretation 2 at Level 2.
- **Wording clarification only:** in Level 2 step 1 (l.31), require the brief to carry each axis's one-line definition from Level 1, so the two levels score the same question. Optionally note on axis 3 that perceived category distinctiveness belongs to axis 1.

### C. Direction concept carry-through

**What happened.**
- DIRECT committed "Canvas, tape and ink" and distinguished it from the rejected "Round clock" on color, **materiality** ("flat ink and tape" vs "glow/texture"), interaction and composition (`context.md` l.92).
- Level 2 (major): the concept "stayed in the document and never reached the render" (§21).
- REFINE added a torn end to the hero tape bar and two black gaffer-tape strips holding the booking form (§23; `context.md` l.39; `Hero.astro` l.22, `Booking.astro` l.40 to l.41).

**Four things that must not be conflated.**

| Mechanism | Governs | Applied here? |
|---|---|---|
| User-supplied concept → structure (LAYOUT-009) | a DETECTED / EVIDENCED concept, translated onto an organizing surface during EXPLORE | No, correctly: DEFINE recorded HYPOTHESIS (`layout-interaction.md` l.76 ff., applicability) |
| Direction selected in DIRECT/EXPLORE | the committed candidate and its distinguishing dimensions (§5 l.155) | Yes: logged in Rejected Directions |
| Visual signature generated in DESIGN | tokens, type, color, motion tier (Visual System) | Yes |
| Ordinary aesthetic decisions | P8 | Yes |

"Canvas, tape and ink" is a *direction*, not a brief concept. Its metaphorical wording does not activate LAYOUT-009, and the audit does not propose that it should (**C2: EXPECTED BEHAVIOR**).

**Is there a carry-through mechanism today?** No explicit one:
- §5 l.155 checks that the committed and rejected candidates differ on at least 2 of 6 dimensions, **on paper, at DIRECT**. Nothing later checks that the committed candidate's claimed dimensions appear in the built output.
- The fingerprint (§6 l.159) records macrostructure, typography pairing, color-anchor, density and motion tier. Materiality, the dimension this direction was mainly distinguished on, is explicitly outside the check ("worth noting informally").
- Level 1 axis 1's structural test (`critique-protocol.md` l.9) runs only for DETECTED / EVIDENCED.
- Level 2 is the only mechanism that compares the render with the declared direction, and it is stakes-gated. In a run without a Level 2 trigger, this gap would have shipped unnoticed.

**Visual check of the claim (evidence only, no score).**
- Before REFINE: no pre-REFINE screenshots exist, so Level 2's original observation cannot be re-verified (§10).
- After REFINE, in the final screenshots: the tape material appears in the hero divider (a torn end a few pixels long at the right edge, `07`) and in the booking section (two angled black strips on the form card, the most visible instance, `d_book` crop of `01`). Values and Approach use plain tape-thickness red rules. The first viewport (`07`) is carried by condensed heavy uppercase display type in black and red on a pale ground; the tape treatment does not change that first read. At 375 px (`02`) the form card is visible, but whether the strips render could not be confirmed from the capture.
- So the direction now has concrete carriers, but they are localized to two places, and the test agent's own §24 states the identity risk remains and is unverified. The independent reviewer (§5.4) read the same screenshots the same way: the tape accents are local, not a page-wide carrier, and the first-read identity is unchanged. Two consistent reads support Level 2's residual concern. Neither is the independent re-score the protocol would call Level 2, so the post-REFINE status stays formally unverified (§10).

**C1: CONFIRMED GAP (narrow; n = 1 behaviourally, absence verified in text).**
- **Evidence:** `context.md` l.35 to l.39, l.92; `TEST-RESULTS.md` §21, §23, §24; `SKILL.md` §5 l.155, §6 l.159; `critique-protocol.md` l.9.
- **Current behaviour:** the committed direction's distinguishing dimensions are asserted at DIRECT and never verified against the render unless Level 2 runs.
- **Expected behaviour:** at CRITIQUE, the dimensions on which the committed direction was distinguished from its rejected candidates are checked against the rendered output.
- **Why the architecture fails:** every existing distinctiveness mechanism either compares plans (§5), compares against the project's own past (§6), compares against named model clusters (SLOP-011), or is gated on DETECTED (structural test). None compares the render with the committed direction.
- **Affected file:** `references/critique-protocol.md`, Level 1 axis 1.
- **Smallest correction (no new rule, no new stage):** one sentence in axis 1, parallel to the existing structural test: "For page/multi-page-site BUILD/REDESIGN with a committed DIRECT direction, name, for each dimension it was distinguished on in Rejected Directions (§5), the rendered element that carries it (a carrier surface in `layout-interaction.md` LAYOUT-009's list); a dimension with no rendered carrier is a finding for REFINE." Naming the carrier is the independent reviewer's wording, adopted because it is checkable. It is not an automatic fail of the axis.
- **Regression risk:** medium-low. (1) It must not be read as LAYOUT-009 (organizing surfaces, mandatory translation). It reuses only LAYOUT-009's carrier vocabulary. (2) It must not push literal motifs: this run's HYPOTHESIS literal-motif ban (`SKILL.md` l.42) still governs anything derived from the hypothesis. (3) It could encourage decorative "proof" of a direction (tape stickers added to pass a check). The benchmark must watch for that.
- **Later benchmark:** yes, BM-C (§12), before any wording is authorized.

**Is a new rule needed?** No. The evidence supports one diagnostic question inside an existing axis. A new rule-catalog entry would duplicate the §5 dimension list and LAYOUT-009's carrier list.

### D. Level 2 → REFINE → Level 2

**What happened.** Level 2 raised four major findings; REFINE addressed all four; VALIDATE re-ran; CRITIQUE (Level 1 and Level 2) did not re-run. The report states the distinctiveness improvement is "unverified" (§23, §24, §26.4).

**Governing text.**
- `SKILL.md` §1 l.28: REFINE "only if VALIDATE/CRITIQUE produced findings". No stage says what runs after REFINE.
- `critique-protocol.md` l.16: the automatic trigger needs "two consecutive revision passes", which presupposes re-scoring after revision.
- l.21: the stakes trigger is a property of the work, so it still holds after REFINE.
- Precedent: PT-20 ("no revision loop or cap") and the Pre-Test Hardening report's "Not done: a REFINE loop definition (PT-20)".

**Two plausible interpretations.**
1. CRITIQUE runs once. After REFINE, VALIDATE re-runs on the touched areas and the run ships. (The test followed this.)
2. REFINE returns to VALIDATE → CRITIQUE. Level 1 re-scores; since the stakes trigger still holds, Level 2 re-runs in full. This doubles Level 2 cost on every triggered run.

Neither is stated; interpretation 2 is disproportionate, interpretation 1 leaves the one independently found major issue verified only by the agent whose blind spot produced it. That is exactly the case the protocol's own rationale (l.16: "a second, differently-biased reviewer earns its cost") is about.

**Disposition: SPECIFICATION AMBIGUITY** (not a confirmed gap: the run disclosed the unverified state honestly, and no harm was observed beyond that). The minimum stakes-gated condition, as a proposal:

After any REFINE, Level 1 re-scores the axes REFINE changed (cheap; it also makes l.16's "two consecutive revision passes" evaluable). A targeted Level 2 re-check runs once, only when all hold:
1. Level 2 ran in this CRITIQUE stage;
2. it raised a **major** finding on a judgement axis (1 Genericness or 3 Distinctiveness as clarified in B2), which no mechanical gate can re-verify;
3. REFINE changed the output to address that finding;
4. the SHIP report relies on the fix (it claims the finding resolved).

Scope: a fresh agent, given the rendered output and the named finding(s) only (not Level 1 scores), asked whether each is resolved. It is a verification of named findings, not a second independent discovery pass, and the report says so. Cap: one re-check. Otherwise the report states "Level 2 finding <id> addressed in REFINE, not independently re-verified", which this run already did. Findings verifiable by VALIDATE (this run's overlay comment, meta text size, breakpoint) never trigger the re-check.

Wording belongs with the PT-20 REFINE-loop clarification, not as a separate change.

### E. HARDEN coverage

**Governing text.**
- `SKILL.md` §1 l.29: HARDEN runs for "ship-readiness tasks; skip for prototype/POLISH". Neither term is defined (PT-35).
- `performance-hardening.md` l.24 to l.30: HARDEN-001 is a manual checklist walk (extreme input, error scenarios, i18n/RTL/CJK/`Intl`/pluralization) with no per-item applicability.
- l.7 to l.12: PERF-001 is "universal for any shipped web page"; rendered CWV measurement needs Enhanced.
- `SKILL.md` §1 l.56: a mechanical-countable check gates SHIP when its capability is available; otherwise `skipped — capability unavailable`.

| Item | Required by DE? | What happened | Disposition |
|---|---|---|---|
| HARDEN-001 walk (extreme input, i18n/RTL) | Yes once HARDEN runs, but applicability per item is unstated (RTL/CJK for an English-only single-language page is not obviously relevant) | Not walked; some error scenarios were covered (validation errors, endpoint absent, JS disabled) | **E1 SPECIFICATION AMBIGUITY** |
| PERF-001 CWV (rendered) | Yes, gates SHIP when capability available | Not run; reason not given. Enhanced (Playwright) was available; LCP/CLS are measurable in-page, INP needs interaction; Lighthouse was not installed | **E2 DEFERRED INVESTIGATION** |
| Screen reader | No DE rule requires it (accessibility-tree checks are specified instead) | Not run | **E3 ACCEPTABLE / NOT A GAP** |
| Cross-browser | No DE rule requires it (A11Y-012 notes Chromium-only evidence as a limit, not a requirement) | Chromium only | **E3 ACCEPTABLE / NOT A GAP** |
| `astro check` | Project tooling, not a DE rule | Not run (package not installed, not added) | **E3 ACCEPTABLE / NOT A GAP** |
| Full keyboard visual walk | A11Y-002 (P1): static `:hover`/`:focus-visible` pairing plus "actual keyboard walk" in Enhanced; completeness not quantified | Static pairing and reachability sweeps (40/60 stops) done; visual check on the first 8 desktop stops; disclosed; axis 5 = 4 | **E4 ACCEPTABLE / NOT A GAP** |

**E1 detail.**
- Interpretation 1: HARDEN-001 is a full checklist once HARDEN runs. Interpretation 2: items apply where the product has the input or locale (e.g. no RTL walk for a monolingual site that does not declare RTL support). The test followed neither explicitly; it reported "partial".
- Wording clarification only: resolve PT-35 (for example, an unbounded BUILD that implements counts as ship-readiness unless the user says prototype, as the independent reviewer proposed); give HARDEN-001 an applicability line naming which items are conditional on the product's content, locales and data; and require HARDEN to report each HARDEN-001 item as run, not applicable (with reason) or not run. No item becomes newly mandatory.
- The external agent did not stop early in a way the current text forbids; the text does not say what "done" is.

**E2 detail.** The spec is clear enough here: a runnable mechanical check is not silently omitted. The run neither ran it nor reported `skipped — capability unavailable` with a reason. That is an execution deviation, disclosed as "not run". One observation does not justify a spec change. Watch in the next test.

### F. Level 2 trigger semantics

**Governing text.** `critique-protocol.md` l.21: "Production-facing, brand-critical, or high-traffic work (explicit stakes signal from the brief or Product Truth)". l.23: the explicit brand-quality-bar trigger applies only to **multi-page-site** greenfield BUILD. l.26: no default Level 2 for component/section BUILD. PT-21 and PT-52 already record the missing threshold.

**Analysis.**
- "Production-quality" names an implementation standard, not a deployment intent. "Brand credibility" names the page's goal. Neither is an "explicit stakes signal" in the literal sense.
- But Product Truth is a business's public homepage whose job is to take bookings. Read against Product Truth, "production-facing" plausibly holds.
- The categories the brief asked us to separate:

| Category | Signal | Level 2 under current text |
|---|---|---|
| Production-quality implementation | how well it is built | not a trigger on its own (ambiguous) |
| Production-facing product | intended for real users of a real product/business | trigger |
| Brand-critical | the surface is the brand's primary expression, or the brief makes brand perception the goal | trigger |
| High-traffic | stated or evident scale | trigger |
| Ordinary greenfield marketing page | none of the above | no trigger at page scope (multi-page trigger needs an explicit brand bar) |

- This brief sits between rows 1 and 2/3. The activation was defensible, disclosed as a judgement call, and in hindsight productive (Level 2 produced the run's most useful findings, including the A11Y-012 applicability). It was not over-triggered; it was **not deterministic**.

**Disposition: SPECIFICATION AMBIGUITY.**
- Both readings: (1) literal, explicit-words-only, no trigger; (2) Product-Truth-based, trigger. The test followed (2).
- Wording clarification only: define "production-facing" as the deliverable being intended for real users of a real product or business (from the brief or Product Truth), and state that a request for production-quality implementation alone is not a stakes signal. State whether l.23's multi-page limit on the greenfield brand-quality trigger also bounds l.21 for greenfield page builds (the independent reviewer noted that l.21 can bypass it). Resolve PT-52's tie-break at the same time. Do not remove the trigger.

### G. Heuristic false positives (INTX-003, TYPE-006)

**Governing text.**
- `layout-interaction.md` l.123 to l.130: INTX-003 is mechanical-countable in Enhanced mode ("check for wrapped clickable text at the required floor widths"); the measurement technique is not specified.
- `typography.md` l.62 to l.71: TYPE-006 is "Detection only — no single fix is prescribed by default … Which strategy applies is a per-case judgment"; its targets are orphans, widows and awkward rag on the final line.

**Analysis.**
- INTX-003: the agent's height-based heuristic flagged the wordmark and primary CTA; both were verified single-line (`nowrap`, one line-height). The rule's target is actual wrapping, so a verified non-wrap is not a finding. Triage worked.
- TYPE-006: the flagged lines were deliberate stacked lockups ("Book / your / first / session"). A designed one-word-per-line lockup is not an orphan (a single word left alone on a final line of a flowing headline). The one real orphan ("We teach / it" at 900 px) was caught and fixed. Detection plus per-case judgement is what the rule asks for.
- Both rules already carry sufficient per-case guidance for a correct outcome, and the outcome was correct. A reference measurement technique might reduce triage cost, but one project's markup is not grounds to specify one.

**Disposition: EXPECTED BEHAVIOR.** No clarification recommended now. If a later run shows a false *negative* or an incorrectly dismissed orphan, revisit with a technique benchmark (BM-G, §12).

### Additional findings (from `TEST-RESULTS.md` §26 and §27)

**H1. Category-convention pressure under a brand-mandated palette: DEFERRED INVESTIGATION.**
- Black and red were a P2 brand constraint. That combination is both SLOP-011 cluster 2 (declared as a Known Exception, correctly) and category-guessable in the SLOP-013 sense (`anti-slop-registry.md` l.99 ff.; SLOP-013 has no exceptions field, but P2 outranks P6, so the palette itself is not a violation).
- When the palette is fixed, the other dimensions carry all of the distinctiveness burden. Here the display treatment (condensed heavy uppercase, `context.md` l.59) matches the sports-poster convention by effect even though TYPE-002's face-level cross-check was run and passed. The agent flagged this risk itself at Level 1 axis 1 (§20).
- The skill has no guidance for this situation. But n = 1, the judgement is aesthetic, and the gap may already be covered by C1's rendered check plus axis 1. Investigate within BM-C before proposing anything.

**H2. A11Y-012 applicability for disclosure panels that overlay content: SPECIFICATION AMBIGUITY.**
- `accessibility.md` l.133: applies to "a drawer, sheet, off-canvas navigation panel or modal dialog"; does not apply to "inline disclosures or accordions that expand in place".
- The build's mobile menu is a native `<details>` whose panel overlays the page. It is a disclosure (excluded kind) that does not expand in place (excluded condition does not hold) and is not one of the named overlay kinds. The builder read it as in-place; Level 2 read it as an overlay; the builder then applied A11Y-012 and it passed (§19).
- Wording clarification only: state whether a disclosure or dropdown panel that visually overlays content is in scope. Evidence of a failure is absent (native `<details>` removes closed content), so this is about applicability, not a defect.

**H3. DIRECT candidates not shown to the user before commit: ACCEPTABLE / NOT A GAP.** `SKILL.md` l.44 says DIRECT "states 2 candidate directions … before committing". It does not require user approval, and in an unbounded Implement profile the commit is the agent's. Both candidates were stated in `context.md` Rejected Directions with the required dimensions.

**H4. `accessibility.md` read through a condensed extraction: EVIDENCE INSUFFICIENT.** The skill says the CRITIQUE stage "loads" the file; it does not define full reading. The H2 misclassification happened in a run with a condensed read, but whether a full read would have prevented it is unknown. Missing evidence: a run with a full read on the same markup.

**H5. The test left no record in this repository: TEST-PROMPT AMBIGUITY (test protocol).**
- `STATE.md` still showed the Pre-Test Hardening milestone with the pending gate "Authorization of the first external test"; no test milestone, authorization text or report was recorded in the control plane. The verbatim brief and the Level 2 subagent's brief and output were not preserved.
- The Pre-Test Hardening report §6 step 6 lists what to record, but not where or that the verbatim brief and subagent I/O must be kept.
- Corrected test instruction: save the verbatim brief as `test-evidence/BRIEF.md`, save the Level 2 brief and raw output under `test-evidence/`, and record the test milestone and its authorization in `STATE.md` with a pointer report under `benchmarks/external-test/`. This limits future audits' EVIDENCE INSUFFICIENT findings (B2, C1 pre-REFINE state, A1 exact wording).

---

## 5. Cross-finding synthesis

### 5.1 Are B, C, category genericness and the Level 2 disagreement one problem?

Partly. Three distinct things are involved, and only two share a cause.

1. **Declared-versus-rendered distinctiveness (C1, H1, and the substance of Level 2's findings).** Every existing Level 1 distinctiveness mechanism is relative or on paper:
   - §5 compares the committed direction with the rejected one, on paper, at DIRECT;
   - §6 compares with the project's own past, which is empty on a first project;
   - SLOP-011 compares with named model clusters, and a declared Known Exception satisfies it;
   - the structural test is gated on DETECTED.
   None asks whether the *rendered* output carries the committed direction, or how it sits against the category convention. Level 2 is the only mechanism that does, and it is stakes-gated. That single missing check explains both "the concept never reached the render" and, in part, "the render still reads as the category default". One correction point serves both: axis 1 (C1).
2. **Scoring semantics (B1, B2).** A vacuous comparison scored as a number, and an axis label that means different things to the two levels. This explains why the disagreement *looked* like a perception conflict when axis 1 scores agreed. It is not the same problem as (1) and needs its own, smaller, clarification.
3. **Brand-mandated category palette (H1).** A real pressure, but n = 1 and aesthetic. It may be fully absorbed by (1). Kept separate until evidence says otherwise.

So: **not four fixes, and not one abstraction.** One diagnostic (C1, the only confirmed gap, which also covers most of H1's substance) and one scoring clarification (B1 with B2), with H1 held for the benchmark.

### 5.2 Related, but separate

- **A and C/H1.** LAYOUT-010 exists because candidates stayed inside the Genre's default family (`layout-interaction.md` l.90 evidence). This run disabled that mechanism by P2 reading and then showed category-default convergence. That correlation is not evidence of cause (compatible entries existed, §4.A, but their effect is unknowable). BM-A in §12 is designed to separate the two.
- **D and C1.** A re-check after REFINE (D) is how the C1 finding would be verified when Level 2 raised it. D's condition is written so that C1-type findings (judgement axes) qualify and mechanical ones do not.
- **E1, F1 and D1** all trace to earlier-recorded routing clarifications (PT-35, PT-21/PT-52, PT-20). The external test confirms them in practice; it does not add new root causes.

### 5.3 Not related

G1 (heuristic triage) and H2 (A11Y-012 applicability) are independent of the distinctiveness cluster.

### 5.4 Independent review reconciliation (`loop.md` §8)

One fresh, read-only, blind reviewer (general-purpose subagent) received the evidence and skill paths and the seven questions, not this audit's verdicts. It changed nothing.

| Question | Reviewer | This audit (draft) | Reconciliation |
|---|---|---|---|
| A | TEST-PROMPT AMBIGUITY. Rule: follow what the user names; when the stated purpose plausibly covers the pools, follow the purpose and disclose | A1 TEST-PROMPT AMBIGUITY + A2 SPECIFICATION AMBIGUITY. Rule: an "external" exclusion bounds runtime acquisition | **Agreed on A1.** A2 kept as a secondary wording ambiguity (the reviewer also offers an optional skill sentence). **Adopted** the purpose clause into the proposed rule (§4.A); it confirms the agent's reading was right for a "baseline" |
| B | SPECIFICATION AMBIGUITY. Scoring 3 already conflicts with l.7; the axis-3 label and missing Level 2 definitions explain the disagreement; axis 1 agreed (3/3) | B1 CONFIRMED GAP, B2 SPECIFICATION AMBIGUITY; same axis-1 observation | **Adopted:** B1 downgraded to SPECIFICATION AMBIGUITY. The general clause arguably already covers the case, so the defect is unclear application, not a missing mechanism. Corrections unchanged |
| C | CONFIRMED GAP (narrow). No new rule; one sentence in axis 1 naming the rendered carrier per logged dimension | CONFIRMED GAP (narrow); same location | **Agreed.** The reviewer's "name the carrier" wording adopted as more checkable |
| D | SPECIFICATION AMBIGUITY (PT-20). Re-score Level 1 on changed axes; scoped Level 2 re-check only when a major finding drove REFINE and the ship claim relies on it | SPECIFICATION AMBIGUITY; targeted, capped re-check for major judgement-axis findings | **Agreed;** both additions adopted |
| E | SPECIFICATION AMBIGUITY (PT-35). PERF-001's rendered part leans "stopped early"; screen reader, cross-browser and `astro check` not required | E1 SPECIFICATION AMBIGUITY, E2 DEFERRED (execution deviation), E3/E4 ACCEPTABLE | **Agreed in substance;** the split is finer, not different. The reviewer's PT-35 wording and per-item reporting adopted into E1 |
| F | SPECIFICATION AMBIGUITY (PT-21/PT-52). Not over-triggered; l.23 vs l.21 scope question | SPECIFICATION AMBIGUITY; not over-triggered | **Agreed;** the l.23/l.21 question adopted into F1 |
| G | ACCEPTABLE / NOT A GAP. The false positives came from the agent's heuristic, not the rule | EXPECTED BEHAVIOR | **Label-only difference.** Kept EXPECTED BEHAVIOR because the rules call for detection plus per-case triage and the triage worked as intended; the reviewer's point (heuristic, not rule) matches §4.G's reasoning |
| Screenshots | Level 2 claim supported after REFINE; tape accents local; identity not materially changed | Consistent with the evidence; post-REFINE status unverified | **Adopted as a second consistent read** (§4.C). Still not a formal Level 2 re-score, so the status stays unverified |
| Shared cause | Partly: B and the disagreement share one cause (axis-3 label/definitions); C is related but separate; both corrections land in the critique protocol, no new rule id | Same (§5.1) | **Agreed** |

No disagreement remains unreconciled, so the outcome is not `UNRESOLVED` (`loop.md` §8).

---

## 6. Confirmed architectural gaps

| ID | Gap | Affected file | Smallest correction | Regression risk | Benchmark first? |
|---|---|---|---|---|---|
| C1 | No render-level check that the committed direction's distinguishing dimensions were built | `critique-protocol.md` axis 1 | One qualitative diagnostic using §5's logged dimensions and LAYOUT-009's carrier list; prompt for REFINE, never an automatic fail | Medium-low (decorative box-ticking; confusion with LAYOUT-009) | Yes (BM-C) |

Full detail is in §4.C. B1 was classified CONFIRMED GAP in the first draft and downgraded after independent review (§5.4).

## 7. Specification ambiguities

| ID | Unclear semantics | Readings | Test followed | Proposed wording clarification |
|---|---|---|---|---|
| B1 | Whether an empty fingerprint comparison is scored or `not assessable` | trivially satisfied (scored) / not assessable (l.7) | scored 3 | Axis 3 clause: the first generation is `not assessable: first Fingerprint History entry`; the entry is still recorded as baseline |
| A2 | Whether "external references" reaches the T3 pools | pools are external-derived references / pools are skill knowledge | the first | T3 pools are governed skill knowledge; an "external references" exclusion bounds runtime acquisition; naming the pools or "no references at all" excludes them; declare the reading in one line |
| B2 | Axis 3 label vs definition; Level 2 brief lacks definitions | fingerprint divergence / perceived distinctiveness | both (L1 vs L2) | Level 2 brief carries each axis's one-line definition |
| D1 | What runs after REFINE | CRITIQUE once / full re-run | the first | Targeted, capped Level 2 re-check for major judgement-axis findings changed by REFINE; bundle with PT-20 |
| E1 | HARDEN trigger and HARDEN-001 item applicability | full checklist / conditional items | "partial" | Applicability line per HARDEN-001 item; define "ship-readiness" (PT-35) |
| F1 | "Production-facing" threshold | explicit words only / Product Truth-based | Product Truth-based | Define production-facing as intended for real users of a real product/business; production-quality alone is not a stakes signal; resolve PT-52 |
| H2 | A11Y-012 and disclosure panels that overlay content | in scope / out of scope | out, then in after Level 2 | State the case explicitly |

## 8. Test-prompt ambiguities

| ID | Wording | Corrected instruction |
|---|---|---|
| A1 | "no external visual references, Figma or the licensed library (a reference-free baseline)" | "Do not acquire or consult external visual references (Figma, the licensed library, the web, reference catalogs, other skills). The skill's internal reference pools may be used as the skill specifies." For a deliberate no-pool baseline, name `visual-references.md` and `principle-pool.md` explicitly |
| H5 | Test setup did not require preserving the brief, subagent I/O, or a control-plane record | Save the verbatim brief and the Level 2 brief and raw output under `test-evidence/`; record the test milestone and authorization in `STATE.md`; place a pointer report under `benchmarks/external-test/`; capture pre-REFINE screenshots |

Neither justifies a skill change.

## 9. Expected / acceptable behavior

| ID | Why it is consistent with current governance |
|---|---|
| C2 | LAYOUT-009 applies only to DETECTED / EVIDENCED; DEFINE recorded HYPOTHESIS with a stated reason; a direction's metaphorical name does not change that |
| E3 | Screen reader, cross-browser and `astro check` are not DE requirements; the report listed them as not done |
| E4 | A11Y-002's static check passed, reachability sweeps ran, the partial visual walk was disclosed, and axis 5 reflected it |
| G1 | Both rules require rendered detection plus per-case judgement; the one real orphan was fixed, false positives were verified and recorded |
| H3 | DIRECT "states" candidates; no approval step is specified for an Implement profile; the log meets §5 |
| A (behaviour) | The agent's P2 reading in A was compliant with §3 whichever reading of the prompt is right; the ambiguity is in the wording, not in the behaviour |

## 10. Evidence-insufficient findings

| ID / question | Missing evidence | Not inferred |
|---|---|---|
| H4 | A run with a full `accessibility.md` read on the same markup | whether the condensed read caused the H2 misclassification |
| B2 (part) | The Level 2 subagent's brief | whether the reviewer received DE's axis definitions |
| C1 (part) | Pre-REFINE screenshots | the exact extent of "never reached the render" before REFINE |
| C / H1 post-REFINE | An independent re-score of the refined build | whether the tape treatment resolved the Level 2 distinctiveness concern |
| A (effect) | A paired run with the T3 pools allowed | whether any compatible REF/PRN entry would have changed the identity |
| A1 (exact wording) | The verbatim brief | the precise phrasing beyond the `TEST-RESULTS.md` summary |
| E2 | Why CWV was not attempted | whether the agent judged the capability unavailable |

---

## 11. Follow-up investigation plan

Prioritization reflects behavioural impact, architectural leverage, recurrence potential, evidence confidence, and change cost/risk. It is not a ranking of design outcomes.

**MUST INVESTIGATE NEXT**
1. **C1 + H1, direction carry-through and category convergence.** Highest leverage: it is the only gap whose consequence (a direction that exists only in documentation) ships silently whenever Level 2 does not trigger, which is the common case at page scope. Evidence is one run; benchmark before wording (BM-C).
2. **B1 + B2, distinctiveness scoring semantics (both specification ambiguities).** Text-verifiable, low cost, low risk, and it recurs on every first project. Candidate for a small clarification bundle after authorization; BM-B is optional.
3. **A1 + H5, next-test protocol.** No skill change: corrected instructions for the next external test so that it produces evidence this audit could not use.

**SHOULD INVESTIGATE**
4. **D1** with PT-20 (REFINE loop): write the targeted re-check condition; BM-D.
5. **F1** with PT-21/PT-52: threshold wording; BM-F.
6. **A2**: one-sentence T3/P2 clarification; BM-A.
7. **H2**: A11Y-012 applicability wording (the rule is new; clarifying it early is cheap).

**DEFER**
8. **E1** (HARDEN applicability, PT-35) and **E2** (watch for recurrence).
9. **G1** (revisit only on a false negative).
10. **H4** (revisit only if a misclassification recurs with a condensed read).

## 12. Proposed benchmark definitions

None is run in this milestone. Each fits the existing `benchmarks/<topic>/` convention; no new benchmark phase is needed.

| ID | Shape | What it tests | Minimal setup | Pass/fail signal | Guards against |
|---|---|---|---|---|---|
| BM-C | Direction-to-build carry-through | Whether the committed direction's §5 distinguishing dimensions (especially materiality/composition) appear in the render, with and without the proposed axis-1 diagnostic | 2-3 greenfield page BUILDs at page scope **without** a Level 2 trigger, briefs that invite a material/physical direction; one brand-mandated category palette among them (covers H1). Independent evaluator compares render with `context.md` dimensions | Carriers present on at least one carrier surface for each claimed dimension; evaluator notes any decorative box-ticking | C1 turning into sticker-style "proof"; confusion with LAYOUT-009 |
| BM-B | First-project distinctiveness | Axis 3 on a first generation reports `not assessable`; axis 1 carries category judgement; Level 2 given axis definitions scores axis 3 the same way | Re-score the External Test A evidence (read-only) under the clarified text, plus one fresh first-project run | L1 and L2 axis 3 both use the fingerprint definition; no numeric first-entry axis 3 | Losing the Fingerprint History baseline entry |
| BM-A | Internal-T3 vs external-reference exclusion | Whether the instruction wording changes T3 pool use, and whether pool use changes candidate breadth | Same brief, three prompt variants: (i) "no external references (Figma/licensed library/web)", (ii) that plus "internal pools allowed", (iii) "no reference pools at all" | (i) and (ii) load and screen the pools; (iii) does not; the reading is declared in one line | Forcing T3 use against an explicit P2 |
| BM-D | Critique → refine → re-critique | The targeted re-check fires only for major judgement-axis Level 2 findings changed by REFINE, and only once | One Level 2-triggered BUILD seeded with a genericness-prone brief; one with only mechanical Level 2 findings | Re-check in the first, none in the second; report wording for the unverified case | Unconditional double Level 2 cost |
| BM-F | Level 2 trigger semantics | Deterministic activation across the five categories in §4.F | Five one-paragraph briefs, one per category, classification only (bounded, no build) | Same trigger decision across two independent runs per brief | Removing the trigger to save cost |
| BM-E | HARDEN capability-limited case | HARDEN-001 item applicability and PERF-001 reporting when the browser is available but lab tooling is not | One ship-ready BUILD, monolingual, Enhanced without Lighthouse | Conditional items reported as not applicable with reason; CWV measured in-page or `skipped` with reason | Making every checklist item mandatory |
| BM-G | Heuristic triage (deferred) | INTX-003/TYPE-006 detection technique vs false negatives | Seeded fixtures: real wraps, real orphans, nowrap flex children, designed lockups | No real wrap/orphan dismissed | Rule text tuned to one project's markup |
| BM-H2 | Overlaying disclosure panel | A11Y-012 applicability decision for `<details>`/dropdown panels that overlay content | Two fixtures: in-place disclosure, overlaying disclosure | Consistent applicability decision across runs | Widening A11Y-012 to all disclosures |

## 13. Explicit non-changes

Based on this evidence alone, the following **should not** be changed:

1. **P2 authority.** Do not weaken P2 or add an exception to make T3 pools load against an explicit user instruction.
2. **LAYOUT-009's activation.** Do not activate Concept → Structure for directions, metaphors in direction names, or HYPOTHESIS outcomes.
3. **The fingerprint system.** Keep the 5 dimensions, the 2-of-5 test, redirect-not-refusal and per-project scope. Do not add materiality or a sixth dimension, and do not add cross-project comparison.
4. **Critique scores and tiers.** No new axis, score, tier or pass mark. B1 reuses `not assessable`.
5. **Level 2 as a default.** Do not make Level 2 unconditional, and do not make a full Level 2 re-run follow every REFINE.
6. **The production-facing trigger.** Do not remove or narrow it to reduce cost; clarify it.
7. **HARDEN scope.** Do not make screen-reader testing, cross-browser testing, Lighthouse, framework type-checks or every HARDEN-001 item mandatory.
8. **INTX-003 and TYPE-006.** Do not add project-specific exemptions (lockups, nowrap flex children) or a prescribed measurement script.
9. **SLOP-011 / SLOP-013.** Do not add a brand-palette exception or a new anti-slop entry for black-and-red or combat-sports conventions. No new Anti-Slop entry for a category's conventions from one project.
10. **Aesthetic preferences.** Do not encode this audit's or the Level 2 critic's view of condensed display type, black-and-red, or tape as a rule.
11. **Genre/Register classification.** Editorial for this brief was evidence-traced; no change to Genre inference.
12. **A11Y-012's principle and validation.** Only its applicability wording is in question (H2).
13. **The external test project.** Nothing in `<external-test-a-project>` was or should be modified by this milestone.

## 14. Recommended next milestone

**Recommendation (requires human authorization; not authorized by this milestone):** *Direction Carry-Through & Distinctiveness Semantics Benchmark*: run BM-C (2-3 greenfield page BUILDs without a Level 2 trigger, one with a brand-mandated category palette) and BM-B (read-only re-score of the External Test A evidence plus one first-project run), against the unchanged skill, to establish whether C1 recurs and whether the proposed axis-1 diagnostic and axis-3 first-entry clause would catch it without inducing decorative box-ticking.

Alternatives, in order:
1. A text-only *Targeted Specification Clarification* bundling B1, B2 and A2 (text-verifiable, low risk), leaving C1 for the benchmark.
2. A second external test using the corrected instructions in §8 (A1, H5), which would also supply the missing evidence in §10.

What the human needs to decide: whether to gather more behavioural evidence first (recommended, because C1 rests on one run) or to authorize the low-risk text clarifications now.
