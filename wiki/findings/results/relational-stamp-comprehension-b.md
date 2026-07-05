---
type: result
id: relational-stamp-comprehension-b
title: The stamp-comprehension pre-probe (Option B) — both models read the round stamp as a recency value on demand; v4's position-following is comprehending-but-not-spontaneously-using, not stamp-blindness
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-16
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/relational-history-perturbation-v4
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: concept/relational-meaning
---

# Result: stamp-comprehension pre-probe (Option B) — both models read the stamp as recency on demand

> **Status: proposed (2026-06-16).** The **Option B gate** from the ratified decision
> [`decisions/resolved/relational-v5-text-position-neutralization`](../../decisions/resolved/relational-v5-text-position-neutralization.md)
> (adopt-default: B then A, staged; C the binding fallback). v4 found both panel models follow
> physical text-position, and its binding scope limit is that *"position-following here is
> indistinguishable from stamp-blindness"* — the result could not tell "the model read the round
> stamps and chose position over them" from "the model never parsed the round numbers as recency
> at all." **This pre-probe resolves exactly that ambiguity, and the answer is clean: both
> models read the stamp as a recency value when directly asked.** It is a **gate**, not a
> relational result; it advances the staged design (both models earn an Option-A arm) and does
> **not** move [`conjecture/commutative-convention`](../conjectures/commutative-convention.md)
> off `proposed`. `anchor: internal-contrast-only` (within-model behavioural check over
> byte-identical content; no human-comparison claim — ratified 2026-06-16).

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The Option-A arm this gate earned ran
> the same day: [`result/relational-spontaneous-recency-a`](relational-spontaneous-recency-a.md)
> (session 20) found both models recover a reassigned term by its most-recent binding and fired the
> conjecture's own falsification clause —
> [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) was retired
> (FALSIFIED, 2026-06-16) and the positive promoted to
> [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## The question (precise)

Do `claude-sonnet-4.6` and `gemini-3.5-flash` read the per-line round **stamp** as an ordered
recency value **at all**, when physical line-position is neutralized so that **only** the stamp
value disambiguates the answer? This is the precondition the ratified routing requires before
any geometry-decoupled chronology arm (Option A) is worth building: without it, an Option-A
chronology null would be uninterpretable (stamp-blind vs comprehending-but-not-using).

## Instrument (frozen; see PREREG)

Run dir: [`experiments/runs/2026-06-16-relational-stamp-comprehension-b/`](../../../experiments/runs/2026-06-16-relational-stamp-comprehension-b/).
Same instrument family as v4 (stamped per-line rounds; forced single-label elicitation;
never-parse-`finish_reason: length`; cost ledger + hard stop) — but **no harvested near-twin
descriptions are needed**: each round coins a frozen **nonce** convention, so there is no
stimulus-certification burden.

- Each record: **K=4** stamped lines, `- Round {r}: we agreed to call it "{NONCE}".`, with round
  values drawn from frozen **non-contiguous** quadruples (e.g. `{2,4,7,9}`) so the answer needs
  the stamp *value*, not a "round 1 = first" default.
- Two query directions, within-subject: **MR** ("agreed MOST RECENTLY / latest round" → max-round
  nonce) and **LR** ("agreed EARLIEST / first round" → min-round nonce). Both force use of the
  stamp as an *ordered scale*.
- **Balanced-block design (the load-bearing control).** 12 present-sets (4-nonce subsets, each
  nonce in exactly 6 sets) × a 4×4 Latin square, so within each set the correct nonce cycles
  through all 4 members once **and** the correct line's physical slot cycles through all 4
  positions once. **Proven at build:** every constant-physical-slot strategy **and** every one of
  the 8! fixed nonce-preference orderings scores **exactly 1/K = 0.25** — so no position or
  lexical shortcut can clear the floor; only reading the stamp value can. 48 records/model
  (24/query) × 2 models = **96 finding-bearing calls**.
- Frozen verdict (pre-registered): **PASS** iff `accuracy ≥ 0.80` and the Wilson-95 lower bound
  `> 0.25`; **FAIL** (stamp-blind on this instrument) otherwise.
- INTRO is **neutral** — it states that a higher round number means more recently and that lines
  are not in round order, but does not instruct the model to weight recency or position.

**Discipline.** Two independent pre-run critic passes: the first returned **NO-GO** (a
then-unratified decision — since resolved — and a residual nonce-identity cue worth ~0.46 under
an unconstrained-nonce build); the balanced-block design drove every lexical shortcut to exactly
1/K and the decision was ratified, after which a **fresh** independent critic returned **GO**. An
independent **post-run verifier reproduced every number from the raw data** (own route, not
`analyze.py`): all 48 correct-answers re-derived from the rendered lines (0 mismatches), parse
audit 0/0/0/0, cost re-summed — **REPRODUCED**, no discipline violation.

## The headline (verified — numbers not altered)

Both models comprehend the stamp value at **ceiling**, with position-following at exactly chance:

| model | accuracy | Wilson 95% CI | MR acc | LR acc | pick==last-line | pick==first-line | NA | verdict |
|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **1.000** | [0.926, 1.000] | 24/24 | 24/24 | 0.250 | 0.250 | 0 | **PASS** |
| gemini-3.5-flash | **1.000** | [0.926, 1.000] | 24/24 | 24/24 | 0.250 | 0.250 | 0 | **PASS** |

- **Both models score 1.000**, on **both** query directions (latest *and* earliest), with a clean
  parse record (0 retried, 0 non-strict, 0 length-truncated, 0 NA across all 96 calls).
- The **position-follower diagnostic is at exactly 0.25** for both models in both directions —
  i.e. when the correct line is *not* the physically-last (or -first) one, the models do **not**
  default to position; they follow the stamp. So the ceiling is genuine stamp-reading, not a
  position artifact the design failed to neutralize.

**Verdict: both models PASS the comprehension gate → both earn an Option-A position-rotated,
stamp-gated chronology arm.** `both_fail_close_at_C = false`; Option C is not triggered.

## What this licenses — and what it does NOT (binding scope)

A **PASS** here licenses **only** the narrow, within-model claim that *the model can read a round
stamp as a recency value when directly asked to.* In particular:

- **It does NOT license "the model spontaneously weights recency."** The B task *directs attention
  to recency* ("which did you agree on most recently?"); v4's task asked the model to recover a
  convention without directing attention to the stamp. So the defensible joint reading of B + v4
  is exactly the one the ratification fixed in advance: **the models comprehend the stamp value on
  demand but did not spontaneously weight it in v4's convention-recovery task.** This is the
  ratified narrow wording, carried verbatim; it must **not** be inflated to "comprehends recency"
  in general, nor to "the models chose to ignore recency."
- **It revises v4's reading without overturning it.** v4 said position-following was
  *indistinguishable from stamp-blindness*. B removes the stamp-blindness horn: both models are
  **not** stamp-blind. So v4's position-following is now best read as **comprehending-but-not-
  spontaneously-using** — a sharper, more interesting picture than blindness, and precisely the
  distinction v4 explicitly left open. v4's headline (both models follow physical text-position in
  its convention-recovery task) stands unchanged; only the *explanation* of it is narrowed.
