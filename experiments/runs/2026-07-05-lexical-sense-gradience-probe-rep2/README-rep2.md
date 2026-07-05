# Run record — lexical-sense-gradience probe REP2 (the owed A2a cross-date fresh-item replication)

**Date:** 2026-07-05 (session 181)
**Design (frozen, unchanged):** [`design/lexical-sense-gradience-v1`](../../designs/lexical-sense-gradience-v1.md)
**Governing decisions (RESOLVED, unchanged):** [`decisions/resolved/lexical-sense-gradience-operationalization`](../../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md) · [`decisions/resolved/lexical-sense-gradience-anchor`](../../../wiki/decisions/resolved/lexical-sense-gradience-anchor.md)
**Conjecture probed:** [`conjecture/lexical-sense-gradience`](../../../wiki/findings/conjectures/lexical-sense-gradience.md) (clauses a + c)
**Anchor:** [`resource/dwug-usage-graphs`](../../../wiki/base/resources/dwug-usage-graphs.md) (DWUG EN v3.0.0, Zenodo 14028531, CC BY-ND 4.0)
**v1 run:** [`2026-05-30-lexical-sense-gradience-probe-v1`](../2026-05-30-lexical-sense-gradience-probe-v1/) → [`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)
**Promotes/strengthens:** [`claim/lexical-sense-gradience`](../../../wiki/findings/claims/lexical-sense-gradience.md) (`supported`, single-run-flagged — this run is the flagged strengthening it names)

## Why this run (A2a; PROTOCOL §4; program item A2a)

[`claim/lexical-sense-gradience`](../../../wiki/findings/claims/lexical-sense-gradience.md) is the
project's lexical shadow-beater, promoted s176 at **direction/agreement** scope with its
**magnitudes explicitly flagged single-run** — its specific instrument-and-control combination
(graded ρ vs the DURel median with the model-internal topic partial) had run exactly **once**
(2026-05-30, one temperature-0 draw). It was the **only remaining flagship positive without a
cross-date replication** (CC done s169, dative s175, AANN gradient s178). This run is the owed
A2a powered re-run: the **byte-frozen v1 instrument** on **200 fresh DWUG pairs drawn disjoint
from v1**, on a fresh date, to lift the single-run flag and (if it replicates) license a
full-scope, magnitude-bearing edition.

## What is frozen and what changed (the ONLY differences from v1)

The instrument is **byte-identical to v1** — verified by sha256:

| file | sha256 | identical to v1? |
|---|---|---|
| `probe.py`   | `e5eebabec7490eb1297cf68276d3c69b6b67bdaea8824c0b0ab61ddc52a5e0cf` | **yes** |
| `analyze.py` | `60c127980863ce1192b3b420b608ecac5bbf987b31e0b783d74a718938c40266` | **yes** |

The build recipe `build_items_rep2.py` differs from v1's `build_items.py` in **exactly three
mechanical ways, none touching the design**:

1. **SEED** `20260530` → `20260705` (a fresh draw, fresh date).
2. **v1-exclusion:** every pair frozen in the v1 manifest (`{id1,id2}`, 200 pairs over 373
   distinct usages) is removed from the candidate pool **before sampling** → the rep2 set is
   **disjoint from v1 at the pair level** (asserted in-script; independently re-verified: **0
   shared pairs**).
3. new output paths (this run dir + a rep2-specific gitignored full-text file), so v1's frozen
   files are never touched.

Everything else — the Q4 within-period filter, the ≥2-judgment requirement, `N_PER_LEVEL=50`,
`PER_LEMMA_LEVEL_CAP=4`, the B1 span-recovery fix, the B2 span-sanity gate, the overlap
covariate, the STOP list, the three framings (`durel`/`cont`/`topic`), the manifest schema, the
report-the-correlation reading rule — is **byte-identical** to v1.

## The frozen rep2 item set

- **DWUG archive sha256** `64eef477154b82cb27925ab4ea8c030a8e23840b538dd06b6464aa1e55af2dbf`
  — **identical to the v1 freeze** (same Zenodo source, verified pre-run; the script `assert`s it).
- **Manifest freeze sha256 (rep2)** `9b6b66bd9465e9c83a1e76d92a233d55fe326a6c65440320c71047cfbdb3cb24`
  (v1 was `7b4ad11f…`).
- **200 pairs, balanced 50 per rounded-median DURel level 1–4**, across **41 lemmas** (v1: 43),
  within-period only, each pair with ≥2 annotator judgments (median = human gold). Candidate
  pool after v1-exclusion is large at every level (919 / 3126 / 1056 / 3366), so the disjoint
  draw is unforced.
- Human-median distribution (rep2): 1.0 ×50 · 1.5 ×17 · 2.0 ×20 · 2.5 ×13 · 3.0 ×50 · 3.5 ×8 ·
  4.0 ×42. **n≥3-annotator subset: 64/200** (v1: 49/200 — a slightly *more* reliable gold this
  draw; `analyze.py` reports the n≥3 subset ρ as the S3 robustness check either way).

### Disjointness — the honest scope (pair-level, not usage-level)

The **probed item is a PAIR of usages**, and **0 rep2 pairs appear in v1** (asserted + verified).
DWUG's corpus is a **finite inventory of uses per lemma**, so a single usage can recombine into a
*different* fresh pair: **61/357** rep2 usages also appear in *some* v1 pair. This is disjointness
at the unit of analysis (the pair) but **not** at the usage level — weaker than the AANN rep2's
"0 shared surface items" (AANN *generates* items; DWUG cannot). It is stated here and on the
result page so the replication's scope is not overclaimed: **fresh pairs, partially recombined
usages, same finite corpus, same frozen instrument, fresh date.**

## Data / licence handling (unchanged from v1)

DWUG EN is CC BY-ND 4.0 over copyrighted CCOHA text. This run does **not** commit the archive or
the corpus sentences: `experiments/data/dwug/` is gitignored; `build_items_rep2.py` re-downloads
DWUG from Zenodo (URL + archive sha256 pinned + asserted) and regenerates the item set from the
fixed seed + frozen filters. Committed: the recipe, the manifest (pointers + human DURel gold +
overlap covariate; **no corpus text**), and raw JSON of model outputs + gold (**no corpus
sentences**).

## Pre-registration / no-retuning

- Seed, filters, balance, cap, all three framings, both controls, and the v1-exclusion rule
  fixed **before any model call**. Manifest frozen + committed (sha above) **before** the probe.
- **Instrument byte-frozen** (sha-verified table above) — no post-hoc code change.
- Reading rule: `analyze.py`'s report-the-correlation (Spearman ρ per model per framing with
  bootstrap 95% CI; partial ρ | overlap and | topic; per-human-level means; ρ(sense,topic)).
  **No threshold is tuned after the run.**
- Gates run this session: independent fresh-agent **pre-run critic**; one **non-Anthropic
  decorrelation vote** (probe REST path); independent fresh-agent **post-run verifier**
  (recompute from raw).

## Results / cost

*(filled after the run)*
