# PREREG — BLiMP R1 C4-FREQUENCY-MATCHED content-word-swap arm (A3b, s232; the s210 SWAP-INCONCLUSIVE successor)

**Frozen s232, before any model call. RUN DEFERRED** to a full-$5 UTC day (s232 landed on the tight
2026-07-15 UTC day, ~$1.81 headroom; the ~$1.3–1.6 run does not fit alongside a freeze vote — the s228→s229
precedent). **Ratified s232** (autonomous cross-session adversarial review + one non-Anthropic decorrelation
vote): **ADOPT-WITH-MODIFICATION — Q1-A DUAL-BAND / Q2-A / Q3-A**, subject to freeze BLOCKERs **B1–B4** +
SHOULD-FIX **S5–S8**, all honored below
([`decisions/resolved/blimp-c4-matched-swap-arm-design`](../../../wiki/decisions/resolved/blimp-c4-matched-swap-arm-design.md);
design [`design/blimp-c4-matched-swap-arm-v1`](../../designs/blimp-c4-matched-swap-arm-v1.md); review
[`REVIEW-ratify-s232.md`](REVIEW-ratify-s232.md) + vote [`VOTE-ratify-s232.json`](VOTE-ratify-s232.json)).
This document + `build_swap_c4.py` + `build_disjoint_sample.py` + `analyze_swap_c4.py` + `probe.py` are the
frozen recipe; the C4-banded swap-build is **independently reproduced by a fresh-agent verifier from this
recipe before any item is scored** (G5-plus). Because the C4-matched swapped-condition accuracies are
**unknown at freeze** (novel words; ORIGINAL re-run fresh on a **disjoint** sample), the arm carries **no
known-accuracy exposure**; its only DoF is the build, fenced here.

## Question (does NOT re-open the ratified C8 gates)

The s210 content-word-swap arm ([`result/blimp-swap-arm-v1`](../../../wiki/findings/results/blimp-swap-arm-v1.md))
returned **SWAP-INCONCLUSIVE**: the load-bearing **deep-scope** stratum dropped 3/3 under a SUBTLEX-matched
swap (Δ̄acc −0.095 / −0.057 / −0.072, all CIs exclude 0), but the drop is **confounded** by a **+0.204 C4
pretraining-frequency gap** (originals' mean unigram log-freq 2.817 vs swap set 2.614 over 3M C4 sentences;
swap words ~1.6× rarer, 2.3% never occur). So the deep drop is **neither** SWAP-STABLE **nor** clean
exact-string memorization. This arm closes that confound by matching the swap words on the **C4
pretraining proxy** too, and re-runs the deep (+ shallow-anchor) stratum. **It does not re-open** the
ratified C8 gates (Q1-C both-arms / G8 / covariate-and-swap-required, resolved s208/s210); the **measurement
instrument is inherited byte-frozen from s210** — the only new operationalization is the C4-frequency-match.

## Panel & elicitation (the s205 instrument, carried verbatim)

Panel = the three [`config/models.md`](../../../config/models.md) slots (`panel.A/.B/.C`), temperature 0,
zero-shot, single-turn, **both presentation orders** per pair, `google/*` reasoning suppressed. The exact
s205 forced-choice prompt (frozen in `probe.py`, **byte-identical to the s210 probe.py except the items
filename** `items_swap.json`→`items_swap_c4.json`): *"Which of these two sentences is the more grammatically
acceptable sentence of standard written English? … Answer with ONLY the single digit 1 or 2."* `usage.cost`
via [`experiments/lib/openrouter.py`](../../lib/openrouter.py). `ABORT_USD = 1.60` per model (the s210 value).

## Q1-A (THE CRUX) — the DUAL-BAND C4-frequency-matching op (all numbers PINNED, BLIND, pre-committed)

Each substitute for a swapped open-class position (common noun / proper name / attributive adjective — the
frame-safe categories; verbs + adverbs held fixed) must be **novel**, POS/morphology-preserving (the s210
recipe, byte-identical), **and** in-band on **both** frequency channels of the original **FORM**:

