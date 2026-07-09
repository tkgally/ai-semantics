---
type: essay
id: cue-strength-recovery-decoupling
title: "The cue-strength–recovery decoupling: raw contrastive-frame co-occurrence density does not predict which lexical relations the frontier panel recovers"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: revised
contingent-on: []
created: 2026-07-06
updated: 2026-07-09
links:
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: theory/shadow-depth-table-v1
  - rel: depends-on
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: essay/shortcut-vs-competence-mis-cut
  - rel: depends-on
    target: essay/two-distributional-hypotheses
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Essay: the cue-strength–recovery decoupling

> **Status: revised (drafted 2026-07-06 session 187; revised 2026-07-08 session 193 — H1/H2 discharged
> by a fresh noun probe; revised 2026-07-09 session 196 — the adjective-antonymy replication in J&K's
> home POS scopes the decoupling to NOUNS [H1-PARTIAL across the POS boundary], while its antonymy-shadow
> half strengthened; see the dated revision boxes).** A
> philosophical-track essay in the project's own voice. It introduces **no new measurement** and makes
> **no human comparison**: every empirical
> assertion cites [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)
> at that page's stated strength (`status: proposed`, `anchor: internal-contrast-only`; **n = 3
> orderings, not coefficients**; **nouns only**; the residual arm **descriptive-only** because the
> pre-registered calibration gate fired). The original contribution is a **reading** of one
> observation the result logs but deliberately does not develop — the *cue-strength–recovery
> decoupling*, which the result page flags as "**a seed for a future essay/conjecture**" — together
> with a **new falsifiable bet** about what predicts relation-wise recovery if raw co-occurrence
> density does not. That new bet is this essay's bar under [`PROTOCOL.md`](../../../PROTOCOL.md) §3.
> The reading makes **no claim that recovery is non-distributional** — that is the one misreading the
> essay works hardest to forbid.

## Thesis

