---
type: design
id: lexical-relation-shadow-saturation-v1
title: "lexical-relation shadow-saturation probe v1 — is antonymy the relation whose panel relatum-recovery is least separable from a distributional/contrastive-frame control (internal-contrast, no human comparison)? DESIGN, not frozen; three gates open"
meaning-senses:
  - distributional
  - inferential
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: operationalizes
    target: conjecture/lexical-relation-shadow-saturation
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
---

# Design v1 — lexical-relation shadow-saturation (antonymy internal-contrast)

**A design + decision-trail unit (program A1b). Status: DESIGN, NOT FROZEN (s184, 2026-07-06).**
Three value-laden gates were routed to
[`decisions/resolved/antonymy-internal-contrast-scoring`](../../wiki/decisions/resolved/antonymy-internal-contrast-scoring.md):
**Q1** (what the distributional control *is*), **Q2** (how "recovery" is scored with no human gold),
**Q3** (the `anchor: internal-contrast-only` declaration). Nothing here is frozen; no `prep.py`
exists yet. This page operationalizes [`conjecture/lexical-relation-shadow-saturation`](../../wiki/findings/conjectures/lexical-relation-shadow-saturation.md).

> **Update (2026-07-06, session 185 — GATES RATIFIED, still not frozen).** The decision
> [`decisions/resolved/antonymy-internal-contrast-scoring`](../../wiki/decisions/resolved/antonymy-internal-contrast-scoring.md)
> **ratified ADOPT DEFAULTS** (fresh adversarial reviewer **+** one non-Anthropic decorrelation vote,
> converging): **Q1-C** (faithful contrastive-frame G² control primary + labelled embedding sensitivity,
> the run gated on a corpus license scout), **Q2-A** (WordNet-target Soundness hit-rate residual), **Q3
> `internal-contrast-only`** (now set in front-matter; `contingent-on` cleared). Four freeze-time
> conditions are recorded on the resolved decision; the load-bearing one is **condition 1 (clause-2
> granularity):** Cao-2025b ranks only **four** relations (ANT/SYN/HYP/HOL — it collapses hyper/hypo→HYP
> and holo/mero→HOL), but this probe tests **six**, collapsing exactly the hyponymy and meronymy the
> design names as the "larger residual" contrast set; at freeze, clause 2 must either have the Q1-A
> corpus supply a **6-relation** cue-strength ranking (preferred — baseline does double duty) or be
> restricted to Cao's 4-relation mapping with the collapse reported. Conditions 2–4 (proxy-corpus fence;
> "contrastive-frame G²" is the project's own synthesis, frozen in `prep.py`; the Q3 gloss covers
> model-vs-distributional-baseline) are carried into the freeze. **Still DESIGN, NOT FROZEN** — the run
> owes its corpus license scout, the `prep.py` freeze + PREREG, the pre-run critic + non-Anthropic vote,
> then the run. Per [`program.md`](../../wiki/program.md) A1b: **design s184, ratified s185, run s185+.**

---

## The one question (nothing wider)

On a same-task **relatum-production** probe over the six WordNet lexical relations (hypernymy,
hyponymy, holonymy, meronymy, antonymy, synonymy), run on the panel against a **distributional /
contrastive-frame co-occurrence control**: is **antonymy the relation whose model recovery is
*least separable* from the control** — the smallest "over-and-above the distributional shadow"
residual — while meronymy / hyponymy retain a larger residual? Equivalently: does the across-relation
ranking of *raw* recovery track how strongly each relation is distributionally/contrastively cued,
with antonymy at the top of both?

This is the conjecture's internal-contrast form. It makes **no human comparison** (Q3): both the
model and the control try to recover the *same definitional target* (the WordNet relatum), and the
finding is a **within-instrument, model-vs-baseline contrast**, not a model-vs-human competence
claim. The human-compared form stays blocked on its unlicensed anchor (Cao's `ProbeResponses`; no
`LICENSE` file, 2026-06-29) and is out of scope here.

## Grounding in the sources (verbatim)

