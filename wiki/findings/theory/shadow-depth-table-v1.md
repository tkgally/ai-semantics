---
type: theory
id: shadow-depth-table-v1
title: The shadow-depth table (v1) — five weeks of probes arranged as one measured object, each beater row a residual over a named distributional control with its 95% CI, each saturated corner a marked reading; the flagship deliverable of the 2026-07 program
meaning-senses:
  - distributional
  - constructional
  - inferential
  - referential
  - human-comparison
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-03
updated: 2026-07-03
links:
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
  - rel: refines
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/aann-behavioral-gradient-v2
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: essay/presupposition-environment-gated
  - rel: depends-on
    target: result/presupposition-doppelganger-control-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: result/accommodation-cue-strength-v1
  - rel: depends-on
    target: conjecture/lexical-relation-shadow-saturation
  - rel: depends-on
    target: concept/distributional-meaning
---

# Theory (draft): the shadow-depth table, v1

> **UPDATE (2026-07-03, s173): the presupposition saturated corner's control has RUN** (program A1a →
> [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)).
> Verdict BEATS-DOPPELGANGER but **under-licensed** (word-form-keyed, surface-cue-reconstructable): the
> corner is neither a measured flat-null nor a beater-side move, so it **stays in the saturated section**
> as a *reading with a measured caveat*. No beater row added; no number in the beater table changed. The
> corner row's status cell + "what the arranged object shows" §2 are updated in-page; this remains v1
> (the row-inclusion ratification stands).