- **SUBTLEX band** `BAND = 0.10` — |Lg10WF(sub) − Lg10WF(orig)| ≤ 0.10 (the s210 human-frequency band, kept).
- **C4 band** `C4_BAND = 0.30` — |c4log(sub) − c4log(orig)| ≤ 0.30, where `c4log(w) = log10(count_w + 1)`
  over the pinned C4 stream. The eligible pool per position is the **INTERSECTION** of the two bands;
  selection is seeded-deterministic (per-position item-hash; **no free seed** — see B2).

**B1 (BLOCKER — one BLIND switch, not two floating knobs).** The C4 half-width is **fixed at a single value
0.30** (not chosen after seeing feasibility), and the pool-adequacy switch is a single pre-committed rule:
- `POOL_FLOOR = 5` — a position whose intersection has **< 5** candidates is **DROPPED-AND-LOGGED** (the
  position is not swapped; if that leaves a pair with 0 swaps or fails re-validation the pair drops per the
  s210 Q3-A rules). Never band-widened.
- `TRIGGER_FRAC = 0.25` — the **Q1-A→Q1-B fallback**: if **> 25%** of swap-eligible positions across the
  whole build are dropped for a below-floor/empty intersection, the entire build re-runs under **Q1-B**
  (C4-primary: C4 band only, SUBTLEX reported not bound). This is a **frequency-only, accuracy-blind**
  criterion computed at build time (`build_swap_c4.py:main`), pinned before any model call. The half-width,
  floor, and trigger are all fixed constants — no post-hoc widening or dual-vs-primary re-selection.

**B2 (BLOCKER — anti-seed-shopping).** The **only** RNG seed is `SEED = 20260715` (date-derived, pre-announced),
used solely by `build_disjoint_sample.py` to draw the disjoint subsample. **Substitute selection is
seed-FREE**: `pick_c4` seeds each position's shuffle from `sha256(f"{uid}|{pid}|{i}|…")` — fully determined
by item identity, so there is **no global seed to scan** and no output-selecting seed. PREREG **forbids seed
scanning**; the fresh-agent run verifier attests the pinned seed + the committed recipe reproduce the
committed lexicon exactly and that **no seed selection occurred**. Output-sha pinning alone is insufficient;
the seed itself is pinned and pre-announced.

**S5 (SHOULD-FIX — single pinned C4 stream scale).** `C4_NUM_SHARDS = 3` → ~**22.3M** C4 sentences (the s208
covariate-arm scale), **not** the 3M diagnostic prefix — quantization at 3M bit exactly the rare deep-scope
words that drove the +0.204 gap (2.3% never occurred). The band **and** the G-C4-match-adequacy report are
computed at this **same** scale (via the import-pinned s208/s210 `build_cooc_c4.py:stream_sentences` adapter;
no new corpus adoption; ODC-BY, [`resource/cooccurrence-corpus-scouting`](../../../wiki/base/resources/cooccurrence-corpus-scouting.md)).

## Q2-A — scope (both strata) + the DISJOINT fresh ORIGINAL baseline

- **6 s210 frame-safe paradigms, both strata** (selection **inherited byte-frozen** from s210, not re-run):
  shallow `determiner_noun_agreement_2/_1`, `regular_plural_subject_verb_agreement_1`; deep
  `sentential_negation_npi_scope`, `only_npi_scope`, `superlative_quantifiers_1`. The **deep-3 carry the
  load-bearing test**; the near-ceiling **shallow-3 are the destructive-control anchor** (a shallow drop
  under C4-matching flags a broken build, not memorization).
- **G-disjoint — the sample is DISJOINT from s210 BY CONSTRUCTION.** `build_disjoint_sample.py` draws
  `SAMPLE_N = 160` pairs/paradigm (**S7**: 130→160 headroom so dual-band attrition still reaches
  `TARGET_N = 100` usable) from `(paradigm pairs MINUS the s210 kept pair ids)` under `SEED = 20260715`;
  the draw is asserted disjoint from the s210 kept ids and the 6 paradigm files are sha-verified against the
  s210 pins. **Certified at freeze** ([`disjoint_sample.json`](disjoint_sample.json), sample_sha256
  `1f90050c947f07ba62c09412d2c1c8e630fe2f484a85fda3da3966b8dc7da4e7`; all 6 paradigms **0 overlap** with
  s210); independently re-verified by the run verifier. **ORIGINAL re-run fresh in-session** alongside the
  new C4-matched SWAP → `Δacc = acc_swap − acc_orig` is a **within-run paired** quantity with **no
  known-accuracy exposure** on either condition (the s210 ORIGINAL accuracies are **not** reused).
