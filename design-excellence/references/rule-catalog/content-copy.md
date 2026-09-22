# Content & Copy — Rule Catalog (T2)

Copy is design material, not decoration — evaluated with the same intentionality as spacing and color, per `FORENSIC-EXTRACTION.md`'s Anthropic extraction, the strongest single source on this category.

---

### CONTENT-001 — Copy as design material
- **category:** content-copy · **layer:** P5 · **severity:** moderate
- **principle:** write from the end user's perspective, naming things by what users understand ("notifications," not "webhook config"). Default to active voice; a CTA names the exact resulting action ("Save changes," not "Submit"). Vocabulary stays identical through a flow — a "Publish" button produces a "Published" toast, never "Success!" or a different verb.
- **applicability:** universal.
- **evidence:** copy is one of the fastest ways a generated interface reads as templated, even when the visual system is strong.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (grep for a CTA's verb reappearing in its resulting confirmation state).
- **remediation:** align the confirmation copy's verb to the triggering action's verb.

### CONTENT-002 — Error-message formula
- **principle:** what happened / why / how to fix — never blame the user, never apologize performatively, no humor. Failure and empty states are "moments for direction, not mood": explain what happened and how to fix it in the interface's own voice; an empty screen is an invitation to act, not a dead end.
- **category:** content-copy · **layer:** P5 · **severity:** major
- **applicability:** universal.
- **evidence:** the formula is reusable near-verbatim as a template across error/empty-state copy.
- **freshness:** status: permanent.
- **validation:** self-critique-prompt.
- **remediation:** rewrite against the formula; add a concrete next action for empty states (what will be here / why it matters / how to start).

### CONTENT-003 — No fabricated data or invented metrics
- **principle:** stat-led layouts, comparison rows, proof bars, and testimonials must never contain a number or name the user didn't supply. Required fallback: a labeled placeholder ("—," "metric to confirm") or removing the stat slot entirely — never a plausible-sounding fabrication.
- **category:** content-copy · **layer:** P1 (safety — on the enumerated list in `SKILL.md` §3) · **severity:** critical
- **applicability:** universal — a correctness/trust issue, not a taste issue, and applies well beyond visual design to any generative content task.
- **exceptions:** none.
- **evidence:** layouts that "demand" a number in a slot cause fabrication under pressure; the fallback removes that pressure.
- **freshness:** status: permanent.
- **validation:** mechanical-countable (flag numeric/named claims not traceable to user-supplied brief content).
- **remediation:** replace with a labeled placeholder or remove the slot; disclose to the user that data is needed (per `SKILL.md` §3's P1 disclosure rule).
