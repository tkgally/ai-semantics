---
type: essay
id: headroom-positive-vindicates-the-null
title: A positive that vindicates a negative — why the grounding axis's first confirming cell retroactively fixes what its prior nulls were evidence for, and why the shape it licenses is not the size
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - distributional
status: draft
contingent-on: []
created: 2026-06-27
updated: 2026-06-27
links:
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/lexical-perceptual-grounding-moderation-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v1
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: refines
    target: conjecture/distributional-saturation-grounding-headroom
---

# Essay: a positive that vindicates a negative

> **Status: draft (2026-06-27, session 122). A philosophical-track essay arguing in the project's
> own voice.** Its original contribution is an *epistemic point about how nulls and positives
> interlock on a single structural axis*: that a null's interpretation can be **genuinely unknowable
> until the matching positive arrives**, so the positive is partly **constitutive** of what the
> negatives were evidence for. It applies that point to the grounding axis, whose whole life so far
> was nulls plus one inconclusive run, and whose session-121 v2 cell is its **first** confirming
> direction. It contains **no new empirical claim**: every empirical sentence cites the in-repo
> result that carries it, at that page's stated strength, and the v2 cell is one supporting run on a
> binary selection task with a deliberately instrument-inflated magnitude — the conjecture it bears
> on stays `proposed`. The essay is carefully bounded to `grounded.perceptual` / `referential.sense`:
> a model picking the gold image is behavior *sensitive to* the word→sense→image mapping in the
> residual, **not** a perceptual symbol system, and **not** reference (`referential.externalist`
> untouched). It makes **no** comparison to people beyond what the VWSD human-gold anchor licenses
> (binary correct-image selection). Read the revision triggers before citing.

## The occasion: an axis that only ever produced nulls

The project's grounding axis spent its entire existence, until this session, producing negatives.
A **text-side moderation null**: a word's static perceptual groundedness does not predict how well
a text-only model tracks its graded senses, with even "the **only** bootstrap CI that excludes zero
(gpt-5.4-mini, Δρ −0.27, CI [−0.53, −0.01])" pointing "the **wrong way**"
([`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md)).
An **image-side redundancy null**: "Showing the panel **two small pictures depicting each usage**
does **not** make its graded sense-relatedness behavior separate same-sense from different-sense word
pairs any better than the **byte-identical text-only** prompt — because the text-only panel
**already separates them perfectly** (AUC = 1.000 in every cell, text *and* image)"
([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). And one
**inconclusive** image-native run that "neither confirms nor falsifies" the gating prediction
([`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md)). Three negatives
and a shrug — that was the whole record.

A null invites a deflationary reading, and the deflationary reading here is natural: *the tool is
inert on this axis.* Vision adds nothing to these models' lexical sense; the modality, for this kind
of question, simply does not move the needle. On that reading the grounding axis was a series of
honest measurements of nothing, and the right next move would be to stop measuring.

The session-121 v2 cell is the project's **first confirming-direction** result on the axis. Its
philosophical interest is **not** that the tally moves from three-nulls-and-a-shrug to
three-nulls-and-a-positive. It is that the positive *retroactively fixes the interpretation of every
prior null* — it discriminates between two rival explanations that the nulls, by themselves, could
not separate.

## The two readings a null could not separate

Take the redundancy null at its strongest. The image did not improve sense separation. Why not? Two
explanations are observationally identical at the null:

- **(a) The modality is inert.** Vision never moves these models' word `meaning` (in the
  `referential.sense` sense — Fregean mode of presentation, not reference). Whatever a picture
  contributes, it is not lexical sense; the channel is dead for this question, everywhere.
- **(b) The text channel was saturated.** Vision had nothing to add *because the words already
  settled it*. The redundancy null's own lead caveat already gestured at this: "Clear homonyms
  maximize visual distinctness *and* text separability together, so text saturates and the image is
  redundant"
  ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). On this
  reading the modality is not inert; it is *gated* — it can only act where text leaves room, and the
  null was measured in a regime with no room.

