# PHASE 6.0 — Creative Direction Correction Plan

Status: **PLAN ONLY.** No file inside `design-excellence/design-excellence/` (the skill package) was modified to produce this document. This is the only file created for Phase 6.

Evidence sources actually inspected: `SKILL.md` (full, loaded by the invoking command), `ARCHITECTURE.md` (§24 Scenario A, §23 tiering), `design-excellence/references/anti-slop-registry.md`, `references/style-catalog.md`, `references/rule-catalog/{typography,layout-interaction,color}.md`, `references/critique-protocol.md`; benchmark artifacts at `design-excellence-benchmark/` — `brief.md`, `.design/context.md`, `index.html`, and rendered screenshots `home-1440px.png` / `home-390px.png`.

---

## 1. Executive diagnosis

The benchmark's hypothesis is **supported by direct, file-level evidence, not just visual impression.** This is not merely "the output looked generic" — the skill's own reference material names the exact failure in advance and was not consulted at the moment it mattered, and the skill's own canonical worked example for *this exact brief archetype* prescribes a different Genre than the one actually produced.

Two distinct failure classes emerged, and they must not be conflated into one fix:

1. **A confirmed regression against the skill's own documented behavior.** `ARCHITECTURE.md` §24 Scenario A is literally titled *"Build a premium chiropractic website from scratch"* — the same brief archetype, word for word — and specifies `Genre=Atmospheric-Expressive inferred from "peace, tranquility, serenity, calm" brief language`, with independent (Level 2) critique recommended given brand stakes. The benchmark's brief contains that trigger language verbatim (`brief.md` line 15: "Calm"). The actual run inferred `genre: editorial` (`.design/context.md` frontmatter) and there is no evidence Level 2 critique ran. This is not a subjective taste gap — it is the system not reproducing its own specified reference behavior.

2. **A real architectural gap in how DIRECT explores alternatives, and in how Anti-Slop's atomic checks fail against a gestalt (combination) pattern.** `anti-slop-registry.md` SLOP-011 names the exact color/type/accent cluster the benchmark produced as a documented model self-tell — and it survived anyway, because nothing in the pipeline validates the *combination* of choices, only checks each dimension in relative isolation, and because the only "exploration" of alternatives on record (`context.md`'s Rejected Directions) rejected the one genre the architecture itself recommends, on a narrow, incorrect premise (that Atmospheric-Expressive requires stock photography).

The user's hypothesis — "better at preventing generic design than generating distinctive design" — is correct as stated, but the mechanism is more specific than general over-caution: DIRECT never generates competing candidates to evaluate, Genre inference collapsed to a category stereotype instead of the brief's actual emotional register, and Anti-Slop's per-item structure has no gestalt/cluster-level gate even though one of its own entries (SLOP-011) is explicitly written as a cluster.

---

## 2. Evidence

### 2.1 Genre misrouted against the skill's own canonical example

- `ARCHITECTURE.md` line 517–521 (Scenario A): same brief archetype ("premium chiropractic website"), specifies `Genre=Atmospheric-Expressive`, `Register=Brand-led`, and "CRITIQUE(floor; **independent recommended** given real-business/brand stakes)".
- `brief.md` line 15: brand should feel "Calm" — matches the architecture's own cited trigger phrase almost exactly.
- `style-catalog.md` line 56, `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s `best_for` field: *"brand-led hospitality/wellness/lifestyle/experiential work — exactly the register this skill's own prior project work (**a calm, serene chiropractic clinic brief**) called for."* This is the style catalog's own demonstration entry, and it names this precise brief type as its textbook example.
- `.design/context.md` (benchmark) frontmatter: `genre: editorial`. Rejected Directions log: *"Atmospheric-expressive genre (mood photography, large ambient imagery) — rejected: brief prohibits stock-photo-heavy layouts and no real photography exists."*

The rejection reasoning is the tell: it equates Atmospheric-Expressive with "mood photography, large ambient imagery" — but `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s actual definition (line 50–60) is "committed color, layered depth, deliberate texture/material language, larger type contrast" — none of which requires photography. Genre was rejected for a property it doesn't actually require. **CONFIRMED GAP.**

### 2.2 SKILL.md §4's Genre-inference instructions are underspecified relative to what ARCHITECTURE.md actually intended

