# Design Excellence Autonomous Evolution Loop

## Purpose

This loop governs autonomous maintenance, auditing, research,
validation, and incremental evolution of Design Excellence.

The objective is not to maximize change, fill the Principle Pool, or
generate activity. Improve the system only when evidence demonstrates
that improvement is warranted.

Persistent memory is the control-plane repository (§0), not chat
history.

## Completion Sprint Mode (active since 2026-09-28)

A human mandate (2026-09-28) replaces per-milestone authorization with
one standing objective: **finish the Design Excellence skill**. While
this mode is active it is the execution model, and it takes precedence
over the milestone language elsewhere in this file:

| Section | While the sprint is active |
|---|---|
| §1 Core Loop | One continuous cycle: DISCOVER → DIAGNOSE → FIX → VALIDATE → INTEGRATE → REVALIDATE → CONTINUE. Step 2 (confirm milestone authorization) and step 9 (close and stop) do not apply; the other steps apply to each problem worked. |
| §2 Autonomous Authority | Applies, except that these are pre-authorized: working any defect or completion item, editing `SKILL.md`, rules and references when runtime or static evidence supports it, editing `loop.md` and `STATE.md`, refreshing the installed copy, and local commits. Every other item on the §2 STOP list remains a human gate. |
| §5 Closed Branches | Unchanged, except the human-authorized reopening recorded in §5. |
| §6 One Milestone Per Run | Suspended. A defect found during the sprint is sprint work, not a new milestone. |
| §7 Self-Modification | `loop.md` and `STATE.md` may be edited to keep them truthful; autonomy boundaries, human gates and safety/provenance rules may not be weakened. |
| §11 Budgets | Per-milestone iteration and wall-clock budgets are suspended; the per-problem troubleshooting cap and the "same structural failure twice → reassess" rule apply. |
| §12 State Model | `STATE.md` is the live sprint record (objective, active problem, tried, passed, failed, blocked, remaining). Evidence stays in reports and workspaces. |
| §16 Completion | The sprint completes only when the skill passes the completion gate in `STATE.md`. |
| §17, §19 | Handoff and safety apply unchanged; the sprint stops only when complete or when a genuine external blocker leaves no independent work. |

Always, sprint or not:
-   Never push. Never write outside this repository, except the
    installed skill copy, and only through `tools/install-skill.ps1`
    (mirror, full parity check, write guard re-applied).
-   An unvalidated or ineffective fix is reverted, not left in place.
-   A permission, classifier or security denial is recorded and never
    worked around; independent work continues.
-   The Integration Contract (§3), provenance (§4), anti-gaming (§15)
    and the identity boundary are unchanged. Every new Principle Pool or
    visual-reference entry is held uncommitted for the human's review
    of that entry before commit (authorization of 2026-09-28, §5).

## 0. Governance Home

-   **Control plane.** `C:\Users\<user>\Desktop\design-excellence` (this
    repository) is the control-plane repository for autonomous Design
    Excellence evolution.
-   **Authoritative loop files.** `loop.md` (this contract) and
    `STATE.md` (the single authoritative operational state, §12), both
    at this repository's root.
-   **Workspace location.** Design Excellence workspaces, disposable
    test projects, benchmark and evidence workspaces, and temporary
    artifacts live inside this repository, in subdirectories kept
    separate from governed files (the skill directory, `loop.md`,
    `STATE.md` and committed reports); never as new folders beside
    this repository, and never inside the external reference catalog or
    a reference library. An existing repository-local workspace may be
    reused when reuse cannot contaminate earlier evidence. Workspaces
    stay uncommitted (§14). The installed user-level copy of the skill
    is an installed runtime copy, not a workspace, and stays outside
    this repository. Any other location outside this repository is used
    only when an operation inherently requires it or an authorization
    or governance rule requires it.
-   **External repository.** The external reference catalog is an
    external governed research/reference repository, separate from this
    repository. The loop may inspect it read-only, and only when the
    authorized milestone permits it. It is never the loop's persistent
    state, and the loop never writes loop state into it.
