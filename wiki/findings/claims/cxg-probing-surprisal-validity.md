---
type: claim
id: cxg-probing-surprisal-validity
title: Surprisal contrast on form–meaning minimal pairs is a valid (but bounded) operationalization of constructional meaning sensitivity in LLMs
meaning-senses:
  - constructional
  - distributional
  - inferential
status: proposed
anchor: pending
contingent-on:
  - cxg-probing-anchor
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: source/weissweiler-2023-cxg-insight
  - rel: supports
    target: claim/formal-competence-aann-ceiling
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: operationalizes
    target: conjecture/function-word-substitutability
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
---

# Claim: surprisal contrast on form–meaning minimal pairs is a valid (but bounded) operationalization of constructional meaning sensitivity

## Statement

Contrasting an LLM's assigned surprisal (equivalently, continuation log-likelihood) between the members of a **form–meaning minimal pair** — a licit instantiation of a construction versus a minimally-different variant that breaks the construction — is taken here to be a **valid operationalization** of the model's *sensitivity to that construction*. (In-repo this is established only for the AANN instance; for constructions generally it is advanced provisionally — see *Anchor* and [`decisions/open/cxg-probing-anchor`](../../../decisions/open/cxg-probing-anchor.md).) Where a human-normed minimal-pair set exists, the per-item surprisal contrast can be regressed against human acceptability/judgment to license a graded claim about whether the model's behavior reflects the construction's constraint structure.

The validity is **bounded** in three specific ways, each of which the claim states up front:

1. **Sensitivity is not meaning-tracking.** A reliable surprisal contrast evidences that the model is *sensitive to the form–meaning unit*; it does not, by itself, evidence that the model has internalized the construction's *characteristic meaning* (the unified/evaluative reading, in the AANN case). This is the same wedge as [`claim/formal-competence-aann-ceiling`](formal-competence-aann-ceiling.md), now stated for the method rather than the task: the contrast is a necessary, not sufficient, condition for a meaning claim.
2. **The frequency confound.** A surprisal gap can be produced by surface-collocation frequency rather than construction knowledge. A valid probe must dissociate the two — through frequency control on swapped items and through held-out lexical material — or its positive result is weak (memorization, not construction).
3. **Anchor-boundedness.** The contrast is interpretable as *meaning* sensitivity only against a human resource that itself measures the form–meaning pairing. Against a pure grammaticality battery it measures only form sensitivity, which is a different (formal-competence) claim.

Because the general, cross-construction version of this claim lacks an adequate in-repo human anchor (see *Anchor* below), its empirical language is provisional pending [`decisions/open/cxg-probing-anchor`](../../../decisions/open/cxg-probing-anchor.md).

## Grounding

### The method is the CxG-probing program's own (Weissweiler et al. 2023)