`SKILL.md` §4 states inference order as "Genre sets the default band → brief language may move it → Register sets a hard ceiling" but gives no concrete mapping from brief language to Genre — no keyword list, no emotional-register-to-Genre table, nothing like the worked example in `ARCHITECTURE.md` §24. The 573-line architecture document's worked example didn't survive compression into the ~180-line T0 file. DEFINE is left to a same-context judgment call with no durable anchor, which is exactly the failure mode that produced a category-stereotype answer ("premium healthcare" → editorial-premium) instead of a brief-derived one (calm/human/trustworthy → atmospheric-expressive, per the skill's own example). **CONFIRMED GAP.**

### 2.3 DIRECT has no candidate-generation step

`SKILL.md` §1 describes DIRECT only as: "establishing direction for a surface with none yet." Nothing in T0, T1, or `critique-protocol.md` instructs generating 2–3 plausible directions and evaluating them against the brief before committing. `.design/context.md`'s "Rejected Directions" section (§5 of `SKILL.md`, populated per `ARCHITECTURE.md` line 207) is the only mechanism that could serve this function, and in the benchmark it recorded exactly 3 entries — 2 of which are anti-pattern avoidances explicitly demanded by the brief ("centered hero + 3 cards," "generic wellness palette"), not genuine creative alternatives considered and weighed. Only one entry (Atmospheric-Expressive) was a real alternative direction, and it was rejected on the incorrect premise in §2.1. **CONFIRMED GAP** — DIRECT behaves as classify → select one direction → implement, exactly the pattern the command's diagnosis section asked to verify.

### 2.4 Anti-Slop's own named cluster was reproduced

`anti-slop-registry.md` SLOP-011 (lines 83–89) names four "model self-tell clusters" for the current model generation. Cluster (1): *"warm cream `#F4F1EA` + high-contrast serif + terracotta accent near `#D97757`."* `.design/context.md`'s actual Visual System (benchmark): "warm bone background, deep warm-charcoal ink, deep terracotta/clay primary accent" + "Newsreader (serif, editorial headlines) + Public Sans." This is cluster (1), reproduced almost exactly, in the one entry of the registry explicitly flagged "**highest-priority entry for review**" for exactly this reason (line 89). **CONFIRMED GAP**, and it demonstrates a structural weakness: every other Anti-Slop entry is checked as an individual, atomic item (italic on headings, single-word accents, card uniformity, etc.), but SLOP-011 is written as a *combination* pattern. There is no step in VALIDATE or CRITIQUE that checks a finished direction against SLOP-011's cluster definitions as a gestalt — only against individual rules, which each may pass in isolation (a warm neutral background is not itself banned; a serif display face is genre-legitimate per `STYLE-EDITORIAL-01`; a single accent color under 10% coverage passes `COLOR-001`'s Restrained tier).

### 2.5 A mechanically-countable Anti-Slop rule was violated and not caught

`anti-slop-registry.md` SLOP-003 (lines 26–31): tracked-out eyebrow labels, "mechanically checkable: count instances, fail if count exceeds `ceil(sectionCount / 3)`." The rendered homepage (`home-1440px.png`) shows numbered eyebrows on 6 of its sections (01—Enfoque, 02—Servicios, 03—Para quién, 04—El espacio, 05—Primera visita, 06—Equipo) against roughly 8–9 total sections (hero, 6 numbered, CTA band, footer) → `ceil(9/3) = 3`. Actual count (6) exceeds the threshold by 2×. This rule has an explicit mechanical validation method and still shipped violated. This is **not** an architecture gap — the rule and its check exist and are correctly specified — it is an **execution gap**: nothing in the pipeline forces VALIDATE's mechanically-countable checks to actually run and gate the output before SHIP, as opposed to being available-but-optional prose the generating pass can silently skip.

### 2.6 Self-critique cannot reliably catch what DIRECT itself produced

`critique-protocol.md` Level 1 (lines 5–16) is self-administered by the same context that generated the output, scoring "Genericness — would this be produced for any similar brief" as axis 1. Level 2 (independent, isolated-subagent review) exists specifically because, per the protocol's own reasoning (line 27, line 34), a single context cannot self-audit its own blind spots — this is stated explicitly as the rationale for Level 2's existence. Yet Level 2 only triggers for REDESIGN, an explicit stakes signal, or two consecutive Level-1 failures (line 20–23) — none of which fire by default for a first-pass greenfield BUILD, even though `ARCHITECTURE.md`'s own Scenario A for this exact brief type recommends independent critique for brand stakes (§2.1 above). Self-critique is structurally the wrong tool to catch a self-tell cluster the generating pass itself reached for — this is confirmed by the protocol document's own stated rationale for why Level 2 exists at all.

### 2.7 No imagery/art-direction decision framework exists anywhere

Full-package grep for `imagery|photograph|illustration|art direction` returns exactly one hit in the entire skill package: `SKILL.md` §6, a parenthetical stating imagery is "worth noting informally" but explicitly **excluded** from any tracked/blocking criteria. There is no rule in any T2/T3 file that gives a decision framework for whether, what kind, or how much imagery a direction should carry. The benchmark's own reasoning for omitting imagery (`.design/context.md` line 28: "no stock photography — identity carried by typography, color, and the alignment-rule motif (also pragmatic: no real photos available...)") conflates "no real client-supplied photos" with "no imagery of any visual-weight-bearing kind" — a false equivalence the brief itself didn't require (the brief banned *stock-photo-heavy* layouts, not all imagery; illustration, abstract graphic systems, and original AI-generated imagery were never considered or rejected — they don't appear anywhere in Rejected Directions). **CONFIRMED GAP.**

### 2.8 VISUAL_DENSITY is wired to spacing only, not visual mass

`layout-interaction.md` LAYOUT-007 (Phase 4 addition) is the sole rule-catalog consumer of `VISUAL_DENSITY`, and its entire effect is section-rhythm spacing values (48–96px vs. compact). `LAYOUT-001` also references density for macrostructure bundle selection (Bento Grid vs. Long Document), but that reference points to a "catalog of named bundles" that `LAYOUT-001` line 15 claims is "populated in `style-catalog.md`" — it is not; `style-catalog.md` contains 4 Genre-level entries, not a macrostructure-bundle catalog (Bento Grid, Long Document, Marquee Hero, Specimen, Manifesto are named in `LAYOUT-001`'s principle text but never defined anywhere in the package). Density=4 (Medium) in the benchmark therefore had no lever over image presence, graphic/color-field mass, or composition complexity — because no such lever exists in the rule catalog at all. This directly supports the user's §7 hypothesis: density currently means "spacing," not "visual mass." **CONFIRMED GAP** (scope) + **CONFIRMED reference/data gap** (the undefined bundle catalog `LAYOUT-001` depends on).

### 2.9 DESIGN_VARIANCE has narrow real effect, and a Medium-band no-op

`color.md` COLOR-001 (lines 6–14) and `layout-interaction.md` LAYOUT-001 are the only two rule-catalog consumers of `DESIGN_VARIANCE` (per the Phase 4 correction notes cited in both files). Both specify behavior only for High band (push tiers up / raise fingerprint bar) and Low band (hold down / permit consistency) — **Medium band (4–7) is unspecified in both rules and defaults to the Genre's own default, i.e. variance has no operative effect at Medium.** The benchmark's variance was 6 (Medium) — squarely in the unspecified range. This is consistent with, though not sufficient alone to fully explain, why a Medium-high-declared variance still produced a maximally-safe, genre-default result. **CONFIRMED GAP** (banding leaves a real no-op zone) — narrower in scope than a full "variance has no teeth" claim.

### 2.10 No responsive headline/hero validation exists

Full-package grep for `orphan|widow|rag|line-break` (case-insensitive) across `design-excellence/design-excellence/` returns zero hits. `INTX-003` (`layout-interaction.md` lines 84–91) covers clickable text (buttons/nav/CTAs) never wrapping — it explicitly does not cover a static `<h1>` headline. `TYPE-003` (line length) is scoped to running body prose, explicitly excluding display/headline type. `LAYOUT-002` (squint test) checks hierarchy survival, not line-break quality. The mobile hero orphan-word defect the benchmark exposed has no rule anywhere in the catalog that would have caught it. **CONFIRMED GAP.**

---

## 3. Root causes

**Architectural causes:**
- DIRECT has no candidate-generation/evaluation sub-step; it is a single-direction commit point, not an explore-then-select point (§2.3).
- Anti-Slop entries are validated atomically; there is no gestalt/cluster-level validation pass, even though the registry itself contains at least one entry (SLOP-011) explicitly written as a combination (§2.4).
- `VISUAL_DENSITY`'s conceptual scope in `SKILL.md` §4 (declared as a general dial) was never given a rule-catalog consumer broader than spacing rhythm (§2.8).

**Rule causes:**
- `SKILL.md` §4's Genre-inference instructions lack the concrete brief-language mapping that `ARCHITECTURE.md`'s own worked example depends on (§2.2).
- `DESIGN_VARIANCE`'s two wired consumers (`COLOR-001`, `LAYOUT-001`) both leave Medium band unspecified, a real no-op gap (§2.9).
- No rule exists for headline/hero responsive integrity — orphans, widows, rag (§2.10).
- No rule/framework exists for imagery or art-direction decision-making (§2.7).

**Routing causes:**
- Level 2 (independent) critique does not trigger by default for a first-pass greenfield BUILD even at brand-critical stakes, contradicting `ARCHITECTURE.md`'s own Scenario A recommendation for this exact brief type (§2.1, §2.6). This is a routing/trigger-condition gap in `critique-protocol.md`, not a Level-1-vs-Level-2 design flaw.

**Reference/data causes:**
- `LAYOUT-001` references a "catalog of named bundles" (Bento Grid, Long Document, Marquee Hero, Specimen, Manifesto) that is never actually populated anywhere in the package — `style-catalog.md` only has Genre-level entries (§2.8).
- `style-catalog.md`'s own atmospheric-expressive entry directly names this brief archetype as its textbook example, but nothing in `SKILL.md`'s DEFINE-stage instructions forces cross-checking a rejected-direction rationale against the style catalog's own `best_for` text before finalizing Rejected Directions (§2.1).

**Implementation causes (this specific run, not necessarily systemic):**
- SLOP-003's mechanically-countable eyebrow-count check was not actually run/enforced before SHIP (§2.5) — the rule and its validation method are correctly specified; execution didn't gate on it.
- The mobile hero was not checked against real rendered line-wrap at the 390px breakpoint before SHIP, despite `SKILL.md`'s VALIDATE stage nominally covering "always." This is an execution gap layered on top of the rule gap in §2.10 — even a new rule needs an execution point that actually runs it.

---

## 4. Proposed Phase 6 changes

### CD-1 — Add a lightweight candidate-direction step inside DIRECT
- **Problem:** DIRECT commits to a single direction without generating/weighing alternatives (§2.3).
- **Evidence:** §2.1, §2.3 — Rejected Directions log contains only 1 genuine creative alternative, rejected on an incorrect premise.
- **Proposed solution:** for page/multi-page-site scope BUILD/REDESIGN only (never section/component — matches existing scope-gating in §1), DIRECT names 2 plausible Genre/macrostructure directions (not full designs) before committing, states one line of why each is or isn't right for *this* Product Truth, and logs the rejected one in Rejected Directions with the real reason. This is the existing Rejected Directions mechanism, made mandatory-with-minimum-count rather than incidental.
- **Files likely affected:** `SKILL.md` §1 (DIRECT row description), `SKILL.md` §5 (Rejected Directions section requirements).
- **Expected behavioral change:** a genuine second candidate gets weighed, not just anti-patterns the brief already banned.
- **Risk:** low — this is additive, cheap (two one-line candidates, not two full designs), and doesn't touch P1/accessibility/anti-slop.
- **Priority:** HIGH.

### CD-2 — Cross-check Genre rejection rationale against the style catalog's own `best_for` text
- **Problem:** Atmospheric-Expressive was rejected on a premise (`requires photography`) its own catalog entry doesn't state (§2.1).
- **Evidence:** §2.1 — `style-catalog.md` line 56 vs. `.design/context.md` Rejected Directions text.
- **Proposed solution:** when DEFINE or DIRECT rejects a Genre that `style-catalog.md` is loaded for (T3 load already happens at DIRECT/DESIGN per `SKILL.md` §7), the rejection rationale must be checked against that Genre's own `best_for`/`keywords` fields, not an assumed stereotype. If the rejection reason doesn't match anything actually in the entry, that's a signal to reconsider, not proceed.
- **Files likely affected:** `SKILL.md` §5 (Rejected Directions requirements), possibly a one-line addition to `style-catalog.md`'s header instructing this cross-check.
- **Expected behavioral change:** genre rejections become evidence-based against the catalog's own text, not assumption-based.
- **Risk:** low.
- **Priority:** HIGH.

### CD-3 — Concrete Genre-inference anchor in SKILL.md §4
- **Problem:** §4's inference order has no operative brief-language-to-Genre mapping (§2.2).
- **Evidence:** §2.2 — `ARCHITECTURE.md`'s worked example didn't survive compression into T0.
- **Proposed solution:** add one short, illustrative (not exhaustive) example directly to §4 — the same kind of one-line anchor `ARCHITECTURE.md` §24 Scenario A already contains ("brief language like 'calm/serene/human' points toward Atmospheric-Expressive over a category default like 'healthcare = editorial-premium'"). Not a keyword-matching table (that would re-introduce the "more rules" trap the command explicitly warned against) — one grounding example is enough to break the category-stereotype reflex, consistent with how Register/Genre inference is already described as "a judgment call... not a fixed keyword list" elsewhere in `SKILL.md` §7.
- **Files likely affected:** `SKILL.md` §4.
- **Expected behavioral change:** DEFINE has a concrete anchor for one of its highest-leverage decisions, reducing convergence to category stereotypes.
- **Risk:** low — one sentence, no new mechanism.
- **Priority:** HIGH.

### AS-1 — Gestalt/cluster check for SLOP-011-style combination entries
- **Problem:** Anti-Slop entries validate atomically; SLOP-011 is written as a cluster and has no cluster-level check (§2.4).
- **Evidence:** §2.4 — cluster reproduced near-exactly while every contributing element passed its own individual rule.
- **Proposed solution:** at CRITIQUE (Level 1, "Genericness" axis in `critique-protocol.md`), add one explicit sub-check: compare the finished direction's color-anchor + typography + accent combination against SLOP-011's named clusters as a whole, not just each dimension separately. This is a check-ordering fix, not a new rule — SLOP-011 already exists and already says what to look for.
- **Files likely affected:** `critique-protocol.md` (Level 1 axis 1 description), possibly a one-line cross-reference added to `anti-slop-registry.md` SLOP-011 itself pointing at where the cluster-level check now lives.
- **Expected behavioral change:** a direction that individually passes SLOP-001 through SLOP-010 but matches a named SLOP-011 cluster as a whole gets flagged before SHIP, not after a human looks at a screenshot.
- **Risk:** low — reuses an existing entry, adds one check step, no new registry content.
- **Priority:** HIGH.

### VAL-1 — VALIDATE actually gates on mechanically-countable Anti-Slop rules before SHIP
- **Problem:** SLOP-003's countable eyebrow-ratio check exists and wasn't enforced (§2.5).
- **Evidence:** §2.5 — 6 eyebrows against a computed ceiling of 3.
- **Proposed solution:** `SKILL.md` §1's VALIDATE row already says "always... but only the gates relevant to what was touched" — add one line making explicit that mechanically-countable rules flagged `validation: mechanical-countable` in the loaded rule-catalog/anti-slop entries are a hard pass/fail gate before SHIP, not advisory text a generation pass can silently not apply. This doesn't add a new rule — it closes the gap between "the rule says it's mechanically checkable" and "something actually checks it."
- **Files likely affected:** `SKILL.md` §1 (VALIDATE row).
- **Expected behavioral change:** rules already marked mechanically-countable (SLOP-003, TYPE-001, TYPE-003, LAYOUT-004, LAYOUT-005, LAYOUT-007, COLOR-001, COLOR-003, and the new HERO-001 in §9 below) actually gate output.
- **Risk:** low-medium — this is the change most likely to add real per-task cost (an explicit count/measure pass), but it's proportional (only the categories already loaded for the task).
- **Priority:** HIGH — this is the cheapest, highest-confidence fix in this plan; the rule already exists, only enforcement is missing.

### CRIT-1 — Brand-stakes default for Level 2 critique on greenfield multi-page BUILD
- **Problem:** Level 2 doesn't trigger by default for a first-pass greenfield BUILD even at brand-critical stakes, contradicting the architecture's own Scenario A (§2.1, §2.6).
- **Evidence:** §2.6 — `ARCHITECTURE.md` line 519 explicitly recommends independent critique for this scenario; `critique-protocol.md`'s trigger list doesn't structurally cover "greenfield multi-page BUILD with an explicit premium/brand-quality bar in the brief."
- **Proposed solution:** add one trigger condition to `critique-protocol.md`'s existing list: a genuinely-empty, multi-page-site-scope BUILD where the brief itself states a brand-quality bar (the word "premium," "flagship," "brand identity," or equivalent — matched the same judgment-call way Register/Genre inference already works, not a keyword list) escalates to Level 2 by default, same as REDESIGN already does.
- **Files likely affected:** `critique-protocol.md` (Level 2 trigger conditions).
- **Expected behavioral change:** the one class of task most likely to need an outside eye (a from-scratch brand launch) gets one by default, matching what the architecture already specified for this exact scenario type.
- **Risk:** low-medium — adds cost (one subagent dispatch) but only for genuinely high-stakes greenfield work, which is already a small subset of tasks.
- **Priority:** HIGH.

### IMG-1 — Minimal imagery/art-direction decision framework
- **Problem:** zero decision framework exists for whether/what/how imagery should be used (§2.7).
- **Evidence:** §2.7 — one parenthetical in the entire package, and it excludes imagery from any tracked criteria.
- **Proposed solution:** add one short rule to a T2 file (likely `layout-interaction.md`, since imagery-as-layout-weight is closer to that category than to color or typography) that gives a 4-question decision sequence: (1) does this brief/subject warrant visual weight beyond typography+color — yes/no, stated; (2) if yes, is real/provided photography available — if not, is illustration, an abstract graphic system, or original (non-stock-looking) imagery appropriate instead of defaulting to none; (3) what role does it play (hero-anchor, supporting texture, wayfinding); (4) how does it interact with the type/layout system already chosen (LAYOUT-001's macrostructure). This does not mandate imagery — "no imagery, and here's why" remains a fully legitimate answer to question 1, same as the benchmark's actual answer, but it must be an answered question, not a silent default.
- **Files likely affected:** `layout-interaction.md` (new rule), `SKILL.md` §6 (imagery already listed as an informal fingerprint dimension — no change needed there, just point to the new rule).
- **Expected behavioral change:** "no imagery" becomes a stated, evaluated decision instead of the only option that was ever on the table.
- **Risk:** low — this is explicitly a decision *procedure*, matching `TYPE-002`'s existing pattern (generative, not a constraint), not a "use images" mandate the command explicitly warned against adding.
- **Priority:** MEDIUM.

### DENS-1 — Extend VISUAL_DENSITY's scope statement, without inventing new consumers wholesale
- **Problem:** density currently means spacing only; the concept the dial name implies (visual mass) is broader (§2.8).
- **Evidence:** §2.8 — `LAYOUT-007` is the sole real consumer; `LAYOUT-001`'s bundle catalog is unpopulated.
- **Proposed solution:** two parts. (a) Populate `LAYOUT-001`'s referenced "named bundle catalog" — it's already promised to exist in `style-catalog.md` and doesn't; this is closing a broken cross-reference, not adding new scope. (b) Add one line to `SKILL.md` §4's dial description clarifying `VISUAL_DENSITY` covers spacing *and* macrostructure choice (already true via `LAYOUT-001`) and, once IMG-1 exists, the imagery decision's visual weight (question 3 in IMG-1) — wiring the existing dial to the existing new rule, not inventing a third mechanism.
- **Files likely affected:** `style-catalog.md` (populate the bundle catalog referenced by `LAYOUT-001`), `SKILL.md` §4 (one-line scope clarification).
- **Expected behavioral change:** `LAYOUT-001`'s own stated mechanism becomes usable (it currently references content that doesn't exist); density's effective scope matches what `SKILL.md` already implies.
- **Risk:** low-medium — populating the bundle catalog is genuinely new content, closer to "more rules" than the command wants; keep it minimal (5 named bundles, one line each, no new format).
- **Priority:** MEDIUM.

### VAR-1 — Specify Medium-band behavior for DESIGN_VARIANCE's two existing consumers
- **Problem:** `COLOR-001` and `LAYOUT-001` both leave Medium band unspecified, a real no-op zone (§2.9).
- **Evidence:** §2.9.
- **Proposed solution:** one line each in `COLOR-001` and `LAYOUT-001`'s `applicability` fields stating Medium-band behavior explicitly (e.g., "Medium band: genre default applies, but at least one dimension — color tier or macrostructure — should visibly move off the genre's most conservative option, not both stay at minimum"). This is filling a stated-but-empty band, not adding new dial consumers.
- **Files likely affected:** `color.md` (COLOR-001), `layout-interaction.md` (LAYOUT-001).
- **Expected behavioral change:** a variance=6 brief (like the benchmark) can no longer land at the genre's most conservative possible output on every axis simultaneously.
- **Risk:** low.
- **Priority:** MEDIUM.

### HERO-1 — New rule: responsive headline/hero integrity
- **Problem:** no rule anywhere checks orphan/widow/awkward rag in display headlines (§2.10).
- **Evidence:** §2.10 — the mobile orphan-word defect the benchmark exposed; zero grep hits for the concept anywhere in the package.
- **Proposed solution:** add one new rule to `typography.md` (structural, not a "current AI tell," so `typography.md` is the right home per that file's own stated scope, not `anti-slop-registry.md`): display/hero headlines are checked at each declared responsive breakpoint for orphaned single words on the final line (use a non-breaking space between the last two words, or rebalance the line break, as the fix) and are validated the same "mechanical-countable, rendered, Enhanced mode" way `INTX-003` already validates clickable-text wrapping — this is the same technique applied to a different element class, not a new validation mechanism.
- **Files likely affected:** `typography.md` (new rule, id `TYPE-006`).
- **Expected behavioral change:** the exact defect the benchmark exposed gets a durable, reusable check instead of remaining a one-off fix.
- **Risk:** low — narrowly scoped, mechanically checkable, no P1/accessibility interaction.
- **Priority:** HIGH — cheapest, most concrete, directly reproduces a real observed defect.

---

## 5. Creative Direction proposal

The smallest change that introduces genuine exploration without turning the skill into a style generator is **CD-1 + CD-2 together**, not a new pipeline stage. Do not add a new named stage between DIRECT and SHAPE — that would violate §11's "preserve what already works" (routing architecture) and the command's explicit "do not create new rules/catalogs" constraint. Instead:

- DIRECT, for page/multi-page-site BUILD/REDESIGN only, produces a minimum of 2 named candidate directions (Genre + one-line macrostructure sketch each) before committing — reusing the *existing* Rejected Directions mechanism in `.design/context.md`, just requiring it to contain at least one genuine creative alternative (not only anti-pattern avoidances the brief already demanded), and requiring the rejection reason to be checked against the style catalog's actual `best_for`/`keywords` text (CD-2) rather than an assumed stereotype.
- This costs roughly two sentences of extra reasoning at DIRECT — cheap, proportional to §1's stated cost model, and does not touch BUILD, VALIDATE, or any P1 gate.
- It does not become a style generator because it doesn't enumerate a catalog of styles to choose from — it asks DIRECT to justify its single choice against one real alternative, using data that's already loaded (`style-catalog.md` is already a T3 load at DIRECT/DESIGN per `SKILL.md` §7).

---

## 6. Imagery / Art Direction proposal

**IMG-1** (§4) is the smallest change supported by evidence: a 4-question decision *procedure* (matching `TYPE-002`'s existing generative-procedure pattern, not a constraint), living in `layout-interaction.md`. It explicitly permits "no imagery" as a valid, stated answer — the benchmark's actual choice may well have been correct for this specific brief (no real photography existed, and the brief itself flagged stock-photo-heavy layouts as a thing to avoid) — the gap is that this was never an evaluated decision against alternatives (illustration, abstract graphic systems, AI-generated imagery), it was the only option ever on the table. Do not add a "must include imagery" rule, a stock-photo sourcing mechanism, or an imagery style catalog — none of that is supported by the evidence, and the command explicitly warned against forcing imagery.

---

## 7. Dial improvements

Both dials need their **existing, already-stated scope actually wired up**, not a broader redefinition:

- `DESIGN_VARIANCE`: **VAR-1** closes the Medium-band no-op (§2.9). No new consumers proposed beyond `COLOR-001`/`LAYOUT-001` — extending variance into typography/imagery/shape-language/interaction, as the command's investigation section asked about, is **NOT SUPPORTED BY EVIDENCE** from this single benchmark; the two existing consumers weren't even fully exercised (Medium band was a no-op) before the benchmark ran, so there's no evidence yet that they're insufficient in scope, only that they're incompletely specified. Revisit broader variance scope only after VAR-1 ships and a future benchmark still shows convergence.
- `VISUAL_DENSITY`: **DENS-1** closes the broken `LAYOUT-001` cross-reference (populate the bundle catalog it already promises) and wires density into IMG-1's imagery-weight question once that rule exists. This is the dial closer to the user's "visual mass" hypothesis (§7 of the command) — supported, but the fix is "make the existing promised mechanism real," not "add materiality/color-field/typography-scale as new density-consumed dimensions," which would be new scope beyond what evidence supports from one benchmark.

---

## 8. Anti-Slop correction

Evidence supports a **narrow, specific** correction, not a general "anti-slop needs positive counterpart" rewrite:

- Anti-Slop's structure as "a negative constraint system" is not itself the problem — every individual SLOP entry the benchmark violated (SLOP-003, SLOP-011) had a correctly-specified, mechanically-checkable rule. The problem is (a) SLOP-011 is a *cluster* rule with no cluster-level check (**AS-1**, §4), and (b) mechanically-countable rules across the whole catalog aren't guaranteed to actually gate SHIP (**VAL-1**, §4).
- The broader claim in the command's §9 — that repeated avoidance rules *themselves* mechanically converge toward "editorial typography, whitespace, hairlines, lists, asymmetric grids, minimal decoration" — is **PLAUSIBLE but not directly confirmed** by this single benchmark. What *is* confirmed is that DIRECT's lack of a real alternative-exploration step (§2.3) and Genre's collapse to category stereotype (§2.1–2.2) are sufficient on their own to explain the convergence, without needing to indict Anti-Slop's negative-constraint structure itself. Do not weaken or restructure Anti-Slop into "constraint + positive direction" as a general redesign — CD-1/CD-2 already supply the positive-direction counterpart at the one place (DIRECT) where the evidence shows it was actually missing.

---

## 9. Responsive creative validation

**HERO-1** (§4) should be added as a new rule in `typography.md`, not folded into `anti-slop-registry.md` (it's a structural/technical defect, not a "current AI tell" that ages — matches that file's own stated scope split at its header) and not treated as a new validation *system* — it reuses `INTX-003`'s existing "mechanical-countable, rendered, Enhanced mode, check at required floor widths" validation pattern, applied to one additional element class (display/hero headlines) instead of only clickable text. This is the most concrete, lowest-risk, most directly evidence-backed change in this plan.

---

## 10. Files to change

- `SKILL.md` — §1 (DIRECT row: CD-1; VALIDATE row: VAL-1), §4 (Genre-inference anchor: CD-3; dial scope clarification: DENS-1), §5 (Rejected Directions requirement: CD-1, CD-2).
- `references/rule-catalog/typography.md` — new rule `TYPE-006` (HERO-1).
- `references/rule-catalog/layout-interaction.md` — new rule for imagery decision procedure (IMG-1); `LAYOUT-001` Medium-band clarification (VAR-1).
- `references/rule-catalog/color.md` — `COLOR-001` Medium-band clarification (VAR-1).
- `references/style-catalog.md` — populate the macrostructure-bundle catalog `LAYOUT-001` already references (DENS-1); no structural/schema change.
- `references/critique-protocol.md` — one new Level 2 trigger condition (CRIT-1); one sub-check added to Level 1 axis 1 (AS-1).
- `references/anti-slop-registry.md` — optional one-line cross-reference added to SLOP-011 pointing at where its cluster-level check now lives (AS-1) — content of the entry itself unchanged.

## 11. Files explicitly NOT to change

- `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md` — historical design documents, not runtime dependencies (per `SKILL.md`'s own header).
- `references/existing-project-safety.md` — untouched by every finding above.
- `references/gesture-physics.md` — untouched, out of scope.
- `references/rule-catalog/motion.md`, `references/rule-catalog/accessibility.md`, `references/rule-catalog/content-copy.md`, `references/rule-catalog/performance-hardening.md` — no finding in this benchmark implicates any rule in these four files; do not touch them in Phase 6.
- `AUDIT-3.5.md` — prior phase's report, historical record.
- Anything inside `design-excellence-benchmark/` (`brief.md`, `.design/context.md`, `*.html`, `css/`, `js/`) — the benchmark output itself; it is evidence, not something to correct in place. Any re-test (§14) runs as a fresh generation, not an edit of the existing output.
- The four existing Anti-Slop entries' own statements (SLOP-003, SLOP-011, SLOP-012) — their content is correct as written; only enforcement (VAL-1) and cluster-checking (AS-1) around them change.

---

## 12. Phase 6 implementation order

1. **HERO-1** (typography.md) — isolated, zero interaction with any other proposed change, directly reproduces a confirmed observed defect. Ship first to validate the change process on the lowest-risk item.
2. **VAL-1** (SKILL.md VALIDATE row) — enforcement-only change, no new rule content; makes every subsequent mechanically-countable rule (including HERO-1, once shipped) actually gate output.
3. **CD-3** (SKILL.md §4 Genre anchor) — smallest, single-sentence fix with the highest evidence confidence (§2.1/§2.2), independent of the others.
4. **CD-1 + CD-2** (SKILL.md §1 DIRECT row, §5 Rejected Directions) — ship together, since CD-2 is the check that makes CD-1's candidate-rejection reasoning trustworthy.
5. **AS-1** (critique-protocol.md Level 1 axis 1) — depends conceptually on CD-1/CD-2 existing (a cluster-check is more meaningful once DIRECT is actually producing/rejecting real alternatives), but is independently shippable.
6. **CRIT-1** (critique-protocol.md Level 2 trigger) — independent, ship any time after AS-1 for consistency of the critique-protocol edits in one pass.
7. **VAR-1** (color.md, layout-interaction.md Medium-band clarifications) — independent, low-risk, can ship any time.
8. **IMG-1** (layout-interaction.md new rule) — ship after CD-1 exists, since the imagery decision is naturally exercised during the same DIRECT pass that now produces real alternatives.
9. **DENS-1** (style-catalog.md bundle population, SKILL.md §4 scope line) — ship last; it's the only change requiring genuinely new content (5 bundle definitions) rather than a correction to existing content, and depends on IMG-1 existing for its cross-reference to be meaningful.

Do not batch all nine into one edit pass — each is independently testable, and the re-test in §14 should confirm each tier before the next lands, consistent with `SKILL.md` Core Principle 12 ("leverage over coverage").

---

## 13. Success criteria

A Phase 6 re-test succeeds if, on a re-run of the same benchmark brief:

1. **Genre inference** — `.design/context.md` records `genre: atmospheric-expressive` (or a different, explicitly-justified genre whose rejection rationale correctly cites `style-catalog.md`'s actual `best_for`/`keywords` text, not an assumed stereotype) — resolves CD-2/CD-3.
2. **Rejected Directions** — contains at least one genuine creative alternative beyond brief-mandated anti-pattern avoidances, with a rejection reason traceable to the style catalog's actual content — resolves CD-1.
3. **SLOP-011 cluster check** — the finished direction's color-anchor + typography + accent combination does not match any of SLOP-011's four named clusters without an explicit, declared exception in Known Exceptions — resolves AS-1.
4. **SLOP-003 eyebrow ratio** — mechanically verified (count ≤ `ceil(sectionCount/3)`) before SHIP, not just theoretically checkable — resolves VAL-1.
5. **Mobile hero headline** — no single-word orphan on the final line at any declared breakpoint — resolves HERO-1.
6. **Imagery decision** — `.design/context.md` records an explicit answer to IMG-1's four questions, even if the answer is "no imagery, because X" — resolves IMG-1.
7. **Independent critique** — for this specific brief (greenfield, multi-page, explicit "premium" brand-quality bar), a Level 2 critique record exists — resolves CRIT-1.
8. **Human evaluation (qualitative, not mechanically gated)** — a fresh visual read no longer describes the result primarily via "too much empty space," "recurring alignment-rule motif," "no imagery," or "safe editorial." This is the outcome all of 1–7 are instrumental toward, and should be assessed by a fresh (non-generating) reviewer, per the same isolation principle `critique-protocol.md` already uses for Level 2.

Do not treat 1–7 as sufficient on their own without 8 — mechanical compliance with the new rules is necessary but the command's own diagnosis (§1) was a human visual judgment, and the re-test's final gate should be too.

---

## 14. Benchmark re-test

Exact re-run procedure:

1. Re-create a fresh working directory (do not edit `design-excellence-benchmark/` in place — per §11, that folder is evidence). Symlink the corrected skill package the same way the original benchmark did (`.claude/skills/design-excellence` → the skill package).
2. Re-run `brief.md` verbatim, unchanged — no modification to the brief between benchmark runs, so the comparison is isolated to the skill's behavior.
3. Capture the same artifacts as the original run for direct comparison: `.design/context.md` (register/genre/dials/Rejected Directions), rendered screenshots at 1440px and 390px for at minimum the home page (the page that exposed both the SLOP-011 cluster and the hero orphan defect).
4. Score against §13's 8 criteria in order; stop and report if any of 1–5 fails outright (mechanical, unambiguous) before proceeding to the qualitative pass (8).
5. For criterion 8, dispatch a fresh-context reviewer (per `critique-protocol.md`'s own isolation mechanism — a genuinely new agent, not a fork of the session that ran the re-test) with only the rendered screenshots and the original brief, blind to the Phase 6 changes, and ask the same open question the original human evaluator effectively answered: does this feel like a distinctive, considered visual identity, or a safe/generic one.
6. Report results per-criterion, not as a single pass/fail — a partial success (e.g., genre correctly inferred but imagery still absent by a defensible, stated choice) is a legitimate outcome, not a failure, provided the decision was actually evaluated rather than defaulted.
