---
type: design
id: blimp-c4-matched-swap-arm-v1
title: "BLiMP R1 C4-frequency-matched swap arm (the s210 SWAP-INCONCLUSIVE honest successor) — does the deep-scope drop survive matching the swap words on C4 PRETRAINING-proxy frequency, not just human SUBTLEX frequency? Disambiguates exact-string memorization from a pretraining-rarity confound. DESIGN, not frozen; three gates open"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: draft
anchor: resource/blimp
contingent-on:
  - []
created: 2026-07-15
updated: 2026-07-15
links:
  - rel: refines
    target: result/blimp-swap-arm-v1
  - rel: operationalizes
    target: result/blimp-forced-choice-sweep-v1
  - rel: depends-on
    target: result/blimp-swap-arm-v1
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
  - rel: depends-on
    target: design/blimp-swap-arm-v1
  - rel: depends-on
    target: resource/blimp
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Design v1 — BLiMP R1 C4-frequency-matched swap arm (program A3b; the s210 SWAP-INCONCLUSIVE honest successor)

> **A design + decision-trail unit (s231).** Status: **DESIGN — three operationalization gates open,
> ratifiable s232+.** The instrument is inherited **byte-frozen** from the s210 content-word-swap arm
> ([`design/blimp-swap-arm-v1`](blimp-swap-arm-v1.md); PREREG
> [`experiments/runs/2026-07-11-blimp-swap-arm/`](../runs/2026-07-11-blimp-swap-arm/)); the **only new
> operationalization** is that the swap substitutes are matched to the originals on **C4
> pretraining-proxy log-frequency**, not only on human SUBTLEX-US `Lg10WF`. This closes the one confound the
> s210 result named as load-bearing. Per PROTOCOL §3/§A1 and the A3b/A1b/A5 precedent (design one session,
> ratify the next, run after ratification): **design s231, ratifiable s232+, freeze + run after
> ratification.** A control that opens value-laden operationalization choices is not run in the session that
> opens it.

## The one-line problem this unit exists to solve

