# Gesture Physics (T4)

Loaded only when a drag/gesture interaction is actually in scope for the current task — never as part of the default Motion loading path (`motion.md` step 10 points here explicitly; nothing else in this skill references these formulas). Source: Emil Kowalski's `apple-design`/`emil-design-eng` material, per `FORENSIC-EXTRACTION.md` §7 — the strongest physically-grounded, copy-pasteable content found across all six sources.

---

### GESTURE-001 — Velocity-based dismissal threshold
- **category:** interaction · **layer:** P5 · **severity:** moderate
- **principle:** compute velocity as `|distance| / elapsedMs`; dismiss the gesture above a threshold of roughly `0.11`, regardless of total distance traveled — a fast flick should be enough even if the finger didn't move far. Combine with damping/rising friction at drag boundaries instead of a hard stop, capture the pointer once dragging starts, and ignore extra touch points mid-drag.
- **applicability:** any drag-to-dismiss or swipe interaction (bottom sheets, dismissible cards, drawers).
- **evidence:** matches how quality bottom-sheet/carousel implementations actually feel; a purely distance-based threshold misses fast, short flicks.
- **freshness:** status: permanent.
- **validation:** manual (implementation-level, not mechanically checkable from static source).
- **remediation:** n/a — this is a construction formula, not a violation-checkable rule.

### GESTURE-002 — Momentum-projection formula
- **category:** interaction · **layer:** P5 · **severity:** minor
- **principle:** project where a released gesture will settle using exponential decay, not textbook `v² / (2·decel)`: `projectedDistance = (velocity / 1000) · decayConstant / (1 − decayConstant)`, with `decayConstant ≈ 0.998`.
- **applicability:** any momentum-scrolling or fling-to-position interaction.
- **evidence:** matches the feel of high-quality native momentum scrolling more closely than the textbook physics formula.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** n/a.

### GESTURE-003 — Rubber-band resistance at drag boundaries
- **category:** interaction · **layer:** P5 · **severity:** minor
- **principle:** `resistedOvershoot = (overshoot · dimension · constant) / (dimension + constant · |overshoot|)` — produces the characteristic "harder to pull the further past the edge" feel instead of a hard stop or unresisted overscroll.
- **applicability:** any interaction with a draggable boundary (pull-to-refresh, bounded carousels, dismissible sheets).
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** n/a.

### GESTURE-004 — 2D drag decomposed into independent X/Y springs
- **category:** interaction · **layer:** P5 · **severity:** minor
- **principle:** for two-dimensional drag, run independent spring simulations on the X and Y axes rather than one combined vector spring — a single combined spring desyncs visibly when the two axes have different velocities at release.
- **applicability:** any free 2D drag interaction (not applicable to single-axis drag/swipe).
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** n/a.

### GESTURE-005 — Relative-velocity spring handoff
- **category:** interaction · **layer:** P5 · **severity:** minor
- **principle:** when a spring animation is interrupted mid-flight by a new gesture, hand off using the *relative* velocity between the gesture and the animation's current trajectory (`gestureVelocity / (target − current)`), not the gesture's raw velocity alone — this is what makes an interrupted spring feel continuous rather than "brick-walled."
- **applicability:** any interruptible spring-driven animation (cross-reference `MOTION-006`).
- **evidence:** the mechanical reason springs — not CSS transitions — are the correct tool for anything gesture-interruptible.
- **freshness:** status: permanent.
- **validation:** manual.
- **remediation:** n/a.