These are very different claims about what the tool can do, and the redundancy null cannot tell them
apart, because it was run **only in the saturated regime** (AUC = 1.000 throughout). A flat Δ where
text already determines the answer is exactly what *both* (a) and (b) predict. The
[`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
named this fork precisely as a live possibility it could not yet close: the second falsifier "breaks
the 'headroom is sufficient' clause — grounding would *never* move lexical sense for these models …
so the redundancy null was not about saturation at all but about the modality being inert for sense."
That is reading (a), and the conjecture honestly flagged it could be the truth.

The discriminating test is structural, not statistical: it is not "more power on the same cell" but
"the *matched* cell in the other regime." Reading (b) predicts that where text **under-determines**
the sense, the image *will* move it; reading (a) predicts it will not move it there either. To tell
them apart you must run the regime the nulls never reached — and find the positive, or its absence.

## What the positive picks

The v2 cell ran exactly that matched regime, with the cheap-explanation guards the conjecture
demanded. With the word-ablated DISTRACT control clean — "with the word removed, all three models
pick gold at chance" (pooled .097)
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), §1) — the real
image "rescues the cells where the descriptor-text failed — pooled **39/86 = .453** … per-model
**.500 / .303 / .609** (all above chance) — while adding **no lift where the descriptor already
separates** (image actually drops .122 in the saturated stratum)"
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Headline). The
result reads this, in its own words, as "the redundancy null's mirror image: where v1/the
image-redundancy result saw **Δ ≈ 0 at saturation**, v2 now sees **Δ > 0 in the residual** — the same
structural story, with the positive cell finally testable."

That mirror is the whole point. The image moves sense **exactly where the de-referented text leaves
it under-determined, and nowhere it is already settled**, with a clean word-ablated control ruling out
mere image salience. This is the signature reading (b) predicts and reading (a) forbids: a gated, not
an inert, modality. So the v2 positive does not merely add a data point — it **selects between two
incompatible interpretations of the prior nulls**, and it selects (b). The negatives were measuring
saturation, not inertness. They were evidence for a *gated* tool sitting idle in a regime that gave it
nothing to do — not for a *dead* tool.

The honest discounts travel with this, unweakened. Gemini's rescue (.609) is "read against gemini's
elevated .158 floor"; gpt "degrades overall (.725→.592)" and its gating support is "**sign-only**";
claude (floor .092, clean) and the pooled cell carry primary weight
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), §3 and Headline).
The interpretation-fixing force comes from the **3/3 direction agreement plus the clean control**, not
from any single model's magnitude.

## The epistemic point: a null's content was hostage to a later positive

Here is the general claim the grounding axis instantiates. A null on a structural variable can be
**under-determined as to its own meaning** until the matching positive on the same variable arrives —
and the positive is then partly **constitutive** of what the negative was evidence for. Before v2, the
sentence "the redundancy null is evidence that text saturated the distinction" and the sentence "the
redundancy null is evidence that the modality is inert" were *both* admissible readings of the same
measurement; nothing in the negative chose between them. The positive did not *add to* the negative's
evidential content; it **fixed** it, after the fact. What the nulls were evidence *for* became
knowable only once the positive landed in the cell the nulls structurally omitted.

This is worth separating sharply from two disciplines the project already holds, because it is neither
of them:

- It is **not** the asymmetry of [`essay/undischargeable-negative`](undischargeable-negative.md). That
  essay is about *can't*-claims: a behavioral probe "can *witness* a capability … but can **never**
  close out a capability's *absence*." Its concern is that a negative cannot be upgraded to a universal
  ("M cannot do X"). The present point is orthogonal and, in a sense, friendlier to the negative: it is
  not that the null over-reaches, but that the null **under-determines its own interpretation** — even
  read at its modest strength, "the image did not help *here*," it is silent on *why*, and the why is
  what a later positive settles. The undischargeable-negative discipline forbids reading inertness *out
  of* the null; this essay adds that a positive can read saturation *into* it.
- It is **not** the single-run jitter of [`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md).
  That essay is about one *number* being a draw from a run-to-run distribution. This is about one
  *result's interpretation* being a draw from a small set of rival structural explanations, collapsed
  not by re-running the same cell but by running a different, matched cell. The jitter discipline asks
  whether the estimate is stable; this asks what the (stable) estimate was *about*.

