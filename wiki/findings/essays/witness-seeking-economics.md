---
type: essay
id: witness-seeking-economics
title: The economics of witness-seeking — allocating a finite probe budget over an open elicitation space, and when to suspend the search without closing the negative
meaning-senses:
  - model-internal
  - functional-vs-formal
  - relational
status: revised
contingent-on: []
created: 2026-06-18
updated: 2026-07-05
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
    target: result/scivetti-let-alone-forced-decomposition-v1
  - rel: depends-on
    target: result/scivetti-let-alone-powered-rerun-v1
  - rel: depends-on
    target: essay/output-channel-confound
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
> new empirical claim** and makes **no human comparison of its own**: every empirical sentence cites the
> in-repo page that carries it, at that page's stated strength. The composition results it reads are
> non-witness nulls / `internal-contrast-only`; the let-alone result the session-61 deepening adds is
> *human-anchored* ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)),
> but the leg this essay leans on is the **within-model** format/uptake contrast — the essay introduces no
> human comparison the cited page does not already carry. Read the revision triggers before citing.
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
>
> **Deepening (2026-06-18, thirty-fifth session — the on-signature non-witness re-read; logged per essay
> discipline).** A later session re-examined this essay against the figure-to-figure result it had just
> recorded and found the economics **under-credited** what an *on-signature* non-witness is worth. The
> probe-value model below (expected information × probability-it-fires) counts a non-witness only as
> "lowering the posterior." But the figure-to-figure run *also* paid a **diagnostic dividend**: by removing
> one implicated sub-axis (the per-move read-off) while holding the failure-signature observation fixed, its
> non-witness *relocated* the implicated axis from a two-way disjunction (read-off vs. chaining) to a single
> named axis (chaining) — telling the next session where the difficulty is *not*. The new section **"The
> diagnostic dividend"** adds this as a value-component of an on-signature, **single-variable** easing (it
> pays out even when it returns no witness) and gives a second rationale for the project's single-variable
> design discipline. The closure ≠ suspension line is untouched: relocating the implicated axis hands the
> next probe a sharper target — the opposite of closing the negative.
>
> **Update (2026-06-18, later session — trigger (a) and trigger (f) both tested; logged per essay
> discipline).** This essay named the next well-targeted easing — a **worked-example scaffold** on the
> implicated **chaining** axis — and it was then run
> ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md)):
> one worked example demonstrating the chaining mechanic, added to the byte-identical fig trials (a clean
> **single-variable** easing; pre-run critic GO, post-run verifier REPRODUCED). **Trigger (a) did NOT fire —
> no witness** (gemini DIRECT 0.625, gpt 0.156; claude RESPECTS-ORDER at ceiling). The diagnostic-dividend
> mechanism paid out exactly as the section below predicts, in its **persist** branch: the single-move
> signature *persisted* (gpt's *intensified* to 84.4% single-move with the order stated), so the easing
> **subtracted a sub-axis** — the single-move reading is **not** a demonstration/comprehension gap (showing
> the procedure did not help), so the residual difficulty is chaining **execution**. This is the second
> on-signature non-witness to pay a constructive dividend, corroborating the section's claim. **Trigger (f)
> did NOT fire:** the signature *persisted/intensified*, it did not *change kind* (the models did not stop
> being single-move readers and fail some new way) — so this is the persist case the section already treats,
> not the contrasting change case (f) anticipates. The closure ≠ suspension line holds: the suspension note
> on the result page was **updated**, not closed — only **fewer chaining steps** remains un-eased, and it is
> near its ≥2-move floor.
>
> **Update (2026-06-19, next session — the witness-search REOPENED-AND-RESOLVED-POSITIVE; logged per essay
> discipline).** The single most important vindication of this essay's central distinction (logical closure
> vs. practical suspension): the composition negative was **suspended on budget, never closed** across four
> instruments — and a fifth, cheap, well-targeted probe found a **witness**. The implicated axis was not
> chaining *capacity* but the **execution format**: every prior run forbade a working surface, and permitting
> step-by-step output (reasoning-effort knob held constant) flipped **both** gemini (DIRECT 0.625→1.000) and
> gpt (0.156→0.969) to RESPECTS-ORDER at/near ceiling
> ([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)).
> Had the project *closed* the negative (declared "these models can't compose") after four non-witnesses, it
> would have been **wrong**. Because it only *suspended*, a single targeted probe could and did reopen and
> resolve it positive — the exact payoff this essay's "suspend, never close" discipline is for. The
> "ease the **implicated** axis" rule also delivered: the truly-implicated axis was the elicitation surface,
> and easing it found the witness in **one** probe (~$0.74).
>
> **Refined-forward (2026-06-19, next session): [`essay/output-channel-confound`](output-channel-confound.md).**
> A companion essay reads the same witness as an **allocation correction** to this one. The decisive axis —
> the **output channel** (forced single token vs. a working surface) — was eased *fifth*, after four content
> easings, yet it is **cheap** and **recurs across the whole instrument library**, so a narrow channel is a
> standing rival explanation for *any* forced-format serial-computation negative. That essay adds the output
> channel to this essay's implicated-axis menu and ranks it **among the first** controls to vary, not the
> last. It preserves the closure ≠ suspension line (the channel-widening **reopened-and-resolved-positive**)
> and the "ease the implicated axis" rule (it names the under-weighted axis), and bounds the confound to
> capabilities that are **serial and externalizable** (single-token tasks are untouched).
>
> **Update (2026-06-20 — a suspension where the *probe*, not the model, hit the wall; logged per this
> essay's reporting discipline).** The cross-family composition probe (a heterogeneous spatial+attribute
> operation pair, the different-*kind* step the depth suspension pointed to) was **built and suspended
> before any spend**
> ([`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md)
> point (i); run [README](../../../experiments/runs/2026-06-20-relational-order-composition-cross-family/README.md)).
> It sharpens the essay's **cost term** in a way the depth discussion only half-anticipated. The cost of
> a witness-seeking probe is not only the API spend; it includes the **shortcut-proofing cost** — the
> design work to certify that *no* non-composing reader can clear the bar — and this run shows that cost
> grows not just with composition *depth* (the competing-reader family the depth note tracked) but with
> **operation heterogeneity**: a single-bit answer over two near-orthogonal operations proved unusually
> leak-prone (the independent pre-run gate found **five** distinct shortcut classes — object-anchoring,
> a geometry×cell confound, and three round-magnitude leaks — each fixed, with a residual content-
> conditional overfitting gap remaining). With the model-side prior already low (the working-surface
> composition capacity is panel-concordant on every axis tested, no strain anywhere), the rising
> build-cost tipped the allocation to **suspend** — a spending decision, **never** a closure, asserting
> nothing about the models, and reopenable by a cleaner (e.g. non-binary-answer) design. Two disciplines
> are preserved exactly: the gate **was not weakened to get a GO** (the project declined to spend rather
> than relax the 0.50 bar — the relational-line GO-discipline), and the suspension is filed as a
> **witness-search suspension**, not a kind-4 "the models can't."
>
> **Deepening (2026-06-20, session 61 — the partial witness; logged per essay discipline).** The value
> model below sorts a witness-seeking probe's outcome into *fires* (a witness, flips to presence) or *does
> not fire* (a non-witness — lowers the posterior, possibly paying a diagnostic dividend). A later
> empirical session produced a **third** outcome the binary had no slot for: a probe that eased the
> implicated axis and returned a **directional but underpowered lift** — neither a clean fire nor a clean
> miss ([`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md):
> forcing uptake lifted gpt's let-alone +0.21 yet left it below baseline and the within-item sign test
> underpowered, p = 0.090 — "**partially fired / candidate**"). The new section **"The partial witness"**
> adds this outcome to the value model and resolves the allocation question it raises: the correct
> continuation is a **powered re-run of the same axis** (more items), which the "axis novelty / same axis
> twice" caution would wrongly discourage and which must be carefully distinguished from the parent essay's
> futile "more of the same probe cannot." The discriminator is **whether the first run produced a
> directional effect**: powering an underpowered *signal* resolves a live easing's statistics, not the
> existence question a clean non-witness already answered. The closure ≠ suspension line is untouched — a
> partial witness *keeps the search live* and names the funded next probe. (The principle was first stated,
> in the single-case, on [`essay/output-channel-confound`](output-channel-confound.md)'s trigger (b) — "a
> powered re-run … not 'more of the same'"; this deepening promotes it into the economics' general value
> model, its proper home.)
>
> **Resolution (2026-06-20, session 62 — the partial witness's first *resolved* instance; logged per essay
> discipline).** The powered re-run trigger (g) prescribed has now landed
> ([`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)): the
> same forced-decomposition axis, instrument byte-identical, the let-alone set enlarged to its human-anchored
> **ceiling** (33 = 24 test + the 9 *disjoint* train items). The slot resolves **both** ways trigger (g)
> anticipated, at once. (i) *As a capability witness, the easing is a clean **miss**:* gpt's accuracy stayed
> **below** the ≈0.90 baseline (combined 0.636, CI hi 0.778 < 0.90), reproducing the session-60 *accuracy*
> exactly (via offsetting label flips — gpt churns too, see (ii)) and extending to disjoint items — no presence is reached, the below-baseline residual is confirmed
> (and is, read from the sibling essay, [`essay/output-channel-confound`](output-channel-confound.md) trigger
> (b)'s cleanest *firing*: a channel-controlled residual). (ii) *And the self-extinguishing bound's "design,
> not count, limits power" sub-clause is **realized**:* the run exposed ~12% temp-0 label stochasticity (a
> baseline-matcher swung to 0.708 on the *identical* items), a per-run swing comparable to the residual gap —
> so what now limits precision is **measurement noise, not item count**, and the funded next probe redirects
> to a **repeated-run / multi-sample** design on a *new* (measurement) axis, **not** a third item-count
> re-run. The exemption is therefore **spent** exactly as designed — it bought one adequately-aimed
> resolution, then extinguished, the further re-run it forbids being "more items" (the ceiling is reached)
> while permitting the orthogonal repeated-run axis. Closure ≠ suspension is untouched: the residual stays
> undischargeable ("confirmed below-baseline in two runs" is not "demonstrated bound"), the search stays live
> on the measurement axis. **No new empirical claim; the human-anchored leg is read at stated strength
> (descriptive + contamination-caveated); no new human comparison is made.**

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

## The diagnostic dividend: what an on-signature non-witness buys even when it doesn't fire

The K=4 worked instance above is the *floor* of a non-witness's value — an off-signature easing whose
failure barely moves the posterior. The **figure-to-figure** easing that followed
([`result/relational-order-composition-c-figure-to-figure`](../results/relational-order-composition-c-figure-to-figure.md))
reaches a *ceiling* a non-witness can hit, and it forces a refinement the two-factor value model above does
not yet contain. That probe re-rendered the byte-identical K=4 trials (same `stimuli.json` sha) so each move
became an explicit figure→figure lookup table with no positions shown — easing the **on-signature** axis (the
per-move read-off the single-move signature implicates), changing the *single* variable of rendering. It
found **no witness**: neither gemini (DIRECT 0.656) nor gpt (0.250) cleared the on-demand gate. By the
two-factor model so far, that is an on-signature non-witness — it "meaningfully lowers the posterior," more
than the off-signature K=4 did. True, but incomplete.

What the two-factor model misses is that this non-witness *also* told the project **where the difficulty is
not**. The mechanism is general. A failure *signature* is rarely a single hypothesis; it is usually a small
disjunction of them. The single-move-reader signature — the model applies only one of the two stamped moves —
was, before this probe, compatible with (at least) two readings: **(1)** the per-move read-off is too costly,
so the model economizes by doing one move; or **(2)** the chaining itself — holding two operations and
applying *both* in sequence — is the bottleneck, independent of any per-move cost. The K=6 and K=4
instruments could not separate these: both kept the positional read-off, so both left (1) and (2) bundled.
The figure-to-figure rendering removed the read-off while holding everything else fixed (byte-identical
trials), and **the signature persisted** — "the single-move-reader signature persists even when each move is
a trivial lookup," with gpt still applying "only one of the two moves 65.6% of the time" on the order-stated
arm ([`result/relational-order-composition-c-figure-to-figure`](../results/relational-order-composition-c-figure-to-figure.md)).
A signature that *survives* the removal of sub-axis (1) **disfavors (1) and promotes (2)** (on this one
`internal-contrast-only` run, at the strength its page states): "the difficulty is **not** the per-move
computation the figure-maps removed; it is **holding and applying two operations in sequence** (the chaining
itself)." The probe relocated the implicated axis from a two-way disjunction toward a single named axis — a
real information gain, collected on a **non-witness**.

So an on-signature, single-variable easing has **two** payouts, not one:

- **If it fires,** the negative flips — the witness the whole search is for.
- **If it does not fire but the signature *persists* through the removal of one implicated sub-axis,** the
  probe has *subtracted that sub-axis from the implicated set*. It does not so much lower a scalar posterior
  as **redraw the implicated-axis map** that drives the next allocation, telling the next session which
  un-eased axis to fund (here: the **chaining** axis — a worked-example scaffold, or fewer chaining steps —
  rather than anything touching the read-off). (Had the signature instead *changed* — the model ceasing to be
  a single-move reader and failing some new way — that too would be diagnostic, redrawing the map in a
  different direction.)

This is the refinement the "axis novelty / signature match" section above was missing: an on-signature easing
ranks above an off-signature one not only because its non-witness *lowers the posterior more* (the reason
given there) but because its non-witness is **constructive** — it sharpens the map of where the difficulty
lives and so aims the *next* probe better than the prior signature could. The contrast is exact in the
project's own record: the off-signature K=4 non-witness left the implicated-axis map unchanged (its failures
were ones in which "single-move readers dominate," the "identical failure signature to K=6"); the on-signature
figure-to-figure non-witness *redrew* it (read-off out, chaining in).

Two bounds keep this honest. **First, the dividend is collected only by a genuinely single-variable easing** —
one that isolates a sub-axis while holding the others fixed, as the byte-identical-trial figure-to-figure
design did (only the rendering changed). A confounded "easier" probe that moves several axes at once forfeits
the dividend: when the signature persists you cannot tell which removed axis was the inert one. So the
diagnostic dividend is a *second* argument for the single-variable, on-signature easings the project already
prefers — the first was cleaner inference on the witness question; the second is that only such a design lets
the *non-witness* pay out. **Second, the dividend does not touch the closure ≠ suspension line.** Relocating
the implicated axis closes nothing — it names the next un-eased axis to probe, which *extends* the search with
a sharper target rather than ending it. An on-signature non-witness that pays a diagnostic dividend is, if
anything, the strongest case for keeping the witness-search *open* (now better-aimed), not for suspending it;
the suspension recorded for this line still rests on the **budget**, not on the implicated-axis map having
gone blank.

## The partial witness: a directional-but-underpowered easing, and the "power-up" move

The value model so far — even with the diagnostic-dividend refinement — sorts a witness-seeking probe's
outcome into two bins: it **fires** (a witness, the negative flips to a presence) or it **does not** (a
non-witness, which lowers the posterior and may pay a diagnostic dividend by relocating the implicated axis).
A later session produced an outcome that fits neither bin cleanly, and seeing why forces a third slot.

The occasion is the let-alone output-channel search. A forced single-token format had left all three panel
models near chance on the phrasal-scalar **let-alone** NLI items; a working surface lifted two of them to the
human baseline, but the weakest model, `gpt-5.4-mini`, had largely **declined** the offered surface (a
*channel-not-taken-up*, [`essay/output-channel-confound`](output-channel-confound.md)). The well-targeted
next probe forced uptake — a mandatory construction-neutral decomposition before the answer — and it worked
as a manipulation: gpt's median let-alone working jumped from 8 to 120 tokens, 24/24 items genuinely worked.
With the channel now actually exercised, the easing returned **a directional lift that does not reach a
witness**: gpt's accuracy rose **0.375 → 0.583** (+0.21, 7 gains / 2 losses), but the within-item sign test
is **underpowered** (p = 0.090 on 9 discordant pairs, short of the pre-registered 0.05 bar → verdict
UNCHANGED) and the rate **stays below the ≈0.90 baseline** the other two models reach. The result page reads
the outcome as "a **partial output-channel effect** … part is channel-bounded … and part survives a
genuinely-exercised wide channel," registered "**partially fired / candidate**: the *direction* is the
contrast case … the *power* is not yet there to call it clean"
([`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md)).

