---
type: conjecture
id: dative-alternation-information-structure
title: LLMs track the information-structure constraint on dative alternation
meaning-senses:
  - constructional
  - inferential
  - distributional
status: tested
contingent-on: []
created: 2026-05-28
updated: 2026-07-17
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/languageR-dative-corpus
  - rel: depends-on
    target: resource/dais-dative-ratings
  - rel: depends-on
    target: result/dative-information-structure-v1
---

> **TESTED 2026-06-20 (session 51) → CONFIRM, 3/3 panel models.**
> [`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md) ran the frozen
> instrument: every panel model shifts DOC/PD preference in the human direction across the
> information-structure manipulation (given recipient → DOC, given theme → PD), with length and animacy
> held identical by construction, and the effect **survives the end-weight dissociation control** for all
> three. Effect magnitude is sharply decorrelated (gemini +0.52 ≫ claude +0.33 ≫ gpt +0.06, all clearing
> their bootstrap lower bound) — **prediction 3 confirmed**. The secondary corpus-gradient correlation
> (Spearman ρ 0.48–0.83) strengthens but is non-decisive by pre-registration. Human-anchored to
> [`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md). Caveat: single
> panel/date/run, small item N, a graded-preference (not logprob) measure.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The single-run caveat above was
> discharged in stages: the fresh-item v2 ran session 53
> ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md), CONFIRM
> 2/3 — gpt WEAK on that occasion); the A2a powered re-run landed session 175
> ([`result/dative-information-structure-powered`](../results/dative-information-structure-powered.md))
> with **PANEL CONFIRM 3/3 at N=100** — claude +0.316 [0.298,0.334], gemini +0.524 [0.506,0.542],
> gpt +0.056 [0.039,0.074] — so gpt's v2 WEAK did not hold at power (its shift clears zero at N=100,
> recovering its v1 value; the v2 dip reads as founding-N item noise); and the line was promoted
> session 174 as
> [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

> **Graded-acceptability companion anchor ADOPTED 2026-07-17 (session 245, cross-session adversarial
> review — [`decisions/resolved/dais-dative-rating-anchor`](../../decisions/resolved/dais-dative-rating-anchor.md);
> fresh-reviewer ADOPT-A-WITH-MODIFICATION + a convergent non-Anthropic vote).** The
> *"anchor-dependent, non-decisive"* graded-acceptability slot that Prediction 2 and the secondary-confirm
> clause below have reserved since founding — *"graded acceptability ratings if that anchor is adopted"* —
> is now filled by **DAIS** ([`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md);
> Hawkins, Yamakoshi, Griffiths & Goldberg 2020, CC BY 4.0, 50,136 human slider judgments), adopted as a
> **scoped SECONDARY** companion to the primary `languageR::dative` production anchor. **Scope (load-bearing):**
> DAIS grounds the graded human *preference surface* over recipient/theme **definiteness and length** on
> isolated pairs — a genuinely graded human magnitude in the same directional family (pronoun 37.7 →
> longIndefinite 18.3). It does **NOT** anchor the project's discourse-context **within-item givenness
> shift** (a different instrument on byte-identical phrasings, which stays anchored to the production
> *direction* only), and it is deliberately **not** wired as an `anchors:` link on the promoted
> [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md).
> **No result, verdict, or confirm criterion changes** (this fills the yardstick's reserved secondary slot;
> a human-vs-model *magnitude* correlation on DAIS remains a separate, powered, pre-critiqued probe — the
> decision's Option B, out of scope for the adoption).
>
> **Option B RAN 2026-07-18 (session 248) → the secondary-confirm graded-acceptability slot is filled by a
> PARTIAL/dissociated result: VERDICT LENGTH-ONLY** ([`result/dais-graded-preference-correlation-v1`](../results/dais-graded-preference-correlation-v1.md);
> frozen, ratified instrument; 1,200 calls; verifier REPRODUCED). The panel **tracks the human graded
> verb-bias magnitude** (Arm A per-verb ρ +0.61/+0.76/+0.63, and the binding alternating-only control
> survives 3/3 — not merely the memorizable alternating/non-alternating split) and **reproduces the raw
> recipient definiteness/length gradient** (Arm B monotonicity beats chance 3/3), but its recipient
> gradient is **not cleanly a definiteness surface**: the within-length definiteness contrast clears at
> **short** length 3/3 yet **fails at long length 3/3** (end-weight-dominated) → LENGTH-ONLY. This is a
> **secondary, non-decisive** confirmation of the graded-acceptability clause on the *verb-bias* and *raw
> gradient* surfaces, and an honest **null-leaning dissociation** on the clean *definiteness* surface; per
> this conjecture's confirm criterion it **cannot convert or rescue the primary givenness test**, which it
> does not touch. Registered predictions §B bet: **LOST** (TRACKS did not obtain).

> **Operationalization RATIFIED 2026-06-20 (session 50, ADOPT MODIFIED).** The human anchor is
> in-repo ([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md) —
> Bresnan et al. 2007, `languageR::dative`, 3263 corpus observations coded for the
> information-structure factors below plus the NP/PP outcome), and the operationalization decision
> ([`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md))
> is now resolved: corpus production surface as the **primary** anchor (Bresnan & Ford 2010
> ratings an opportunistic upgrade only); a **behavioral graded forced-choice** indicator
> (surprisal / continuation-likelihood is **unavailable under pure autonomy** — no panel
> prompt-logprobs, the AANN surprisal blocker); **synthetic minimal pairs** built to the corpus
> factor structure; and the **load-bearing control** dissociating *length* from *givenness*
> (given material is shorter in the corpus, so a short-before-long preference would mimic
> information-structure sensitivity), now bound by numeric thresholds. The active build spec
> ([`experiments/runs/2026-06-20-dative-information-structure/README.md`](../../../experiments/runs/2026-06-20-dative-information-structure/README.md))
> carries the binding conditions. **Confirm is scored on the within-model preference *shift* in
> the human direction (the corpus-licensed primary test); tracking the human production-probability
> gradient is a secondary, strengthening measure** — see the resolved decision and the revised
> confirm criterion below.

# Conjecture: LLMs track the information-structure constraint on dative alternation

## Statement

The English dative alternation — *Mary gave John the book* (double object, DOC) vs. *Mary gave the book to John* (prepositional dative, PD) — is constrained by information structure (Bresnan & Nikitina 2009 and downstream work): given/discourse-old material tends to precede new material; pronominal recipients strongly prefer DOC. The conjecture: production-style preferences in current LLMs are sensitive to this information-structure constraint, not merely to surface-form frequency.

## Why this is interesting

The DOC/PD choice is one of the most-studied form-meaning pairings in English. The meaning side is partly **constructional** (the two constructions have weakly different semantics — DOC favors a "successful transfer / recipient affectedness" reading) and partly an **inferential** consequence of information structure (what is given vs. new). If LLMs respect the information-structure side without respecting the constructional-semantic side (or vice versa), that is a sharper diagnostic than the usual coarse "do LLMs know syntax" framing.

## Predictions

*(Indicator updated 2026-06-20: the surprisal/continuation-likelihood wording below is superseded by a behavioral graded forced-choice indicator — no panel prompt-logprobs are available under pure autonomy. The predictions are otherwise unchanged. See the ratified blockquote above and [`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md).)*

1. In a minimal-pair production-preference probe (a graded forced-choice between DOC and PD given a controlled discourse context), LLMs prefer DOC when the recipient is given/pronominal and the theme is new, and prefer PD when the theme is given/pronominal and the recipient is new.
2. The effect is **graded**, not categorical: the model's preference strength should track the human signal (the corpus production-probability surface, or graded acceptability ratings if that anchor is adopted) on parallel items rather than flipping at a hard threshold.
3. Effect size will vary cross-model in a way that decorrelates from surface accuracy — i.e., two models with similar overall benchmark performance can differ in how cleanly they track information structure here.

## What would confirm / falsify

- **Confirm (primary, corpus-licensed):** the model's DOC/PD preference **shifts in the human direction** across information-structure conditions (given/pronominal recipient → DOC; given/pronominal theme → PD), with length and animacy held constant, across at least 30 controlled minimal-pair items, in at least two of three panel models. *(Modification ratified 2026-06-20: confirm is scored on this within-model shift — the test the corpus production surface licenses. The original standalone "human acceptability scores/ratings" clause is the Option-B/C path only.)*
- **Strengthens a confirm (secondary, anchor-dependent, non-decisive):** the model's per-condition preference also tracks the **human gradient** — the corpus-model predicted PP/NP production probability per factor configuration (Option A), or Bresnan & Ford 2010 graded acceptability ratings (Option B, if that anchor is verified and adopted). This secondary correlation may strengthen a confirm or characterize a weak result, but **cannot on its own convert a weak result to a confirm, nor rescue a failed primary test.**
- **Weak:** the primary preference shift exists but does not track the human gradient — the model has a surface preference but not graded information-structure sensitivity.
- **Falsify:** preference flips with shallow confounds (recipient/theme length, animacy of theme) but **not** with the information-structure manipulation when length and animacy are controlled (the length-matched given/new control arm).

## Human anchor (resolved)

→ **Resolved into the in-repo anchor + the ratified operationalization decision (2026-06-20):**
the corpus is catalogued as [`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)
(Bresnan et al. 2007, `languageR::dative`); the anchor-choice question (corpus production surface
— **adopted as primary** — vs. Bresnan & Ford 2010 ratings — an opportunistic upgrade only) plus
the indicator and the length/givenness control were the three sub-questions of
[`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md),
ratified ADOPT MODIFIED.

## Notes / caveats

- The construction is **English-specific** in this exact form. A cross-linguistic version is more ambitious; bracket it.
- Information structure is itself underdetermined without a discourse model; control discourse explicitly in the stimulus.
- Watch for the operationalization-tuning failure mode: do not refine the stimulus set after seeing the first batch of model outputs (charter §8).