- **G-power / S1 attrition (S7, PINNED before build).** `USABLE_FLOOR = 60` usable pairs/paradigm. If a
  **deep** paradigm falls below the floor after dual-band attrition it is **dropped**; if **≥2** deep
  paradigms remain → re-verdict on **deep-2**; if **< 2** remain → **ATTRITION-INCONCLUSIVE** (pre-registered,
  never a post-hoc choice). TOST equivalence power is stated at the achieved post-attrition usable-N per deep
  paradigm; the dual-band intersection thins the pool, so a true-stable effect that widens the CI lands the
  conservative, non-promoting STILL-INCONCLUSIVE, not a false STABLE.

## Q3-A — the FOUR-OUTCOME disambiguation map (blind-scoring locked) + bounded, cross-session candidacy

Read on the C4-matched **deep** stratum (inherited G-metric; the adequacy gate FIRST). Bands are **identical**
for the refusing and the candidacy poles (the anti-cheat symmetry).

- **G-C4-match-adequacy FIRST (B3, BLOCKER).** From the frozen build (blind, build-time, pre-model-call):
  `g_C4 = mean over all subs of (c4log(orig) − c4log(swap))`, at the 22.3M scale. If **|g_C4| > 0.05**
  (`MAX_SETMEAN_C4_GAP`, an **exact** threshold — the `~` is dropped) → **STILL-INCONCLUSIVE-BY-MATCH-FAILURE**:
  the +0.204 confound was **not demonstrably closed**, so **no DROPS/STABLE verdict is read**.
- **DEEP-STILL-DROPS** — the **whole** deep Δ̄ CI ≤ −0.05 (Δ̄ ≤ −0.05 **and** the CI upper bound ≤ −0.05, the byte-frozen s210 rule) on ≥2/3 → a **cleaner exact-string / lexical-item
  memorization** signal (survives **both** frequency controls); R1 refused promotion **more firmly** (a
  first-class negative).
- **DEEP-SWAP-STABLE** — deep + shallow Δ̄ CI ⊂ [−0.05, +0.05] on ≥2/3 → the s210 drop **was** the C4
  confound; with the s208 **SURVIVES-COVARIATE**, R1 becomes a **bounded promotion-review CANDIDATE**,
  bounded to "not exact-string memorization, not the surface freq proxy, not the pretraining-proxy freq gap"
  — **still not** construction-frequency-controlled (G3′ travels). A later, separate, **cross-session**
  review writes/refuses the `claim`; this run earns candidacy, **never** ratifies.
- **STILL-INCONCLUSIVE** — otherwise (even a two-confound-clean swap did not resolve the deep-scope alignment
  at this N; a candid ceiling).

**B4 (BLOCKER — the blind-scoring lock, hard, fresh-agent WRITTEN attestation).** `analyze_swap_c4.py`'s
scoring code + the exclusion criteria + this four-outcome decision table are frozen **before any re-run**;
the run verifier gives a **written** attestation that **no human-readable intermediate output was inspected
until the whole batch was scored**. This is the load-bearing guard for the known-drop exposure and is a hard
condition on the run, not a convention.

## Metric + verdict bands (G-metric — inherited byte-frozen from the s210 PREREG)

`Δ_pair = acc_swap_pair − acc_orig_pair` (order-averaged per member; orig/swap of the same pairID paired);
per model, per stratum `Δ̄ = mean Δ_pair`; percentile bootstrap CI (`BOOT = 5000`, `SEED = 20260715`).
**Equivalence** = CI ⊂ [−0.05, +0.05] both strata ≥2/3; **drop** = the whole deep Δ̄ CI ≤ −0.05 (Δ̄ ≤ −0.05 **and** CI-upper ≤ −0.05, byte-frozen from s210 — stricter than 'CI excludes 0'), ≥2/3. The
±0.05 margin's justification (matches the s205 `DEPTH_MARGIN`) is inherited byte-frozen.

