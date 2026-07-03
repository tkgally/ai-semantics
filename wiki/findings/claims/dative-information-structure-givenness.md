---
type: claim
id: dative-information-structure-givenness
title: The dative alternation's information-structure (givenness) effect is a twice-observed, human-direction-anchored, shortcut-immune production-preference positive for 2 of 3 panel models (claude + gemini robust; gpt's v1 CONFIRM did not replicate — WEAK, CI includes 0); a directional/ordering claim with magnitude+interval deferred to the owed powered re-run
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: supported
anchor: human-anchored
contingent-on: []
created: 2026-07-03
updated: 2026-07-03
links:
  - rel: anchors
    target: resource/languageR-dative-corpus
  - rel: depends-on
    target: result/dative-information-structure-v1
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: conjecture/dative-alternation-information-structure
  - rel: supports
    target: theory/constructional-meaning-in-llms
  - rel: supports
    target: theory/shadow-depth-table-v1
  - rel: supports
    target: essay/concordant-verdict-hides-spread
---

# Claim: the dative alternation's information-structure (givenness) effect is a twice-observed, shortcut-immune production-preference positive — for 2 of 3 panel models

> **Status: supported (2026-07-03).** Cross-session, independent, adversarial claims-promotion review
> ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item B1) of the dative **givenness**
> information-structure line —
> [`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)
> (session 51, panel CONFIRM 3/3) and
> [`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)
> (session 53, panel CONFIRM 2/3, fresh disjoint items). It promotes the **givenness** behavioral
> positive only, and it is deliberately disjoint from the sibling reachability closure
> [`claim/dative-pronominality-partial-reach`](dative-pronominality-partial-reach.md), which bounds
> the *pronominality* edge of the same line and leaves this givenness result "exactly as published."
> It mirrors the shape of [`claim/comparative-correlative-covariation`](comparative-correlative-covariation.md):
> **directional/ordering scope; magnitude+interval deferred** to the owed A2a powered re-run.

## Statement

Across two controlled runs on **disjoint item sets** (v1, session 51; v2, session 53) on the ratified
3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), **2 of the 3 models —
`claude-sonnet-4.6` and `gemini-3.5-flash` — robustly shift their double-object (DOC) vs.
prepositional-dative (PD) production preference in the human-attested information-structure
direction**: a discourse-**given recipient** raises DOC preference and a **given theme** lowers it
(favouring PD), across a within-item manipulation whose two scored phrasings are **byte-identical**
across the item's two discourse contexts. Because every surface feature of the test sentence is held
identical, the finding-bearing within-item shift is **immune by construction** to any length-only,
position-only, order-only, always-DOC, always-PD, shorter-first, or longer-first reader (each yields
shift = 0 — certified at build and re-derived by both runs' independent pre-run critics). For these
two models the effect is **twice-observed at near-identical magnitude on disjoint items** and
**survives the end-weight dissociation control** (12/12 items in both runs).

The claim is **scoped and qualified**, never panel-uniform:

- **The panel verdict is CONFIRM (2/3), not 3/3, and the third model is fragile.** `gpt-5.4-mini`'s
  v1 CONFIRM (+0.056) **did not replicate**: on fresh items its main-arm shift fell to **+0.018 with a
  bootstrap 95% CI of [−0.011, 0.047] that includes zero** (15/32 items positive — "a coin flip";
  sign-p 0.70) → **WEAK**. The honest statement is gpt's shift is *"too small to distinguish from zero
  on this fresh item set,"* **not** that gpt is proven insensitive.
- **The per-model effect sizes decorrelate by an order of magnitude and do NOT compress on
  replication** (gemini ≫ claude ≫ gpt; gemini-to-gpt ratio ≈9× in v1, ≈27× in v2). Per the reading
  discipline of [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md),
  this licenses a *direction/existence* statement but **not** a panel *uniformity* or *magnitude*
  statement.
- **Directional/ordering scope only — no magnitude claim.** Item N is founding-size (32 main + 12
  control per run), below [`PROTOCOL.md §4`](../../../PROTOCOL.md)'s ~100–150 powered N; **no magnitude
  with an interval is claimed here.** The magnitude+interval is deferred to the **owed A2a powered
  re-run** (program A2a lists "dative information-structure `[ ]`" as owed, one at a time), exactly as
  [`claim/comparative-correlative-covariation`](comparative-correlative-covariation.md) was promoted
  direction-only before its powered re-run landed.

## Grounds

Two own-design results, byte-identical instrument, replicating the **direction** on disjoint item
sets. Read the **per-model shifts and their intervals** below, not a pooled panel scalar.

Main within-item shift `shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)`,
per model, with a 10 000-resample bootstrap 95% CI over items (verdict map fixed before any call:
CONFIRM iff mean shift > 0 **and** bootstrap lower bound > 0):

| model | v1 shift | v1 95% CI | v1 items+ | v1 verdict | v2 shift | v2 95% CI | v2 items+ | v2 verdict |
|---|---:|---|---:|---|---:|---|---:|---|
| `claude-sonnet-4.6` | **+0.327** | [0.289, 0.359] | 31/32 | CONFIRM | **+0.325** | [0.286, 0.362] | 32/32 | CONFIRM |
| `gemini-3.5-flash` | **+0.524** | [0.495, 0.552] | 32/32 | CONFIRM | **+0.500** | [0.458, 0.537] | 32/32 | CONFIRM |
| `gpt-5.4-mini` | +0.056 | [0.023, 0.086] | 22/32 | CONFIRM | **+0.018** | **[−0.011, 0.047]** | 15/32 | **WEAK** |

- **What replicated (the claim's spine).** *"The two strong members replicate almost exactly. claude's
  main shift is +0.325 (v1 +0.327) and gemini's is +0.500 (v1 +0.524) — both within a few thousandths
  of their v1 values, both 32/32 items positive, both clearing their bootstrap lower bound by a wide
  margin, both surviving the end-weight dissociation control 12/12"*
  ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)). The shift
  moves preference *around the model's own neutral both-new default* in both directions — for claude the
  given-recipient / given-theme DOC-preference cells are 0.708 / 0.382 (v1) and 0.714 / 0.389 (v2)
  against a neutral 0.580 / 0.607; for gemini 0.791 / 0.266 (v1) and 0.778 / 0.278 (v2) against 0.559 /
  0.558 — a genuine bidirectional context shift, not a one-sided ceiling artifact.
