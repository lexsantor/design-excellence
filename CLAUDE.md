# Design Excellence

## Project Context

This repository is the canonical workspace for the Design Excellence project.

Repository root:

`C:\Users\<user>\Desktop\design-excellence\`

The repository contains the Design Excellence skill, its governance, benchmarks, reports, historical research, disposable test workspaces and supporting project artifacts.

Do not assume that files outside this repository are part of the current project unless an instruction explicitly says so.

---

## Instruction Hierarchy

Before acting, identify which layer governs the requested action:

1. `loop.md` — autonomous evolution loop, authorization boundaries, milestone governance and operational state rules.
2. `STATE.md` — current operational state and authorized milestone.
3. `design-excellence/SKILL.md` — Design Excellence behavior and design pipeline.
4. Repository documentation and benchmark reports — historical evidence and project context.
5. This `CLAUDE.md` — permanent repository-level working conventions.

Do not duplicate or override rules from `loop.md`, `STATE.md` or `SKILL.md`.

When rules conflict, follow the higher-authority source.

---

## Workspace Organization

The Desktop is no longer a workspace location for this project.

All future Design Excellence workspaces, benchmarks, evidence, reports, temporary artifacts and disposable test projects MUST live inside:

`C:\Users\<user>\Desktop\design-excellence\`

Do NOT create new project folders directly under:

`C:\Users\<user>\Desktop\`

Do NOT recreate or reuse the old Desktop-level workspace paths.

Previously created Desktop-level Design Excellence workspaces have been reorganized inside this repository. Their new in-repository locations are canonical.

Before creating a new workspace:

1. Inspect the existing repository structure.
2. Reuse an appropriate existing location whenever possible.
3. Create a new subdirectory inside this repository only when necessary.
4. Keep disposable work clearly separated from governed source files.

The following external installed skill copy is intentionally outside the repository and must remain there:

`C:\Users\<user>\.claude\skills\design-excellence\`

Do not move the installed copy into this repository.

---

## Repository Areas

Treat these areas according to their purpose:

- `design-excellence/` — governed Design Excellence skill source.
- `.claude/` — repository-local Claude configuration and skills.
- `benchmarks/` — benchmark definitions, results and milestone evidence.
- `scratchpad/` — historical, experimental or disposable material.
- `STATE.md` — operational state.
- `loop.md` — autonomous-loop governance.
- `CLAUDE.md` — permanent repository-level working conventions.

Do not treat `scratchpad/` as authoritative merely because it contains copied projects, skills or `CLAUDE.md` files.

In particular, nested `CLAUDE.md` files inside historical or copied third-party material apply only to their respective nested directories and are not repository-level instructions.

---

## Change Discipline

Do not modify governed files merely to make a task easier.

Before changing architecture, governance, the Design Excellence skill, rule catalogs, benchmark methodology or other governed behavior:

- inspect the relevant governing documents;
- confirm the authorized scope;
- follow `loop.md`;
- preserve existing boundaries;
- validate the change;
- record the resulting state where required.

Do not create a new milestone without explicit human authorization.

A recommendation, proposed next step or user confirmation of a minor action does not by itself authorize a new milestone unless the governing rules explicitly treat it as authorization.

---

## Workspace Safety

Disposable experiments must remain disposable.

Do not overwrite:

- governed source files,
- previous benchmark evidence,
- historical reports,
- closed-branch artifacts,
- unrelated project files.

Prefer new isolated workspaces for experiments when reuse could contaminate previous evidence.

Do not silently delete evidence because it is no longer convenient.

If an artifact must be moved for repository organization, preserve its contents and provenance.

---

## External Resources

External references, licensed libraries, public-sector systems, UI libraries and third-party projects are not automatically authorized project inputs.

Before acquiring, importing, modifying or promoting external material, follow the relevant authorization and governance rules in `loop.md` and the Design Excellence skill.

Do not infer authorization from the mere presence of an external resource inside `scratchpad/`.

---

## Execution Principle

Work end-to-end within the authorized scope.

When an issue is discovered, follow the autonomous issue-resolution policy in `loop.md` rather than unnecessarily stopping for human input.

Do not use this file to bypass authorization boundaries.

When uncertain about scope, inspect `loop.md` and `STATE.md` before acting.