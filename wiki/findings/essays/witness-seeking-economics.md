---
type: essay
id: witness-seeking-economics
title: The economics of witness-seeking — allocating a finite probe budget over an open elicitation space, and when to suspend the search without closing the negative
meaning-senses:
  - model-internal
  - functional-vs-formal
  - relational
status: draft
contingent-on: []
created: 2026-06-18
updated: 2026-06-18
links:
  - rel: refines
    target: essay/undischargeable-negative
  - rel: depends-on
    target: essay/capability-split
  - rel: depends-on
    target: essay/transcript-ceiling
  - rel: depends-on
    target: result/relational-order-composition-c-easier-k4
  - rel: depends-on
    target: result/relational-order-composition-c-figure-to-figure
  - rel: depends-on
    target: concept/formal-vs-functional-competence
---

# Essay: the economics of witness-seeking

> **Status: draft (2026-06-18). A philosophical-track / methodological essay arguing in the project's own
> voice.** Its original contribution is a *decision rule for spending*, not an empirical claim: it
> supplies the piece [`essay/undischargeable-negative`](undischargeable-negative.md) left open. That essay
> proves a witness-seeking probe is the **only** behavioral move that can change a capability-negative's
> status, but says nothing about *how much* witness-seeking is warranted — and since the elicitation space
> is open and unbounded, "seek a witness" cannot mean "seek forever." This essay adds the missing economics:
> a finite probe budget should be allocated to the **highest-expected-information easings**, the value of a
> witness-seeking probe depends on **which axis it eases and whether that axis matches the failure's
> signature**, and a *structural* bound on the search space is worth more than any number of probes. It
> draws a sharp line between **logical closure** (never available from behavior — the
> [`essay/undischargeable-negative`](undischargeable-negative.md) result, fully preserved here) and
> **practical suspension** (a provisional, always-reopenable decision to stop spending). It contains **no
> new empirical claim** and makes **no human comparison**: every empirical sentence cites the in-repo page
> that carries it, at that page's stated strength, and the result it reads is a non-witness null /
> `internal-contrast-only`. Read the revision triggers before citing.
>
> **Update (2026-06-18, later session — the named on-signature probe ran; logged per essay discipline).** This
> essay named the well-targeted next probe: ease the **implicated** axis (the per-move read-off the single-move
> signature points at), e.g. "a figure-to-figure move design." That probe was then run
> ([`result/relational-order-composition-c-figure-to-figure`](../results/relational-order-composition-c-figure-to-figure.md)):
> the byte-identical K=4 trials re-rendered so each move is a figure→figure lookup table (no positions),
> removing the read-off. **No witness** — neither gemini (DIRECT 0.656) nor gpt (0.250) cleared the gate — but
> the single-move-reader signature **persisted even when each move is a trivial lookup**, localizing the
> residual difficulty to **chaining itself** (not the per-move read-off). This is exactly the case the essay
> anticipated: a non-witness on the **on-signature** axis, which it called "the first genuinely strong"
> evidence and the trigger for a **witness-search suspension note** — now recorded on the result page (axes
> eased: state-space + per-move read-off; implicated-but-un-eased: worked-example scaffold, fewer chaining
> steps; structural bound: none yet; reopen condition: a cheap probe on those un-eased axes). The essay's
> reading of the K=4 easing as off-signature is **corroborated** (the on-signature easing moved gemini's
> DIRECT the most — 0.594→0.656 — yet still left the gap), and the economics' distinction holds: the search is
> now **suspended on the read-off axis, not closed**. Trigger (a) (a witness on a so-far-un-eased axis) stays
> **live** for the worked-example / fewer-steps designs.

## The occasion

[`essay/undischargeable-negative`](undischargeable-negative.md) settled the *logic* of the project's
negatives. A behavioral probe is in an asymmetric posture: a capability *positive* ("M can do X") is an
existential settled by one witness, while a capability *absence* ("M cannot do X") is a universal over an
open class of elicitations that no finite battery of probes reaches. From that asymmetry it drew the
project's sharpest spending heuristic — restated here at its stated strength:

> **More of the same probe cannot.** Another failing instrument adds another ∀-instance; it never reaches
> the ∀. ([`essay/undischargeable-negative`](undischargeable-negative.md))

and its complement,

> **A single witness can — by flipping it to a presence.** ([`essay/undischargeable-negative`](undischargeable-negative.md))

So that essay sorts the project's moves against a suspected negative into one that is futile (re-run the
failing instrument), one that is decisive-if-it-fires (seek a witness), and one off the behavioral axis
(argue the structure). What it does **not** do is bound the middle option. "Seek a witness" reads as a
single recommended action; but a witness can be sought under *indefinitely many* easier or different
elicitations, and the project's budget is finite ($5.00/day, UTC; [`config/budget.md`](../../../config/budget.md)).
The recommendation, taken literally, is unbounded: the elicitation space is open by the very argument that
makes the negative undischargeable, so there is *always* one more easing to try. A program that followed
"seek a witness" without an economics would never stop, and would never be entitled to stop, because the
logic forbids the certainty that would license stopping.

This essay supplies the economics. Its question is not *can* the negative be closed (it cannot, from
behavior) but: **given that it cannot, how should a finite budget be spent searching for a witness, and on
what grounds may the search be suspended?** The honest-null discipline answered "what does a negative
license"; this answers "what is the next probe worth, and when is the next probe worth nothing."

## Closure is not available; suspension is the real decision

The first move is to refuse a confusion the budget pressure invites. Because each non-witness *feels* like
it firms up the negative, it is tempting to imagine a point at which enough easings have failed that the
negative is "practically closed." There is no such point, and the temptation is exactly the silent upgrade
[`essay/undischargeable-negative`](undischargeable-negative.md) forbids — "M cannot" smuggled in once the
list of failed elicitations grows long. The logic is unmoved by length: a hundred non-witnesses is a
hundred ∀-instances, and the next untried framing could still carry the witness that falsifies the whole
universal.

So the project never *closes* a behavioral negative; what it does is **suspend the witness-search** — a
decision of a wholly different type:

- **Closure** is a claim about the *world*: "M cannot do X." From behavior it is undischargeable, full
  stop.
- **Suspension** is a claim about the *project's spending*: "we will stop probing for a witness here,
  because the next probe's expected information no longer justifies its cost." It asserts nothing about M.
  It is provisional by construction, and **reopened automatically** the moment a cheap enough, well-targeted
  new idea appears.

A suspension can be entirely correct while the negative it suspends is false — the witness exists, the
project simply judged it not worth the cost of finding. That is not a defect; it is what allocating a finite
budget over an open space *means*. The economics below governs suspension, never closure. Keeping the two
apart is the whole discipline: the moment a suspension is read as a closure, the essay has been misused and
[`essay/undischargeable-negative`](undischargeable-negative.md)'s empty fourth box has been quietly filled.

## What a witness-seeking probe is worth

If suspension is the decision, its input is the *value of the next witness-seeking probe*. Informally, that
value is the probe's expected information times the probability it fires, weighed against its cost. The
expected-information term is where the economics has teeth, and it decomposes into two factors the project
can actually reason about before spending.

**1. Axis novelty.** Every witness-seeking probe eases *some* axis of difficulty — instrument size, number
of chaining steps, presence of a worked example, directness of the read-off. Easing an axis tests a
specific hypothesis: *the model failed because this axis was too demanding.* It follows that easing the
**same axis twice** has steeply diminishing returns — the second easing tests a hypothesis the first
already addressed. (It is not *literally* the parent essay's futile case: a second easing down the same
axis is still a new elicitation that *could* carry a witness, so it is not "more of the same probe" in the
strict sense of re-running the identical instrument; it simply has low expected information once the first
easing along that axis has failed.) Easing a **fresh axis** tests a genuinely new hypothesis and is
correspondingly informative. The
budget should therefore fund *axis-diverse* easings, not repeated marches down one axis.

