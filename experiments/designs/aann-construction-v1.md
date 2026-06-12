---
type: design
id: aann-construction-v1
title: AANN construction probe v1 — licit/illicit contrast with Mahowald 2023 as human anchor
meaning-senses:
  - constructional
  - distributional
  - functional-vs-formal
  - human-comparison
status: retired (unrun — indicator unexecutable under pure autonomy, 2026-06-12)
contingent-on:
  - aann-behavioral-operationalization
created: 2026-05-28
updated: 2026-06-12
links:
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: concept/constructional-meaning
---

# Experiment design v1 — AANN construction

> **RETIRED UNRUN (2026-06-12).** This design's ratified indicator (per-token continuation-
> likelihood contrast, with a prompted-acceptability *logprob* fallback) is unexecutable under
> the project's pure-autonomy constitution: OpenRouter exposes no echo/prompt-logprobs on any
> model, no local GPU exists, and no key will be provisioned — see the cross-session resolution
> `wiki/decisions/resolved/aann-panel-logprob-blocker.md` (2026-06-12). The page is kept intact
> as the record of the v1 measurement chain; a behavioral v2 design under
> `wiki/decisions/open/aann-behavioral-operationalization.md` will supersede it. The conjecture
> itself is NOT retired and the probe was never run.

**Status (historical)**: both governing decisions — `decisions/resolved/aann-operationalization.md` and `decisions/resolved/aann-stimulus-source.md` — were **ratified 2026-05-29** (Mahowald 2023 as the AANN anchor; continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1 + held-out adjectives locked before the run). That fixes the design's yardstick. The design itself is **unrun**: nothing in this page may be promoted to a settled finding until the probe actually runs.

## 1. Construct

The **AANN construction** as a form-meaning pairing in Goldberg's sense: form = *a* + Adjective + Numeral + Plural-Noun (*a beautiful three days*); meaning = the modified plural quantity construed as a unified, often evaluatively-loaded stretch. The construct of interest is whether a panel model treats this pairing as productive — i.e., generalizes the form preference to held-out lexical material *in a way that tracks the construction-specific constraints* documented in the CxG / formal-semantics literature on AANN (Solt 2007; Dalrymple & King 2019; Bylinina & Nouwen 2018; Goldberg & Michaelis 2017).

## 2. Indicator

(Per `decisions/resolved/aann-operationalization.md`, ratified 2026-05-29.)

**Primary indicator (Option A)**: continuation-likelihood contrast. For each item tuple (template, adjective, numeral, noun), compute the panel model's average per-token log-probability for the **licit AANN** instantiation and for each of the four **minimally-illicit** Mahowald-2023 variants:

- AANN (licit): *The family spent a beautiful three days in London.*
- Switched: *The family spent a three beautiful days in London.*
- No modifier: *The family spent a three days in London.*
- Singular noun: *The family spent a beautiful three day in London.*
- No article: *The family spent beautiful three days in London.*

Two derived numbers per panel model:

- **Rank-above-degenerate rate** — fraction of items on which the licit AANN string is assigned higher per-token log-probability than *all four* degenerate variants.
- **Signed gradient correlation** — Spearman ρ between the per-item signed contrast (AANN minus mean degenerate) and the Mahowald MTurk-mean rating, on the subset of items for which Mahowald released ratings.

**Fallback (Option B)** — if a panel model does not expose adequate token logprobs through its OpenRouter chat endpoint: Mahowald's prompted-rating replication (in-context "good"/"bad" examples, target sentence, take p("good") from response logprobs). Score and threshold computed parallel-wise.

The choice between A and B is **per model**, locked before the probe runs, and recorded in the run record. It is *not* re-decided after seeing first-batch outputs (cf. charter §8 retuning-after-seeing-results failure mode).

## 3. Method

### 3.1 Item set

Drawn from `resource/mahowald-2023-aann-stimuli` (the Mahowald 2023 templatic generator and his MTurk-rated subset). Two halves:

- **Anchored half**: items that overlap with Mahowald's released `aann-sents/` and have MTurk ratings in `mturk_data/`. Used to compute the signed gradient correlation against the human anchor.
- **Held-out half**: items built from at least 30 adjectives per category drawn from **outside** Mahowald's slot-filler superset. The held-out adjective list is committed alongside the probe code, lexically frozen *before* probe execution, and documented in the run record. Used to test productivity beyond seen items.

Total target item count: order ~600 items × 5 variants per item × 3 panel models = ~9000 prompt evaluations per indicator. (See §6 for cost.)

### 3.2 Panel

Per `config/models.md`:

- `panel.A` — `anthropic/claude-sonnet-4.6`
- `panel.B` — `openai/gpt-5.4-mini`
- `panel.C` — `google/gemini-3.5-flash` (with reasoning-token mitigation per panel calibration caveats)

### 3.3 Probe protocol

For each panel model:

1. Confirm logprob availability via a 5-item dry run before any full-scale call. If unavailable, flip to Option B for that model and record the flip.
2. For each of the ~600 items:
   - Submit the licit AANN string and each of the four degenerate variants as separate completions.
   - Record: full prompt, completion tokens (or full string for Option B), per-token logprobs, latency, usage tokens.
3. Persist raw JSON to `experiments/data/aann/runs/<run-date>/<panel-slot>/`.

