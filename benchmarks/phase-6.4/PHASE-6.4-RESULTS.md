# Phase 6.4 — Results
## Visual References: Control vs Test

**Status:** Phase completed  
**Benchmark:** Clínica Atlas  
**Arms:** A — Control / B — Test  
**Purpose:** Determine whether the Visual References capability materially expands the design possibility space during DIRECT / EXPLORE without creating copying, forced usage, or new convergence.

---

## 1. Executive conclusion

Phase 6.4 validated the **Visual References mechanism**, but not the sufficiency of its current reference pool.

The implementation works as intended:

- references can be loaded conditionally;
- compatibility can eliminate references before use;
- references are optional rather than quota-driven;
- abstract principles can influence candidate generation;
- references can influence a candidate that is ultimately rejected;
- adopted references can be adapted rather than copied;
- Visual References integrate with EXPLORE without becoming a new pipeline stage;
- Anti-Slop, Register/Genre, Dials, and Concept → Structure remain separate mechanisms.

The strongest evidence is REF-003 in Arm B: an abstract principle around bounded-set wayfinding produced an enumerated navigation model that shipped. This is a genuine design decision that plausibly would not have emerged from the Editorial genre defaults alone.

However, the experiment also exposed a significant limitation:

> The current six-entry reference pool is heavily editorial-coded.

As a result, Visual References broadened the **mechanism space** more clearly than the **visual/genre possibility space**. Both candidates remained within adjacent premium-editorial territory.

Therefore:

**Phase 6.4 implementation: validated.**  
**Visual Reference catalog: needs diversification.**  
**Architecture: keep. Do not replace LAYOUT-010 or add a new pipeline stage.**

---

## 2. Benchmark conditions

### Arm A — Control

- Same Clínica Atlas brief.
- Same current design-excellence skill.
- Visual References deliberately unavailable to the execution path.
- No Phase 6.2/6.3/6.4 results used as design guidance.
- Fresh, genuinely-empty project.

### Arm B — Test

- Same Clínica Atlas brief.
- Same current design-excellence skill.
- `references/visual-references.md` available.
- No additional project-local visual references.
- No prior phase results used as design guidance.
- Fresh, genuinely-empty project.

The comparison therefore isolates the availability of the Visual Reference capability as closely as the benchmark environment permits.

---

# 3. Arm A — Control findings

Arm A executed the full greenfield pipeline through Level 2 critique and refinement.

The two EXPLORE candidates were genuinely different:

### Candidate A — The Spine Line
- asymmetric editorial grid;
- persistent structural axis;
- serif + sans;
- warm-stone / ink-indigo palette;
- static structural anchor;
- abstract line motif.

### Candidate B — The Adjustment
- scroll-driven structural reorganization;
- geometric sans;
- cooler slate;
- denser tile-based composition;
- interaction carrying the concept.

The candidates differed across all six declared exploration dimensions.

Candidate A was selected because the brief explicitly called for low motion and Candidate B depended heavily on scroll-triggered structural reflow.

### Concept → Structure

The Atlas name was interpreted as the C1 vertebra and translated into a persistent spine line.

Level 2 critique identified an important weakness: the first spine line was structurally real but visually indistinguishable from a generic editorial margin rule.

REFINE added joint ticks at section boundaries, giving the concept a more formal expression independent of explanatory copy.

### Key control result

Arm A established that the current skill can already generate two meaningfully different directions without Visual References.

However, it still converged toward a recognizable premium editorial / professional-services vocabulary.

---

# 4. Arm B — Test findings

Arm B also executed the full greenfield pipeline.

Visual References were explicitly considered and filtered.

| Reference | Outcome |
|---|---|
| REF-001 | Constructively informed Candidate A, which was later rejected |
| REF-002 | Discarded because its motion requirements conflicted with Low MOTION_INTENSITY |
| REF-003 | Constructively influenced Candidate B and the shipped navigation |
| REF-004 | Minor carrier-level influence through numerals |
| REF-005 | Discarded because applying process imagery would require unavailable/fabricated material |
| REF-006 | Discarded because its motion requirements conflicted with Low MOTION_INTENSITY |

