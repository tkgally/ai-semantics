---
type: essay
id: audit-brackets-instrument-competence
title: "One audit, two directions — bracketing an instrument's competence for a magnitude read, and why the same held-out-recovery device guards opposite artifacts in successive designs"
meaning-senses:
  - grounded.perceptual
  - referential.sense
status: draft
contingent-on: []
created: 2026-06-27
updated: 2026-06-28
links:
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: design/vwsd-grounding-headroom-nlbaseline
  - rel: depends-on
    target: note/vwsd-grounding-headroom-nlbaseline-audit-v1
  - rel: depends-on
    target: note/vwsd-grounding-headroom-nlbaseline-regrade-v1
  - rel: refines
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: essay/headroom-positive-vindicates-the-null
---

# Essay: one audit, two directions

> **Status: draft (2026-06-27, session 123). A philosophical-track / methodological essay arguing in
> the project's own voice.** Its original contribution is a *measurement-epistemics point about
> magnitude reads*: when a behavioral probe measures a **size** rather than a **direction**, the
> dominant uncertainty is often not the model but the **instrument's own competence**, and a single
> authored channel's competence level silently *sets* the magnitude — so the honest move is not to
> assert the channel is competent (by policy or intent) but to **bracket** its competence empirically
> between its two symmetric failure modes. Its second, concrete contribution is the observation that
> the **same** held-out-recovery audit device serves as a guard against *opposite* artifacts in
> successive designs — a *leak* audit in v2 (bar a channel that reveals **too much**) becomes an
> *adequacy* audit in the NL-baseline successor (bar a channel that reveals **too little**): one
> measurement device, pointed in two directions. It contains **no new empirical claim** and makes
> **no human comparison** beyond what the VWSD binary correct-image gold already licenses; every
> empirical sentence cites the in-repo page that carries it, at that page's stated strength, and the
> magnitude verdict it discusses (narrow vs wide residual) is **un-run and unmeasured** — the
> NL-baseline result does not exist. The essay is bounded to `grounded.perceptual` /
> `referential.sense` on binary VWSD gold; it ratifies nothing and pre-judges no result. Read the
> revision triggers before citing.
>
> **Revision log.** *2026-06-28 (session 129):* the NL-baseline result the original draft called
> "un-run and unmeasured … the NL-baseline result does not exist" now **exists** — built and audited at
> session 127 ([`note/vwsd-grounding-headroom-nlbaseline-audit-v1`](../notes/vwsd-grounding-headroom-nlbaseline-audit-v1.md))
> and re-graded under a session-128-ratified valid two-judge category-match
> scorer ([`note/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../notes/vwsd-grounding-headroom-nlbaseline-regrade-v1.md))
> → **0.438 strict referent-recovery, below the [0.60, 0.95] floor**, a clean degenerate-side NO-GO a
> fresh independent critic verified is a *valid* low rate, not a scorer artifact. This **exercised the
> essay's central device and it held**, firing **none** of the revision triggers below: **(a) did NOT
> fire** — the two-sided band was **not** empty/un-hittable; it was reachable and the channel scored
> *below* it, so the band's **degenerate-side guard fired exactly as designed** (the band working, not
> failing — do not misread a below-floor channel as an un-hittable band); **(c) did NOT fire** — the
> leak→adequacy duality **generalized**, the *same* held-out-recovery device was re-pointed into the
> s128 adequacy audit rather than replaced by a new construction; **(b)/(d) are not yet engaged** — no
> magnitude was read (the channel did not clear the floor), so no unaudited magnitude was accepted (b)
> and no narrow-under-band magnitude returned (d). Net: the essay is **strengthened, not revised in
> substance** — "bracket, don't assert" delivered an honest degenerate-side deferral on a real run. The
> *estimation-epistemics* sequel — why the s127 expert hand-read over-credited and the instrument
> corrected it across the floor — is developed in
> [`essay/instrument-corrects-the-hand-read`](instrument-corrects-the-hand-read.md).

## The occasion: a probe that measures a size, not a shape

The grounding axis has reached a clean structural fact and a stubbornly open magnitude. The structural
fact is the **gating shape**: perception moves an LLM's lexical sense behavior only in the residue the
text distribution leaves under-determined. [`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md)
supports it — with the word-ablated DISTRACT control clean (pooled .097 ≈ chance), the real image
"rescues the cells where the descriptor-text failed — pooled **39/86 = .453** … per-model
**.500 / .303 / .609** (all above chance) — while adding **no lift where the descriptor already
separates** (image actually drops .122 in the saturated stratum)". The neighboring
[`essay/headroom-positive-vindicates-the-null`](headroom-positive-vindicates-the-null.md) reads that
result for what it settles about the prior nulls (the modality is *gated*, not *inert*) and is careful
to add that the positive "licenses the **shape**, not the **size**."

This essay picks up precisely where that one stops. The open question is the **size**: how *narrow* is
the residual a competent text channel leaves — is most concrete lexical sense already in the
distributional shadow, or not? That is the conjecture's prediction 3 ("for concrete lexical sense the
headroom is narrow"), and v2 cannot touch it. The reason is v2's own first-class Limitation 1:

> "**The headroom magnitude is operationalization-inflated.** The TEXT arm uses Option-B descriptors
> that *deliberately* strip the referent name (the v2 fix for v1's caption leakage). So 'text-failed'
> means 'the visual-form-only descriptor + target word + trigger under-determined the sense,' not 'a
> competent natural-language description failed.' The image rescuing ~45% of such cells confirms the
> gating **shape** but says nothing about the **size** of the residual a fluent text channel would
> leave — that is why prediction 3 ('narrow headroom for concrete sense') is **not** supported or
> refuted here. A natural-language (non-abstracted) baseline would test magnitude; v2 tests shape"
> ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Limitation 1).

The clause that matters here is *"a competent natural-language description"*. v2's residual is .453
wide, but that width is manufactured by an **incompetent-by-design** channel — one that was barred from
naming the referent. The size you actually want is the residual a *competent* channel leaves. And the
moment you ask for that, you have to say what "competent" means — and there is the trap this essay is
about.

## The thesis: for a magnitude read, the dominant uncertainty is the instrument's competence

Here is the general claim. When a probe measures a **direction or shape** — *does X gate Y at all?* —
the instrument's competence can be sloppy and the verdict survives, because the verdict is a sign, not
a number. v2 is exactly this: its de-referented channel is a *bad* description channel, yet the gating
*shape* reads cleanly off it, because all the shape needs is that the residual exists and the image
acts only inside it. The instrument's incompetence inflated the residual without flipping the sign.

When the same probe is repointed to measure a **magnitude** — *how wide is the residual?* — that
tolerance evaporates. The number it returns is **a function of the channel's competence**, almost by
definition: a more competent describer leaves a narrower residual, a less competent one a wider one.
The decision page states this as the load-bearing structural fact, not a side caveat:

> "the residual width the probe measures depends entirely on **how competent the description channel is
> held to be**" ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).

So for the magnitude read, the dominant source of uncertainty is **not the model** — it is the
**instrument**. A magnitude reported off an unaudited authored channel is reporting the channel's
competence as if it were a property of language. This is the inversion worth naming: on a shape read
you can mostly forget the instrument and look at the model; on a magnitude read you must mostly forget
the model and audit the instrument, because the instrument is silently setting the number.

## Why asserting competence is not enough — and bracketing is

The tempting response is to assert competence: write a policy ("name the depicted referent plainly and
completely, as a competent describer would"), have a capable model author to it, and call the channel
competent. The decision page calls this option Q1-B and rejects it precisely as **assertion, not
measurement**: it "pins the channel only by **intent** — nothing empirically locates where the channel
landed between oracle and degenerate"
([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).
A policy that *reads* reasonable does not certify where the channel actually landed; the author is
itself a model, so the competence is displaced into the author's behavior, unmeasured.

The honest alternative is not to *assert* a competence level but to **bracket** it — to bound it
empirically between its two symmetric failure modes. And the two failure modes here are exactly
symmetric, because they are the two ways an instrument can lie about a magnitude:

- **Over-competent → artificially NARROW.** An *oracle* channel that restates the gold sense so
  completely the model can always match it collapses the residual. "Narrow headroom" then reads as
  confirmed — but as "an artifact of an over-competent channel, not as a fact about language"
  ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).
  This is v2's manufactured artifact run in reverse: v2 stripped referent names and *inflated* the
  residual; an oracle names them so completely it *collapses* it.
- **Under-competent → artificially WIDE.** A *degenerate-weak* channel — vague, partial, missing the
  referent the way v2's de-referenced descriptors did — inflates the residual, refuting "narrow
  headroom" "**by an under-competent channel, not by language**"
  ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).
  This is v2's own failure mode, re-imported.

The bracketing device is a **pre-registered two-sided band** on a held-out **recovery audit**: a fresh
model held out from the author is shown only the description (no image, no target word) and asked to
recover the depicted referent; the recovery rate must fall **inside** a band whose lower bound bars the
degenerate channel and whose upper bound bars the oracle. Recovery too high → oracle → reject (the
read would be artifactually narrow); recovery too low → degenerate → reject (artifactually wide). The
channel is certified competent only if it lands between, and competence is then fixed **empirically,
not by intent**. This is option Q1-C, ratified this session (ADOPT-DEFAULT, session 123, cross-session
adversarial review).

The philosophical payoff is the reporting posture it forces. Because the band is a *band* and not a
point, the magnitude is never reported as an absolute. The decision's honesty note, which binds every
option, makes this terminal:

> "the magnitude read is **always** 'how narrow the residual is under THIS competence standard,' **never**
> an absolute property of language … the probe measures a *conditional* magnitude, conditioned on the
> audited competence standard, not 'the true narrowness of concrete-sense headroom'"
> ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).