## G-coverage (inherited) + S6 per-word C4 report

`G-coverage` floor **0.50** — a paradigm below it is flagged weak and **EXCLUDED** from the stratum verdict
(the dual-band swap lowers coverage vs s210; this floor is the pre-committed retained-position gate the
ratifier + vote asked for, alongside `USABLE_FLOOR`). **S6 (per-word adequacy report + soft check):**
`analyze_swap_c4.py` reports the per-word signed C4 gap distribution and the fraction within a tighter
`PERWORD_C4_TIGHT = 0.15` band, and raises a **`directional_cancellation_flag`** if a small set-mean hides
large within-band per-word gaps of both signs (|set-mean| ≤ 0.05 **and** per-word mean|gap| > 0.10 **and**
min(frac_swap_rarer, frac_swap_commoner) > 0.30) — so a set-mean ≤ 0.05 achieved by directional cancellation
is **visible**, not hidden.

## Diagnostics (inherited)

- **INSTRUMENT-FAILURE guard (s205, verbatim):** poslock rate > 0.50 AND |ans1_rate − 0.5| > 0.40 on ≥2/3 →
  the 2AFC collapsed to position-answering → readings voided (reported, not silently dropped).
- **G-freq (achieved SUBTLEX match):** the per-word `Lg10WF` gap distribution of orig→swap substitutes
  (≤0.10 by construction; reported).

## Anti-cheat fence (LOAD-BEARING — the s210 deep drop is KNOWN at design time)