- **It makes no human-comparison claim** (`anchor: internal-contrast-only`). No in-repo resource
  grounds stamp-/order-comprehension, and none is owed because no human contrast is asserted.
- **It does not touch [`conjecture/commutative-convention`](../conjectures/commutative-convention.md)**,
  which stays `proposed`. B is a precondition for the test that *could* move it (Option A), not
  that test.

## Why this matters for the staged design

The decision's whole rationale for staging B before A was that, without B, an Option-A chronology
null is uninterpretable. B's clean both-PASS outcome means an Option-A null would now carry real
content: **"comprehends recency on demand but does not spontaneously weight it when fixing/recovering
a convention"** — a genuinely relational distinction (stamp-blindness vs chronology-neglect) that
v4 fused. So the staged path is now warranted to proceed to Option A for both models, under its own
separate freeze and the binding carry-forward that Option A's stamp-requiring task must be certified
**unsolvable by a positional/lexical shortcut** on idealized-reader fixtures by an independent pre-run
critic *before* any A run (else route to C).

## Honesty box

- **A gate, not a relational finding.** This says nothing about whether LLM conventions are
  path-dependent; it removes one of two competing explanations for v4.
- **On-demand ≠ spontaneous.** The single most important caveat: passing a *direct* recency
  question is weaker than spontaneously weighting recency in a convention task. The result is
  scoped to the former, exactly.
- **n = 48/model, ceiling read.** Both models are at 1.000 with a Wilson lower bound of 0.926,
  far above the 0.80 floor — a clean binary-gate pass, not a marginal one. The NA rate is 0, so
  the ceiling is not an artifact of selective non-answering (a known failure mode for
  forced-format gates; checked and absent here).
- **Panel scope.** claude + gemini only — the A-eligible relational panel carried from v4 (gpt was
  dropped from the finding-bearing relational panel for a stimulus-generation reason, not a
  comprehension one; this pre-probe did not re-open that).
- **Spend.** 96 finding-bearing calls + 2 liveness = **$0.052863 billed** (`usage.cost`-summed,
  0 missing), well inside the $0.50 per-run hard stop and the $5.00/day cap.