The s210 swap arm ([`result/blimp-swap-arm-v1`](../../wiki/findings/results/blimp-swap-arm-v1.md)) returned
**SWAP-INCONCLUSIVE**: replacing the exact BLiMP content words with novel, **SUBTLEX-US-frequency-matched**
(`Lg10WF` ±0.10) same-POS words dropped forced-choice accuracy on the load-bearing **deep-scope** stratum on
all three models (per-model signed Δ̄acc **−0.095 / −0.057 / −0.072**, all CIs exclude 0). But the drop is
**confounded**: over 3,000,000 C4 sentences the originals' mean unigram log-frequency is **2.817** vs the
swap set's **2.614** — a **+0.204 log-unit gap** (swap words ~1.6× rarer in pretraining; 2.3% never occur).
So the deep drop is **neither** SWAP-STABLE **nor** a clean exact-string-memorization signal: it is tangled
with the swap set simply being **rarer in pretraining**. The C8 chain closed on that ambiguity (R1 stays
descriptive/non-promotable), and the result registered the fix explicitly (scope cap #4): *"A clean
successor arm would **C4-frequency-match** the swaps; only then could a deep drop be read as exact-string
memorization rather than pretraining rarity."* This design is that arm.

## What it disambiguates (the symmetric prize)

R1 = **PROFILE-ALIGNED** (per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP per-paradigm
human agreement, ρ_prof +0.606 / +0.543 / +0.628, n=40 —
[`result/blimp-forced-choice-sweep-v1`](../../wiki/findings/results/blimp-forced-choice-sweep-v1.md)). The
s208 covariate arm returned **SURVIVES-COVARIATE 3/3**
([`result/blimp-profile-frequency-control-covariate-v1`](../../wiki/findings/results/blimp-profile-frequency-control-covariate-v1.md)).
Per the ratified **G8**, a human-comparison promotion of R1 needs **SURVIVES-COVARIATE ∧ SWAP-STABLE**. The
s210 swap arm did not deliver SWAP-STABLE — but for a reason (the C4 confound) that a frequency-matched swap
can remove. Matching the swap words on the **pretraining proxy** and re-running the deep stratum splits the
INCONCLUSIVE landing into two first-class, pre-registered outcomes:

- **DEEP-STILL-DROPS under C4-matching** → the exact strings were load-bearing **beyond** pretraining
  frequency → a **cleaner exact-string / lexical-item memorization signal** than s210 could show; R1 is
  refused promotion **more firmly**, and the honest reading ("the panel's deep-scope grammatical profile
  rides at least partly on having seen the BLiMP strings") is **sharpened** rather than left confounded.
- **DEEP-NO-LONGER-DROPS (SWAP-STABLE) under C4-matching** → the s210 deep drop **was** the pretraining-
  frequency confound; with pretraining frequency matched, the per-paradigm profile is statistically
  equivalent-to-unchanged under swap → **SWAP-STABLE now obtains**, and combined with the s208
  SURVIVES-COVARIATE, R1 becomes a **bounded promotion-review candidate** (a later, separate, cross-session
  adversarial review writes the `claim` — this run earns candidacy, never ratifies).
- **STILL-INCONCLUSIVE** → the disambiguation fails at the achievable N/match; report honestly and state what
  a cleaner instrument would need.

Both promoting outcomes and both refusing outcomes are pre-registered with **identical** bands; that
symmetry is the anti-cheat backbone (below).

## What is inherited byte-frozen from s210 (so the only new DoF is the C4 match)

The freeze session re-uses the s210 instrument **unchanged** — this is not a re-design of the measurement,
only of the swap-word selection criterion:

- **Elicitation:** the exact s205 forced-choice prompt, temperature 0, zero-shot, single-turn, **both
  presentation orders**, `google/*` reasoning suppressed, `usage.cost` via `openrouter.py`.
- **Paradigm set (Q1, accuracy- and human-agreement-blind):** the **same 6 frame-safe paradigms** the s210
  swappability rule selected — shallow `determiner_noun_agreement_2/_1`,
  `regular_plural_subject_verb_agreement_1`; deep `sentential_negation_npi_scope`, `only_npi_scope`,
  `superlative_quantifiers_1` — with the same G-frame exclusions (island/filler-gap and every `irregular_*`
  excluded; the **scope-deep pole covered, island-deep not**; that generality cost is reported).
- **Substitution recipe:** contrast locus never touched; only frame-free open-class categories (common
  nouns + proper names + attributive adjectives) swapped; main verbs + adverbs held fixed; POS + morphology
  preserved; the det-noun carve-out and sv subject guard verbatim.
- **Metric + verdict bands (G-metric):** SWAP-STABLE = per-model per-stratum signed Δ̄ bootstrap CI **within
  ±0.05** on both strata for ≥2/3; SWAP-DROPS = Δ̄ ≤ −0.05 with CI excluding 0 in a stratum ≥2/3; else
  INCONCLUSIVE. The ±0.05 margin's justification (matches the s205 `DEPTH_MARGIN`) is inherited.
- **Diagnostics:** the INSTRUMENT-FAILURE guard, the G-coverage 0.50 floor, the G-freq achieved-match report,
  and — now flipped from a post-hoc diagnostic to a **pre-build target** — the C4 pretraining-proxy
  distribution (`build_cooc_c4.py:stream_sentences`, the same 3M-sentence bounded stream the s210
  `analyze_swap.py --c4` used).

**Only Gate Q1 below changes the s210 recipe.** Q2 and Q3 fix scope and the disambiguation reading; both
default to the s210 posture with the minimal adjustment the new question forces.

---

## GATE Q1 (THE CRUX) — the C4-frequency-matching operationalization

The swap is a valid *pretraining-frequency-controlled* memorization control only if each substitute is (a)
novel, (b) POS/morphology-preserving (inherited), (c) **matched to the original on the models' pretraining
proxy (C4 log-frequency)**, and — the tension this gate resolves — **without silently re-opening the human
SUBTLEX-frequency gap the s210 arm controlled**. SUBTLEX (human-facing) and C4 (pretraining-proxy) frequency
are correlated but not identical (a word can be human-frequent yet pretraining-rare, e.g. speech-register
words), so a single-norm match on one leaves a residual gap on the other. The value-laden choice is *which
norm(s) bind, and how tightly*.

- **Q1-A (provisional default) — DUAL-BAND: SUBTLEX-US `Lg10WF` ±0.10 **AND** C4 log-frequency within a
  pinned band of the original, per replaced word.** The eligible substitute pool for each position is the
  **intersection** of the two bands; the substitute is drawn seeded-deterministically from that intersection
  (the s210 `pick()` discipline, blind to accuracies). This controls **both** confounds at once — it keeps
  the s210 human-frequency guarantee **and** closes the +0.204 pretraining gap — so a residual deep drop
  cannot be *either* a human-frequency *or* a pretraining-frequency artifact, only exact-string memorization
  (within the reported bands). **Sub-parameter (pinned at freeze after a pool-feasibility check): the C4
  band width, default ±0.30 log-units** — narrower than the +0.204 gap the arm exists to close, wide enough
  to keep the intersection pool non-empty for most positions; the freeze session reports pool sizes and, if
  the intersection is too thin for a position, **drops-and-logs** it (never widens the band after seeing
  which words survive — G-lexicon-determinism). *Cost of the default:* a smaller eligible pool ⇒ more
  dropped positions ⇒ possible power loss on thin paradigms (restated per G-power, drop below the usable
  floor). This is the honest price of a two-confound control and is reported, not hidden.
- **Q1-B — C4-PRIMARY: match on the C4 band only; report (do not bind) the achieved SUBTLEX gap.** Larger
  pool, less attrition; but it **risks re-introducing a human-frequency gap** — the very confound the s210
  arm controlled — so a deep drop could become a human-frequency artifact instead of a pretraining one. The
  ratifier may prefer this if the dual-band pool proves unworkably thin, but the default pays the attrition
  to control both.
- **Q1-C — SET-LEVEL C4 mean-match: match the swap-set *mean* C4 log-frequency to the original-set mean, not
  per word.** Cheapest on pool attrition (any in-band-SUBTLEX substitute is admissible as long as the set
  means balance), but set-level matching permits large **per-item** C4 mismatches that cancel in the mean —
  a weaker control that a per-paradigm Δacc could still ride. Admissible as a **labelled sensitivity
  cross-check** of Q1-A, not the default.

**Why value-laden.** Dual-band (Q1-A) buys a two-confound-clean Δacc at the cost of pool attrition and power;
C4-primary (Q1-B) buys power back by re-exposing the human-frequency channel; set-level (Q1-C) buys the most
power at the cost of per-item match quality. The default spends power to control **both** frequency channels
per word, because the whole point of the successor arm is that *neither* frequency proxy can explain a
surviving drop.

## GATE Q2 — scope (which strata / paradigms) and the ORIGINAL baseline

- **Q2-A (provisional default) — re-run the SAME 6 frame-safe paradigms, both strata, on a FRESH seeded
  ≈100-pair subsample DISJOINT from the s210 sample, ORIGINAL re-run fresh in-session.** Keeping both strata
  preserves the s210 verdict structure: the **deep-3 carry the load-bearing test** (that is where the s210
  drop and the C4 gap both concentrate), while the near-ceiling **shallow-3 remain the anchor** showing the
  swap machinery itself is not destructive. Drawing a **disjoint** ≈100-pair subsample (a new seed, item
  ids certified disjoint from the s210 sample) and **re-running the ORIGINAL condition fresh** alongside the
  new C4-matched SWAP condition makes `Δacc = acc_swap − acc_orig` a **within-run paired** quantity with
  **no known-accuracy exposure** on *either* condition (both are re-scored this run; the s210 per-item
  accuracies are not reused as a baseline). This is the A2a-rep2 disjointness posture applied to the swap
  arm.
- **Q2-B — deep-3 only** (drop the near-ceiling shallow stratum). Halves the run cost (~$0.67); the deep-3
  is where the disambiguation lives. Rejected as default because the shallow stratum is the cheap
  destructive-control anchor (a shallow drop under C4-matching would flag a broken swap build, not
  memorization) — worth keeping for ~$0.67 more.
- **Q2-C — reuse the s210 ORIGINAL accuracies as the baseline** (do not re-run originals). Halves calls
  again but re-introduces known-accuracy exposure into the comparison and cannot rule out cross-session
  drift. Rejected (the swap arm's whole value is its freedom from that exposure — the s210 design rejected
  the identical option for the identical reason).

## GATE Q3 — the disambiguation verdict + the promotion rule

- **Q3-A (provisional default) — the symmetric disambiguation map; candidacy bounded exactly as s210 bounded
  it, plus the new pretraining-frequency control; promotion always cross-session.** Reading the inherited
  G-metric on the C4-matched deep stratum:
  - **DEEP-STILL-DROPS** (C4-matched deep Δ̄ ≤ −0.05, CI excludes 0, ≥2/3) → a **cleaner exact-string /
    lexical-item memorization** reading than s210 (survives both frequency controls); R1 **refused
    promotion** and the memorization reading against
    [`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md) is
    sharpened. A **first-class negative**, not a disappointment.
  - **DEEP-SWAP-STABLE** (C4-matched deep Δ̄ CI within ±0.05, ≥2/3, both strata) → the s210 drop **was** the
    C4 confound; SWAP-STABLE now obtains; **with the s208 SURVIVES-COVARIATE**, R1 becomes a **bounded
    promotion-review candidate**. The candidacy is bounded to "R1's profile alignment is **not explained by
    exact-string / lexical-item memorization, the surface-lexical frequency proxy, *or* the pretraining-
    proxy frequency gap**" — it is **still not** construction-frequency-controlled nor template-difficulty-
    controlled (G3′ travels). A later cross-session review writes the `claim` or refuses it.
  - **STILL-INCONCLUSIVE** → neither promotion nor a clean memorization reading; the arm is reported and the
    line notes that even a two-confound-clean swap did not resolve the deep-scope alignment (a candid
    ceiling on what the swap paradigm can show at this N).
- **Q3-B — treat any stable outcome as a mere robustness datum; never re-open promotion.** Too conservative:
  the s208 SURVIVES-COVARIATE is already in hand, so a genuine DEEP-SWAP-STABLE under a two-confound-clean
  swap *is* the G8 conjunction the program pre-committed would earn candidacy. Rejected.
- **Q3-C — write the R1 claim this session (or the run session).** Rejected: promotion is always a separate,
  cross-session, adversarial review (PROTOCOL §3); the control session earns candidacy, never ratifies.

## Anti-cheat fence — LOAD-BEARING (the s210 deep drop is KNOWN)

This arm is designed **after** the s210 deep-drop magnitudes are known (−0.095 / −0.057 / −0.072), which is
a different exposure from the s210 arm (whose swapped accuracies were unknown at freeze). Three fences hold
the exposure:

1. **The new condition's accuracies are still unknown at freeze.** The C4-matched swap words are novel and
   different from the s210 SUBTLEX-matched ones, and the ORIGINAL is re-run fresh on a **disjoint** sample
   (Q2-A), so **no** accuracy in the Δacc is known when the recipe is frozen. The designer cannot tune the
   *outcome*; the C4-band is a mechanical frequency criterion, not an accuracy target.
2. **The verdict map is symmetric and pre-registered.** DEEP-STILL-DROPS (refuse) and DEEP-SWAP-STABLE
   (candidacy) carry **identical** bands. A design motivated by *wanting* R1 promoted would be the anti-cheat
   violation the charter forbids (PROTOCOL §2: ratification fixes the yardstick, never the result). This
   design is framed as a **disambiguation** whose two poles are equally publishable; the fresh-agent
   ratifier must confirm the framing is not result-motivated.
3. **Build-only DoF, verifier-reproduced.** As in s210, the frozen C4-banded lexicon + the substitution
   recipe + the disjoint-sample seed are frozen in `PREREG.md` and **independently reproduced by a
   fresh-agent verifier from the recipe before any item is scored** (G5-plus). The C4 counting reuses the
   s208/s210 `build_cooc_c4.py` streaming adapter import-pinned (no new corpus adoption; the license posture
   is the in-repo C4 one — [`resource/cooccurrence-corpus-scouting`](../../wiki/base/resources/cooccurrence-corpus-scouting.md)).

## Instrument-line note (the swap-redesign sequence has a governor)

This is the **second** swap-type arm on R1 (s210 SUBTLEX-matched → this C4-matched). It is **not** yet at the
PROTOCOL §3 instrument-stopping threshold (3 null-yielding redesigns on one construct), and the s208
covariate arm SURVIVED (a positive corroboration, not a null), so the line is not in a null streak. But the
freeze session should record that a **third** swap redesign (e.g. a verb-swap arm with a valence guard, the
other s210-named successor) would trip the governor and require a cross-session line-continuation review
before it runs.

## Cost (pre-flight — from OBSERVED s210 economics, per the s229 cost lesson)

- **Default (Q1-A dual-band, Q2-A both strata, N≈100/paradigm, 6 paradigms):** 6 × 100 pairs × 2 conditions
  × 2 orders × 3 models = **7,200 calls ≈ $1.3–1.6** at the **observed** s210 per-call economics (the s210
  arm ran 7,200 calls billed ~$1.34). **Under the $2.50 prefer-split flag → no split**, and it fits a full
  $5 UTC day as the day's main run. Hard per-model `ABORT_USD ≈ 1.60` in `probe.py` at freeze (the s210
  value).
- **Q2-B (deep-3 only):** ~$0.67. **Q1-C sensitivity cross-check:** no extra model cost (C4 streaming
  compute only). The C4 pre-build banding streams the same bounded 3M-sentence C4 prefix as the s210
  diagnostic — **$0 model cost**, build compute only.
- **This design session (s231):** the only spend is **one non-Anthropic decorrelation vote** (`gpt-5.4-mini`
  via the probe REST path, ~$0.002–0.004) as QA to the fresh-agent design critic — trivially under the
  ~$1.82 UTC-2026-07-15 headroom.

## Scope caps — LOAD-BEARING (read before citing any result this design produces)

1. **Controls R1 only, and now the exact-string memorization sub-confound *net of both* the human-frequency
   (s210) and the pretraining-proxy-frequency (this arm) channels.** It still does **not** control
   **construction** frequency or template difficulty (G3′ travels), and does **not** touch R2 (DEPTH-GRADED,
   within-panel) or R2h.
2. **C4 is a *proxy* for pretraining, not the panel's actual training distribution.** "C4-frequency-matched"
   reads "matched on a public web-text proxy for pretraining exposure," never "matched on the models' true
   training frequency." A residual per-word C4 gap within the band is reported.
3. **SWAP-STABLE means "not driven by memorizing the exact BLiMP strings (net of both frequency proxies),"
   never "grammatical competence."** Absolute accuracy stays a contamination upper bound.
4. **Deep-pole generality cost** (scope-deep covered, island-deep not) and **perturbation bound**
   (nouns/names/adjectives only; verbs/adverbs fixed) carry unchanged from s210.
5. **n = 3 models; per-model, per-stratum Δacc, never pooled.** Acceptability, not inference; behavioral
   2AFC, not logprob; the s205 elicitation.

## Handoff (what s231 did, and what remains)

1. **s231:** wrote this design; opened the decision
   ([`decisions/open/blimp-c4-matched-swap-arm-design`](../../wiki/decisions/open/blimp-c4-matched-swap-arm-design.md);
   Q1–Q3, provisional defaults **Q1-A / Q2-A / Q3-A**); ran the design pre-run critic (fresh agent, verdict
   authority) + one non-Anthropic decorrelation vote, recorded under
   [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm-design/`](../runs/2026-07-15-blimp-c4-matched-swap-arm-design/).
   **Nothing frozen, nothing run.** No `predictions.md` row yet — the bet is registered **at freeze** (the
   s210 swap-arm lineage: predictions row registered at freeze, not at design), with no outcome pre-filled.
2. **Ratify (s232+):** a fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** fork the s210 `build_swap.py` into a C4-banded `build_swap_c4.py` (add
   the C4-band intersection to the substitute pool; sha256-pin the C4-banded lexicon; deterministic seeded
   selection from the intersection; disjoint-sample seed) + re-use the s210 `probe.py` (the s205 elicitation,
   both orders, `ABORT_USD`) + fork `analyze_swap.py` into `analyze_swap_c4.py` (per-model per-stratum signed
   Δacc + bootstrap CIs + the achieved SUBTLEX **and** C4 per-word gap distributions); pin the lexicon +
   bands + disjointness + verdict map in `PREREG.md` **before any swapped item is built or scored**; the
   swap-build is **independently reproduced by a fresh-agent verifier before scoring** (G5-plus); independent
   pre-run freeze critic + one non-Anthropic vote; register the `predictions.md` bet at freeze.
4. **Run (after freeze):** the C4-matched swap arm (~$1.3–1.6, one full-$5 UTC day); post-run verifier
   recomputes every figure from the frozen items + the fresh C4-banded swap build.

## Freeze-time conditions (bind the freeze session)

- **G5-plus (anti-cheat — the swap arm's build is its only exposure, *and* the s210 drop is known).** The
  C4-banded swap-build is frozen in PREREG and **independently reproduced by a fresh-agent verifier from the
  recipe before any item is scored**; the C4-banded lexicon is committed + sha256-pinned; the disjoint-sample
  seed is pinned; the symmetric verdict map is frozen. The fresh-agent ratifier explicitly checks the design
  is a disambiguation, not a promotion-seeking retune.
- **G-C4-band (the new DoF — pinned, not inherited).** The C4 band width (default ±0.30 log-units) is pinned
  in PREREG after a **pool-feasibility check** (report intersection pool sizes per position); never widened
  after seeing which words survive. If a position's intersection pool is empty it is **dropped-and-logged**
  (Q1-A), not force-filled by widening.
- **G-frame / G-metric / G-coverage / G-power / G-freq / G3′** — all **inherited byte-frozen from the s210
  PREREG** (frame-safe paradigm restriction; ±0.05 equivalence bands; 0.50 coverage floor; N≈100 fresh pairs
  with the usable-pair floor and power-restatement; the ±0.10 SUBTLEX achieved-match report; the
  construction-frequency caveat travels).
- **G-disjoint (Q2-A).** The re-run ORIGINAL + C4-matched SWAP sample is a fresh seeded ≈100-pair subsample
  **certified disjoint** from the s210 sample (item ids), asserted + independently re-verified at freeze.
- Carry the standard fences: PREREG committed before any swap build or model call; independent pre-run critic
  + one non-Anthropic vote at freeze; `ABORT_USD`; `predictions.md` row at freeze; the s205 INSTRUMENT-FAILURE
  guard verbatim.
