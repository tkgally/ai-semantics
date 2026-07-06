---
id: antonymy-internal-contrast-scoring
title: "A1b antonymy internal-contrast — what the distributional control IS (no co-occurrence data in-repo), how to score relatum recovery with no human gold, and the internal-contrast-only anchor"
status: open
opened: 2026-07-06
opened-by: session-184
contingent-artifacts:
  - design/lexical-relation-shadow-saturation-v1
---

# Decision: the three value-laden gates of the A1b antonymy internal-contrast probe

## Why this is owed

Program item **A1b** operationalizes
[`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md)
in its **internal-contrast** form (no human comparison; the human-compared form stays blocked on
Cao's unlicensed `ProbeResponses`). The conjecture itself opened **no** decision — it recorded a bet,
not a methodological choice. Turning it into a runnable probe forces three choices that *are*
value-laden, so A1b is a fresh design + decision-trail unit (design landed s184:
[`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md)).
The s182/s183 scouts established the crux that makes this non-trivial: **there is no co-occurrence
data in-repo** — SubTLEX-US is a pure unigram norm and its raw corpus is not in-repo — so the control
the conjecture names cannot simply be computed; it must be *chosen and built*.

Nothing here changes any finding; it fixes the **yardstick** for a probe that has not run. Ratifying
is eligible from **session 185** (never the opening session), per [`PROJECT.md`](../../../PROJECT.md)
§12.3: independent adversarial review + one non-Anthropic panel vote; Tom's standing override
outranks.

## Gate Q1 — what the distributional control IS

The conjecture specifies a *"co-occurrence / contrastive-frame distributional control … with special
weight on symmetric contrastive frames"* — Cao 2025b's G² (log-likelihood) over contrastive
co-occurrence. But no in-repo artifact can compute it (SubTLEX-US carries no bigram/co-occurrence
data; the 51M-word source corpus is not in-repo). Options:

- **A — contrastive-frame co-occurrence (G²) from a fetched, license-verified corpus.** Faithful to
  the conjecture and to Cao 2025b. Requires a corpus fetch **and a license scout** (candidates: an
  open OpenSubtitles/Wikipedia dump, a UD-linked corpus — UD is in-scope per program A6). Blocks the
  *run* on that scout; never adopt an unverified-license corpus (s168 discipline).
- **B — static-embedding cosine as the control.** In-repo-buildable, no fetch, but measures *general
  distributional similarity*, not *contrastive-frame co-occurrence* — a **weaker, different shadow**.
  Antonyms sit close in embedding space, so B already "predicts" antonyms — but via similarity, not
  the contrastive frame the conjecture is about; a small antonymy residual under B risks confirming
  the conjecture for the wrong reason.
- **C (provisional default) — A primary + B as a sensitivity check**, side-by-side, **iff** a corpus
  clears the license scout; if none does, A1b's *run* waits on the scout and the design ships
  design-only (an honest block, not a downgrade to the weaker control). The frame-ablation arm (a
  within-model manipulation needing no external corpus) runs under either and is the complement.

## Gate Q2 — scoring "recovery" with no human gold

- **A (provisional default) — WordNet-definitional target + model-vs-control hit-rate residual.**
  Both the model and the Q1 control produce *k* candidate relata per cue+relation; each is scored by
  **Soundness** 𝒮 = fraction that are WordNet-valid relata (Cao's metric). Residual(r, m) =
  𝒮(model) − 𝒮(control); the conjecture predicts it **smallest for antonymy** on ≥2/3 models.
  WordNet is the shared *definitional target*, not a human competence gradient — so no human
  comparison enters, and Q3 (`internal-contrast-only`) follows cleanly.
- **B — per-relation rank-correlation** of the model's and control's candidate rankings ("least
  separable" = highest correlation). More continuous; harder to read as a "residual," more sensitive
  to the control's calibration.
- **C — an alternative** (e.g. a Completeness 𝒞 pairing), surfaced for completeness.

The chosen residual, *k*, stratification, and outlier caps are **frozen before any probe** (anti-cheat);
the **flat-residual null** and the **inverted** outcome are pre-named first-class results.

## Gate Q3 — the anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — the result makes no human-comparison
  claim (its force is a model-vs-control within-instrument contrast), so no `resource` anchor is
  required (CLAUDE.md terminal state). This follows from Q2-A. Per CLAUDE.md this declaration itself
  needs cross-session adversarial ratification — which this decision supplies. Until ratified, the
  design carries `anchor: pending` naming this decision in `contingent-on:`.

## Provisional defaults, together

**Q1-C** (faithful control primary + embedding sensitivity, gated on a license scout) · **Q2-A**
(definitional-target hit-rate residual) · **Q3 internal-contrast-only**. These cohere: Q2-A makes the
probe a clean model-vs-baseline contrast, which is exactly what Q3's internal-contrast-only certifies,
and Q1's job is to make the "baseline" the *contrastive-frame* shadow the conjecture is actually about.

## What ratification unblocks

Fix Q1–Q3 → run the license scout (if Q1-A/C) → freeze `prep.py` + thresholds + PREREG → pre-run
critic + non-Anthropic vote → run on the panel (powered N ~120–150 cues, ≈ $0.8–1.6) → post-run
verifier. Design: [`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md).
