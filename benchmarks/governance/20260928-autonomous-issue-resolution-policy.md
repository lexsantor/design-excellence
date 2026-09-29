# Autonomous Issue Resolution & Escalation Policy

- **Date:** 2026-09-28
- **Status:** COMPLETED
- **Authorization (human, verbatim):** "Autorizo el milestone Autonomous Issue Resolution & Escalation Policy."
- **Changed:** `loop.md` only (plus `STATE.md` and this report). No Design Excellence skill file changed.

## 1. Stop-and-return points found before the change

| # | Where | Problem |
|---|---|---|
| 1 | §1 step 2, §19 | Proceed only if `STATE.md` already names the authorized milestone; the human authorizes in the session, so a strict reading stops at the start |
| 2 | §2 gate list | Read as absolute even when the milestone's own authorization names the action; only one item carried "unless the milestone explicitly authorizes it" |
| 3 | §7 | Only operational `STATE.md` fields may change, so strictly even recording the human's milestone authorization needed separate approval |
| 4 | §17 | Every human decision required a 7-part report; no short form for one out-of-scope action |
| 5 | §13 step 5 | "retry only when the retry can produce materially new evidence" blocked plain retries after transient failures |
| 6 | §11 | Fix-and-revalidate passes could be counted as meaningful iterations, and one exhausted 10-minute troubleshooting cap could be read as `BUDGET-STOPPED` for the whole milestone |
| 7 | §8 | In-scope reviewer findings had no stated autonomous path |
| 8 | whole file | Nothing said that a discovered defect stays inside the milestone and is fixed without asking |

## 2. Change

- **New §2.1 In-milestone issue resolution:** discovery vs decision; five conditions for autonomous resolution; INVESTIGATE → CLASSIFY → REPAIR → VALIDATE → CONTINUE as working steps inside the Core Loop (not a stage); decision table A–E; "no permission needed" list; human boundary; the exact escalation question with its sí/no semantics, `BLOCKED`-resumable recording and `UNRESOLVED`/`FAILED` close; exclusions (§3, §5, starting another milestone, multi-direction choices go to §17); a non-weakening clause (§3, §5, §6, §7, §9, §11, §14, evidence, explicit milestone stop conditions).
- **§1 step 2:** a milestone the human explicitly authorizes in the session is authorized by that text and is recorded in `STATE.md` before execution; a recommendation, an unnamed milestone or a "sí" to the §2.1 question is never a milestone authorization.
- **§2:** a listed action is authorized only when the milestone's authorization names it, within its scope, never where `loop.md` forbids it (§6, §14 no automatic push); §3 and §5 keep their rules.
- **§6:** a milestone `BLOCKED` only on a §2.1 question resumes when answered.
- **§7:** recording a human-given authorization (budget as given or §11 default) and the milestone result is covered by that authorization.
- **§8:** an in-scope reviewer finding is fixed and revalidated autonomously; it is not a disagreement.
- **§11:** corrective passes belong to the iteration that found the problem; a pass producing new evidence about the hypothesis is a meaningful iteration; the per-problem troubleshooting cap ends work on that problem, not the milestone; only iteration and wall-clock budgets produce `BUDGET-STOPPED`.
- **§12:** the Authorization field is named as status, exact text and scope (existing practice).
- **§13:** transient retries need no new evidence and no permission; in-scope failures are repaired autonomously.
- **§17:** the full handoff is for end-of-milestone strategic decisions and §3/§5 gates; a single out-of-scope action uses the §2.1 question.

No new milestone type, stage, mode, score, trigger, P-layer, approval system, agent hierarchy, state file or permission framework. The §1 step 2 bullet and the §12 wording go slightly beyond "execution inside milestones": they align the text with how authorization is actually given and recorded (disclosed here; the human requirement is unchanged).

## 3. Independent review and reconciliation

One fresh read-only general-purpose reviewer; no BLOCKING. All findings adopted:

| Finding | Class | Resolution |
|---|---|---|
| Per-problem troubleshooting cap could end the milestone | SHOULD-FIX | §11: ends that problem, not the milestone |
| Condition 5 blocked every fix in a governance-scoped milestone | SHOULD-FIX | "beyond what the authorization covers" |
| Multi-direction choice is not yes/no | SHOULD-FIX | routed to §17 handoff |
| "before or while executing" conflicted with §1/§6 | SHOULD-FIX | "before executing it" |
| "Expand into an independent body of work" could be settled by a "sí" | SHOULD-FIX | starting another milestone excluded from the question; "sí" is never a milestone authorization (§1) |
| §2 sentence could let an authorization name "push" | SHOULD-FIX | "never where `loop.md` forbids it (§6, §14)" |
| `BLOCKED` conflicted with §6 terminal statuses; "no" close status unnamed | SHOULD-FIX | `BLOCKED` resumable (§2.1, §6); close as `UNRESOLVED` or `FAILED` |
| §13 step 5 still read as blocking retries | MINOR | "(transient failures: see below)" |
| §7 could let the agent set its own budget | MINOR | "as given by the human or the §11 defaults" |
| Case D action may be in scope but unauthorized | MINOR | prose clarified; template unchanged |
| Corrective passes could be used to relabel experiments | MINOR | "a pass that produces new evidence about the hypothesis is a meaningful iteration" |
| §12 field list vs practice | note | aligned |

No unreconciled disagreement.

## 4. Validation

- Full diff read after reconciliation; `git diff --check` clean; only `loop.md` modified before this report and `STATE.md`.
- The escalation question is present verbatim (whitespace-normalized across the blockquote line break).
- Remaining "stop" wording: §0 conflict, §1 missing authorization, §5 mirror mismatch, §9 unresolvable conflict, §11 budgets and repeated structural failure, §16/§19 close-out. None fires on discovering a defect.
- Expansion paths checked: new milestones need human text (§1, §6); "sí" is scoped to one action and never a milestone authorization; §3/§5/§7/§9/§11/§14 are named as not relaxed.
- Pre-existing untracked items untouched; no skill, catalog or external project file changed.

## 5. Limitations

- The policy is text; whether an agent actually stops less, and asks in the exact form, is untested behaviour.
- "Within scope" and "materially useful" remain judgement calls; the policy moves the default towards acting but cannot remove interpretation.
- Existing milestone briefs that list their own stop conditions still bind (§2.1 non-weakening clause); a brief phrased as "stop and report if X" keeps stopping on X.

## 6. Agents

One read-only reviewer. No other agents.
