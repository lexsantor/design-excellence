# Performance & Production Hardening — Rule Catalog (T2)

Layer P7 by default (production readiness); the non-destructive-editing rule is layer P1 (on the enumerated safety list in `SKILL.md` §3) and cross-references `existing-project-safety.md` rather than duplicating it.

---

### PERF-001 — Core Web Vitals essentials
- **principle:** LCP <2.5s, INP <200ms, CLS <0.1. In practice: explicit `width`/`height` on all images to prevent layout shift, batch DOM reads then batch writes to avoid layout thrash, `content-visibility: auto` for long off-screen lists.
- **category:** performance · **layer:** P7 · **severity:** major
- **applicability:** universal for any shipped web page.
- **freshness:** status: permanent (the metrics/thresholds are current web-platform standards, not source-specific opinion).
- **validation:** mechanical-countable (static: missing width/height attributes) + rendered (Enhanced mode: actual CWV measurement).
- **remediation:** add missing dimensions; defer non-critical work off the main thread.

### PERF-002 — Lazy-loaded LCP is a critical anti-pattern
- **principle:** never `loading="lazy"` the largest-contentful-paint element (typically the hero image). Fix: `fetchpriority="high"` + `preload="metadata"` (or `<link rel="preload">`) on the LCP element; lazy-load only below-the-fold media.
- **category:** performance · **layer:** P7 · **severity:** critical
- **applicability:** universal wherever a hero/primary image exists above the fold.
- **evidence:** measured cost is roughly 2× slower LCP and meaningfully more poor-experience sessions versus a preloaded hero — a concrete, persuasive number, not "optimize LCP" in the abstract.
- **freshness:** status: permanent (the mechanism); the specific benchmark figures are illustrative, not re-verified per project.
- **validation:** mechanical-countable (flag `loading="lazy"` on the detected hero/LCP candidate).
- **remediation:** remove lazy-loading from the LCP element, add `fetchpriority="high"`.

### HARDEN-001 — Extreme-input and error-scenario coverage
- **principle:** test against long/short/emoji/RTL/large-number/many-item content; against error scenarios (network failure, 4xx/5xx, validation, permission, rate-limit, concurrent edit); against i18n (RTL layout, CJK line-breaking, `Intl`-based date/number formatting, proper pluralization — not naive `s`-suffixing). Text-overflow: truncate/line-clamp/wrap explicitly chosen — see `HARDEN-003` for the specific flex/grid truncation gotcha, not restated here.
- **category:** performance · **layer:** P7 · **severity:** major
- **applicability:** ship-readiness tasks; skip for prototype/POLISH scope (per `SKILL.md` §1, HARDEN is conditional).
- **evidence:** each item names a specific, recurring failure class rather than "handle edge cases" in the abstract.
- **freshness:** status: permanent.
- **validation:** manual (a checklist walk).
- **remediation:** apply the specific fix for the failing case.

### HARDEN-002 — Non-destructive editing of existing code
- **category:** performance/production · **layer:** P1 (safety — enumerated) · **severity:** critical
- **principle:** see `existing-project-safety.md` in full — that file is the canonical, only location for this rule's content. This id exists solely so the P1 enumerated list in `SKILL.md` §3 has a concrete rule to point to; it is a pointer, not a second copy (Phase 4 correction — this entry previously restated the principle text, which violated "one rule, one place").
- **applicability:** universal whenever Project State ≠ genuinely-empty.
- **exceptions:** see `existing-project-safety.md` §2 (Improve vs. Replace).
- **freshness:** status: permanent.
- **validation:** see `existing-project-safety.md`.
- **remediation:** see `existing-project-safety.md`.

### HARDEN-003 — `min-width: 0` flex/grid overflow gotcha
- **principle:** a flex or grid child does not shrink below its content's intrinsic width by default; add `min-width: 0` (or `min-width: 0; overflow: hidden` for truncation) to allow it to shrink and let `text-overflow: ellipsis`/`line-clamp` actually work.
- **category:** performance · **layer:** P7 · **severity:** moderate
- **applicability:** universal wherever a flex/grid child contains truncating text.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag truncation CSS on a flex/grid child missing `min-width: 0`).
- **remediation:** add the missing property.
