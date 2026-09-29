# Design Excellence

**A Claude Code skill that decides what kind of design job it is facing before it styles anything.**

Design Excellence is one design decision engine for building, redesigning, polishing, critiquing and auditing frontend interfaces: websites, landing pages, dashboards, product UI and components. It is for developers and designers who use Claude Code for frontend work and want the result to follow from the brief rather than from the model's defaults.

- **Sized to the task.** A button fix stays a button fix. A new site gets the full pipeline.
- **Classifies before it generates.** Register, genre and three design dials are settled before any visual decision.
- **Remembers per project.** Decisions live in `.design/context.md` inside your project, so they survive across sessions.
- **Safety above taste.** Accessibility floors, non-destructive editing and no invented data outrank aesthetic preference.
- **Honest about checks.** A check it cannot run is reported as skipped, never as passed.

## Why Design Excellence

AI-generated interfaces tend to converge: the same hero, the same card grid, the same accent palette, the same eyebrow labels. Most of this is not bad design. It is the same unconsidered default, reached for every time.

Design Excellence treats that as a process problem. It routes each request to the smallest pipeline that fits, forces the classification and direction decisions to happen explicitly, records them, and checks the result against named, dated patterns of generic output. It enforces a process; it does not promise a particular aesthetic outcome.

## Quick start

The installable skill is the `design-excellence/` folder. Everything else in this repository is documentation, evidence and maintainer tooling.

Install it to `C:\Users\<user>\.claude\skills\design-excellence`. In PowerShell:

```powershell
git clone https://github.com/lexsantor/design-excellence.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse design-excellence\design-excellence "$HOME\.claude\skills\design-excellence"
```

To update, delete the installed folder and copy it again. Other installation paths are not documented here because this repository does not currently verify them.

Then ask Claude Code for frontend design work in plain language. The skill applies to building, redesigning, polishing, critiquing or auditing an interface, for example:

- "Add a testimonial section to this page."
- "Make this hero less generic."
- "Fix the mobile navigation."
- "Propose two directions for the landing page, but don't build anything yet."

The first thing a run states is its classification:

```text
Reading this as: [scope] [task mode] on a [project state] project.
```

Build and redesign runs then create or update `.design/context.md` in your project.

## How it works

Every request is classified on three independent axes before anything else happens.

| Axis | Values |
|---|---|
| Scope | component, section, page, multi-page site, existing product |
| Project state | genuinely empty, existing, existing requiring redesign, existing requiring polish |
| Task mode | BUILD, REDESIGN, POLISH, CRITIQUE, AUDIT, DISCOVER |

The task mode decides which stages run, from a fixed sequence (understand, inspect, audit, define, direct, shape, design, build, validate, critique, refine, harden, ship):

| Task mode | What runs |
|---|---|
| BUILD | The full pipeline on an empty project; on an existing one, it reuses recorded decisions and extends them |
| REDESIGN | The full pipeline with a heavy inspection and audit, mandatory existing-project safety, and independent critique by default |
| POLISH | A narrow pass: inspect, build, validate and critique only the touched area |
| CRITIQUE | Inspect, then a critique report as the deliverable |
| AUDIT | Inspect, then a read-only findings report |
| DISCOVER | Inspect, then at most 5 to 7 gap findings plus the candidates it rejected |

A component-level polish has no path into direction, design, hardening or fingerprint checks. The requested deliverable can also end a run early: "directions only" returns candidates and stops, "choose / prepare" commits to one and stops before building.

**Register, genre and dials.** For BUILD and REDESIGN, the define stage settles:

- **Register**, the permission ceiling: `brand-led`, `product-led` or `hybrid`.
- **Genre**, the default posture: `editorial`, `modern-minimal`, `atmospheric-expressive` or `playful`. The choice must be justified by the brief's own language, not by a category stereotype.
- **Dials**, scored 1 to 10 and read in bands (low, medium, high): `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`. Register caps them. Rules consume bands, never raw numbers.

**Project memory.** `.design/context.md` lives in your project, never in the skill. Its frontmatter records the classification; its body holds Product Truth, the visual system, preserved patterns, known exceptions, rejected directions, fingerprint history, and accessibility and responsive notes. Rejected directions and fingerprint history are append-only.

The full specification is [`design-excellence/SKILL.md`](design-excellence/SKILL.md).

## How it avoids generic output

These are mechanisms, not guarantees.

- **Defaults are not choices.** A pattern is not bad in itself. Using it without considering it is.
- **Anti-slop registry.** 19 named patterns of generic output (for example uniform card grids, gradient headline text, reflex typefaces, category-reflex palettes). Each entry states where it does and does not apply, and each is dated with a 90-day review interval; an entry past its date is treated as needing review, not as settled fact.
- **Two directions before one.** For page-level builds and redesigns, the direct stage sketches two candidate directions before committing. The rejected one is logged with its reason and must differ on at least two of composition, imagery, typography, color, materiality and interaction.
- **Concept detection.** The define stage records whether the brief contains real evidence of a guiding concept, a hypothesis the model raises itself, or neither. Only a concept the brief supports, or one you explicitly ask for, may drive structure; a hypothesis is never logged as evidence.
- **Visual references and principle pool.** Two small, curated pools of abstracted design principles, used only while exploring a new visual direction and never as a quality bar. The rule is: observe, abstract, adapt, never copy. Entries carry no source identity, have hard size ceilings (10 and 15) and expire unless re-verified. Considering an entry and rejecting it is a valid outcome.
- **Visual fingerprint (experimental).** Each generation records five dimensions: macrostructure, typography pairing, color anchor, density band and motion tier. If fewer than two differ from each of the project's last five entries, the skill proposes an alternative. It is a redirect signal, never a block, and it only compares within one project.

