---
type: design
id: blimp-forced-choice-sweep-v1
title: "BLiMP forced-choice sweep — a depth-stratified, HUMAN-ANCHORED grammatical-acceptability profile: does the panel's per-paradigm forced-choice accuracy track the per-paradigm human-agreement profile (and does error concentrate on the structurally-deep paradigms)? DESIGN, not frozen; three gates open"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: frozen
anchor: resource/blimp
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: resource/blimp
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: depends-on
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: theory/lexicon-grammar-continuum-v2
---

# Design v1 — BLiMP forced-choice sweep (program A3b)

**A design + decision-trail unit (program A3b — the standing unrun program unit: a selected-paradigm,
human-agreement-anchored forced-choice sweep of BLiMP). Status: DESIGN — three gates open, ratifiable
s205+.** This page operationalizes the depth axis of
[`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md)
against a **genuine human anchor** — the per-paradigm human-agreement rates BLiMP ships in
`raw_results/summary/human_validation_summary.csv` (verified firsthand this session; see *Grounding*).
Per PROTOCOL §3/§A1 and the A1b/adjective-antonymy precedent (design one session, ratify the next, run
after ratification): **design s204, ratifiable s205+, run after ratification.** A probe that opens a
value-laden decision is not run in the session that opens it.

> **This unit is HUMAN-ANCHORED, not internal-contrast-only — that is the point.** Almost every empirical
> unit of the last ~15 sessions (the relation-recovery / decoupling line, the antonymy-shadow line) has
> been `internal-contrast-only` (a within-model corpus contrast, no human key). BLiMP restores a
> first-class **human-comparison** line to the program: per-paradigm human forced-choice agreement is
> published, license-clear (CC-BY), and varies from ~0.47 to ~0.99 across paradigms — a real human
> difficulty *profile* the panel's own difficulty profile can be measured against. The anchor is a
> `resource` link to [`resource/blimp`](../../wiki/base/resources/blimp.md), not a `pending`/`internal`
> dodge (Gate Q3).
>
> **RATIFIED s205 (2026-07-10, autonomous cross-session adversarial review): Q1-B / Q2-A / Q3-A.**
> Fresh-agent reviewer (verdict authority) RATIFY-WITH-CONDITIONS + convergent fresh non-Anthropic vote
> (`gpt-5.4-mini`, $0.0025515); record
> [`decisions/resolved/blimp-forced-choice-sweep-design`](../../wiki/decisions/resolved/blimp-forced-choice-sweep-design.md)
> + [`REVIEW-ratify-s205.md`](../runs/2026-07-10-blimp-forced-choice-sweep/REVIEW-ratify-s205.md). The
> anchor is now earned (`anchor: resource/blimp`, human-comparison — the result page carries the
> `anchors: resource/blimp` typed link); `contingent-on` cleared. **Q1-B is realized by the maximal
> defensible whole-category rule** (every paradigm in the on-axis `linguistics_term` categories → **40
> paradigms**; off-axis categories excluded with structural reasons), which removes all within-stratum
> curation DoF and makes ρ_prof genuinely powered (n=40). **Added binding condition C8** (below): reading
> 1 is non-promotable without a training-frequency confound control; absent it, reading 1 runs but is
> **descriptive/directional only**. Frozen for the run s205 — see the run's `PREREG.md`; F2–F7 + C8 bind.

---

## Why this unit is owed now — and what makes the human anchor real

**A3b has sat unrun since the program was adopted (2026-07-02).** The resource has been catalogued since
2026-06-21 ([`resource/blimp`](../../wiki/base/resources/blimp.md)) with its license verified (CC-BY;
HuggingFace mirror `nyu-mll/blimp` = `cc-by-4.0`) and one paradigm file fetched + sha256-pinned. The
backlog names it as *"cheap and human-agreement-anchored … determiner–noun agreement near AANN; NPIs;
quantifiers."* Two things make it the right empirical pick this session:

1. **Two-track balance owes empirical** (s197/s200/s203 were philosophical/consolidation), and B1's
   promotion sweep is complete, and the within-noun empirical route is closed (s202). Of the tractable
   empirical picks, A3b is the one with a **verified, in-hand human anchor** (A6 needs a fresh
   license scout; A5 needs fresh corpus anchors per alternation).
2. **The human anchor is genuinely per-paradigm, not just the aggregate.** BLiMP's headline number is
   *aggregate* human agreement 96.4% — that alone would anchor only a single ceiling. But the repo ships
   **per-paradigm** human agreement in `raw_results/summary/human_validation_summary.csv` (columns
   `Condition,accepted,total_mean,count`; fetched + inspected firsthand this session, see *Grounding*).
   Per-paradigm human agreement varies from ~0.47 (`wh_questions_object_gap_long_distance`) to ~0.99
   (`transitive`, `left_branch_island_simple_question`) — a real human **difficulty profile**. That
   converts the unit from "how accurate is the panel" (a contamination-fragile absolute) into "does the
   panel's *difficulty profile* across paradigms track the *human* difficulty profile" (a
   contamination-robust relative), which is the load-bearing, defensible reading (Gate Q3).

BLiMP is the paradigm **formal-competence** benchmark in the field's own framing
([`source/mahowald-2024-dissociating`](../../wiki/base/sources/mahowald-2024-dissociating.md): formal vs
functional linguistic competence). The project already carries one formal-competence claim
([`claim/formal-competence-aann-ceiling`](../../wiki/findings/claims/formal-competence-aann-ceiling.md));
A3b broadens the formal-competence evidence from a single construction (AANN) to a **depth-stratified
sweep across grammatical phenomena**, with a per-paradigm human anchor the AANN line lacked at this
granularity.

## The two readings (one human-anchored, one internal-contrast)

On a depth-stratified subset of BLiMP paradigms (Gate Q1), run the panel in behavioral forced-choice
(Gate Q2) and measure:

1. **(PRIMARY — human-anchored) Profile alignment.** Per model, the Spearman correlation across the
   selected paradigms between (i) the model's per-paradigm forced-choice accuracy and (ii) BLiMP's
   per-paradigm human agreement (`total_mean`). **PROFILE-ALIGNED** = clearly positive on ≥2/3 models
   (the contrasts humans find hard — long-distance dependencies, islands, NPI scope — are also the ones
   the panel gets wrong): a shared difficulty structure between human and model grammatical judgment.
   **PROFILE-DIVERGES** = near-zero or negative on ≥2/3 (the panel's errors fall where humans are
   confident, or vice versa): the panel's grammatical difficulty structure is *not* the human one.
   Both are first-class. This is the **human-comparison** claim; the anchor is `resource/blimp`'s
   per-paradigm human agreement.
   - **Sub-reading 1a (absolute, contamination-bounded):** per-paradigm panel accuracy vs the human
     ceiling, reported as an **upper bound** (contamination inflates it; see Q3). Descriptive; never the
     headline.
2. **(SECONDARY — internal-contrast, shadow-depth) Depth gradient.** Within the panel (no human key),
   does forced-choice error concentrate on the **structurally-deep** paradigms (island effects, NPI
   scope, long-distance / distractor agreement) relative to the **locally-detectable** ones (adjacent
   determiner–noun and regular subject–verb agreement)? This is the BLiMP realization of the
   shadow-depth axis: adjacent-agreement contrasts are n-gram / local-window-detectable (shallow
   shadow); island and scope contrasts require structural representation the local co-occurrence
   statistics under-determine (deeper shadow). **DEPTH-GRADED** = mean accuracy on the shallow stratum
   clearly exceeds the deep stratum on ≥2/3 models. This stands even if the human anchor is coarse — it
   is a within-panel contrast.

**The two readings are distinct and must not be conflated.** Humans *also* find deep contrasts harder
(their agreement dips on islands / long-distance), so a panel depth-gradient (reading 2) partly *mirrors*
a human one. Reading 1 (profile alignment) is what separates "the panel is hard exactly where humans are
hard" (aligned) from "the panel has its own idiosyncratic difficulty structure" (diverges) — e.g. a
panel that aces islands (memorized) but stumbles on a locally-easy contrast would be DEPTH-flat yet
PROFILE-divergent. Report both; do not let a depth-gradient be read as profile-alignment.

## Grounding in the sources (verbatim, at their stated strength)

- **The dataset + aggregate human anchor (already in-repo):**
  [`resource/blimp`](../../wiki/base/resources/blimp.md) — *"BLiMP consists of 67 individual datasets,
  each containing 1,000 minimal pairs … human aggregate agreement with the labels is 96.4%."* License
  *"CC-BY … VERIFIED 2026-06-21."* Each pair is `(sentence_good, sentence_bad)` differing minimally in
  grammatical acceptability; the JSON schema (`sentence_good`, `sentence_bad`, `field`,
  `linguistics_term`, `UID`, `pairID`) was parsed firsthand at cataloguing.
- **The per-paradigm human anchor (verified firsthand THIS session — the fact that makes reading 1
  possible):** `https://raw.githubusercontent.com/alexwarstadt/blimp/master/raw_results/summary/human_validation_summary.csv`,
  fetched + inspected s204. Header row: **`Condition,accepted,total_mean,count`**. `Condition` = the
  per-paradigm UID; `total_mean` = the per-paradigm human agreement rate; `count` ≈ 97–100 human
  judgments/paradigm. Example rows (verbatim values): `determiner_noun_agreement_1` → total_mean
  **0.958** (count 97); `npi_present_1` → **0.83** (100); `only_npi_scope` → **0.72** (100); `wh_island`
  → **0.73** (100); `coordinate_structure_constraint_subject_extraction` → **0.514** (99). Range across
  paradigms ≈ **0.47–0.99**. *(The full per-UID table is re-fetched + sha256-pinned at freeze; the
  numbers above are the firsthand-inspected examples, not the frozen anchor — freeze re-verifies every
  UID used.)*
- **BLiMP = formal, not functional, competence (the framing):**
  [`source/mahowald-2024-dissociating`](../../wiki/base/sources/mahowald-2024-dissociating.md) — the
  formal/functional distinction; BLiMP is the formal-competence (grammatical well-formedness) benchmark,
  **not** an entailment / inference / implicature test (the resource page's sharp "what it cannot ground"
  limits are carried into the scope cap below).
- **The depth axis this operationalizes:**
  [`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md)
  (the continuum's single test sorts phenomena by how much is already written into co-occurrence) and
  [`theory/lexicon-grammar-continuum-v2`](../../wiki/findings/theory/lexicon-grammar-continuum-v2.md).

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Acceptability, not inference.** BLiMP contrasts **grammatical well-formedness**, never
   truth-conditional / entailment / implicature relations (resource page). No result here bears on the
   inferential or reference axes — only on the formal-competence / local-vs-structural-shadow reading.
2. **Contamination upper bound (the central caveat).** BLiMP is synthetic, published 2019, and very
   widely used in LM training + evaluation; its sentences are plausibly in the panel's pretraining data.
   **Absolute accuracy is therefore an upper bound, likely inflated by exposure** — never a headline
   number. The load-bearing readings are **relative**: the across-paradigm *profile* (reading 1) and the
   within-panel depth *gradient* (reading 2), both far more robust to a roughly-uniform memorization
   boost than any absolute per-paradigm accuracy (Gate Q3).
3. **n = 3 models; orderings/directions, not pooled coefficients.** Verdicts are directions on ≥2/3
   models. The profile Spearman is reported per model with its CI, never pooled across models.
4. **Behavioral forced-choice, not BLiMP's original logprob scoring.** BLiMP's paper scored LMs by
   probability comparison; the closed panel is logprob-free, so this is a **behavioral 2AFC** (present
   both, ask which is acceptable). Panel accuracy is therefore not directly comparable to the paper's
   published LM logprob accuracies — it is a **different measurement** (flagged, not smuggled). Position
   bias is a known 2AFC artifact and is controlled (Gate Q2).
5. **Selected paradigms, not the full 67.** v1 is a depth-stratified subset (Gate Q1). It cannot support
   a "BLiMP overall" score; a full sweep is a possible v2 if v1 warrants.
6. **English only; agreement-heavy coverage** (resource page). No cross-lingual reading.

## Panel & settings

Panel = the three [`config/models.md`](../../config/models.md) slots (`panel.A`/`.B`/`.C` — never
hardcode slugs); all three as subjects, cross-model divergence is data. Temperature 0, zero-shot,
single-turn, neutral system prompt. `google/*` gets `reasoning={"effort":"minimal"}` (config caveat) —
and, because forced-choice needs only a one-token answer, a low `max_tokens` with reasoning suppressed to
keep the gemini reasoning-token bill bounded (config Caveat 1). Every call records `usage.cost` via
[`experiments/lib/openrouter.py`](../lib/openrouter.py).

## Design — item scheme (fresh subsample of the selected BLiMP paradigms)

- **Items.** For each selected paradigm (Gate Q1), draw a **fresh, seed-fixed subsample of N ≈ 100–120
  minimal pairs** from that paradigm's 1,000 (PROTOCOL §4 powered N; re-fetched from the repo `data/`
  dir + sha256-pinned at freeze, CC-BY recipe-not-corpus). Each item = `(sentence_good, sentence_bad)`.
- **Elicitation (Gate Q2, default Q2-A).** Present the two sentences as an unlabelled pair ("Sentence 1
  / Sentence 2") and ask, with a neutral fixed instruction, **which is the more grammatically acceptable
  sentence of standard written English (answer 1 or 2)**. Run each item in **both presentation orders**
  (good-first and good-second) to net out position bias; record the order-flip rate as a diagnostic.
- **Scoring.** Per item, the model is **correct** if it selects `sentence_good`. Two scored quantities,
  both pre-registered: (a) **order-averaged accuracy** (mean over the two orders); (b) **consistency
  accuracy** (correct only if it picks `sentence_good` in *both* orders — the position-bias-hardened
  variant). Per-paradigm accuracy = mean over that paradigm's items. Reading-1 Spearman and reading-2
  strata use quantity (a) as primary and (b) as the robustness check (both frozen).
- **Depth strata (Gate Q1).** Each selected paradigm is assigned, **at freeze, before any model call**,
  to one of the pre-registered depth strata (shallow-local / medium / deep-structural) by a written,
  paradigm-agnostic rule (locality of the licensing dependency), never post-hoc to fit the accuracies.

## GATE Q1 — the paradigm set + the depth axis

Which BLiMP paradigms enter the sweep, and how they are stratified for the depth reading. The choice
trades program-relevance (the AANN-adjacent agreement family), depth-spread (enough range to test
readings 1 and 2), and cost.

- **Q1-A — AANN-adjacent agreement family only** (the 8 determiner–noun agreement paradigms, ± the
  regular/irregular subject–verb agreement paradigms). Tightest program link (AANN), but **no depth
  spread** — all local agreement, so reading 1's profile Spearman is over near-identical human-easy
  paradigms (all `total_mean` ≈ 0.95+) and reading 2 has no deep stratum. Rejected: cannot carry either
  headline reading.
- **Q1-B (provisional default) — a depth-stratified set of ~9–12 paradigms spanning four strata**, each
  with a published per-paradigm human agreement:
  - **shallow-local:** `determiner_noun_agreement_1`, `determiner_noun_agreement_with_adjective_1`
    (the AANN-adjacent family), `regular_plural_subject_verb_agreement_1`;
  - **medium (agreement across intervening material):** `distractor_agreement_relational_noun`,
    `distractor_agreement_relative_clause`;
  - **deep-scope (NPI / quantifier licensing):** `npi_present_1`, `only_npi_scope`,
    `sentential_negation_npi_scope`, `existential_there_quantifiers_1`;
  - **deep-structural (islands / long-distance):** `wh_island`, `adjunct_island`,
    `coordinate_structure_constraint_subject_extraction`.
  the ~10 paradigms listed above are the *seed* of the set; **the s204 pre-run critic raised the floor
  to ≥16 paradigms** (F2) — a per-model Spearman over ~10 points is badly under-powered (at n≈10 a ρ of
  +0.4 is indistinguishable from 0), so the freeze must expand toward the top of the range / beyond and
  state the achieved-n power in PREREG, or reading 1 is descriptive-only. Every listed paradigm has a
  per-paradigm human agreement in the now-committed `human_validation_summary.csv` (the example values
  above are verbatim from it). **The exact final list (≥16) + the shallow/medium/deep assignment are
  frozen in PREREG before any model call, by a structural locality rule independent of the
  human-agreement values (F6).** Cost is bounded (§Cost).
- **Q1-C — the full 67-paradigm sweep.** Most complete; supports a genuine "BLiMP overall" panel score.
  But ~5.6× the calls of Q1-B, dilutes the depth-axis focus with off-theme categories (binding,
  ellipsis, irregular forms, control/raising), and pushes cost toward / past the prefer-split flag.
  **Rejected for v1** (a full sweep is a clean v2 if v1's profile reading warrants it) — but a reviewer
  may prefer it if the depth-axis subset is judged too curated (a fishing risk; see *why value-laden*).

**Why value-laden.** The paradigm set *is* the instrument: a curated depth-stratified subset (Q1-B)
makes readings 1 and 2 sharp but invites a "you picked the paradigms that make the story" objection — so
Q1-B must pre-commit the full list and the stratum assignment **by a written locality rule, before any
model call**, and report the subset honestly as a selected, not exhaustive, sweep. The full sweep (Q1-C)
removes the curation objection at the cost of focus and spend. This is the central choice.

## GATE Q2 — forced-choice elicitation + position-bias control

The panel is logprob-free, so BLiMP's original probability-comparison scoring is unavailable; the
behavioral analog is a 2AFC, whose known artifact is position bias.

- **Q2-A (provisional default) — behavioral 2AFC, BOTH presentation orders per item, position-bias
  netted.** Present the pair, ask which is more acceptable (answer 1/2), run good-first and good-second,
  score order-averaged (primary) + consistency (robustness), report the order-flip rate. Pays 2× calls
  to net out a known, large 2AFC artifact that would otherwise confound the per-paradigm profile.
- **Q2-B — single fixed-random order per item** (half the calls). Cheaper, but uncontrolled position
  bias contaminates per-paradigm accuracy and could masquerade as a profile signal. Rejected as default
  (the project controls for exactly this class of artifact).
- **Q2-C — isolated absolute acceptability rating** (present each sentence alone, rate acceptable/not or
  1–5, then compare within pair). Rejected: discards BLiMP's minimal-pair within-item contrast (its whole
  design), and absolute ratings are noisier + scale-biased.

**Why value-laden.** The format fixes what "accuracy" means and whether a known artifact confounds the
headline profile. Q2-A is the rigorous default; the 2× call cost vs Q2-B is a real trade the reviewer
weighs.

## GATE Q3 — contamination scope + the anchor declaration

BLiMP is synthetic and widely trained on. What may the result claim, and against what anchor?

- **Q3-A (provisional default) — report the RELATIVE profile (reading 1) + depth gradient (reading 2)
  as the load-bearing findings; absolute accuracy as a contamination upper bound; anchor =
  HUMAN-COMPARISON via [`resource/blimp`](../../wiki/base/resources/blimp.md)'s per-paradigm human
  agreement.** Rationale: memorization from exposure inflates absolute accuracy roughly *uniformly*
  across paradigms, so the *relative* difficulty ordering (and its alignment with the human profile) is
  far more robust than any absolute number. The profile-alignment claim (reading 1) is a genuine
  human-comparison claim; the depth-gradient (reading 2) is within-panel internal-contrast. The result
  page carries an `anchors:` link to `resource/blimp`; it is **not** `internal-contrast-only`.
- **Q3-B — add a lexical-perturbation contamination control:** re-instantiate each item with novel
  open-class content words (from a controlled list) so exact-string memorization cannot help, and compare
  accuracy on original vs perturbed. Stronger contamination handling, but template re-instantiation
  risks breaking grammaticality (needs re-validation), adds substantial build cost, and BLiMP's
  vocab-controlled templates are not trivially re-runnable without the original generation code.
  Attractive as a **v2 upgrade** or a bounded content-word-swap arm; weighed at ratification against the
  scope it adds to v1.
- **Q3-C — decline the unit: BLiMP accuracy is uninterpretable under contamination.** Rejected as
  over-cautious: the relative profile / depth readings are robust to a uniform memorization boost, and a
  human-anchored grammatical-competence profile is worth having with the caveat stated. Declining
  forfeits the program's one in-hand human-anchored grammatical line.

**Why value-laden.** Whether the unit anchors a human-comparison profile claim despite contamination
(Q3-A), invests in a perturbation control (Q3-B), or declines (Q3-C). The default trusts the *relative*
profile while flagging *absolute* numbers as an upper bound — and, importantly, declares a **real human
anchor** rather than retreating to internal-contrast-only.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

Let `acc(m, p)` = model m's order-averaged forced-choice accuracy on paradigm p; `H(p)` =
BLiMP per-paradigm human agreement (`total_mean`). ρ_prof(m) = Spearman over the selected paradigms of
`acc(m, ·)` vs `H(·)`.

- **Reading 1 (verdict-bearing, human-anchored) — PROFILE-ALIGNED** iff ρ_prof(m) is **clearly positive**
  (band frozen at freeze, e.g. > +0.4) on **≥2/3** models. **PROFILE-DIVERGES** iff ρ_prof(m) is
  **near-zero or negative** (e.g. < +0.2) on ≥2/3. The **[+0.2,+0.4] middle band is a pre-registered
  INCONCLUSIVE** outcome (no uncovered dead-zone; exact bands fixed before any model call). **Power
  (F2):** the bands are calibrated to the achieved paradigm-count n at freeze (≥16); if n is too small
  to distinguish the bands, reading 1 is reported **descriptively with its CI** and is **non-promotable
  on this run alone**.
- **Reading 2 (verdict-bearing, STRICTLY within-panel / internal-contrast) — DEPTH-GRADED** iff mean
  `acc` on the shallow-local stratum **exceeds** the deep (islands + NPI-scope) stratum by a
  pre-registered margin on ≥2/3 models; **DEPTH-FLAT** iff not. This uses **no human key** — purely the
  panel's own shallow-vs-deep accuracy gap. Subject to F4 (sub-0.6-agreement paradigms are excluded from
  the accuracy strata, kept only in reading 1's profile Spearman).
- **Reading 2h (human-anchored sub-reading, split out per F5) — EXCEEDS-HUMAN-DIP** iff the panel's
  shallow-minus-deep accuracy gap is **larger** than the human shallow-minus-deep agreement gap on ≥2/3
  models (the panel finds the deep contrasts *disproportionately* harder than humans do); **TRACKS-DIP**
  iff comparable. Because it references `H(p)`, this is a **human-comparison** quantity and is reported
  under the human-anchored umbrella, never under the internal-contrast label (F5).
- **Pre-named nulls (first-class):** ρ_prof near-zero (panel difficulty structure unrelated to the human
  one); DEPTH-FLAT (the panel is uniformly at ceiling / floor, e.g. contamination saturates every
  paradigm — itself an informative contamination signal); or a **position-bias blowout** (order-flip
  rate so high that consistency accuracy collapses) — pre-registered as an INSTRUMENT-FAILURE outcome
  that voids the accuracy readings and is reported as such, not silently dropped.
- **Saturation/range guard (F3):** if a model's across-paradigm accuracy **variance is near zero** (all
  paradigms near ceiling), ρ_prof(m) is computed over near-constant values = noise → reported as
  **INCONCLUSIVE**, not a coefficient. Per-model absolute-accuracy dispersion is reported as a
  contamination diagnostic (a frequency-driven pseudo-alignment vs a structural one).
- **Anti-cheat fence (PROTOCOL §B):** the paradigm list, the stratum assignment, the subsample seed +
  N, the elicitation prompt + both orders, the ρ_prof bands, and the depth-margin threshold are **all
  frozen in `PREREG.md` before any model call**. No band, stratum, or paradigm is added/dropped after
  accuracies are seen. PROFILE-DIVERGES, DEPTH-FLAT, and the nulls are pre-named first-class results.

## Cost (pre-flight estimate)

Forced-choice, one-token answers, temperature 0. Q1-B ≈ 10 paradigms × ~110 items × 2 orders × 3 models
≈ **6,600 calls**; prompt ≈ 90–130 tokens (two short sentences + instruction), completion ≈ 1–5 tokens.
At the corrected rate card (`openrouter.py`: claude 3/15, gpt-mini 0.75/4.5, gemini 1.5/9 per MT) that
is **≈ $0.6–1.6** across the panel (claude ≈ $0.5, gpt-mini ≈ $0.1, gemini the wildcard — reasoning
suppressed to hold it near estimate). Inside one UTC day's $5 cap; **near enough to the $2.50 prefer-split
flag with gemini's reasoning-token risk that PREREG must (a) suppress/cap gemini reasoning and (b)
pre-register a split into two half-sweeps (shallow+medium paradigms, then deep) if the re-estimate at
freeze exceeds $2.50.** A hard `ABORT_USD` (≈ $2.0) goes in `probe.py` at freeze. Re-estimated at freeze
once the paradigm list + N + orders are fixed.

## What each outcome feeds

- **PROFILE-ALIGNED:** a human-anchored finding that the panel's grammatical difficulty structure tracks
  the human one across phenomena — a broad, human-comparison counterpart to the single-construction
  formal-competence line
  ([`claim/formal-competence-aann-ceiling`](../../wiki/findings/claims/formal-competence-aann-ceiling.md)).
  A candidate row for the shadow-depth reading and, if it replicates, a promotion-review target.
- **PROFILE-DIVERGES:** a first-class negative — the panel's grammatical judgments are hard/easy on
  *different* phenomena than humans; cautions any "formal competence mirrors human competence" reading
  and sharpens the formal/functional dissociation.
- **DEPTH-GRADED (beyond the human dip):** a within-panel realization of the shadow-depth axis on
  grammatical phenomena — error concentrates where the contrast is structurally deep / n-gram-invisible;
  feeds [`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md)
  and the continuum theory with a grammar-side gradient.
- **DEPTH-FLAT / contamination-saturated:** an informative contamination result — memorization saturates
  even the structurally-deep contrasts; the accuracy readings are voided and the contamination caveat is
  the finding.
- **Registers a [`predictions.md`](../../wiki/predictions.md) row** at **freeze** (a probe-specific
  profile-alignment / depth-gradient bet); outcome updated the run session.

## Handoff (what s204 did, and what remains)

1. **s204 (this session):** wrote this design; **verified AND committed the per-paradigm human anchor**
   (`experiments/data/blimp/human_validation_summary.csv`, sha256 `ea0e7c21…`) and extended
   [`resource/blimp`](../../wiki/base/resources/blimp.md) with the per-paradigm profile (discharging the
   critic's Blocker 1 / F1); opened
   [`decisions/open/blimp-forced-choice-sweep-design`](../../wiki/decisions/open/blimp-forced-choice-sweep-design.md)
   (Q1–Q3, provisional defaults Q1-B / Q2-A / Q3-A); ran the design pre-run critic (fresh agent) + one
   non-Anthropic decorrelation vote (recorded under
   [`experiments/runs/2026-07-10-blimp-forced-choice-sweep-design/`](../runs/2026-07-10-blimp-forced-choice-sweep-design/)).
   **Nothing frozen, nothing run.**
2. **Ratify (s205+):** fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** write `prep.py` (re-fetch the selected paradigm `.jsonl` files +
   `human_validation_summary.csv`, sha256-pin; fresh seeded subsample; both-order item build) + `probe.py`
   (forced-choice, both orders, `usage.cost`) + `analyze.py` (per-paradigm accuracy, ρ_prof, depth
   strata, order-flip diagnostic); fix the paradigm list + stratum assignment + N + ρ-bands +
   depth-margin; commit PREREG before any model call; independent pre-run critic + one non-Anthropic
   vote; `ABORT_USD` set; gemini reasoning suppressed.
4. **Run (after freeze)** on the panel; post-run verifier recomputes every figure from raw. Powered N per
   PROTOCOL §4.

## Freeze-time conditions (bind the freeze session; from the s204 pre-run review — honor all at freeze)

From the s204 fresh-agent pre-run critic (verdict authority; **GO-WITH-CONDITIONS**, no NO-GO, no
fabrication) + the non-Anthropic decorrelation vote (`gpt-5.4-mini`, GO-WITH-CONDITIONS, convergent on
Q1-B/Q2-A/Q3-A), recorded in
[`REVIEW-design-s204.md`](../runs/2026-07-10-blimp-forced-choice-sweep-design/REVIEW-design-s204.md) +
[`VOTE-s204.json`](../runs/2026-07-10-blimp-forced-choice-sweep-design/VOTE-s204.json). The critic
raised three blockers the vote missed; **F1 is discharged this session**, F2–F7 bind the freeze:

- **F1 (BLOCKER — DISCHARGED s204).** *"The per-paradigm human anchor is not in the repo."* The critic
  grepped and found the per-paradigm numbers only in this design / the decision / `program.md`, not in
  `resource/blimp.md` (which carried only the aggregate 96.4%) — so the `anchors: resource/blimp`
  declaration over-read the resource. **Fixed this session:** `human_validation_summary.csv` fetched +
  **committed** (`experiments/data/blimp/human_validation_summary.csv`, 3,057 bytes, sha256
  `ea0e7c21de6b9df2fd8a94d0b175e84ea57627e4cbfa1fcba4ef8b3d0fba1b2d`, 69 rows), and
  [`resource/blimp`](../../wiki/base/resources/blimp.md) extended with a *"Per-paradigm human agreement"*
  subsection cataloguing the columns, the 0.47–0.99 range, and every UID this design cites. The anchor
  is now genuinely in-repo; the Q3-A `anchors: resource/blimp` declaration is *earned* once Q3 ratifies.
  (The design keeps `anchor: pending` until the Q3 gate ratifies s205+.)
- **F2 (BLOCKER — power).** The PRIMARY reading is a Spearman over the selected paradigms; at n≈10 a
  ρ_prof of +0.4 is not distinguishable from 0 (the ~0.05 two-sided threshold at n=10 is ρ≈0.64).
  **Freeze ≥16 paradigms** across the four strata (or adopt Q1-C, the full 67), and **state the
  achieved-n power for ρ_prof in PREREG**. If n stays low, reading 1 is **descriptive/directional
  only** (report ρ with its CI, framed "consistent with alignment/divergence"), **never a decided
  PROFILE-ALIGNED claim, and non-promotable to a `claim` on this run alone.** *(This raises Q1-B's floor
  from the "~9–12" first draft to ≥16; the decision page's Q1 carries the condition.)*
- **F3 (BLOCKER — contamination uniformity).** The "memorization inflates uniformly, so the relative
  profile is robust" premise is load-bearing and untested; if exposure correlates with human-ease
  (frequent local-agreement constructions are both human-easy *and* most memorized) it inflates ρ_prof
  **spuriously**. Pre-register a **saturation/range guard:** if a model's across-paradigm accuracy
  variance is near zero (all near ceiling), ρ_prof(m) is **INCONCLUSIVE**, not a coefficient. Report
  per-model absolute-accuracy dispersion as a contamination diagnostic.
- **F4 (SHOULD-FIX — gold reliability).** Low-human-agreement paradigms have contested gold labels
  (e.g. `coordinate_structure_constraint_subject_extraction` human 0.514 ≈ chance). Set a
  **human-agreement floor ≈0.6** for paradigms entering the reading-2 *accuracy* contrast; sub-floor
  paradigms stay in the reading-1 profile Spearman but are reported **descriptively**, since "accuracy"
  against a shaky key is not grammatical competence.
- **F5 (SHOULD-FIX — label integrity; applied in-design this session).** The reading-2 "exceeds the
  human dip" quantity uses `H(p)`, so it is **not** internal-contrast. Applied above: reading 2 is kept
  **strictly within-panel** (shallow-vs-deep accuracy gradient, no human baseline), and the
  "excess-over-the-human-dip" comparison is moved under a **human-anchored sub-reading (2h)** in the
  verdict map. No human-baselined quantity wears the internal-contrast label.
- **F6 (panel-vote + critic condition).** Publish the final **selected** paradigms **and the excluded
  ones with reasons**, plus the paradigm→stratum mapping, in PREREG **before any model call**, decided
  **solely on syntactic/structural (locality) criteria with no reference to expected model performance
  or to the human-agreement values** (keeps reading 1 and the depth stratification independent — the
  vote's load-bearing condition).
- **F7 (recommended, not blocking).** Add a **bounded content-word-swap contamination arm** on 2–3
  paradigms (one shallow, one deep) — swap open-class content words from a controlled list, re-check the
  minimal contrast survives, compare original-vs-swapped accuracy — turning "we assume uniform
  inflation" into "we checked whether swapping surface strings moves accuracy."
- Carry the design's own fences: gemini reasoning suppressed/capped; a hard `ABORT_USD`; **split into
  two half-sweeps if the freeze re-estimate exceeds $2.50** (a hard rule keyed to the re-estimate, not a
  "must consider"); PREREG committed before any model call; independent pre-run critic + one
  non-Anthropic vote at freeze.
- **C8 (BLOCKER — added s205 ratification; the fresh reviewer's promotion-blocking condition).** The
  PRIMARY reading-1 verdict (PROFILE-ALIGNED) is **non-promotable to a `claim`** unless a
  training-frequency confound has been controlled — because non-uniform, human-agreement-correlated
  contamination (frequent local-agreement constructions being *both* human-easy *and* most-memorized;
  rare island/scope contrasts *both* human-harder *and* less-memorized) can inflate ρ_prof by a
  training-frequency artifact **with perfectly healthy across-paradigm variance, which F3 does not
  catch**. Satisfy C8 by **either** the F7 content-word-swap arm on ≥2 shallow + ≥2 deep paradigms
  (original-vs-swapped accuracy, pre-registered), **or** a pre-registered corpus-frequency covariate for
  each construction partialled from ρ_prof — decided and frozen in PREREG before any model call. **Absent
  either, reading 1 may run and be reported descriptively/directionally only** (exactly the F2 low-n
  downgrade), and promotion waits on a later session that adds the control. **Symmetric-F2 binding
  reading:** descriptive-only vs promotable status is fixed at freeze by the achieved-n power calc,
  applied identically regardless of the observed sign of ρ_prof — so a PROFILE-DIVERGES null is a
  first-class descriptive null, never a quietly-invoked escape hatch. *(s205 realization: this run
  defers the C8 control — reading 1 is descriptive/directional + non-promotable-on-this-run; a
  per-paradigm absolute-accuracy dispersion contamination diagnostic is reported. The verdict-bearing
  outputs this run are reading 2 (within-panel depth gradient) and reading 2h (human-anchored
  excess-over-dip); the C8 frequency control is the pre-registered next step for a promotion-prep
  session.)*