On the frontier panel, the relation the corpus cues most is **not** the relation the panel recovers
best, and the second-most-cued relation is recovered **worst**. Across the six WordNet noun relations,
raw contrastive-frame co-occurrence cue-strength and recovery come apart: the across-relation Spearman
between them is ≈ **−0.086**, the same on all three models
([`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)).

Two claims the project had been running together therefore separate. *"The distributional shadow is
largest where contrastive-frame co-occurrence is densest"* can stand — antonymy is measured, from our
own corpus, as the most distinctively cued relation (contrastive-frame control 𝒮 ≈ **0.077** vs
**0.010–0.028** for the other five). But *"recovery is easiest where that co-occurrence is densest"* is
**false on the panel**: **hypernymy**, the *fourth*-most-cued relation (control 𝒮 ≈ 0.023), is the
**best**-recovered (raw 𝒮 ≈ **0.36–0.39**), and **meronymy**, the *second*-most-cued (control 𝒮 ≈
0.028), is the **worst**-recovered (raw 𝒮 ≈ **0.12–0.18**). The honest statement of the finding is
narrow and exact: *raw contrastive-frame co-occurrence cue-strength is a poor predictor of which
lexical relations the panel recovers* — **not** that recovery escapes distribution. (The relations
here are inferential-role structure in the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)
sense — knowing *X is a kind of Y*, or *X is the opposite of Y*, licenses inferences — and "recovery"
is same-task relatum production; the essay asks only what corpus statistic tracks that recovery.)

## The identification the decoupling breaks

The project's shadow-depth program sorts phenomena by "**how much of the phenomenon is already written
into surface co-occurrence — how much daylight there is between the phenomenon and its distributional
trace**" ([`essay/shadow-depth-cross-cuts-grain`](shadow-depth-cross-cuts-grain.md)). At the lexical
pole, that abstract axis was given a concrete stand-in: **contrastive-frame cue-strength**. The
[`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md) makes the
identification explicit — antonym pairs "recur in tight, near-symmetric contrastive frames," so antonymy
is placed as "the relation where the distributional shadow is *largest*, so it is the relation where the
'over and above' residual that a genuine competence claim must show is *smallest*." Put as a chain:
*most contrastively-framed ⇒ deepest shadow ⇒ smallest over-and-above residual ⇒ recovery least
informative*. The first arrow does the smuggling — it reads cue-density as a proxy for shadow-depth, and
hence for how cheaply recovery is bought by co-occurrence.

The decoupling attacks that first arrow. If cue-density predicted recovery-difficulty, the most-cued
relation would be the one recovered most cheaply and the one whose recovery a co-occurrence control most
fully reconstructs. On the panel it is neither. Antonymy is the most-cued relation *and* one of the
relations whose recovery **clears wide daylight** above the contrastive-frame control (HIT@3 residual
**+0.61 to +0.67**, among the *largest* of the six alongside hypernymy, with **meronymy** the smallest
3/3) — the opposite of "deep shadow, small residual." And across all six relations, cue-strength rank and recovery rank are
essentially uncorrelated (**−0.086**). So *"the shadow is largest where co-occurrence is densest"* and
*"recovery is easiest where co-occurrence is densest"* are two claims, and on the frontier panel they
point in different directions. Cue-strength is not, on this panel, a usable stand-in for shadow-depth.

## What the panel actually shows — and the floor it does not over-read

The recovery ranking is genuinely scrambled against cue-strength, not merely noisy. Ordered by
cue-strength the relations run antonymy (0.077) ≫ meronymy (0.028) > holonymy (0.026) > hypernymy
(0.023) > synonymy ≈ hyponymy (0.010); ordered by raw recovery they run hypernymy (≈0.37) > antonymy
(≈0.32) > synonymy ≈ hyponymy (≈0.24) > holonymy ≈ meronymy (≈0.15). The most-cued relation lands second
in recovery; the second-most-cued lands last; the fourth-most-cued lands first. All orderings hold 3/3
([`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)).

One thing must **not** be read out of this. The relations *least separable* from the control on the
panel are the part-whole relations (meronymy, holonymy) — but the result page is explicit that this is
"**because they are simply the hardest (lowest raw recovery, 0.12–0.20), not because a co-occurrence
shadow explains them**." The residual arm is **descriptive-only**: the pre-registered calibration gate
fired (mean control 𝒮 ≈ 0.029, below the 0.05 floor), so the top-3 contrastive-frame control
recovers almost none of *any* relation's WordNet relata, so a "small residual" at the part-whole end is a
**floor effect**, not a measured deep shadow. This is exactly why the weight of the finding — and of this
essay — rests on **clause 2** (the cue-strength–recovery decoupling, a comparison of two directly
measured rankings) and not on residual magnitudes (which the weak control leaves under-licensed). The
decoupling is the robust part; the residual sizes are descriptive scaffolding around it.

## Why this is not "recovery is non-distributional"

This is the misreading the essay most needs to block, and the project already has the discipline that
blocks it. [`essay/shortcut-vs-competence-mis-cut`](shortcut-vs-competence-mis-cut.md) (ratified s151)
established that a residual over a co-occurrence control grades **local versus transferable
distributional generalization**, *not* distribution versus non-distribution — because "the control is one
chosen statistic … a particular operationalization of 'the shadow,'" and "not predicted by *this* local
co-occurrence statistic" is not the same as "not distributional." The decoupling is the **mirror image**
of that lesson, applied to the *predictor* rather than the *residual*: contrastive-frame cue-strength is
**one** distributional statistic, and its failure to rank-predict recovery licenses only "*this*
statistic does not predict recovery," never "*no* distributional statistic predicts recovery." A
different distributional measure — one keyed to hierarchical or definitional co-occurrence rather than
symmetric contrastive frames — could rank-predict recovery perfectly well and leave the decoupling intact,
because it would be a *different* shadow.

[`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md) sharpens where the whole
observation lives. Contrastive-frame cue-strength and any hierarchical or definitional co-occurrence
statistic are **both** form-internal — both are Harris-style within-language contrast measures, neither
is Firth-situated or world-relating. So the decoupling is a fact *inside the Harris box*: one
form-internal distributional statistic does not predict recovery, while another form-internal statistic
might. It says nothing about reference, grounding, or the situated half of the distributional tradition —
the [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) caveat that
distributional structure is "**by itself, silent on reference and on truth**" is untouched here, because
the essay never leaves distribution. The precise claim is a **within-distributional** one: *raw
contrastive-frame co-occurrence cue-strength decouples from recovery*, full stop.

## What might predict recovery instead — a hypothesis the data only suggest

If cue-strength does not predict recovery, what does? The result did not measure this, and the essay
will not pretend it did. But the ranking has a suggestive shape worth stating as a **conjecture, clearly
labelled as one**. The two best-recovered relations are **hypernymy** and **antonymy** — arguably the two
most *definitionally central* relations: the hypernym is the genus a genus-and-differentia definition
names first ("a robin is a **bird** that …"), and antonymy is the tightest paradigmatic contrast. The two
worst-recovered are **meronymy** and **holonymy** — the part-whole relations, which sit at the periphery
of how a lexicon defines a word. A candidate reading, then: relation-wise recovery may track **taxonomic
/ definitional structure** — IS-A centrality, position in the WordNet hierarchy — rather than raw
contrastive-frame co-occurrence density.

Three honesty stakes must be driven in around that candidate before it is cited:

1. **s186 did not measure it.** No taxonomic-structure proxy was computed and correlated with recovery;
   this is a pattern read *off* the ranking, not a result. It is a hypothesis for a later probe.
2. **The obvious crude proxy is already known to fail.** If "taxonomic structure" is operationalized as
   **gold fan-out** (WordNet gold-set size), s186's own numbers break it: **hyponymy** carries the
   *largest* fan-out (gold size **24.0**) yet is only middling in recovery, and **antonymy** carries a
   tiny fan-out (**1.1**) yet is second-best recovered — so gold-set size alone does *not* track recovery.
   Whatever the right taxonomic proxy is, it is **not** simple fan-out (and hypernymy's fan-out of 14.1,
   though large, is only the second-largest of the six). This is precisely why the candidate is a
   conjecture: the data suggest *a* taxonomic story while ruling out its crudest form.
3. **It would still be a distributional story.** Taxonomic and definitional structure has its own dense
   distributional footprint — Hearst-style hypernym frames ("*X* such as *Y*", "*Y* and other *X*"),
   genus-naming definitional templates. So the candidate is emphatically **not** offered as a
   non-distributional predictor. If it wins, it wins as a *different distributional statistic* out-ranking
   contrastive-frame co-occurrence — the same within-distribution move the previous section insists on.

So the seed is: on the panel, a taxonomic/definitional-structure statistic may out-predict contrastive-frame
cue-strength for relation-wise recovery. Stated as a bet below; asserted as a result nowhere.

## The honest counter

The decoupling could be less than it looks, and the reading is bounded accordingly.

- **The control corpus is a proxy.** Cue-strength here is G² over a fetched Simple English Wikipedia dump,
  a stand-in for the panel's unknown pretraining distribution (result condition 2). A cue-strength
  measured on a corpus closer to the panel's training mix could rank the relations differently, and the
  decoupling is only as good as that proxy. The safer half of the bet below is designed to test exactly
  this by re-running against a different control corpus.
- **Cue-strength is one frame-family.** The control is built from symmetric/contrastive frames ("*X*
  versus *Y*", "neither *X* nor *Y*", conjunction/adjacency) — the operationalization antonymy is
  *designed* to top. That this particular statistic fails to predict recovery is not evidence that *no*
  co-occurrence statistic does; it is the whole point of the "not non-distributional" section, and it also
  bounds the claim: the decoupling is specifically of **contrastive-frame** cue-strength from recovery.
- **n = 3, orderings not coefficients; nouns only.** The finding is three models agreeing on a rank
  scramble, over WordNet's noun relations, with the taxonomic relations that exist only for nouns. The
  named adjective-antonymy replication (Justeson & Katz's home part of speech) **has now run (s196) and
  the decoupling did NOT cleanly cross the POS boundary** (H1-PARTIAL; item-level ρ ≈ +0.25) — precisely
  because adjectives lack the taxonomic (hypernymy) relation that carries the noun scramble; the reading
  is scoped to nouns accordingly (2026-07-09 revision box). A different panel could still behave
  differently.
- **The residual magnitudes are descriptive.** Because the calibration gate fired, nothing here should be
  read as a precise measurement of how *much* co-occurrence explains each relation. The essay leans only
  on the *ordering* facts (which relation out-ranks which on cue-strength and on recovery), which the
  post-run verifier reproduced from raw.

None of these rescues cue-strength as a recovery predictor on the evidence in hand; they scope how far the
decoupling generalizes, and each is a live arm of the bet.

## The new bet

The decoupling is registered as a falsifiable bet with two halves, one safe and one risky
([`predictions.md`](../../predictions.md)):

- **H1 (safer) — the decoupling replicates.** On a fresh test of relation-wise relatum recovery (a fresh
  relation set, a *different* control corpus, or the named adjective-antonymy replication), recovery rank
  again decouples from raw contrastive-frame co-occurrence cue-strength: a near-zero or negative
  across-relation rank correlation, ≥2/3 models. **Falsified** if cue-strength recovers its predictive
  power on a fresh set (a clearly positive rank correlation, ≥2/3 models) — i.e. s186's decoupling was
  corpus- or set-specific.
- **H2 (sharper, riskier) — taxonomic structure is the missing predictor.** On that same fresh test,
  recovery rank tracks a **pre-registered taxonomic/definitional-structure proxy** (IS-A / hypernym-tree
  connectivity, or a definitional-frame statistic — *not* bare gold fan-out, which s186 already breaks)
  **better** than it tracks contrastive-frame cue-strength. **Falsified** if no taxonomic-structure proxy
  out-predicts cue-strength, or cue-strength out-predicts every taxonomic proxy — i.e. the decoupling is
  real but taxonomic structure is not what fills the gap.

H1 is close to a re-run of s186's clause 2 on fresh material; H2 is the genuine risk — it predicts a
*specific* replacement predictor and can lose cleanly even if H1 wins.

> **Revision — 2026-07-08 (s193): both bets discharged by a fresh probe.**
> [`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)
> ran the fresh test the design
> [`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../../experiments/designs/lexical-relation-recovery-taxonomic-proxy-v1.md)
> operationalized (gates ratified s193; fresh cues disjoint from s186; a **different** corpus family,
> C4 web text; IS-A depth pre-registered before recovery). **H1 REPLICATES 3/3** (ρ_cue near-zero on
> a fresh corpus — the safer bet holds; the decoupling is not corpus-specific). **H2 fires-FOR at 2/3**
> — the pre-registered primary proxy, IS-A path depth, out-predicts cue-strength (predicted negative
> direction). So this essay's central reading is now **empirically supported, not just conjectured**:
> raw contrastive-frame cue-strength is a poor recovery predictor *and* a taxonomic-structure statistic
> (hierarchical position) does better. **The reading is scoped, not upgraded, by three honest limits
> the run surfaced:** H2 is 2/3 (not 3/3 — hypernymy is both deep and best-recovered, capping one
> model's depth correlation); the effect is **between-relation, not within-cue** (item-level depth→recovery
> ρ ≈ 0); and the corpus **Hearst-frame** operationalization of the "definitional-frame statistic"
> candidate **lost** (wrong-signed), so the surviving taxonomic answer is *structural hierarchy*, not
> *corpus genus-naming frequency*. All still `internal-contrast-only`, nouns only, within-distributional
> — H2 winning is one form-internal statistic out-ranking another, never recovery escaping distribution.
> The essay's thesis stands and is strengthened; the "what might predict recovery" section is no longer
> only a hypothesis for that grain.

> **Revision — 2026-07-09 (s196): the decoupling is scoped to NOUNS — it does not cross the POS boundary.**
> The third freshness route trigger (a) named — the **adjective-antonymy replication** in J&K's home POS
> — ran: [`result/adjective-antonymy-replication-v1`](../results/adjective-antonymy-replication-v1.md).
> Over four WordNet **adjective** relations (antonymy, synonymy, similar-to, also-see; 130 fresh cues
> each; the same byte-frozen contrastive-frame G² control on C4), the across-relation decoupling **did
> not cleanly replicate**: ρ_cue = **+0.4/+0.8/+0.4** (soundness) → **H1-PARTIAL/AMBIGUOUS** (no clean
> replicate at ≤+0.30, no clean 2/3 break), and the **powered item-level arm agrees** — a cue's own
> cue-strength positively predicts its own recovery, ρ ≈ **+0.25** on all three models (against the noun
> run's item-level ρ ≈ 0). **On adjectives, contrastive-frame cue-strength partially *recovers* its
> predictive power.** The reason is structural, and it sharpens rather than refutes the thesis: on nouns
> the decoupling was carried by **hypernymy** — a *low*-cue-strength but taxonomically central relation —
> being *best*-recovered, scrambling the recovery rank against cue-strength. **Adjectives have no
> hypernymy** (no IS-A taxonomy — the same fact that makes H2 untestable), and the most-cued adjective
> relation, antonymy, is *also* the best-recovered, so nothing scrambles the ordering. **The decoupling
> is therefore a noun phenomenon, carried by a taxonomic relation adjectives lack** — not a universal
> fact about frontier lexical recovery. This scopes the essay's central reading to the **noun** grain;
> it does not retract it (the decoupling replicated 3/3 across two noun corpora, s186+s193), and the
> antonymy-shadow half of the same probe *strengthened* (see the antonymy-outlier essay). **Consequence
> for promotion:** the decoupling→`claim` route this replication was meant to open is **blocked** — a
> claim needs the decoupling to hold across POS, and it did not; the s193 result stays a `result`.
> `internal-contrast-only`, adjectives only, within-distributional throughout.

## What this essay is not

- **Not a human comparison.** The essay imports no human recovery baseline and asserts nothing about how
  the panel compares to people. It reads a **within-instrument, internal-contrast** result (model recovery
  vs a corpus-statistic control, on a shared WordNet target that cancels in the contrast) and stays there.
- **Not a claim that recovery is non-distributional.** The load-bearing claim is exactly that *raw
  contrastive-frame co-occurrence cue-strength* decouples from recovery. A different distributional
  statistic may predict recovery; the essay in fact conjectures one (a taxonomic/definitional-structure
  measure, itself distributional). Nothing here touches reference or grounding.
- **Not a measured predictor.** The taxonomic-structure candidate is a hypothesis the ranking *suggests*,
  not something s186 measured — and its crudest form (gold fan-out) is already falsified by s186's own
  hyponymy/antonymy fan-out figures. It is offered as a bet, labelled as one.
- **Not a claim about residual magnitude.** Because the pre-registered calibration gate fired, the essay
  makes no claim about *how much* co-occurrence explains any relation's recovery; the residual arm is
  descriptive-only and the weight is on the two directly measured rankings.
- **Not a universal claim about which relation is best-recovered.** "Hypernymy is best-recovered / antonymy
  second" is scoped to *this panel*. On Cao's and Diera & Scherp's older/smaller models antonymy is the
  best-recovered relation (the premise the [`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md)
  built on); that ordering does **not** transfer to the frontier panel, which is part of what the essay
  reports, not a contradiction it hides.

## Revision triggers (read before citing)

- **(a) A fresh relation-recovery probe reunites cue-strength and recovery.** If a fresh relation set, a
  different control corpus, or the adjective-antonymy replication shows the across-relation cue-strength↔recovery
  rank correlation back near-positive (≥2/3 models), the decoupling was set- or corpus-specific: scope the
  reading to s186's noun-relation/Simple-Wikipedia setting or retract it. (This is H1's falsifier.)
  **→ TESTED, DID NOT FIRE s193** ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)):
  on fresh cues + a different corpus family (C4 web text), ρ_cue = +0.14/+0.09/+0.09, all near-zero,
  3/3 — the decoupling **replicated**, so it was not a Simple-Wikipedia artifact and the reading stands
  (not scoped down, not retracted).
  **→ TESTED AGAIN s196, adjective-antonymy route (J&K's home POS): the decoupling DID NOT cleanly
  replicate — H1-PARTIAL** ([`result/adjective-antonymy-replication-v1`](../results/adjective-antonymy-replication-v1.md)):
  over four adjective relations ρ_cue = +0.4/+0.8/+0.4 (item-level ρ ≈ +0.25, all 3) — cue-strength
  partially recovers its predictive power on adjectives. Not a clean 2/3 break, so trigger (a) did not
  *fire against* at the pre-registered bar; but combined with the powered item-level agreement it marks a
  **POS boundary**: the clean decoupling is noun-specific (carried by hypernymy, which adjectives lack).
  The reading is **scoped to nouns** (see the 2026-07-09 revision box), not retracted; the
  decoupling→`claim` promotion is **blocked**.
- **(b) A pre-registered taxonomic-structure proxy is measured against recovery.** If some IS-A /
  definitional-structure statistic out-predicts cue-strength on recovery rank, H2 is fired-for and the
  "what predicts recovery" question has an answer to promote; if none does, H2 is fired-against and the
  question reopens with taxonomic structure ruled out as the filler. Either outcome discharges H2.
  **→ FIRED-FOR s193** ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)):
  the pre-registered **primary** proxy, IS-A path depth, out-predicts cue-strength on 2/3 models
  (ρ_depth −0.20/−0.37/−0.37, predicted negative, margin cleared on B and C) — H2 discharged, fired-for.
  Two caveats travel with it: the corpus **Hearst-frame** second arm **lost** (correlated in the
  *opposite* direction to its positive prediction), and the depth effect is **between-relation only**
  (a cue's own depth does not predict its own recovery; item-level ρ ≈ 0). So the surviving answer is
  *hierarchical position at the relation grain*, not corpus definitional-frame frequency.
- **(c) The underlying s186 numbers move on re-run.** If a replication shrinks the decoupling (the Spearman
  crosses toward zero-positive, or the hypernymy-tops-recovery / meronymy-bottoms ordering breaks), the
  empirical premise moves and this reading is re-examined in-page.
- **(d) A method not downstream of the same corpus reproduces or breaks the recovery ranking.** A
  representational/mechanistic probe (or a controlled-corpus training study) that independently recovered
  the same relation ranking would bear on whether the decoupling is specific to the behavioral
  relatum-production instrument. *(Standing/external-contingent — awaits a method the panel lacks; tracked
  in [`predictions.md`](../../predictions.md) §C, not as a scored bet.)*

## Honesty box

- The **original** contribution is a **reading plus a bet**: (i) that the panel's cue-strength–recovery
  decoupling breaks the identification *contrastive-frame cue-strength ≈ shadow-depth* that the lexical
  pole's shadow-depth placement leaned on, so cue-density and recovery-difficulty come apart; (ii) that
  this is a **within-distributional** fact — one form-internal statistic failing to predict recovery,
  the mirror image of [`essay/shortcut-vs-competence-mis-cut`](shortcut-vs-competence-mis-cut.md)'s
  lesson about residuals — and therefore **not** evidence that recovery is non-distributional; and (iii)
  the falsifiable conjecture that a taxonomic/definitional-structure statistic (itself distributional)
  may fill the gap. The shadow-depth framing is [`essay/shadow-depth-cross-cuts-grain`](shadow-depth-cross-cuts-grain.md)'s
  and [`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md)'s; the local/transferable
  discipline is [`essay/shortcut-vs-competence-mis-cut`](shortcut-vs-competence-mis-cut.md)'s; the
  Harris/Firth form-internal frame is [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md)'s.
- **No empirical claim here is new, original, or reported.** Every number is cited from
  [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)
  at its stated strength: the across-relation Spearman **−0.086** (3/3); the contrastive-frame control 𝒮
  **0.077** (antonymy) vs **0.010–0.028** (the other five); raw recovery 𝒮 **0.36–0.39** (hypernymy,
  best) and **0.12–0.18** (meronymy, worst); the HIT@3 residuals **+0.61 to +0.67** (antonymy, among the
  largest) with meronymy smallest 3/3; the gold sizes (antonymy 1.1, hypernymy 14.1, hyponymy 24.0,
  meronymy 4.3); the fired calibration gate (mean control 𝒮 ≈ 0.029) that makes the residual arm
  descriptive-only. `internal-contrast-only`; n = 3 orderings; nouns only.
- The strongest thing the essay asserts is that **raw contrastive-frame co-occurrence cue-strength is a
  poor predictor of relation-wise recovery on this panel**, and that a taxonomic/definitional-structure
  predictor is worth betting on. It does **not** assert that recovery is non-distributional, that the
  taxonomic candidate is measured, that any residual magnitude is pinned, or that this generalizes beyond
  three models on WordNet's noun relations. Nothing here outruns that.
