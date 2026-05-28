---
id: aann-operationalization
title: What counts as evidence that a panel model "tracks" the AANN construction?
status: open
opened: 2026-05-28
opened-by: lead-agent
contingent-artifacts:
  - conjecture/aann-construction
  - design/aann-construction-v1
---

# Decision: AANN operationalization

## Question

The AANN conjecture says LLMs treat the AANN construction (*a beautiful three days*) as a productive form-meaning unit. To move that from a slogan to a testable claim, we need to commit, *before* running the probe, to (a) the indicator function we will compute on model behavior, (b) the contrast set the indicator is computed over, (c) the threshold above which we say the model "tracks the construction." This is the canonical operationalization gate from charter §8 — the place an autonomous loop will quietly retune until a null becomes positive if we do not pin it down in advance.

## Options for the indicator

### A. Continuation-likelihood contrast (provisional default)

For each (template, adjective, numeral, noun) tuple, compute the model's average per-token log-probability assigned to the **licit AANN** instantiation versus each of Mahowald's four **minimally-illicit** variants (switched order, no modifier, singular noun, no article). Indicator = the signed contrast averaged over items, plus the per-item signed-rank correlation against Mahowald's MTurk human ratings on the matched subset.

- **Pros**: clean, graded, behaviorally direct, comparable across panel models if all three expose log-probs via OpenRouter; matches the small-model lane (charter §5) for follow-up.
- **Cons**: not all panel models expose token logprobs reliably via OpenRouter; reasoning-token leakage on Gemini / DeepSeek (per panel-calibration caveats in `config/models.md`) may interact with this.

### B. Prompted acceptability rating (Mahowald-replication)

Reuse Mahowald's prompt template — a few in-context "good"/"bad" judgments on diverse sentences, then ask the model to rate the target — and take the probability of "good" as the rating.

- **Pros**: apples-to-apples comparison with Mahowald's published GPT-3 numbers and with his MTurk human ratings; doesn't require model-side logprob access for arbitrary tokens (only for the two response tokens, which all current chat APIs can usually return via `logprobs`).
- **Cons**: depends on whether the panel models' chat APIs expose response-token logprobs cleanly; conflates "rates as good" with "is sensitive to" — a reasoning-tuned model may produce verbose meta-commentary instead of a clean token.

### C. Forced-choice paraphrase / inferential probe

Present the model with an AANN sentence and ask it (e.g.) which of two paraphrases preserves meaning — one capturing the unified/evaluative reading, one capturing the merely-distributive compositional reading. Score by chosen-option probability.

- **Pros**: targets the *meaning* directly rather than only form preference; closer to a `constructional` × `inferential` co-tagged claim.
- **Cons**: introduces a new generation/answer-format dependency; not what the human anchor measures (Mahowald measures acceptability, not paraphrase choice) — so it answers a *different* question that the human resource cannot directly anchor.

## Options for the threshold

For Option A (the provisional default):

- **T1 (default)**: A panel model "tracks the construction" if, on held-out adjectives (see below), it (i) ranks the AANN variant above all four degenerate variants on ≥ 80% of items, **and** (ii) its signed per-item contrast correlates with Mahowald's MTurk-mean rating at Spearman ρ ≥ 0.30 on the matched subset. The conjecture is supported (in its current form) when ≥ 2 of 3 panel models meet T1.
- **T2 (stricter)**: same as T1 but ρ ≥ 0.50.
- **T0 (looser)**: drop the correlation requirement; rank-above-degenerate on ≥ 70% of items is enough. Reserve T0 for a sanity check; do not treat it as confirming the conjecture.

## Held-out vs. seen adjectives

The conjecture predicts generalization, not memorization. Define held-out items in advance:

- **Train-side surface**: any (adjective, numeral, noun) combination whose exact string appears in Mahowald's released `aann-sents/` is treated as "seen by Mahowald's probe corpus" — not necessarily by the panel models' training data, but a known-public anchor.
- **Held-out**: at least 30 items per condition built from adjectives **not** in Mahowald's slot-filler superset, drawn from the same six adjective categories (this requires a small extension to the templates — list to be locked before the probe runs and committed alongside the probe code).

## Provisional default (in force until Tom ratifies)

- **Indicator**: Option A (continuation-likelihood contrast), with Option B as fallback on any panel model whose chat API does not expose adequate logprobs.
- **Threshold**: T1.
- **Held-out items**: ≥ 30 per adjective category, drawn from outside Mahowald's superset, locked in `experiments/data/aann/held-out-adjectives.txt` *before* the probe is run.

Why this default rather than the looser T0: the bootstrap calibration probe already showed a cross-model AANN divergence (`experiments/runs/2026-05-28-panel-calibration/README.md`). The point of T1 is to make the conjecture's support claim mean something — not to lower the bar until a null becomes positive.

## What downstream is contingent on this

- `wiki/findings/conjectures/aann-construction.md` (now `contingent-on: aann-operationalization`).
- `experiments/designs/aann-construction-v1.md` (entire design is provisional under this default; if Tom ratifies a different indicator the design must be rewritten before the probe runs, not after).
- All future `claim` / `result` pages spawned by the AANN probe.

## Notes for the resolver

Tom: the choice that bites is **A vs. B** (logprob contrast vs. Mahowald-replication prompt). The threshold (T1 vs. T2) bites less — it's tunable post-hoc only in the sense of being *more* conservative, never less. If you'd rather lock T2, say so; raising the bar is always safe.