This is a **partial witness**, and it sits *between* the two outcomes the value model names. It is not a
fire: no presence is settled — the rate stayed below baseline and the within-item test failed to clear its
bar, so the existence question ("can this model do let-alone, channel given and used") is still open. But it
is emphatically **not a clean non-witness** either: the easing *moved the rate substantially in the witness
direction*. Filing it as a non-witness — "posterior down a notch" — would mis-describe a strong directional
signal as evidence *against* a witness; filing it as a fire would over-read an underpowered lift as a settled
presence. Either misfiling loses the actual information, which is precisely *that the implicated axis is alive
but the run could not resolve it*.

The allocation consequence is where the partial witness earns its own treatment, because the move it calls
for looks, at first, like the one move both this essay and its parent forbid. The natural next probe is a
**powered re-run of the *same* axis** — the same forced-decomposition easing, on **more** let-alone items —
to resolve whether the +0.21 is real or sampling noise. Yet [`essay/undischargeable-negative`](undischargeable-negative.md)
warns that "**more of the same probe cannot**," and the **axis-novelty** rule above warns that "easing the
**same axis twice** has steeply diminishing returns." Taken flatly, both would discourage exactly the
high-value probe. The deepening's claim is that they do **not** apply here, and the value model must say why.

The discriminator is **whether the first run produced a directional effect.** "More of the same probe cannot"
governs a re-run of an instrument that returned a **clean non-effect** — another ∀-instance, after which the
negative is exactly as un-established as before *because nothing moved*; the re-run tests a hypothesis the
first run already answered ("this axis, eased, did not carry a witness"). A re-run after a *partial* witness
is a different act on a different question. The first run did **not** answer its hypothesis — it returned a
*shift it lacked the power to certify*. The second run, on more items, does not re-ask "does easing this axis
help?" (the first run already showed it does, directionally); it asks "**is the observed shift real?**" — a
**power** question the first run, at n = 24 with 9 discordant pairs, structurally could not settle. Powering a
live directional signal is statistical resolution of an *implicated, productive* axis, not a diminishing-
returns march down an *exhausted* one. The axis-novelty rule therefore needs a scope clause: *its
diminishing-returns verdict on "the same axis twice" holds when the first easing returned a clean
non-witness; it is suspended when the first easing returned a partial witness, where the same axis is the
single highest-value place left to spend.*