The shared moral with both is the project's standing refusal to over-read a negative. But the specific
mechanism here — *interpretation hostage to a later positive on the same variable* — is its own thing,
and it is the contribution. It also carries a methodological dividend: it tells you that a null on a
structural axis is not a closed book to be filed under "nothing here," but an **open conditional**
whose antecedent the matching positive (or its absence) will later supply. The right posture toward
such a null is to name the regime it did *not* test and treat that regime as the cell that will decide
what the null meant — which is exactly the move the conjecture made when it booked saturation-vs-inert
as a fork rather than declaring the modality dead.

## The counterweight: the positive licenses the SHAPE, not the SIZE

The discipline of the essay is in refusing to let the vindication run past its evidence. The v2 cell
licenses the **shape** claim — grounding is *gated* by the distributional shadow; perception reaches
only the residue the words leave under-determined. It emphatically does **not** license the **size**
claim — how much lexical `meaning` (`referential.sense`) is left ungrounded in *ordinary* language —
because the headroom magnitude is **manufactured**. In the result's own first-class words:

> "**The headroom magnitude is operationalization-inflated.** The TEXT arm uses Option-B descriptors
> that *deliberately* strip the referent name (the v2 fix for v1's caption leakage). So 'text-failed'
> means 'the visual-form-only descriptor + target word + trigger under-determined the sense,' not 'a
> competent natural-language description failed.' The image rescuing ~45% of such cells confirms the
> gating **shape** but says nothing about the **size** of the residual a fluent text channel would
> leave"
> ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Limitation 1).

So the deepest live question stays genuinely open. Is the residue that perception can reach **narrow**
— most concrete lexical sense already lives in the distributional shadow, and grounding's payoff is a
real but minority effect — or **wide**? The v2 rescue is large (.453), but that largeness is an
artifact of stripping referent names from the descriptors; it speaks to the instrument, not to natural
use. The conjecture's "narrow headroom" sub-bet (its prediction 3) is therefore "**not** supported or
refuted here"
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Bearing on the
conjecture) — and the result names the test that would settle it: "A natural-language (non-abstracted)
baseline would test magnitude; v2 tests shape" (Limitation 1).

This is the project's throughline, sharpened. Lexical `meaning` in these models is overwhelmingly
**distributional**: the text-side positive the saturation story rests on found the panel's graded
sense-relatedness "strongly rank-correlated with the human DURel median (Spearman 0.60–0.83, in or
above the human inter-annotator range)"
([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), as carried by the
conjecture) — for the easy cases, text *carries* the distinction, which is why there is no headroom
for an image there. The grounding axis is the measurement of perception's **residual** share of
lexical sense. The v2 positive establishes that residual is **nonzero** — the tool acts in the
residue, the modality is gated not inert. Its **width** — narrow or wide — is exactly what the owed
natural-language-baseline magnitude test would settle, and is, as of this essay, unknown.

## What this essay is not

