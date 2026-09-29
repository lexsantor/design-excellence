# Comprehensive Pre-Test Skill Readiness Audit — Results

**Status:** COMPLETED. Read-only audit; no correction was made.
**Authorization:** human authorization recorded verbatim in `STATE.md` (2026-09-27), "Autorizo Comprehensive Pre-Test Skill Readiness Audit. …". It allows one report plus operational `STATE.md` updates. It forbids changes to `SKILL.md`, `loop.md`, the Integration Contract, the Rule Catalog, the Principle Pool and T2/T3/T4 governance, as well as reference acquisition, new benchmarks, runtime architecture changes, refactoring and push.
**Repository state audited:** HEAD `a8ef950`, plus the uncommitted `STATE.md` authorization record.
**Delegation:**
- 2 read-only operational subagents with non-overlapping areas: A (routing, pipeline, reachability) and B (Rule Catalog, authority, tiers, critique, context, provenance).
- The main agent audited area C (loop, state, installation, documentation, first-run risks) and did all synthesis.
- 1 `loop.md` §8 reviewer (§11 of this report).
- That makes 3 subagents, within the `loop.md` §9 cap of 3 including the reviewer. The authorization allowed "hasta 3 subagentes operativos" plus a §8 review, which could be read as 4. The conservative reading was applied.

**Classes.**
- **A** confirmed defect;
- **B** probable execution risk;
- **C** documentation/clarity issue;
- **D** intentional design decision;
- **E** not assessable from current evidence;
- **P** test precondition: a setup or governance condition outside the skill text, added on reviewer advice (§11).

A finding is **A** only when the repository text itself proves the defect: a missing target, a contradiction, or an impossible instruction. How a session will *behave* because of it is **B** unless runtime evidence exists.
- Every quote was read in the file cited.
- ✓ marks findings the main agent re-verified first-hand.
- The §8 reviewer independently re-verified every A finding and eight B findings (§11).
- Subagent working notes are disposable and are not committed.

---

## 1. Executive Readiness Summary

**Answer to the milestone question.**

> *Could a fresh Claude Code session now use this skill on a real project and follow the intended system reliably enough to begin meaningful end-to-end testing, and what would most likely break first?*

**Not yet on a typical real project. Yes, after two test preconditions and two targeted specification decisions (§10 MUST FIX).**

**What the runtime evidence covers:**
1. **Greenfield BUILD on a plain stack**, the best-supported path (Phase 7 01–05, 7.6, 7.7).
2. **Component- and section-scope BUILD, and component-scope POLISH, on existing projects, completed end to end.**
   - The committed overlay benchmarks (`OVERLAY-FOCUS-BEHAVIOURAL-BENCHMARK-RESULTS.md` §3; `OVERLAY-FOCUS-COVERAGE-EXPANSION-RESULTS.md` §4–§5) contain 5 completed BUILD runs and 1 completed POLISH on existing projects.
   - In them, fresh builders modified the project and ran VALIDATE and Level 1.
   - Their prompts were ordinary client requests plus "follow the skill's pipeline; read only the skill's files". There was no "do not modify" scaffolding.
3. **Page-scope bounded-profile runs** in Phase 9.2, which were scaffolded ("do not modify", read-only skill directory, "stop and ask") and partial: "No PASS claim … for any scenario".

**What it does not cover:** every one of those existing-project fixtures already had a filled `.design/context.md`, and all were plain HTML/CSS/JS or vanilla/Vite. Never exercised:
- an existing project **without** `.design/`;
- a framework or package-manager stack;
- T4 sources as real dependencies ("never operationalized", `PHASE-7.7-RESULTS.md` l.158);
- completed CRITIQUE, AUDIT or DISCOVER deliverables;
- the bounded implement route (R3).

**What would most likely break first, derived from the findings:**
1. **The skill is not found (PT-01, test precondition).**
   - Its only registration is an untracked, gitignored project-level junction inside this repository (`.gitignore` l.17–18).
   - It is absent from the user-level skill folders; the reviewer confirmed this independently.
   - A session opened in an external project will not load it.
2. **A competing design skill may answer instead (PT-60, B).** About 30 design skills with overlapping descriptions are installed at user level, including impeccable and lexia-design. Once PT-01 is fixed, a terse prompt may trigger a different skill.
3. **A POLISH, CRITIQUE or AUDIT on an existing project with no `.design/` follows under-specified instructions (PT-02, A).**
   - POLISH prescribes `INSPECT(cache read only)` when no cache exists, while `existing-project-safety.md` makes the scan mandatory.
   - The DEFINE row's POLISH clause is ambiguous against the POLISH row and the Hard rule.
   - Nothing says where POLISH gets register, genre, dials or Product Truth when they are absent.
   - BUILD-existing and REDESIGN are better covered, because "DEFINE(reuse if present)" and safety §4 imply a bootstrap.
4. **On a framework stack, the session may try to create a stack file inside the skill package (PT-03, A).**
   - The T4 row places stack files in `references/stacks/*.md`, a directory that does not exist, and no template exists.
   - Whether a write reaches this governed repository depends on how the skill is installed.
5. **Level 1 critique may score what it cannot check (PT-05, PT-06, PT-59).**
   - SLOP-011 cannot be loaded under T3 on BUILD-existing.
   - Whether `accessibility.md` is loaded rests on interpretation.
   - Level 1 has no not-assessable option.

**No finding shows the architecture to be unsound.** Authority layering, the Principle Pool and visual-reference provenance boundaries, the implementation-only status of the T4 sources, the Replace gate and `CRITIQUE(floor)` / `(floor only)` all hold (§8, D items). The defects are specification gaps and contradictions at the edges real projects hit first.

