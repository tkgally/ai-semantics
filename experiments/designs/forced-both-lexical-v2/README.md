# forced-both-lexical-v2 — build attempt under the ratified co-activation anchor

This is the **second** build attempt for the discriminating test named by
[`essay/layer-specialness-vs-always-resolvability`](../../../wiki/findings/essays/layer-specialness-vs-always-resolvability.md),
under the resolved gate
[`decisions/resolved/forced-both-lexical-operationalization`](../../../wiki/decisions/resolved/forced-both-lexical-operationalization.md)
**and** the session-93 anchor ruling
[`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../../wiki/decisions/resolved/sense-coactivation-anchor-semeval-puns.md)
(ADOPT DEFAULTS: Q-A adopt the SemEval-2017 Task 7 pun corpus as the **Q4 sense-co-activation**
anchor; **Q-B-1** co-activation does *not* discharge **Q1-ii** no-dominance — a *separate, frozen,
not-model-based dominance step with an argued transfer-to-item* is still owed; **Q-C-1** attested
homographic puns may serve as forced-both stimuli, homonym subset, sha256-frozen).

The session-91 attempt ([`result/forced-both-lexical-build-attempt-v1`](../../../wiki/findings/results/forced-both-lexical-build-attempt-v1.md))
hit the Q1-ii wall two ways: **no power** (only 1/8 candidate words had ≥5 SemCor tags on both
senses) **and** a structural defect (general-usage balance does not transfer to the constructed
sentence's in-item balance). v2 removes the *power* problem and isolates the *transfer* problem.

## What v2 builds (vs v1)

| | v1 (session 91) | v2 (this build) |
|---|---|---|
| forced-both stimuli | 8 **author-built** zeugma frames | **attested** SemEval-2017 homographic puns (Q-C-1), human-certified co-active (Q4 anchor) |
| no-dominance signal | SemCor per-sense tag counts (US corpus) | **eDom** (Maciejewski & Klepousniotou 2016) + **Rodd & Gilbert** spoken norms — human, CC BY 4.0, the [`resource/homonym-meaning-dominance-norms`](../../../wiki/base/resources/homonym-meaning-dominance-norms.md) word-grain dominance |
| power | 1/8 words powered | **43 items / 23 words** balanced in general usage (below) |
| remaining blocker | power **+** transfer | **transfer only** — the question this design puts to the pre-run critic |

## The frozen subset (license-clean, sha256-stamped)

`build_frozen_subset.py` re-fetches the corpus (verifies sha256), applies the frozen homonymy proxy,
intersects the homographic pun-word vocabulary with the two CC BY 4.0 dominance-norm sets, and emits
the balanced-homonym candidate items.

- SemEval archive sha256 `70e82d89…b4f4d0a` — **re-verified this session** (deterministic re-fetch,
  HTTP 200, 748,424 bytes, identical hash).
- homographic subtask-3 total: **1298**; homonym subset (different-lexfile proxy): **1105**;
  homonym items whose word is in a dominance-norm set: **220**;
  **balanced-homonym items: 43** (23 distinct words).
- `frozen_subset.json` sha256 **`a066dfbc…b5c9c9fd`** (see `frozen_subset.sha256`).

**License discipline (binding).** The committed `frozen_subset.json` contains only: item-ids,
pun-word lemmas, WordNet 3.1 sense keys (factual annotations), and CC BY 4.0 dominance values.
**No pun sentence text is committed** — the SemEval data includes a CC BY-NC 4.0 subset, so the joke
text is never mirrored (re-fetch deterministically with the URL + sha256 on the resource page). The
dominance values are CC BY 4.0 (cite Maciejewski & Klepousniotou 2016; Rodd & Gilbert / *J.
Cognition* 10.5334/joc.194).

## The open question this design puts to the pre-run critic

**Is Q-B-1's "argued transfer-to-item dominance step" satisfiable for these 43 items?** i.e. does
*general-usage* word-grain balance (the only buildable not-model-based dominance signal) defensibly
transfer to *in-item* balance for the specific pun sentences — enough that a **commit** verdict could
be certified non-spurious (Q1-ii / Q3.3 higher bar on commit)? See
[`dominance_transfer_analysis.md`](dominance_transfer_analysis.md) for both sides. A fresh
independent pre-run critic rules **GO** (build the Q2-i instrument over the 43 items and run within
budget) or **NO-GO** (trigger (c) again — the fork stays at R1). Per the gate, a NO-GO defers; it
never relaxes a band.

## Reproduce (no API)

```
# 1. re-fetch corpus (verify sha256 70e82d89…b4f4d0a)
curl -L https://alt.qcri.org/semeval2017/task7/data/uploads/semeval2017_task7.tar.xz -o semeval2017_task7.tar.xz
sha256sum semeval2017_task7.tar.xz
mkdir -p semeval && tar -xJf semeval2017_task7.tar.xz -C semeval
# 2. fetch CC BY 4.0 dominance norms
curl -L https://osf.io/download/pmbkm/ -o edom_norms.csv      # eDom Norms File (OSF 7k3eh)
curl -L https://osf.io/download/2mduw/ -o spoken_norms.csv    # Rodd&Gilbert Dominance Norms (OSF uy47w)
# 3. build the frozen subset (emits out/frozen_subset.json; no joke text)
python3 build_frozen_subset.py
```