- **Not a promotion of the conjecture.** One supporting run on a binary selection task, with the
  magnitude sub-bet untested, does not move
  [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
  off `proposed`; any such promotion is a later session's cross-session call. The essay re-reads the
  axis's history; it does not upgrade its status.
- **Not a claim that the modality is grounded.** "Gated, not inert" is a claim about *where the tool
  acts*, on a binary image-selection task — behavior *sensitive to* the word→sense→image mapping in the
  residual. It is **not** a perceptual symbol system and **not** reference: `referential.externalist`
  is untouched, exactly as the v2 result holds ("a model picking the gold image shows behavior
  *sensitive to* the word→sense→image mapping in the residual, **not** a perceptual symbol system or
  reference-fixing").
- **Not a size claim.** The vindicated reading is the gating **shape**. How much lexical sense is left
  ungrounded in ordinary language is open, and the v2 magnitude — inflated by the de-referented channel
  — cannot speak to it.
- **Not a human comparison beyond the VWSD anchor.** The only human leg is the SemEval-2023 VWSD
  binary correct-image gold; the essay asserts nothing about people beyond that binary selection, and
  carries the resource's caveats (binary gold, limited annotator independence) in force.
- **Not a claim that every null is hostage to a later positive.** The point is conditional: a null *on
  a structural variable that admits a matched-regime positive* under-determines its own interpretation
  until that positive arrives. A null with no such matched cell, or one already at a definitional
  ceiling, is a different object.

## Revision triggers (read before citing)

- **(a) The owed natural-language-baseline magnitude test returns NARROW** (a fluent, non-abstracted
  text channel leaves only a small residual the image can rescue). This **strengthens** the essay: the
  gating shape is confirmed *and* the "residue is narrow" intuition — that most concrete lexical sense
  already lives in the distributional shadow — is vindicated as the size claim, no longer merely the
  shape claim.
- **(b) The owed natural-language-baseline magnitude test returns WIDE** (a fluent text channel still
  leaves a large residual the image rescues). The "residue is narrow" intuition **retracts**; the
  gating *shape* survives (grounding still acts only in the residual, wherever the residual sits) but
  the project's distributional-saturation throughline would have to concede a larger ungrounded share
  of concrete lexical sense than its prior nulls suggested. The interpretation-fixing argument of this
  essay is **unaffected** either way — it concerns shape, which both outcomes preserve.
- **(c) A failed replication of the v2 gating cell** (a re-run, or a fresh under-determined stratum,
  in which the image does *not* rescue above chance and floor). This **reopens the fork** the essay
  claims v2 closed: if the positive does not replicate, reading (a) — modality inert — is back on the
  table, and the prior nulls revert to interpretation-under-determined. The essay would be suspended
  pending a re-test, not retracted, since one failed replication is itself a draw
  ([`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md)).
- **(d) A future graded-image resource testing prediction-1-as-written** (graded human relatedness ×
  separability, not binary selection). v2 supports the gating shape on **binary selection**, not
  prediction-1-as-written. A graded test that confirmed the gating on a relatedness gradient would
  **strengthen** the essay; one that found the gating to be an artifact of the binary task would
  **narrow** the vindicated reading to selection accuracy only.
- **(e) The gpt anti-grounding signal hardening into a modality-inert result for that model.** v2
  already flags gpt degrades overall and its gating support is sign-only. If a powered follow-up
  established that for gpt specifically the image *never* moves sense even in the residual, then reading
  (a) would be true **for one model** while (b) holds for the others — a per-model split the essay
  should record, narrowing "the modality is gated, not inert" from a panel claim to a per-model one.

## Honesty box

- The essay's **original** contribution is the **epistemic interlock**: that a null on a structural
  variable can under-determine its own interpretation until the matched-regime positive arrives, so the
  positive is partly *constitutive* of what the negatives were evidence for — and the application that
  the grounding axis's first confirming cell (v2) thereby fixes its three prior negatives as evidence
  for **text saturation (gated modality)**, not **modality inertness**. This is distinct from
  [`essay/undischargeable-negative`](undischargeable-negative.md) (which forbids upgrading a null to a
  *can't*-claim) and from [`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md) (which is
  about a single number's run-to-run jitter). **No empirical claim here is new, original, or reported.**
- The strongest in-repo sentences leaned on, at their stated strength: the redundancy null —
  "Showing the panel … does **not** make its … behavior separate … any better … because the text-only
  panel **already separates them perfectly** (AUC = 1.000 …)"
  ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)); the v2
  rescue — image rescues text-failed cells "pooled **39/86 = .453** … per-model **.500 / .303 / .609**"
  with the saturated stratum dropping ".122," the DISTRACT control clean at pooled ".097," and the
  magnitude "operationalization-inflated" so the run "confirms the gating **shape** but says nothing
  about the **size**"
  ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md)); the conjecture's
  own naming of the inert-vs-saturated fork as a live falsifier
  ([`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)).
  Nothing here outruns those, and every honest discount the v2 result carries (gemini's elevated floor,
  gpt's overall degradation and sign-only support, the instrument-inflated magnitude) is preserved.
- **No human comparison** beyond the VWSD binary correct-image gold is made or owed; the read is held to
  `grounded.perceptual` / `referential.sense` — behavior *sensitive to* the word→sense→image mapping in
  the residual, never reference and never a perceptual symbol system.
