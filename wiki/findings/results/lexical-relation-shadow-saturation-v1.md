---
type: result
id: lexical-relation-shadow-saturation-v1
title: "Antonymy shadow-saturation FALSIFIED — antonymy is the relation whose panel recovery is LEAST explained by a contrastive-frame co-occurrence control, not most; and recovery does not track corpus cue-strength (internal-contrast)"
meaning-senses:
  - distributional
  - inferential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: operationalizes
    target: design/lexical-relation-shadow-saturation-v1
  - rel: contradicts
    target: conjecture/lexical-relation-shadow-saturation
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
---

# Result — lexical-relation shadow-saturation v1 (antonymy internal-contrast)

> **Status: proposed (reading-bearing result; s186, 2026-07-06). VERDICT: the shadow-saturation
> conjecture is FALSIFIED in its internal-contrast form.** On a same-task relatum-production probe
> over six WordNet noun relations, run on the panel against a contrastive-frame co-occurrence (G²)
> distributional control, **antonymy is NOT the relation whose recovery is least separable from the
> control** — it carries one of the *largest* residuals, not the smallest. And **raw recovery does
> not track corpus cue-strength** (Spearman ≈ −0.09; antonymy tops cue-strength but hypernymy, not
> antonymy, is best-recovered). Both of the conjecture's confirmation clauses fail.
> `anchor: internal-contrast-only` (ratified s185): the force is a model-vs-distributional-baseline
> within-instrument contrast — **no human comparison**. This is a first-class negative.

