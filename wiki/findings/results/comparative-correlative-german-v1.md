---
type: result
id: comparative-correlative-german-v1
title: "German comparative-correlative replication (A6): the construction-isolation covariation contrast survives the surface-statistics change from English `the…the` to German `je…desto/umso` — REPLICATES 3/3, internal-contrast-only"
meaning-senses:
  - constructional
  - distributional
  - inferential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-12
updated: 2026-07-12
links:
  - rel: supports
    target: claim/comparative-correlative-covariation
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: design/comparative-correlative-german-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: source/meinunger-2023-je-desto
  - rel: depends-on
    target: resource/cross-linguistic-cc-replication-scouting
---

# Result — German comparative-correlative replication (A6)

> **VERDICT: REPLICATES 3/3.** On a **German** port of the frozen English comparative-correlative
> instrument, all three panel models isolate the proportional-covariation reading to the German CC
> construction (`je…desto/umso`) — a **within-model** construction-isolation assertion gap of **+92.6 /
> +88.2 / +88.2 pp** (claude / gpt / gemini; all 95% CI lower bounds ≥ +79), a **100 / 97 / 97%**
> inverse-direction flip, and a covariation reading that **persists at 95–100% on deliberately absurd
> scale pairs**. The reading does **not** track UD-German-GSD corpus frequency/co-occurrence. So the
> construction-driven reading survives a surface-statistics change from the English `the…the` template
> to a **different** function-word + verb-final-subordinate realization. This is a **partial** discharge
> of the distributional-shadow worry (German is typologically close and its CC is itself frequent — a
> *modest* lever; the typologically-distant Japanese arm is the stronger, committed-but-conditional
> successor). **`anchor: internal-contrast-only`** — a within-model claim only; **no human comparison**
> (no non-English CC human dataset exists per the scout), **no** claim of human-level German CC competence.

**Run:** 2026-07-12 (session 213), program A6. **Design (FROZEN):**
[`design/comparative-correlative-german-v1`](../../../experiments/designs/comparative-correlative-german-v1.md);
governed by [`decisions/resolved/cross-linguistic-cc-replication-scope`](../../decisions/resolved/cross-linguistic-cc-replication-scope.md)
(**Q1-C / Q2-B / Q3-A**, ratified s213 — this decision is the ratifying authority for the terminal
`internal-contrast-only` state, condition ix). **Ported from** the English powered instrument
[`result/comparative-correlative-covariation-powered`](comparative-correlative-covariation-powered.md)
(the ONLY change is the target language). **Run record:**
[`experiments/runs/2026-07-12-comparative-correlative-german/`](../../../experiments/runs/2026-07-12-comparative-correlative-german/).
816 probe calls + 36 smoke calls, **0 NA**, **$0.300** main + $0.013 smoke billed.

## What was run

A faithful **German port** of the frozen English v1/powered CC instrument: 34 German scale pairs
(24 typical + 10 atypical) × 4 forms = **136 items**, each pair reusing the **same scalar words** across
forms (the same-word non-CC controls). Forms: `cc-positive` (*Je* +comp … , *desto* +comp … → increase),
`cc-inverse` (… *desto* +antonym-comp … → decrease), `ctrl-two` (two independent declaratives),
`ctrl-single` (one comparative clause). Both instruments (forced-choice covariation direction; NLI),
all-German scaffolding, the ratified 3-family panel, temperature 0. Items **self-audited** against the
ingested German CC grammar source [`source/meinunger-2023-je-desto`](../../base/sources/meinunger-2023-je-desto.md)
(`je`-clause verb-final; `desto`/`umso`-clause verb-second) and **frozen (sha256) before the run**
(anti-cheat). A **German-competence smoke test** gated the run: all three models **12/12 (100%)** on
unambiguous non-CC German comprehension items — so a null could have been read as constructional
failure, not comprehension noise; the run was not withheld.

## Grounds — magnitudes with 95% CIs (cluster bootstrap over scale pairs, B=2000, seed 20260712)

Read the **orderings and rates**, not fitted coefficients: n = 3 models; per-cell counts are small
(single items move a cell several pp). Frozen thresholds (T1≥30pp / T2≥70% / T3 within 15pp) reported
for continuity with English v1; the deliverable is the point estimate + interval.

| quantity | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash |
|---|---:|---:|---:|
| FC CC covariation accuracy % | 100.0 [100,100] | 98.5 [95.6,100] | 98.5 [95.6,100] |
| **T1 construction-isolation assertion gap (pp)** | **+92.6 [83.8, 98.5]** | **+88.2 [79.4, 95.6]** | **+88.2 [80.9, 94.1]** |
| inverse-flip % (cc-inverse → decrease) | 100.0 [100,100] | 97.1 [91.2,100] | 97.1 [91.2,100] |
| positive-increase % | 100.0 [100,100] | 100.0 [100,100] | 100.0 [100,100] |
| typical − atypical accuracy (pp) | 0.0 [0,0] | 5.0 [0,16.7] | 5.0 [0,16.7] |
| atypical assertion % | 100.0 [100,100] | 95.0 [83.3,100] | 95.0 [83.3,100] |
| NLI CC accuracy % | 100.0 [100,100] | 98.5 [95.6,100] | 98.5 [95.6,100] |
| NLI cc-vs-ctrl accuracy gap (pp) | +2.9 [0,7.4] | −1.5 [−4.4,0] | −1.5 [−4.4,0] |