So the value model gains a third outcome and its continuation rule:

- **Fires** → the negative flips to a presence; the search on this capability is settled positive.
- **Partial witness** (a directional lift, underpowered, no presence reached) → the implicated axis is
  *alive but unresolved*; fund a **powered re-run of the same axis** (more items, more discordant pairs),
  explicitly **exempt** from the "same axis / more of the same" caution, until the signal is either confirmed
  (it becomes a fire) or dissolved (the lift was noise → it becomes a clean miss).
- **Misses** (a clean non-witness) → the posterior drops, possibly with a diagnostic dividend; fund a
  *fresh, on-signature* axis next, **not** a re-run of this one (here the caution binds with full force).

Two bounds keep the new slot from being abused. **First, the power-up exemption is narrow and self-
extinguishing.** It licenses re-running the *same* axis *only* because the first run produced an underpowered
directional effect; it does not license re-running an axis that returned a clean non-effect, and it does not
license endless re-runs — once the re-run carries adequate power, its verdict is terminal (a fire or a clean
miss), and a further re-run *would* be "more of the same." The exemption buys exactly one adequately-powered
resolution, not a standing license. **Second, the partial witness does not touch the closure ≠ suspension
line.** It neither closes the negative — gpt's below-baseline residual stays undischargeable; "candidate" is
not "demonstrated bound" — nor suspends the search; it does the opposite of both, *keeping the search live and
naming the funded next probe.* If anything, a partial witness is the strongest case against suspension: an
axis that visibly moves the rate is the last axis a budget should abandon.

