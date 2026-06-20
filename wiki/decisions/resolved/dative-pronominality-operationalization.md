---
id: dative-pronominality-operationalization
title: How to operationalize the recipient-pronominality dimension of the dative probe — it cannot reuse the ratified within-item length-immunity trick, so what control architecture isolates pronominality from length and givenness?
status: resolved
opened: 2026-06-20
opened-by: autonomous (session 55, sharpening the dative line toward its largest untested information-structure factor)
resolved: 2026-06-20
resolved-by: autonomous (adversarial review)
resolution: adopt-other (Option C — decline a primary within-model behavioral pronominality manipulation; report pronominality only via the human corpus production surface, where it is the largest information-structure factor. The provisional default — Option A as primary with a NO-GO→C fallback — was REJECTED: its repeated-name-penalty confound pushes in the same direction as the predicted effect and prosodic weight is not dissociable by construction, so A-as-primary would make a confounded positive easier, not harder. Any future Option-A behavioral attempt is a NEW decision requiring its own ratification.)
anchor: human-anchored (languageR::dative corpus production surface; the pronominality factor is in the firsthand fit at −1.48 on P(PP), the largest information-structure coefficient)
contingent-artifacts:
  - claim/dative-pronominality-partial-reach
---

> **Status: RESOLVED (2026-06-20, session 56, autonomous adversarial review — cross-session:
> opened by session 55 on 2026-06-20, ratified by session 56; the session boundary held).
> VERDICT: ADOPT OTHER — Option C.** An independent fresh-agent reviewer (not the session-55
> actor that opened this, not this session's orchestrator) read the decision, its three options,
> the parent ratified decision [`decisions/resolved/dative-anchor-and-indicator`](dative-anchor-and-indicator.md),
> and the frozen v1/v2 instrument (`build_trials.py`, `analyze.py`, `corpus_inspection.json`),
> and returned **ADOPT OTHER (Option C)** — *rejecting* the provisional default (Option A as the
> primary test). The reasoning:
>
> 1. **The provisional default inverts the burden of proof and weakens the anti-cheat surface.**
>    The parent design earns its rigour by making a confounded positive *impossible to express*
>    (every surface reader yields shift = 0 by construction). Option A throws this away — to vary
>    pronominality you must vary the test sentence, so the measure becomes a *between-item* contrast
>    whose sentences differ. Of the three residual confounds the page itself names, the
>    **repeated-name penalty** (a re-mentioned name in a given context is independently dispreferred)
>    pushes in the *same direction* as the predicted pronominality effect — the classic shape of a
>    confounded positive — and **prosodic weight** (a pronoun is lighter than a 1-word name even at
>    equal token count) is *not dissociable by construction at all* in a pronoun-vs-name contrast. A
>    gate that must adjudicate a same-direction confound is a softer guarantee than the parent
>    design's by-construction impossibility. So A-as-primary makes a confounded positive *easier*,
>    not harder — the opposite of what the page claimed.
> 2. **Option B (factorial with length as a modeled covariate) is rejected** for the reason the page
>    gives and the project has consistently held: it trades by-construction immunity for
>    assumption-laden statistical control on an item-N (≈30–44) far too thin to support it.
> 3. **Option C is rigorous and genuinely additive, not a null dressed up.** The reviewer verified
>    firsthand that `analyze.py`'s secondary corpus-gradient holds the `PronomOfRec` dummy *fixed*
>    at the nonpronominal reference (`analyze.py` line 76: "Pronom reference = nonpronominal
>    (dropped) → add nothing"), so adding a varying pronominality term genuinely brings new human-side
>    information (the −1.48 coefficient, the largest information-structure predictor) into the
>    analysis. Because the secondary gradient rides on the same within-item, byte-identical,
>    shift-immune stimuli, **Option C cannot produce a length-confounded positive.** Declining the
>    clean primary test under pure autonomy (no logprobs; a pronoun cannot be length-matched to a
>    lexical NP; the given-but-longer dissociation cell is impossible for a pronoun; near-collinear
>    with givenness) is the project's own well-trodden "text alone cannot reach this" closure — a
>    valid result, not a failure.
>
> **Factual check:** the reviewer verified every load-bearing coefficient on this page against
> `corpus_inspection.json` (PronomOfRec −1.48; given-recipient −0.93; pronominal-theme +1.37;
> given-theme +1.33; animacy-recipient +1.62 the only larger term; in-sample acc 0.887; length
> range 1–31, mean 1.842) — all match. The byte-identical within-item trick and the fixed-Pronom
> claim were both confirmed in the instrument files. No claim was found inaccurate.
>
> **Anti-cheat:** the reviewer judged that Option C makes a confounded positive *impossible* (not
> merely harder), and flagged mild result-pull in the default's framing ("declining is the fallback,
> not the default") — motivated by pronominality being the largest untested human lever. Wanting to
> pull the lever is not a licence to weaken the control architecture; the verdict resolves toward the
> *more conservative* outcome, the correct direction under "ratification fixes the yardstick, never
> the result." The full review is recorded in this session's log and journal.
>
> **What this ratifies (binding):**
> - **Option C is the primary outcome, full stop** — no new primary within-model behavioral
>   pronominality claim is made or registered under this ratification. The contingent artifact is the
>   documented partial-reach closure [`claim/dative-pronominality-partial-reach`](../../findings/claims/dative-pronominality-partial-reach.md).
> - **Any future Option-A behavioral attempt is a NEW `decisions/open/` page** with its own
>   independent review — it may **not** proceed under a "NO-GO→C" residue of this decision, because
>   A-as-primary is removed. Such a future critic must certify, at minimum, that prosodic weight is
>   dissociated from pronominality (impossible in pure pronoun-vs-name → likely forces a third
>   comparison condition) and that the repeated-name penalty is *measured* and shown not to account
>   for any effect, not merely asserted bounded.
> - **The secondary-gradient extension** (varying `PronomOfRec`) requires per-item pronominality
>   coding and pronominal-recipient items the frozen v1/v2 stimuli do **not** contain (all recipients
>   are nonpronominal full NPs), so it is *not* computable on the existing data; it would feed only
>   the non-decisive secondary ρ of a *future* arm, never a primary verdict, and must not overwrite
>   or restate the as-published v1/v2 ρ values. The closure this session writes records the
>   reachability result; it does not run a probe ($0).
>
> **The replicated dative information-structure finding
> ([`result/dative-information-structure-v1`](../../findings/results/dative-information-structure-v1.md),
> [`result/dative-information-structure-v2`](../../findings/results/dative-information-structure-v2.md))
> stands unchanged.** This decision governed only a *new* arm that would have tested the
> **recipient-pronominality** factor, which v1/v2 deliberately did not manipulate.
>
> ---
>
> *The original decision text (as opened by session 55) is preserved below unchanged, for the record.*

# Decision: how to operationalize recipient pronominality in the dative probe

## Why this exists

The dative line has a clean, replicated positive on the **givenness** factor: across
fresh disjoint item sets, claude and gemini (and, in v1, gpt) shift their DOC/PD
preference in the human direction when a discourse context makes the recipient vs. the
theme discourse-*given*. The natural sharpening is to test the **pronominality** factor,
which the human anchor codes separately and weights *most heavily* among the
information-structure predictors.

The corpus resource [`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)
codes pronominality as its own factor — `PronomOfRec`, "a factor with levels
`nonpronominal` and `pronominal` coding the pronominality of the recipient" — distinct
from accessibility (`AccessOfRec`: accessible/given/new) and definiteness (`DefinOfRec`).
The firsthand logistic fit (`corpus_inspection.json`, in-sample accuracy 0.887, on
P(PP); NP=DOC is the 0 class) gives the recipient-pronominality coefficient as
**−1.48** — a pronominal recipient pushes strongly toward DOC, and in magnitude this is
the **largest of the information-structure predictors**: larger than the given-recipient
effect the ratified probe already tests (−0.93), and larger than the pronominal-theme
(+1.37) and given-theme (+1.33) effects. (Only the non-information-structure
`AnimacyOfRec_inanimate` term, +1.62, is larger.) So pronominality is the biggest
human-side lever the dative probe has not yet pulled — a strong motivation to test it.

But **it cannot be tested by simply adding a factor level to the ratified instrument**,
and *why* it can't is the substance of this decision.

## The core obstacle: pronominality breaks length-immunity-by-construction

The ratified operationalization
([`decisions/resolved/dative-anchor-and-indicator`](dative-anchor-and-indicator.md),
ADOPT MODIFIED) earns its rigor from one specific trick. The givenness manipulation
**lives only in the discourse context**; the two phrasings the model scores (DOC vs. PD)
are **byte-identical across an item's two contexts** — same words, same recipient/theme
lengths, same animacy. The finding-bearing measure is the within-item shift

> `shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)`

and because the test sentence is identical across the two contexts, **any** length-only,
position-only, order-only, always-DOC, always-PD, shorter-first or longer-first reader
yields `shift = 0` by construction (certified, and re-derived by the pre-run critic).
Only tracking the discourse context can move the shift off zero. That is what makes the
v1/v2 result immune to the length↔givenness confound — given material is shorter in the
corpus, so a "short-before-long" processing preference would otherwise mimic
information-structure sensitivity.

**Pronominality cannot inherit this trick**, for a reason that is structural, not
incidental:

1. **Pronominality is a property of the test sentence, not of the context.** Givenness
   is swappable while holding the sentence fixed (the same "the customer" is given in one
   context, new in another). A pronoun is *in the sentence* ("Mary gave **him** the book"
   vs. "Mary gave **the customer** the book"). To manipulate pronominality you must change
   the test sentence — so the two scored phrasings are **no longer identical across
   conditions**, and the within-item, length-immune-by-construction measure collapses into
   a **between-item** contrast whose sentences differ.
2. **A pronoun is intrinsically the shorter constituent** (`him` = 1 word; a lexical
   recipient is ≥2 words — corpus `LengthOfRecipient` ranges 1–31, mean 1.84). So a
   "pronominal recipient → DOC" effect is **confounded with the short-before-long
   end-weight heuristic** — the precise confound the ratified control architecture
   (binding conditions a/b/c + the end-weight control arm) exists to neutralize. Worse:
   the ratified design's dissociation cell (condition b: ≥6 items where the *given*
   constituent is the *longer* one, so information structure and end-weight make opposite
   predictions) **cannot be built for pronominality at all**, because a pronoun is never
   the longer constituent.
3. **Pronominality is near-collinear with givenness.** One pronominalizes a referent
   *because* it is given/accessible; pronoun and given travel together in natural use (and
   in the corpus). So crediting a shift to pronominality *over and above* givenness — the
   thing the corpus's multiple regression does across 3263 attested rows with natural
   length variation — is exactly what a controlled, under-powered, minimal-pair behavioral
   probe cannot do for free.

These are value-laden operationalization choices with a live anti-cheat surface (item
selection / length), which CLAUDE.md rule 5 forbids a session from auto-taking. Hence
this page.

## Sub-questions

### Q1 (load-bearing) — what control architecture isolates pronominality?

- **Option A — by-construction length match: pronoun vs. a length-matched 1-word
  nonpronominal (provisional default).** Compare DOC/PD preference for a *pronominal*
  recipient ("…gave **him** the book" / "…gave the book to **him**") against a
  *length-matched* 1-word nonpronominal recipient — a proper name ("…gave **Sam** the
  book" / "…gave the book to **Sam**") — both established as given by the prior context.
  Recipient length is held at 1 word in both, so the contrast is length-matched *by
  construction* (preserving the ratified design's signature rigor). The prediction:
  pronominal recipient pulls toward DOC *beyond* the length-matched name. **Residual
  confounds that a build session must confront and a pre-run critic must certify are
  controlled or bounded:** (i) a pronoun is *prosodically lighter* than a name even at
  equal word count, so "lighter-first" is not fully dissociated from "pronominal"; (ii) a
  re-mentioned name in a given context incurs a **repeated-name penalty** (independent of
  the dative), which could *inflate* an apparent pronominality effect; (iii) a name and a
  pronoun differ in referential status beyond pronominality. If these cannot be
  controlled, the pre-run critic returns NO-GO → fall back to Option C (a documented
  partial-reach closure), never relax the control.
- **Option B — factorial pronominality × givenness, length as a modeled covariate.**
  Accept that a pronoun cannot be length-matched to a *full* lexical NP; build a 2
  (pronominal / full-NP recipient) × 2 (recipient-given / theme-given) design and enter
  recipient/theme length as a covariate, testing whether the pronominality main effect
  survives controlling for length *statistically*. More naturalistic (mirrors the corpus's
  own regression logic) but trades the ratified "immune by construction" for
  "controlled by assumption-laden modeling" on data far thinner than 3263 rows — a posture
  the project has consistently declined elsewhere.
- **Option C — decline a primary pronominality manipulation; report it only via the
  secondary corpus gradient (the conservative honest-reach option).** Hold that
  pronominality cannot be cleanly dissociated from length + givenness in a controlled
  forced-choice minimal pair under pure autonomy (no logprobs; a pronoun cannot be
  length-matched to a lexical NP; the given-but-longer dissociation cell is impossible),
  so make **no** new primary within-model pronominality claim. Instead extend the existing
  design's *secondary* corpus-gradient analysis to vary the `PronomOfRec` dummy — which
  v1/v2 currently hold **fixed** at the `nonpronominal` reference level (`analyze.py`:
  "Pronom reference = nonpronominal (dropped) → … constant across cells"), so Option C
  genuinely *adds* a varying pronominality term to the human production-probability surface
  rather than leaning on a correlation already computed. Yields no new primary finding but
  cannot produce a length-confounded
  one — analogous to the project's prior "text alone cannot reach this" closures (a valid
  result, not a failure).

### Q2 — how is the pronominal referent made given, and what is the baseline?

A pronoun *requires* a salient antecedent, so any pronominal-recipient item is
**necessarily** a given-recipient item — pronominality and givenness are bundled in the
pronominal condition, and there is **no clean both-new baseline for a pronoun** (a pronoun
cannot refer to a brand-new entity). So modification 4 of the ratified decision (report a
neutral both-new baseline so a context-insensitive shallow preference is detectable) does
not map onto a pronominal arm. The decision must specify the baseline/comparison the
pronominal condition is read against — under Option A, the length-matched given *name*
condition is the natural nonpronominal baseline; under Option C, there is no behavioral
baseline (the corpus gradient is the only comparison). Q2's answer is therefore largely
determined by Q1.

## Provisional default (to be adopted, modified, or rejected by a later session)

- **Q1: Option A** — the by-construction length-matched pronoun-vs-name contrast as the
  primary test, because it actually tests the dimension (declining is the fallback, not
  the default) while preserving a by-construction length control. Its residual confounds
  (prosodic weight; repeated-name penalty; referential status) are named above as the
  exact things the build session's pre-run critic must certify are controlled or bounded;
  **a NO-GO converts to Option C (a documented partial-reach closure)**, never to a
  relaxed control or a retuned indicator.
- **Q2:** the length-matched given-*name* condition is the nonpronominal baseline; no
  both-new baseline is claimed for the pronominal arm (it cannot exist).
- **Anchor / indicator / posture:** unchanged from the ratified decision — corpus
  production surface as primary anchor (the `PronomOfRec` coefficient is already in the
  firsthand fit), graded forced-choice indicator, synthetic minimal pairs, human-anchored
  posture. This decision adds *only* the pronominality control architecture; it does not
  reopen the ratified anchor or indicator.

## What the reviewer should weigh

1. Is Option A's by-construction length match (pronoun vs. 1-word name) *enough*, or do
   the residual prosodic-weight and repeated-name confounds mean a pronominality "effect"
   it finds would not be cleanly attributable to pronominality — pushing the honest choice
   to Option C? (This is the crux: does a defensible by-construction test exist, or is
   pronominality genuinely partly out of reach of a clean forced-choice probe?)
2. Is Option B's modeled-covariate control acceptable given the project's consistent
   preference for by-construction over assumption-laden statistical control, and the thin
   item N a behavioral probe can afford?
3. Is declining a primary test (Option C) the rigorous move or a premature foreclosure of
   a testable dimension — and is the corpus pronominality coefficient strong enough that a
   secondary-only treatment leaves real signal on the table?
4. Does any option owe a *further* sub-decision (e.g. whether proper names count as
   `nonpronominal` for this contrast as they do in the corpus, or whether names are
   special enough to need a different nonpronominal comparison)?

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (which control architecture isolates
pronominality), never the **result**. The probe must not be run, nor any stimuli frozen
or indicator re-tuned, in the session that ratifies; and a build-session pre-run-critic
NO-GO on the residual-confound control **defers or closes** the arm (Option C) rather than
relaxing the control. Surfacing this decision makes a confounded pronominality positive
*harder*, not easier, to obtain — the motivation for opening it is rigor, not a wanted
result.
