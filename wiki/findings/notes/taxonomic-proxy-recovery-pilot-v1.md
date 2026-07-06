---
type: note
id: taxonomic-proxy-recovery-pilot-v1
title: "Taxonomic-proxy recovery pilot v1 — a $0 exploratory pass + provisional pre-registration of one IS-A structural proxy for the future H1+H2 relation-recovery probe (NOT a test of H2)"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: depends-on
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: theory/shadow-depth-table-v1
---

# Note: taxonomic-proxy recovery pilot v1 (method / pre-registration record)

> **Status: recorded (s188, 2026-07-06). A $0 method + pre-registration record. It makes NO new
> claim about LLM recovery and it CANNOT confirm or fire H2.** Every quantity here is either a
> **structural statistic of WordNet** (computed over the s186 cue sets — a property of WordNet, not
> of any model) or a figure **cited from** [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md).
> **No API call, no model call, no human comparison** was made. The correlations below are
> **EXPLORATORY over the very same n = 6 relations that *generated* the H2 hypothesis**
> ([`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md)), so
> they are circular by construction and cannot test it. Per the `note` page type
> ([`CLAUDE.md`](../../../CLAUDE.md)) this record carries **no new measurement** and is **never sole
> support for a claim**. Scope caps carried from s186: `internal-contrast-only`; **nouns only**;
> **n = 6 relations, exploratory**; the s186 residual arm is **descriptive-only** (its calibration
> gate fired).

## Why this note exists (and what it is forbidden from doing)

The essay [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md)
registers a two-part bet ([`predictions.md`](../../predictions.md) §B). **H2** predicts that, on a
**fresh** relation-recovery test, recovery rank tracks *"a **pre-registered
taxonomic/definitional-structure proxy** (IS-A / hypernym-tree connectivity, or a definitional-frame
statistic — **not** bare gold fan-out)"* **better than** it tracks contrastive-frame cue-strength.
The essay is explicit that H2 **may not be fired off the s186 data**: it "*did not measure*" any
taxonomic proxy, the pattern is "*read off the ranking, not a result*," and firing requires a fresh
probe with the proxy fixed **before** recovery is seen.

This note does the **design due-diligence** for that future probe, and nothing more:

1. It computes a small, **a-priori** set of WordNet structural proxies over the s186 cue sets and
   reports their **exploratory** n = 6 rank correlation with s186 recovery — transparently, the ones
   that correlate and the ones that do not.
2. It re-confirms that **bare gold fan-out** (the crude proxy the essay says s186 already breaks)
   does **not** track recovery — the known-fails baseline.
3. It **pre-registers exactly one** frozen proxy specification, on **principled** grounds, as the
   default taxonomic proxy for the future fresh H1+H2 probe — **provisionally**, subject to that
   probe's own pre-run critic and cross-session ratification.

**What this note may not do, and does not do:** it does **not** fire, confirm, weaken, or partially
discharge H2; it does **not** create a `claim` or `result`; it does **not** compare any model to any
human. H2 is dischargeable **only** by a fresh test (fresh relation set / different control corpus /
the named adjective-antonymy replication) whose proxy was pre-registered before its recovery was
observed. That test is not this note.

## Lead caveat — why the exploratory correlations below cannot count as evidence

- **Circularity.** The taxonomic-structure hypothesis was **read off** the s186 recovery ranking
  (hypernymy/antonymy best; part-whole worst). Correlating a proxy against *that same ranking* asks
  whether a story fits the data that suggested it. It can only ever "succeed"; it is a sanity/pilot
  check, not a test.
- **n = 6.** Six relations. A Spearman on n = 6 has an enormous confidence interval; the two-sided
  p-values reported are shown **only** for completeness and are **not interpretable** here — with
  several proxies tried post-hoc on the hypothesis-generating data, no p means what it says.
- **Same corpus, same panel, same task.** Recovery is the s186 mean raw soundness; nothing fresh is
  introduced. Every s186 fence still binds (`internal-contrast-only`, nouns-only, proxy control
  corpus, descriptive-only residual arm).

Read the table below as *which proxy is worth freezing for a real test*, never as *which proxy
predicts recovery*.

## What was computed (reproducible; WordNet + s186 outputs only)

**Recovery** (the target ranking): per-relation **mean raw soundness 𝒮** across the three s186 model
slots, read from the committed `results.json` (`raw_soundness`). This is the exact recovery quantity
the essay's clause 2 uses. Values (mean A/B/C):

| relation | recovery 𝒮 (mean) | cited s186 range |
|---|---|---|
| hypernymy | 0.373 | 0.36–0.39 (best) |
| antonymy | 0.314 | ≈0.32 |
| hyponymy | 0.242 | ≈0.24 |
| synonymy | 0.241 | ≈0.24 |
| holonymy | 0.154 | ≈0.15 |
| meronymy | 0.145 | 0.12–0.18 (worst) |

This reproduces the essay's stated ordering exactly (hypernymy > antonymy > synonymy ≈ hyponymy >
holonymy ≈ meronymy), and it is rank-stable across all three models (per-model checks below).

**Proxies** (WordNet structural statistics over each relation's **130 s186 cues**, from `items.json`).
For each cue lemma I take its **first WordNet noun synset** (`wn.synsets(cue, pos='n')[0]`, the
most-frequent-sense convention) — a deliberately **gold-independent** cue-centrality choice, so a
proxy is a property of the *cue*, not a restatement of the answer set — then average over the 130
cues. All 130 cues in every relation resolve to a noun synset (**0 skipped**, 6/6 relations). Four
a-priori candidates, each named by the essay's reasoning:

- **IS-A path depth** — `synset.min_depth()`, the shortest hypernym-path length from the root
  (deeper = more specific). Operationalizes the essay's *"IS-A centrality, position in the WordNet
  hierarchy."*
- **Hypernym-tree connectivity** — subtree size = number of distinct descendants in the transitive
  hyponym closure, `len(set(synset.closure(lambda s: s.hyponyms())))`. Operationalizes the essay's
  *"hypernym-tree connectivity."* (Heavy-tailed; reported as a raw mean.)
- **Definitional / gloss length** — token count of the synset definition, `len(synset.definition().split())`.
  A **cheap WordNet stand-in** for the essay's *"definitional-frame statistic"* — see the honesty note
  below: it is **not** the theorized construct.
- **Polysemy** — number of noun senses of the lemma, `len(wn.synsets(cue, pos='n'))`. A weak
  lexical-centrality candidate, included as a fourth exploratory proxy.

**Baseline (known-fails):** **bare gold fan-out** = mean WordNet gold-set size per relation, recomputed
from `items.json`. Reproduces the s186 gold sizes (antonymy 1.05, synonymy 2.99, hypernymy 14.09,
hyponymy 23.96, holonymy 2.79, meronymy 4.31 ≈ the result page's 1.1 / 3.0 / 14.1 / 24.0 / 2.8 / 4.3).

**Sanity check:** cue-strength (frame-G² control soundness) vs recovery, to confirm the recovery
vector matches s186's decoupling. The s186 tie-naive pipeline value **−0.086** reproduces **exactly**
(slot A raw vs cue-strength); my tie-corrected `scipy.stats.spearmanr` gives **−0.116** vs mean
recovery. The ~0.03 gap is purely tie-handling (synonymy/hyponymy tie in both cue-strength and
recovery); **−0.086 is the authoritative s186 figure** and both are near-zero, as the essay reports.

## Exploratory results (n = 6 relations; scipy tie-corrected Spearman vs mean recovery)

| proxy (a priori candidate) | direction observed | ρ vs recovery | p (uninterpretable, n=6) | out-predicts cue-strength? |
|---|---|---:|---:|---|
| **IS-A path depth** (min_depth) | shallower/more-general → higher recovery | **−0.600** | 0.208 | yes (0.60 > 0.12) |
| definitional / gloss length | shorter gloss → higher recovery | **−0.829** | 0.042 | yes (0.83 > 0.12) |
| polysemy (# noun senses) | fewer senses → higher recovery | **−0.486** | 0.329 | yes (0.49 > 0.12) |
| hypernym-tree connectivity (subtree) | (near-flat) | **−0.143** | 0.787 | no (≈ baseline) |
| **gold fan-out** (BASELINE, known-fails) | (near-flat) | **+0.143** | 0.787 | no |
| cue-strength (frame-G², SANITY) | (near-flat) | −0.116 (s186: −0.086) | 0.827 | — |

Per-model stability (sign-stable 3/3): IS-A depth −0.60 / −0.60 / −0.64; gloss −0.83 / −0.83 / −0.93;
subtree −0.14 / −0.14 / −0.32; polysemy −0.49 / −0.49 / −0.61.

**Readings (all exploratory, none a finding):**

1. **Gold fan-out fails, as the essay said.** ρ = +0.143 (near-zero, faintly *positive*) — hyponymy
   carries the largest fan-out (24.0) at only middling recovery, antonymy the smallest (1.05) at
   second-best. The crude proxy is confirmed useless here; whatever the future test freezes, it is
   **not** fan-out.
2. **The IS-A family *splits*.** Path **depth** correlates moderately (−0.60: relations whose cues sit
   *higher/more superordinate* in the hierarchy are better recovered — antonymy shallowest at 6.08 and
   near-top of recovery, meronymy deepest at 7.55 and bottom), but raw subtree **connectivity** does
   **not** (−0.14, indistinguishable from the fan-out baseline and heavy-tailed). So of the essay's two
   IS-A candidates, *depth* is the promising, well-behaved one and raw *connectivity* is not.
3. **Gloss length tops the table — and this is exactly the trap.** At −0.83 it is the strongest
   exploratory correlate (the only one with p < 0.05). **It is deliberately NOT pre-registered** (next
   section): pre-registering the top correlate over the hypothesis-generating data is the fishing move
   this note exists to refuse, and gloss length is in any case a cheap WordNet echo, not the essay's
   theorized definitional-frame construct.

## The pre-registration (exactly one proxy; provisional; principled, not fished)

**Frozen proxy specification for the future fresh H1+H2 relation-recovery probe:**

> **IS-A path depth.** For each relation's cue set, take each cue's first WordNet noun synset
> (`wn.synsets(cue, pos='n')[0]`), compute its `min_depth()` (shortest hypernym-path length from the
> WordNet root), and average over the cues → the relation's **mean IS-A depth**. On the fresh test,
> correlate the relations' mean IS-A depth against recovery rank (Spearman). **Predicted sign:
> negative** — more-superordinate (shallower) cue sets recover better — with **H2 winning only if
> |ρ(depth, recovery)| is clearly greater than |ρ(cue-strength, recovery)|** and in the predicted
> direction, ≥2/3 models.

**Why IS-A depth, on principle (and explicitly not because it topped — it did not):**

- **It names the essay's construct most directly.** The essay's a-priori candidate is *"IS-A
  centrality, position in the WordNet hierarchy"*; `min_depth` is the single most standard, most
  reproducible operationalization of position-in-the-hierarchy.
- **Fewest free parameters; well-behaved.** It is one WordNet primitive — no heavy tail (unlike
  subtree connectivity), no tokenization/definitional-style choices (unlike gloss length), no
  answer-set coupling (unlike fan-out). It is a property of the **cue**, not the gold.
- **The predicted sign is theory-set, not pilot-set.** The negative direction follows from the
  essay's reasoning (the hypernym is the genus a definition "names first"; part-whole relations "sit
  at the periphery" and are the deepest, most specific cues). The pilot's −0.60 is *consistent* with
  that a-priori direction but did not choose it.
- **It out-predicts cue-strength in the pilot without being the maximum.** IS-A depth (−0.60) clears
  the cue-strength baseline (−0.12) by a wide margin yet sits **below** gloss length (−0.83). Choosing
  the second-strongest correlate on principle, over the strongest, is the anti-fishing discipline made
  concrete: had gloss length been chosen, the choice would have been driven by the exploratory maximum
  on circular data, which is precisely forbidden.

**Honesty note on the definitional-frame arm (deferred, not fished away).** The essay's *"definitional-frame
statistic"* candidate properly means **corpus** Hearst-style hypernym frames ("X such as Y", "Y and
other X") and genus-naming templates — a statistic requiring a corpus, which $0 WordNet cannot supply.
WordNet **gloss length** is only a cheap echo of it, and its topping the pilot table is not evidence
for the theorized construct. The proper corpus definitional-frame proxy is **legitimate future work**:
the fresh H1+H2 design may pre-register it as a **second** proxy arm (H2 is satisfied if *any*
pre-registered taxonomic/definitional proxy out-predicts cue-strength), but its specification must be
frozen against fresh data by that design, not lifted from this circular pass.

**Provisional status.** This pre-registration is **not ratified**. It is a design input that a future
relation-recovery design must carry through its own **pre-run critic** (with the non-Anthropic panel
vote, PROTOCOL §A3) and, if it becomes a resolved operationalization, a **cross-session adversarial
ratification** (PROTOCOL §2). A later session may substitute a sibling IS-A-family statistic (e.g. a
depth normalization, or a properly-specified corpus definitional-frame proxy) **with written argument**;
absent that, IS-A path depth is the default frozen proxy.

## What this note licenses / does not license

**Licenses:** a reproducible, in-repo record that (i) bare gold fan-out is re-confirmed as a
non-predictor of s186 recovery (ρ ≈ +0.14), (ii) among the essay's named taxonomic candidates, IS-A
path *depth* is exploratorily promising and raw subtree *connectivity* is not, and (iii) IS-A path
depth is pre-registered — provisionally — as the future probe's default proxy specification.

**Does NOT license:**

- **Firing, confirming, weakening, or partially discharging H2.** H2 remains **open** and is
  dischargeable only by a **fresh** test with a pre-registered proxy. This note changes no bet's
  status.
- **Any statement that taxonomic structure predicts recovery.** The correlations are exploratory,
  circular (same n = 6 that generated the hypothesis), and not significance-testable at n = 6.
- **Any human comparison.** Nothing here compares a model to a person; the proxies are WordNet
  structure and the recovery is the s186 `internal-contrast-only` within-instrument contrast.
- **Any move beyond nouns, or beyond the s186 setting.** Nouns only (WordNet's taxonomic relations
  are noun-only); the s186 proxy-corpus and descriptive-only-residual fences still bind.
- **Sole support for a claim.** As a `note`, this page is never cited as sole support for a claim
  ([`CLAUDE.md`](../../../CLAUDE.md)).

## Provenance / reproducibility

- **Recovery + cue-strength + gold sizes:** committed `results.json` / `items.json` under
  [`experiments/runs/2026-07-06-antonymy-shadow-saturation/`](../../../experiments/runs/2026-07-06-antonymy-shadow-saturation/), the s186 run behind
  [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md).
- **Proxies:** WordNet 3.0 via NLTK (`wn.synsets(...)[0]`, `min_depth`, hyponym `closure`,
  `definition`), computed over the 130 cues per relation in `items.json`; every value in the tables
  above is reproducible from those two inputs plus a standard WordNet install. No API call, **$0**.
- **Cited figures** (at the source's stated strength): the s186 cue-strength–recovery Spearman
  **−0.086** (3/3), the gold sizes (antonymy 1.1 … hyponymy 24.0), and the recovery ranges all from
  [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md);
  the H2 clause and the "not bare gold fan-out" constraint from
  [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md) and its
  [`predictions.md`](../../predictions.md) §B row.
- **Bears on** the "saturated corner" line of [`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md)
  only as method scaffolding for a future probe; it moves nothing on that page.
