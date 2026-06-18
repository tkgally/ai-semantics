---
type: essay
id: capability-split
title: A capability split is not a panel property — what a one-model positive licenses, and the reporting discipline a split forces
meaning-senses:
  - model-internal
  - relational
status: draft
contingent-on: []
created: 2026-06-18
updated: 2026-06-18
links:
  - rel: depends-on
    target: result/relational-order-composition-c
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: refines
    target: essay/update-is-not-constitution
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/formal-vs-functional-competence
---

# Essay: a capability split is not a panel property

> **Status: draft (2026-06-18). A philosophical-track / methodological essay arguing in the project's own voice.** Its original contribution is a *reporting discipline*, not an empirical claim: when a panel **splits** on a probe — some models pass, some are uninterpretable — the finding must be attributed to the **model(s) that showed it**, never averaged into a claim about "the panel" or "LLMs." There is **no new empirical claim** here and **no human comparison** anywhere (the result it reads, [`result/relational-order-composition-c`](../results/relational-order-composition-c.md), is `internal-contrast-only`; the human leg is unanchored in-repo). Every empirical sentence cites the in-repo page that carries it, at that page's stated strength, and the recommendation is hedged as a recommendation throughout. Read the revision triggers before citing.
>
> **Revision (2026-06-18, later session — evidence moved, logged per essay discipline).** The essay was written when the Option-C probe had run on **two** models (claude RESPECTS-ORDER, gemini UNINTERPRETABLE). Its **revision trigger (a)** — "a third (or further) composing model" — was then tested directly: the same frozen instrument was re-run on `gpt-5.4-mini` (panel.B, the third panel model). gpt did **not** compose: it failed the on-demand gate harder than gemini (DIRECT 0.194 < 0.80 → **UNINTERPRETABLE**), so trigger (a) did **not** fire in the composing direction. The effect on the argument is to **sharpen**, not overturn it: order-sensitive composition is now confirmed a **one-of-three** capability (claude alone), with **two** separately-trained models unable to compose two non-commuting moves on demand in this instrument. The thesis (read splits as splits; never average) stands, strengthened. Sentences below that said "two-model" / "both panel models" have been updated to the three-model panel; the "thing to watch" widens from *claude > gemini* to *claude > {gemini, gpt}*. Trigger (a) stays **live** for any *further* model that might compose.

## The occasion