> **Status: draft (2026-07-03, session 171). The program's flagship deliverable
> ([`wiki/program.md`](../../program.md) §"Flagship deliverable"; item A1c).** This page introduces
> **no new measurement and no new human comparison.** It arranges results that already exist — each
> cited at its source page's stated strength — along the shadow-depth axis of
> [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md), so the
> continuum reading becomes one legible object. Its inclusion and presentation rules were surfaced,
> not smuggled, and are now the **ratified** default (adopt-A on all three sub-questions) of
> [`decisions/resolved/shadow-depth-table-row-inclusion`](../../decisions/resolved/shadow-depth-table-row-inclusion.md)
> (ratified session 172, autonomous adversarial review + a non-Anthropic panel vote; anchor-discipline
> and modesty tests both PASS, no result changed). Read the two honesty boxes at the foot before citing.
>
> *(`anchor: internal-contrast-only` on the front-matter means only that **this arrangement adds no
> new human comparison** — three of its beater rows carry their own human anchors, stated in the
> anchor column and shown standing; the front-matter label governs the page's own claim, not its
> rows'.)*

## What this table is

The lexicon–grammar continuum ([`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md))
runs one test across the whole word↔construction cline: *does the model track a meaning gradient
that beats the distributional shadow?* The [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)
argues that this test does not sort phenomena by **grain** (word vs construction) but by
**shadow-depth** — how much of the phenomenon is already written into surface co-occurrence — and
that shadow-depth **cross-cuts** grain: each pole holds *both* a demonstrated shadow-**beater** and
a shadow-**saturated corner**.

This page turns that reading into a table. Each **beater** row is a probe on the project's panel
with a **named distributional control that strips the shadow** and a **measured residual over that
control with a 95% CI**. Each **saturated** row is a phenomenon the essay places at the deep-shadow
end by an argued reading, with **no matched-control panel result** — marked as a reading/bet, not a
measured row. The table's claim is the **structure**, at the essay's weak evidential strength — not
a measured shadow-depth scalar per phenomenon.

## The two row forms (read before the table)

The four beater rows do not share one statistical form, and the table never silently equates them
(decision default, question 1):

- **Matched-material residual (form i):** a **within-model** contrast — the model's behavior on the
  phenomenon minus its behavior on a control built from the *same surface material*, so a
  distribution-only account predicts no gap. The comparative-correlative gap is the paradigm; the
  dative's within-item shift is control-**by construction** (the two phrasings are identical across
  an item's two discourse contexts, so length/order/position cancel).
- **Partialled correlation (form ii):** a **model–human** gradient correlation (Spearman ρ against a
  human gradient) that **survives partialling out a distributional covariate** — the model's own
  topic-similarity rating (lexical) or Zipf word-frequency (AANN). The residual is the *partial*
  correlation: rank information about the human gradient carried *over and above* the shadow.

Form (i) is a magnitude in the model's own behavior; form (ii) is agreement with humans net of a
shadow. They point the same way — a residual the distributional shadow does not explain — but they
are **not commensurable**, so **no cross-row comparison of magnitudes is made or implied.**

## The table

Point estimates are per model, **claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash**. Every number
is quoted from the linked source page at its stated strength; see that page for full CIs, gates, and
caveats.

### Beater rows — a measured residual over a named control (shallow shadow)

| phenomenon | grain / pole | distributional control (the shadow) | residual over the control | row form | anchor | source |
|---|---|---|---|---|---|---|
| **Comparative-correlative covariation** | construction (grammatical) | matched **same-word** non-CC controls (same scalar words, no CC syntax) | construction-isolation assertion gap **≈87 pp** — 86.8 / 88.2 / 86.8, 95% CI lower bound **≈78 pp**; controls still assert ≈12% (off-ceiling) | (i) matched-material | internal-contrast-only | [`result/comparative-correlative-covariation-powered`](../results/comparative-correlative-covariation-powered.md) |
| **Dative information-structure** | construction (grammatical) | within-item shift design — length/order/position **immune by construction** | within-item DOC-shift **+0.325 [0.286, 0.362] / +0.018 [−0.011, 0.047] / +0.500 [0.458, 0.537]**; **2/3 CONFIRM** (gpt WEAK, CI includes 0) | (i) matched-material (by design) | human — Bresnan `languageR::dative` production direction (direction only) | **[`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)** · [`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md) |
| **AANN acceptability gradient** | construction (grammatical) | **Zipf word-frequency** (partialled); noun-class marginal | partial ρ \| frequency **0.692 / 0.661 / 0.736** (base cell-level ρ 0.702 [0.61,0.77] / 0.684 [0.60,0.75] / 0.751 [0.68,0.81]); held-out replication on unseen adjectives | (ii) partialled correlation | human — Mahowald Exp-2 MTurk gradient | [`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md) |
| **Lexical sense gradience** | word (lexical) | model's own **topic/context-similarity** rating (partialled); lexical overlap (near-degenerate) | partial ρ \| topic **0.52 / 0.50 / 0.73** (base DURel ρ 0.679 [0.59,0.75] / 0.601 [0.49,0.69] / 0.804 [0.75,0.85]) | (ii) partialled correlation | human — DWUG DURel median (human–human ρ 0.69) | [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) |

### Saturated corners — a placed reading, no matched-control panel result (deep shadow)

| phenomenon | grain / pole | why placed deep (the shadow reconstructs the behavior) | status of the placement | source |
|---|---|---|---|---|
| **Presupposition (projection + accommodation)** | construction (grammatical) | behavior is fully described by *follow the surface cue; reliability set by the environment*: projection collapses under the conditional antecedent (survival **0.42 / 0.17 / 0.17**), accommodation gated by context support (neutral **1.00 / 0.92 / 1.00** vs contradicting **0.33 / 0.58 / 0.42**), and the gate is cue-strength-**graded** — a *deeper* shadow, not a computed split | **reading, control now RUN (2026-07-03, A1a).** The matched surface-cue doppelgänger control [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md) returned **BEATS-DOPPELGANGER** (pooled residual +0.78 / +0.47 / +0.94) — **under-licensed** (word-form-keyed; surface-cue-reconstructable; cleft leg no clean cross-panel residual). So: **not** the flat null, **not** a beater-side move. Stays a saturated **reading with a measured caveat**; `internal-contrast-only` (anchor ratified s174). [`essay/under-licensed-middle`](../essays/under-licensed-middle.md) sharpens *why*: the word-varying factive/aspectual legs that dominated the verdict could not, **by construction**, reach a beater — only a construction-grain control (the cleft) can, and it gave no clean cross-panel residual | [`essay/presupposition-environment-gated`](../essays/presupposition-environment-gated.md), [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md), [`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md), [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md) |
| **Antonymy relation recovery** | word (lexical) | antonymy is the relation models recover best (Cao 𝒮≈0.57 vs ≈0.30; Diera "antonymy easiest") *and* the relation whose distributional shadow is largest — antonym pairs recur in tight contrastive frames (Justeson & Katz: 75% in conjoined structures), so the over-and-above residual is smallest exactly where the model looks best | **reading/bet.** Prior-art on **non-panel** models + the **blocked** [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md) (`anchor: pending`, unrun). No panel contrastive-frame control | [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md) |

## What the arranged object shows

1. **Each pole carries a beater and a saturated corner, and grain does not separate them.** The
   grammatical pole holds three beaters (CC, dative, AANN) and one saturated corner (presupposition);
   the lexical pole holds one beater (sense gradience) and one saturated corner (antonymy). Read the
   table by column "shadow-depth", not by grain: the beaters cluster at the shallow end **at both
   grains**, and the two saturated corners at the deep end **at both grains**. This is the essay's
   structural claim, now displayed rather than argued — and it is the reason the table exists.

2. **The beater side is genuinely measured; the saturated side is now partly measured
   (2026-07-03).** The evidential asymmetry the essay insists on is visible as a table boundary:
   everything above the second header has a residual over a named control with a CI; everything below
   it has a *reading*. **Update:** program **A1a**'s presupposition doppelgänger control has now RUN
   ([`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)),
   and the outcome is instructive precisely because it lands in **neither** clean pole: the corner is
   **not** a measured flat-null (the doppelgänger *is* discriminated, BEATS-DOPPELGANGER) and **not** a
   measured shadow-beater (the residual is word-form-keyed and surface-cue-reconstructable, so it does
   not move to the beater side). It converts the presupposition *reading* into a *reading with a
   measured caveat*, not into either kind of row. The antonymy corner's control (the blocked conjecture)
   remains **owed**.

3. **The two row forms both survive their shadow, differently.** Form (i) shows the residual as a
   large within-model gap the same words in a plain frame do not produce (CC ≈87 pp; the dative
   shift, immune to length by construction). Form (ii) shows it as human-gradient agreement that
   does not wash out when the distributional covariate is partialled (sense gradience gemini
   0.80→0.73; AANN 0.75→0.74). Neither is a depth-of-processing verdict; both are "a residual the
   shadow does not explain."

## What it does not show (binding — the same bounds as every source row)

- **No new measurement, no new human comparison.** This is an arrangement of existing results. The
  CC row's ≈87 pp is a **within-model** magnitude (`internal-contrast-only`) and must **not** be read
  against the human-anchored rows as if commensurable; the human-anchored rows compare a model
  gradient to a human gradient, a different quantity.
- **No fine ordering among the beaters.** The residual forms and CIs are not commensurable, so the
  table orders only coarsely (beater vs saturated, per pole). It does **not** claim CC's shadow is
  "shallower" than sense gradience's, or rank the beaters by residual size (decision default,
  question 3).