-   **Report authority.** Catalog milestone reports remain authoritative
    for catalog milestones. Design Excellence reports remain
    authoritative for Design Excellence milestones. The loop cites them
    and never rewrites them.
-   **Precedence.** The Phase 10.7 Integration Contract (§3) governs
    over `loop.md`, and `loop.md` governs over `STATE.md`. On any
    conflict, stop and hand off (§17).
-   **Identity hygiene.** `loop.md` and `STATE.md` sit outside the skill
    directory `design-excellence/` and are never loaded by the skill.
    They are tracked Design Excellence files and are bound by the
    Integration Contract's identity boundary like any other. They refer
    to the catalog, the library, and their branches only by neutral
    governed terms (external reference catalog, licensed reference
    library, external research/reference repository, commercial
    reference family). They carry no product, vendor, marketplace,
    cluster or source names, filesystem paths of the catalog or any
    library, catalog or record ids, commit hashes, capture or
    provenance identifiers, measurements, or source material.

## 1. Core Loop

Execute this cycle in order, inside the one authorized milestone (§6):

1.  **AUDIT STATE**
    -   Read `STATE.md`, git status of this repository, the milestone's
        previous report, and the reports it depends on.
    -   Confirm every governing file was read completely (compare line
        counts); a truncated read is a technical failure (§13).
    -   Identify what is known, unknown, stale, contradictory, or
        unresolved.
2.  **CONFIRM AUTHORIZATION**
    -   Proceed only if `STATE.md` names a milestone whose authorization
        status authorizes it and whose status is `READY` or
        `IN PROGRESS`. Otherwise stop.
    -   A milestone the human explicitly authorizes in the current
        session is authorized by that text. Record it in `STATE.md`
        (milestone name, exact authorization text, scope, status
        `IN PROGRESS`) before executing it; this recording is covered
        by that authorization (§7). A recommendation, a milestone the
        human did not name, or a "sí" to the §2.1 escalation question
        is never a milestone authorization (§6).
    -   Everything done in this run must fall inside that
        authorization.
3.  **FORM A BOUNDED HYPOTHESIS**
    -   Within the milestone, state what is being tested and what
        evidence would confirm or reject it.
    -   Define scope, allowed files, evidence required, stopping
        conditions, and rollback boundary before execution.
    -   Never optimize toward a predetermined positive result.
4.  **INVESTIGATE / EXPERIMENT**
    -   Inspect existing material before creating anything.
    -   Use the smallest experiment capable of resolving the hypothesis.
    -   Prefer read-only work; disposable copies live in a
        repository-local workspace (§0), outside governed state.
    -   Preserve existing systems by default.
    -   Never modify raw reference libraries.
5.  **VALIDATE**
    -   Run deterministic checks appropriate to the change.
    -   Verify provenance, licensing, schema integrity, paths,
        references, and regressions where applicable.
    -   Never treat successful execution as proof that the hypothesis is
        correct.
6.  **CRITIQUE**
    -   Always perform the self-critique floor.
    -   Run independent review when §8 requires it.
7.  **RECONCILE**
    -   Compare evidence against the hypothesis.
    -   Record agreement, contradiction, uncertainty, and limitations.
    -   Reject the hypothesis when evidence does not support it.
    -   Do not reinterpret failures as successes merely to continue.
8.  **UPDATE PROJECT MEMORY**
    -   Write the milestone report (§12) and update the operational
        fields of `STATE.md`.
    -   Record what changed, what did not change, why, evidence, and the
        next unresolved question.
9.  **CLOSE THE MILESTONE** Record exactly one outcome (§6), then stop.
    Never start another milestone.
10. **COMMIT** per §14.

## 2. Autonomous Authority

Within the authorized milestone only, the agent may: inspect this
repository and, read-only, the catalog and reference libraries; create
disposable work copies in a repository-local workspace (§0); run local
builds and validation; perform bounded experiments; run read-only
subagents (§9); write the milestone report; update the operational
fields of `STATE.md`; and create one local commit on completion (§14).

STOP and request human authorization before:

-   any action gated by the Integration Contract (§3);
-   reopening a closed branch or acquiring references in any family, new
    or existing, unless the milestone explicitly authorizes it (§5);