The relational ladder built in [`essay/update-is-not-constitution`](update-is-not-constitution.md) had, until 2026-06-18, two firm rungs, and both were occupied by **both** panel models at ceiling. Rung (i), order-sensitive overwrite, is a both-model positive ([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md): "both panel models … recover the term by its **most-recent binding**", SPONT latest-binding rate 1.000). Rung (ii), integration in its survival sense, is likewise both-model (the integration result is reported as both models composing at ceiling, carried into the claim's scope limit 2). For these rungs the project could write — cautiously — "these models do X," because the two separately-trained models concurred.

Option C broke that pattern. The non-commuting-operation probe ([`result/relational-order-composition-c`](../results/relational-order-composition-c.md)) made composition genuinely order-load-bearing (two stamped moves, STEP and FLIP on a 6-track, whose two orders reach different end states). Its verdict **splits**, and reads the same way across the **full three-model panel**: `claude-sonnet-4.6` orders the two moves by their round stamps spontaneously at ceiling (COMP target **1.000**, Wilson [0.949, 1.000]; DIRECT on-demand gate **0.861** PASS) — **RESPECTS-ORDER**; `gemini-3.5-flash` **cannot compose the two moves even when told the order** (DIRECT gate **0.583** < 0.80) — **UNINTERPRETABLE**; and `gpt-5.4-mini`, run later on the byte-identical instrument, fails the on-demand gate harder still (DIRECT **0.194** < 0.80) — **UNINTERPRETABLE**. This is the **first relational rung that splits the panel** — and the split is now confirmed a **one-of-three** picture: claude alone composes; two separately-trained models cannot. The result page states the consequence in its honesty box without softening it: the positive is "**one of three models, not the panel — narrower than rungs (i)–(ii), which both models cleared**" ([`result/relational-order-composition-c`](../results/relational-order-composition-c.md), Honesty box).

This essay argues what that split forces methodologically. The argument is about **attribution and reporting**, not about which model is better.

## The core thesis: a one-model positive is not a property of "the models"

Take the two earlier rungs and ask what licensed their phrasing. Rung (i) and rung (ii) were stated as if about a *kind* — "both panel models," "LLM referential conventions are order-sensitive." That phrasing was warranted, but for a narrower reason than it reads: the panel happened to **concord**. Two separately-trained models cleared the same bar, so a (cautious) generalization over "these models" had two concordant instances behind it. The both-model ceiling did the licensing work; the kind-level phrasing rode on the concordance.

When the panel splits, that licensing evaporates. A one-model positive is **not** evidence about "the models" or about "LLMs" as a class — it is a **capability split**: a statement that one specific model does X and another, on this instrument, does not (here, cannot). The unit of the finding is the model, not the panel. Spell the contrast out:

- A **both-model ceiling** licenses a cautious *"these (two, separately-trained) models do X."* The concordance is the evidence; the generalization is bounded to the panel and still under-claimed.
- A **one-model positive** licenses only *"`claude-sonnet-4.6` does X (in this instrument); `gemini-3.5-flash` and `gpt-5.4-mini` do not / cannot here."* No panel-level sentence is licensed, because two-thirds of the panel supplies no usable signal.

The earlier rungs' "both panel models" framing silently presupposed concordance. The split shows that concordance is a *contingent fact about those runs*, not a safe default — and where it fails, a finding that quietly inherits the kind-level phrasing would be over-attributing one model's behavior to a class the evidence does not cover.

## What a one-model positive licenses, and what it forbids

A split positive is **genuinely weaker** than a both-model result. The project does not have to argue this from first principles; the result page already concedes it (the positive is "narrower than rungs (i)–(ii)", quoted above). Concretely:

- It **forbids** a class claim. One model spontaneously ordering two non-commuting operations is *not* evidence that "LLM order-sensitive composition" is a property of current models in general. The second model in this very panel failed the on-demand gate. Generality is bounded, and the result page names the untested directions explicitly — "other operation pairs, >2 moves, image referents, cross-family dyads, a panel that can all compose" ([`result/relational-order-composition-c`](../results/relational-order-composition-c.md), Honesty box).
- It is **not nothing**, either. A one-model positive is an **existence result**: at least one current model spontaneously orders two non-commuting operations by their stamps at ceiling, with transparent reasoning (the result records claude "routinely writes *'Let me trace the moves in round order'* … before answering"). Existence results are real findings — they establish that the behavior is *available to some current system* — they are just narrowly scoped: an existential, not a universal, and certainly not a property of the panel.

The discipline, then, is to read a split as **one existential plus one (instrument-bounded) negative**, never as a degraded universal. Averaging the two — "the panel respects operation order at a rate of …", or "the models partly do X" — would manufacture a panel-level quantity out of two qualitatively different verdicts, one of which the gate refuses to read at all.

## The negative half is an instrument limit, not a clean null — do not over-read it

The single most important guardrail on this essay: **neither gemini's nor gpt's UNINTERPRETABLE is an "order-blind" null.** The result page is explicit that the gate "**correctly refuses to read**" gemini's COMP rate, because the DIRECT on-demand gate failed — gemini cannot reliably compose the two non-commuting moves *even when told the order explicitly* (DIRECT 0.583). So we "cannot tell spontaneous order-blindness from inability-to-compose" ([`result/relational-order-composition-c`](../results/relational-order-composition-c.md), "gemini — UNINTERPRETABLE"). The honesty box names this as a capability limit: gemini's failure "is a **composition-ability limit, not a parse artifact** … The instrument is simply too hard for it — so it yields no usable order-sensitivity signal." The third model carries the same caveat, more sharply: **gpt-5.4-mini fails the on-demand gate harder (DIRECT 0.194)**, with the bulk of its errors being **single-move** readers (it applies only one of the two stamped moves), so its UNINTERPRETABLE is likewise a composition-ability limit, not a clean order-blind null. Both negatives are instrument verdicts; neither licenses a claim that the model "lacks order-sensitive composition" in general.

What this licenses is therefore strictly bounded. The essay may say: *gemini-3.5-flash cannot compose these two non-commuting moves in this instrument, so the instrument yields no usable order-sensitivity signal for it.* The essay may **not** say: *gemini lacks order-sensitive composition in general* — that would convert an instrument-capability limit into a clean capacity null the data does not support. A different, easier operationalization might let gemini compose; the result simply does not bear on that. This is the same discipline the formal/functional concept page already enforces from another direction: "failure on a world-knowledge task does not show that a model lacks formal linguistic competence" ([`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)) — a failure on a hard instrument bounds what the instrument shows, not what the model can do. Here the bound runs through an on-demand **capability** gate (can-it-compose) before any meaning-side reading is attempted; below that gate, the meaning-side question (does-it-spontaneously-order) is simply unasked.

So the split is **asymmetric in kind**: a positive that is a real existential, paired with a negative that is an instrument verdict, not a capacity verdict. Treating the negative as a clean null would be the mirror-image error of treating the positive as a panel property — both flatten the split into a tidier object than it is.

## The methodological correction: report SPLIT verdicts as splits, never as panel claims

Here is the standing recommendation, scoped carefully. It is a recommendation about **reporting**, grounded in this one split — *not* an accusation that the project has mis-stated past findings. The care matters, so state both halves.

First, the project's past relational/constructional findings stated as "both models" / "the panel" were, on inspection, **already careful**: the order-sensitive-reassignment claim scopes itself to the regime, carries four binding scope limits, and stays `internal-contrast-only` ([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)). The claim did not over-reach to "LLMs"; it said "both panel models," which is what it had. So the recommendation is **not** "the project mis-stated its findings."

Second, the recommendation *is*: the split makes explicit a default the project should not have relied on going forward. "Both panel models" was warranted by concordance, and concordance is now shown to be contingent. The discipline:

> **Concordant vs. split verdicts.** A panel finding should explicitly mark whether its verdict is **CONCORDANT** (every model in the panel cleared the bar) or **SPLIT** (some did, some did not / could not). A SPLIT verdict is **never** averaged into a panel-level claim: it is reported as a per-model existential plus a per-model negative, with the negative further marked **clean null** vs. **instrument-uninterpretable**. A concordant verdict may license a cautious panel-scoped sentence; a split verdict licenses only model-scoped sentences.

The Option-C result already practices exactly this — it reports two verdicts (RESPECTS-ORDER / UNINTERPRETABLE) and refuses to combine them. The recommendation generalizes that practice: make the concordant/split distinction a *named* property of every panel finding, so that no future split can quietly inherit the kind-level phrasing the concordant rungs earned. The cost of not doing so is precisely the over-attribution this essay warns against — one model's existential dressed as a panel property.

## A thing to watch, not a finding: claude > {gemini, gpt} across this probe

One temptation must be named and refused. On *this* probe, claude cleared a gate **two** other models could not — and a reader might reach for "claude is the stronger model." The essay does **not** assert that, and treating it as established would be fabrication of a cross-task pattern. A single probe, on a single operationalization (STEP/FLIP, two moves, two rounds, text figures), is one data point; the earlier relational rungs were *concordant*, so on those the models were indistinguishable. There is no in-repo cross-task tabulation of claude-vs-gemini-vs-gpt outcomes, and none is built here. That two of three models fail *this* instrument is consistent with the instrument being hard, not with a stable capability ranking.

So this is logged as an **open thing to watch**, not a finding: *if* a cross-task pattern of claude outperforming the others were to emerge across several probes, the "watch this" note could be upgraded toward a finding (revision trigger (c)). Until then, the only defensible reading of this split is the local one — on this instrument, one model composed and two could not — with no extrapolation to relative model capability in general.

## Revision triggers (read before citing)

- **(a) A further composing model.** *Partially discharged 2026-06-18:* the third panel model, gpt-5.4-mini, was run on the Option-C instrument and did **not** compose (DIRECT 0.194 → UNINTERPRETABLE), so the split did not widen toward a panel property — it sharpened to one-of-three. The trigger stays **live** for any *additional* model: if some future model run on this instrument (or an equivalent) *composes*, the split widens to a panel-minority or panel-majority picture and the framing must be updated to a graded one. A *majority* would still not license a "kind" claim, but would change the existential's reach.
- **(b) gemini or gpt composing under an easier operationalization.** If a less demanding non-commuting-operation design lets gemini or gpt clear the on-demand gate and then compose, the failure here was **instrument difficulty, not a stable capability gap** — bounding the split to *this* instrument and weakening any "capability split" reading toward "this-instrument split." This is the most likely way the present framing over-reads, and it is now the more salient trigger given that *two* models fail this instrument.
- **(c) A cross-task pattern of claude > {gemini, gpt}.** If, across several distinct probes, claude clears gates the other panel models cannot, the "thing to watch" note above could be upgraded toward an actual finding about relative capability — which this essay explicitly declines to assert on one probe.
- **(d) A panel that all composes.** If a future panel is assembled in which every model clears the on-demand gate and composes, order-sensitive composition would become a concordant rung after all, and the lesson here would narrow to a historical note about one transitional panel.

## What this essay is not

Not a new empirical claim — its original contribution is the **concordant/split reporting discipline** and the attribution argument, a methodological scaffold; every empirical sentence cites the in-repo page that carries it at that page's stated strength. Not a claim that claude is the stronger model — it argues the opposite caution, that one probe licenses no cross-task ranking. Not a claim that gemini or gpt lacks order-sensitive composition in general — only that neither can compose *these two moves in this instrument*, which yields no usable signal for either. Not a claim that the project mis-stated its past findings — those were careful; the recommendation is forward-looking. Not a human comparison — the cited result is `internal-contrast-only`, and no human capability split is asserted or owed.

## Honesty box

- The essay's **original** contribution is methodological: read a split panel as a per-model existential plus a per-model (instrument-bounded) negative, never as an averaged panel claim, and mark every panel verdict CONCORDANT vs. SPLIT. No empirical claim is original here.
- The strongest empirical sentences supported: on the Option-C non-commuting-operation probe, claude orders the two moves by their round stamps at ceiling (COMP 1.000, Wilson [0.949, 1.000]; DIRECT 0.861 PASS); **both** gemini (DIRECT 0.583) and gpt (DIRECT 0.194) fail the on-demand gate → UNINTERPRETABLE ([`result/relational-order-composition-c`](../results/relational-order-composition-c.md)). Nothing here outruns that. The positive is **one of three models, not the panel** — the result page says so verbatim.
- Both negatives are **instrument-capability limits, not clean order-blind nulls**: the gate "correctly refuses to read" each model's COMP rate. The essay therefore makes no claim about gemini's or gpt's order-sensitivity in general.
- "claude is the stronger model" is **not** asserted — it is a single probe; the earlier rungs were concordant; two of three models failing one hard instrument is consistent with instrument difficulty. It is logged as a thing to watch (trigger (c)), not a finding.
- This is **one operationalization** (STEP/FLIP, two moves, text figures). The reporting discipline it motivates is general, but its empirical instance is narrow.
- **No human comparison** is made or owed: the cited result is `internal-contrast-only`, and the human leg of any order/composition contrast is unanchored in-repo.