**Counts** (after de-duplication and reviewer reconciliation):

| Class | Count |
|---|---|
| A | 10 |
| B | 20 |
| C | 26 |
| D | 16 |
| E | 10 |
| P | 2 |

## 2. Confirmed Defects (A)

Fields: ID · location · condition · why it matters in a fresh real-project run · evidence · confidence · scope · blocks first test? · follow-up.

| ID | Location | Observed condition | Why it matters | Evidence | Conf. | Scope | Blocks? | Follow-up |
|---|---|---|---|---|---|---|---|---|
| **PT-02** ✓ (RA-01, RA-02, RA-05, RB-11) | `SKILL.md` l.21, l.32, l.34, l.73, l.146–150; `existing-project-safety.md` l.5–7, l.16, §5 | POLISH = `INSPECT(cache read only)` though no `.design/preflight-cache.json` exists on first contact, while the safety file makes the scan "mandatory, before any design decision". The DEFINE row "skip if POLISH and `.design/context.md` already has register/genre/dials" is **ambiguous**: it reads as allowing POLISH→DEFINE when context is absent, against l.73 and the Hard rule (l.32). §5 defines `context.md` creation only for Greenfield; Polish is "read, but do not write unless…". Safety §5 diffs against a Constraints list that may not exist. BUILD-existing ("DEFINE(reuse if present)", l.71, with l.104 "stored in `.design/context.md`") and REDESIGN (safety §4) do imply a bootstrap | POLISH, CRITIQUE and AUDIT on the default state of a real external project must guess whether to scan, whether to write `.design/`, and whether to run DEFINE. Dial-band rules (COLOR-001, LAYOUT-001/007, MOTION-002) and Level 1 Genericness have no inputs | quotes as listed; every existing-project fixture had a filled `.design/context.md` (Phase 6.5 Case 5; 9.2 fixtures; both overlay benchmarks) | high (text); medium (behaviour) | POLISH, CRITIQUE, AUDIT / INSPECT, DEFINE, CRITIQUE | **yes**, conditionally: if the first test is a POLISH, CRITIQUE or AUDIT on a project without `.design/` | targeted specification correction: the no-context bootstrap for POLISH, CRITIQUE and AUDIT |
| **PT-03** ✓ (RC-02, RA-09, RB-13) | `SKILL.md` l.179, l.185; `loop.md` §2 | Stack files are placed in `references/stacks/*.md` inside the skill package; "A stack file is created the first time this skill runs inside a project with real evidence of that stack"; no template; directory absent. `loop.md` §2 requires human authorization before "adding … runtime knowledge in `design-excellence/`" | The first framework project may trigger creation of an unspecified file inside the skill package. Where the skill is installed as a junction to this repository, that write lands in the governed repo. l.185 could alternatively mean that maintainers author the file on first evidence; either way no location, owner or template is specified | quotes; `PHASE-7.7-RESULTS.md` l.143 "any `references/stacks/*.md` (no stack evidence)"; 9.2 harness declared the skill directory read-only; no benchmark had stack evidence. (The earlier citation of l.100/l.191 as contradictions was withdrawn: l.100 limits what a P2 instruction authorizes, and l.191 concerns untrusted content; reviewer R-02) | high (text gap); medium (write occurs; depends on install) | all modes on stack projects / INSPECT, T4 | **yes**, conditionally: on any framework-stack test with a writable, repo-linked skill | specification correction (location, owner, template, or declare deferred) **or** a test guard (read-only skill directory) |
| **PT-05** ✓ (RA-11, RB-04; narrowed) | `critique-protocol.md` l.9; `SKILL.md` l.8, l.183 | Level 1 axis 1 requires SLOP-011's named clusters, but T3 loads `anti-slop-registry.md` only in CRITIQUE/AUDIT mode, at DIRECT/DESIGN with a new system, or for genericness-themed requests. l.8 forbids reading unlisted references | On BUILD-existing and plain POLISH, a mandatory Level 1 check cannot be performed without breaking the loading rule | quotes as listed | high | BUILD-existing, POLISH / CRITIQUE L1 | no | targeted clarification (Level 1 loads SLOP-011 where axis 1 applies) |
| **PT-10** ✓ (RB-01) | `accessibility.md` l.12–15 vs l.87–95 | A11Y-001 is P1 "because it matches contrast" but embeds `web-target-size` 24×24, focus-not-obscured, consistent-help and redundant-entry, universally. A11Y-005 sets the same 24×24 at P5, touch-only, "Do not apply to a mouse-driven desktop dashboard" | Non-contrast criteria reach P1 (which may override the user under §3); direct contradiction on target size | quotes; `SKILL.md` l.96 enumerated P1 list | high | all / VALIDATE, CRITIQUE | no | Rule Catalog correction milestone |
| **PT-12** (RB-02) | `motion.md` l.22 vs `kinetics.md` l.40, l.84 | Kinetics restates a "MOTION-002 vocabulary" that adds "hierarchy/reveal" and "orientation" | Lets decorative motion pass the purpose gate when Kinetics is loaded | quotes (agent B; reviewer confirmed) | medium-high | BUILD with motion / DESIGN, BUILD | no | T4 consistency correction |
| **PT-13** (RB-03) | `motion.md` l.44, l.50–51 | MOTION-004's remediation (`grid-template-rows: 0fr→1fr`) animates a layout property the rule forbids; its mechanical check does not flag it | Remediation produces a violation | quotes (agent B; reviewer confirmed) | medium | motion / BUILD, VALIDATE | no | Rule Catalog correction |
| **PT-14** (RB-05) | `color.md` l.53–60 | COLOR-006 gates SHIP but depends on a per-industry default-palette pool and named alternatives that exist nowhere | Unexecutable gate; the session must invent data | absence verified (agent B; reviewer confirmed) | medium-high | DESIGN, VALIDATE | no | Rule Catalog correction |
| **PT-15** (RB-06) | `layout-interaction.md` l.15 | LAYOUT-001 says its named page-structure bundles live in `style-catalog.md`; that file has none | Dead reference | absence verified (reviewer confirmed) | high | DESIGN | no | documentation/catalog correction |
| **PT-16** (RB-07) | LAYOUT-007 (§6 for §4); A11Y-001 "see COLOR-005" (COLOR-003/004 intended); `style-catalog.md` l.7 `do_not_apply_to` vs schema `do_not_use_for`; PERF-002 `preload="metadata"` on an image | Four wrong cross-references or attributes. The first two are misdirections closer to C (reviewer MINOR); kept here as one grouped A because the last two are outright wrong | Misdirection; PERF-002's attribute has no effect on images | quotes (agent B; reviewer confirmed) | high | various | no | catalog clean-up |
| **PT-17** ✓ (RA-04 part) | `SKILL.md` l.72 vs `critique-protocol.md` l.22 | SKILL: REDESIGN "CRITIQUE escalates to Level 2 by default", with no scope; protocol: "Task Mode = REDESIGN at page/multi-page-site scope" | Section-scope REDESIGN gets Level 2 under one file and not the other | quotes verified | high | REDESIGN section / CRITIQUE | no | routing clarification |

