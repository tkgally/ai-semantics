---
type: claim
id: lexical-sense-gradience
title: "On 200 DWUG EN within-period usage pairs, the panel's graded sense-relatedness rating rank-tracks the human DURel median (Spearman 0.60–0.83, in/above the human inter-annotator range) and the monotonic signal survives partialling the model's own topic-similarity rating — a powered, human-anchored lexical shadow-beater, cross-date replicated 3/3 on fresh pair-disjoint items (single-run flag discharged), promoted at direction/agreement scope"
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: supported
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-07-04
updated: 2026-07-05
links:
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-sense-gradience-rep2
  - rel: supports
    target: conjecture/lexical-sense-gradience
  - rel: supports
    target: theory/shadow-depth-table-v1
  - rel: supports
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Claim: the panel's graded sense-relatedness rating rank-tracks the human DURel median and beats the model's own topic shadow — lexical, behavioral, single-run

> **Status: supported (PROMOTE-SCOPED) — 2026-07-04, session 176.** Cross-session, independent,
> adversarial claims-promotion review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item B1) of the
> lexical sense-gradience monotonicity line —
> [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) (run
> 2026-05-30, the project's first lexical result and first own-design result with a real human anchor). The
> reviewer did not produce the result. It promotes **only** the conjecture's central bet — clauses
> (a) monotonic graded-sense tracking + (c) survives the context/topic shadow — of
> [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md). It does **not**
> touch the conjecture's distinctive bet (clause b, polysemy as a discrete regime *beyond* graded
> distance), which is a separate **powered null**
> ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)) and stays
> unpromoted.
>
> **Why SCOPED, not full-scope.** Unlike the two lines promoted before it —
> [`claim/comparative-correlative-covariation`](comparative-correlative-covariation.md) (three runs +
> a powered re-run on fresh disjoint items) and
> [`claim/dative-information-structure-givenness`](dative-information-structure-givenness.md) (v1 + v2 +
> powered, all disjoint items) — **this result's specific instrument-and-control combination has been
> run exactly once** (one date, one temperature-0 draw). The `durel`/`cont` dual framing is a
> **within-run instrument robustness** check, **not** a fresh-item replication; and the load-bearing
> shadow-beater (the model-internal topic partial) is a **single computation**. So the claim is
> promoted at **direction + agreement** scope, with **magnitudes stated with their intervals but
> explicitly flagged single-run**, mirroring the corpus's practice of promoting single-primary-run
> results only when scoped tightly and anchored properly
> ([`claim/lexical-graded-scale-ungraded-commitment`](lexical-graded-scale-ungraded-commitment.md),
> the sibling lexical claim; [`claim/relational-order-sensitive-reassignment`](relational-order-sensitive-reassignment.md)).
> The direction/agreement core is stronger than that sibling on **power** (N=200) and **human
> anchoring** (a graded human IAA comparison) and weaker on **multi-instrument corroboration** — the
> trade the scope records.
>
> *(Decorrelation note, [`PROTOCOL.md §3`](../../../PROTOCOL.md)/§2: the owed non-Anthropic panel vote
> was routed by the orchestrator via the probe REST path — `openai/gpt-5.4-mini`, cutoff-aware preamble,
> `usage.cost` $0.003639 for both s176 promotion votes combined — and returned **PROMOTE-SCOPED**,
> converging with this fresh-agent verdict and endorsing the same single-run, direction/agreement scope.
> Convergence is comfort; no divergence to weigh.)*

