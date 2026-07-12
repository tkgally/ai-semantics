---
type: result
id: comparative-correlative-japanese-v1
title: "Japanese comparative-correlative replication (A6): the construction-isolation covariation contrast survives the typologically-distant surface-statistics change to Japanese `〜ば〜ほど` (no overt comparative morpheme) — REPLICATES 3/3, internal-contrast-only"
meaning-senses:
  - constructional
  - distributional
  - inferential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: supports
    target: claim/comparative-correlative-covariation
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: design/comparative-correlative-japanese-v1
  - rel: depends-on
    target: result/comparative-correlative-german-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: source/japanese-ba-hodo-cc
  - rel: depends-on
    target: resource/cross-linguistic-cc-replication-scouting
---

# Result — Japanese comparative-correlative replication (A6)

> **VERDICT: REPLICATES 3/3.** On a **Japanese** port of the frozen English/German comparative-correlative
> instrument, all three panel models isolate the proportional-covariation reading to the Japanese CC
> construction (`〜ば〜ほど`) — a **within-model** construction-isolation assertion gap of **+94.1 / +83.8 /
> +95.6 pp** (claude / gpt / gemini; all 95% CI lower bounds ≥ +75), a **100 / 100 / 97.1%** inverse-direction
> flip, and a covariation reading that **persists at 100 / 95 / 95% on deliberately absurd scale pairs**. The
> reading does **not** track UD-Japanese-GSD corpus frequency/co-occurrence. Japanese is the **typologically
> distant** lever the scope decision reserved as the *stronger* test (SOV, agglutinative, verb-final, and
> crucially **no overt comparative morpheme** — no `-er`/`more`/`mehr`/`desto`; the "more" is carried entirely
> by the ば…ほど frame + predicate repetition). So the construction-driven reading survives a surface-statistics
> change far larger than German's — a **stronger** discharge of the distributional-shadow worry, though **still
> partial** (n = 3 decoders; two non-English languages ≠ all) and **still within-model**. **`anchor:
> internal-contrast-only`** — no human comparison (no non-English CC human dataset exists per the scout), **no**
> claim of human-level Japanese CC competence.

**Run:** 2026-07-13 (session 215), program A6, the **Japanese** (stronger, typologically-distant) arm — the
committed-but-conditional successor the scope decision names (Q1-C), unblocked by the German replication
(s213, REPLICATES 3/3) + `-ba…hodo` source-verification (s215). **Design (FROZEN):**
[`design/comparative-correlative-japanese-v1`](../../../experiments/designs/comparative-correlative-japanese-v1.md);
governed by [`decisions/resolved/cross-linguistic-cc-replication-scope`](../../decisions/resolved/cross-linguistic-cc-replication-scope.md)
(**Q1-C / Q2-B / Q3-A**, ratified s213 — the ratifying authority for the terminal `internal-contrast-only`
state, condition ix). **Ported from** the English powered instrument
[`result/comparative-correlative-covariation-powered`](comparative-correlative-covariation-powered.md) and its
German port [`result/comparative-correlative-german-v1`](comparative-correlative-german-v1.md) (the only change
is the target language). **Run record:**
[`experiments/runs/2026-07-13-comparative-correlative-japanese/`](../../../experiments/runs/2026-07-13-comparative-correlative-japanese/).
816 probe calls + 36 smoke calls, **0 NA**, **$0.296** main + $0.012 smoke billed.

## What was run

A faithful **Japanese port** of the frozen English/German CC instrument: 34 Japanese scale pairs
(24 typical + 10 atypical) × 4 forms = **136 items**, each pair reusing the **same scalar words** across
forms (the same-word non-CC controls). Forms: `cc-positive` (`〜ば〜ほど`, dim2 rises → increase),
`cc-inverse` (same antecedent, dim2 falls → decrease), `ctrl-two` (two independent declaratives),
`ctrl-single` (one より-comparative clause, dim2 unmentioned). Both instruments (forced-choice covariation
direction; NLI), all-Japanese scaffolding (FC answers 増加/減少/不明; NLI digit), the ratified 3-family panel,
temperature 0. Items **self-audited** against the ingested Japanese CC grammar source
[`source/japanese-ba-hodo-cc`](../../base/sources/japanese-ba-hodo-cc.md) (antecedent `[Pred‑ば][Pred]ほど`
with predicate repetition; verb-final consequent) and **frozen (sha256) before the run** (anti-cheat). A
**pre-run critic** (fresh-agent, verdict authority, GO + a non-Anthropic Japanese-fidelity vote whose
substantive point was honored as **condition C1** — four cc-inverse consequents made explicitly
scale-decreasing before the run) and a **Japanese-competence smoke test** (all three models **12/12 (100%)**
on unambiguous non-CC Japanese items — so a null could have been read as constructional failure, not
comprehension noise) gated the run.

