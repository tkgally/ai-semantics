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

The instrument's **behavioral logic and analysis are byte-frozen from v1**. The pre-run critic
(below) caught that a *fully* byte-identical `probe.py` would read v1's input filename
(`lexical_v1_fulltext.jsonl`) and — because v1 and rep2 both number items `lx-{level}-{idx}` —
could silently join v1 predictions to rep2 gold. The fix (critic's option a) changes **one
constant**: `probe.py`'s `FULLTEXT` path now points at this run's items. sha256:

| file | sha256 | vs v1 |
|---|---|---|
| `probe.py`   | `63a804cbd327ebe0ff570f2e806b2aa34d7e257f8ecd9255753b94dfa79fbf48` | **the single `FULLTEXT` input-path constant** `lexical_v1…`→`lexical_rep2…` (+ an explanatory comment); the three framing system prompts, guillemet item rendering, parsing, temperature-0 panel loop are line-for-line identical (`diff` shows only these lines) |
| `analyze.py` | `60c127980863ce1192b3b420b608ecac5bbf987b31e0b783d74a718938c40266` | **byte-identical** (`diff -q` clean) — the load-bearing statistics (Spearman, partials, bootstrap CI, per-level means) are frozen |

So what is frozen is the **load-bearing part** — every prompt the model sees, the parsing, the
three framings, and all analysis math — and the only `probe.py` change is which frozen item file
it loads. The build recipe `build_items_rep2.py` differs from v1's `build_items.py` in **three
selection-affecting ways, plus one hardening**:

1. **SEED** `20260530` → `20260705` (a fresh draw, fresh date).
2. **v1-exclusion:** every pair frozen in the v1 manifest (`{id1,id2}`, 200 pairs over 373
   distinct usages) is removed from the candidate pool **before sampling** → the rep2 set is
   **disjoint from v1 at the pair level** (asserted in-script; independently re-verified: **0
   shared pairs**).
3. new output paths (this run dir + a rep2-specific gitignored full-text file), so v1's frozen
   files are never touched.
4. *(hardening, does not touch selection)* `ensure_dwug()` now `assert`s the archive sha256
   equals the pinned value (v1 only printed it) — so a wrong-archive download fails loudly.

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
  4.0 ×42. **n≥3-annotator subset: 64/200** (v1: 48/200 — a slightly *more* reliable gold this
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

## Pre-run gates (recorded)

**Independent fresh-agent pre-run critic — verdict NO-GO → fixed → re-verified.** The critic
verified byte-identity of the analysis/prompt logic (`diff` clean), the disjointness (independently
reproduced **0 shared pairs**, 200 pairs, 41 lemmas, 50/50/50/50 balance, the exact median
distribution), the anti-cheat (human gold never enters any prompt), and the cost/power — but caught
one **BLOCKER (B1):** the byte-frozen `probe.py` read v1's input filename, which either crashes
(the v1 fulltext is absent) or, if that file were regenerated, would **silently join v1 predictions
to rep2 gold** (colliding `lx-{level}-{idx}` ids). **Fixed** by pointing `probe.py`'s single
`FULLTEXT` constant at the rep2 items (critic option a; recomputed sha above) and **smoke-tested**
before any spend: the resolved input is `lexical_rep2_fulltext.jsonl` (200 items), its item_ids
**equal** the manifest's (0 mismatch), and a 1-item end-to-end call returned parseable ratings on
all three framings that join to the manifest (smoke cost $0.002004). The critic's interpretation
CONDITIONS are carried to the result/claim: **C1** — disjoint at the pair level but 61/357 usages
recombine, so v1+rep2 are **not** two fully independent draws (no naive pooling/meta-as-independent;
keep the "fresh pairs, recombined usages" framing, never AANN-style "0 shared items"); **C2** — v1's
S1 (near-degenerate overlap control), S2 (model-internal topic partial = modest, not a clean
sense/topic dissociation), S4 (homonymy floor) carry forward unchanged — lifting the single-run flag
licenses only the **direction/agreement** magnitude, not a representational reading; **C3** — the
n≥3 gold is better this draw (64 vs 48) but half-integer levels stay 2-rater, not reliable gold.
Two NITs (v1 n≥3 stated 49, actually 48; "exactly three" build-diff wording) fixed in this README.

**Non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, probe REST path) — GO-WITH-CONDITIONS**
($0.001507 + a truncated first call $0.000860; cutoff-aware preamble). No hard blocker; endorsed
pair-level disjointness as a legitimate replication unit *for a claim about correlations over
pairwise judgments*, while stressing it is weaker than usage-level ("fresh pairs" replication, not
"fully new underlying evidence"); told to keep the pair/usage overlap quantified **in the writeup,
not a footnote**; and to guard against upgrading to a broad model-understanding / general-lexical
reading or implying the re-run resolves more than **cross-date stability of the same instrument**
(it does not address instrument fragility or lemma-specific dependence). All conditions converge with
the critic's and are honored here and on the result page.

## Results / cost

**1800 calls, 0 NA in every arm, 0 missing cost. Total billed $0.68507**
(claude $0.41022 / gpt $0.10133 / gemini $0.17352). **Far below v1's $3.134** — gemini billed
$0.174 here vs $2.606 in v1 (its reasoning-token burn on this instrument is date/item-dependent,
not fixed; v1's spike was an anomaly). Well under the $2.50 single-run flag and the fresh $5/day cap.

**Headline: REPLICATES 3/3.** Spearman ρ(model sense, human DURel median), n=200, v1 → rep2:

| model · framing | v1 ρ (CI) | rep2 ρ (CI) | partial\|topic v1→rep2 |
|---|---|---|---|
| claude · durel | 0.679 (.59–.75) | 0.715 (.642–.777) | 0.52 → 0.604 |
| claude · cont  | 0.696 (.61–.78) | 0.739 (.664–.799) | 0.54 → 0.640 |
| gpt · durel    | 0.601 (.49–.69) | 0.528 (.409–.639) | 0.50 → 0.392 |
| gpt · cont     | 0.675 (.58–.75) | 0.631 (.530–.723) | 0.58 → 0.506 |
| gemini · durel | 0.804 (.75–.85) | 0.808 (.748–.852) | 0.73 → 0.657 |
| gemini · cont  | 0.825 (.76–.87) | 0.801 (.740–.848) | 0.75 → 0.639 |

Every rep2 base ρ falls within v1's CI (all overlap, all clear of zero); the topic partial survives
3/3 both framings. gpt is again the weakest and most elicitation-sensitive corner (ordinal durel
0.528, partial|topic 0.392 — down from v1, still positive/non-collapsing, CI overlaps). Single-run
flag on the direction/agreement claim **discharged**. Full reading:
[`result/lexical-sense-gradience-rep2`](../../../wiki/findings/results/lexical-sense-gradience-rep2.md).
Independently re-verified from raw by a fresh-agent post-run verifier (recompute; verdict recorded on
the landing commit).
