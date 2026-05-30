---
type: result
id: caused-motion-near-miss-v2c
title: Caused-motion v2c (near-miss form control) — the construction's causation inference is genuinely form-keyed (construction 100% affirm vs near-miss withheld; gap 62.5–100 pp under forced-choice), tightening the v1 floor; NLI is more permissive of the Gricean causal reading
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: proposed
anchor: pending
contingent-on:
  - conflicting-cue-human-anchor
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: refines
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: supports
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: open-question/instrument-sensitivity-constructional-inference
---

# Result: caused-motion probe v2c (near-miss form control)

**One-line:** holding the verb + object + displacement **outcome** roughly constant and varying only the **form**, the caused-motion construction's causation-of-motion inference is **genuinely keyed on the construction form**, not on a loose "verb happened + object ended up displaced → caused it" shape. All three models affirm the causation at **100%** for the construction but **withhold** it substantially for near-miss frames (coordinated *and* / temporal sequence), with the construction-vs-near-miss gap **62.5–100 pp under forced-choice**. This **tightens the v1 floor**. NLI is more permissive of the **Gricean** post-hoc causal reading (the *and*-frame is read as causation-entailing more often), so the gap is smaller there — a general instrument/form effect across all three models, not a single-model crack.

Run record: [`experiments/runs/2026-05-30-caused-motion-near-miss-probe-v2c/`](../../../experiments/runs/2026-05-30-caused-motion-near-miss-probe-v2c/README.md). Design: [`design/caused-motion-near-miss-v2c`](../../../experiments/designs/caused-motion-near-miss-v2c.md). Refines [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md). **Internal-contrast-only** (`anchor: pending`; [`decisions/open/conflicting-cue-human-anchor`](../../decisions/open/conflicting-cue-human-anchor.md)). Cost **$0.21213 billed**.

## Why this probe