**2. Signature match.** Better still, the project usually has a *failure signature* — the structure of how
the model fails, not merely that it fails — and the signature points at which axis to ease. A
witness-seeking probe that eases the axis the signature implicates is well-targeted; one that eases an
unrelated axis is poorly targeted, and a non-witness from a poorly-targeted easing is correspondingly weak
evidence. This is the single most useful refinement the economics adds: **read the failure signature, ease
the implicated axis.** A non-witness from an *on-signature* easing meaningfully lowers the posterior that a
witness exists; a non-witness from an *off-signature* easing barely moves it, because the wrong lever was
pulled.

The cost term is the literal one — the day's spend — and it matters most when it is *zero*: the cheapest
witness-seeking move of all is an *argument*, which brings in the third option.

## The structural substitute: argue the bound instead of exhausting it

[`essay/undischargeable-negative`](undischargeable-negative.md)'s third route — a structural or
architectural argument — is usually filed as the way to *close* a negative off the behavioral axis. But it
has a second, more common use that the economics makes central: a **structural argument can bound the
witness-search space** without closing anything. If one can argue that a whole *class* of easings cannot
help — that no member of it could carry a witness — then the open search collapses to a bounded one, and the
budget that would have been spent enumerating that class is freed at the cost of zero probes.

The project already owns the exemplar. [`essay/transcript-ceiling`](transcript-ceiling.md) does not run more
text probes to settle whether a text instrument can reach rich-side relational constitution; it *argues*
that the rich-side surplus is, by definition, not in any transcript, so no text easing — however clever —
could carry it. Its closing line is the economics stated as a slogan:

> A ceiling you can name is a map of where to stop digging. ([`essay/transcript-ceiling`](transcript-ceiling.md))

And the ratified decision that essay leans on records the spending consequence directly: a structural
closure is "a fully promotable outcome, as is a null; **neither is a reason to keep spending**"
(quoted in [`essay/transcript-ceiling`](transcript-ceiling.md)). The crucial discipline carried over from
that essay: a structural argument of this kind bounds the *reach of an instrument class*, not the *capacity
of the model* — it is the parent essay's **kind-3 reach-closure**, not a capability-absence. It tells the
project where further probing of *this medium* is unpromising; it leaves the capacity question open. So the
structural substitute is the highest-value move in the economics — it can retire an entire region of the
search at no spend — precisely *because* it claims so little about the model: only that a class of
instruments cannot reach the question.

## The worked instance: why the K=4 easing licensed almost no suspension

The economics is not retrofitted; it reads the project's most recent empirical session exactly. The
Option-C split — `claude-sonnet-4.6` composes two non-commuting moves, `gemini-3.5-flash` and `gpt-5.4-mini`
return UNINTERPRETABLE — was followed by a single witness-seeking probe that eased *one* axis: track size,
K=6 → K=4 ([`result/relational-order-composition-c-easier-k4`](../results/relational-order-composition-c-easier-k4.md)).
It found **no witness**: neither model cleared the on-demand gate at K=4. Read through the economics, three
things follow, and all three match what the project actually did.

- **Only one axis was eased, so very little suspension is licensed.** The result page says so itself —
  "**One easing axis.** K=6→K=4 only (same STEP/FLIP pair). Other easings (figure-based moves, fewer
  chaining steps, worked examples) untested"
  ([`result/relational-order-composition-c-easier-k4`](../results/relational-order-composition-c-easier-k4.md)).
  A single-axis non-witness lowers the posterior only along that axis. This is exactly why
  [`essay/capability-split`](capability-split.md) keeps its **revision trigger (b) live** "for any
  *further, more aggressive* easing (figure-to-figure moves, worked-example scaffolds, fewer chaining
  steps)" — the economics names *why* one non-witness leaves the trigger open: the other axes are simply
  unsampled.