## Grounds — magnitudes with 95% CIs (cluster bootstrap over scale pairs, B=2000, seed 20260713)

Read the **orderings and rates**, not fitted coefficients: n = 3 models; per-cell counts are small (single
items move a cell several pp). Frozen thresholds (T1≥30pp / T2≥70% / T3 within 15pp) reported for continuity;
the deliverable is the point estimate + interval.

| quantity | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash |
|---|---:|---:|---:|
| FC CC covariation accuracy % | 100.0 [100,100] | 98.5 [95.6,100] | 98.5 [95.6,100] |
| **T1 construction-isolation assertion gap (pp)** | **+94.1 [88.2, 98.5]** | **+83.8 [75.0, 91.2]** | **+95.6 [89.7, 100.0]** |
| inverse-flip % (cc-inverse → decrease) | 100.0 [100,100] | 100.0 [100,100] | 97.1 [91.2,100] |
| positive-increase % | 100.0 [100,100] | 97.1 [91.2,100] | 100.0 [100,100] |
| typical − atypical accuracy (pp) | 0.0 [0,0] | 5.0 [0,16.7] | 5.0 [0,16.7] |
| atypical assertion % | 100.0 [100,100] | 95.0 [83.3,100] | 95.0 [83.3,100] |
| NLI CC accuracy % | 100.0 [100,100] | 89.7 [82.4,95.6] | 97.1 [92.6,100] |
| NLI cc-vs-ctrl accuracy gap (pp) | +2.9 [0,7.4] | −4.4 [−14.7,5.9] | −2.9 [−7.4,0] |

**The construction-isolation contrast (the load-bearing signal).** On the forced-choice instrument the panel
asserts a covariation direction for **100 / 98.5 / 98.5%** of Japanese CC items but for only
**5.9 / 14.7 / 2.9%** of the matched same-word non-CC controls — a **+94.1 / +83.8 / +95.6 pp** gap, every CI
lower bound ≥ +75. This reproduces the English powered gap (≈87 pp, lb ≈78) and the German gap
(+92.6/+88.2/+88.2) in a language whose CC surface form is **radically different** — no comparative morpheme,
verb-final, agglutinative. **Direction, not template:** inverse CCs flip to *decrease* at 100/100/97%.
**Not memorization/n-gram:** the covariation reading persists at **100 / 95 / 95%** on the 10 absurd scale
pairs (teacup roundness ↔ traffic-jam length, sock stripes ↔ thunder loudness, …) whose direction can come
only from the construction. **Cross-instrument:** NLI CC accuracy is 100/89.7/97.1% and NLI control accuracy
is 97.1/94.1/100% (the models correctly read controls as *neutral*), so the small/negative NLI cc-vs-ctrl gaps
reflect both cells near ceiling, not a failure. Gates: **T1 3/3, T2 3/3, T3 3/3.**

**gpt-5.4-mini is again the weakest arm** (T1 +83.8, the lowest of the three; NLI CC 89.7; it over-reads a
direction into 14.7% of controls) — the same "weakest/most-elicitation-sensitive" pattern the English powered
re-run and German arm show for this model. All three signatures still clear their gates on it.

## Q2-B frequency/co-occurrence control (UD Japanese-GSD, CC BY-SA 4.0 — freeze condition vi)

