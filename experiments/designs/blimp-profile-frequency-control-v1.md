---
type: design
id: blimp-profile-frequency-control-v1
title: "BLiMP profile-alignment frequency control (C8 promotion-prep) — does R1 (the panel's grammatical difficulty profile tracks the human one, ρ_prof +0.54–0.63) survive a training-frequency confound control? DESIGN, not frozen; three gates open"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: draft
anchor: resource/blimp
contingent-on:
  - blimp-profile-frequency-control-design
created: 2026-07-11
updated: 2026-07-11
links:
  - rel: operationalizes
    target: result/blimp-forced-choice-sweep-v1
  - rel: depends-on
    target: resource/blimp
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Design v1 — BLiMP profile-alignment frequency control (program A3b, C8 promotion-prep)

**A design + decision-trail unit — the pre-registered training-frequency confound control that binding
condition C8 of the s205 BLiMP ratification names as the gate on promoting R1. Status: DESIGN — three
gates open, ratifiable s208+.** This page operationalizes the promotion-blocking control for the PRIMARY
human-anchored reading of [`result/blimp-forced-choice-sweep-v1`](../../wiki/findings/results/blimp-forced-choice-sweep-v1.md):
**R1 PROFILE-ALIGNED** (per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP's per-paradigm
human agreement, ρ_prof **+0.606 / +0.543 / +0.628**, all CIs > 0, n = 40 paradigms). Per PROTOCOL §3/§A1
and the A3b/A1b precedent (design one session, ratify the next, run after ratification): **design s207,
ratifiable s208+, run after ratification.** A control that opens a value-laden decision is not run in the
session that opens it.