The methodological warrant is [`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md), the founding methodological statement of the CxG-probing line. The paper frames a construction as a two-sided object — its central move (source page §2.1, verbatim):

> "According to CxG, meaning is encoded in abstract constellations of linguistic units of different sizes."

Probing for a construction is therefore not the same as probing for a syntactic pattern or for a semantic preference in isolation; it is probing for the form–meaning unity. The source page records the paper's review of repurposed probes (masked prediction, **surprisal**, NLI) and of construction-specific minimal-pair probes, and names the minimal-pair design directly (source page §3.3, verbatim):

> "Some works in probing based on Generative Grammar have relied on finding minimal pairs of sentences that are identical except for one specific feature that, if changed, will make the sentence ungrammatical"

That quote is the lineage of the method and also its boundary: minimal pairs inherited *from Generative Grammar* test whether a change makes the sentence **ungrammatical** — a form contrast. Carrying the method into CxG means the contrasted feature must be the **form–meaning pairing**, not merely well-formedness, for the result to bear on `constructional` meaning rather than only on form. This is precisely the distinction Bound (1) and Bound (3) above protect.

### The method's known limit is named by the same source

The paper states that the established minimal-pair / acceptability methodology is limited (source page §3.1, verbatim):

> "While this is a useful starting point for probing, it is also limited... this methodology currently does not tell us anything about if the model has identified the extent of the construction correctly, or if the model has correctly learned how each slot can be filled."

This is the textual basis for Bound (1): a clean surprisal contrast on a single licit/illicit pair leaves open whether the model has the *extent* of the construction and the *slot semantics* right. It tells us the model is sensitive to the contrasted feature; it does not tell us the model has the construction's meaning.

### The frequency confound is named by the same source

The source page records, among the paper's open challenges, the "confound between construction knowledge and memorization of surface collocations." Bound (2) is this challenge applied to the surprisal indicator specifically: a per-token log-probability gap can be carried by the unigram/bigram statistics of the swapped material. The defense the CxG-probing program prescribes — and that this project's AANN design adopts — is held-out lexical material plus explicit frequency control (see [`conjecture/aann-construction`](../conjectures/aann-construction.md) prediction 1, which controls for unigram frequency, and the held-out-adjective requirement in [`decisions/open/aann-operationalization`](../../../decisions/open/aann-operationalization.md)).

## Relation to the companion claim

[`claim/formal-competence-aann-ceiling`](formal-competence-aann-ceiling.md) establishes what a **structural-acceptability ceiling cannot evidence**: matching human acceptability ratings shows formal competence, not constructional meaning-tracking. This claim is its methodological counterpart — it establishes what a **form–meaning minimal-pair surprisal contrast can evidence**, and where that evidence stops. The two are consistent and mutually sharpening:

- The acceptability claim warns that a *form* ceiling is silent on meaning. This claim says the surprisal-contrast *method* is valid for sensitivity but, by Bound (1), is likewise not sufficient for the meaning claim on its own.
- Together they specify the upgrade path: to move from *sensitivity* to *meaning-tracking* requires the gradient / inferential evidence the acceptability claim calls for (adjective-type and noun-type gradients tracking the construction's semantics; or a `constructional` × `inferential` paraphrase probe, Option C in [`decisions/open/aann-operationalization`](../../../decisions/open/aann-operationalization.md)).

The link to the companion claim is `supports`: this claim makes the companion's method-level corollary explicit and gives the positive complement (what the method *can* do) to the companion's negative result (what acceptability *cannot* do).

## What this claim operationalizes

- [`conjecture/aann-construction`](../conjectures/aann-construction.md): its predictions are stated in terms of continuation-likelihood / surprisal contrasts on AANN-licit vs. illicit minimal pairs. This claim is the validity warrant for that indicator (Option A in [`decisions/open/aann-operationalization`](../../../decisions/open/aann-operationalization.md)), including the frequency-control and held-out requirements that make a positive result more than memorization.
- [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md): its predictions compare behavioral shift (KL on continuation distributions, inference flips) after frequency-matched function-word vs. content-word swaps — the same minimal-pair-surprisal logic, with the frequency control (Bound 2) elevated to the core design feature. This claim warrants that the method is valid *provided* the matched-pair set is locked before model outputs are seen.

## Anchor

`anchor: pending`. The only in-repo human-anchored minimal-pair resource is [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md), linked here with `rel: anchors`. It is a **partial** anchor: it grounds the method for the single AANN form–meaning minimal-pair set (with item-level MTurk ratings to regress the surprisal contrast against), but the claim is cast more generally — for form–meaning minimal-pair surprisal across constructions. The Weissweiler source itself names the field-wide "absence of human-normed data for many constructions" as the reason the general anchor does not exist off the shelf.

The anchor question is queued as [`decisions/open/cxg-probing-anchor`](../../../decisions/open/cxg-probing-anchor.md) (provisional default: scope the empirical force of the claim to AANN, treat cross-construction generality as a provisional extrapolation, and do **not** anchor against a Generative-Grammar grammaticality battery, which would re-import the formal-vs-constructional confound that Bound (3) and the companion claim warn against). Until that decision is ratified, the cross-construction generality in the Statement is written as provisional and must not be cited as settled.

## What this claim does not say

- It does not say a surprisal contrast is evidence of constructional *meaning-tracking*. By Bound (1) it is evidence of *sensitivity to the form–meaning unit*; the meaning claim needs the additional gradient/inferential evidence specified by the companion claim.
- It does not say surprisal is the only valid indicator. Prompted acceptability (Option B) and forced-choice paraphrase (Option C) are alternatives with their own validity profiles; this claim warrants the surprisal contrast specifically and notes (Bound 3) that the indicator's interpretation depends on what the human anchor measures.
- It does not endorse a grammaticality minimal-pair battery (BLiMP-style) as a *meaning* anchor. Such batteries anchor form sensitivity; using one to ground a constructional-meaning claim would conflate the two senses the companion claim keeps apart.

## Scope and limits

- The method's validity is demonstrated in-repo only for AANN; the general statement is an extrapolation pending [`decisions/open/cxg-probing-anchor`](../../../decisions/open/cxg-probing-anchor.md).
- Surprisal-contrast probes require the panel models to expose token log-probabilities reliably; where they do not, the fallback is prompted acceptability (Option B), which is a *different* indicator with a different validity argument and is not covered by this claim.
- Status is `proposed`: the validity argument rests on the Weissweiler methodological framing plus one worked, partially-anchored construction. It has not been demonstrated across a multi-construction human-normed battery.