(1) The C4-matched condition's accuracies are **unknown at freeze** (novel words; ORIGINAL re-run fresh on a
**disjoint** sample) — no accuracy in Δacc is known when the recipe is frozen; the C4 band is a mechanical
frequency criterion, not an accuracy target. (2) The verdict map is **symmetric** — DROPS (refuse) and STABLE
(candidacy) carry identical ±0.05 bands; the successor motivation (s210 scope-cap #4) leans toward the
**refusing** pole (S8 — kept visible: a promotion-seeker would be betting **against** the known prior drop),
and the fresh-agent freeze critic confirms the framing is an even-handed disambiguation, not a
promotion-seeking retune. (3) Build-only DoF, **verifier-reproduced before scoring** (G5-plus), the
**seed pinned + pre-announced** (B2), and the **blind-scoring lock** (B4). Result-motivation check at
ratification: **NONE**.

## Pre-named outcomes (symmetric — the anti-cheat guarantee)

DEEP-STILL-DROPS (first-class negative), DEEP-SWAP-STABLE (bounded cross-session candidacy),
STILL-INCONCLUSIVE, STILL-INCONCLUSIVE-BY-MATCH-FAILURE (B3), ATTRITION-INCONCLUSIVE (S7), an
INSTRUMENT-FAILURE void, a coverage-floor exclusion, and a Q1-A→Q1-B fallback (B1) are **all pre-registered**.
`predictions.md` bet registered at this freeze, no outcome pre-filled.

## Freeze-gate dispositions (freeze critic + freeze vote, s232)

The independent fresh-agent **freeze critic** (verdict authority) returned **GO-WITH-CONDITIONS**
([`REVIEW-freeze-s232.md`](REVIEW-freeze-s232.md)) — B1/B2/B3/B4 all PASS, no promotion-seeking retune — with
one BLOCKER + four SHOULD-FIX; the non-Anthropic **freeze vote** (`gpt-5.4-mini`,
[`VOTE-freeze-s232.json`](VOTE-freeze-s232.json), **$0.004198**) also **GO-WITH-CONDITIONS**, convergent.
Disposition:

- **F1 (BLOCKER — a real bug, FIXED at freeze).** `analyze_swap_c4.py:stratum_deltas` used `uid not in keep`
  (dead code — `keep` is keyed by every uid), so a below-`USABLE_FLOOR` paradigm was never excluded from the
  pooled stratum Δ̄. Changed to `not keep[uid]` this session, making the code match the already-ratified S7
  attrition rule (no re-ratification; the critic confirmed it is symmetric across drops/stable, not
  promotion-seeking).
- **F2 (SHOULD-FIX — DONE at freeze).** `build_swap_c4.py:main` now computes + prints the B3 adequacy
  set-mean `g_C4` at **build time** (blind, no accuracy) with a `<<< DO NOT SPEND >>>` warning on
  MATCH-FAILURE, so an inadequate match aborts **before** the ~$1.3–1.6 probe spend.
- **F3 (SHOULD-FIX — DONE at freeze).** The PREREG + analyzer prose "CI excluding 0" is reconciled to the
  operative byte-frozen s210 rule: **drop = the whole deep Δ̄ CI ≤ −0.05** (Δ̄ ≤ −0.05 AND CI-upper ≤ −0.05),
  which is *stricter* than "CI excludes 0" (conservative; harder to declare the negative).
- **F4 (SHOULD-FIX — noted).** The det-noun carve-out C4-band-matches on the *plural* form but records/places
  the singular, so its recorded adequacy gap is on a form pair it did not band-filter. Affects only the
  shallow det-noun **control** stratum; blind + symmetric; if anything makes the adequacy gate *harder* to
  pass. The run verifier records this as a known conservative quirk.
- **F5 (SHOULD-FIX — run-verifier attestation).** `instr_fail` is reported as a flag, not injected into the
  verdict string (inherited from s210). The run verifier's written attestation must state explicitly that a
  fired INSTRUMENT-FAILURE flag **voids** the accuracy read.
- **FV1 (freeze vote — RUN condition).** The Q1-A→Q1-B fallback is a **single irrevocable auto-branch** inside
  one `build_swap_c4.py` invocation (no manual re-run, no alternate fallback path); the run operator does not
  re-run the build after seeing the dropped-position rate.
- **FV2 (freeze vote — RUN condition).** Before any scoring, the committed **lexicon sha + the
  dropped-position log + the fallback (mode) decision** are frozen as a single immutable artifact bundle
  (`selection_c4.json` + `items_swap_c4.json`), verifier-attested — no after-the-fact narrative smoothing.
- **S6 stays a REPORT, not a gate** (both the ratifier's per-word check and both votes concur): the per-word
  directional-cancellation flag is a visibility/caution flag; making it a hard gate would over-constrain and
  reintroduce discretion. The hard adequacy gate stays the signed set-mean (B3).

## Instrument-line governor (recorded)

This is the **second** swap-type arm on R1 (s210 SUBTLEX-matched → this C4-matched); **not** yet at the
PROTOCOL §3 instrument-stopping threshold (3 null-yielding redesigns; and s208 SURVIVED, so no null streak).
A **third** swap redesign (e.g. the s210-named verb-swap-with-valence-guard arm) would trip the governor and
require a cross-session line-continuation review before it runs.

## Scope caps (carry into any citation)

1. Controls **R1 only**, and the exact-string memorization sub-confound **net of both** the human-frequency
   (s210) and the pretraining-proxy-frequency (this arm) channels; does **not** control **construction**
   frequency or template difficulty (G3′), does not touch R2/R2h.
2. **C4 is a proxy** for pretraining, not the panel's true training distribution; "C4-frequency-matched" =
   "matched on a public web-text proxy," never "matched on true training frequency." A residual per-word C4
   gap within the band is reported.
3. SWAP-STABLE = "not driven by memorizing the exact BLiMP strings (net of both frequency proxies)," **never**
   "grammatical competence"; absolute accuracy stays a contamination upper bound.
4. Deep-pole generality cost (scope-deep covered, island-deep not); perturbation bound (nouns/names/adjs only).
5. n = 3 models; per-model, per-stratum Δ, never pooled.

## Cost (pre-flight — from OBSERVED s210 economics; NOT a low pre-flight)

**RUN (deferred):** 6 × ~100 pairs × 2 conditions × 2 orders × 3 models = **7,200 calls ≈ $1.3–1.6** (the
s210 arm ran 7,200 calls billed ~$1.34). Fits a full-$5 UTC day as the day's main run. The C4 pre-build
stream is **$0 model cost** (build compute + network only). **This freeze session (s232):** $0 model cost +
two decorrelation votes (ratify + freeze, `gpt-5.4-mini`, ~$0.004–0.006 each), trivially under the ~$1.81
UTC-2026-07-15 headroom; the RUN is deferred to the next full-$5 UTC day.