> **Update — 2026-07-05, session 181: the single-run flag is DISCHARGED for the direction/agreement
> core (cross-date replicated 3/3).** The owed A2a re-run landed —
> [`result/lexical-sense-gradience-rep2`](../results/lexical-sense-gradience-rep2.md): the **byte-frozen
> instrument** on **200 fresh DWUG pairs drawn disjoint from v1** (0 shared pairs; 61/357 usages
> recombine — pair-disjoint, not usage-disjoint), fresh date, seed 20260705. **Every rep2 base ρ falls
> within v1's 95% CI and every CI overlaps** (claude durel 0.679→0.715, cont 0.696→0.739; gpt 0.601→0.528,
> 0.675→0.631; gemini 0.804→0.808, 0.825→0.801), and the **topic-partial shadow-beater survives 3/3 on
> both framings** (partial\|topic 0.60/0.39/0.66 durel, 0.64/0.51/0.64 cont). 1800 calls, 0 NA,
> **$0.68507** (far below v1's $3.134 — gemini's reasoning burn was an anomaly, not a fixed cost).
> Fresh-agent post-run verifier **REPRODUCED (0 discrepancies, max abs diff 0.0005 / 24 stats)**; pre-run
> fresh-agent critic (NO-GO on a frozen-probe input-path bug, fixed + smoke-tested) + non-Anthropic vote
> GO-WITH-CONDITIONS. **What this discharges:** the *single-run* caveat on the **direction/agreement**
> core — the graded ρ vs the DURel median and its survival of the topic partial are now cross-date
> replicated, not one draw. **What it does NOT upgrade** (pre-run critic C1 + vote): this is **cross-date
> stability of the same instrument on fresh pairs from the same finite corpus** — **not** two fully
> independent draws, **not** a twice-powered independent magnitude, **not** a representational or broad
> "model understanding" reading. The scope stays direction/agreement; gpt remains the weakest,
> most-elicitation-sensitive corner (ordinal durel 0.528, partial\|topic 0.392 — down from v1, still
> positive/non-collapsing, CI overlaps). Full-scope, magnitude-vs-human promotion still not licensed.

## Statement

Across **200 DWUG EN within-period usage pairs** of the same target word (50 per rounded human DURel
level 1–4, 43 CCOHA lemmas, synchronic, ≥2-annotator human gold), all three ratified panel models
(`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`) rate the graded sense-relatedness of the two
usages so that **their rating rank-correlates positively with the human DURel median** — a graded,
monotone signal, not a near-binary same/different collapse. The correlation is robust across an
ordinal (`durel`) and a continuous (`cont`) prompt framing, its bootstrap 95% intervals are well clear
of zero, and the panel's agreement with the human median sits **in or above the published human
inter-annotator range** for DWUG EN. The monotonic signal **survives partialling out the model's own
topic-similarity rating** (the lexical analogue of the constructional distributional shadow) — modestly,
and by a **model-internal, single-run** control.

The claim is **scoped to a direction-and-agreement statement**, and every qualifier below is
load-bearing:

- **Direction + agreement, not magnitude-vs-human.** What is supported is that the panel orders usage
  pairs by human-rated sense-relatedness (the direction) and does so at an agreement level in/above the
  human–human range (the calibration). The per-model correlation **magnitudes** are stated **with their
  95% intervals but flagged single-run** — they are one draw, not a replicated or twice-powered
  magnitude, and they are **not** compared to any human effect size.
- **`referential.sense`, not reference or representation.** The graded signal is over *usage
  similarity* as an operational stand-in for *sense relatedness* (`referential.sense`), recovered
  through the model's distributional behavior. It is **behavioral** — what the models *do* — and is
  **not** evidence of graded sense *representations*.
- **The central bet only.** This promotes clauses (a)+(c) of the conjecture. The distinctive clause
  (b) — that polysemy is handled as a *discrete regime beyond graded distance*, absent for homonyms —
  is a separate, adequately-powered **null**, disclaimed below.

## Grounds

One own-design result, independently re-verified from raw JSON (the result page records the recompute
as **CLEAN**). 1800 calls, 0 NA; cost $3.134 billed. Read the **orderings, the CIs, and the surviving
partials** below, not a pooled scalar; the point estimates are per model,
`claude-sonnet-4.6` / `gpt-5.4-mini` / `gemini-3.5-flash`.