**Test preconditions (P).** These are not defects in the skill text (reviewer R-06), but meaningful testing depends on them.

| ID | Condition | Evidence | Blocks? | Follow-up |
|---|---|---|---|---|
| **PT-01** ✓ (RC-01) | The skill is registered only through an untracked, gitignored project-local junction in this repository. It is not in `~/.claude/skills` or `~/.agents/skills`; plugin folders were searched by the main agent only | `git ls-files .claude` empty; `.gitignore` l.17–18 "Local Claude skill junction"; reviewer confirmed both user skill folders | **yes**: a session in an external project cannot load it | test-setup step (install at user level or in the test project) |
| **PT-04** ✓ (RC-08) | `loop.md` §2 covers "disposable work copies outside both repositories"; it does not cover writing into a real external project | §2 text | **yes**, as a decision: if testing runs as a loop milestone, writes into a real project need explicit authorization naming it, or the test must use a disposable copy | human decision before testing |

## 3. Execution Risks (B)

| ID | Location | Condition | Why it matters | Evidence | Conf. | Scope | Blocks? | Follow-up |
|---|---|---|---|---|---|---|---|---|
| **PT-06** (RB-08, RB-09 narrowed ✓) | `critique-protocol.md` l.7 vs l.32; `SKILL.md` l.56 | Level 1 must "Score six axes 1–5". Only axis 3 has a "where in scope" exemption; a general not-assessable option exists only for Level 2. Several mechanical checks need rendering without saying so (COLOR-001/004 area, TYPE-003 measure, A11Y-001 pairs, PERF-001 INP). "Enhanced" is defined only inline as "Enhanced/browser-rendering capability" | Paths to invented scores or to checks reported as run that could not run, on screenshot, no-render and directions-only runs | quotes; Gap Discovery C2 records a prior instance; 9.2J scored "n/a (not built)" unprompted | medium | CRITIQUE, VALIDATE | no, but it distorts test evidence | clarification: Level 1 N/A rule; capability tags on rules |
| **PT-07** (RA-06) | `existing-project-safety.md` l.3, l.7; `SKILL.md` l.74–76 | AUDIT, CRITIQUE, DISCOVER and directions-only may write `.design/preflight-cache.json`; no exemption | A read-only audit creates files in the user's repo | R6/R7 decision logs: avoided only because the prompt forbade writes (reviewer confirmed) | medium | read-only modes / INSPECT | no | clarification |
| **PT-08** (RB-10) | `SKILL.md` l.56 vs §3 P2/P4 | Every mechanical-countable rule gates SHIP with no P2 (user instruction) or P4 (existing system) exemption; only SLOP-004 states one. §3's "P2 wins" offers a resolution, so this is slightly inflated (reviewer) | P5–P8 rules (TYPE-001, COLOR-005, INTX-001, SLOP-001) may act as blockers against explicit user or existing-system choices | quotes (agent B) | low-medium | VALIDATE / SHIP | no | authority clarification |
| **PT-09** (RB-17) | `content-copy.md` l.26, l.32 | P1 CONTENT-003 keys on data "the user didn't supply" | Real figures and names already in an existing site may be treated as fabricated and replaced by placeholders. The reviewer judged this under-weighted, given the existing-project work above | quotes (reviewer confirmed) | medium-high | existing projects / BUILD, POLISH | no | clarification (existing content counts as supplied) |
| **PT-11** (RB-14) | `reicon.md`, `kinetics.md`, `smoothui.md` | No verified package names, install steps or APIs ("none of that is verified", `reicon.md` l.5); Reicon is the default icon source | A guessed install could add a wrong or unsafe dependency to a real repo | quotes (reviewer confirmed) | medium | BUILD with icons, motion or components / T4 | no | T4 verification, or a "confirm before install" rule |
| **PT-18** (RA-03) | `SKILL.md` l.64, l.70–72 | BUILD vs REDESIGN is undecidable for a new surface in an existing project; the identical R2 prompt was classified REDESIGN once and BUILD twice | Changes AUDIT stage, safety §4 and Level 2 by wording | `PHASE-9.2D-RERUN-RESULTS.md` l.79 (untracked `scratchpad/`; reviewer confirmed) | high | BUILD/REDESIGN | no; hurts comparability | routing clarification |
| **PT-19** (RA-04) | `SKILL.md` l.22–23, l.34, l.48 | Section-scope REDESIGN and section-scope "directions" have no route (DIRECT, SHAPE and profiles are page-only) | Common requests ("rework the hero") force guessing | quotes | medium-high | section scope | no | routing clarification |
| **PT-20** (RA-07) | `SKILL.md` l.28, l.71, l.73; protocol l.16 | REFINE absent from the BUILD-existing and POLISH rows; no revision loop or cap, though Level 1 escalation needs "two consecutive revision passes" | The one automatic Level 2 trigger cannot be evaluated; loops are improvised | quotes; 06R improvised fixes | medium | BUILD-existing, POLISH | no | routing clarification |
| **PT-21** (RA-08) | protocol l.21 vs l.26 | "Production-facing" has no threshold; any one trigger suffices; yet "do not run Level 2 by default for BUILD at component/section scope" | Real repos may trigger Level 2 on every component build, or inconsistently | quotes | medium | CRITIQUE L2 | no | clarification |
| **PT-22** (RA-10) | `SKILL.md` l.60–78 | No rule for compound requests ("audit and fix") | One half silently dropped | — | medium | AUDIT/CRITIQUE + BUILD | no | routing clarification |
| **PT-23** (RA-12) | `SKILL.md` l.19, l.64, l.74; protocol l.5–7 | Critique of a screenshot with no code has no Project State; rubric is self-critique-shaped | Output shape and INSPECT behaviour improvised | quotes | medium | CRITIQUE | no | clarification |
| **PT-24** (RA-13) | `SKILL.md` l.20, l.66, l.74–76 | AUDIT and DISCOVER content and output format undefined; CRITIQUE vs AUDIT vs DISCOVER split by verb only; no deliverable ever observed | Improvised report shape; different critique depth by wording | R4 "Findings count: not delivered" | medium | AUDIT, CRITIQUE, DISCOVER | no | clarification plus completed-run benchmark |
| **PT-25** (RA-14; corrected) | `PHASE-7-CROSS-PROJECT-ANALYSIS.md` l.534; `FINAL-SKILL-COMPLETION-RESULTS.md` l.272 | Routing reported "6/6", "Incorrect pipeline routing: none" | Phase 7's 6/6 covers 5 empty BUILDs and 1 REDESIGN. The overlay benchmarks since add component/section BUILD and component POLISH on existing projects (with `.design/`), but CRITIQUE, AUDIT, DISCOVER, the implement route and no-`.design/` projects remain unvalidated | quotes; overlay benchmark §3/§4 | high | test planning | no | treat the uncovered routes as unvalidated |
| **PT-26** ✓ (RC-03) | benchmarks (all) | No run on a framework or package-manager project; T4 never real dependencies | Stack detection, existing component systems and T4 install paths are untested | Phase 7-01…05 "no build step"; 06R vanilla/Vite; overlay benchmarks plain HTML; `PHASE-7.7-RESULTS.md` l.158 (reviewer confirmed) | high | all real stacks | no | test plan |
| **PT-27** (RB-12) | `existing-project-safety.md` l.9 | An existing `.design/context.md` "supersedes" the code scan; no staleness or `schema_version` check | A stale or foreign `.design/` (another tool) steers decisions | quote | medium | existing projects / INSPECT | no | clarification |
| **PT-28** (RB-15) | protocol l.31, l.33 | Level 2 reviewer brief lists rule ids without file paths; preferred external critics bring their own rubric | A fresh reviewer cannot resolve ids | quotes | medium | CRITIQUE L2 | no | clarification |
| **PT-29** (RB-16) | `SKILL.md` §1/§7 | AUDIT and DISCOVER have no defined path to the accessibility rules that say they apply in AUDIT | Accessibility may be under-checked in audits | — | medium | AUDIT, DISCOVER | no | clarification |
| **PT-30** (RB-18) | `SKILL.md` §6; protocol l.7 | Fingerprint History can fill with section entries and critique stamps, skewing the "last 5" comparison; "session note" undefined | Fingerprint contamination within a project | quotes | low-medium | multi-page BUILD | no | clarification |
| **PT-59** (RA-11, RB-04 accessibility half; reviewer R-03) | `critique-protocol.md` l.13; `SKILL.md` l.174, l.181 | Axis 5 is "never skipped, regardless of scope", while §7's example says "a nav-bug POLISH loads `layout-interaction.md` and maybe `accessibility.md`". T2 loads a category that is "in scope", and axis 5 can reasonably put accessibility in scope, so this is interpretation, not proof | Sessions may score axis 5, including conditional A11Y-012 and A11Y-006/-008, without the rule text loaded | quotes | medium | POLISH, BUILD-existing / CRITIQUE L1 | no | clarification (Level 1 implies loading `accessibility.md`) |
| **PT-60** (reviewer R-05) | environment: `~/.claude/skills`, `~/.agents/skills`, session skill list | About 30 installed design skills have descriptions overlapping `design-excellence` (for example impeccable, lexia-design, frontend-design, design-taste-frontend) | A terse prompt in a fresh session may invoke a different skill, so the test would not exercise this one | reviewer listing of both skill folders; session skill list | medium | skill selection | no, if the test invokes the skill explicitly | test setup: invoke `design-excellence` explicitly and record which skills loaded |