-   starting, changing, or re-authorizing a milestone (§6);
-   any self-modification (§7);
-   adding, replacing, removing, or changing the meaning of any runtime
    knowledge in `design-excellence/` (visual references, principles,
    rules, style or anti-slop entries);
-   creating, changing, or deleting catalog records, schemas, or config;
-   changing P0 to P8 authority or safety boundaries;
-   changing fundamental Design Excellence architecture;
-   introducing a new permanent external source family;
-   changing licensing/provenance policy;
-   changing the Principle Pool ceiling or admission philosophy;
-   introducing a capability that materially changes runtime behavior;
-   pushing to a remote repository;
-   performing irreversible or materially costly external actions;
-   resolving a genuine strategic choice between multiple viable
    directions.

"Documentation within authorized scope" never covers any action on this
list. Do not ask for authorization merely because a task is complex.
An action on this list is authorized only when the current milestone's
authorization names it explicitly, and then only within that
authorization's scope and never where `loop.md` forbids it (§6 one
milestone per run, §14 no automatic push); §3 actions and closed
branches (§5) keep their own rules.

### 2.1 In-milestone issue resolution

Discovering something unexpected does not by itself create a human
gate. A gate exists only when resolving the discovery needs a decision
that the current authorization does not determine. Before asking,
determine whether the authorization already implies the correct
action; if it does, state "X prevents completing the authorized
milestone; I will fix it with Y, which is within scope" and proceed.
Never ask "I found X, what should I do?" when the milestone already
implies the answer.

A defect, failure, inconsistency, missing requirement, implementation
obstacle, failed validation or unexpected behaviour found during an
authorized milestone is resolved autonomously when resolving it is:

1.  directly related to the milestone objective;
2.  necessary or materially useful to complete the milestone;
3.  within the milestone's authorized scope (files, systems, actions);
4.  reversible or safely recoverable; and
5.  free of any change to the milestone objective, architecture,
    governance, product intent, security boundary or authorization
    boundary beyond what the authorization covers.

Default behaviour: INVESTIGATE → CLASSIFY → REPAIR → VALIDATE →
CONTINUE, then record the issue and its resolution in the milestone
report. These are working steps inside the existing Core Loop (§1),
not a stage, and a problem found during a milestone stays part of it:
it never becomes a new milestone. Fix-and-revalidate passes, reviewer
reconciliation and other corrective passes belong to the iteration in
which the problem arose (§11).

| Case | Action |
|---|---|
| A. Within authorized scope | investigate → fix → validate → continue |
| B. Necessary correction outside authorized scope | stop at the boundary and ask the escalation question below |
| C. Optional improvement, not needed to complete the milestone | do not implement; record it as a follow-up in the report |
| D. Safety, security, destructive or materially irreversible action not explicitly authorized | stop and ask the escalation question before acting |
| E. Temporary or tool failure | retry and investigate autonomously (§13); escalate only if it creates a real case B or D |

**No permission needed** (execution responsibilities, not authorization
requests) for: routine debugging; correcting the agent's own mistakes;
fixing failed validation; rerunning a failed command; repairing an
implementation defect; correcting documentation inconsistencies inside
the authorized files; gathering additional evidence; inspecting
additional relevant files; running additional bounded validation;
corrective edits required to satisfy the milestone; reconciling
in-scope reviewer feedback; retrying after a transient or tool
failure; fixing a regression caused by the current milestone's work;
and cleaning up temporary artifacts the current milestone created
inside its disposable workspace. Do not escalate because a fix is
inconvenient, unexpected or larger than anticipated while it stays
within scope.

**Human boundary.** Case B or D applies when the required action
would: change the milestone objective, product intent or architectural
direction; change governance outside the authorized governance scope;
introduce a new stage, mode, score, trigger, P-layer or equivalent
control mechanism; change a security or safety boundary or an
external-system permission; modify an unrelated project; take a
destructive or materially irreversible action not explicitly
authorized; expand into an independent body of work; choose between
materially different product or design directions the authorization
does not determine; or resolve a contradiction that needs a human
policy preference rather than technical interpretation. Everything in
the §2 list above not named by the authorization is on this boundary.