- **What did not replicate (the load-bearing qualifier).** *"gpt's v1 CONFIRM does not replicate. On
  fresh items gpt's main-arm shift is +0.018 with a bootstrap 95% CI of [−0.011, 0.047] that includes
  zero (15/32 items positive — a coin flip; sign-p 0.70). Under the pre-registered lower-bound gate this
  is WEAK, not CONFIRM"*
  ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)). A reported
  wrinkle — gpt's v2 **control**-arm shift is +0.144 (12/12 positive), larger than its near-zero main
  arm, "a small, real signal that gpt is not *wholly* context-insensitive" — is **not** used to change
  the verdict, because the pre-registered primary is the main arm and the control may not rescue a failed
  primary. gpt is WEAK.
- **The spread reproduces and widens.** *"The order-of-magnitude spread reproduces and does not compress
  … gemini +0.500 ≫ claude +0.325 ≫ gpt +0.018 — a gemini-to-gpt ratio of ≈27× (v1's was ≈9×)"* — so
  v1's concordant 3/3 label demonstrably *"hid a fragile member,"* vindicating the carry-the-spread
  discipline this claim honours by scoping to per-model magnitudes and 2/3.
- **Both runs are recompute-verified.** v1 fresh post-run verifier: *"REPRODUCED — no material
  discrepancies."* v2 fresh post-run verifier: *"The raw per-call data independently reproduces the run's
  headline … No verdict-changing or materially different number was found."* Data quality both runs: *"0
  NA, 0 stern-retries, 0 length-truncations"* across all 720 trials per run.

## Human-comparison leg (direction only — magnitude is NOT anchored)

The claim's human-comparison force is on the **direction of the effect**, not its size. The anchor is the
Bresnan et al. (2007) `languageR::dative` **production** corpus
([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md); "3263
observations on the following 15 variables"; outcome distribution NP(DOC)=2414 / PP(PD)=849), which codes
the exact factors and outcome the probe manipulates:

- the information-structure factors — `AccessOfRec` *"a factor with levels `accessible`, `given`, and
  `new` coding the accessibility of the recipient"* and `AccessOfTheme` *"a factor with levels
  `accessible`, `given`, and `new` coding the accessibility of the theme"* — are the human-side coding of
  the given/new manipulation the probe imposes in discourse context; and
- the outcome — `RealizationOfRecipient` *"a factor with levels `NP` and `PP` coding the realization of
  the dative"* (NP = DOC, PP = PD) — is the human-side analogue of the model's DOC/PD preference.

The specific **production direction** that anchors the claim is that the firsthand logistic fit on the
inspected rows *"reproduces all five canonical human directions (given/pronominal recipient → DOC;
given/pronominal theme → PD; longer theme → DOC by end-weight) at in-sample accuracy 0.887"* — of which
the two the givenness probe tests are **given recipient → DOC** and **given theme → PD**. The models'
shift is in that human direction. Per the resource's own caution, this is a *"production"* signal —
*"the right anchor for 'does the model's production preference track the human production surface', the
wrong anchor for 'does the model rate sentences the way humans rate them'"* — and it is **not** a
per-item human acceptability rating and **not** a human effect-*size*. So the human-comparison statement
is exactly: *for claude and gemini, the model's production preference shifts in the direction the human
production corpus attests.* No human comparison of magnitudes is made or owed (the Bresnan & Ford 2010
graded-rating anchor was ratified an opportunistic upgrade only and was not used).

## The controls that earn the rigor

The claim's "not a shortcut" force rests on the design, not on the raw shift sizes:

- **Immune by construction.** The two phrasings the model scores are byte-identical across an item's two
  discourse contexts (same words, same recipient/theme lengths, same animacy); the givenness manipulation
  lives *only* in the swappable context. So any length-only / position-only / order-only / always-DOC /
  always-PD / shorter-first / longer-first reader yields shift = 0 — certified at build (v1
  `certification.json`: *"all eight enumerated shortcut readers → max|shift| = 0.000000"*; v2 the same),
  and independently re-derived by the pre-run critics with **ten further** surface readers in v1 and
  **fourteen** in v2, all zero. Only tracking the discourse context can move the shift off zero.
- **End-weight dissociation control.** On the 12 control items the *given* constituent is made the
  *longer* one, so information structure predicts the longer-first order, *opposing* end-weight. The
  shift stays positive for claude and gemini in both runs (v1 +0.305 / +0.404; v2 +0.335 / +0.461,
  12/12), so their main effect is not a short-before-long heuristic.

This is why the dative row is a **beater** in the flagship
[`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md) — a within-model residual over a
distributional control (here the control is *by construction*), shown there at exactly this **2/3**
strength with gpt's WEAK (CI includes 0) displayed, not hidden.

## Where it sits on the evidence ladder

On [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)'s ladder this is
a **Tier-2 (gradient semantic tracking) positive**, human-anchored to a corpus production surface — for
claude and gemini now *twice-observed at near-identical magnitude on disjoint items*. It patterns with the
project's recurring **add/easy-direction** observation: current decoders track a well-described soft
constraint in the human direction cleanly, *and* membership in "tracks it cleanly" is itself
model-specific and not guaranteed to replicate (gpt). It does **not** reach **Tier 4
(inference-licensing)**: the effect is a gradient *preference*, not the licensing of a
construction-contributed entailment the lexical items cannot supply. The `inferential` sense-tag here
marks that the tracked constraint is discourse-inferential (given-before-new), **not** a claim that the
construction licenses an inference — that stronger reading is explicitly disclaimed.

## What this claim does NOT say

- **No magnitude with an interval.** The per-run shifts (e.g. claude +0.325, gemini +0.500) are
  founding-N point estimates on 32 main items; the claim states their **direction and replication**, not
  a powered magnitude. The magnitude+interval is **owed and deferred** to the A2a powered re-run
  (~100–150 items), mirroring the CC claim's magnitude-deferral before its powered run landed.
- **No panel-uniform claim.** gpt's effect does not clear zero on fresh items; the claim covers the panel
  *including* that non-replication ("2 of 3 robust; the third WEAK"), it does not average it away.
- **Not acceptability, not logprob.** The indicator is a **stated production preference** elicited on a
  graded working surface (100 points distributed by naturalness, the model reasoning briefly before its
  `FINAL:` line); it is logprob-/surprisal-free (none available under pure autonomy). It measures *stated*
  naturalness preference, not a per-item human acceptability rating.
- **No human comparison of sizes.** Only the *direction* is human-anchored; the cross-model magnitude
  spread is a within-panel observation, not a human-comparison.
- **Not a model ranking.** Prediction 3's content is that the spread *decorrelates from general
  competence*, so "gemini > claude > gpt at the dative" licenses no "better model" reading, and the
  project has no in-repo cross-task tabulation that would.
- **No model-internal or grounding claim.** Behavioral only; silent on representations and on grounding in
  Bender & Koller's sense.
- **Distinct from the pronominality closure.** This is the *givenness* behavioral positive; the
  *pronominality* factor is handled separately as a documented reachability partial-reach
  ([`claim/dative-pronominality-partial-reach`](dative-pronominality-partial-reach.md)), which makes **no**
  behavioral claim and leaves this result untouched. The two do not overlap and do not contradict.

## Bounds

- **Founding-N; the powered re-run is owed (lead caveat on magnitude).** 32 main + 12 control items per
  run. Under [`PROTOCOL.md §4`](../../../PROTOCOL.md) a claim-carrying *magnitude* needs ~100–150 items;
  the claim's **direction/ordering** scope is what is supported now, and the A2a powered re-run (program
  A2a: dative information-structure `[ ]`) is the named, owed unit that would attach an interval.
- **Per-model spread / gpt fragility is load-bearing.** The "for 2 of 3 models" scoping is not a
  courtesy; the order-of-magnitude spread and gpt's non-replication are the reason no panel-uniform or
  magnitude sentence is licensed.
- **Production preference, working surface, logprob-free.** As above — a stated-preference behavioral
  measure, anchored to a production direction, not to acceptability ratings.
- **Single-lab, single-date-per-version, single-run-per-version, small N, cross-model shared priors.** v2
  adds a second date and a fresh item set — a real strengthening for claude and gemini — but this is not a
  multi-date time series, the panel is three specific model versions, and three decoders converging is
  weak evidence on its own; the human corpus direction is what gives the result independent bearing.
- **A secondary corpus-gradient ρ tracks the primary** (Spearman ρ, same ranking both runs: v1 claude
  0.83 / gemini 0.79 / gpt 0.48; v2 claude 0.81 / gemini 0.84 / gpt 0.37) but is **non-decisive by
  pre-registration** — it may not convert a WEAK to a CONFIRM — and codes six institutional recipients as
  inanimate (conservative), a value-laden choice feeding only that secondary ρ.

## Anchor

This claim carries `anchor: human-anchored` with an `anchors:` link to
[`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md) because it makes a
**human-comparison** statement on its **direction** leg: the models' production preference shifts in the
direction the Bresnan et al. (2007) production corpus attests (given recipient → DOC, given theme → PD,
via `AccessOfRec` / `AccessOfTheme` against `RealizationOfRecipient`, in-sample accuracy 0.887). That link
grounds **only the direction of the effect**, not its magnitude (no human effect-size anchor is in-repo)
and not a per-item acceptability comparison (the corpus is production, not judgment). The claim is
therefore **not** `internal-contrast-only`: it does lean, in part, on the human production direction, and
states that leg at exactly its (direction-only, production, corpus-gradient) strength.

## Anti-cheat

Promotion fixes the **yardstick** — the human production direction and the pre-registered lower-bound
gate — never the result. The claim states no more than two disjoint replications and their controls
license: for 2 of 3 models the stated production preference shifts in the human-anchored direction across
a shortcut-immune within-item manipulation, twice, on disjoint items; the third model's effect does not
clear zero on fresh items; magnitude is not yet powered. The exciting over-read — "LLMs understand the
dative alternation's information structure," or "the panel tracks givenness" read as uniform or as a
size — is exactly what the 2/3 scoping, the magnitude deferral, and the direction-only human anchor
refuse. Nothing here outruns the two result pages it consolidates.

## Status

`status: supported`. What is supported is the **scoped directional/ordering claim**: the givenness
information-structure effect is replicated across two controlled runs on disjoint item sets, is immune by
construction to length/position/order shortcuts and survives the end-weight dissociation control, is
human-anchored on its direction leg, and holds robustly for `claude-sonnet-4.6` and `gemini-3.5-flash`
while `gpt-5.4-mini`'s v1 CONFIRM does not replicate (WEAK). `supported` attaches to that direction, the
replication, and the 2/3 panel verdict — **not** to any magnitude (deferred to the owed A2a powered
re-run) and **not** to a panel-uniform or human-level-competence reading, both explicitly disclaimed
above. The two underlying results remain `status: proposed` (this promotion consolidates them; it does not
restate their per-run readings). `contingent-on: []` — the governing operationalization
([`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md),
ADOPT MODIFIED) is ratified.
