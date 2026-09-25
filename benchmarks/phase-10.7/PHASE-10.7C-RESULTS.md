# Phase 10.7C: Results
## Visual References freshness, Read-hook diagnosis, architecture regression

**Status:** PASS (one non-blocking AMBIGUOUS item, §4)
**Scope:** one header sentence in `visual-references.md` and one pointer phrase in LAYOUT-010. No new fields, lifecycle, stage, load event or governance mechanism. No REF or PRN record changed. No principle curation.
**Method:** main-agent, read-only trace of the current text against every regression area; no subagents (a text trace resolves each area directly, so no fresh-context executor was needed). Observed text only; no scores.

---

## 1. Changes

| Workstream | Change | Where |
|---|---|---|
| 1 Freshness | Header sentence: an entry whose `last_verified_date + review_interval_days` has passed when the file is consulted is **not considered**; it is re-verified (new `last_verified_date`) or removed, never silently kept, the same rule `principle-pool.md` applies | `visual-references.md` line 7 |
| 1 Consistency | LAYOUT-010 freshness line said only `principle-pool.md` states a staleness rule; now "each file states its staleness rule in its header" | `layout-interaction.md` line 100 |

`visual-references.md` has no `status` field, so its rule is date-based only. `principle-pool.md` additionally excludes `status: stale`. Both exclude overdue entries. All nine REF entries are fresh today (2026-09-21 + 90 = 2026-12-20); PRN-0001 is fresh (2026-12-24).

## 2. Read-hook diagnosis

**Cause: external, user-global plugin, not this repository.** The claude-mem plugin (`thedotmack/claude-mem` 12.0.1, enabled in `~/.claude/settings.json`) registers a PreToolUse hook on Read (`src/cli/handlers/file-context.ts`, `fileContextHandler`). For any file ≥ 1,500 bytes that has prior claude-mem observations, it returns `permissionDecision: allow` with `updatedInput: { file_path, limit: 1 }` and an observation timeline as additional context.

**Evidence (this session):** Read on `visual-references.md` and `principle-pool.md` returned line 1 only with the hook message "Only line 1 was read to save tokens." A second Read with explicit `offset: 1, limit: 40` also returned line 1 only: `updatedInput` replaces the whole input, so the hook's own advice ("Read again with offset/limit") cannot work. This is a plugin defect.

**Not caused by:** the repository (no hook config; `.claude/settings.local.json` only enables the shadcn MCP server), `CLAUDE.md`, or Design Excellence instructions.

**Not fixed.** The only local off-switch is `CLAUDE_MEM_EXCLUDED_PROJECTS` in `~/.claude-mem/settings.json`, which is user-global configuration and would also stop memory capture for this project. That is outside this repository's scope. Recorded as an environment limitation. Shell read-only inspection (`cat`, `sed -n`) remains a valid fallback and was used here. Edit still works on gated files.

## 3. Architecture regression