Program **A1b**. Design [`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md);
gates ratified s185 ([`decisions/resolved/antonymy-internal-contrast-scoring`](../../decisions/resolved/antonymy-internal-contrast-scoring.md));
conjecture [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md).
Frozen `PREREG.md` + two pre-run review rounds (`REVIEW.md`) + post-run verifier under
`experiments/runs/2026-07-06-antonymy-shadow-saturation/`. Panel = the three [`config/models.md`](../../../config/models.md)
slots (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash), temperature 0, zero-shot; 2,730 calls,
6/2730 empty, 0 errors; **$0.4661 billed**. An independent **post-run verifier reproduced every
load-bearing figure from raw** (0 discrepancies beyond Spearman rank-tie third-decimals; all five
claims A–E confirmed; hand spot-checks of gold alignment sensible, no off-by-one).

## What was measured

Six WordNet **noun** relations (antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy),
**N = 130 cues each**, frequency-matched on SubTLEX-US Lg10WF (medians 3.005–3.015, band [2.0, 4.5]).
Nouns only because WordNet's taxonomic relations exist only for nouns — an adjective-antonymy
replication (J&K's home POS) is named future work. The distributional **control** ranks a
6,810-word content-noun pool by contrastive-frame G² (Dunning log-likelihood over co-occurrence in
symmetric/contrastive frames — "X versus Y", "neither X nor Y", "from X to Y", conjunction/adjacency)
from a fetched **Simple English Wikipedia** dump (CC BY-SA 4.0; 21,307,378 sentence-units), takes its
top-3, and is scored against the same WordNet gold the model is. Two scorers: **Soundness** 𝒮
(precision over produced, Cao's metric) and gold-size-insensitive **HIT@3** (≥1 produced word in
gold) — the latter added at freeze to neutralise the antonymy-gold-size confound the pre-run reviews
flagged. Residual = score(model, neutral prompt) − score(control), bootstrapped over cues.

## The numbers (per model A/B/C)

| Relation | raw 𝒮(model) | control 𝒮 (frame) | HIT@3 residual | gold size |
|---|---|---|---|---|
| **antonymy** | 0.32 / 0.30 / 0.33 | **0.077** | **+0.67 / +0.61 / +0.66** | 1.1 |
| synonymy | 0.24 / 0.22 / 0.26 | 0.010 | +0.49 / +0.43 / +0.51 | 3.0 |
| **hypernymy** | **0.39 / 0.37 / 0.36** | 0.023 | +0.68 / +0.69 / +0.63 | 14.1 |
| hyponymy | 0.24 / 0.22 / 0.26 | 0.010 | +0.40 / +0.37 / +0.45 | 24.0 |
| holonymy | 0.14 / 0.12 / 0.20 | 0.026 | +0.28 / +0.23 / +0.38 | 2.8 |
| **meronymy** | 0.14 / 0.12 / 0.18 | 0.028 | **+0.25 / +0.19 / +0.32** | 4.3 |

- **Clause 1 (antonymy least-separable) — FALSIFIED.** The **smallest** HIT@3 residual is **meronymy**
  on all three models (holonymy second-smallest); antonymy is near the *top*. The conjecture's
  registered falsifier — "a weakly-cued relation is recovered best / antonymy keeps a large residual"
  — is met: antonym recovery clears large daylight above the contrastive-frame control (+0.61–0.67
  HIT). The relations least separable from the control are the **part-whole** relations
  (meronymy/holonymy), and that is because they are simply the **hardest** (lowest raw recovery,
  0.12–0.20), not because a co-occurrence shadow explains them.
- **Clause 2 (raw recovery tracks cue-strength, antonymy top of both) — FALSIFIED.** The
  across-relation Spearman between raw recovery and corpus cue-strength is **−0.086** on every model.
  Antonymy **is** top of corpus cue-strength (𝒮 control 0.077 vs 0.010–0.028 — the essay's premise
  holds, measured from our own corpus), but it is **not** top of recovery: **hypernymy** is best
  recovered (0.36–0.39), while meronymy — the *second*-most-cued relation — is *worst* recovered.
  Distributional cue-strength does not predict which relations the panel recovers.

## Load-bearing caveat — the residual arm is descriptive-only (pre-registered calibration gate)

The pre-registered calibration gate **fired**: mean 𝒮(control, frame) = 0.029 (< 0.05) and the
median Spearman between the residual ranking and the raw-recovery ranking = 0.943 (≥ 0.90). So the
top-3 contrastive-frame control recovers almost none of *any* relation's WordNet relata, and the
residual ranking is essentially the raw-recovery ranking with a near-constant tiny subtraction. The
"least-separable" residual is therefore reported **descriptively** — the control is too weak to be a
strong separability instrument — and the weight of the finding shifts, exactly as PREREG named, to
**clause 2** (recovery does not track cue-strength) and the **frame-ablation** arm. This does not
rescue the conjecture: its own premise was that co-occurrence *saturates* antonymy recovery, and the
data show the opposite — even the most-cued relation's recovery is overwhelmingly **un**explained by
this co-occurrence control.

## Frame-ablation (antonymy, model-internal — needs no corpus)

Antonym recovery with the contrastive frame **present** vs **suppressed** (neutral): HIT@3 stays
high under suppression — **neutral 0.84–0.90 → frame 0.79–0.85** (Δ ≈ −0.02 to −0.11, i.e. the frame
does *not* raise whether the antonym is found; it slightly lowers it by inviting extra fillers).
Soundness *rises* with the frame (0.30–0.33 → 0.72–0.80) only because the frame elicits fewer, more
focused answers (higher precision), not because it surfaces antonyms the neutral prompt missed.
**Antonym recovery survives frame suppression** — the panel finds the antonym without the
contrastive scaffold — so antonymy competence here is **not merely frame-cued**. This is the
partial witness the companion essay's revision **trigger (a)** was left live for, firing in the
*surviving* direction.

## What this licenses, and what it does not (scope caps — read before citing)

- **Internal-contrast only.** No human comparison; the control is a corpus statistic and WordNet is
  a shared definitional target that cancels in the residual (Q3, ratified s185).
- **Read at the strength the control licenses** (essay [`shortcut-vs-competence-mis-cut`](../essays/shortcut-vs-competence-mis-cut.md),
  ratified s151). A residual over a co-occurrence control grades **local vs transferable
  distributional** generalization, **not** distribution vs non-distribution. So "antonym recovery
  survives / exceeds the contrastive-frame control" falsifies the **local-shadow-saturation** reading
  — antonymy recovery is *not* nothing but local frame-completion — but does **not** establish
  competence beyond distribution. The referential/grounded question is untouched.
- **n = 3, orderings not coefficients.** All three models agree on every ordering reported here
  (meronymy smallest residual 3/3; hypernymy best-recovered 3/3; Spearman −0.086 3/3).
- **Proxy-corpus fence** (condition 2): the control corpus is a proxy for the panel's unknown
  pretraining distribution.
- **Nouns only; gold fan-out disclosed.** Antonymy carries the highest %gold-in-V (0.881) and the
  highest control 𝒮 — asymmetries that would *shrink* its residual toward "smallest"; the finding is
  robust *against* that tilt (antonymy is nonetheless among the *largest* residuals), and the
  gold-size-insensitive HIT@3 + size-matched views agree.

## What it feeds

- **Contradicts** [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md):
  both confirmation clauses fail; the registered [`predictions.md`](../../predictions.md) bet is a
  **loss** (an honest negative — the calibration record gains a falsified lexical bet).
- **Revises** [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md)
  **trigger (a)** — fired in the surviving direction (panel antonym recovery exceeds the
  contrastive-frame control), scoped to local-vs-transferable per the s151 note.
- **Moves the "saturated corner"** of [`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md):
  the antonymy row was a marked *reading/bet* ("saturated"); this probe measures it and the reading
  does **not** hold — antonymy is not the shadow-saturated relation on the panel. Recorded as a
  measured internal-contrast reading, with the descriptive-only caveat.
- **A new observation, logged not over-read:** the panel's **cue-strength–recovery decoupling** —
  the relation the corpus cues most (antonymy) is not the one the panel recovers best (hypernymy),
  and the second-most-cued (meronymy) is recovered worst. Distributional cue-strength is a poor
  predictor of relation-wise recovery on these models — a seed for a future essay/conjecture.