**Escalation question.** Ask exactly one question, in this form,
without a report before it:

> He encontrado [problema]. Para resolverlo necesito [acción concreta
> fuera del scope]. ¿Lo corrijo?

Name one concrete action, so that yes or no settles it; for case D
the action is the one that is not explicitly authorized, even where it
lies within scope. Record it as the pending human gate in `STATE.md`
(status `BLOCKED`, resumable, §6). An answer, in the same session or
later, returns the status to `IN PROGRESS` and clears the gate; that
update is covered by the answer. "sí" authorizes exactly that action,
nothing broader; perform it and continue the milestone. "no" forbids
it; continue with the safest valid alternative within scope if one
exists, otherwise close the milestone as `UNRESOLVED` (or `FAILED` if
its objective cannot be met), with the issue documented (§6). §3
Integration Contract actions, closed-branch reopening (§5) and starting
another milestone (§6) are never settled by this question: they end in
the §3/§17 handoff. Nor is a choice between several viable directions,
which is not a yes/no question: it ends in the §17 handoff.

This section changes execution authority inside an authorized
milestone only. It never authorizes a new milestone (§6), relaxes §3,
§5 or §7, changes agent limits (§9), budgets (§11) or commit rules
(§14), lowers the evidence standard, or overrides a stop condition the
milestone's own authorization states explicitly. Every fix is still
inspected before editing, validated and reported; failed attempts are
recorded, never hidden (§19).

## 3. Phase 10.7 Integration Contract

The loop is bound by the ratified Phase 10.7 Integration Contract,
held in the external reference catalog. The loop never edits it.

The following ALWAYS require explicit human authorization:

-   accepting a Principle Pool entry (contract Gate 1);
-   exporting or promoting a principle into Design Excellence (contract
    Gates 2 and 3);
-   changing the identity/provenance boundary;
-   allowing catalog observations, evidence, captures, or products to
    cross into Design Excellence;
-   making Design Excellence depend on the catalog or any raw library at
    runtime;
-   changing the Integration Contract itself.

Invariants the loop must preserve: Design Excellence behaves identically
where the catalog and raw libraries do not exist; only accepted,
identity-stripped principles cross, and only through Gates 1 to 3.

When a finding implies one of these actions is needed, the milestone
ends in a human handoff (§17). The loop does not prototype the crossing
in either repository, not even as a draft.

## 4. Knowledge Levels and Terminology

**Catalog model** (external repository):

PRODUCT → ARTIFACT → EVIDENCE → OBSERVATION → PRINCIPLE

-   **PRODUCT**: a source item held in a registered read-only library.
-   **ARTIFACT**: an inspectable part of a product (code package,
    shipped build, live service).
-   **EVIDENCE**: a typed, provenance-bearing record of what was
    inspected.
-   **OBSERVATION**: a concrete, checkable fact about one product,
    citing its evidence. It states what is there, never what to do.
-   **PRINCIPLE**: an abstraction supported by observations, with a
    lifecycle (draft, accepted, rejected, and so on).

PRODUCT through OBSERVATION carry source identity and stay in the
catalog.

**Design Excellence runtime knowledge** is separate from that model:

-   `REF-00x` entries in `visual-references.md` are governed
    visual-reference abstractions authored under Design Excellence
    governance. They are not raw catalog references and not catalog
    records.
-   `principle-pool.md` holds accepted principles exported under the
    Integration Contract.

In this contract, "reference" alone means catalog source material
(PRODUCT through OBSERVATION); "REF entry" means a Design Excellence
visual-reference abstraction.

Rules:

-   Rejecting a candidate as a Principle does NOT necessarily make the
    underlying source useless as research material. It stays in the
    catalog and may inform catalog research.
-   A rejected catalog candidate, or anything derived from catalog
    material, MUST NOT be reintroduced into Design Excellence as a REF
    entry, principle, rule, or any other runtime knowledge without the
    relevant human gate (§2, §3).
-   Renaming, rewriting, reclassifying, merging, or re-abstracting
    rejected material does not bypass the integration gate. If an idea
    traces to catalog material, it is gated whatever its form.