The partial witness also carries a second reading that doubles the value of resolving it, and the two essays
meet here. Because gpt now externalizes the computation **and still falls short**, the same result is the
closest thing in the record to [`essay/output-channel-confound`](output-channel-confound.md)'s **trigger (b)**
— a serial-computation negative that *survives* a genuinely-widened channel (a *channel-controlled* residual,
not a channel-bounded one). A powered re-run therefore serves double duty: it either confirms a real
below-baseline residual (firing that essay's long-sought cuts-both-ways contrast case) or reveals the lift as
noise and the residual as a full channel artifact after all. The economics ranks such a dual-purpose,
on-signature, productive-axis re-run **high** — it is the rare re-run that the "more of the same" caution does
not condemn precisely because the first run left a *signal*, not a *null*, behind.

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
- **Not a human comparison of the essay's own.** The composition results it reads are
  `internal-contrast-only`; the let-alone result the partial-witness section reads is *human-anchored*
  (its accuracy-vs-≈0.90-baseline leg is anchored for comp-correlative, descriptive for let-alone), but the
  leg this essay leans on is the **within-model** format/uptake contrast, and it reads the page's
  baseline references only at that page's stated strength — introducing no new human comparison. The
  economics is general to any program that probes an open capability under a budget (it would bind for human
  probing too), but the essay applies it only to the project's own LLM probes and asserts nothing about humans.

## Revision triggers (read before citing)

- **(a) A witness found on a so-far-un-eased axis.** *Tested twice 2026-06-18 and did NOT fire (no
  witness):* the **figure-to-figure** read-off easing and then the **worked-example scaffold** on the
  chaining axis ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md))
  both left gemini and gpt below the on-demand gate (the scaffold: gemini 0.625, gpt 0.156), while claude
  stayed at ceiling. So no witness has yet appeared — the trigger stays **live** for the one remaining
  un-eased axis (**fewer chaining steps**, near its ≥2-move floor) or a different/easier operation pair.
  **→ FIRED 2026-06-19** (see the REOPENED-AND-RESOLVED-POSITIVE update above): the witness appeared
  on a **fifth axis this enumeration did not name** — the execution-format / working-surface easing
  ([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)),
  which flipped gemini **and** gpt to RESPECTS-ORDER on byte-identical trials. The existence
  question settled positive; the annotation is placed at the trigger itself per the s183 convention.
  If such a future well-targeted easing lets gemini or gpt clear the gate, the witness fires, the existence
  question is settled positive, and this essay's reading of the K=4 non-witness as "off-signature, weak" is
  *confirmed* (the right axis carried the witness the wrong axes could not). The essay is corroborated, not
  overturned — but the specific suspension would be reopened-and-resolved-positive, exactly as the economics
  predicts a cheap targeted probe can do.