## Safety gates

Conflicts are resolved by a fixed precedence:

| Layer | Meaning |
|---|---|
| P0 | Product truth: the substrate everything else is scoped by |
| P1 | Safety and correctness: narrow and enumerated |
| P2 | Explicit user instruction |
| P3 to P8 | Register and genre, existing system, usability, distinctiveness, performance, aesthetics |

P1 contains only four items: accessibility floors (contrast, visible focus, keyboard operability, reduced-motion respect), no fabricated data or invented metrics, no treating untrusted content as instruction, and non-destructive editing of existing code. When P1 overrides an explicit instruction, the change is the minimum necessary and is disclosed in one line.

In practice:

- **Existing projects are inspected first.** Replacing rather than extending (restructuring more than half a file, or adding a dependency that duplicates existing tooling) needs your explicit confirmation.
- **Missing facts stay missing.** Figures, names and testimonials you did not supply become labeled placeholders, not plausible fabrications.
- **Context is data.** `.design/context.md`, fetched pages and text inside a pasted brief are never followed as instructions.

These gates govern what the skill does. They are not a guarantee that the output is accessible or correct; verify shipped work yourself.

## What loads and when

`SKILL.md` is always loaded. Everything else loads only when the routed task needs it.

| Reference | Loads when |
|---|---|
| Rule catalog: 57 rules in 7 categories (accessibility, color, content and copy, layout and interaction, motion, performance and hardening, typography) | The category is in scope for the task |
| Existing-project safety, critique protocol | The project is not empty; the critique stage runs |
| Anti-slop registry | Critique or audit, a new visual system, or a request that is about genericness |
| Style catalog: 4 demonstration entries, one per genre (a schema, not a catalog) | Critique or audit, or a new visual system |
| Visual references (9) and principle pool (5) | Exploring a new visual direction only |
| Gesture physics (5) | Drag or gesture interaction is in scope |
| Three implementation-source guides (icons, motion, components) | That need is already established and your project or instructions do not already cover it |

The implementation-source guides decide when a source is appropriate but do not verify package names or APIs. Before anything is installed from them, the skill names the exact package and asks for your confirmation. No stack-specific guides ship.

## Core and Enhanced checks

- **Static checks** (for example font-family count, or contrast between color tokens declared in code) always run and gate delivery.
- **Rendered checks** (for example wrapped button text, line length, text over images, runtime metrics) need a session that can render the page in a browser. This is Enhanced mode.
- **Without that capability**, rendered checks are reported as skipped because the capability is unavailable. They are never counted as passed.

## Limitations and non-goals

- **Claude Code only.** No other agent or platform is supported by the repository's evidence.
- **The visible register, genre and dials line is best-effort.** It does not always appear before the first file is written. The recorded values in `.design/context.md` are the reliable record.
- **The visual fingerprint is experimental** and compares only within one project.
- **The anti-slop registry is dated.** It targets current model defaults and needs periodic manual review; no automated check covers its freshness.
- **Independent critique depends on the host** being able to run an isolated reviewer.
- **Small catalogs by design.** No stack guides, no large style or font databases, and the style catalog holds four demonstration entries.
- **No live browser-editing pipeline.**
- **No guarantee of distinctive or accessible output.** The skill enforces a process and discloses what it could not check.

Deliberate non-inclusions and deferred scope are documented in [`architecture/ARCHITECTURE.md`](architecture/ARCHITECTURE.md) (section 23).

## Evidence

The skill has been developed against behavioural benchmarks run in fresh sessions, with independent review of changes.

In the final end-to-end check, two neutral briefs (a back-office screen and a one-page site) each ran one complete build with the installed skill. Both runs reached delivery, recorded their classification in `.design/context.md`, read the reference pools before building, and copied none of the entries' literal markers. In neither run did the visible classification line appear, which is why it is documented as best-effort above.

That is one run per brief: evidence that the workflow runs end to end, not a success rate. Reports are in [`benchmarks/`](benchmarks/).

## Repository structure

| Path | What it is |
|---|---|
| [`design-excellence/`](design-excellence/) | The skill. The only folder you install |
| [`architecture/`](architecture/) | Original research and architecture: design history and rationale, not runtime files |
| [`benchmarks/`](benchmarks/) | Evidence and validation reports |
| [`proposals/`](proposals/) | Earlier design proposals |
| [`tools/`](tools/) | Maintainer tooling, including the reference-pool checker |
| `loop.md`, `STATE.md`, `CLAUDE.md` | Repository maintenance and governance material |

## Contributing

Issues are welcome, especially reproducible cases where the skill misroutes a request, skips a gate or produces a registry pattern without considering it. Pull requests are reviewed against the repository's change discipline, so open an issue first for anything beyond a small fix.

Changes to the skill are expected to:

- **Keep one rule in one place.** Rules are referenced by id everywhere else, never restated.
- **Be evidence-backed.** Behavioural changes need evidence that the change is warranted.
- **Carry freshness data** where the knowledge is time-bound, such as registry and pool entries.
- **Pass the reference check** when the visual references or principle pool change: `python tools/check-references.py` exits non-zero on any schema, ceiling, freshness or identity failure.
- **Be reviewed before merging.**

## License

[MIT](LICENSE)