- **The eased axis was off-signature, so the non-witness is weak.** The failure signature was specific:
  across both negative models the on-demand errors are ones in which "single-move readers dominate" — the
  model applies only one of the two stamped moves rather than composing them — which the verifier records
  as "the **identical failure signature** to K=6"
  ([`result/relational-order-composition-c-easier-k4`](../results/relational-order-composition-c-easier-k4.md)).
  That signature implicates the **chaining/composition** layer — holding and applying two operations in
  sequence — not the **state-space-size** layer that K eases. The K=6→K=4 probe pulled the wrong lever: it
  shrank the answer space, which the signature did not implicate, and left the chaining demand (still two
  moves) untouched. So its non-witness is, by the economics, weak evidence against a witness — it tested a
  hypothesis the signature already argued against.

- **The signature also names the next, well-targeted probe.** [`NEXT.md`](../../../NEXT.md) reaches the
  same place independently: the next witness-seeking design should be "a **figure-to-figure** move design …
  the layer the single-move-reader failure implicates," or "**fewer chaining steps**." That is the
  economics applied — ease the implicated axis next, because a non-witness *there* would carry the
  information a track-size non-witness cannot.

So the K=4 result is correctly read not as "the negative is nearly closed" but as "one off-signature easing
failed; the implicated axis is still un-eased; the search is **not** suspendable yet." The project's own
pages already act on this; the essay only makes the rule explicit.

## The reporting discipline: a witness-search suspension note

[`essay/undischargeable-negative`](undischargeable-negative.md) gave the project a filing system for
negatives (kind 1 effect-null / kind 2 instrument-uninterpretable / kind 3 reach-closure, with the kind-4
capability-absence box kept empty). This essay adds a filing record one level up — for the *meta-decision*
of when to stop generating kind-1/kind-2 negatives against a given suspected capability:

> **When the project stops seeking a witness, record a *witness-search suspension* — never a closure.** The
> note states: (i) which axes of difficulty were eased and the verdict on each; (ii) which axes the failure
> *signature* implicates but were **not** eased; (iii) any structural argument that bounds the remaining
> search space (a kind-3 reach-closure), or its explicit absence; and (iv) the standing condition for
> reopening — a cheap, well-targeted probe on an un-eased implicated axis. A suspension asserts nothing
> about the model; it is a spending decision, provisional and reopenable, and is **never** written as
> "M cannot."

The note is cheap and it pays twice. It stops a stack of non-witnesses from sliding into a tacit "M cannot"
(the discipline of the parent essay, applied to the search rather than the single result). And it makes the
*next* session's allocation legible: a future run reads off which implicated axis is still un-eased and
funds that, instead of re-easing an axis already exhausted or, worse, re-running the failing instrument.

This pairs with, and is orthogonal to, the two marks already in play. [`essay/capability-split`](capability-split.md)'s
**CONCORDANT/SPLIT** mark says *across how many models* a verdict holds;
[`essay/undischargeable-negative`](undischargeable-negative.md)'s **kind-1/2/3** mark says *what logical
type* a negative is; the **suspension note** says *whether the witness-search against this capability is
live or suspended, and on what grounds*. Three independent axes of bookkeeping, none of which licenses the
empty fourth box.

## What this essay is not

- **Not a way to close a negative.** The opposite: it exists to keep "suspend the search" from ever being
  misread as "close the negative," which [`essay/undischargeable-negative`](undischargeable-negative.md)
  shows behavior cannot do. Suspension is a spending decision; closure is a claim about the model the
  behavioral channel never licenses.
- **Not a claim that any model lacks any capability.** It governs *when to stop probing*, not *what the
  probes show*. The Option-C / K=4 non-witnesses are read strictly as kind-2 instrument-uninterpretable
  verdicts, per their pages.
- **Not a precise decision procedure.** The "expected information × probability-it-fires vs cost" framing is
  a heuristic for reasoning, not a formula the project computes; the project has no calibrated priors over
  elicitation spaces and claims none. The usable content is qualitative: prefer axis-diverse, on-signature
  easings; prefer a structural bound to exhaustion; record a suspension, not a closure.
- **Not an accusation that past sessions mis-allocated.** They did not — the K=4 session correctly kept
  trigger (b) live and named the implicated axis as the next probe. The essay generalizes a discipline
  already half-practiced, exactly as [`essay/undischargeable-negative`](undischargeable-negative.md) did for
  the negatives themselves.