Temperature = 0 throughout. Reasoning-token mitigation: where the model supports it, set `reasoning: {"enabled": false}` (Gemini); otherwise set `max_tokens` ≥ 1024 and budget accordingly. Document the per-model setting in the run record.

### 3.4 Analysis

For each panel model:

- Compute the **rank-above-degenerate rate** on (a) anchored items, (b) held-out items.
- Compute the **signed gradient correlation** against MTurk-mean ratings on anchored items only.
- Apply the T1 threshold from `decisions/resolved/aann-operationalization.md`.
- Report all four numbers for all three models in a single table, including failure modes (logprobs unavailable, reasoning truncation, etc.). Per panel-as-subjects (charter §6), cross-model divergence is itself a result.

No item-level cherry-picking. No post-hoc threshold adjustment.

## 4. Human anchor

**Named anchor**: Mahowald 2023 MTurk acceptability ratings (`resource/mahowald-2023-aann-stimuli`). Specifically:

- Experiment 1 ratings (126 raters × 3 critical sentences = 378 ratings) on the four-way degenerate-variant contrast — used to ground the rank-above-degenerate rate.
- Experiment 2 / 3 ratings on adjective-type × noun-type interactions — used to ground the signed gradient correlation.

Caveat: MTurk is not a balanced linguistic-expert panel. The anchor grounds *graded acceptability*, not theoretical-CxG-licit-vs-illicit per se; that distinction is recorded in the resource page (`mahowald-2023-aann-stimuli.md`, §Known limits).

The anchor is `external-only` in this session. A future run mirroring the Mahowald repo into `experiments/data/aann/` is a prerequisite to *running* the probe (`NEXT.md` will list this).

## 5. Predictions (re-stated from `conjecture/aann-construction`)

1. On the anchored half, each panel model achieves rank-above-degenerate rate ≫ 0.5 (chance under no preference between five variants is 0.2; the trivial-form prior — preferring any singular-article string without other constraints — should still give well under 0.8). **Quantitative prediction**: ≥ 0.8 on anchored, ≥ 0.7 on held-out, for ≥ 2 of 3 panel models.
2. Signed gradient correlation against Mahowald MTurk means: Spearman ρ ≥ 0.30 (T1) for ≥ 2 of 3 panel models, on the anchored subset.
3. Per the calibration-probe hint: `gpt-5.4-mini` will underperform the other two on the gradient correlation specifically, even if it passes the coarse rank-above-degenerate threshold.

## 6. Pre-flight cost check (`config/budget.md` §Pre-flight)

Back-of-envelope estimate, assuming ~600 items × 5 variants = 3,000 completions per model:

| Model | Tokens in / call | Tokens out / call | Pricing (in / out per MT) | Est. cost |
|-------|-----------------:|------------------:|---------------------------|----------:|
| `panel.A` claude-sonnet-4.6 | ~50 | ~30 | $3 / $15 | ~$1.80 |
| `panel.B` gpt-5.4-mini | ~50 | ~30 | $0.20 / $0.60 | ~$0.10 |
| `panel.C` gemini-3.5-flash | ~50 | ~30 (caveat: reasoning tokens) | $0.15 / $0.60 | ~$0.10 + reasoning-token overage |

Total: under $5, comfortably within the budget rule. The reasoning-token caveat could roughly double Gemini's number; still well under the $5-single-run flag. **No pre-flight budget escalation required.**

## 7. Falsification criteria

The conjecture (re-stated): LLMs treat AANN as a productive form-meaning unit that generalizes to held-out lexical items in a way that tracks construction-specific constraints.

- **Confirm**: ≥ 2 of 3 panel models pass T1 on both anchored and held-out items.
- **Weak / partial**: T1 met on anchored items only, not on held-out (memorization-like).
- **Partial differently**: rank-above-degenerate met but gradient correlation < 0.30 (form preference without graded constructional sensitivity — a `formal-vs-functional` finding, not a `constructional` finding).
- **Falsify (current form)**: T1 not met by any panel model, *or* met by models in a way that tracks unigram adjective frequency rather than the construction (sanity-check regression on adjective unigram log-frequency from a public n-gram resource — to be specified in the *run* design, not relitigated here).

A null on any of the above is a **claim-worthy result**, not a non-finding (charter §2.6). Write it.

## 8. What this design does **not** do

- Does not address the `inferential` half of the conjecture (does the model draw the unified/evaluative paraphrase). That requires a different indicator (Option C in the operationalization gate) and is queued as a v2 design after v1 lands.
- Does not cross-link to the *way*-construction or function-word-substitutability conjectures. Those are independent loop turns.
- Does not pre-suppose Mahowald's *theoretical analysis* of AANN — only his stimulus set and ratings. The project remains constructive, not adjudicative (charter §1).

## 9. Handoff hooks

When the *next-next* run executes the probe:

1. Mirror `https://github.com/mahowak/aann-public` into `experiments/data/aann/aann-public/` (license-check first).
2. Promote `resource/mahowald-2023-aann-stimuli` from `external-only` to `catalogued` after inspecting file contents.
3. `decisions/resolved/aann-stimulus-source.md` and `decisions/resolved/aann-operationalization.md` are both resolved (ratified 2026-05-29); the run still does not promote anything to a settled finding until the probe has executed and produced results.
4. Lock the held-out adjective list and commit it under `experiments/data/aann/held-out-adjectives.txt` *before* the probe runs.
5. Write the probe code under `experiments/runs/<date>-aann-probe-v1/` mirroring the calibration probe's structure.