-   Learning of a topic through catalog material is not derivation. An
    idea traces to catalog material when any of its normative clauses
    (norm, scope, thresholds, exceptions, examples, validation,
    remediation) is supported only by catalog material, is more specific
    than its independent support, or reproduces the normative content of
    a rejected or unaccepted principle in any wording. Independent
    support is the text of an authoritative source in a source family
    the Rule Catalog already admits (or one admitted through the §2
    source-family gate), Design Excellence-native evidence measuring
    Design Excellence's own behaviour, or an existing Design Excellence
    entry other than a Principle Pool entry (Principle Pool content
    crossed from the catalog under the Integration Contract and never
    supports a rule). Evidence gathered with criteria written from
    catalog material can show a failure; it cannot supply a norm.
    Runtime knowledge whose every normative clause has independent
    support, and which carries no catalog content, is not
    catalog-derived: it enters only through the ordinary §2 human
    authorization, whose request discloses the catalog surfacing and any
    overlap with rejected principles, and whose milestone report records
    a clause-by-clause provenance trace, which the milestone's §8
    reviewer checks. A clause that fails this test is dropped or stays
    gated. This creates no route for catalog material itself to cross.
-   Do not expand the Principle Pool merely to increase its count.

When evaluating references, ask: Is the source legally and operationally
usable? Is it relevant to a real design problem? Can its useful
decisions be inspected? Can those decisions be adapted without copying
identity? Does it add meaningful possibility beyond the existing
library? If it fails Principle admission, where does it remain useful,
without crossing the gate?

## 5. Closed Branches

These branches are hard-closed:

-   **Licensed reference library code curation**: closed in Phase 16.
    No further code-product discovery or curation batches for the
    Principle Pool.
-   **Public-sector reference family**: closed for Principle Pool
    discovery in Phase 19. No further acquisition, sampling, or
    screening for the pool.
-   **Licensed reference library design-file fallback** (curating its
    design source files instead of its code): not authorized.

**Human-authorized reopening (2026-09-28, Completion Sprint only).**
Exact text: "Autorizo reabrir la biblioteca de referencia licenciada
(demos en vivo de themes-links.md y archivos Figma de figma-links.md)
para el Completion Sprint, y autorizo que los principios abstraídos,
sin identidad de fuente, entren en visual-references.md /
principle-pool.md, con mi revisión final de cada entrada antes del
commit." Scope: the live demos listed in `themes-links.md` and the
design files listed in `figma-links.md` only. The authorization covers
inspection and the proposal of identity-free entries into those two
files, within their own ceilings and schemas. It does not cover the
external catalog (never written) or any other source, and each entry
waits for the human's review before commit.

Reopening any of them requires explicit human authorization. Governance
is not limited to new families: any acquisition or curation batch in
any family, new, existing, or previously closed, requires a milestone
that explicitly authorizes it.

Reading existing reports and records for an authorized audit is not
reopening a branch.

`STATE.md` mirrors this list. Only a human changes either copy. If the
copies differ, the more restrictive reading applies and the loop stops
for a human.

## 6. One Milestone Per Run

Autonomous execution is strictly bounded to ONE milestone per run: the
milestone explicitly named and authorized in `STATE.md`.

The loop may complete it, fail it, reject its hypothesis, mark it
unresolved, or stop at a gate or budget, and update `STATE.md` with the
result. Status values: `READY`, `IN PROGRESS`, `COMPLETED`, `REJECTED`,
`FAILED`, `UNRESOLVED`, `BLOCKED` (human gate), `BUDGET-STOPPED`.

It MUST NOT autonomously start another milestone. Starting a milestone
not already authorized in `STATE.md` is a human gate. A terminal status
ends autonomous work: `Next action` becomes a request for human
authorization, which may include a recommendation. A recommendation is
not an authorization.

An interrupted `IN PROGRESS` milestone may resume in a later run. A
milestone `BLOCKED` only on a pending §2.1 escalation question resumes
when the human answers it.
Iterations and elapsed time carry over; they do not reset.

## 7. Self-Modification

