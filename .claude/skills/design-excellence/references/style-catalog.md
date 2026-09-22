# Style Catalog (T3)

**This is a schema template with four demonstration entries, not a catalog.** `FORENSIC-EXTRACTION.md` §21 and `ARCHITECTURE.md` §11/§23 both explicitly exclude porting UI UX Pro Max's full 88–192-row style catalog wholesale — that's infrastructure this skill deliberately doesn't take on in V1. What's worth keeping from that source isn't the row count, it's the **schema**: making a style choice accountable (explicit trade-offs stated up front) instead of a vibe call. This file defines that schema and populates it with one real, fully-specified entry per Genre (`SKILL.md` §4) — enough to demonstrate the pattern and be immediately usable, not enough to become a second catalog needing its own freshness governance.

Loaded at DIRECT/DESIGN stage for a new visual system. **Loading honesty (Phase 4 correction):** at its current size — four entries, ~700 words total — the whole file loads in one read; there is no per-genre file split to load a smaller slice from. "Sliced to Genre" means attending primarily to the one matching entry when reasoning about it, not a smaller file read. Splitting this into four separate files would be premature fragmentation for a ~700-word file with no real token savings — that becomes worth doing if this catalog grows substantially past its current four demonstration entries, not before.

**Provenance governance (Phase 6.5 addition — closes a contamination found during Phase 6.4 benchmarking):** descriptive fields such as `best_for`, `do_not_apply_to`, and `keywords` here (and `observed`, `compatible_with`, and `non_application_note` in `visual-references.md`) must not cite specific prior benchmark projects, briefs, or sessions. Historical/project evidence belongs only in rule-catalog `evidence` fields (`layout-interaction.md` etc.), whose explicit purpose is design-history justification — a different, legitimate use. A prior version of `STYLE-ATMOSPHERIC-EXPRESSIVE-01`'s `best_for` field cited this skill's own Clínica Atlas benchmark brief by description; this was benchmark residue, not architecture, and has been replaced with a generic register/genre statement.

## Schema

```
Style
├── id
├── genre                    (editorial | modern-minimal | atmospheric-expressive | playful)
├── keywords
├── color_anchor_guidance     (references COLOR-001/COLOR-004, not a fixed palette)
├── typography_guidance       (references TYPE-001/TYPE-005)
├── motion_tier_default       (references MOTION_INTENSITY band default, SKILL.md §4)
├── best_for
├── do_not_use_for
├── accessibility_risk_tier   (low | medium | high, with the specific risk named)
├── performance_cost_tier     (low | medium | high, with the driver named)
└── status                    (active | deprecated, with replacement_id if deprecated)
```

---

### STYLE-EDITORIAL-01
- **genre:** editorial
- **keywords:** hairline rules, generous margins, serif display, dense column grid, restrained accent
- **color_anchor_guidance:** Restrained-to-Committed tier (COLOR-001); single accent used sparingly against tinted-neutral ground.
- **typography_guidance:** brand-register fluid scale (TYPE-005), serif or high-contrast display face selected via the TYPE-002 procedure — never defaulted for "editorial = serif" reflexively (see anti-slop registry SLOP-014's warning against reflex selection).
- **motion_tier_default:** Low `MOTION_INTENSITY` — restraint is the point; motion, when present, is a single orchestrated reveal, not scattered.
- **best_for:** long-form content, publications, portfolio/case-study pages, brand journalism.
- **do_not_use_for:** dense transactional dashboards, high-frequency-interaction product UI.
- **accessibility_risk_tier:** medium — hairline rules and generous negative space can under-signal interactive affordances; verify focus states are not lost in the restrained palette (A11Y-002).
- **performance_cost_tier:** low — no heavy motion/effects layer by default.
- **status:** active

### STYLE-MODERN-MINIMAL-01
- **genre:** modern-minimal
- **keywords:** system-adjacent type, tight neutral palette, functional hierarchy, low decoration
- **color_anchor_guidance:** Restrained tier (COLOR-001), ≤10% accent by default.
- **typography_guidance:** product-register fixed scale (TYPE-005), 1–2 families (TYPE-001), system fonts legitimate.
- **motion_tier_default:** Low–Medium `MOTION_INTENSITY` — feedback/state-transition purposes only by default (MOTION-002).
- **best_for:** product UI, SaaS dashboards, utility tools, any product-led register work.
- **do_not_use_for:** a brief that explicitly wants visual richness/expressiveness — forcing this genre onto an atmospheric-expressive brief produces the generic "SaaS-card kit" tell (SLOP-007).
- **accessibility_risk_tier:** low — the genre's own restraint tends to support clear hierarchy and contrast.
- **performance_cost_tier:** low.
- **status:** active

### STYLE-ATMOSPHERIC-EXPRESSIVE-01
- **genre:** atmospheric-expressive
- **keywords:** committed color, layered depth, deliberate texture/material language, larger type contrast
- **color_anchor_guidance:** Committed-to-Drenched tier (COLOR-001); accent-area ceiling may explicitly exceed the 3–5% default (up to ~20–30%), declared in `.design/context.md`.
- **typography_guidance:** brand-register fluid scale, type used as an active design element for headlines, not a neutral vehicle.
- **motion_tier_default:** Medium–High `MOTION_INTENSITY` — delight-tier purposes are eligible here where they're suppressed elsewhere.
- **best_for:** brand-led hospitality/wellness/lifestyle/experiential work calling for committed color and layered depth as the register's own default expressiveness, not a toned-down version of it.
- **do_not_use_for:** product-led register work, where Register (SKILL.md §4) caps variance/density regardless of how the brief reads.
- **accessibility_risk_tier:** high — committed color and layered depth (glassmorphism, translucent stacking per SLOP-008) carry real contrast and legibility risk; A11Y-001/COLOR-007 checks are mandatory, not optional, at this tier.
- **performance_cost_tier:** medium-to-high — depends on how much of the motion/material language is actually implemented (blur, layered shadow).
- **status:** active

### STYLE-PLAYFUL-01
- **genre:** playful
- **keywords:** high color commitment, bounce/spring motion licensed, irregular/asymmetric composition, friendly type pairing
- **color_anchor_guidance:** Committed-to-Full-palette tier (COLOR-001).
- **typography_guidance:** brand-register, a wider pairing range is licensed than modern-minimal, still governed by TYPE-001's family-count discipline.
- **motion_tier_default:** High `MOTION_INTENSITY` — MOTION-011's bounce/elastic exception applies by default here (it's off by default everywhere else).
- **best_for:** consumer-facing, youth-oriented, or deliberately informal brand-led work.
- **do_not_use_for:** any product-led register task — Register's ceiling caps this genre's own defaults down when combined with product-led register.
- **accessibility_risk_tier:** medium — high motion intensity makes MOTION-007 (`prefers-reduced-motion`) enforcement especially load-bearing here, not optional polish.
- **performance_cost_tier:** medium — more animation surface area to keep on compositor-friendly properties (MOTION-004).
- **status:** active
