---
type: result
id: relational-integration-rung-ii
title: Rung (ii) — both models INTEGRATE a compatible earlier turn rather than overwriting it; the non-terminal turn survives into the recovered referent (agreements compose, thin not constituted)
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-17
updated: 2026-06-17
links:
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: supports
    target: essay/update-is-not-constitution
  - rel: refines
    target: concept/relational-meaning
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
---

# Result: rung (ii) — the earlier, non-terminal turn survives (integration, not overwrite)

> **Status: proposed (2026-06-17).** Climbs the next rung of the relational ladder named in
> [`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md). The established
> bottom rung ([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md))
> shows both models recover a **reassigned** term (turns that *conflict*) by its most-recent binding —
> a thin **OVERWRITE** rule. **Rung (ii)** asks whether an earlier, **non-terminal** turn *survives*
> when it is *compatible* with the latest (refinement, not replacement). **It does: both models
> integrate at ceiling — they compose the two turns rather than discarding the earlier one.** Still
> **thin / single-reader-recoverable**; this does **not** approach constitution. `anchor:
> internal-contrast-only` (within-model contrast over balanced content; no human-comparison claim).

## The question (precise)

[`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
**scope limit 2** lists *"non-overwrite repairs"* as untested, and
[`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md) names the rung-(ii)
signature verbatim: *"recovery that is a function of more than the max-stamp binding — measurably
sensitive to a non-terminal turn whose content an overwrite rule would throw away."* The essay's
**revision trigger (a)** turns on exactly this result. The question: when a coined term's latest
turn is **compatible** with an earlier turn (the latest *refines* rather than *replaces*), does the
recovered referent reflect **both** turns (integration — the earlier turn survives), or only the
latest (overwrite — the earlier turn is discarded)?

## Instrument (frozen; pre-run-critic-gated)

Run dir: [`experiments/runs/2026-06-17-relational-integration-rung-ii/`](../../../experiments/runs/2026-06-17-relational-integration-rung-ii/).
Design: [`relational-integration-rung-ii`](../../../experiments/designs/relational-integration-rung-ii.md).

- **Two-constraint refinement.** A coined term **DAX** is constrained over **two stamped rounds**
  about a **2×2 figure grid** (2 shapes × 2 patterns → 4 figures, e.g. `{striped triangle, striped
  circle, dotted triangle, dotted circle}`): the **earlier** round (lower stamp) gives a **shape**
  (*"DAX was a triangle"*), the **latest** round (higher stamp) gives a **pattern** (*"DAX was
  striped"*). Each constraint matches **2** of the 4 figures; exactly **one** figure is the
  **both-match target** (the striped triangle). The two constraints are *compatible* — so a rung-(i)
  overwrite rule (keep the latest pattern → 2 candidates) and a rung-(ii) composition rule (the
  striped triangle) give **different** answers. That is the whole discriminator.
- **Two arms.** **INTEG** (headline, 48/model): *"Which of your figures does DAX refer to?"* — no
  instruction to combine. **DIRECT** (on-demand gate, 32/model): explicitly restates both
  constraints and asks for the figure. DIRECT confirms the model *can* conjoin in this instrument;
  if `direct_acc < 0.80` the INTEG result is UNINTERPRETABLE.
- **Shortcut-proof by construction.** Balanced-block roster (within each 2×2 block, K=4 records cycle
  the target through all 4 figures under a Latin square). Proven at build, separately per arm: every
  constant-grid-slot follower scores **exactly 1/K = 0.25**; every fixed figure-identity preference
  scores **1/K** (within-block target uniformity; checked over all 16 constant-figure pickers +
  20 000 random orderings); **every single-attribute reader** (latest-pattern-only = overwrite;
  earlier-shape-only; each under four tie-breaks) scores **exactly 0.50**; frequency flat. So **only
  conjoining the earlier (shape) AND latest (pattern) turn can clear the 0.50 integration bar.** Six
  idealized-reader fixtures certify the verdict map (only a genuine integrator → INTEGRATION).
- **Independent pre-run critic GO** (fresh agent): reproduced the build and frozen sha256
  (`b80772e6…`, deterministic), re-derived every shortcut bound from scratch (all single-attribute
  readers exactly 0.50; the integration criterion's false-positive rate against a true-0.50 reader
  ≈ **3%**; ≥ 31/48 needed to clear), confirmed the verdict map is symmetric and not rigged, and
  ruled the design a **fresh frozen design under the already-ratified `internal-contrast-only`
  posture — no new decision owed.**
- Forced single-label elicitation; strict parse; `finish_reason == "length"` never parsed; one stern
  retry then NA; `HARD_STOP_USD = 0.50`.

## The headline (verified — numbers not altered)

Both separately-trained models integrate at ceiling — the earlier, non-terminal turn survives in
**every** trial:

| model | INTEG target (integration) rate | Wilson 95% | latest-only (overwrite) | earlier-only | neither | pick==last-line / first-line | DIRECT on-demand acc | NA | verdict |
|---|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.000 | 0.000 | 0.250 / 0.250 | **1.000** (32/32) | 0 | **INTEGRATION** |
| gemini-3.5-flash | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.000 | 0.000 | 0.250 / 0.250 | **1.000** (32/32) | 0 | **INTEGRATION** |

- **INTEG target rate = 1.000** for both, Wilson lower bound 0.926 — far above the **0.50** ceiling
  every single-attribute (overwrite or earlier-only) reader is pinned to. Beating 0.50 requires using
  **both** turns, so the earlier turn demonstrably **survived** into the referent.
- **Overwrite (latest-only) rate = 0.000.** Neither model ever discarded the earlier turn and kept
  only the latest pattern — the pure-overwrite reading was taken **zero** times.
- **earlier-only = 0.000, neither = 0.000; grid-position-following at exactly chance** (0.250 /
  0.250) — the answer is the conjunction, not a single attribute and not a position artifact.
- **DIRECT on-demand gate = 1.000** both models — conjunction is within capability in this
  instrument, so the INTEG result is interpretable (an INTEG null, had it occurred, would have been a
  genuine spontaneous-non-integration, not an inability).
- **Clean record:** 160/160 strict parses, 0 NA, 0 retried, 0 length-truncation.

**Discipline.** Independent pre-run critic GO (re-derived shortcut bounds; ruled no new decision
owed). Independent **post-run verifier** reproduced every number from raw via its own route
(re-derived each both-match target directly from the rendered grid + history lines, audited
parses/cost, confirmed the frozen sha256) — **REPRODUCED**.

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):** the models' relational update rule is **not a blind
overwrite**. When the latest turn is *compatible* with an earlier one, both models **compose** the two
— the earlier, non-terminal turn's content survives into the recovered referent, at ceiling. This is
the essay's **rung (ii)** signature ("measurably sensitive to a non-terminal turn whose content an
overwrite rule would throw away"). It fills [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
**scope limit 2** ("non-overwrite repairs" — now tested → integration) and **occupies** the rung the
essay had only mapped. Combined with the established rung (i) (overwrite when turns *conflict*), the
picture is coherent: **the latest agreement supersedes when it contradicts an earlier one, but
composes with it when the two are compatible** — a sensible, but still thin, convention-update rule.

It does **NOT** show:

- **Not rich constitution.** Per [`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md),
  rung (ii) is on the **thin / single-reader-recoverable** side of the thin/rich criterion: a single
  reader handed the record can compose the two stated constraints. Integration is a *stricter*
  dependence than overwrite, but it is **not** path-dependence (rung iii) and **not** between-agent
  constitution (rung iv). This result does not move the claim toward those rungs.
- **Not order-SENSITIVE integration.** The two constraints are *compatible*, so a **commutative**
  conjunction ("DAX is striped AND a triangle") passes this test exactly as a genuinely
  order-sensitive composition would. The headline measures whether the earlier turn **survives**, not
  whether the composition is itself non-commutative. "Order-sensitive integration" in the strong
  sense stays a further, untested refinement.
- **Not a hard task, but a live contrast.** Conjoining two compatible attributes is easy in isolation
  (DIRECT = 1.000 confirms it). The result is informative because the **overwrite alternative was
  genuinely live**: the established rung-(i) finding is that these same models *do* default to
  latest-binding-wins when turns conflict. A blind overwrite would have kept only the latest pattern
  (rate 0.50); the models instead retained the earlier turn (rate 1.000). The null was a real
  possibility; the data ruled it out. **But the triviality cuts the other way for *spontaneity*:**
  because DIRECT and INTEG are both at ceiling, the conjunction is easy enough that a ceiling on the
  spontaneous (no-instruction) arm is *weaker* evidence of genuinely spontaneous composition than a
  mid-range result would be — and it does **not** rule out overwrite behaviour under harder load
  (more turns, larger grids, or refinements that *partially conflict* rather than cleanly compose).
  The headline rests entirely on the real, pre-registered gap between INTEG (1.000) and the 0.50
  single-attribute ceiling; it should not be read as more than that.
- **Not a human comparison** (`anchor: internal-contrast-only`). No in-repo resource grounds human
  integration/overwrite at this grain; none is owed because no human contrast is asserted.

## Honesty box

- **Ceiling effect, two independent models, n=48/model INTEG.** Wilson LB 0.926, overwrite rate
  exactly 0.000, position at chance, DIRECT at ceiling, 0 NA. As clean as a behavioural contrast gets
  — but **saturated**: 48/48 censors the magnitude at the ceiling, so this establishes *direction*
  (integration over overwrite), not a finer estimate of how often integration would fail under harder
  load.
- **One operationalization.** Shape+pattern attributes, pattern-always-latest, two-round histories,
  trivially discriminable figures. Generality (shape-latest; >2 turns; partially-conflicting
  refinements; image referents; cross-family dyads) is untested.
- **Thin, not rich — and not order-sensitive.** This climbs one rung on the thin side and explicitly
  does **not** separate commutative composition from order-sensitive integration, nor approach
  path-dependence (rung iii) or constitution (rung iv).
- **Spend.** 160 finding-bearing calls + 2 liveness = **$0.10379 billed** (`usage.cost`-summed,
  0 missing), inside the $0.50 per-run hard stop and the $5.00/day cap (day total ≈ $0.222).