- **(b) A structural bound on a witness-search space.** An in-repo argument that a whole class of easings
  cannot carry a witness (the relational program's transcript ceiling is the existing exemplar for the
  *rich-side* question; an analogous bound for some *thin-side* composition capability would be new) would
  let a suspension be backed by a kind-3 reach-closure rather than by exhaustion — the highest-value
  terminator in the economics. This sharpens the essay. *Attempted 2026-06-19 for the thin-side
  composition capability and the bound does **not** exist:*
  [`essay/floor-is-not-a-ceiling`](floor-is-not-a-ceiling.md) examined the only candidate — the **≥2-move
  floor** (a composition needs ≥2 moves) plus the behavioral localization to "chaining execution" — and
  showed it is **not** a kind-3 reach-closure but a **task-parameter floor**: it caps one easing axis
  (step count) while leaving the elicitation space open along others (a different operation pair, an
  execution-format scaffold, many-shot), and any "irreducible core" step that would close it smuggles in
  the undischargeable behavioral universal (the forbidden kind-4 box). So the composition witness-search
  stays **suspended on budget, never structurally closed**. The trigger fired in the *negative* — a
  **reasoned null** rather than the new bound it anticipated — which **sharpens** this essay anyway: that
  refining essay adds the **gate a candidate must pass to count as a structural bound** (a class-level /
  medium-level exclusion, not a task-parameter floor — "not every floor is a ceiling"). The trigger stays
  **live** for a *genuine* medium-level exclusion of some composition witness (its trigger (c)).
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
- **(f) An on-signature easing whose failure signature *changes* rather than persists.** The diagnostic-
  dividend section reasons from a *persisting* signature (read-off removed, single-move reading survives →
  difficulty is chaining). If a future single-variable on-signature easing instead *shifts* the signature —
  the model stops being a single-move reader and fails some new way — the dividend is still collected but
  redraws the implicated-axis map differently; the section would gain a contrasting worked case, sharpening
  (not overturning) the general claim that an on-signature non-witness is constructive. *Tested 2026-06-18
  and did NOT fire:* the worked-example-scaffold easing
  ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md))
  left the single-move signature *persisting and intensifying* (gpt 65.6% → 84.4% single-move), not
  changing kind — the **persist** case the section already treats, which subtracted the demonstration-gap
  sub-axis. The trigger stays **live** for any future on-signature easing whose signature shifts to a new
  failure mode.
