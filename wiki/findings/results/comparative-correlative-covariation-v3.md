---
type: result
id: comparative-correlative-covariation-v3
title: Comparative-correlative v3 — the covariation reading mostly survives operator embedding (negation/modality); claude+gemini track operator scope at/near ceiling, gpt-5.4-mini cracks under forced-choice via an excluded-middle over-inference
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: refines
    target: result/comparative-correlative-covariation-v2
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: supports
    target: claim/comparative-correlative-covariation
---

# Result: comparative-correlative probe v3 (embedded CC / operator scope)

**One-line:** placed under an operator that cancels or suspends its assertion — sentential **negation** ("it is not the case that the more X, the more Y") or **epistemic hedging** ("it remains unproven whether…") — the comparative correlative's covariation reading **mostly survives**: claude-sonnet-4.6 and gemini-3.5-flash track the operator scope at/near ceiling (they withhold the covariation direction), so the v1/v2 robustness is **not** a bare "the-more…the-more → INCREASE" template. The third panel model, gpt-5.4-mini, **cracks under the forced-choice instrument specifically**, via a logical **over**-inference (the excluded-middle fallacy), not template-firing.

Run record: [`experiments/runs/2026-05-30-comparative-correlative-probe-v3/`](../../../experiments/runs/2026-05-30-comparative-correlative-probe-v3/README.md). Design: [`design/comparative-correlative-v3`](../../../experiments/designs/comparative-correlative-v3.md). Refines [`result/comparative-correlative-covariation-v2`](comparative-correlative-covariation-v2.md). **Internal-contrast-only** (`anchor: internal-contrast-only`; [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). Cost **$0.09326 billed**.

## Why this probe

[`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md) and [`result/comparative-correlative-covariation-v2`](comparative-correlative-covariation-v2.md) found the CC's proportional-covariation reading robust at/above ceiling (incl. multi-step composition and following the construction against conflicting world knowledge). Both probed the CC as an **asserted** relation. v3 asks the sharper `functional-vs-formal` question: does the model track the operator scope when the identical construction is **negated** or **hedged** — or does a surface template fire regardless? Unlike the v2 conflicting-cue arm (where the conflicting cue is extra-linguistic world knowledge), here the cancelling operator is **inside the sentence**, so the test is purely compositional-semantic. This is the embedded-CC arm the v2 design deferred to v3 under the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md) gate (no new decision).

## Method (frozen pre-run; numbers independently re-verified)

- **Stimuli** (project's own, frozen pre-run, sha256[:16] `98d1fd150e36fe30`): 16 items × 5 arms — `baseline-pos` (asserted positive CC), `baseline-inv` (asserted inverse CC — the **direction anchor** guarding against an INCREASE-bias readout), `negation` (negated positive CC), `modal-epistemic` (epistemically-hedged positive CC), `negation-inv` (negated *inverse* CC — the **control** against a flat "any 'not' → UNDETERMINED" heuristic, since negating a decrease does not entail an increase).
- **Instrument** reused verbatim from v1/v2: NLI hypothesis is always the positive covariation; FC asks INCREASE/DECREASE/UNDETERMINED. Temperature 0, no logprobs → the ratified 3-family panel ([`config/models.md`](../../../config/models.md)). FC is the **primary** instrument on the embedded arms (its UNDETERMINED gold is the least gold-contestable); NLI is secondary (its finer 2/1/1 per-arm gold is defensible but pragmatically debatable — see Caveats).
- **Reading rule** (ratified report-the-rate; no tuned bar): per-arm operator-correct rate, plus the **embedding-cancellation rate** (fraction of embedded items off the bare positive direction).
- **Adversarial passes:** an independent read-only pre-run critic re-derived every gold from the sentence text (VERDICT: sound to run as-is, all 16 golds correct); an independent read-only post-run verifier recomputed every figure from `raw/*.json` (VERDICT: **CLEAN — all figures verified**).

## Result

Operator-correct rate (% of non-null preds matching the per-arm, per-instrument gold):

| model | instr | base-pos | base-inv | negation | modal | negation-inv | embed-cancel |
|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | NLI | 100 | 100 | 100 | 100 | 100¹ | 100 |
| claude-sonnet-4.6 | FC | 100 | 100 | 100 | 100 | **66.7** | 100 |
| gpt-5.4-mini | NLI | 100 | 100 | 100 | **66.7** | 100 | 100 |
| gpt-5.4-mini | FC | 100 | 100 | **75** | **66.7** | **0** | 60 |
| gemini-3.5-flash | NLI | 100 | 100 | 100 | 100 | 100 | 100 |
| gemini-3.5-flash | FC | 100 | 100 | 100 | 100 | 100 | 100 |

¹ claude NLI `negation-inv` is over 2 valid items: the single NA (96 calls, 1 NA) is claude's NLI on `negi-alarm`, where it over-reasoned past the 64-token cap and emitted no digit (its FC for that item is present). `negi-alarm` is the hardest, doubly-recoded item.

**Two readings, both honest:**

1. **The covariation reading mostly survives operator embedding (support for CC robustness).** claude and gemini are at/near ceiling on every embedded arm — they withhold the covariation direction under negation and epistemic hedging and never collapse to the bare positive template. gemini is **100% on every arm, both instruments**. claude's only two slips are both on `negi-alarm` (FC→DECREASE, NLI→NA), the doubly-recoded item. So the v1/v2 ceiling is **not** a "the-more…the-more → INCREASE" template artifact: it survives an in-sentence operator that cancels the assertion. The `baseline-inv` arm (100% everywhere) confirms the panel is genuinely direction-tracking, not INCREASE-biased — closing a gap the v2 item set lacked.

2. **gpt-5.4-mini cracks under forced-choice, via over-inference (not template-firing).** Its FC errors are an **excluded-middle fallacy**: on `negation-inv` (0%) all three negated-inverse items are answered **INCREASE** — it treats ¬(X decreases) as entailing X increases; on one `negation` item it flips to **DECREASE** (¬increase ⟹ decrease); on one `modal` item it reads "Researchers still debate whether…" as **asserting** INCREASE. Crucially this is **over-inference, not a surface template** — gpt-5.4-mini withholds correctly on 3/4 direct negations and is at ceiling on both baselines, so it is not blindly saying INCREASE. Its NLI is much stronger (only a "unproven ⟹ false" slip, reading `mod-exercise`'s hedge as a contradiction). The failure is **instrument-localized** (FC ≫ NLI gap) and model-specific.

## Where it sits / how it relates

- **Supports** [`conjecture/comparative-correlative-construction`](../conjectures/comparative-correlative-construction.md) at the strong end: the covariation reading is robust enough to survive an operator that cancels the assertion (for 2/3 models, both instruments). Sits at the theory ladder's Tier-4 (inference-licensing), now stress-tested for compositional operator scope.
- **Refines** v2: v2 showed the panel follows the construction against *world knowledge*; v3 shows it also tracks an *in-sentence* cancelling operator — but exposes that this is not uniform across the panel.
- **Advances** [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md): another own-design result where gpt-5.4-mini diverges by instrument (NLI strong, FC weak), now with a precise mechanism (the excluded-middle over-inference under negation), not just a rate gap. The instrument-fragility is again confined to gpt-5.4-mini.
- **Contrast with the shallow side of** [`result/coercion-implicit-cue-v2b`](coercion-implicit-cue-v2b.md): there the decoders **under**-computed (affirmed an impossible coercion from an implicit cue); here the failing model **over**-computes (infers a direction the operator leaves open). The CC stays the project's most robust constructional positive, but v3 shows its robustness is model- and instrument-conditioned at the operator-scope frontier.

## Caveats (lead with these)

- **Internal-contrast-only; no human claim.** The Scivetti CC subset has no negated/hedged CC items → no in-repo human norm on the embedded arms. The baseline arms keep the v1/v2 phenomenon-level Scivetti CC anchor, but **no human-comparison claim** is made for the embedded arms. Tracked by [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md).
- **Small n; single run; text-only.** 16 items, 5 arms (3–4 items each), one temperature-0 pass per model. The per-arm rates rest on 3–4 items, so a single item moves a cell by 25–33 pp; read the *pattern* (claude/gemini ceiling vs gpt-5.4-mini's FC-localized over-inference), not the exact percentages.
- **The `negation` NLI gold assumes the strict-proposition reading.** "It is not true that the more X, the more Y" is scored as **contradicting** the positive hypothesis (nli_gold=2). Under a weaker pragmatic reading (denying only a strict/lawlike link while a weak positive association survives) it would be neutral. The strict reading was fixed pre-run and the pre-run critic judged it defensible; the FC primary instrument (UNDETERMINED gold) does not depend on this choice, and the headline (claude/gemini ceiling, gpt-5.4-mini FC over-inference) holds under either reading.
- **The 1 NA** (claude NLI `negi-alarm`) is a truncation artifact (over-reasoning past the 64-token cap), not a refusal; reported, not imputed.
- **First run on the corrected cost harness.** Cost is the API-**billed** `usage.cost` ([`experiments/lib/openrouter.py`](../../../experiments/lib/openrouter.py)); gemini billed 14× its rate-card estimate ($0.072 vs $0.005), confirming the prior token-estimate undercount.
