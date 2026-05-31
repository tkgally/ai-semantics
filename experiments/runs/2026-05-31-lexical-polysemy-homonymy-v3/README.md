# Run record — lexical-v3: polysemy-vs-homonymy discreteness on a homonymy-enriched WiC noun subset

**Date:** 2026-05-31 · **Design:** [`design/lexical-polysemy-homonymy-v3`](../../designs/lexical-polysemy-homonymy-v3.md) · **Anchor:** [`resource/wic-word-in-context`](../../../wiki/base/resources/wic-word-in-context.md) (WiC binary same/different-sense, CC BY-NC 4.0; Tom decision 3a) · **Conjecture:** [`conjecture/lexical-sense-gradience`](../../../wiki/findings/conjectures/lexical-sense-gradience.md) clause (b).

This is the clean clause-(b) re-run the [`result/lexical-polysemy-homonymy-v2`](../../../wiki/findings/results/lexical-polysemy-homonymy-v2.md) null pointed to: DWUG EN held only **3 clean homonym lemmas**; WiC supplies a homonymy-enriched, human-rated (binary) contrast. The instrument is the **same ratified graded panel as v1** (gate Q1: DURel 4-point + 0–100); the human anchor is WiC's **binary** T(same)/F(different) label; all claims scoped to a **binary same/different separation**, never a graded correlation (WiC has no graded axis).

## FREEZE (recorded BEFORE any model call)

| Artifact | sha256 |
|---|---|
| `WiC_dataset.zip` (pilehvar package, ships test gold) | `f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2` |
| `manifest.csv` (161 items: WiC id + lemma + pos + gold + stratum + overlap covariate; **NO corpus sentences**) | `89dff8e9442ce14128887b59c9c22493019664d526903630bc42a1004dce868e` |
| `stratification.csv` (the design-added polysemy/homonymy layer, etymology-sourced) | `dc74fddb464d7b1cd2df48ce7639f1766b8165657479a9559b72696efffdd5e6` |

Freeze means: the item set, the stratification, the indicators (`analyze.py`), the model-floor band (durel=1, cont≤10), the permutation/bootstrap machinery, and the overlap-matched control are **all fixed before any probe call**. No threshold is tuned after seeing ratings.

## Item set (frozen)

| Stratum | lemmas (n=11 each) | T items | F items | total |
|---|---|---|---|---|
| **HOMONYM** | ball, bank, case, date, pitch, pitcher, plane, rock, school, seal, tear | 21 | 39 | 60 |
| **POLYSEME** | bed, body, court, drink, fire, grain, heart, mouth, stick, train, voice | 36 | 65 | 101 |

161 items total. NOUNS only (homonymy is cleanest/most concrete for nouns; matches the WordNet noun-synset framing of [`resource/wordnet-sense-inventory`](../../../wiki/base/resources/wordnet-sense-inventory.md)). Calls = 161 × 2 framings × 3 models = **966**.

## Stratification method — etymology-grounded (gate Q2), NOT the bare WordNet structural rule

Tom's steer this round was to *prefer the gate's WordNet lexicographer-file rule over the etymological fallback* now that nltk WordNet is installable. I **evaluated** that rule (`explore.py`) and recorded a methodological finding:

> **The bare WordNet lexicographer-file + hypernym rule OVER-CALLS homonymy ~6:1.** Of 2,585 WiC (lemma,pos) keys it labels **1,487 HOMONYM vs 869 POLYSEME**, flagging textbook **polysemes** like *make, break, take, head, work, play* as homonyms — because WordNet's fine sense granularity scatters *related* senses across different lexnames with shallow common hypernyms (e.g. *make* → 44 "clusters"). For verbs it is essentially useless (no unique beginner; sense inflation). For nouns it still mislabels **light** as a homonym (2 noun clusters) when the noun is single-origin.

So the gate's **etymology AND-condition is load-bearing**, exactly as written ("different lexicographer files … **and** distinct etymologies"). The classifier used here is therefore the **etymology-grounded rule** (as in v2), restricted to nouns, with the WordNet structural signal recorded only as a supporting cue:

- **HOMONYM** — the noun has **≥2 distinct etymological origins, both common in general modern English** (separate Wiktionary "Etymology N" sections / distinct Etymonline headwords, each carrying a common noun sense), backed by a **quoted** distinct-origin statement in `stratification.csv`.
- **POLYSEME** — one general-register origin (senses related by metaphor/metonymy/specialization).
- **AMBIGUOUS → EXCLUDED** — references disagree, or the second origin is rare/archaic/narrowly-technical/regional. Recorded with reason, applied uniformly. Excluded this run: **grave** (2nd noun technical/archaic), **key** (island sense regional), **light** (the WordNet false-homonym: noun single-origin, *not-heavy* root is adj/verb).

Etymology evidence was gathered verbatim from Wiktionary + Etymonline (an independent fetch pass), **blind to any model rating** (no model has been called at freeze time); the classification calls are the orchestrator's, recorded with quotes in `stratification.csv` for audit.

**Granularity limit (lemma-level).** WiC does not expose the underlying sense ids per item, so the homonym/polyseme label is applied at the **lemma** level. A homonym lemma's F (different-sense) items are *more likely* cross-etymon than a polyseme lemma's F items, but some homonym-F items may be within-etymon polysemy splits (e.g. *case* = instance-vs-legal-case, both from *casus*). This dilutes the homonym signal toward the null — a conservative direction. Stated in the result.

## Indicators (frozen; report-the-number, NO pass bar)

Human anchor = WiC binary label; model signal = graded relatedness rating *r* (durel 1–4 / cont 0–100). Per model × framing:
- **(P-b-ii)** per-stratum **AUC**(*r* vs T/F) computed separately within HOMONYM and POLYSEME, + mean T−F gap. Headline = **AUC_homonym − AUC_polyseme** (predicted **positive**).
- **(P-b-i)** among **F** items, mean *r* and **floor-fraction** (durel=1 / cont≤10) by stratum. Headline = **floorfrac_homonymF − floorfrac_polysemeF** (predicted **positive**); mean_r_homonymF < mean_r_polysemeF.
- **Uncertainty:** whole-**lemma** label-permutation null (10k) for both headline diffs; bootstrap CI (5k) on the AUC diff.
- **Matched control:** overlap by stratum×gold + AUC diff recomputed on the low-overlap subset (overlap ≤ global median).

**Nulls are first-class:** N1 (no separable homonym low mode), N2 (equal separation). A clean N1+N2 *closes* clause (b) with adequate power — the point of v3. Lead with the null if N1/N2 hold.

## Protocol status

- [x] Build + freeze (sha256 above) — **before any model call**
- [ ] Independent pre-run stratification critique (read-only)
- [ ] 30-item billed pre-flight (drop to durel-only if it projects > $5; flag NEXT.md if still > $5)
- [ ] Run 966 calls (temp 0, logprob-free)
- [ ] Independent post-run number verification
- [ ] Write result page (null-first if N1/N2 hold)

## Cost

Estimate ≈ $1.7 billed (966 calls, 2 framings; v1 ran 1,800 calls / 3 framings for $3.13, gemini-dominated). Under the $5 single-run flag; pre-flight confirms.

## Files

- `explore.py` / `explore_nouns.py` — WiC + WordNet survey (no API); produced the over-call finding above.
- `build_items.py` — downloads WiC (gitignored), applies `stratification.csv`, emits `manifest.csv` (committed) + `fulltext.jsonl` (gitignored), prints sha256s.
- `stratification.csv` — the frozen etymology-grounded polysemy/homonymy layer (committed).
- `manifest.csv` — committed (ids/gold/stratum/overlap; no corpus text).
- `probe.py` — the panel runner (durel+cont × 3 models); imports `experiments/lib/openrouter.py`.
- `analyze.py` — per-stratum AUC + T−F gap + floor-fraction + permutation + bootstrap + overlap-matched (pure-Python).