No reference was forced into the final design.

No literal-copy outcome was identified.

---

# 5. Strongest evidence: REF-003

REF-003 described a wayfinding pattern where navigation behaves as an index of a bounded set rather than simply a menu.

The abstracted principle was:

> navigation framed as “where am I in a bounded set” rather than “where can I go”.

This became:

- `01 Inicio`
- `02 Tratamientos`
- `03 El centro`
- `04 Sobre nosotros`
- `05 Contacto`

The implementation used the project's own typography, color, mechanics, and responsive behavior.

This is the clearest evidence that Visual References can generate a meaningful design possibility rather than merely decorate a preselected direction.

---

# 6. What Visual References changed

The evidence supports three distinct effects.

### 6.1 Candidate generation

REF-001 helped produce a genuine Candidate A rather than a token alternative.

It was ultimately rejected, but it materially affected the EXPLORE search space.

### 6.2 Structural/navigation possibility

REF-003 introduced a navigation model that was not a natural consequence of the Editorial genre alone.

This is the strongest demonstrated capability of Phase 6.4.

### 6.3 Discriminative filtering

Three references were rejected on concrete grounds:

- motion-intensity mismatch;
- fabrication risk;
- incompatibility with the available content.

This confirms that Visual References are not operating as “use everything available”.

---

# 7. What Visual References did NOT solve

Visual References did not eliminate the broader premium-editorial convergence.

Arm B's final design still contained:

- numbered index navigation;
- folio numerals;
- hairline rules;
- zero-radius materiality;
- asymmetric editorial grid;
- restrained accent;
- editorial typography.

The independent critique described this as an emergent “AI premium editorial” pattern.

The benchmark therefore exposes an important distinction:

> Visual References can broaden design mechanisms while still leaving the overall visual-language family constrained.

The current pool is the likely limiting factor.

---

# 8. Control vs Test

| Dimension | Arm A — Control | Arm B — Test |
|---|---|---|
| EXPLORE candidates | Genuinely different | Genuinely different |
| Concept → Structure | Active | Active |
| Reference influence | None | Demonstrated |
| Candidate generation | Strong | Strong |
| Reference filtering | N/A | Demonstrated |
| Literal copying | N/A | None observed |
| Navigation possibility | Conventional editorial navigation | Enumerated bounded-set index |
| Overall visual family | Premium editorial | Premium editorial |
| Macrostructure convergence | Present | Still present |
| Genericness risk | Present | Present |
| Production/critique quality | Strong | Strong |
| Visual-reference mechanism | N/A | Validated |
| Genre-space expansion | N/A | Limited |

The important comparison is not “B is better than A”.

The useful conclusion is:

> B demonstrated an additional source of design possibility that A did not have, but the additional possibility remained largely inside the same editorial-coded visual universe.

---

# 9. Critical finding: reference-pool bias

The current six references are predominantly related to:

- documentation;
- editorial composition;
- specimen/index navigation;
- print-derived typography;
- portfolio/case-study interaction;
- process/editorial imagery.

This creates a risk:

```text
Visual References
        ↓
Editorial-coded reference pool
        ↓
Editorial candidate generation
        ↓
Premium editorial convergence
```

This does not mean the Visual References architecture is wrong.

It means the data supplied to that architecture is too narrow.

The next iteration should therefore diversify the reference pool rather than redesigning the mechanism.

---

# 10. Critical finding: Concept Detection governance

Both arms inferred a concept from the brand name “Atlas”.

The interpretation was:

`Atlas → C1 vertebra / foundational support → structural reference point`

This produced useful design work, but it exposes a governance question.

The Phase 6.3 architecture defined Concept → Structure as requiring meaningful concept evidence from the brief. A brand name alone may be insufficient evidence if the brief does not indicate that the name is intended as a conceptual design anchor.

This should be resolved before the next benchmark.

Recommended future behavior:

- a brand/name can activate Concept → Structure when the brief explicitly explains or foregrounds the name's conceptual meaning;
- or when the user explicitly asks the system to embody the brand/name concept;
- otherwise, a semantic association may be proposed as a hypothesis during exploration, but should not automatically be treated as detected concept evidence.

This is a governance refinement, not a reason to remove Concept → Structure.

---

# 11. Benchmark contamination discovered

Both arms identified a contamination risk in:

`references/style-catalog.md`

An entry reportedly contains a `best_for` reference to:

> “a calm, serene chiropractic clinic brief”

This appears to reference prior Clínica Atlas benchmark history.

Both runs explicitly detected and disregarded this material during reasoning.

This is nevertheless a structural risk because project-specific benchmark conclusions should not become part of the reusable skill's generic reference knowledge.

Before future benchmark runs, the source of this entry should be traced and, if confirmed as benchmark residue, removed or isolated.

---

# 12. What was validated

### Validated

- Visual Reference loading path.
- DIRECT / EXPLORE integration.
- Optional reference usage.
- Compatibility filtering.
- Evidence-based rejection.
- Observe → Abstract → Adapt.
- Reference influence on candidate generation.
- Reference influence on shipped design.
- Reference influence on rejected candidates.
- Adaptation without literal copying.
- Independence from Anti-Slop.
- Independence from Register/Genre.
- Independence from the three dials.
- Compatibility with Concept → Structure.
- No need for a new pipeline stage.
- No need for a scoring system.
- No need for a reference quota.

### Not yet validated

- Whether a sufficiently diverse reference pool can reliably expand the visual-language space.
- Whether references can prevent premium-editorial convergence.
- Whether a larger or more diverse pool introduces undesirable style contamination.
- Whether brand-name inference should activate Concept → Structure automatically.

---

# 13. Architectural conclusion

Do not replace the current Visual References architecture.

Keep:

```text
DIRECT / EXPLORE
      ↓
Visual Reference Evidence
      ↓
Observe → Abstract → Adapt
      ↓
Candidate generation / comparison
```

Keep `LAYOUT-010`.

Keep the six-entry schema.

Do not add:

- a new pipeline stage;
- a visual-reference score;
- a classifier;
- a vector database;
- a mandatory reference quota;
- automatic style selection.

The mechanism has enough evidence to remain part of the Design OS.

---

# 14. Recommended next phase

## Phase 6.5 — Reference Diversity + Concept Evidence Governance

Two focused objectives:

### A. Diversify Visual References

Expand the reference pool deliberately across different production/design families while keeping each entry principle-based rather than style-preset-based.

The goal is not “more references”.

The goal is:

> more materially different design possibilities.

References should remain expressed as:

`Observed production behavior → abstract principle → applicability`

rather than:

`Brand/style name → copy this aesthetic`.

### B. Tighten Concept evidence

Clarify when a brand/name is sufficient to activate Concept → Structure.

Prevent the system from inventing conceptual meaning simply because a name has an interesting semantic association.

---

# 15. Explicit non-goals for Phase 6.5

Do not use Phase 6.5 to:

- redesign the entire pipeline;
- add Reicon;
- add Kinetics;
- add SmoothUI;
- add more dials;
- expand Anti-Slop;
- create a giant visual catalog;
- introduce automated aesthetic scoring;
- introduce a vector database;
- redesign Concept → Structure;
- solve every possible source of genericness.

Those capabilities can be evaluated after the current governance and reference-pool issues are resolved.

---

# 16. Final Phase 6.4 status

**Phase 6.4 implementation: SUCCESSFUL.**

**Visual References mechanism: VALIDATED.**

**Visual Reference catalog: NEEDS DIVERSIFICATION.**

**Concept evidence governance: NEEDS REFINEMENT.**

**Architecture: KEEP.**

The experiment demonstrated that Visual References can create meaningful new design possibilities without forcing usage or copying. It also demonstrated that a narrow reference pool can create a new convergence pattern of its own.

The next optimization should therefore improve the **quality and diversity of the input evidence**, not add more machinery to the pipeline.