**The construction-isolation contrast (the load-bearing signal).** On the forced-choice instrument the
panel asserts a covariation direction for **100 / 98.5 / 98.5%** of German CC items but for only
**7.4 / 10.3 / 10.3%** of the matched same-word non-CC controls — a **+92.6 / +88.2 / +88.2 pp** gap,
every CI lower bound ≥ +79. This reproduces the English powered gap (≈87 pp, lb ≈78) in a language whose
CC surface form is different. **Direction, not template:** inverse CCs flip to *decrease* at 100/97/97%.
**Not memorization/n-gram:** the covariation reading persists at **100 / 95 / 95%** on the 10 absurd
scale pairs (teacup roundness ↔ traffic-jam length, …) whose direction can come only from the
construction. **Cross-instrument:** NLI CC accuracy is 100/98.5/98.5% and NLI control accuracy is
97.1/100/100% (the models correctly read controls as *neutral*), so the small NLI cc-vs-ctrl gap
reflects both cells near ceiling, not a failure. Gates: **T1 3/3, T2 3/3, T3 3/3.**

## Q2-B frequency/co-occurrence control (UD German-GSD, CC BY-SA 4.0 — freeze condition vi)

Frozen before the run ([`freq_control.json`](../../../experiments/runs/2026-07-12-comparative-correlative-german/freq_control.json)):
per-pair UD-German-GSD content-word (ADJ+NOUN) frequency + in-corpus co-occurrence. The residual
loophole this closes — does the covariation reading track corpus **frequency/association** rather than
the construction? — is answered **no**:

- **CC-assertion is at ceiling regardless of corpus frequency** (typical vs atypical CC-assertion:
  1.00/1.00/1.00 vs 1.00/0.95/0.95), so ρ(CC-assertion, mean-freq) is undefined/≈0.08 (no variance).
- **Control-assertion does not rise with co-occurrence** (ρ(ctrl-assertion, co-occurrence) =
  +0.04 / −0.16 / −0.18) — the models do not read covariation into controls more when the scalar words
  co-occur.
- The construction-isolation **gap** has only a weak positive frequency dependence
  (ρ(iso-gap, mean-freq) = +0.10 / +0.29 / +0.30) — not a strong confound.
- The **primary** co-occurrence control is the typical/atypical split itself: the 10 atypical pairs have
  near-zero UD-GSD co-occurrence (mean 3.4 sentences; 1.5 content words/pair outright OOV) yet get the
  covariation reading at 95–100%.

**Caveat (pre-run critic C2, stated plainly).** The automatic lemma resolver has bounded form→noun
collision noise (the copula surface `waren`/`war` resolves to the content noun *Ware*; `vertrauten`→
*Vertraute*; `Start-ups`→*Start*), which inflates some frequency/co-occurrence counts. It is **frozen,
symmetric across typical/atypical, and feeds only this corroboration covariate** — it does not touch the
primary construction-isolation contrast. The Q2-B arm is a **bounded corroboration covariate**, not a
clean frequency match; the typical/atypical split carries the primary co-occurrence control.

## Scope — what this result does and does NOT claim

- **Does:** a **within-model** result that the CC construction-isolation covariation contrast **survives**
  the English→German surface-statistics change, with the magnitudes/intervals above. A **partial**
  discharge of the distributional-shadow worry for [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md):
  the panel's covariation reading is not merely English-`the…the`-n-gram matching, since it reproduces on
  a different surface realization.
- **Does NOT:** any human comparison (`anchor: internal-contrast-only`; ratified Q3-A — no non-English CC
  human dataset exists); any claim of **human-level** German CC competence; any claim that German
  **fully** discharges the shadow worry. German is typologically close to English and its CC is itself a
  frequent template — a *modest* lever. The **Japanese** arm (`-ba…hodo`, typologically distant) is the
  stronger, **committed-but-conditional** successor (Q1-C), gated on this German replication + Japanese
  CC-form source-verification + a Japanese competence smoke test.
- **n = 3 models** remains a hard bound; the panel reading is a convergence across three decoders, not a
  population estimate. Absolute near-ceiling accuracy is consistent with (but does not require) some
  German CC exposure in pretraining; the load-bearing signal is the **within-model gap** (CC vs
  same-word control), which no amount of exposure to the words alone produces.

## Verifier note

Post-run figures reproduce from the committed `raw/` outputs via `analyze.py` (0 NA / 816 calls).
Instrument frozen: `sha256(items.csv)=2c2301c8…`, `sha256(freq_control.json)=cae2d144…` (unchanged from
the pre-run freeze). Gold labels were fixed before generation; thresholds are continuity-only and were
not retuned. Per the pre-registered symmetric frame, a null would have been first-class; the result is a
positive replication.