Spearman ρ of the model's sense-relatedness rating against the human DURel median, per framing, with a
bootstrap 95% CI; the partial ρ controlling for the model's own topic-similarity rating; and the
model's internal sense–topic correlation, all quoted verbatim from
[`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md):

| model | `durel` ρ (95% CI) | `cont` ρ (95% CI) | partial ρ \| overlap (durel/cont) | partial ρ \| topic (durel/cont) | ρ(sense, topic) (durel/cont) |
|---|---|---|---|---|---|
| `claude-sonnet-4.6` | 0.679 (0.59–0.75) | 0.696 (0.61–0.78) | 0.67 / 0.69 | 0.52 / 0.54 | 0.64 / 0.68 |
| `gpt-5.4-mini` | 0.601 (0.49–0.69) | 0.675 (0.58–0.75) | 0.59 / 0.66 | 0.50 / 0.58 | 0.46 / 0.52 |
| `gemini-3.5-flash` | **0.804 (0.75–0.85)** | **0.825 (0.76–0.87)** | 0.80 / 0.82 | 0.73 / 0.75 | 0.56 / 0.59 |

- **The direction holds for every model on both framings.** All six correlations are positive with
  intervals clear of zero (the lowest bound is `gpt-5.4-mini`'s 0.49). `gemini-3.5-flash` (0.80–0.83)
  is the strongest, `claude-sonnet-4.6` (0.68–0.70) is closest to the human–human agreement, and
  `gpt-5.4-mini` (0.60–0.68) is the weakest.
- **The per-human-level means are cleanly monotone.** The result page reports, e.g.,
  `claude-sonnet-4.6` under the `cont` framing rising **18.2 → 21.1 → 31.6 → 36.0 → 50.1 → 76.1 → 80.3**
  across human levels 1.0 → 4.0 — a graded gradient, not a step function.
- **The dual framing agrees; the one instrument-sensitive model is `gpt-5.4-mini`.** It is noisier
  under the *ordinal* DURel framing (ρ 0.60, mid-level means non-monotonic) but cleaner under the
  *continuous* framing (ρ 0.68) — the lexical reappearance of the instrument-sensitivity pattern the
  project tracks on the grammatical side. The dual framing is a **within-run** robustness check; it is
  **not** counted as a replication (see *Bounds*).
- **Convergent, cross-anchor support for the direction (clause a) — not a replication of this
  instrument.** A later run on a homonymy-enriched WiC noun subset
  ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)) found the
  rating separates same/different sense at ceiling-ish AUC 0.78–0.91 in *both* strata, which
  independently re-confirms clause (a) on fresh items and a different anchor; and the bridging-context
  run underlying [`claim/lexical-graded-scale-ungraded-commitment`](lexical-graded-scale-ungraded-commitment.md)
  shows the within-item graded *scale* replicates. These corroborate the **phenomenon**; they do **not**
  re-run this claim's specific instrument (graded ρ vs the DURel median with the topic partial), which
  remains single-run.

## Human-comparison leg (agreement / direction only — NOT per-item, NOT magnitude-vs-human)

The human anchor is [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (DWUG EN
v3.0.0), the largest resource of *"graded contextualized, diachronic word meaning annotation in four
different languages, based on 100,000 human semantic proximity judgments"* (Schlechtweg et al. 2021,
EMNLP; abstract quoted verbatim on the resource page). What it grounds here is precise and narrow:

- **The graded human signal itself.** DWUG's DURel annotation scale is, verbatim, *"4: Identical,
  3: Closely Related, 2: Distantly Related, 1: Unrelated"* over pairs of usages of the **same target
  word**, and the resource page records the paper's note that *"annotators make frequent use of the
  intermediate levels of the scale ('2','3') and thus assign graded distinctions of word meaning"* —
  i.e. the human gold is genuinely graded, which is exactly the property the monotonicity clause needs
  and which no binary set (WiC) supplies.
- **The inter-annotator range the panel is compared against.** For DWUG EN the resource page records,
  VERIFIED from the primary Table 3, *"Annotator agreement: Spearman ρ = 0.69 (SPR column),
  Krippendorff's α = 0.61 (KRI column) for English"* over **9 total annotators for English**. The panel
  lands **in or above** that ρ ≈ 0.69 human–human range (`claude` ≈ at it, `gemini` above it, `gpt`
  just below/at its lower framing). This is the whole human-comparison force of the claim: the panel's
  agreement with the human median is not distinguishable-downward from, and for one model exceeds, the
  humans' agreement with each other.

**What the anchor does NOT ground, and the claim therefore does not assert:**

- **Not a strict equivalence of quantities.** As the result page states, *"the 'in/above human
  inter-annotator range' comparison references the published EN agreement (ρ 0.69); model-vs-median and
  annotator-vs-annotator are related but not identical quantities."* The in/above-IAA statement is a
  **rough calibration**, not a claim that the two ρ's measure the same thing.
- **Not a per-item human comparison.** 151/200 pairs rest on only 2 annotators (the half-integer levels
  are 2-rater disagreements, *not* treated as reliable graded gold); the anchor grounds an
  **aggregate/direction** comparison, never a per-item one.
- **Not a magnitude-vs-human.** DWUG carries no human "how strongly should sense track" effect size, so
  the panel's correlation magnitude is a within-run quantity, not a human-comparison of sizes.

## The control that earns the rigor (the topic-similarity partial = the shadow-beater)

The claim's interest over "distributional similarity tracks human usage similarity" (nearly a given —
[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) deems an *outright*
null *"least likely given how well distributional models do on same/different sense tasks"*) rests entirely on **clause (c): the graded signal is not merely the
model tracking how similar the two *sentences* are.** Two controls bear on it, and the claim states
each at exactly its strength:

- **Lexical-overlap partial (rules out only the *surface* shadow).** DWUG's same-lemma usage sentences
  barely share content words, so surface overlap is near-degenerate in this sample; partialling it
  changes ρ by ≤ 0.02 (`partial ρ | overlap` above). This rules out a crude surface-string shadow *a
  priori* — a weak control, and the claim leans on it only for that.
- **Topic-similarity partial (the real shadow-beater) — survives, modestly, single-run,
  model-internal.** The stronger test partials out the model's **own** topic/situation-similarity
  rating (elicited to *ignore* the target word). The correlation **substantially survives**:
  `partial ρ | topic` = **0.52 / 0.50 / 0.73** on the `durel` framing (0.54 / 0.58 / 0.75 on `cont`),
  down from the base 0.68 / 0.60 / 0.80 but clearly positive and non-collapsing for all three models.
  So the sense signal carries rank information about human sense-relatedness **beyond** the model's
  perception of context similarity.

This is stated as **modest** support, exactly as the result page frames it: *"A surviving `partial|topic`
is modest positive support that the sense signal isn't merely echoed context similarity; it is not a
fully independent control, and a collapse would have been ambiguous (sense and topic are genuinely
correlated across items)."* It is a **model-internal** control (both ratings come from the same model,
so it cannot exclude a shared model idiosyncrasy the way a matched-material or by-construction control
can), and it is a **single computation** on one draw. The claim does **not** upgrade it to "cleanly
separates sense from topic."

## Where it sits

- **The project's lexical shadow-beater.** In the flagship
  [`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md) this is the **"Lexical sense
  gradience"** beater row, **form (ii) partialled correlation** — a model–human gradient correlation
  that survives partialling a distributional covariate (here the model's own topic rating). Form (ii)
  is *"agreement with humans net of a shadow"* and, per the table's own honesty box, is **not
  commensurable** with the form-(i) matched-material residuals (CC, dative); **no cross-row magnitude
  comparison is made or implied.**
- **The lexicon–grammar parallel, now evidenced on the lexical side.** The result is the lexical anchor
  of [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md): the same
  form–meaning question — *does the model track a gradient that beats a distributional shadow?* — asked
  at the word grain, where the gradient is graded sense-relatedness and the shadow is context/topic
  similarity, the counterpart of the constructional n-gram/frequency shadow. With this and the
  grammatical beaters (CC, dative, AANN), the continuum has a shadow-beater at **both** grains.
- **Behavioral, not the discreteness bet.** This is a monotonicity/agreement positive. It is **not**
  the conjecture's distinctive discreteness prediction (clause b), which — that polysemy is a *discrete
  regime beyond graded distance* — is an adequately-powered **null**
  ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)) and is not
  claimed here.