## 4. Contradictions / Inconsistencies

These are text-level contradictions or ambiguities. Most are also listed as A or B above.

| # | Contradiction | Where | Class |
|---|---|---|---|
| 1 | POLISH `INSPECT(cache read only)` vs mandatory safety scan | `SKILL.md` l.73 / `existing-project-safety.md` l.5–7 | A (PT-02) |
| 2 | DEFINE row's POLISH clause vs POLISH row and Hard rule (ambiguity) | `SKILL.md` l.21 / l.32, l.34, l.73 | A (PT-02) |
| 3 | Stack files placed inside the skill package vs `loop.md` §2 gate on adding runtime knowledge | `SKILL.md` l.179, l.185 / `loop.md` §2 | A (PT-03) |
| 4 | Level 1 axis 1 requires SLOP-011 vs T3 loading conditions | protocol l.9 / `SKILL.md` l.183 | A (PT-05) |
| 5 | Axis 5 "never skipped" vs "maybe `accessibility.md`" (interpretive) | protocol l.13 / `SKILL.md` l.181 | B (PT-59) |
| 6 | A11Y-001 P1 universal 24×24 vs A11Y-005 P5 touch-only 24×24 | `accessibility.md` l.13 / l.89–91 | A (PT-10) |
| 7 | REDESIGN Level 2 at any scope vs page/multi-page only | `SKILL.md` l.72 / protocol l.22 | A (PT-17) |
| 8 | Kinetics' MOTION-002 vocabulary vs MOTION-002 | `kinetics.md` l.40, l.84 / `motion.md` l.22 | A (PT-12) |
| 9 | MOTION-004 remediation vs MOTION-004 rule | `motion.md` l.44 / l.50–51 | A (PT-13) |
| 10 | "Production-facing" sufficient trigger vs no default Level 2 for component/section BUILD | protocol l.21 / l.26 | B (PT-21) |
| 11 | Project State vocabulary in three forms | `SKILL.md` l.64 / l.137 / l.146–150 | C (PT-33) |
| 12 | REF-007 "navigate by color alone" vs A11Y-011 | `visual-references.md` l.83 / `accessibility.md` A11Y-011 | C (PT-45). A11Y-011's authoring report judged a compliant reading possible ("every" label present). Kept as C |
| 13 | SLOP-010 title (prefers true black) vs COLOR-005 (forbids it) | `anti-slop-registry.md` / `color.md` | C (PT-43) |
| 14 | Level 1 stamp into Fingerprint History vs directions-only (no Fingerprint writes) | protocol l.7 / `SKILL.md` l.50 | C (PT-40) |
| 15 | Directions-only (no committed-direction writes) vs Greenfield "create `context.md` after DEFINE" | `SKILL.md` l.50 / l.147 | C (PT-38) |
| 16 | `loop.md` §12 STATE contents vs `STATE.md` "Authorization scope" section and result-restating Next action | `loop.md` §12 / `STATE.md` | C (PT-49) |