> **What C8 requires, verbatim (from the s205 ratification, on
> [`decisions/resolved/blimp-forced-choice-sweep-design`](../../wiki/decisions/resolved/blimp-forced-choice-sweep-design.md)
> and the [design's freeze conditions](blimp-forced-choice-sweep-v1.md)):** *"The PRIMARY reading-1
> verdict (PROFILE-ALIGNED) is non-promotable to a `claim` unless a training-frequency confound has been
> controlled … Satisfy C8 by either the F7 content-word-swap arm on ≥2 shallow + ≥2 deep paradigms
> (original-vs-swapped accuracy, pre-registered), or a pre-registered corpus-frequency covariate for each
> construction partialled from ρ_prof — decided and frozen in PREREG before any model call."* This design
> makes that choice a value-laden gate (Q1), fixes the frequency proxy it turns on (Q2 — **the crux**),
> and pins what a survival/break licenses (Q3).

> **This unit is HUMAN-ANCHORED, not internal-contrast-only.** R1 is a genuine human-comparison line
> (per-paradigm human agreement is the key). The control does **not** change that type — it tests the
> **validity** of the comparison against the one threat the s205 run left open (C8), exactly as the s204
> critic distinguished contamination-as-validity-threat from contamination-as-type (see that critic's
> *Anchor discipline* section). If the control passes, R1 becomes a promotion-review candidate — the
> program's **first broad human-anchored grammatical-competence claim**. If it fails, R1 keeps only its
> descriptive/directional status and the flagship table's form-(iv) row keeps **only DEPTH-GRADED**.

---

## Why this unit is owed now

1. **Two-track balance owes empirical** (s204 design + s205 run were empirical, but s206 was
   phil/consolidation, so the recent lean tips back toward empirical) — and this is the **named next
   step** for the highest-value open empirical line. R1 is the program's one live path to a *broad*
   human-anchored grammatical-competence claim; C8 is the single pre-registered gate between the s205 run
   and that claim. Nothing else in the backlog is as close to a compounding claim.
2. **The control is cheap and the inputs are frozen.** The whole covariate arm (Q1-A) reuses the s205
   frozen per-paradigm accuracies (`results.json → per_model[*].per_paradigm`, verifier-reproduced) and
   the committed per-paradigm human anchor (`experiments/data/blimp/human_validation_summary.csv`, sha256
   `ea0e7c21…`), and it streams the same frozen C4 shards (00000–00002) the prior corpus runs used — so
   the covariate arm is a **$0-model-cost, corpus-side re-analysis**. Only the swap arm (Q1-B/C) spends
   model calls. C4 shards 00000–00002 are the license-verified proxy corpus, first fetched + frozen at
   [`experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/build_cooc_c4.py`](../runs/2026-07-08-relation-recovery-taxonomic-proxy/build_cooc_c4.py)
   (ODC-BY + the Common-Crawl terms carried to provenance; the deterministic 22,329,495-sentence set;
   scouted at [`resource/cooccurrence-corpus-scouting`](../../wiki/base/resources/cooccurrence-corpus-scouting.md)).
   **Honest reuse boundary (s207 pre-run critic, BLOCKER-1):** what is reusable from that script is only
   the **C4 streaming adapter + tokenization regexes** — it computes unigram document-frequency, cue-anchored
   co-occurrence, and a signed-G² kernel, **no per-n-gram frequency counter**, and its on-disk copies are
   not byte-identical (the import assertion freezes the *G² kernel*, which `F(p)` does not use). So the
   `F(p)` n-gram extraction + aggregation is **new code with genuine researcher DoF**, authored with the
   s205 accuracies already known — the covariate arm's central anti-cheat exposure (freeze condition G1′).
3. **C8 is symmetric.** The control is a yardstick, not a verdict-in-waiting. A **BREAKS** outcome — R1
   dissolves once frequency is partialled out — is a first-class negative that *refuses* the program its
   would-be flagship claim and hardens the honest reading that the panel's grammatical profile is a
   training-frequency shadow. Pre-registering the bands identically for SURVIVES and BREAKS is the whole
   point (Q3, anti-cheat fence).

## The confound C8 names (why R1 is not yet promotable)

R1 says: the panel is grammatically hard **where humans are hard** (ρ_prof > 0). The threat is that this
alignment is manufactured by a **training-frequency artifact** rather than shared grammatical-difficulty
structure:

- Frequent local-agreement constructions (adjacent determiner–noun, regular subject–verb) are plausibly
  **both** human-easy (people rarely disagree on them) **and** the most represented in web-scale
  pretraining (so the panel aces them);
- Rare island / scope / long-distance contrasts are plausibly **both** human-harder (people disagree
  more) **and** less represented (so the panel stumbles more).

If corpus frequency correlates with human agreement `H(p)`, then a panel that is simply "good at frequent
things" will show a positive ρ_prof **with perfectly healthy across-paradigm accuracy variance** — which
is why the s205 F3 saturation/range guard (variance-near-zero → INCONCLUSIVE) does **not** catch it
(F3 passed at s205: SD 0.12/0.15/0.11). C8 is the residual, un-caught threat.

**What would rebut it:** show that the alignment is **over-and-above** frequency — i.e. R1 survives a
control that removes the frequency signal (a partialled covariate, Q1-A), or that R1 does not depend on
memorizing the exact surface strings (a content-word swap, Q1-B), or both (Q1-C).

## GATE Q1 — the control strategy (THE CRUX)

C8 names two admissible controls; they test **different sub-confounds** and are not interchangeable.

- **Q1-A (provisional default) — the corpus-frequency covariate, partialled from ρ_prof.** For each of
  the 40 frozen paradigms compute a per-paradigm frequency proxy `F(p)` from C4 (Q2), then report the
  **partial Spearman** ρ_prof·F(m) = correlation of `acc(m,·)` with `H(·)` **controlling `F(·)`**, per
  model with its CI. Directly targets C8's literal confound (paradigm-level frequency correlated with
  human agreement inflating ρ_prof). **$0 model cost** (reuses the frozen s205 accuracies; only C4
  streaming compute). **n = 40, partialling one covariate ⇒ df = 37**, two-sided p<0.05 at partial
  |ρ| ≈ 0.32 — genuinely powered (the raw ρ_prof +0.54–0.63 sit well above that, so a survival vs a
  break is distinguishable, unlike the n≈10 power failure the original A3b design had to fix). *Weakness:*
  the covariate only controls what the proxy `F(p)` captures; its validity is entirely Q2's problem, and
  it inherits an **anti-cheat exposure** the swap arm does not — the designer already knows the s205
  accuracies and ρ_prof, so "freeze the covariate before computing it" is weaker than "freeze before any
  data." Mitigation is freeze condition G1′ (below), but the residual exposure is real and is the chief
  argument for adding the swap arm (Q1-C) — the s207 pre-run critic + vote both **require Q1-C for a
  promotion** (G8), leaving the covariate arm alone to earn only a robustness result.
- **Q1-B — the F7 content-word-swap behavioral arm.** Re-instantiate ≥2 shallow + ≥2 deep paradigms with
  novel open-class content words (from a controlled frequency-balanced list), **re-validate that the
  minimal grammatical contrast survives the swap**, re-run the panel forced-choice (both orders), and
  compare original-vs-swapped accuracy per paradigm. If accuracy is **stable** under swap on both strata,
  the profile is not driven by memorizing the exact BLiMP strings. *Strengths:* fresh items + fresh calls
  ⇒ **no anti-cheat exposure** to the known accuracies; it is a direct behavioral test. *Weaknesses:* it
  controls **exact-string / lexical memorization**, **not construction frequency** (a content-swapped
  island is still a rare *construction*), so it does not rebut C8's literal confound; it costs model calls
  (est. ~$0.3–0.6, below); and re-instantiation risks breaking grammaticality (needs re-validation, a
  build cost + its own DoF).
- **Q1-C — both.** The covariate as the direct partial-out of construction frequency, the swap arm as a
  convergent behavioral check on exact-string memorization. Most complete (the two sub-confounds are
  complementary; a claim that clears both is far better armored); most spend + build. A reviewer who
  judges the covariate's proxy-fidelity + anti-cheat exposure too weak to license promotion **on its own**
  should vote C.

**Why value-laden.** The covariate and the swap arm answer *different* questions ("is the alignment
over-and-above corpus frequency?" vs "does the alignment survive swapping the exact words?"). C8 accepts
either, but they are not equivalent evidence for a promotion. The default (Q1-A) buys the direct,
$0 control at the cost of proxy-dependence and an anti-cheat exposure; Q1-C buys full armor at real spend.
**This is the central choice, and NEXT.md flags it as the crux.**

## GATE Q2 — the frequency proxy `F(p)` (the covariate's crux; live iff Q1 includes the covariate)

The covariate is only as good as `F(p)`. Three operationalizations, targeting different notions of
"frequency," with different fidelity/entanglement/cost:

- **Q2-A (provisional default) — per-paradigm mean surface-string corpus frequency.** Over each
  paradigm's frozen `sentence_good` items, `F(p)` = the mean log C4 frequency of the sentence's
  content-word bigrams/trigrams (a familiarity/exposure proxy: how frequent is the *surface material* of
  this paradigm's items). Cheap (byte-reuse the C4 streaming + n-gram counting from `build_cooc_c4.py`),
  reuses the frozen items, ~$0. *Risk:* it is a proxy for **lexical familiarity**, not construction
  frequency, and it partly entangles with detectability; a paradigm can be lexically ordinary yet a rare
  *construction*.
- **Q2-B — the good−bad local-detectability margin.** `F(p)` = the mean difference in local-n-gram C4
  frequency between the good and bad member of each pair (how much surface co-occurrence favors the good
  sentence). This is the **shadow-depth axis** itself, operationalized as a covariate. *Risk — the
  central Q2 hazard:* partialling detectability from ρ_prof is a very **strong, possibly over-strong**
  control, because human difficulty `H(p)` **also** tracks depth/detectability (deep contrasts are hard
  for people too) — so removing detectability can strip out **genuine shared grammatical-difficulty
  structure**, not just a frequency artifact, and a BREAKS here would **not** cleanly separate "frequency
  artifact" from "the shared structure *is* the depth structure." Report only with that caveat made
  load-bearing; likely the wrong sole covariate.
- **Q2-C — construction-level frequency.** `F(p)` = the C4 rate of the licensing configuration itself
  (e.g. the pattern that realizes the paradigm's construction), by a per-paradigm pattern match. Most
  faithful to C8's literal "corpus-frequency covariate for each construction," but **high build cost**
  (a hand-authored, defensible pattern per paradigm across 40 paradigms) + heavy operationalization DoF
  (each pattern is a researcher choice) — itself an anti-cheat surface.

**Why value-laden.** Fidelity-to-C8 trades against cost and against over-control. Q2-A is the cheapest,
least-entangled memorization-exposure proxy but the least construction-specific; Q2-B is faithful to the
depth axis but risks controlling away the very structure R1 might genuinely share with humans; Q2-C is
faithful to the literal confound but expensive and DoF-heavy. The default trusts Q2-A **as the primary**
with **Q2-B reported as a labelled, deliberately-conservative sensitivity arm** (an *upper bound on how
much of ρ_prof frequency-plus-detectability can explain*), never as the sole control — mirroring the
antonymy line's "embedding cosine only a labelled sensitivity check" discipline
([`decisions/resolved/antonymy-internal-contrast-scoring`](../../wiki/decisions/resolved/antonymy-internal-contrast-scoring.md)).

## GATE Q3 — the promotion rule + the honest proxy-scope

BLiMP is contamination-bounded and C4 is a **proxy** for the panel's unknown pretraining distribution.
What may a survival license, and how is the proxy's imperfection carried?

- **Q3-A (provisional default) — the control is a promotion GATE, and its outcome is reported as a
  standalone result either way.** Pre-register: **SURVIVES** iff the partial ρ_prof·F(m) stays clearly
  positive (band frozen, e.g. partial ρ ≥ +0.3 with CI excluding 0) on ≥2/3 models → R1 PROFILE-ALIGNED
  becomes a **promotion-review candidate** (a later cross-session, adversarial promotion review writes
  the `claim`; the control does not itself write the claim). **BREAKS** iff partial ρ_prof·F(m) drops to
  near-zero / CI includes 0 on ≥2/3 → R1 is **refused promotion**; the shadow-depth table's form-(iv) row
  keeps **only DEPTH-GRADED**; the honest reading becomes "the panel's grammatical profile is (at least
  partly) a training-frequency shadow." A pre-registered **[+0.0,+0.3] with-CI-spanning-0** middle is
  **INCONCLUSIVE**. The result page is `anchor: resource/blimp` (human-comparison), never
  internal-contrast-only. **Two load-bearing proxy caveats (G3′):** (i) C4 ≠ the panel's actual training
  corpora, so a SURVIVES reads "R1 survives control against a **C4-frequency proxy**," not "against actual
  training frequency"; (ii) under the Q2-A default the covariate partials out **surface-lexical
  familiarity, not construction frequency** (C8's literal confound), so the covariate arm's honest reach is
  "over-and-above **lexical/surface exposure**," never "over-and-above construction frequency" unless Q2-C
  is run — and even the swap arm targets exact-string memorization, so construction frequency is only ever
  *indirectly* addressed. The promotion candidacy carries **both** caveats into the claim review; it does
  not launder them away.
- **Q3-B — the control produces only a within-model robustness datum, never a promotion gate.** If the
  proxy is judged too weak a stand-in for the panel's real pretraining distribution to license a
  human-comparison promotion, report the partial-ρ as an internal-contrast robustness check on R1 and
  leave R1 permanently descriptive. Rejected as default (it forfeits the one clear path to the program's
  first broad human-anchored grammatical claim on a proxy-imperfection that a stated caveat already
  handles), but a reviewer who weights proxy-infidelity heavily may prefer it.
- **Q3-C — treat a SURVIVES as itself sufficient to write the claim this line's next session** (no
  separate promotion review). Rejected: promotion is always a **separate, cross-session, adversarial**
  review per PROTOCOL §3 / the B1 procedure — the control session may **earn candidacy**, never ratify
  the claim in its own run.

**Why value-laden.** Whether the frequency control is a promotion **gate with a stated proxy caveat**
(Q3-A), a demoted robustness-only datum (Q3-B), or a claim-writing license (Q3-C, over-reach). The default
keeps promotion cross-session and carries the proxy's imperfection honestly into the candidacy.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

Let `acc(m,p)` = model m's order-averaged forced-choice accuracy on paradigm p (**reused verbatim from
the frozen s205 `results.json`**); `H(p)` = BLiMP per-paradigm human agreement (`total_mean`, committed);
`F(p)` = the Q2 frequency proxy. ρ_prof(m) = the raw s205 Spearman; **ρ_prof·F(m) = the partial Spearman
of `acc(m,·)` vs `H(·)` controlling `F(·)`.**

- **Covariate arm (Q1-A/C) — SURVIVES** iff ρ_prof·F(m) bootstrap CI **excludes 0** on **≥2/3** models
  (the binding criterion; at df=37 that already requires partial |ρ| ≳ 0.325, so the +0.3 figure is a
  non-binding floor, not a second gate); **BREAKS** iff the CI includes 0 on ≥2/3; the exact band is fixed
  in PREREG before `F(p)` is computed. Report the **raw→partial drop** (ρ_prof(m) − ρ_prof·F(m)) as the
  effect-of-control magnitude, per model with CI, and state power as **P(bootstrap CI excludes 0) at the
  expected partial magnitude, per model** (not the point-threshold — the weaker models' wide n=40 CIs make
  an INCONCLUSIVE landing the realistic risk even on a true partial ≈+0.35).
- **`corr(F, H)` branches (BLOCKER-3 / G6 — the confound's own structure decides interpretability):**
  report the frequency–human correlation `corr(F, H)` first. If it is **near zero**, the confound C8
  posited is **absent** and R1 is corroborated by that fact alone (a first-class sub-outcome). If it is
  **above a pre-registered high threshold**, `F` and `H` are strongly collinear (the very confound
  scenario the control exists for): the partial coefficient has inflated variance and, insofar as `F`
  tracks depth, partialling it strips genuine shared structure — so the partial ρ is reported
  **INCONCLUSIVE (over-control-suspect)**, a distinct branch from both SURVIVES/BREAKS and the
  `corr(F,H)≈0` corroboration. Only the **intermediate-collinearity** regime yields an interpretable
  SURVIVES/BREAKS.
- **Swap arm (Q1-B/C) — SWAP-STABLE** iff mean original-vs-swapped accuracy change is within a
  pre-registered band (e.g. |Δacc| ≤ 0.05) on both the shallow and deep swapped paradigms for ≥2/3
  models (the profile does not depend on exact-string memorization); **SWAP-DROPS** iff accuracy falls
  materially under swap (exact strings were load-bearing) — a first-class negative.
- **Combined promotion verdict (Q1-C):** promotion candidacy requires **SURVIVES ∧ SWAP-STABLE**; either
  a BREAKS or a SWAP-DROPS refuses promotion (the stricter conjunction is deliberate — a claim armored
  against both sub-confounds is the only one worth the program's first broad grammatical claim).
- **Pre-named nulls (first-class):** BREAKS (R1 is a frequency shadow); SWAP-DROPS (R1 is exact-string
  memorization); `corr(F,H)`≈0 (no confound to control — R1 corroborated); an INCONCLUSIVE middle band.
  Each is pre-registered and reported, never silently dropped.
- **Anti-cheat fence (PROTOCOL §B).** The Q2 proxy definition (which n-grams, the content-word selection,
  log-vs-raw, the aggregation to `F(p)`), the partial-ρ method + bootstrap, the SURVIVES/BREAKS/collinearity
  bands, and (for the swap arm) the swap word-list + grammaticality re-validation rule are **all frozen in
  `PREREG.md` before `F(p)` is computed or any swapped item is scored**, and the new `build_freq.py` is
  **independently reproduced by a fresh-agent verifier from the frozen spec before `F(p)` touches the real
  paradigm→H mapping** (freeze condition G1′). The `F(p)` code reuses only the C4 **streaming adapter +
  tokenization** from `build_cooc_c4.py` (import-assertion-pinned to the copied code); the n-gram
  extraction + aggregation are **new code with genuine DoF** — the reuse does **not** carry "no new DoF,"
  and a scrambled paradigm→H sanity check is **necessary-not-sufficient** (a scramble collapses ρ_prof to
  ~0 regardless of `F`). BREAKS, SWAP-DROPS, and the nulls are pre-named first-class results. *(The reuse
  of the known s205 accuracies is this design's single sharpest exposure — the chief argument for adding
  the swap arm, Q1-C; see the pre-run critic conditions below.)*

## Panel & settings (swap arm only)

The covariate arm makes **no model call**. If the swap arm (Q1-B/C) is adopted: panel = the three
[`config/models.md`](../../config/models.md) slots (`panel.A/.B/.C`), temperature 0, zero-shot, both
presentation orders (the s205 Q2-A control), `google/*` reasoning suppressed/capped (config Caveat 1),
`usage.cost` recorded via [`experiments/lib/openrouter.py`](../lib/openrouter.py).

## Cost (pre-flight estimate)

- **Covariate arm (Q1-A):** **$0 model cost.** C4 streaming compute only (the s193/s199/s202 pattern;
  minutes, run in background, no billed spend).
- **Swap arm (Q1-B), if adopted:** ~4 paradigms × ~110 items × 2 orders × 3 models ≈ **2,640 calls** ≈
  **$0.3–0.6** across the panel (the s205 per-call economics; gemini reasoning suppressed). A hard
  `ABORT_USD` (~$1.0) in `probe.py` at freeze.
- **Q1-C:** the swap-arm cost only (~$0.3–0.6); the covariate is free.
- **This design session (s207):** the only spend is **one non-Anthropic decorrelation vote**
  (`gpt-5.4-mini` via the probe REST path, ~$0.002–0.003) as QA to the fresh-agent design critic.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Controls R1 only.** This unit tests the promotability of the **PROFILE-ALIGNED** reading. It does
   **not** touch R2 (DEPTH-GRADED, within-panel — already verdict-bearing) or R2h (TRACKS-DIP).
2. **C4 is a proxy for the panel's unknown pretraining distribution, and the Q2-A proxy is surface-lexical,
   not construction-level.** A SURVIVES means "over-and-above a **C4 surface-lexical** frequency proxy,"
   never "over-and-above the panel's actual training frequency" nor "over-and-above **construction**
   frequency" (both Q3-A caveats; only Q2-C reaches construction frequency, at the over-control hazard G2).
3. **Reuses the frozen s205 accuracies** — the covariate arm adds **no new grammatical measurement**; its
   force is entirely in the partialling. The accuracies, human anchor, and items are byte-frozen and
   verifier-reproduced (s205); this design only adds `F(p)` and the partial-ρ.
4. **Acceptability, not inference; behavioral 2AFC, not logprob; 40-paradigm observed set** — all the
   s205 scope caps carry unchanged ([`result/blimp-forced-choice-sweep-v1`](../../wiki/findings/results/blimp-forced-choice-sweep-v1.md)).
5. **n = 3 models; per-model partial coefficients with CIs, never pooled.**

## What each outcome feeds

- **SURVIVES (∧ SWAP-STABLE if Q1-C):** R1 becomes a promotion-review candidate — the program's first
  broad human-anchored grammatical-competence claim (with the C4-proxy caveat); the shadow-depth table's
  form-(iv) row hardens from descriptive toward a claim. A `predictions.md` row (registered at **freeze**)
  fires-for.
- **BREAKS:** a first-class negative — the panel's grammatical difficulty profile is (at least partly) a
  training-frequency shadow; R1 stays descriptive; the table's form-(iv) row keeps **only DEPTH-GRADED**;
  the honest reading against the essay is sharpened (the human-alignment of the grammar-side gradient does
  not clear a frequency control).
- **`corr(F,H)`≈0:** the C8-posited confound is empirically absent — R1 corroborated *because there was no
  frequency structure to inflate it*.
- **[`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md):**
  either outcome sharpens the grammar-side placement (survives → shared structure over-and-above
  frequency; breaks → the alignment is frequency-mediated). No revision trigger fires from the design
  itself; the run's outcome may.

## Handoff (what s207 did, and what remains)

1. **s207 (this session):** wrote this design; opened
   [`decisions/open/blimp-profile-frequency-control-design`](../../wiki/decisions/open/blimp-profile-frequency-control-design.md)
   (Q1–Q3, provisional defaults **Q1-A / Q2-A / Q3-A**); ran the design pre-run critic (fresh agent,
   verdict authority — **GO-WITH-CONDITIONS**, provenance + anchor CLEAN, three blockers) + one
   non-Anthropic decorrelation vote (`gpt-5.4-mini`, **GO-WITH-CONDITIONS, Q1-C**, $0.0042; recorded under
   [`experiments/runs/2026-07-11-blimp-frequency-control-design/`](../runs/2026-07-11-blimp-frequency-control-design/)).
   **The three blockers are discharged in-design this session** (the `build_cooc_c4.py` misdescription
   corrected → G1′; the surface-vs-construction scope caveat added → G3′; the collinearity branch added →
   G6); G1′–G8 bind the freeze. **Both reviewers converge on Q1-C (swap arm) being required for a
   promotion** — recorded on the open decision, to be weighed at ratification. **Nothing frozen, nothing
   run.**
2. **Ratify (s208+):** a fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** write `build_freq.py` (reuse only `build_cooc_c4.py`'s C4 streaming
   adapter + tokenization, import-pinned to the copied code; the n-gram extraction + `F(p)` aggregation
   are new, frozen in PREREG, and **independently reproduced by a fresh-agent verifier before `F(p)`
   touches the real paradigm→H mapping**; compute `F(p)` over the frozen s205 items; sha256-pin) +
   `analyze_partial.py` (partial Spearman ρ_prof·F with bootstrap CIs from the frozen s205 accuracies +
   committed human anchor; `corr(F,H)` + the collinearity branch) [+ `swap_probe.py` if Q1-B/C]; fix the
   proxy + bands + bootstrap + collinearity threshold in `PREREG.md` **before `F(p)` is computed**; run a
   proxy-validity audit (G7) before inspecting any partial outcome; independent pre-run freeze critic +
   one non-Anthropic vote; register the `predictions.md` bet at freeze.
4. **Run (after freeze):** the covariate arm ($0) [+ the swap arm if adopted]; post-run verifier
   recomputes every figure from the frozen accuracies + a fresh `F(p)` build.

## Freeze-time conditions (bind the freeze session)

From the s207 fresh-agent pre-run design critic (verdict authority; **GO-WITH-CONDITIONS**, no NO-GO, no
fabrication — provenance + anchor discipline CLEAN) + the convergent non-Anthropic decorrelation vote
(`gpt-5.4-mini`, GO-WITH-CONDITIONS, Q1-C), recorded in
[`REVIEW-design-s207.md`](../runs/2026-07-11-blimp-frequency-control-design/REVIEW-design-s207.md) +
[`VOTE-s207.json`](../runs/2026-07-11-blimp-frequency-control-design/VOTE-s207.json). The critic raised
three blockers; **BLOCKER-1/2/3 are discharged in-design this session** (the `build_cooc_c4.py`
misdescription corrected; the surface-vs-construction scope caveat added; the collinearity branch added);
the conditions below bind the freeze:

- **G1′ (anti-cheat — this design's sharpest exposure; BLOCKER-1).** The covariate arm reuses the
  **already-known** s205 accuracies and ρ_prof, and `F(p)` is **new code with genuine DoF** (only the C4
  streaming adapter + tokenization are reused from `build_cooc_c4.py` — it has **no n-gram counter**, and
  its import-assertion pins the *G² kernel* `F(p)` does not use). Bind: (a) the import-time assertion in
  `build_freq.py` pins the *actually-copied* streaming/tokenization code, not the G² kernel; (b) the
  `F(p)` recipe (n-gram order, content-word selection, log/aggregation, item-set targeting), partial-ρ
  method, and all bands are fixed in PREREG **before `F(p)` is computed**; (c) `build_freq.py` is
  **independently reproduced by a fresh-agent verifier from the frozen spec before `F(p)` touches the real
  paradigm→H mapping**; (d) a scrambled paradigm→H negative control is reported but is
  **necessary-not-sufficient** (a scramble collapses ρ_prof regardless of `F`). The swap arm (Q1-B), using
  fresh items + fresh calls, is free of this exposure — the standing argument for Q1-C.
- **G2 (over-control — Q2-B).** A detectability-margin proxy (Q2-B) is a **labelled conservative
  sensitivity arm only, never a decision gate**, with the "may strip genuine shared depth structure, so a
  BREAKS-under-Q2-B does not cleanly imply a frequency artifact" caveat load-bearing on every mention.
- **G3′ (proxy scope — BLOCKER-2).** Every SURVIVES/BREAKS statement carries **both** caveats: "against a
  **C4-frequency proxy**, not actual pretraining frequency" **and** "the Q2-A covariate controls
  **surface-lexical familiarity, not construction frequency**." The covariate arm's honest reach is
  "over-and-above lexical/surface exposure"; construction frequency is reached only by Q2-C (at the G2
  over-control hazard), and even Q1-C leaves it only indirectly addressed.
- **G4′ (power).** State power as **P(bootstrap CI excludes 0) at the expected partial magnitude, per
  model** (not the point threshold); the CI-exclusion gate at df=37 requires partial |ρ| ≳ 0.325, so the
  +0.3 SURVIVES figure is a non-binding floor. If a proxy needs paradigm exclusions that drop n, re-state
  power and downgrade to descriptive if it falls too low.
- **G5 (swap grammaticality — Q1-B/C).** The swapped items' minimal grammatical contrast is **re-validated
  before scoring** (a broken pair is dropped, logged, and reported — never silently repaired); the swap
  word-list is frequency-balanced and frozen in PREREG.
- **G6 (collinearity guard — BLOCKER-3).** A frozen high-`corr(F,H)` threshold above which the partial ρ
  is reported **INCONCLUSIVE (over-control-suspect)** — distinct from both SURVIVES/BREAKS and the
  `corr(F,H)≈0` corroboration branch.
- **G7 (proxy-validity audit — vote condition).** A single primary `F` definition + one pre-specified
  sensitivity variant; **no post-hoc proxy tuning**; before inspecting any partial outcome, show `F(p)`
  has a sensible relation to an external frequency benchmark.
- **G8 (promotion gate — both reviewers converge).** **The Q1-C swap arm is required for a human-comparison
  PROMOTION;** the covariate arm alone earns only a **robustness / corroboration** result, never a
  promotion candidacy. Promotion candidacy inherits the G3′ surface-vs-construction scope. *(This is a
  freeze/ratification recommendation from the s207 critic + vote; the decision stays open — s208+ ratifies
  Q1/Q2/Q3 and may adopt or refine G8.)*
- Carry the standard fences: PREREG committed before any `F(p)` computation or model call; independent
  pre-run critic + one non-Anthropic vote at freeze; `ABORT_USD` on the swap arm; `predictions.md` row at
  freeze.
