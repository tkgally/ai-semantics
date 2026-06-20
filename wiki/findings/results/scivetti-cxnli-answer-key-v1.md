---
type: result
id: scivetti-cxnli-answer-key-v1
title: The 2026 panel reaches human native-speaker NLI accuracy on the full Scivetti CxNLI base task in 2 of 3 models — with the phrasal scalar let-alone the one construction all three fail
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: proposed
contingent-on: []
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: refines
    target: result/cxnli-distinction-divergence-v1
  - rel: supports
    target: conjecture/caused-motion-construction
  - rel: supports
    target: conjecture/way-construction
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: supports
    target: conjecture/conative-construction
---

# Result: Scivetti CxNLI answer-key probe v1 (the full Exp-1 base task)

This is the first time the project scores its panel against the **actual
human-annotated** Scivetti CxNLI items rather than the project's own synthetic
minimal pairs. It runs the long-queued step the resource page
[`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
flagged on 2026-05-29 ("the next step is to actually run a probe… compare panel-model
NLI labels against the per-item gold labels and report against the aggregate ≈0.90
human baseline"), on the **full** 390-item Experiment-1 test set across all 8
constructions — the measurement the earlier
[`result/cxnli-distinction-divergence-v1`](cxnli-distinction-divergence-v1.md) could
not make (its base arm was a 20-item subsample of 5 constructions; this **discharges
its limit 1**). Run record: [`experiments/runs/2026-06-20-scivetti-cxnli-answer-key/`](../../../experiments/runs/2026-06-20-scivetti-cxnli-answer-key/README.md).

**One-line finding.** On the full Scivetti CxNLI base task, **2 of 3 panel models reach
the human native-speaker accuracy** (claude-sonnet-4.6 0.903 and gemini-3.5-flash 0.915
both have 95% CIs containing the ≈0.90 baseline; gpt-5.4-mini sits ~9 pp below at
0.813). The one construction **all three models fail** is the phrasal scalar
**`let-alone`** (0.46–0.67, near 3-way chance), **not** any argument-structure
construction — the four ratified-anchor constructions (caused-motion, conative,
way-manner, comparative-correlative) are all at or near the baseline in claude and
gemini. The result is **answer-key agreement, not a competence proof**: contamination
is possible (see *Limits*), so the **`let-alone` shortfall is the robust signal** and
the matches are the weaker one.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), run **as subjects**
  (charter §6). Temperature 0; gemini reasoning `effort: minimal`. NLI instrument
  (`NLI_SYS` + `parse_nli`) **reused verbatim** from
  [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md); the 0/1/2
  label scheme is the dataset's own.
- **Items.** The **full** released Exp-1 test set (`CxNLI_3_examples_test.tsv`): **390
  items**, balanced **130/130/130** across entailment/neutral/contradiction, 8
  constructions. No item selection — the full set, so the operationalization gate's
  chief cheat-surface (item selection) is structurally absent. Gold labels were **not**
  shown to the model. Read in place from the un-licensed Scivetti repo (commit
  `82699473`), **not mirrored** (recipe-not-corpus: only the sha-manifest +
  per-construction labels are committed, never the premise/hypothesis text).
- **Integrity.** 390/390 rows per model, **0 unparseable**, **0 missing `usage.cost`**.
- **Cost** (billed `usage.cost`): **$0.3305** (claude $0.2026 / gpt $0.0491 / gemini
  $0.0788). Under the $2.50 single-run flag.

## Results

Human reference (fixed, not retuned): Scivetti Exp-1 **native-speaker accuracy ≈ 0.90**
([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md);
"native speaker accuracy on the NLI task is 90%"). Chance on the 3-way task ≈ 0.33.

| model | overall acc | Wilson 95% CI | vs human 0.90 |
|---|---:|---|---|
| claude-sonnet-4.6 | **0.903** | [0.869, 0.928] | **MATCHES** (0.90 inside CI) |
| gpt-5.4-mini | **0.813** | [0.771, 0.848] | **BELOW** (CI upper 0.848 < 0.90) |
| gemini-3.5-flash | **0.915** | [0.883, 0.939] | **MATCHES** (0.90 inside CI) |

### Per-construction accuracy (acc; * = ratified human anchor)

| construction | n | claude | gpt | gemini |
|---|---:|---:|---:|---:|
| comparative-correlative * | 30 | 1.000 | 0.900 | 1.000 |
| caused-motion * | 36 | 0.917 | 0.861 | 0.972 |
| conative * | 78 | 0.962 | 0.821 | 0.936 |
| way-manner * | 33 | 0.818 | 0.849 | 0.939 |
| causative-with | 54 | 0.982 | 0.926 | 0.982 |
| intransitive-motion | 69 | 0.899 | 0.797 | 0.870 |
| resultative | 66 | 0.894 | 0.773 | 0.894 |
| **let-alone** | 24 | **0.542** | **0.458** | **0.667** |

Macro accuracy over the four ratified-anchor constructions: claude **0.924**, gpt
**0.858**, gemini **0.962**. The human-comparison **claim** is scoped to these four
(the constructions the anchor was ratified for, 2026-05-29) plus the dataset-level
overall accuracy; the other four are reported descriptively from the same
human-annotated release.

## Interpretation (modest)

1. **The base answer-key task is largely solved by the two stronger models, and the
   weaker one trails uniformly.** claude and gemini land inside the human baseline's
   interval; gpt-5.4-mini is ~9 pp under, the same model that was the only one below
   baseline on the base arm of [`result/cxnli-distinction-divergence-v1`](cxnli-distinction-divergence-v1.md).
   So the *model ordering* (gpt weakest) reproduces on the full set.
2. **The one consistent failure is a phrasal, not an argument-structure, construction.**
   `let-alone` — a scalar coordinator whose inference requires ordering two clauses on a
   pragmatic scale — is at 0.46–0.67 for all three (claude and gpt below 0.55, near
   3-way chance). It is the worst construction in **every** model, by a wide margin, and
   it was **absent** from the prior distinction study (which used the 5 argument-structure
   constructions). This is the new locus: the argument-structure constructions the
   project has probed most (caused-motion, way, conative) are at or near ceiling on the
   base task, while the scalar phrasal construction is where the panel breaks down.
3. **The add/cancel difference does not show up at the base answer-key level — as the
   monotonicity conjecture itself predicts it should not.** For
   [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
   ADD (caused-motion ∪ way-manner) vs CANCEL (conative) accuracy is: claude 0.870 vs
   0.962 (**−0.092**, cancel *higher*), gpt 0.855 vs 0.821 (+0.035), gemini 0.957 vs
   0.936 (+0.021) — small and **inconsistent in sign**. This is **consistent with** the
   conjecture's own scope statement: the asymmetry it posits is a *de-confounded,
   matched-difficulty* property of the suppression-with-no-cue cue arms, **not** a base
   answer-key gap; at base ceiling both directions are near-ceiling and the conative is
   in fact *highest* for claude. The contrast here is **baseline-difficulty-confounded
   and is not the matched-difficulty test the conjecture requires** — it neither
   confirms nor falsifies, but it removes a naive reading ("cancel is always harder")
   that this datum would have invited.

## What this does and does not license

**Does license:** a project-owned, revisable, **human-anchored** statement that on the
full Scivetti CxNLI base task the 2026 panel reaches native-speaker NLI accuracy in 2/3
models (claude, gemini) and falls ~9 pp short in the third (gpt-5.4-mini), with the
phrasal scalar `let-alone` the single cross-model failure point. Scoped to the four
ratified constructions for the per-construction human comparison; descriptive elsewhere.

**Does NOT license:**
- **A competence-vs-memorization verdict.** Answer-key agreement only; contamination is
  possible (see *Limits*), so a *match* cannot distinguish learned construction-meaning
  from item memorization. The *shortfall* (let-alone; gpt overall) is the robust
  direction — failure survives possible contamination, a match does not.
- **A model-internal or grounding claim.** Behavioral NLI accuracy only.
- **A test of the conjectures' own predictions.** This uses *Scivetti's* items and gold,
  not the project's controlled minimal pairs; it bears on caused-motion / conative /
  way / comparative-correlative as anchored answer-key accuracy, not as a test of their
  specific contrasts (which need the project's own stimuli — already run separately).
- **A tight per-construction magnitude** for the small cells (let-alone n=24,
  comparative-correlative n=30) — read the CIs.

## Limits

- **Single gold label, answer-key not gradient.** The release gives one adjudicated
  gold label per item, not a per-item human distribution
  ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  *Known limits*): accuracy-vs-baseline, never a human gradient.
- **Contamination (load-bearing caveat, pre-registered).** Items derive from public
  corpora and the dataset is on public GitHub, so panel models may have seen them.
  Contamination **inflates** accuracy, so the matches are the *weaker* evidence and the
  `let-alone`/gpt shortfalls the *robust* signal. Stated before the run (PREREG §5).
- **One run, one date, one zero-shot framing.** A different framing (forced-choice, CoT,
  few-shot) could shift absolute accuracies. The cross-model convergence on `let-alone`
  is the robustness signal; single per-construction cells are not replicated.
- **Shared priors (charter §2.5).** Three decoders agreeing is weak on its own; the
  Scivetti human baseline (small, aggregate) is the independent bearing.

## Provenance

- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (CxNLI Exp-1 gold labels + ≈0.90 native-speaker baseline; ratified 2026-05-29 as the
  answer-key anchor for caused-motion / conative / way-manner / comparative-correlative).
  Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
  Operationalization (NLI instrument + answer-key human-baseline comparison) governed by
  the already-ratified [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md);
  no new decision owed (independent pre-run critic GO, fresh agent).
- No license upstream → read in place, **not mirrored**; committed artifacts are the
  recipe (`prep.py`), the sha-manifest (`1c5cffb18c5ef78e`), and the per-item
  labels/gold (no premise/hypothesis text).
- Run record + code + redacted outputs + cost:
  [`experiments/runs/2026-06-20-scivetti-cxnli-answer-key/`](../../../experiments/runs/2026-06-20-scivetti-cxnli-answer-key/README.md).
  Numbers reproducible from the committed `raw/` + `analyze.py` against a local Scivetti
  clone. Independent post-run verifier (fresh agent) **REPRODUCED** every accuracy,
  Wilson CI, baseline verdict, parse-integrity check, and the billed cost.

## Status

`status: proposed`, `contingent-on: []` (the governing operationalization decision and
the Scivetti anchor are both ratified; this result uses only aggregate/answer-key
bearing). What is `proposed` is the project's reading. Promotion past `proposed`-level
awaits Tom's review and ideally a replication or alternate-framing sweep of the
`let-alone` failure (the discriminating signal).

> **Follow-up (2026-06-20, session 58): the `let-alone` failure was largely an
> output-channel artifact.** The alternate-framing sweep this Status line called for has
> run — [`result/scivetti-let-alone-working-surface-v1`](scivetti-let-alone-working-surface-v1.md)
> re-ran the SAME `let-alone` items under a **working surface** (format-only). **2 of 3
> models LIFT to the human ≈0.90 baseline** on the same items (claude 0.542→0.792, gemini
> 0.667→0.917; within-item sign test p = 0.035; ceiling control PRESERVED), so the
> near-chance here was substantially a **forced single-token channel** effect masking the
> construction's *scalar/serial* inference, **not** a clean scalar-phrasal competence
> boundary. gpt-5.4-mini did not recover, but largely **declined** the offered surface
> (bare one-token answers), so its persistence is channel non-uptake, not a demonstrated
> channel-controlled failure. The "`let-alone` failure is the robust signal" framing above
> still holds *relative to the forced channel*, but the cross-model **dissociation** it
> implied is now read as channel-sensitivity, not a content-type difficulty.