## What this claim does NOT say

- **Not a magnitude-vs-human, and not a per-item human agreement.** The human anchor grounds
  **direction + aggregate agreement** (in/above IAA) only. The magnitudes are within-run; the per-item
  gold is 2-rater-noisy for 151/200 pairs.
- **Not a twice-powered *independent* magnitude (though now cross-date replicated).** As of 2026-07-05
  the direction/agreement is replicated on a second date (rep2, fresh pair-disjoint items) — so it is no
  longer single-run. But rep2 shares 61/357 usages with v1 (pair-disjoint, not usage-disjoint), so unlike
  the CC and dative magnitudes — attached by powered re-runs on **fully** fresh disjoint items — this is
  cross-date *stability of the same instrument*, not two independent draws; the magnitudes are reported as
  a **replicated direction/agreement**, not pooled into a single tighter interval, and still **not**
  compared to a human effect size.
- **Not a representational claim.** Behavioral rank-tracking only; silent on whether the models carry
  graded sense *representations* (the deferred small-model representation lane).
- **Not the polysemy-vs-homonymy discreteness separation.** Clause (b) is a separate powered null; the
  low DURel end of this sample even *mixes* homonymy (e.g. `lass`/`lassi`), so the "Unrelated" floor is
  partly homonymy, not graded polysemy.