- **The saturated placements are bets.** Placing presupposition and antonymy at the deep end is the
  essay's reading, offered at weak evidential strength (n=3 models, small synthetic/prior-art item
  sets, one saturated corner per pole, the discriminating control still owed). A matched-control
  probe could move either corner to the beater side; the table would then gain a row and lose a bet.
- **Behavioral, not representational; single runs; small N; n=3 models.** Every source page's scope
  bound carries onto its row unchanged. gpt-5.4-mini's dative WEAK (CI includes 0) is shown, not
  hidden — the dative row is a **2/3** beater, and the panel-label-hides-spread discipline of
  [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md) applies to
  it.

## Revision triggers (read before citing)

- **A saturated corner gets a control and beats it** → it moves to the beater side, the table gains
  a measured row, and the "each pole has a saturated corner" structure weakens at that pole. This is
  the live outcome of program **A1a** (presupposition) and the antonymy conjecture.
- **A saturated corner gets a control and fails it** → the reading/bet becomes a **measured**
  saturated row (the strongest state this table can reach on the deep side), and the asymmetry the
  second honesty box records is discharged.
- **A beater fails to replicate, or its shadow-control turns out not to hold** → that row leaves the
  shallow end and the "each pole has a beater" half weakens. (The dative's gpt member is already the
  fragile case: a further replication that pushed claude or gemini's shift toward zero would matter.)
- **A new controlled probe lands** (any A1/A2 item with a named control + CI) → it is added as a new
  beater row in the same edition, keeping the table the live roll-up the program intends.
- **The row-inclusion decision is reopened and re-ratified differently** → the ratified default
  ([`decisions/resolved/shadow-depth-table-row-inclusion`](../../decisions/resolved/shadow-depth-table-row-inclusion.md),
  adopt-A on all three) stands as of session 172; only a *materially different* row-form or
  anchor-type presentation would reopen it (e.g. admit only form (i)), and the table is rebuilt to match.

## Honesty box 1 — what is original here, and what is not

The **original** contribution is the **arrangement**: collating five weeks of independently
verified, operationalization-ratified results (each `status: proposed`, gated by a pre-run critic
and a recompute-from-raw verifier) into one object sorted by shadow-depth, with row forms and anchor types made explicit so the beater/
saturated boundary and the internal-contrast/human-anchored boundary are both legible. The
**shadow-depth reading** is from [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md);
the **continuum frame** from [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md); every
**number** from the linked result page at its stated strength. No number here is new, re-measured, or
re-analyzed.

## Honesty box 2 — weakest where it most needs strength

The table is strongest on the beater side (four verified, controlled, interval-bearing results — the
**dative** row now promoted to [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)
(2/3, direction-only, magnitude deferred to the owed powered re-run), the other three `status: proposed`) and
**weakest on the saturated side**, which is the half that carries the essay's structural claim. The
two saturated corners are **readings/bets, not controlled failures to beat a shadow**: no matched
distributional control has been run on the panel for either. So the table demonstrates the
**beater** half of the structure (each pole has a measured shadow-beater) and only **argues** the
**saturated** half (each pole has a shadow-saturated corner). The honest one-line summary: *the
project has measured that the shadow can be beaten at both grains, and it has a well-argued but
uncontrolled reading that each grain also has a corner where the shadow is deep enough to leave no
residual — the controls that would settle the second half are named and owed.*