Frozen before the run ([`freq_control.json`](../../../experiments/runs/2026-07-13-comparative-correlative-japanese/freq_control.json)):
per-pair UD-Japanese-GSD content-word (NOUN+ADJ) frequency + in-corpus co-occurrence, with both the corpus
sentences and the items tokenized by the **same analyzer** (janome 0.5.0, IPAdic) — a documented
Japanese-specific consistency choice (Japanese is unsegmented; see the design's *Q2-B* section). The residual
loophole this closes — does the covariation reading track corpus **frequency/association** rather than the
construction? — is answered **no**:

- **CC-assertion is at ceiling regardless of corpus frequency** (typical vs atypical CC-assertion:
  1.00/1.00/1.00 vs 1.00/0.95/0.95), so ρ(CC-assertion, mean-freq) is undefined/small
  (None/−0.15/+0.17; no variance to correlate against).
- **Control-assertion does not rise with co-occurrence** (ρ(ctrl-assertion, co-occurrence) =
  −0.33 / −0.05 / +0.04) — the models do not read covariation into controls more when the scalar words
  co-occur.
- The construction-isolation **gap** has only a weak frequency dependence (ρ(iso-gap, mean-freq) =
  +0.06 / +0.20 / +0.13) — not a strong confound.
- The **primary** co-occurrence control is the typical/atypical split itself: the 10 atypical pairs have
  near-zero UD-Japanese-GSD co-occurrence (mean ≈1.1 sentences; ~1.3 content words/pair OOV) yet get the
  covariation reading at 95–100%.

**Caveat (stated plainly, as in the German arm).** The UD-Japanese-GSD corpus is small (8,100 sentences), so
co-occurrence is sparse for **both** families (typical ≈0.7, atypical ≈1.1 sentences) — the corpus cannot
strongly *separate* typical from atypical, and the janome cross-tokenization emits a little collision noise
(e.g. っぽい split from 飽きっぽい). This Q2-B arm is therefore a **bounded corroboration covariate**, not a
clean frequency match; the **typical/atypical split by design** (absurd pairs are absurd regardless of corpus
counts) carries the primary co-occurrence control, and the covariate adds only that the reading does not
visibly track what corpus frequency signal the small treebank does provide.

## Scope — what this result does and does NOT claim

- **Does:** a **within-model** result that the CC construction-isolation covariation contrast **survives** the
  English→Japanese (typologically distant) surface-statistics change, with the magnitudes/intervals above. A
  **stronger** (than German) partial discharge of the distributional-shadow worry for
  [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md): the panel's
  covariation reading is not English-`the…the`-n-gram matching, nor even Germanic-template matching, since it
  reproduces on a construction with **no comparative morpheme at all**.
- **Does NOT:** any human comparison (`anchor: internal-contrast-only`; ratified Q3-A — no non-English CC human
  dataset exists); any claim of **human-level** Japanese CC competence; any claim that Japanese **fully and
  finally** closes the shadow worry. n = 3 decoders and two non-English languages beyond English is not "all
  languages" — the reading remains a within-model convergence across three decoders, not a population estimate.
- **gpt-5.4-mini non-uniformity** (weakest T1, some control over-reading) is carried explicitly, not averaged
  away; it clears every gate but is the elicitation-sensitive arm, consistent with the rest of the CC line.
- Absolute near-ceiling accuracy is consistent with (but does not require) some Japanese CC exposure in
  pretraining; the load-bearing signal is the **within-model gap** (CC vs same-word control), which no amount
  of exposure to the words alone produces.

## Verifier note

Post-run figures reproduce from the committed `raw/` outputs via `analyze.py` (0 NA / 816 calls). An
**independent fresh-agent post-run verifier** (s215) re-ran `analyze.py`, recomputed every headline metric
straight from the raw JSON (bypassing the analyzer), re-derived the CC/control assertion rates, confirmed
0 NA across all 6 raw files and 816 = 34×4×2×3 records, and checked every number in this page against the
analyzer → **REPRODUCED, 0 discrepancies**; over-claim check **PASS** (the `internal-contrast-only` /
within-model / stronger-than-German-but-not-final framing calibrated; gpt-5.4-mini's weakness carried, not
averaged; the Q2-B bounded-covariate caveat honest about the small corpus). Instrument frozen:
`sha256(items.csv)=31597d29…`, `sha256(freq_control.json)=02d275a1…` (post-C1 freeze, live-verified by the
verifier, unchanged from the pre-run commit). Gold labels were fixed before generation; thresholds are
continuity-only and were not retuned. Per the pre-registered symmetric frame, a null would have been
first-class (and, on the stronger lever, especially informative); the result is a positive replication.
