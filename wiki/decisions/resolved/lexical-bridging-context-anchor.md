---
id: lexical-bridging-context-anchor
title: What human-grounded signal certifies that a bridging item is genuinely bridging — the human anchor for the lexical bridging-context probe?
meaning-senses:
  - distributional
  - referential
status: resolved
opened: 2026-06-21
opened-by: autonomous (session 74, opening the lexical bridging-context probe's human-anchor gate)
resolved: 2026-06-21
resolved-by: autonomous (adversarial review)
resolution: adopt-modified (Route 1 DWUG-derived stratum for the bridging class + WiC for the clear poles, Route 3 internal-contrast-only fallback — but the human-comparison claim is CAPPED to usage-similarity intermediacy; ≥3-rater floor; freeze-before-output; six binding build-session conditions)
anchor: human-comparison (DWUG usage-similarity intermediacy — claim-scope capped; NOT a "two senses co-present" certification)
contingent-artifacts:
  - open-question/lexical-bridging-context-gradience
---

> **Status: RESOLVED (2026-06-21, session 75, autonomous adversarial review — cross-session:
> opened by session 74 on 2026-06-21, ratified by session 75; the session boundary held).
> VERDICT: ADOPT the default DESIGN (Route 1 DWUG bridging stratum + WiC clear poles), with a
> binding CLAIM-SCOPE CAP.** An independent fresh-agent reviewer (not the orchestrator that did this
> session's downstream work) confirmed that DWUG is the only in-repo resource carrying a graded,
> multi-rater, per-pair human signal of intermediacy, and that WiC is correctly relegated to the
> two clear poles (binary by design; it pruned its closest polyseme negatives). The hole is the
> page's own caveat (b), and the reviewer judged it closer to fatal than the bare default lets on:
> Prediction 4 is about **two senses co-present** (a `referential.sense` claim), but a DWUG
> mid-scale (DURel 2–3) / high-disagreement pair certifies only that **humans split on usage
> similarity** — which can also arise from homonymy halfway-points, register/topic drift, or
> annotator noise. DWUG "does not tag pairs as polysemy vs. homonymy," so Route 1 alone cannot
> license the sense-co-presence reading.
>
> **Resolution: this is not a reason to demote to Route 3** (that would discard a real human
> intermediacy signal) **— it is a reason to CAP THE CLAIM.** The ratified yardstick certifies a
> **human-rated usage-similarity midpoint / high-disagreement stratum**, and any result may claim
> only that the model's confidence tracks *that*, explicitly labelled as **usage similarity**, never
> as sense co-presence. A sense-relatedness layer (e.g. WordNet) could later strengthen it, but
> adding it now would be designing the yardstick against an unrun result — it is **deferred as a
> noted enhancement, not required**. The rater-thinness caveat (151/200 EN pairs on 2 annotators;
> ρ≈0.69) makes the **≥3-rater floor** right but threatens power; if the floored bridging pool
> cannot support the 3-class contrast, the design **collapses to Route 3** (`internal-contrast-only`)
> and must be relabelled.
>
> ### Binding build-session conditions (load-bearing)
> - **(1) Class definition, frozen before any model output:** bridging = DWUG **within-period** pairs
>   at rounded DURel 2–3 AND/OR high inter-rater disagreement, each surviving the rater floor;
>   clear-same = high-agreement DURel-4; clear-different = high-agreement DURel-1. WiC T/F may
>   supplement the two clear poles **only**, never the bridging stratum.
> - **(2) Rater floor:** **≥3 annotators per pair** to enter any class (the half-integer 2-rater
>   levels are not reliable graded gold). Report the surviving per-class pool size **before** running;
>   if the bridging pool is too small to power the 3-class ordinal contrast, the probe runs as **Route
>   3 `internal-contrast-only`**, not a human-comparison claim.
> - **(3) Freeze rule:** the full stratum (item ids + class labels + rater counts) is frozen with a
>   manifest sha256 **before any model call**. No item may change class after any model output is
>   seen; re-selecting the bridging stratum against model confidence is the named anti-cheat
>   violation and voids the result.
> - **(4) Within-period enforcement:** DWUG diachronic structure means within-period filtering must
>   be enforced as in v1, or cross-period semantic-change pairs masquerade as bridging.
> - **(5) Label discipline:** every artifact states the bridging stratum is a **human-rated
>   usage-similarity midpoint / high-disagreement** stratum. "sense bridge" / "two senses co-present"
>   may describe the *concept being probed*, never the *certification* of a DWUG item.
> - **(6) Claim cap:** the result may make a **human-comparison claim only about usage-similarity
>   intermediacy** (the model is less confident where humans rated / split mid usage-similarity). It
>   may **NOT** claim humans certified two senses co-present. On the DWUG route it is **not**
>   `internal-contrast-only` (a real human signal anchors it), but its human-comparison force is
>   scoped to usage similarity. The Q3 context-ambiguity / distributional-shadow control belongs to
>   the sibling [`lexical-bridging-context-operationalization`](lexical-bridging-context-operationalization.md)
>   gate — handed off here, not re-decided.
>
> ### Residual risks (survive adoption)
> - Usage-similarity-mid ≠ sense-co-presence persists after the cap; the result page must **lead**
>   with it or readers will over-read a positive as "the model represents bridging senses."
> - **Power risk:** the ≥3-rater floor on an already-small within-period pool (v1: 200 pairs / 43
>   lemmas) may leave too few certified bridging items; the design may in practice collapse to Route
>   3. Not resolved by ratification — the builder checks it empirically post-freeze.
> - DWUG EN low end mixes homonymy (v1 flagged `lass`/`lassi`); the mid-band may inherit homonym
>   halfway-points, contaminating the polysemy-bridge reading.
> - Instrument sensitivity (the sibling gate's concern) bounds interpretability of any result built
>   on this stratum.
>
> ### Quote-integrity fix applied at integration
> The reviewer flagged that the route-2 paragraph below presented **"the gold is the expert sense
> split, not a rating panel"** inside quotation marks as if verbatim from
> [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md); the resource page's
> actual wording is "the per-item label is the expert sense split, not a graded judgment" and "Treat
> WiC agreement claims as 'agreement with the lexicographer sense split,' not 'agreement with a
> rating panel.'" The body text has been corrected to de-quote that compression. All other quotes
> (DURel scale; the "intermediate levels … graded distinctions" line; the 151/200 / ρ≈0.69
> rater-thinness figures; the WiC "binary by design" and pruning quotes) were verified **verbatim**
> against their source pages.
>
> ---
>
> *The provisional-default analysis below is preserved as the reviewer's evidence base (with the
> one quote-integrity correction noted above applied inline).*

# Decision: human anchor for the lexical bridging-context probe

## Why this exists

[`open-question/lexical-bridging-context-gradience`](../../findings/open-questions/lexical-bridging-context-gradience.md) re-opens the lexical axis on the one untested clause of [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) (prediction 4): does a model land in an **intermediate, lower-confidence** regime on a *bridging* use — a use engineered or attested so that two senses are genuinely co-present — rather than forcing a discrete same/different-sense pick? That open-question page names two gates it surfaces but does not resolve: an **operationalization** gate and a **human-anchor** gate. This page opens the second.

The human-anchor gate is the load-bearing one, and the open-question page states the difficulty plainly: "'The model is less confident on these items' is **uninterpretable** unless the bridging items are *certified* as genuinely bridging by some human-grounded signal independent of the model. Otherwise an apparent low-confidence band is unfalsifiable — any items the model happens to be unsure about could be relabelled 'bridging' after the fact" ([`open-question/lexical-bridging-context-gradience`](../../findings/open-questions/lexical-bridging-context-gradience.md)). The bridging stratum must be fixed by a signal **external to the model** before any confidence band is read, or the result decides itself. This is a value-laden choice a session must not auto-take ([`CLAUDE.md`](../../../CLAUDE.md) rule 5).

The conceptual object is [`concept/polysemy`](../../base/concepts/polysemy.md): on its account "the senses of a polysemous word … shade into one another, with bridging contexts where two senses are co-present and judgements are genuinely indeterminate," and "these bridging contexts are not anomalies to be disambiguated away; they are the evidence that sense distinctions are scalar, not binary." The anchor question is exactly: which in-repo human signal can certify that a given item sits in that scalar, co-present middle, rather than letting the model's own uncertainty draw the boundary.

This page is opened in parallel with the operationalization gate (the sibling decision `lexical-bridging-context-operationalization`, named by the open-question page, not yet created): operationalization fixes *what "intermediate, less-confident" is measured as*; this page fixes *what certifies an item as genuinely bridging in the first place*. The two are distinct and both must clear (cross-session) before a probe runs.

## The standing caveat that binds any option here

Before the routes: a label discipline binds every one of them, lifted verbatim from the conjecture's standing caveat as the open-question page records it — "the graded set measures usage similarity; the lexicographic gradience claim is about sense relatedness — keep the two labelled distinctly" ([`open-question/lexical-bridging-context-gradience`](../../findings/open-questions/lexical-bridging-context-gradience.md)). A DWUG mid-scale pair is a **usage-similarity** mid-point; calling it a **sense bridge** is the slide this decision must not make silently. Usage similarity and sense relatedness stay labelled distinctly in any artifact that flows from whichever route is ratified. The bridging-context probe is also subject to the distributional shadow — a model could be less confident on bridging items merely because their *contexts* are more ambiguous, not their *senses* — so the certified bridging stratum is a *necessary*, not sufficient, ingredient; the design's own context-ambiguity control (inherited from v1's clause-c discipline) is the operationalization gate's business, not this one's.

## The three candidate routes

The open-question page lifts three candidate human-grounded sources of a bridging stratum. Each is crystallized below as a decision option and sharpened by the feature of the in-repo resource page that actually bears (and the caveat that page forces — stated, not softened).

### Route 1 — DWUG mid-scale (DURel 2–3) / high-disagreement multi-rater pairs as the bridging class

- **What.** Define the bridging stratum from [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md): the **mid-scale** usage pairs (DURel 2–3) and/or pairs with **high annotator disagreement** — usages humans themselves split on — as the bridging class, with high-agreement **DURel-4** pairs as the clear-same anchor and high-agreement **DURel-1** pairs as the clear-different anchor.
- **Strength (the feature that bears).** DWUG is the **one in-repo resource with a graded, multi-rater, per-pair human signal** that can certify "humans themselves found this intermediate." Its page records the DURel scale verbatim ("4: Identical, 3: Closely Related, 2: Distantly Related, 1: Unrelated") and that annotators "make frequent use of the intermediate levels of the scale ('2','3') and thus assign graded distinctions of word meaning" ([`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md), quoting the primary paper). The mid-scale band and the high-disagreement band are precisely a *human-side* certification of intermediacy — independent of the model — which is exactly what the gate requires.
- **Weakness (forced, not softened).** Two real costs.
  - **Per-item rater thinness.** DWUG EN human–human agreement is **ρ ≈ 0.69**, and the v1 result flagged that "151/200 pairs rest on only 2 annotators (the half-integer levels are 2-rater disagreements)" and "the half-integer levels are not treated as reliable graded gold" (as the open-question page records, citing the v1 result and [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md)). So the disagreement signal is real but thin per item; a defensible bridging stratum needs a **≥3-rater** requirement to certify intermediacy reliably, and that requirement **shrinks the usable pool** — already small (v1 ran 200 within-period pairs over 43 lemmas; a certified-bridging subset is smaller still).
  - **A usage-similarity mid-point is not a certified within-sense bridge.** [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) "does not tag pairs as polysemy vs. homonymy." A DWUG mid-scale pair is therefore a **usage-similarity** mid-point, **not** a certified **within-sense** bridge — it does not by itself distinguish a polysemy bridge (two related senses co-present) from a usage that merely sits halfway on a proximity scale for other reasons. The label discipline above is doing live work here, not boilerplate.

### Route 2 — WiC near-boundary items

- **What.** Draw the bridging stratum from items near the decision boundary of [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md).
- **What WiC affords, and where it stops (the feature that bears).** WiC carries **binary** lexicographer-inventory same/different-sense labels over two contexts of the same target word; its page is explicit that it "is **binary by design**" and "cannot ground 'the model's signal is *monotonic* in human-rated relatedness.'" There is **no native per-item human graded or confidence axis** in WiC — its page states "the per-item label is the expert sense split, not a graded judgment" and directs that WiC agreement be read as "agreement with the lexicographer sense split," not "agreement with a rating panel" ([`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md)) — so WiC has **no native "near-boundary" annotation** to read a bridging stratum off. Worse for this exact use, its construction "removed all pairs whose senses were first degree connections … sister senses … those which belonged to the same supersense" (same page, verbatim from the WiC paper) — i.e. it **pruned the closest polyseme pairs**, exactly the near-bridge middle a bridging study most wants.
- **Net.** WiC can supply **clean clear-same (T) and clear-different (F) anchor items** — its large, balanced, POS-typed pool (7,466 items, 50/50) makes it an excellent source of the two *clear* poles. But it does **not** out-of-the-box certify a *bridging* stratum: any "near-boundary" WiC subset would have to be defined by an **added** signal (e.g. a WordNet sense-relatedness measure on the negatives WiC retained, or an external graded re-rating), not read off WiC's binary labels. As a standalone bridging anchor, WiC is insufficient; as a clear-pole anchor paired with another route's bridging certification, it is strong.

### Route 3 — Fresh engineered bridging constructions — NO human anchor

- **What.** Author deliberately ambiguous sentences (the "I read the paper" style bridge of [`concept/polysemy`](../../base/concepts/polysemy.md)) so that two senses are by-design co-present, with full control over the co-presence.
- **Posture.** This gives **full control** over co-presence but carries **no human grounding** for which items are genuinely bridging. A probe on this route is a **within-model contrast only** and, if promoted, would need the ratified **`anchor: internal-contrast-only`** terminal declaration ([`CLAUDE.md`](../../../CLAUDE.md) anchor discipline, state b) — a within-model claim, **never** a human-comparison one. It is a **strictly weaker, different claim** than routes 1–2 (it shows whether the model's behavior is internally consistent with intermediacy on items *the author* designed as bridging, not whether humans certify them as bridging), and it must be **labelled as such**. It must **never** be used to dodge the human-anchor obligation — the terminal `internal-contrast-only` state is for results a later session ratifies as making no human-comparison claim, not a way around a genuine anchor question (the discipline introduced 2026-05-31, now under the autonomous cross-session procedure; see [`CLAUDE.md`](../../../CLAUDE.md)).

## Provisional default (not a decision)

The provisional default — **laid out for a later reviewer, not chosen here** — is the **DWUG-derived bridging stratum (Route 1)**: mid-scale (DURel 2–3) and/or high-disagreement multi-rater pairs as the bridging class, with high-agreement DURel-4 and DURel-1 pairs as the clear-same / clear-different anchors. The reason is the one the gate turns on: DWUG is the **one in-repo resource that can certify human-side intermediacy** — a graded, multi-rater, per-pair human signal — so it is the only route that supplies an independent certification of "genuinely bridging" rather than letting the model draw its own boundary. WiC (Route 2) is best used *alongside* it for the two clear poles, since WiC cannot certify a bridging stratum on its own. The engineered-construction route (Route 3) is **more controllable but `internal-contrast-only`** — a strictly weaker, different claim — and is recorded as the explicit fallback if no defensible human-certified bridging stratum survives the rater-thinness and usage-vs-sense caveats above.

This choice is **not made here.** It is laid out for a later session's independent adversarial-review pass. **No human anchor is invented**; the default names only what the existing resource pages already say they afford — the DWUG mid-scale/disagreement signal, the WiC clear poles, and the explicit absence of human grounding for engineered items. The two binding caveats (per-item rater thinness shrinking the usable pool; a DWUG mid-scale pair being a usage-similarity mid-point, not a certified within-sense bridge) must be cleared by the ratifying session, and the usage-similarity-vs-sense-relatedness label discipline binds whatever route is ratified.

## Anti-cheat note

Ratifying this decision fixes the **yardstick** — *what certifies an item as genuinely bridging* — never the **result**. The probe must not be run, nor the bridging stratum re-selected against model outputs, in any session that ratifies; certifying the stratum *after* seeing which items the model is unsure about is exactly the unfalsifiability this gate exists to prevent (the open-question page's named failure mode: relabelling post hoc the items the model happens to be unsure about). The bridging stratum is **frozen before any model output is seen**. A NO-GO from a later review defers the probe rather than relaxing the certification. This page was opened 2026-06-21 (session 74); the earliest ratification is a later session's independent adversarial-review pass with written rationale, recorded `resolved-by: autonomous (adversarial review)`; the session boundary must hold.