## 5. Dead or Unreachable Rules / Capabilities

| Item | Why dead or unreachable | Class |
|---|---|---|
| Stack modules (`references/stacks/*.md`) | Directory absent; no template; no defined location owner (PT-03); never triggered | A (as specified) |
| COLOR-006 | Depends on a palette pool and alternatives that do not exist (PT-14) | A |
| LAYOUT-001 named bundles | Referenced in `style-catalog.md`, which has none (PT-15) | A |
| SLOP-011 on BUILD-existing and POLISH | Required by Level 1 axis 1 but not loadable on those routes (PT-05) | A |
| TYPE-002 / SLOP-014 "overused fonts" list | The list does not exist; "browse real foundries" presumes web access (RB-24) | C (PT-44) |
| A11Y-006 (P1 drag alternative) | Never referenced outside its entry; `gesture-physics.md` does not point to it; not in axis 5; reached only if `accessibility.md` is loaded on a drag task | B (PT-59) |
| A11Y-008 (never disable zoom, critical, near-universal) | Filed under Conditional, not on axis 5 | B (PT-59) |
| A11Y-012 (conditional, on axis 5) | Listed on axis 5, but reached only when `accessibility.md` is loaded | B (PT-59) |
| Level 1 automatic escalation trigger | Needs "two consecutive revision passes", but no REFINE loop is defined on the BUILD-existing and POLISH routes (PT-20) | B |
| `pages/<slug>.md` usage and `.design/preflight-cache.json` format | Named but not specified (RB-21 / RA-20) | C (PT-37) |
| "Session note" (Level 1 stamp) | Location and format undefined | C (PT-40) |
| DISCOVER deliverable | Output format undefined; never produced at runtime (PT-24) | B |
| ID integrity | **No dangling rule ids.** Every referenced id resolves (agent B, mechanical). LAYOUT-006 and PRN-0002 are unreferenced gaps in the numbering | D (counted in §8) |

## 6. Missing Test Coverage

Coverage that the architecture claims or requires but that no runtime evidence covers:

1. **An existing project with no `.design/`.** Every existing-project fixture had it, including the overlay benchmarks (PT-02).
2. **Terse prompts without restrictive scaffolding on page-scope and read-only routes.** The overlay benchmarks used ordinary requests for component/section BUILD and component POLISH, but the 9.2 page-scope runs carried "do not modify / skill dir read-only / stop and ask".
3. **Framework and package-manager stacks** (Next.js, React, Tailwind, Vite beyond vanilla). No run (PT-26), so stack detection and existing component-system preservation are untested.
4. **T4 sources as real dependencies** (Reicon, Kinetics, SmoothUI). Never operationalized (PT-11, PT-26).
5. **Completed deliverables for CRITIQUE, AUDIT and DISCOVER**, and POLISH beyond one component-scope run. None or one observed (PT-24, PT-25).
6. **The bounded-profile implement route (R3).** Never run.
7. **DIRECT in directions-only.** Never observed completing (agent A, scenario 6).
8. **Level 2 on real projects.** The trigger threshold and cost were never exercised (PT-21).
9. **The no-render / capability-unavailable path end to end.** Mechanical checks reported `skipped`, Level 1 scoring without render (PT-06).
10. **Compound requests and screenshot-only critique** (PT-22, PT-23).
11. **A writable skill directory** (PT-03).
12. **A stale or foreign `.design/`** (PT-27).
13. **Skill selection among competing installed design skills** (PT-60).

## 7. Test-Blocking Issues

| ID | Why blocking | Condition |
|---|---|---|
| **PT-01** (P) | The skill does not load outside this repository | always, until installed for the test |
| **PT-04** (P) | Writes into a real project fall outside loop authority | if the test runs as a loop milestone against a real (not disposable) project |
| **PT-02** (A) | The scenario follows ambiguous and contradictory instructions, so results would measure improvisation, not the specified system | if the first test is a POLISH, CRITIQUE or AUDIT on an existing project without `.design/` |
| **PT-03** (A) | The session may try to write an unspecified file into the skill package, possibly the governed repo | if the test uses a framework stack and the skill directory is writable and linked to this repository |

Everything else is non-blocking. It will show up during testing and should be watched.

## 8. Non-Blocking Issues

**A (fix after testing unless convenient):** PT-05, PT-10, PT-12, PT-13, PT-14, PT-15, PT-16, PT-17.

**B (watch during testing):** PT-06 to PT-09, PT-11, PT-18 to PT-30, PT-59, PT-60.

**C — documentation and clarity** (PT-54 and PT-57 are unused numbers):

| ID | Item (source) | Location |
|---|---|---|
| PT-31 ✓ | `STATE.md` status was set to "AUTHORIZED — NOT STARTED" in the authorization step, which is not a `loop.md` §6 value (`READY` is); corrected to `IN PROGRESS` when the audit began. Introduced by the main agent itself (RC-05) | `STATE.md`; `loop.md` §6 |
| PT-32 ✓ | This milestone's "hasta 3 subagentes operativos" plus a §8 review can read as 4 against the `loop.md` §9 cap of 3 including the reviewer; resolved conservatively as 2 + 1 (RC-09) | `loop.md` §9 |
| PT-33 | Project State vocabulary drift (RA-15) | `SKILL.md` l.64, l.137, l.146–150 |
| PT-34 | DIRECT trigger wording excludes REDESIGN; resolved in practice (RA-16) | `SKILL.md` l.22 |
| PT-35 | HARDEN depends on undefined "ship-readiness" and "prototype" (RA-17) | `SKILL.md` l.29 |
| PT-36 | "Implement" requires "explicitly asks" (RA-18) | `SKILL.md` l.48, l.52 |
| PT-37 | `pages/<slug>.md`, the preflight cache format, and concept/"prepared direction" recording location unspecified (RA-20, RB-21) | `SKILL.md` l.51, l.130, §5 |
| PT-38 | Directions-only vs the Greenfield `context.md` write (RA-19) | `SKILL.md` l.50, l.147 |
| PT-39 | Whether §2 rows are exhaustive for unbounded runs (RA-21) | `SKILL.md` l.18–30, l.74–76 |
| PT-40 | Level 1 stamp and "session note" undefined; conflicts with directions-only (RA-24, RB-18) | protocol l.7 |
| PT-41 | No explicit load condition for `critique-protocol.md` (RA-22, RB-26) | `SKILL.md` l.174 |
| PT-42 | DISCOVER vs "explore" wording overlap; low risk at runtime (RA-23) | `SKILL.md` l.50, l.76 |
| PT-43 | Anti-slop registry puts a register in `genre` fields; entries lack `validation`/`layer` though SLOP-003 is treated as a gate; SLOP-010 title vs COLOR-005 (RB-22, RB-23) | `anti-slop-registry.md` |
| PT-44 | TYPE-002/SLOP-014 missing font list; web access assumed (RB-24) | `typography.md`, `anti-slop-registry.md` |
| PT-45 | REF-007 "by color alone" wording vs A11Y-011 (RB-25) | `visual-references.md` l.83 |
| PT-46 | Authority wording (RB-26): Kinetics precedence skips P6; COLOR-007 makes a technique P1; A11Y-006's single-pointer clause is not a keyboard item; `existing-project-safety.md` declares the whole file P1; SmoothUI activation clause hard to parse; LAYOUT-002 wrong file | various |
| PT-47 | Citations to non-shipping files: `loop.md`, `PHASE-*-RESULTS.md`, `ARCHITECTURE.md`, `FORENSIC-EXTRACTION.md`. None is a load instruction; `SKILL.md` l.10 declares the design docs non-shipping but not `loop.md` (RA-25, RB-19) | protocol l.13; `layout-interaction.md` l.77–138; others |
| PT-48 ✓ | Evidence for the Phase 8–10 clarifications cited in `SKILL.md` (for example Phase 9.2C/9.2E/9.2I, l.54, l.100) exists only in the untracked `scratchpad/`, not in version control (RC-04) | `scratchpad/phase9.*` |
| PT-49 ✓ | `STATE.md` has an "Authorization scope" section not in the `loop.md` §12 field list, and a Next action that restates results (RC-06) | `STATE.md`; `loop.md` §12 |
| PT-50 ✓ | `loop.md` §18 "Current Strategic Context" still frames the catalog/Principle Pool question as current (RC-07). `loop.md` is never loaded by the skill, so this is not runtime-affecting | `loop.md` §18 |
| PT-51 ✓ | `SKILL.md` l.187 "Every rule … is referenced by id from this file and from every other reference file" overclaims; the intended meaning is "referenced by id, never restated" (RC-10) | `SKILL.md` l.187 |
| PT-52 | Level 2 "any one trigger" vs component/section exclusion has no tie-break (RB-20); overlaps PT-21 | protocol l.18–26 |
| PT-53 | `context.md` `project_state` values do not match §2 Project State names (RB-21); overlaps PT-33 | `SKILL.md` l.137 |
| PT-55 | Level 2 honest-limitation message must be quoted verbatim, which is brittle if paraphrased (agent B note) | protocol |
| PT-56 | `existing-project-safety.md` "preserve/introduce summary" required before BUILD has no format (RA-01 part) | l.16 |
| PT-58 | `rules.md` (browser-tool preferences) and `scratchpad/` are untracked residue at the repo root. They are not loaded by the skill, and they are not this audit's to change | repo root |