| Area | Evidence (current text) | Result |
|---|---|---|
| A Routing | §2 table distinguishes BUILD (empty/existing), REDESIGN, POLISH, CRITIQUE, AUDIT, DISCOVER; §1 Hard rule and section-scope disambiguation separate component POLISH, section POLISH (no SHAPE) and section BUILD (narrow SHAPE, no DIRECT re-run); page BUILD gets DIRECT. DISCOVER = AUDIT-stage gap-finding, 5–7 findings, rejected candidates. Direction exploration is inside DIRECT, "not a new pipeline stage" (§1) | PASS |
| B Bounded profile | §1: directions-only has no commit and no Rejected Directions, Fingerprint or context write implying commitment; choose/prepare commits, logs rejected, runs SHAPE/DESIGN, stops before BUILD; implement = full row. §3 "P2 and pipeline extent": P2 narrows unless P1 requires otherwise. §1: omitted stages don't run "before or after the endpoint" | PASS |
| C REDESIGN + AUDIT | §1 AUDIT row: REDESIGN activates AUDIT; a bounded sequence that omits it prevails. §2 REDESIGN row mirrors this | PASS |
| D Critique depth | §1 CRITIQUE row: `CRITIQUE(floor)` = Level 1 minimum, Level 2 when triggered; only `CRITIQUE(floor only)` caps it. §1 bounded rule: stage selection doesn't govern depth. `critique-protocol.md` Level 2 triggers apply under `CRITIQUE(floor)` | PASS |
| E No-render input | `critique-protocol.md` step 1: (a) render + code, (b) design artifact/spec + relevant code, (c) directions-only exploration deliverable; never fabricate; unassessable axes are reported, not scored | PASS |
| F Pools | Same trigger via §7 (both rows), "not a new load event"; never CRITIQUE/AUDIT; LAYOUT-010 screens every entry, then at most 2–3 combined; family = tie-breaker only; freshness now stated in both headers (§1) | PASS |
| G Principle Pool governance | Ceiling 15, first pass 8, ≤ 2 per cluster, stale counts but not considered; schema status is `accepted \| stale` with only accepted consumable (other statuses cannot enter the file); changes only through reviewed promotion, no automatic sync or eviction; opaque id is the only provenance. Leak grep (catalog paths, UI8, record ids, hex colours, images): no hits | PASS |
| H Concept → Structure | §1 three-state model; brand name alone is at most HYPOTHESIS; HYPOTHESIS never triggers LAYOUT-009 or the structural test (`critique-protocol.md` axis 1); LAYOUT-009 "not an Anti-Slop rule"; runs inside DIRECT/EXPLORE | PASS |
| I Anti-Slop | LAYOUT-009/010 both state orthogonality (subtractive vs generative); Anti-Slop loads for CRITIQUE/AUDIT, the pools never do | PASS |
| J T4 | §7 T4 row plus `reicon.md`/`kinetics.md`/`smoothui.md` precedence: user instruction and existing system first; Reicon default only where new iconography is needed; Kinetics only for already-justified motion; SmoothUI never justifies componentization (Principle 11); stack settled independently; migration requires Replace confirmation. Stage wording: see §4 | PASS (see §4) |
| K Existing-system safety | `existing-project-safety.md` §1–§5 intact: inspect, preserve/introduce summary, Replace confirmation, append-only, redesign preserved-patterns contract, post-build diff; §3 P1 list unchanged | PASS |

## 4. Remaining non-blocking issues

- **AMBIGUOUS, T4 stage wording.** `kinetics.md:20` and `smoothui.md:22` say "at BUILD"; `reicon.md:20` says "at DESIGN/BUILD", unchanged since Phase 7.2 and audited in 7.5. No internal contradiction: selecting Reicon as the icon source in a DESIGN spec is not implementation. It is looser than the phrase "T4 activates only at BUILD". Not changed: this is a regression pass and nothing else contradicts it. Tighten only if a benchmark shows a choose/prepare run adopting Reicon as a dependency before BUILD.
- **Environment:** the claude-mem Read gate (§2) remains active. Future benchmark executors should expect shell-based reads.
- The `SKILL.md` §7 `visual-references.md` row does not mention its freshness rule (the `principle-pool.md` row does). Informational only; the rule lives in the file header, which is where LAYOUT-010 points.

## 5. Integrity

- Changed: `design-excellence/references/visual-references.md`, `design-excellence/references/rule-catalog/layout-interaction.md`, this report.
- Unchanged: `SKILL.md`, `principle-pool.md`, `critique-protocol.md`, all REF/PRN records, Anti-Slop, T4 files, prior benchmark history.
- UI8 catalog (`E:\_UI8\_CATALOG`): clean working tree, HEAD `40226c4` (committed before this session). Raw UI8 library: not accessed.
- Pre-existing untracked `rules.md` and `scratchpad/`: left untouched and not committed.
- Commit: see the git log entry after `6afba31` (`docs: add visual reference staleness rule`).

## 6. Readiness

Ready for the next UI8 principle curation batch: both pools have a stated overdue rule, governance is internally consistent, and every regression area passes. The pool holds 1 of 8 first-pass entries (15 ceiling).