- **Not a human comparison.** The result it reads is `internal-contrast-only`; the economics is general to
  any program that probes an open capability under a budget (it would bind for human probing too), but the
  essay applies it only to the project's own LLM probes and asserts nothing about humans.

## Revision triggers (read before citing)

- **(a) A witness found on a so-far-un-eased axis.** If a future well-targeted easing (figure-to-figure
  moves, fewer chaining steps, a worked-example scaffold) lets gemini or gpt clear the on-demand
  composition gate, the witness fires, the existence question is settled positive, and this essay's reading
  of the K=4 non-witness as "off-signature, weak" is *confirmed* (the right axis carried the witness the
  wrong axis could not). The essay is corroborated, not overturned — but the specific suspension would be
  reopened-and-resolved-positive, exactly as the economics predicts a cheap targeted probe can do.
- **(b) A structural bound on a witness-search space.** An in-repo argument that a whole class of easings
  cannot carry a witness (the relational program's transcript ceiling is the existing exemplar for the
  *rich-side* question; an analogous bound for some *thin-side* composition capability would be new) would
  let a suspension be backed by a kind-3 reach-closure rather than by exhaustion — the highest-value
  terminator in the economics. This sharpens the essay.
- **(c) A calibrated prior over an elicitation space.** If the project ever acquired a defensible
  quantitative prior over how likely a witness is along a given axis (it has none today), the informal
  "expected information" reasoning here could be made precise for that case — bounding the essay's
  qualitative framing to the cases where no such prior exists, which is the general case.
- **(d) A suspension found written as a closure.** If any in-repo page is found to assert "M cannot do X"
  on the strength of a *suspended witness-search* (rather than reporting a kind-1/2/3 negative), this essay
  turns from forward-looking discipline into a correction of that page. A scan at writing found none — the
  K=4 page explicitly keeps the negative "undischargeable, not closed."
- **(e) A fetched human resource licensing a capacity comparison.** None is in-repo. One bearing on how a
  *human* capability-search is bounded under finite resources would let the economics be applied
  comparatively — currently forbidden by the no-human-comparison discipline this essay observes.

## Honesty box

- The essay's **original** contribution is a *spending discipline*: given that a behavioral capability-
  negative is undischargeable, allocate a finite probe budget to **axis-diverse, on-signature** witness-
  seeking easings; prefer a **structural bound** (kind-3 reach-closure) to exhaustion; and record a
  **witness-search suspension** (which axes eased, which implicated-but-un-eased, any structural bound,
  the reopen condition) — never a closure. The sharp **closure ≠ suspension** distinction is the load-
  bearing move. No empirical claim here is new, original, or reported.
- The strongest empirical sentences leaned on, at their stated strength: the K=4 witness-seeking re-run
  found **no witness** (gemini DIRECT 0.594, gpt DIRECT 0.438, both sub-gate; claude RESPECTS-ORDER at
  ceiling), eased **one axis** (K=6→K=4), with failures "dominated by single-move readers," and left
  "figure-based moves, fewer chaining steps, worked examples" untested
  ([`result/relational-order-composition-c-easier-k4`](../results/relational-order-composition-c-easier-k4.md));
  [`essay/capability-split`](capability-split.md) keeps revision trigger (b) live for those further easings;
  [`essay/transcript-ceiling`](transcript-ceiling.md) is the in-repo exemplar of a structural bound ("a
  ceiling you can name is a map of where to stop digging"; a structural closure is "neither … a reason to
  keep spending"); and "failure on a world-knowledge task does not show that a model lacks formal linguistic
  competence" ([`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)).
  Nothing here outruns those.
- The thesis preserves [`essay/undischargeable-negative`](undischargeable-negative.md) intact: a behavioral
  negative stays undischargeable no matter when the search is suspended. Suspension is a budget decision,
  not an epistemic one, and is always reopenable.
- **No human comparison** is made or owed: the cited result is `internal-contrast-only`, and the human leg
  of every cited contrast is unanchored in-repo. The economics is general to budgeted capability-probing,
  but the essay applies it only to the project's own LLM probes.