**D — intentional design decisions (16, not defects):**
- the narrow enumerated P1 list, with most accessibility rules at P5;
- the Visual References and Principle Pool provenance boundary, which holds: no source identity leaks, and neither is used in CRITIQUE or AUDIT;
- T4 sources are implementation-only, with no path to design direction and no premature activation found (SmoothUI l.104–105 routes bundled icons and motion back through their gates);
- freshness intervals (entries fresh until about 2026-12);
- the Level 2 honest-limitation quote;
- the fingerprint is experimental and project-local;
- the Replace confirmation gate halts REDESIGN implementation;
- announce-and-proceed classification;
- EXPLORE is a sub-step of DIRECT;
- bounded profiles are qualifiers;
- no stack files ship by default;
- AUDIT and DISCOVER are exempt from Level 1;
- `CRITIQUE(floor)` vs `(floor only)` is consistent and runtime-confirmed (9.2J);
- the bounded REDESIGN AUDIT-stage exclusion is runtime-confirmed (9.2G);
- `loop.md` and `STATE.md` are outside the skill directory and never loaded by it;
- ID integrity: no dangling rule ids (§5).

**E — not assessable (10):**
- behaviour on terse prompts on page-scope and read-only routes;
- the implement route and completed CRITIQUE, AUDIT and DISCOVER deliverables;
- whether a session actually writes stack files when the directory is writable;
- whether T4 package names resolve safely (no web access);
- whether other installed design skills write `.design/` with a different schema;
- Level 2 cost on real projects;
- PRN-0001 under text resize (the skill has no WCAG 1.4.4 rule);
- whether the installed skill folder would be writable in the test environment;
- budget adherence: past milestones recorded no elapsed time against the `loop.md` §11 60-minute budget;
- first-hand re-verification of every agent-B quote. The main agent spot-checked some, and the reviewer re-verified all A findings and eight B findings.

## 9. Recommended Correction Order

Each step would need its own authorized milestone. None is made here.

1. **Test setup (no skill change):**
   - install the skill so external projects load it (PT-01);
   - invoke it explicitly and record which skills loaded (PT-60);
   - decide the test target and authorization: a disposable copy vs a real project (PT-04);
   - make the skill directory read-only for the test run, or otherwise guard it (mitigates PT-03).
2. **Targeted specification correction: the no-context bootstrap for POLISH, CRITIQUE and AUDIT** (PT-02, with PT-07, PT-27 and PT-56 folded in):
   - what INSPECT does on a cache miss;
   - whether and when `.design/` files are created on an existing project;
   - where POLISH gets register, genre and dials when they are absent;
   - whether read-only modes persist anything;
   - staleness of an existing `.design/`.
3. **Targeted specification correction: stack modules** (PT-03). Location, owner, trigger stage and template, or declare stack files deferred.
4. **Level 1 critique honesty** (PT-05, PT-06, PT-59): Level 1 loads what it checks; a Level 1 not-assessable option; capability tags on rules that need rendering.
5. **Authority leakage** (PT-08, PT-09, PT-10): mechanical gates vs P2/P4; CONTENT-003 on existing content; A11Y-001 vs A11Y-005.
6. **Routing clarifications** (PT-17 to PT-24, PT-28 to PT-30, PT-33 to PT-42): BUILD vs REDESIGN rule, section-scope REDESIGN and directions, REFINE loop and cap, Level 2 thresholds and reviewer brief, compound requests, artifact-only critique, AUDIT and DISCOVER output and accessibility path, fingerprint hygiene.
7. **Catalog and T4 consistency clean-up** (PT-11, PT-12 to PT-16, PT-43 to PT-47, PT-52 to PT-55).
8. **Loop and state hygiene** (PT-31, PT-32, PT-48 to PT-51, PT-58).

## 10. Explicit Pre-Test Gate

**MUST FIX before the first real skill test:**
- **PT-01 (P):** make the skill loadable from the test project, and invoke it explicitly (PT-60).
- **PT-04 (P):** human decision on the test target (disposable copy vs real project) and its authorization.
- **PT-02 (A):** resolve the no-`.design/` bootstrap for POLISH, CRITIQUE and AUDIT. Alternative: choose a first test that avoids this path (greenfield BUILD, or an existing project that already has `.design/`) and record the path as untested.
- **PT-03 (A):** prevent unintended writes into the skill package. Either correct the stack-file specification, or guard the test with a read-only skill directory and record any attempted write as a finding.