[`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md) found the panel affirms the caused-motion construction's causation-of-motion entailment onto **non-motion verbs at ceiling** (90–100%), but its controls were *absent-construction* (no displacement / object moved by another cause). That leaves open whether the ceiling is **construction-specific** or rests on a looser heuristic: "a verb happened and the object ended up displaced, so the verb caused it" (or a Gricean post-hoc-ergo-propter-hoc default). v2c is the **near-miss form control** the off-ceiling coercion v2 specified and deferred: it holds the verb, object, and end-state roughly constant and varies only the **form** between the caused-motion construction and two near-miss frames that report the same content **without** construction-licensing the causation. Run under the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md) gate (no new decision).

## Method (frozen pre-run; numbers independently re-verified)

- **Stimuli** (project's own, frozen pre-run, sha256[:16] `a60b812d4b46bcc4`): 24 items = 8 scenes × 3 forms. The **hypothesis is held identical across the three forms within each scene** ("`<Subj>`'s `<gerund>` caused `<obj>` to move"), so only the form varies:
  - `cm-construction` — the construction (*Maria sneezed the napkin off the table.*);
  - `near-coord` — coordinated *and* (*Maria sneezed, and the napkin ended up off the table.*);
  - `near-seq` — temporal sequence (*Maria sneezed. Moments later, the napkin was off the table.*).
  All 8 scenes are **clean inanimate-propulsion** (sneeze/cough/blow/puff/huff/fan on napkin/crumb/dust/feather/wrapper/smoke/petal/confetti) — the pre-run critic flagged the original animate "whistled the dog" (signaling) / "clapped the pigeon" (startle) / anomalous "laughed the straw" items as heterogeneous causal relations, and they were replaced **before the run** so the construction's physical-causation reading is uniform.
- **Instrument** reused verbatim from the caused-motion v1/v2b harness: NLI 0/1/2; FC "is this statement true: `<hyp>`?" YES/NO/CANT_TELL. Affirm-causation = NLI entailment (0) / FC YES. Temperature 0, no logprobs → the ratified 3-family panel ([`config/models.md`](../../../config/models.md)).
- **Reading rule** (ratified report-the-rate; no tuned bar): per-arm affirm rate + the **construction-vs-near-miss gap** (the internal contrast). The near-miss "withhold" gold labels only the strict-entailment-correct direction; the headline is the within-scene gap (the near-miss withhold reading is pragmatically contestable — Gricean).
- **Adversarial passes:** independent read-only pre-run critic (no BLOCKER; the homogeneity SHOULD-FIX above was applied, re-freezing the set) + independent read-only post-run verifier (every figure recomputed from `raw/*.json` → **CLEAN**).

## Result

Affirm-causation rate (% YES/entailment; n=8 per cell, 0 NA):

| model | instr | cm-construction | near-coord | near-seq | gap (cm − pooled near-miss) |
|---|---|---|---|---|---|
| claude-sonnet-4.6 | NLI | 100 | 87.5 | 75.0 | 18.8 |
| claude-sonnet-4.6 | FC | 100 | 62.5 | **0** | **68.8** |
| gpt-5.4-mini | NLI | 100 | 87.5 | 37.5 | 37.5 |
| gpt-5.4-mini | FC | 100 | 62.5 | 12.5 | **62.5** |
| gemini-3.5-flash | NLI | 100 | 62.5 | 25.0 | 56.2 |
| gemini-3.5-flash | FC | 100 | **0** | **0** | **100.0** |

**Three readings:**

1. **The caused-motion ceiling is construction-keyed (tightens v1's floor).** The construction is affirmed at 100% everywhere, but near-miss frames carrying the *same verb + end-state* are withheld substantially — a 62.5–100 pp gap under forced-choice (gemini a perfect 100%→0% discrimination). So the v1 causation inference does **not** come from a loose "displacement happened → the verb caused it" shape; it is keyed on the **argument-structure form**. This is a genuine `functional-vs-formal` floor result and a positive for [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md).
2. **The gap is instrument-dependent — NLI is more permissive of the Gricean causal reading.** Under NLI the gaps shrink (18.8 / 37.5 / 56.2 pp) because the coordinated *and*-frame is affirmed as causation-entailing far more often (NLI 87.5 / 87.5 / 62.5% vs FC 62.5 / 62.5 / 0%). "X sneezed, and the napkin ended up off the table" pragmatically implicates that the sneeze did it; under an entailment-strict FC framing the panel withholds, under NLI it more often affirms. The **temporal-sequence** frame is the cleaner withhold than the *and*-frame across the board (NLI 75 / 37.5 / 25%; FC 0 / 12.5 / 0%) — exactly the pre-run critic's prediction.
3. **This is a general instrument/form effect, not a single-model crack.** Unlike the conative ([`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md)) and CC v3 ([`result/comparative-correlative-covariation-v3`](comparative-correlative-covariation-v3.md)), where gpt-5.4-mini was the instrument outlier, here all three models show the same NLI-more-permissive-than-FC and near-coord-noisier-than-near-seq pattern. The instrument sensitivity tracks the **pragmatics/entailment boundary**, not a model idiosyncrasy.

## Where it sits / how it relates

- **Refines** [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md): v1's at-ceiling caused-motion affirmation survives a tighter floor — it is construction-driven, not a displacement-detection heuristic. The "add direction is easy" reading on the theory page is reinforced *and* qualified (easy, but genuinely constructional).
- **Advances** [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md) with a **new kind** of instrument effect: a *content-level* NLI-vs-FC divergence (NLI admits the pragmatic causal inference; FC enforces strict entailment), uniform across the panel — distinct from the gpt-5.4-mini-specific cross-instrument cracks the conative/CC-v3 showed. It suggests at least two sources of instrument fragility: a model-specific one and this general pragmatics/entailment one.
- **Sits at** the theory ladder's Tier-4 (inference-licensing): it sharpens what "the construction licenses the inference" means by showing the inference is withheld when the construction is removed but the lexical content kept.

## Caveats (lead with these)

- **Internal-contrast-only; no human claim.** Scivetti has no coordinated/sequence near-miss items → no in-repo human norm on the near-miss arms. The `cm-construction` arm keeps the v1 phenomenon-level caused-motion anchor; **no human-comparison claim** is made for the near-miss arms. Tracked by [`decisions/open/conflicting-cue-human-anchor`](../../decisions/open/conflicting-cue-human-anchor.md).
- **The near-miss "withhold" gold is the strict-entailment reading.** A Gricean reader genuinely infers causation from the *and*-frame, so a model that affirms `near-coord` is not simply wrong — which is why the headline is the within-scene **gap**, not accuracy against the near-miss gold. The result is the *contrast*, and it is robust under either reading of the near-miss.
- **Small n; single run; text-only.** 8 scenes per form, one temperature-0 pass per model. Read the pattern (construction 100% vs near-miss withheld, FC sharper than NLI), not the exact per-cell percentages.
- **Cost note.** Billed `usage.cost` ([`experiments/lib/openrouter.py`](../../../experiments/lib/openrouter.py)); gemini billed ~15× its rate-card estimate (reasoning tokens), reconfirming the budget-tracking fix.
