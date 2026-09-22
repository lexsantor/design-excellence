# Phase 6.5 — Behavioral Benchmark Results

No files modified. All five cases run against the current `SKILL.md` / `layout-interaction.md` / `visual-references.md` / `critique-protocol.md` / `style-catalog.md` as implemented.

---

## Case 1 — Explicit Concept

1. **Routing:** multi-page-site BUILD on a genuinely-empty project (5 pages, no existing files).
2. **Register/Genre/Dials:** hybrid register (brand identity + one conversion goal); editorial genre — evidence-traceable from "professional, trustworthy, calm... premium without being pretentious" against `style-catalog.md`'s own keywords, not a healthcare-vertical stereotype. `DESIGN_VARIANCE` Medium (~6), `MOTION_INTENSITY` Low (Genre default — this trimmed brief doesn't explicitly ban decorative motion the way the original full brief did, so the rationale here is Genre-default, not brief-stated, worth being precise about), `VISUAL_DENSITY` Medium-low (~4, "calm" is direct brief evidence).
3. **Concept status: DETECTED / EVIDENCED.**
4. **Why:** the brief's own text states the naming rationale ("Atlas is named after the C1 vertebra because...") **and** explicitly requests embodiment ("The brand should express this idea... throughout the experience"). Passes the bright-line test twice over — both clauses are literally in the brief.
5. **LAYOUT-009 activates: YES.**
6. **Candidates:**
   - **A — "Anchored Datum"** (pure concept-derived, no reference): fixed hairline-anchored nav + one hairline rule as the only divider language, site-wide. Organizing surfaces: macrostructure + navigation.
   - **B — "The Reference Line"** (concept-derived **and** reference-informed): content architecture organizing surface — each page opens with an identical short "aligned around Atlas" reference point before diverging; navigation reframed via `REF-003` as a bounded numbered index (01 Home … 05 Contact). Organizing surfaces: content architecture + navigation.
   Differ on ≥2 dimensions (navigation, content architecture); each carries the concept on a different organizing surface, satisfying `LAYOUT-009`.
7. **Considered:** all 9 entries checked against hybrid/editorial/Low-motion/Medium-variance.
8. **Rejected:** `REF-002`, `REF-006` (Medium-High motion requirement vs. Low `MOTION_INTENSITY`); `REF-005` (fabrication risk — brief explicitly bans invented credentials/photos, so no real process material exists to photograph); `REF-007` (genre mismatch — modern-minimal/playful, not editorial); `REF-008` (register+genre mismatch, and its own `do_not_apply_to` names "brand-led marketing/landing content" directly); `REF-009` (`do_not_apply_to`: "primary scrolling page content" — exactly what this is).
9. **Adopted:** `REF-003`, into Candidate B. Candidate A uses zero references.
10. **Priority order verified:** compatibility eliminated `REF-007`/`REF-008` first; applicability eliminated `REF-002`/`REF-005`/`REF-006`/`REF-009`; `REF-003` won outright on "materially different possibility" against the one remaining comparable entry (`REF-001`) — the family tie-breaker was **never invoked**, correctly, because there was no tie.
11. **Optional/not forced:** confirmed — Candidate A carries zero references.
12. **No style preset/literal copying:** confirmed — no candidate is named after a movement; `REF-003`'s own `non_application_note` (don't copy its numbering typography) is honored.
13. N/A (not POLISH).

**Result: PASS.**

---

## Case 2 — Brand Name Only