**SHOULD FIX before the first real skill test:**
- **PT-05, PT-59:** Level 1 loads what it checks (SLOP-011, `accessibility.md`).
- **PT-06:** a Level 1 not-assessable option and render-dependence tags. This avoids invented scores that would contaminate test evidence.
- **PT-07:** read-only modes do not write into the user's repo.
- **PT-09:** CONTENT-003 must not strip real existing content.
- **PT-11:** confirm before installing any T4 package whose name is unverified.

**CAN WAIT until after the first real skill test** (observe and record during testing):
- PT-08, PT-10, PT-12 to PT-30 (other than those above), and all C items (PT-31 to PT-58, excluding the unused numbers PT-54 and PT-57).
- Treat the routes listed in §6 as unvalidated. Instrument the test to capture:
  - which skills loaded;
  - routing classification and stages run;
  - files read and written, including anything under the skill directory;
  - every `skipped — capability unavailable`.

---

## 11. Independent review (`loop.md` §8)

**Reviewer.** One fresh, read-only general-purpose agent: the third subagent, within the §9 cap.

**Blindness.** It received this report, because its task was to check the report's claims against the sources. It was instructed to verify every checked claim first-hand rather than adopt the report's reasoning, and it did so: it re-read every A finding and eight B findings, and listed the user-level skill folders itself.

**Not given:** `STATE.md`, git log messages, the web or memory tools.

**Result:** 1 BLOCKING, 6 SHOULD-FIX, 6 MINOR, plus NOTES. It confirmed:
- A findings PT-10, 12, 13, 14, 15, 16 and 17, the core of PT-02, and the facts of PT-01;
- B findings PT-06, 07, 09, 11, 18 and 26;
- the counts and the gate's coverage of every ID;
- scope compliance.

| Finding | Class | Reconciliation |
|---|---|---|
| R-01: the report omitted the committed overlay benchmarks (5 completed existing-project BUILDs and 1 completed POLISH, with writes and Level 1) and so overstated "every other route unvalidated" and "every recent prompt scaffolded" | BLOCKING | **Adopted.** §1, §6 items 2 and 5, and PT-25 rewritten. PT-02 is strengthened: those fixtures also all had `.design/context.md`. The omission is the main agent's error; it ran those benchmarks earlier in this session |
| R-02: PT-03 misread `SKILL.md` l.100 (limits P2 authority) and l.191 (untrusted content) as contradictions | SHOULD-FIX | **Adopted.** Those citations were withdrawn. A stands on the package-internal location, missing template and directory, and the `loop.md` §2 gate. The alternative reading (maintainer-authored) and install dependence are recorded |
| R-03: PT-05's accessibility half is interpretation | SHOULD-FIX | **Adopted.** PT-05 narrowed to SLOP-011 (A); the accessibility half split out as PT-59 (B); summary wording corrected |
| R-04: PT-02 too broad; BUILD-existing and REDESIGN imply a bootstrap; l.21 is ambiguous rather than contradictory | SHOULD-FIX | **Adopted.** Narrowed to POLISH, CRITIQUE and AUDIT; l.21 described as ambiguous; safety §5 evidence added. It remains A because l.73 vs `existing-project-safety.md` l.5–7 is a direct contradiction |
| R-05: competing installed design skills (material miss) | SHOULD-FIX | **Adopted** as PT-60 (B), and in test setup and instrumentation |
| R-06: PT-01 is an install state and PT-04 a governance decision, not skill defects | SHOULD-FIX | **Adopted.** Both moved to a "test preconditions (P)" group and kept MUST FIX. The plugin search was done by the main agent only, which is now noted |
| R-07: "three bounded pre-test actions" vs four MUST FIX items | SHOULD-FIX | **Adopted.** The summary now says two preconditions and two specification decisions |
| §5 labelled A11Y-006/-008/-012 "B (part of PT-05)" while PT-05 is A | MINOR | **Adopted.** Now B (PT-59) |
| §5 ID-integrity D item missing from the D list | MINOR | **Adopted.** D is now 16 |
| §7 lacked conditions for PT-02 and PT-04 | MINOR | **Adopted.** Condition column added |
| PT-27 to PT-30 and PT-58 in no correction step | MINOR | **Adopted.** §9 steps 2, 6 and 8 |
| PT-16's first two items are closer to C | MINOR | **Recorded** in PT-16. It is kept as one grouped A, because two of its four items are outright wrong |
| PT-06 should note axis 3's "where in scope" exemption | MINOR | **Adopted** |
| PT-08 slightly inflated; PT-09 under-weighted; PT-18's evidence file is in the untracked scratchpad | NOTE | **Adopted.** PT-08 confidence lowered, PT-09 raised, PT-18 evidence location noted |
| §11 placeholder | NOTE | Filled (this section) |

No disagreement remains. Final counts: A 10, B 20, C 26, D 16, E 10, P 2.

## 12. Files changed

- `benchmarks/audit/COMPREHENSIVE-PRE-TEST-SKILL-READINESS-AUDIT-RESULTS.md`: created (this report).
- `STATE.md`: the human's authorization record (from the previous step) and operational fields.

No other file was changed. Subagent working notes are disposable, in the session scratchpad, and are not committed.

## 13. Commit

The hash is reported in the final response, since a commit cannot contain its own hash. Nothing was pushed.