- **Not a clean, fully-independent shadow separation.** The surviving control is model-internal and
  single-run; it is *modest* positive support against a topic shadow, not a decisive dissociation.
- **Not a coverage benchmark, and not beyond the tested surface.** 200 pairs, 43 CCOHA lemmas, one
  temperature-0 run per model, DURel framing, English. No claim beyond these lemmas / register /
  framing / date / panel.
- **No cross-model ranking or model-quality reading.** `gemini > claude > gpt` at this task licenses no
  "better model" claim.

## Bounds

- **Cross-date replicated, pair-disjoint (the lead bound, updated 2026-07-05).** The direction/agreement
  core is now confirmed on **two dates** — v1 (2026-05-30, N=200) and rep2 (2026-07-05, N=200 fresh pairs
  drawn disjoint from v1): every base ρ within v1's CI, the topic partial surviving 3/3 both framings
  ([`result/lexical-sense-gradience-rep2`](../results/lexical-sense-gradience-rep2.md)). This **discharges
  the single-run flag** on the direction/agreement claim. What it does **not** reach: rep2 is disjoint at
  the **pair** level but **61/357 usages recombine** v1 usages (DWUG's corpus is finite), so v1+rep2 are
  **not two fully independent draws** — this is cross-date stability of the same instrument on fresh pairs,
  weaker than the CC/dative/AANN re-runs' fresh-item independence, and the magnitudes are **not pooled or
  meta-analyzed as independent**. A full-scope, magnitude-vs-human promotion remains unlicensed.
- **The topic control is model-internal.** A surviving `partial | topic` is modest support that the
  sense signal isn't merely echoed context similarity; it is not a fully independent control, and a
  collapse would have been ambiguous. The lexical-overlap control is near-degenerate and rules out only
  the surface shadow.
- **2-rater gold floor.** 151/200 pairs rest on only 2 annotators; the half-integer human levels are
  2-rater disagreements and are not treated as reliable graded gold. The n≥3 subset ρ is reported in
  the run's `raw/results.json` as a robustness check.
- **Homonymy floor.** Some DWUG lemmas conflate homonyms, so the "Unrelated" end is partly homonymy,
  not graded polysemy — the clean polysemy-vs-homonymy contrast is the deferred (and separately null)
  clause (b).
- **Behavioral, single-lab, cross-model shared priors.** A stated-rating behavioral measure
  (logprob-free); three decoder LLMs converging is weak evidence on its own, and the DWUG human signal
  is what gives the result its independent bearing. DWUG EN is distributed CC BY-ND 4.0 (analysis and
  verbatim mirroring permitted; the data were read, not redistributed modified).

## Anchor

This claim carries `anchor: resource/dwug-usage-graphs` with an `anchors:` link to
[`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) because it makes a
**human-comparison** statement on its **direction/agreement** leg: the panel's graded rating orders
usage pairs as DWUG's annotators do (the DURel 4-point graded gold) and agrees with the human DURel
median at a level in/above the DWUG EN human–human range (ρ ≈ 0.69, Table 3). That link grounds **only
the direction and the aggregate agreement** — **not** a per-item human comparison (2-rater-noisy for
most pairs), **not** a magnitude-vs-human (no human effect-size anchor), and **not** the discreteness
regime (clause b). The claim is therefore **not** `internal-contrast-only`: it leans, in part, on the
DWUG human graded signal, and states that leg at exactly its (aggregate, direction/agreement,
usage-similarity-as-sense-relatedness) strength.

## Anti-cheat

Promotion fixes the **yardstick** — the DWUG DURel graded human median, the ρ ≈ 0.69 human–human range,
and the pre-registered report-the-correlation-with-CI reading — **never the result.** The yardstick was
ratified before the result ([`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md),
[`decisions/resolved/lexical-sense-gradience-operationalization`](../../decisions/resolved/lexical-sense-gradience-operationalization.md));
the item set was frozen pre-run (manifest sha256 `7b4ad11f…`), a pre-run critic's target-span BLOCKER
fixed and re-frozen before any model call, and the numbers independently recomputed from raw JSON. The
exciting over-read — "LLMs represent graded lexical meaning," or "the model cleanly separates sense from
context," or "the panel matches humans on graded sense" as a *magnitude* or *per-item* statement — is
exactly what the single-run cap, the model-internal-and-modest topic control, the 2-rater gold floor,
the homonymy floor, and the direction-only (never size, never per-item) human anchor refuse. Refusing
the promotion outright was a live option and was weighed: it turns on whether a single-run, powered,
convergently-corroborated direction+agreement finding clears [`PROTOCOL.md §3`](../../../PROTOCOL.md)'s
replication prong at *some* scope; the corpus's own single-primary-run precedents
([`claim/lexical-graded-scale-ungraded-commitment`](lexical-graded-scale-ungraded-commitment.md),
[`claim/relational-order-sensitive-reassignment`](relational-order-sensitive-reassignment.md)) say it
does, and the scope above is drawn so that nothing outruns the one result page this consolidates.