1–2. Identical to Case 1 (Register/Genre/Dials don't depend on the concept paragraph, and `SKILL.md` says so explicitly).
3. **Concept status: HYPOTHESIS.**
4. **Why:** the brief supplies zero rationale for "Atlas" — no sentence to point at. But "Atlas" is a real, checkable name (the C1 vertebra; also the mythological Titan) — exactly the class of association `SKILL.md`'s HYPOTHESIS clause describes. Declared: *"Atlas plausibly references the C1 vertebra / the Titan; the brief does not state this, so it is a hypothesis, not evidence."* This is the precise case Phase 6.5 exists to correct — the same name, same underlying fact, that was wrongly promoted to DETECTED in the original Phase 6.3/6.4 runs is here correctly held at HYPOTHESIS because *this* brief withholds the rationale.
5. **LAYOUT-009 activates: NO.**
6. **Candidates** (unconstrained by the hypothesis — neither is required to translate it):
   - **A — "Editorial Calm":** Editorial genre's own default posture, undifferentiated by any concept.
   - **B:** `REF-003`'s bounded index nav, adopted purely as a navigational possibility for a small closed 5-page site — same compatibility reasoning as Case 1, but here explicitly *not* logged as concept-derived.
   Distinct on navigation + macrostructure/color-anchor.
7–9. Same reference set considered; `REF-003` adopted into Candidate B, independent of the hypothesis; same rejections as Case 1.
10. Priority order applies identically to Case 1.
11. Confirmed — Candidate A carries zero references.
12. Confirmed.
13. N/A.

**Result: PASS.** This is the single most important case, and it behaves correctly: bare name → HYPOTHESIS, not DETECTED; `LAYOUT-009` does not fire; DIRECT proceeds unaffected.

---

## Case 3 — Generic Brief

1. **Routing:** multi-page-site BUILD, genuinely-empty (5 pages).
2. **Register/Genre/Dials:** hybrid-leaning-product-led register ("explain services... answer common questions... request an appointment" is utility language, not brand storytelling); Genre modern-minimal — "trustworthy, clear, modern, easy to use" maps directly onto `style-catalog.md`'s own modern-minimal keywords, not editorial's. `DESIGN_VARIANCE` Low-Medium (~3–4, genuinely borderline), `MOTION_INTENSITY` Low-Medium, `VISUAL_DENSITY` Medium (no density signal given, default).
3. **Concept status: NOT DETECTED.**
4. **Why:** no name, no rationale, no recurring object — nothing even exists to form a hypothesis *about*. Cleaner than Case 2, which at least had a real name to hypothesize from.
5. **LAYOUT-009: NO.**
6. **Candidates** (Register/Genre/Dials alone):
   - **A — "Clear Service Grid":** scannable service grid, accordion FAQ, tight neutral palette.
   - **B — "Single-Column Trust Flow":** narrower sequential single-column path (services → team → FAQ → booking), wider whitespace, warmer neutral.
   Distinct on macrostructure, density treatment, color-anchor warmth.
7. **Considered:** genre-filtering does real work here — all six editorial-coded entries (`REF-001`–`006`) are excluded at compatibility (wrong genre). `REF-007` and `REF-008` pass compatibility (product-led/modern-minimal both match); `REF-009` passes on its broad `compatible_with`.
8. **Rejected:** `REF-007` — genuinely borderline, judged against its own `do_not_apply_to` ("Low `DESIGN_VARIANCE` product-led context where a second color system would compete with existing tokens") at the ~3–4 boundary; `REF-008` — `do_not_apply_to` excludes "brand-led marketing/landing content whose entire job is persuasion before commitment," which this is; `REF-009` — considered but not clearly better than the default for a short 5-page brochure site.
9. **Adopted: none.** Both candidates ship reference-free.
10. Priority order verified — this case is the clean demonstration of "considered, then judged unnecessary" as a fully valid, non-degenerate outcome.
11. Confirmed by construction (zero adopted).
12. Confirmed.
13. N/A.

**Result: PASS.** Directly answers the brief's own question: the system produces genuinely differentiated candidates without inventing a concept or forcing a reference.

---

## Case 4 — Product-Led Dashboard

1. **Routing:** page-scope BUILD, genuinely-empty (one dashboard surface).
2. **Register/Genre/Dials:** product-led (explicit — "product-led dashboard," "avoid decorative marketing patterns"); modern-minimal, near-verbatim match to the brief's own words ("speed, clarity, task completion"). `DESIGN_VARIANCE` Low (register ceiling). `MOTION_INTENSITY` Low-Medium (state-feedback only). `VISUAL_DENSITY` High — five simultaneous live widgets need efficient information density, not generous spacing.
3. **Concept status: NOT DETECTED.**
4. **Why:** purely functional brief, no name/metaphor material at all.
5. **LAYOUT-009: NO.**
6. **Reference compatibility:** all six brand-led entries (`REF-001`–`006`) excluded at compatibility (wrong register). `REF-007` passes register+genre compatibility — **but fails applicability**: its `do_not_apply_to` names "a Low `DESIGN_VARIANCE` product-led context where a second color system would compete with existing tokens," and a logistics dashboard already needs its own color-coded state/severity system (on-time/delayed/exception) that `REF-007`'s color-as-navigation principle would directly collide with. Correctly excluded on substance, not by reflex. `REF-008` and `REF-009` both pass compatibility+applicability cleanly — `REF-008` in particular matches its own best-fit description almost exactly ("content organized for someone already committed to a task," which is precisely what an ops dashboard is).
7. **Candidates:**
   - **A — "Status-First Grid":** conventional modern-minimal dashboard, uniform widget-card grid, color reserved strictly for state/severity.
   - **B — "Mid-Task Console"** (`REF-008`-informed): no header/hero framing at all — the exception queue and today's tasks are the first visible content, structured as a state-tracker; status/alerts/search become secondary.
   Distinct on information hierarchy, macrostructure, interaction model.
8. **Rejected:** `REF-007` (applicability — competing color system, reasoned above), `REF-009` (considered as a secondary influence on individual widget tiles, but not the deciding factor at the whole-surface level — genuinely useful but less materially distinguishing than `REF-008`'s hierarchy-level effect).
9. **Adopted:** `REF-008`, into Candidate B, selected as the committed direction (best match to "prioritize speed, clarity, task completion").
10. **Priority order verified**, and critically: **does the shipped UI look like a laboratory?** No — per `LAYOUT-010`'s Adapt step and `REF-008`'s own `non_application_note` (bars copying tolerance-field iconography/instrument styling), only the *hierarchy principle* transfers, not the source's visual skin. The dashboard still uses ordinary cards/tables/badges. This directly satisfies the specific test the brief asked for.
11. Confirmed — Candidate A carries zero references and remains a fully viable, non-strawman alternative.
12. Confirmed.
13. N/A.

**Result: PASS.**

---

## Case 5 — Existing Project + POLISH

1. **Routing:** component-scope POLISH on an existing project ("without changing the established visual identity" is textbook POLISH language).
2. **Register/Genre/Dials:** not re-derived — DEFINE does not run; existing values are read from `.design/context.md` at INSPECT (cache-read only) as inherited context, not freshly classified.
3. **Concept status: N/A** — concept detection is nested inside "when DEFINE runs" (`SKILL.md` §1's opening clause); DEFINE never runs here, so the stage that would produce a status simply doesn't execute. Not "NOT DETECTED" (that's a DEFINE-time output) — genuinely inapplicable.
4. **Why:** Hard rule, `SKILL.md` §1 — component-scope POLISH has no path into DEFINE at all.
5. **LAYOUT-009: does not activate** — no path into DIRECT either, same Hard rule.
6. **DIRECT/EXPLORE: does not run.** No candidates generated.
7–9. **Visual References: not loaded, not considered, none adopted.** `visual-references.md`'s T3 trigger is "DIRECT/DESIGN stage... only," and neither runs.
10. Not exercised — nothing to select from.
11. Trivially satisfied — non-loading is the strongest form of "not forced."
12. N/A — no new design decision is made; the task explicitly forbids one.
13. **Explicit checklist, all confirmed:** Task Mode = POLISH ✓; DEFINE skipped ✓; DIRECT skipped ✓; SHAPE skipped ✓ (its own trigger requires page/multi-page BUILD/REDESIGN or a new-section BUILD — neither applies); DESIGN skipped ✓; Visual References not loaded ✓; concept detection not run ✓; fingerprint check skipped ✓ (`SKILL.md` §6 states this explicitly for component/section POLISH); task stays narrow ✓ (VALIDATE scoped to touched area, CRITIQUE floor-only, HARDEN skipped).

**Result: PASS.**

---

## 1. Behavioral result

| Case | Concept | LAYOUT-009 | Visual References | Routing | Result |
|---|---|---|---|---|---|
| 1 | DETECTED / EVIDENCED | Activates | Considered 9, `REF-003` adopted | multi-page BUILD, genuinely-empty | **PASS** |
| 2 | HYPOTHESIS | Does not activate | Considered 9, `REF-003` adopted (unaffected by hypothesis) | multi-page BUILD, genuinely-empty | **PASS** |
| 3 | NOT DETECTED | Does not activate | Considered `REF-001`/`007`/`009`, none adopted | multi-page BUILD, genuinely-empty | **PASS** |
| 4 | NOT DETECTED | Does not activate | `REF-007` excluded (applicability), `REF-008` adopted, `REF-009` secondary | page BUILD, genuinely-empty | **PASS** |
| 5 | N/A (DEFINE doesn't run) | Does not activate (no path) | Not loaded | component POLISH, existing project | **PASS** |

## 2. Critical findings

**Regressions:** none.

**Unexpected behavior:** none that breaks a rule — but see the coverage gap below.

**Ambiguity (genuine, disclosed, not a defect):**
- Case 3's `DESIGN_VARIANCE` sits right at the Low/Medium boundary that governs whether `REF-007` is excluded — a differently-reasoned run could legitimately adopt it instead. Inherent to `LAYOUT-010`'s deliberately qualitative design, not a bug.
- HYPOTHESIS's "real, checkable" bar (Case 2) has no verification mechanism beyond the model's own judgment — an accepted, disclosed limitation, same class as `LAYOUT-010`'s own selection judgment.

**Architecture problems:** none found.

**Implementation problems:** none found — every rule needed (bright-line concept test, `LAYOUT-009` applicability, `LAYOUT-010`'s 4-step priority, POLISH exclusion chain) executed unambiguously as written.

**Coverage gap (important, not a defect):** the family-diversity tie-breaker was **never actually invoked** in any of the 5 cases. In every case where a reference was adopted, it won outright at step 3 ("materially different possibility") — no case produced a genuine tie between two comparably-strong entries from different families. The tie-breaker's secondary status was verified *structurally* (the rule text gates it correctly behind steps 1–3) but not verified *behaviorally*. A 6th case engineered specifically to produce a step-3 tie would be needed to actually exercise it.

## 3. Most important question

**A. Does explicit concept evidence activate Concept → Structure?** Yes — Case 1, cleanly.
**B. Does a brand name alone remain only a hypothesis?** Yes — Case 2, the exact governance gap Phase 6.4 found is directly reversed.
**C. Does the new pool broaden possibilities without forcing references?** Partially confirmed — Case 4 shows real, substantive broadening (`REF-008`) with a fully viable zero-reference alternative; Case 3 shows correct non-adoption. But only `REF-008` was ever actually *adopted* across all 5 cases; `REF-007` was only ever a rejection, `REF-009` only ever secondary. Two of the three new entries were never the deciding factor.
**D. Does the family-diversity tie-breaker remain genuinely secondary?** Structurally yes; **behaviorally unexercised** — see coverage gap above.
**E. Does POLISH remain narrow?** Yes — Case 5, full exclusion confirmed, no regression.

## 4. Recommendation

**READY FOR NEXT PHASE.**

No defect was found that would justify "MINOR FIX" or "MAJOR FIX" — every rule performed exactly as specified across all 5 cases, and the two headline Phase 6.5 objectives (A and B) are cleanly confirmed. The one caveat is a benchmark-coverage gap, not an implementation problem: the family-diversity tie-breaker (D) and two of the three new catalog entries (`REF-007`, `REF-009` as *adopted* choices, not just rejections) remain structurally correct but behaviorally untested. Recommend a follow-up case specifically engineered to produce a genuine step-3 tie before treating D as fully validated — a targeted addition to the benchmark suite, not a fix to the skill.