So even a clean Q1-C result reads "narrow *under this ratified band, on these 120 items*," never
"language leaves a narrow residual." Bracketing does not deliver the absolute magnitude; nothing can,
because no authored channel is "ordinary language" in the abstract — it is whatever a model wrote under
a policy. What bracketing delivers is the *honest object*: a magnitude with its instrument-competence
explicitly bounded rather than silently assumed. That is the most a magnitude read of an authored
channel can be, and it is worth a great deal more than a number that pretends the channel was perfect.

## One audit, two directions — the device that brackets from both sides

The second, more concrete observation is the one this essay most wants to foreground, because it is
easy to miss and it is genuinely new: **the bracketing is done by a single measurement device, pointed
in two opposite directions in two successive designs.**

v2 already ran a held-out recovery audit — its **Option-C leak audit**. There, a held-out gpt was
shown the de-referenced descriptor and asked to recover the target referent; the worry it guarded was
that the descriptor *leaked too much* (named the referent it was supposed to strip), which would let
text "solve" items by surface word-matching rather than sense. It behaved discriminatively rather than
saturating: "high-leak rate **.130**; Spearman(`leak_i`, `sep_i`) = **.160** over the 120 in common — a
**weak** positive"
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), §5). Thirteen percent
of gold descriptors still let gpt recover the exact target word; the covariate was carried, never
regressed out. The point for this essay is that the *same construction* — show a held-out model the
text channel alone, measure how much of the referent it recovers — already exists in-repo and already
gave a graded, non-saturated, non-degenerate signal on this exact dataset and panel. It is a working
measurement, not a rubber stamp; the ratifying review leaned on exactly this to certify that the
NL-baseline's analogous audit "is **not vacuous**"
([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).

Now watch the same device turn around. In the NL-baseline successor the channel is the *opposite* kind
of channel — a fluent, referent-naming description, where v2's was referent-barred — and so the worry
is the *opposite* worry. The risk is no longer that the channel reveals too much by accident; it is
that the channel is *engineered* to reveal too much (the oracle) or fails to reveal enough (the
degenerate). The very same held-out-recovery construction is re-run, but now read as an **adequacy
audit**: the recovery rate must clear a lower bound (the channel is *adequate*, not degenerate) and
stay under an upper bound (the channel is not an *oracle*). v2's audit barred a channel that revealed
**too much**; the NL-baseline's audit, the same device, brackets a channel from **both** sides at once.

The symmetry is the project's own, and the design states it as the spine of the whole follow-up — the
v1 → v2 → NL-baseline channel progression:

| run | text channel | what it did to the headroom |
|---|---|---|
| **v1** | referent-**NAMING** captions | **saturated** the baseline |
| **v2** | referent-**BARRED** visual-form descriptors | **manufactured** headroom |
| **NL-baseline** | competent natural-language description, names **ALLOWED** | the powered, audited **middle** |

(table content drawn from [`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md),
"the v1 → v2 → NL-baseline symmetry"). v1 named the referent and saturated (artifactually narrow); v2
barred it and manufactured headroom (artifactually wide). The NL-baseline is the fluent middle — and
the device that keeps it in the middle is the held-out recovery audit, the *exact same instrument* that
served v2 as a leak guard, now serving as the two-sided adequacy guard. One measurement device, pointed
in two directions, brackets competence from both ends of the same axis. That a single, already-validated
construction does double duty against opposite artifacts is, I think, the cleanest small lesson the
magnitude follow-up teaches: you do not need a new instrument to bracket competence from both sides;
you need the same recovery audit read against a two-sided band instead of a one-sided threshold.

## Why this is not the neighboring essay (and not a validity-theory restatement)

The bound here is on **instrument competence for a magnitude**, not on the interpretation of a null or
a positive.

- [`essay/headroom-positive-vindicates-the-null`](headroom-positive-vindicates-the-null.md) is about how
  a positive on the gating *shape* retroactively fixes what the prior nulls were evidence for (gated, not
  inert), and it explicitly stops at "shape, not size." This essay starts where it stops: it takes the
  *size* question as given-open and asks what kind of instrument could even measure it honestly. The
  former is about **what a result means**; this is about **what a magnitude instrument must do to be
  trustworthy at all**. They share the shape/size distinction as a hinge but argue about different sides
  of it — that essay defends the shape claim; this one designs the audit for the size claim.
- It is **not** [`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md). That essay is about a
  single *number* being a run-to-run draw from a sampling distribution — the same instrument re-run
  jitters. This essay's uncertainty is not sampling jitter; it is **systematic**: a fixed competence
  level of the channel *biases* the magnitude in a known direction (over-competent → narrow,
  under-competent → wide), and no amount of re-running the same channel removes that bias. The remedy is
  not repeated runs but a held-out audit against a band.
- It is **not** [`essay/undischargeable-negative`](undischargeable-negative.md): that essay is about the
  asymmetry of *can't*-claims (a probe witnesses presence, never closes out absence). The two failure
  modes here are symmetric by construction — over- and under-competence are mirror artifacts, and the
  band bars both equally — which is the opposite of an asymmetric posture.
- It is also **not** [`essay/construct-validity-without-a-criterion`](construct-validity-without-a-criterion.md):
  that essay imports Cronbach–Meehl/Messick validity theory to argue the project's gates are construct
  validation with the criterion leg amputated. This essay is narrower and more concrete — it is about a
  single, specific device (a held-out-recovery band) that brackets an instrument's competence for a
  size read, and the observation that one such device guards opposite artifacts across two designs. It
  borrows no validity-theory machinery and makes no claim about the project's gates in general.

## What this essay is not

- **Not a finding, and not a result.** The NL-baseline result `result/vwsd-grounding-headroom-nlbaseline`
  **does not exist and is not cleared**; the design is "cleared to freeze" but unfrozen, and a later
  session must still author the descriptions, pin the band edges / audit model / recovery-scoring rule,
  freeze before reading the reused IMAGE arm, obtain a fresh pre-run-critic GO, and clear the budget cap
  ([`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)).
  This essay argues for a *method posture*; it reports no magnitude and pre-judges neither a narrow nor a
  wide residual. Both are first-class pre-registered outcomes.
- **Not a claim that the band is hittable.** A pre-run-critic NO-GO "may legitimately conclude the
  competence standard is **un-hittable on VWSD without leaking gold**"
  ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)).
  That the bracketing *strategy* is sound does not entail the band is non-empty on this dataset; if it is
  empty, the magnitude gate defers, and that is an honest outcome the strategy permits, not a failure it
  hides.
- **Not an absolute-magnitude claim.** Even a clean Q1-C read is "narrow/wide *under this ratified
  competence standard*," never a property of language — the conditional is load-bearing and carried
  verbatim-in-force into the design's scope.
- **Not a human comparison beyond the VWSD anchor.** The only human leg is the SemEval-2023 VWSD binary
  correct-image gold; the essay asserts nothing about people beyond binary selection, and the resource's
  caveats (binary gold, limited annotator independence, image redistribution unconfirmed, anchored only
  to the gold test split) travel in force. Bounded to `grounded.perceptual` / `referential.sense`: a
  model picking the gold image is behavior *sensitive to* the word→sense→image mapping in the residual,
  not a perceptual symbol system and not reference (`referential.externalist` untouched).
- **Not a general law of instruments.** The "one audit, two directions" duality is reported as a
  concrete in-repo observation about the VWSD leak→adequacy pair, not as a claim that every magnitude
  probe admits such a dual-use device. Whether the duality generalizes is a revision trigger, not an
  assumption.

## Revision triggers (read before citing)

- **(a) The NL-baseline run finds the two-sided band EMPTY / un-hittable on VWSD** (no competence
  standard between oracle and degenerate is reachable without leaking gold). This is **evidence the
  bracketing strategy fails for perceptual-grounding magnitude on this task** — the central method
  posture would have to concede that for VWSD the magnitude read cannot be made honest by this device,
  and the essay's "bracket, don't assert" prescription would narrow to "bracket where a non-empty band
  exists; where it does not, the magnitude is simply not measurable here." The essay narrows, not
  retracts: the diagnosis (competence sets the magnitude) stands even when the cure is unavailable.
- **(b) A magnitude read on this axis is accepted in-repo WITHOUT an instrument-competence audit** (a
  future result reports a residual width off an unaudited authored channel and is treated as a finding).
  That would be evidence the project does not in fact hold the posture this essay argues for; the essay
  would be **contested**, and either the result or this essay would have to give.
- **(c) The leak→adequacy duality does NOT generalize** — the NL-baseline's adequacy audit turns out to
  require a *different* construction than v2's leak audit (e.g. the held-out-recovery device cannot be
  re-pointed and a new instrument is built). This retracts the second contribution (the "one audit, two
  directions" observation) while leaving the first (bracket-don't-assert) intact; the two contributions
  fail independently and should be cited separately.
- **(d) The audited magnitude returns NARROW under a band a fresh critic certifies non-arbitrary.** This
  **strengthens** the essay: the bracketing device delivered a usable conditional magnitude, vindicating
  "bracket, don't assert" as a working method, not just a counsel of caution. (It does **not** vindicate
  any *absolute* narrowness — the conditional stays.)
- **(e) The two-sided band is shown to be defeatable by shared training distributions** — a held-out
  audit model passes an oracle-ish channel because it shares the author's distribution, so "held out
  from the author" is not true independence. The decision page already concedes and bounds this risk
  (flags (i)/(ii)); if a later session shows the circularity is *fatal* rather than bounded, the
  bracketing device is weaker than this essay credits, and the prescription would have to add an
  independence requirement the held-out-recovery construction cannot meet — narrowing the device's
  warrant.

## Honesty box

- The essay's **original** contributions are two and they fail independently: (1) the
  *method-epistemics point* that a magnitude read's dominant uncertainty is the **instrument's
  competence**, which a single authored channel silently sets, so the honest response is to **bracket**
  competence empirically between its two symmetric failure modes (a two-sided band) rather than assert
  it by policy; and (2) the concrete *one-audit-two-directions* observation that the **same**
  held-out-recovery device serves as a leak guard in v2 and a two-sided adequacy guard in the
  NL-baseline. Neither is an empirical claim about a model; both are claims about how to build and read a
  magnitude instrument. **No empirical claim here is new, original, or reported.**
- The in-repo facts leaned on, at their stated strength and verified against the source files: v2's
  rescue "pooled **39/86 = .453** … per-model **.500 / .303 / .609**," the saturated stratum dropping
  ".122," the DISTRACT control clean at pooled ".097," and the magnitude
  "operationalization-inflated … says nothing about the **size**"
  ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md)); v2's Option-C leak
  audit "high-leak rate **.130**; Spearman(`leak_i`, `sep_i`) = **.160**" (same page, §5); the two-sided
  band, the oracle-vs-degenerate symmetry, and the conditional honesty note from
  [`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)
  (resolved this session, ADOPT-DEFAULT Q1-C); the v1→v2→NL-baseline channel symmetry from
  [`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md).
  Nothing here outruns those, and the result page's honest discounts (gemini's elevated floor, gpt's
  overall degradation and sign-only support) are preserved by not leaning the magnitude argument on any
  single model.
- **No human comparison** beyond the VWSD binary correct-image gold is made or owed; the read is held to
  `grounded.perceptual` / `referential.sense`, and the magnitude verdict (narrow vs wide) is un-run,
  unmeasured, and conditional on a band a later session must still pin. This essay ratifies nothing.