Changes to any of the following require explicit human authorization:

-   `loop.md`;
-   the governance structure of `STATE.md` (its fields, current
    milestone, authorization status, objective, hypothesis, budget, and
    closed branches);
-   autonomy boundaries;
-   human-gate definitions;
-   iteration limits and budgets;
-   repository authority definitions.

The loop may update only the operational fields of `STATE.md`:
iteration, status, blockers, pending human gate, and next action.

An authorization to edit these files applies only to the milestone that
received it. Later runs must not infer it. Recording a human-given
milestone authorization in `STATE.md` (milestone name, exact text,
scope, objective, hypothesis, and a budget as given by the human or the
§11 defaults) and that milestone's result is covered by that
authorization (§1 step 2).

## 8. Independent Review

Any autonomous milestone whose output is a verdict about architecture,
governance, source-family viability, reference admission, integration,
or strategic direction requires one fresh, read-only, blind independent
reviewer before completion.

-   The reviewer receives only the evidence and the question needed. It
    does not receive the main agent's verdict or prior rejection
    history when blind review is appropriate. Blind is the default; if
    the question requires history, record why in the report.
-   The main agent reconciles and records every disagreement. It never
    silently overrides the reviewer. An unreconciled disagreement makes
    the outcome `UNRESOLVED` or a human gate. A reviewer finding whose
    fix lies within scope is fixed and revalidated autonomously
    (§2.1); it is not a disagreement.
-   Critique of design output continues to follow Design Excellence's
    own critique protocol.

## 9. Agent Delegation

The main agent owns execution, synthesis, reconciliation, and final
decisions within authorized scope.

Subagents are optional and bounded: 0 to 1 for ordinary work, 1 to 2
for complex work, 3 at most, the §8 reviewer included. Never use agents
merely to increase throughput.

For autonomous-loop execution, `loop.md` governs agent delegation
within the authorized milestone. Global agent rules remain applicable
unless they conflict with an explicit loop safety or bounded-autonomy
constraint. If such a conflict cannot be resolved deterministically,
stop and request human authorization.

Subagents are read-only by default and have independent, non-overlapping
responsibilities. Never allow parallel agents to write to the same
governed artifact. The main agent reconciles all subagent findings
before modifying shared state.

## 10. Scope Discipline

The loop governs milestone-level autonomy. Design Excellence's internal
task routing and pipeline remain authoritative in `SKILL.md`.

Do not create micro-milestones for ordinary execution.

## 11. Iteration Limits and Budgets

A **meaningful iteration** is one bounded experimental or investigative
attempt that produces new evidence.

Defaults, unless `STATE.md` sets a lower limit (raising one is a human
gate, §7):

-   maximum **5 meaningful iterations per authorized milestone**;
-   autonomous wall-clock budget: **60 minutes per milestone**;
-   active troubleshooting cap: **10 minutes per individual
    external/build/render problem**, unless the milestone explicitly
    authorizes another cap.

Corrective passes on a problem found within an iteration (§2.1:
repair, revalidation, reviewer reconciliation) belong to that
iteration; they are not new meaningful iterations. A pass that
produces new evidence about the hypothesis is a meaningful iteration.
Wall-clock budgets still apply to all passes. Reaching the
per-problem troubleshooting cap ends work on that problem, not the
milestone: record it and continue with the safest in-scope
alternative, or close with it documented. Only the iteration and
wall-clock budgets produce `BUDGET-STOPPED`.

If a budget is reached, stop and report (`BUDGET-STOPPED`).

If the same hypothesis fails twice for the same structural reason, stop
and reassess rather than repeating the experiment. If three consecutive
verified candidates fail for the same documented structural reason,
stop that branch.

Never create an infinite loop.

## 12. State Model

`STATE.md` is the single authoritative operational state for the loop.
It contains only: control-plane repository, current milestone,
authorization (status, exact text, scope), objective, hypothesis,
iteration, budget, status,
blockers, pending human gate, next action, and closed branches.