- **(g) A powered re-run resolving a partial witness. — RESOLVED 2026-06-20 (session 62).** The
  partial-witness section named one open case — gpt's underpowered +0.21 let-alone lift under forced uptake
  ([`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md)).
  Its prescribed continuation is a **powered re-run of the same axis** (more let-alone items, or the disjoint
  train-split items the result page names). When that re-run lands, the partial-witness slot gains its first
  *resolved* instance — either the lift is confirmed (the easing **fires**: a witness, the negative flips to
  a presence) or it dissolves into noise (a **clean miss**: the residual was a full channel artifact, and the
  axis is now exhausted, the exemption spent). Either way the three-outcome model is corroborated; a re-run
  that came back *partial again* (still directional, still underpowered) would instead **sharpen** the
  exemption's self-extinguishing bound — flagging that the design, not just the item count, limits power
  (e.g. too few discordant pairs are reachable on this construction), which would redirect the spend to a
  *different* axis rather than a third re-run.
  **What landed** ([`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md);
  see the dated Resolution block at the head of this essay): **both predicted shapes at once.** As a
  *capability* witness the easing is a **clean miss** — gpt stayed below baseline (0.636, CI hi 0.778 < 0.90),
  reproducing session 60 exactly, so no presence is reached and the below-baseline residual is confirmed (the
  sibling essay's trigger (b) reads the *same* outcome as its cleanest *firing*). **And** the re-run did the
  thing the "partial again" branch foresaw without itself coming back partial: it surfaced ~12% temp-0 **label
  stochasticity** as the binding limit, so **the design (measurement), not the item count, limits power** —
  redirecting the next spend to a *repeated-run / multi-sample* axis, not a third item re-run (the item count
  is at its human-anchored ceiling). The three-outcome model is corroborated and the self-extinguishing bound
  is realized: the exemption bought **one** adequately-aimed resolution and is now **spent**.

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
- The thirty-fifth-session **diagnostic-dividend** deepening is a refinement of this essay's own value
  model, grounded in [`result/relational-order-composition-c-figure-to-figure`](../results/relational-order-composition-c-figure-to-figure.md):
  an on-signature, single-variable non-witness is **constructive** — its persisting failure signature
  relocated the implicated axis from "read-off vs. chaining" to "chaining," redrawing the map that aims the
  next probe. It adds **no** empirical claim (it reads the result page at its stated strength) and does not
  touch the closure ≠ suspension line.
- The session-61 **partial-witness** deepening is likewise a refinement of this essay's own value model, not
  a new empirical claim; it reads [`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md)
  at its stated strength. The numbers leaned on: forcing uptake took gpt's median let-alone working from
  **8 → 120 tokens** (24/24 worked) and its accuracy **0.375 → 0.583** (+0.21, 7 gains / 2 losses), with the
  within-item sign test **underpowered** (p = 0.090, 9 discordant pairs → verdict UNCHANGED) and the rate
  **below the ≈0.90 baseline** — "a **partial output-channel effect** … part is channel-bounded … and part
  survives a genuinely-exercised wide channel," "**partially fired / candidate** … the *power* is not yet
  there to call it clean," with "**a powered re-run (more let-alone items …)** … the next witness axis." The
  deepening's **original** contribution is the third outcome slot (partial witness) and the **power-up scope
  clause** — that re-running the *same* axis after a *directional* easing resolves power, not existence, and
  so is exempt from "more of the same probe cannot" / "the same axis twice," with the exemption bounded as
  narrow and self-extinguishing. The single-case statement of the principle pre-existed on
  [`essay/output-channel-confound`](output-channel-confound.md)'s trigger (b); promoting it into the value
  model is the new work. The closure ≠ suspension line is untouched: a partial witness keeps the search live.
- The session-62 **resolution** of the partial-witness slot (trigger (g)) is likewise no new empirical claim;
  it reads [`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)
  at its stated strength. The numbers leaned on: the powered re-run (let-alone enlarged 24 → 33 with 9
  *disjoint* train items, the human-anchored ceiling) left gpt's accuracy **0.636** (CI hi **0.778 < 0.90**),
  reproducing session 60's 0.583 exactly on the shared 24, with uptake induced (33/33 worked) and the ceiling
  control PRESERVED; and it exposed **~12% temp-0 label stochasticity** (a baseline-matcher read 0.708 on the
  *identical* 24 via 3 adverse flips). The deepening's **original** contribution is to record that the slot's
  *first resolved instance* lands as **a confirmed below-baseline residual (a capability-witness clean miss)
  + a realized "design-not-count-limits-power" redirect** to a repeated-run axis — corroborating the
  three-outcome model and showing the exemption *spent* as designed. The closure ≠ suspension line is
  untouched (the residual stays undischargeable; the search stays live on the measurement axis).
- **No new human comparison** is made or owed. The composition results read here are `internal-contrast-only`
  (their human leg unanchored in-repo); the let-alone result the partial-witness deepening adds **is**
  human-anchored ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md);
  its accuracy-vs-≈0.90 leg anchored for comp-correlative, descriptive for let-alone), so this essay's
  "below the ≈0.90 baseline" references *restate that page's own anchored/descriptive comparison at its
  stated strength* — the essay's contribution is the spending-rule reading off the **within-model** format/
  uptake contrast and adds no human comparison of its own. The economics is general to budgeted
  capability-probing, but the essay applies it only to the project's own LLM probes.