## Status

`status: supported`. What is supported is the **scoped direction-and-agreement claim**: across 200 DWUG
EN within-period pairs, all three panel models' graded sense-relatedness rating rank-tracks the human
DURel median (durel ρ 0.60–0.80, cont ρ 0.68–0.83, all CIs clear of zero), the panel sits in/above the
human–human IAA range (ρ ≈ 0.69), and the monotonic signal survives a modest, model-internal
topic-similarity partial (partial ρ | topic 0.50–0.75), **now cross-date replicated 3/3 on 200 fresh
pair-disjoint DWUG pairs** (rep2, 2026-07-05; every base ρ within v1's CI, topic partial surviving both
framings). `supported` attaches to the **direction**, the **in/above-IAA agreement**, and the
**survives-the-topic-shadow** reading (clause c, at its stated strength) — **not** to a human comparison
of *sizes*, **not** to a per-item human comparison, **not** to a twice-powered *independent* magnitude
(rep2 is pair-disjoint but shares 61/357 usages with v1 — cross-date instrument stability, not two
independent draws; magnitudes are not pooled), and **not** to a representational or discreteness reading,
all explicitly disclaimed above. The underlying results remain `status: proposed` (this claim
consolidates them). `contingent-on: []` — the governing anchor and operationalization decisions are
ratified. The owed non-Anthropic decorrelation vote converged **PROMOTE-SCOPED** (status box); the
**single-run flag named as the next strengthening has now landed** (rep2) — what remains for a
full-scope, magnitude-vs-human edition is a **usage-independent** re-run (a different corpus / generated
items) and a human effect-size anchor, neither yet in hand.