There is no `DECISIONS.md` or `REVIEW.md`. Milestone evidence,
decisions, validation, critique, limitations, and conclusions go in the
milestone report under the existing report convention of the repository
the milestone belongs to: catalog milestones in the catalog's phase
reports, Design Excellence milestones under `benchmarks/`.

Do not duplicate a fact across files. `STATE.md` points to the report;
it does not restate it.

## 13. Failure Handling

When a tool, build, source, reviewer, or experiment fails: 1. classify
the failure; 2. determine whether it affects the hypothesis; 3. attempt
only bounded remediation within the §11 caps; 4. record the remediation;
5. retry only when the retry can produce materially new evidence
(transient failures: see below).

Distinguish:

-   **technical failure**: the experiment could not be executed;
-   **evidence failure**: execution succeeded but evidence is
    insufficient;
-   **hypothesis failure**: evidence contradicts the hypothesis;
-   **governance failure**: the process violated an established rule.

Never silently convert one category into another.

A retry after a transient or tool failure (timeout, dropped connection,
flaky command) needs no new evidence to be justified and no human
permission (§2.1 case E). A failure that stays within scope is
investigated, repaired and revalidated autonomously; only one whose
resolution crosses the §2.1 human boundary is escalated, with the §2.1
question.

## 14. Change and Commit Discipline

Before modifying any file: inspect current state; identify the exact
rule being changed; confirm the change is authorized; make the smallest
coherent change; validate; critique when required; review the diff.

Existing systems are preserved by default. Do not replace an existing
system because a new library or technique is available. Do not
introduce a dependency merely because it simplifies implementation.

Commit once per completed milestone, not once per iteration, containing
only that milestone's intended files. Do not commit merely because an
iteration occurred. Never commit disposable captures, work copies,
dependencies, generated noise, or unrelated modifications. Never push
automatically.

## 15. Anti-Gaming Rules

Never optimize for: number of principles created; number of files
changed; number of experiments completed; number of sources acquired;
number of commits; percentage of successful candidates.

A zero-yield experiment is a valid successful outcome when it correctly
falsifies a hypothesis.

Do not lower an admission bar because a batch produced no results.

Do not invent novelty, evidence, applicability, user value, or design
rationale.

Do not convert a known pattern into a principle merely by changing its
wording.

Do not continue searching after a predefined stopping condition unless
new evidence could materially change the hypothesis.

## 16. Completion Contract

A milestone is complete only when: its objective is answered; its
hypothesis is accepted, rejected, or explicitly unresolved; evidence is
recorded; validation passes; required independent review (§8) is
complete; limitations are documented; `STATE.md` is consistent with the
report; the next action is explicit; no unauthorized work remains
pending.

After completion, do not invent additional work. If the correct result
is **STOP**, stop.

## 17. Human Handoff

When a human decision is required, produce: 1. what was tested; 2. what
the evidence says; 3. what changed; 4. what did not change; 5. the
strategic decision required; 6. the available options and concrete
consequences; 7. the information needed to make the decision.

Record the gate in `STATE.md` and do not continue autonomously past it.

This handoff is for a strategic decision at the end of a milestone, and
for §3 and §5 gates. A single out-of-scope action needed inside an
authorized milestone uses the §2.1 escalation question instead, with no
report before it.

## 18. Current Strategic Context

The strategic question is the relationship between: the licensed
reference library; the external reference catalog; observations; the
Principle Pool; and runtime consumption by Design Excellence.

Do not assume Principle Pool growth is the objective. The licensed
reference library remains the original source of the commercial
reference family.

The current milestone, its objective, and its authorization are defined
in `STATE.md` only. Do not begin any reference acquisition until that
architectural question has been investigated, documented, and a human
has authorized a next step. The human authorized one such step on
2026-09-28: the scoped reopening recorded in §5.

## 19. Loop Safety

At the start of every run: read `STATE.md`; confirm authorization (§1
step 2); check git status; read the previous report; confirm the current
hypothesis is still valid.

At the end of every run: write the result; validate the state; commit
only if the milestone completed (§14); record the next action; stop.

Never push automatically. Never claim completion without evidence. Never
fabricate evidence. Never hide failed experiments. Never weaken a
criterion solely to obtain a positive result.