- **Antonyms co-occur more than chance, and distinctively.** Cao, Yamada & Tokunaga 2025 (COCA,
  17,718,403 sentences), [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../wiki/base/sources/cao-2025-distinctive-cooccurrence-antonymy.md):
  *"We find that antonymy is distinctive in three respects: antonym pairs co-occur with high
  strength, in a preferred linear order, and within short spans."* Strength is measured by **G²**
  (log-likelihood ratio, Dunning 1993, chosen over raw counts/PMI which are *"biased toward extremely
  low or high frequencies"*); *"Antonymy pairs consistently yield both the highest G² scores (ranging
  from 915 to 11,144) and the largest percentage (at least 91%) of significant co-occurring pairs
  across all PoS."* This is the **independent cross-relation cue-strength ranking** the conjecture's
  confirmation clause 2 calls for (ANT distinctively above SYN/HYP/HOL, across POS). The same source
  states the shortcut hazard verbatim: models *"might take advantage of those intra-sentential
  co-occurrence characteristics, using them as a shortcut … rather than relying on knowledge of
  antonymy."*
- **The contrastive/parallel frame is the antonymy signature.** Justeson & Katz 1991 (Brown Corpus,
  predicative adjectives), [`source/justeson-katz-1991-antonym-cooccurrence`](../../wiki/base/sources/justeson-katz-1991-antonym-cooccurrence.md):
  *"antonymous adjectives do co-occur within the same sentence much more often than is expected by
  chance"*; *"we find a strong trend for the antonyms to occur in syntactically parallel and usually
  lexically identical structures"* — **63% (139/219)** of antonym co-occurrences are in lexically
  identical structures, **75% (164/219)** in conjoined structures. This grounds the **frame-ablation
  arm**. **Design fence (do not over-read the source):** J&K catalogue *conjunction* and
  *repeated-frame substitution*; they do **not** catalogue the specific strings "neither X nor Y" /
  "from X to Y" / "X versus Y" (those are the conjecture's own construction, a later-literature
  extension). J&K is adjectives-only and pre-LLM; extension to nominal antonymy is an extrapolation.
- **The model-side antonymy outlier (what this probe tests on the panel).** Cao et al. 2025,
  [`source/cao-2025-semantic-relation-knowledge`](../../wiki/base/sources/cao-2025-semantic-relation-knowledge.md)
  (BERT/RoBERTa + Llama-3, **not** the panel — the gap does not transfer without re-running): *"All
  models perform relatively well for antonymy, where the best model … achieves 𝒮=0.57, whereas for
  other relations, best values typically lie around 𝒮=0.30."* The probe adapts this source's
  **Soundness** metric — 𝒮(r;m) = *"the extent to which words predicted by m are valid relata for
  relation r"* — as its recovery score.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Internal-contrast only.** No human comparison. A small antonymy residual means the panel's
   antonym recovery is barely separable from a *distributional* control; it does **not** compare the
   panel to human competence.
2. **Local, not transferable.** Per the s151 relabeling the conjecture inherits, a *surviving*
   residual grades *local* vs *transferable* distributional generalization; it does **not** certify
   "competence beyond distribution." A small residual is the conjecture's central prediction; a large
   one falsifies the *local-shadow* reading only.
3. **Production, not discrimination.** The bet is about axis (1) relatum production/recovery
   (*"given a cue and the relation 'antonym', produce an appropriate opposite"* — where antonymy is
   easy), **not** axis (2) antonym-vs-synonym discrimination
   ([`essay/antonymy-outlier-distributional-shadow`](../../wiki/findings/essays/antonymy-outlier-distributional-shadow.md)).
4. **n = 3 models; read orderings, not coefficients.** The verdict is an across-relation *ranking*
   direction on ≥2/3 models, never a pooled coefficient.

## Panel & settings

Panel = the three `config/models.md` slots (`panel.A`/`.B`/`.C` — never hardcode slugs); all three
as subjects, cross-model divergence is data. Temperature 0, zero-shot, single-turn, neutral system
prompt. `google/*` gets `reasoning={"effort":"minimal"}` (config/models.md caveat). Every call
records `usage.cost` via `experiments/lib/openrouter.py`.

## Design — item scheme (WordNet relation pairs)

Items are built from **WordNet 3.0** via `nltk` ([`resource/wordnet-sense-inventory`](../../wiki/base/resources/wordnet-sense-inventory.md);
WordNet 3.0 License, BSD-style, **verified** in-repo; `pip install nltk numpy` + `nltk.download('wordnet')`
per prior in-repo idiom). WordNet is the **definitional relation source** (matching Cao 2025b's own
ANT/SYN/HYP/HOL inventory), *not* a human-comparison anchor — it defines what counts as a relatum;
it is not a graded human judgment.

- **Relations (6):** antonymy (`lemma.antonyms()`), synonymy (synset co-members), hypernymy,
  hyponymy, holonymy, meronymy (part/member/substance pooled or split — a **prep choice to fix at
  freeze**). Antonymy is the focal relation; the other five are the contrast set.
- **POS:** adjectives are antonymy-richest (J&K); WordNet nominal antonymy is sparse (Cao 2025b: ~97
  nominal ANT pairs vs 11,664 nominal HYP). **Prep choice to fix at freeze:** adjectives-primary with
  a noun stratum where pairs exist, POS reported per relation. Do **not** pool across POS in scoring.
- **Cue items, powered N (per relation):** because the verdict is a **per-relation residual
  ranking** (antonymy's residual vs the other five), powered N applies **per relation**: target
  **~120–150 cue-relation items per relation** where WordNet supplies enough pairs, for **~600–900
  verdict-bearing items total** across the six (PROTOCOL §4, applied to each residual, not to the
  pooled set). **Antonymy is capped lower by WordNet sparsity** (Cao 2025b: ~97 nominal ANT pairs vs
  11,664 nominal HYP), so its stratum may be smaller and **is reported as such** — a per-relation N,
  not a single pooled N, is stated at freeze. Cues are **frequency-matched** on `Lg10WF` from
  [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md) so raw recovery
  differences are not a frequency artifact (SubTLEX-US *does* supply the unigram frequency control,
  even though it supplies **no** co-occurrence data — see Q1). Cao 2025b's imbalance caveat (nominal
  ANT G² inflated by a few outliers like *man/woman*, *parent/child*) is a **stratification hazard**:
  exclude or cap the highest-G² outliers so the ranking is not one-pair-driven.
- **Per cue:** the model produces up to *k* relata for the named relation (Cao's open-ended format,
  k≈3–5, fixed at freeze); the control produces its own ranked *k* candidates (Q1). Both are scored
  against WordNet relatum membership (Q2).

## GATE Q1 — the distributional control (RATIFIED s185: Q1-C — faithful G² primary + labelled embedding sensitivity, run gated on a corpus license scout)

**The crux the s182/s183 scouts surfaced: there is NO co-occurrence data in-repo.** SubTLEX-US is a
pure **unigram** frequency norm (no bigram/co-occurrence column), and its underlying 51M-word
subtitle corpus is **not** in-repo (only the sha-pinned frequency list is, and it is gitignored). So
the contrastive-frame co-occurrence baseline the conjecture specifies **cannot be computed from any
in-repo artifact** — it must be built from a fetched corpus or substituted. Options (provisional
default marked; ratify at s185):

- **Q1-A — contrastive-frame co-occurrence (G²) from a fetched, license-verified corpus.** Faithful
  to Cao 2025b's method and to the conjecture's "special weight on symmetric contrastive frames."
  **Cost:** a corpus fetch + a **license scout** (a sub-step; candidates: an open OpenSubtitles /
  Wikipedia dump, or a UD-linked corpus — program A6 notes UD treebanks are in-scope). Blocks the run
  on that scout. This is the control that actually tests the *contrastive-frame* shadow.
- **Q1-B — static-embedding cosine as the distributional control.** In-repo-buildable (a
  license-clean static embedding), no corpus fetch. **But** it measures *general distributional
  similarity*, not *contrastive-frame co-occurrence* — a **different, weaker shadow**. Known wrinkle
  (which is partly the point): antonyms sit *close* in embedding space, so a cosine baseline already
  "predicts" antonyms well — but via similarity, not via the contrastive frame the conjecture names.
  Risk: a small antonymy residual under Q1-B could be read as confirming the conjecture when it only
  shows antonyms are distributionally *similar*, not that the model rides the *contrastive frame*.
- **Q1-C (provisional default) — Q1-A primary + Q1-B as a sensitivity check**, reported side-by-side,
  **iff a corpus clears the license scout**; if none does, A1b's *run* waits on the corpus scout and
  this design ships as design-only (an honest block, not a downgrade to the weaker control). The
  frame-ablation arm (below) is the within-model complement that needs no external corpus and can run
  under either.

**Why this is value-laden:** the choice of control *is* the choice of what "the shadow" means. Q1-B
would answer an easier question than the conjecture asks. The decision surfaces whether the weaker
control is acceptable as primary, or whether the faithful control's corpus dependency must be paid.

## GATE Q2 — recovery scoring without a human gold (RATIFIED s185: Q2-A — WordNet-target Soundness hit-rate residual)

How is "recovery" scored when there is no human gold set of correct relata? Options (provisional
default marked):

- **Q2-A (provisional default) — WordNet-definitional target + model-vs-control hit-rate residual.**
  Both the model and the Q1 control produce *k* candidate relata for each cue+relation; each is scored
  by **Soundness** 𝒮 = fraction of produced relata that are WordNet-valid relata of the cue for that
  relation (Cao's metric). The **residual** for relation *r*, model *m* = 𝒮(model) − 𝒮(control). The
  conjecture predicts **residual smallest for antonymy** on ≥2/3 models. This is a clean
  model-vs-baseline internal contrast: WordNet is the shared *definitional target* both recover
  against, not a human competence gradient — so no human comparison enters, and Q3
  (`internal-contrast-only`) follows.
- **Q2-B — per-relation rank-correlation of model vs control relatum scores.** "Least separable" =
  highest correlation between the model's and the control's candidate rankings. More continuous, but
  harder to interpret as a "residual" and more sensitive to the control's calibration.
- **Q2-C — something else** (surfaced for completeness; e.g. a coverage/Completeness 𝒞 pairing).

**Anti-cheat fence (PROTOCOL §B):** the residual definition, the *k*, the stratification, and the
outlier caps are **frozen with the item set before any probe**; no post-hoc tuning of the indicator
after seeing which relation wins. The **null (flat residuals across relations)** and the **inverted**
outcome (a weakly-cued relation recovered best) are pre-named first-class results, not failures.

## Frame-ablation arm (Tier-1 seed #1 — the maintenance-ledger design input)

An in-model manipulation that needs **no external corpus** (so it survives a Q1 block): probe antonym
recovery with the **contrastive frame present vs structurally suppressed**. Two prompt frames per cue,
fixed at freeze:

- **Frame-present:** the cue is embedded in a symmetric contrastive scaffold (e.g. *"___ and its
  opposite: X and ___"* / a conjoined-frame elicitation) — the J&K parallel-frame signature.
- **Frame-suppressed:** a neutral elicitation that names the relation without the contrastive scaffold
  (e.g. *"Give a word that is an antonym of X."* with no parallel frame).

If antonym recovery **collapses** when the frame is suppressed, the panel's antonymy competence is
**frame-cued** (rides the distributional shadow) — the conjecture's mechanism, made a within-model
contrast. If it **survives** frame suppression, that is a partial witness *against* the pure-shadow
reading (the essay's revision trigger (a)). This arm is symmetric across relations (a
contrastive-frame scaffold is antonymy-specific; for the other five it is a control that should *not*
help), which is itself informative.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

- **Primary (verdict-bearing):** the across-relation **ranking of residuals** (Q2). **CONFIRMS** the
  conjecture's clause 1 iff antonymy has the **smallest** residual on **≥2/3** models with meronymy
  and/or hyponymy visibly larger. **SHADOW-SATURATED-FLAT** (the null) iff residuals are flat across
  relations. **INVERTED** iff a weakly-cued relation (e.g. meronymy) is smallest — falsifies the
  cue-strength-tracks-recovery story.
- **Secondary (clause 2):** the across-relation ranking of **raw** model recovery 𝒮(model) is
  positively associated with the independent Cao-2025b **G² cue-strength ranking** (ANT top), on
  ≥2/3 models. Either clause alone is weak; **both same-direction on ≥2/3** is the central bet met.
- **Frame-ablation (descriptive/mechanistic):** the antonymy recovery drop from frame-present to
  frame-suppressed, per model — read as the *degree* to which the competence is frame-cued, not as a
  pass/fail.
- **n = 3, orderings not coefficients** (scope cap 4). No pooling across models or POS.

## GATE Q3 — anchor declaration (RATIFIED s185: internal-contrast-only)

Provisional default: **`anchor: internal-contrast-only`** — a ratified terminal declaration that the
result makes **no human-comparison claim** (its force is a model-vs-control within-instrument
contrast), so no `resource` anchor is required (CLAUDE.md; the terminal state introduced 2026-05-31,
now ratified via the autonomous cross-session procedure). This follows directly from Q2-A. Per
CLAUDE.md this declaration itself requires cross-session adversarial ratification — it is one of the
questions the queued decision carries. Until ratified the design stays `anchor: pending` with the
decision named in `contingent-on:`.

## Cost (pre-flight estimate)

Relatum production is short-output, temperature 0. ~120–150 cue-relation items per relation × 6
relations (≈600–900 verdict-bearing items, antonymy capped lower) × (frame-present +
frame-suppressed) × 3 models ≈ 4,300–5,400 calls at short completions. At observed panel prices
(gpt/gemini cheap on short outputs; the s181/s178 lexical runs billed $0.31–$0.69 at ~1,800 calls)
this projects **≈ $0.8–$1.6** — comfortably inside one UTC day's $5 cap, single-run under the
prefer-split $2.50 flag. A hard `ABORT_USD` (≈ $2.5) goes in `prep.py` at freeze. **Q1-A's corpus
fetch is $0 (bandwidth), but its license scout is the gating sub-step, not the model spend.** The
pre-flight is re-estimated at freeze once k and N are fixed.

## What each outcome feeds

- **CONFIRMS (antonymy smallest residual, ≥2/3):** supports
  [`conjecture/lexical-relation-shadow-saturation`](../../wiki/findings/conjectures/lexical-relation-shadow-saturation.md)
  clause 1; a shadow-depth-table "saturated corner" row gains a *measured* internal-contrast residual
  (currently a marked reading/bet). Does **not** move antonymy to a beater; a small residual is the
  shadow reading.
- **SHADOW-SATURATED-FLAT / INVERTED:** the null / inversion — writes honestly against the conjecture
  (clause-1 falsified for the local-shadow reading, or the cue-strength story fails). A first-class
  negative.
- **Frame-suppression survives (any model):** a partial witness firing the essay's revision trigger
  (a) — logged, not over-read (survives falsifies the *local*-shadow reading only, per scope cap 2).
- **Registers a `predictions.md` row** at freeze (the antonymy-smallest-residual bet), outcome scored
  the run session.

## Handoff (what s185 does, and what remains)

1. **Ratify** [`decisions/resolved/antonymy-internal-contrast-scoring`](../../wiki/decisions/resolved/antonymy-internal-contrast-scoring.md)
   (fresh reviewer + one non-Anthropic vote): fix Q1 (control), Q2 (scoring), Q3 (anchor).
   **✅ DONE s185 — ADOPT DEFAULTS (Q1-C / Q2-A / Q3 internal-contrast-only), both reviewers converged.**
2. If Q1 resolves to A/C: run the **license scout** for a co-occurrence corpus first (own resource
   page + verified license; never adopt unverified — s168 discipline). **Q1 resolved C → scout owed;
   run s185 (see the [`base/resources/`](../../wiki/base/resources/) scout page + `NEXT.md`).**
3. **Freeze (remaining):** write `prep.py` (WordNet item build, frequency-matched, outlier-capped),
   fix k / N / thresholds / verdict map — honoring the four ratified freeze-time conditions, chiefly
   **condition 1** (clause 2 must resolve Cao's 4-relation vs the probe's 6-relation cue-strength
   granularity) — commit PREREG before any model call; independent pre-run critic + one non-Anthropic
   vote; `ABORT_USD` set.
4. **Run (remaining)** on the panel; post-run verifier recomputes from raw. Powered N per PROTOCOL §4.
