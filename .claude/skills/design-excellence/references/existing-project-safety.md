# Existing-Project Safety (T2)

Loaded whenever Project State ≠ genuinely-empty (`SKILL.md` §2). Implements the inspect → preserve → modify → validate model. Directly enforces `HARDEN-002` (layer P1, on the enumerated safety list in `SKILL.md` §3) — this file is that rule's full specification.

## 1. Inspect (mandatory, before any design decision)

Ordered scan, cited with file:line where applicable, cached to `.design/preflight-cache.json`, invalidated on relevant file-mtime change or an explicit "refresh" request:

1. `.design/context.md` — read first if it exists; it supersedes re-deriving anything below from scratch.
2. Fonts — existing `@font-face`/import declarations, font-family usage.
3. Palette — existing color tokens/custom properties in use.
4. Motion-library presence — is GSAP/Framer Motion/a CSS-only approach already established.
5. Spacing scale — existing spacing tokens or a de facto scale inferable from usage.
6. Framework — package.json dependencies, config files, detected stack (feeds `SKILL.md` §7's stack-module rule).

Report back before BUILD starts: an explicit **preserve/introduce summary** — what will be preserved as-is, what will be newly introduced. This is the accountability line with the user; skipping it is the fastest way to lose their trust in what changed and why.

## 2. Improve vs. Replace

**Improve** — extending or restyling in place, reusing existing tokens/components/dependencies. Proceeds without additional confirmation once the preserve/introduce summary has been stated.

**Replace** — restructuring more than half of a file, or introducing a new dependency to solve something existing tooling already covers. **Requires explicit user confirmation before proceeding.** State exactly which files will be modified/created/deleted, and why Improve isn't sufficient, before asking.

When in doubt, default to Improve and ask before crossing into Replace — not the reverse.

## 3. Non-destructive editing rules

- Global stylesheets and shared entry points are **append-only**: preserve existing directives (`@tailwind`, `@import`, etc.), add new rules below them, reuse existing token names rather than shadowing them with a same-purpose duplicate.
- Never delete production files, routes, or components without explicit confirmation of a stated file-level plan.
- State the exact files to be modified/created/deleted **before** editing, not discovered after the fact.
- Reuse existing tokens/components/dependencies over introducing new ones for the same purpose (this skill's own Design Principle 12 in `SKILL.md` §9 — leverage over coverage — applies to the target project's codebase too, not just to this skill's own references).

## 4. Redesign-specific: what never changes silently

For Task Mode = REDESIGN (`SKILL.md` §2), populate `.design/context.md`'s Constraints & Preserved Patterns section with an explicit list before touching anything:

- URL slugs and route structure
- Form field names (breaks server-side handling and analytics if changed silently)
- Navigation labels (breaks bookmarked user mental models and SEO anchor text)
- Any markup with SEO/analytics significance (structured data, tracking attributes)

Capture this baseline before any visual change — it is the redesign's own regression contract, separate from the general Constraints list a BUILD-in-existing-project task would use.

## 5. Post-modification validation

After BUILD:
1. Re-run the Inspect scan (§1).
2. Diff the result against the Constraints & Preserved Patterns list in `.design/context.md`.
3. Confirm nothing on that list actually changed. If something did, that's a `HARDEN-002` violation — disclose it per `SKILL.md` §3's P1 disclosure rule, don't silently ship it.

This is the regression check referenced in `SKILL.md` §1 (VALIDATE stage) for any BUILD-in-existing-project or REDESIGN task.
