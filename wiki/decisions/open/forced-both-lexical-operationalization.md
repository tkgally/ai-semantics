---
id: forced-both-lexical-operationalization
title: "How do you certify a genuinely-unresolvable (forced-both) lexical item — a pun/zeugma/co-activated double-entendre — and score it on an instrument where 'it means both' is NOT a dodge, so the test can separate layer-specialness (A) from always-resolvability (B) for the surviving lexical commit?"
status: open
opened: 2026-06-23
opened-by: autonomous (session 89, surfacing the discriminating-test operationalization named by essay/layer-specialness-vs-always-resolvability)
meaning-senses:
  - distributional
  - referential
  - relational
contingent-artifacts: []
links:
  - rel: operationalizes
    target: essay/layer-specialness-vs-always-resolvability
  - rel: depends-on
    target: result/within-lexical-scalar-vs-disjunctive-v1
  - rel: depends-on
    target: result/cross-level-shared-instrument-v1
  - rel: depends-on
    target: concept/polysemy
---

> **Status: OPEN — opened 2026-06-23 (session 89). Not yet eligible for ratification.** Surfaced
> this session; under the cross-session rule ([`PROTOCOL.md`](../../../PROTOCOL.md) §2,
> [`CLAUDE.md`](../../../CLAUDE.md) rule 5) it is ratifiable only by a *later* session via an
> independent adversarial-review pass with written rationale. **It is NOT runnable until ratified**
> — no probe may be built-to-run, no spend opened, no scoring rule re-tuned, in any session that
> ratifies. The deflationary reading **(B) always-resolvability** holds the burden, exactly as
> [`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md)
> places it ("the burden sits on (A) … to beat (B)"). The **expected first outcome is the essay's
> revision trigger (c)** — *a genuinely-unresolvable lexical item cannot be cleanly certified*, so
> the fork **stays at R1**; this page is written so that "cannot cleanly certify" is an honest
> verdict, not a hidden failure. **This page fixes the YARDSTICK only, never the result**
> ([`CLAUDE.md`](../../../CLAUDE.md) rule 6): it asserts no empirical finding and makes no human
> comparison.

# Decision: how to build and score a genuinely-unresolvable (forced-both) lexical item

## The decision in one paragraph

The within-lexical scalar-vs-disjunctive probe found that the lexical commit-without-hedging
**survives a genuine lexical disjunction — 3/3 models**
([`result/within-lexical-scalar-vs-disjunctive-v1`](../../findings/results/within-lexical-scalar-vs-disjunctive-v1.md)),
and its load-bearing caveat 1 disclosed that the design cannot say *what* the commit is a fact
about. [`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md)
splits that residual into a fork — **(A) layer-specialness** vs **(B) always-resolvability** — and
names the one stimulus that would separate them: a **genuinely-unresolvable lexical item** (a
forced-both pun / zeugma / co-activated double-entendre). This page decides *how that stimulus is
built and scored* — it is the **R2 rung** for the layer-vs-resolvability fork (the essay states the
"discriminating probe is the **R2 rung** for this fork"). It decides nothing about the result:
whether the models commit (supporting A) or decline (supporting B) is for a later, separately-gated
run to discover. What is decided here is only the yardstick — what counts as a certified forced-both
item, and what instrument makes "it means both" structurally unavailable as a dodge — so that
whatever the run finds is interpretable rather than an artifact of the scoring rule.

## Background — the fork this operationalizes

The two rival readings of the surviving lexical commit, from
[`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md):

- **(A) Layer-specialness.** "The commit-without-hedging is a fact about the **word-sense layer
  itself**. The models commit on word senses *whatever the kind or structure of the ambiguity*".
- **(B) Always-resolvability.** "The commit is **not** special to the layer. Word-sense is simply
  the one level whose ambiguities — even disjunctive homonyms — **remain
  resolvable-by-committing-to-a-reading** … The models commit because the *item affords a
  resolution*, not because it is *lexical*."

The SURVIVAL design cannot tell them apart because a balanced homonym is *both* lexical *and*
resolvable — "a balanced homonym is both lexical *and* resolvable, so both readings predict commit"
(same essay, Honesty box). The discriminating stimulus pulls those apart: a forced-both item is
lexical but *not* resolvable-by-a-reading, because "committing to one [loses] the communicative
point." On it the fork's predictions diverge, **asymmetrically**:

- "**(A) layer-specialness predicts the models STILL commit.**"
- "**(B) always-resolvability predicts the models DECLINE.**"

That asymmetric prediction — *commit under (A), decline under (B)*, on a stimulus where the SURVIVAL
homonyms predicted commit under both — is the whole payoff. The essay leaves the operationalization
explicitly undecided; this page is that operationalization.

The forced-both item is the lexical analogue of the relational same-round **dual binding**, which
[`result/cross-level-shared-instrument-v1`](../../findings/results/cross-level-shared-instrument-v1.md)
glosses as "a *genuine underdetermination* (a same-round dual binding with no tie-break —
both/neither)" and on which "all three models take 'UNCLEAR' **every time**" (3/3 models). Reading
(B) predicts the forced-both lexical item draws *that* abstention; reading (A) predicts it draws the
near-zero `UNCLEAR` the balanced homonym drew.

## The first-class NULL / symmetric reporting, declared up front

Per [`CLAUDE.md`](../../../CLAUDE.md) rule 6, the negative is **first-class** and declared **before**
any data. Three outcomes must be reported with no after-the-fact relabelling:

- **Commit** — the forced-both item draws near-zero abstention / a confident single reading. This
  would support **(A) layer-specialness** — the surprising, burden-discharging result, since (B) is
  the parsimonious default. It must clear an **even higher** anti-cheat bar than decline.
- **Decline** — the forced-both item draws the abstention the relational dual-binding draws. This
  would confirm **(B) always-resolvability**, the deflationary default, and must be reported as
  cleanly as a commit.
- **Cannot cleanly certify** — the item cannot be certified forced-both rather than a leaning
  homonym, or "it means both" cannot be excluded as a dodge, or N is too thin. Then **no verdict is
  licensed and the fork stays at R1** (the essay's trigger (c), the honest expected first outcome).

## Q1 — Certifying forced-both vs a leaning homonym

**The question.** What independent (not model-based) procedure certifies that an item is genuinely
**forced-both** — both senses *jointly* required, "pick one" is *wrong* not merely under-determined —
and is **not** a *leaning* balanced homonym (one sense in fact dominant)? This matters because, per
the SURVIVAL result's caveat 2, a lean **suppresses** `UNCLEAR` rather than raising it: "a lean in
**either** direction *suppresses* `UNCLEAR` (a sense-A lean → confident SAME; a sense-B lean →
confident DIFFERENT), so leaners **erode the collapse signal**"
([`result/within-lexical-scalar-vs-disjunctive-v1`](../../findings/results/within-lexical-scalar-vs-disjunctive-v1.md)).
An under-certified "pun" that is really a leaning homonym would therefore present as commit and bias
spuriously toward **(A)** — the failure mode the higher anti-cheat bar exists to catch. The essay
flags exactly this: "an under-certified 'pun' that is really a leaning homonym would bias toward
commit and spuriously support (A)."

**Options.**

- **(Q1-i) Syntactic forcing via zeugma / co-predication diagnostics.** Build each item so one word
  is *yoked to two complements that each demand a different sense*, the construction the essay
  sketches: "A zeugma yokes one word to two complements that demand its two senses together". A word
  read with a single sense would make one complement anomalous, so the construction *grammatically*
  requires both readings at once. This is an item-internal structural criterion, certifiable before
  any model call. ([`concept/polysemy`](../../base/concepts/polysemy.md) records the conjunction /
  anaphora diagnostics for *logical* polysemy via its 2026-06-23 update; the analogous syntactic
  diagnostic here is the co-predication / zeugma frame for *homonymy*, where the two senses are
  unrelated.)
- **(Q1-ii) Independent balance check — human-or-corpus, neither reading dominant.** Add, on top of
  (Q1-i), a check that neither sense is the dominant/default reading of the item in isolation
  (otherwise a forced-both frame can still *lean*). Candidate evidence: an independent annotator
  judgement of "both required, neither dominant," or a corpus/frequency check that the two senses
  are comparably available. This is the harder half and the place a real human anchor could enter
  (see Q4).
- **(Q1-iii) Both (i)+(ii), sha256-frozen before any output.** The structural frame certifies
  *forced-both-ness*; the balance check certifies *no-lean*; both are recorded and frozen before the
  first probe call.

**Provisional default = (Q1-iii):** the zeugma / co-predication syntactic frame **plus** an
independent balance check, both frozen before any run. **Honest caveat (lead with it):** this is the
hard part of the whole decision. A co-predication frame strongly forces both senses but does **not**
by itself guarantee no lean (one complement may still dominate the reading), so the balance check is
not optional; and certifying "neither reading dominant" without leaning on the model's own behavior
is genuinely difficult — the essay's expected verdict (trigger (c), "cannot be certified forced-both
rather than a leaning homonym") lives here. If the balance check cannot be made independent of model
output, the honest move is to *declare the item uncertified*, not to relax the criterion.

## Q2 — The instrument on which "it means both" is NOT a dodge

**The question.** The essay shows the deepest problem: a model can "resolve" a pun by *reporting*
that it means both, which is neither commit nor decline on the SAME/DIFFERENT/UNCLEAR instrument.
Verbatim from
[`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md):

> "The deepest problem is that a pun may still be *resolved* by **reporting that it means both**. If
> the instrument asks "what does the word mean here?" and the model answers "both senses at once —
> that is the joke," the model has neither picked one reading nor abstained; it has *named the
> co-activation*. … If "it means both" is scored as **commit** … then (A) is hard to falsify …
> If it is scored as **decline** … then (B) is hard to falsify … The verdict is then an artifact of
> the scoring rule, not a fact about the models — exactly the operationalization-tuning failure the
> protocol warns against".

Scoring "both" as commit makes (A) unfalsifiable; scoring it as decline makes (B) unfalsifiable.
That is an operationalization-tuning trap, and the inherited SAME/DIFFERENT/UNCLEAR instrument from
[`result/within-lexical-scalar-vs-disjunctive-v1`](../../findings/results/within-lexical-scalar-vs-disjunctive-v1.md)
does not escape it on its own.

**Options.**

- **(Q2-i) A forced-single-application downstream task.** Ask a question that *requires* one sense
  to proceed — an inference, a substitution, or a continuation that **only one reading licenses** —
  so "it means both" is structurally unavailable. The essay names exactly this: the instrument "would
  have to ask a question on which 'it means both' is **not** an available dodge — for instance, a
  *forced single application*: a downstream task that *requires* one sense to proceed … so that a
  model genuinely treating the item as both-at-once must either *refuse the task* (the decline (B)
  predicts) or *force a single reading and lose the other's content* (the over-commit (A) predicts)."
- **(Q2-ii) Keep the offered graded "both/unclear" option, but pre-register the mapping.** Retain
  the SAME/DIFFERENT/UNCLEAR (or an explicit "both") response and **pre-register, before any run, how
  'both' maps to commit vs decline.** Honest but fragile: any pre-registered mapping of "both" is the
  very lever the essay warns makes one reading unfalsifiable, so this option only relocates the trap
  to the freeze rather than dissolving it.
- **(Q2-iii) Other instruments** (e.g. asking for *both* an inference and its negation under each
  reading) — left open for the adversarial reviewer to weigh.

**Provisional default = (Q2-i), the forced-single-application instrument**, because it is the one
design where "it means both" is structurally unavailable as a dodge: the task cannot be *completed*
by naming co-activation. A model that treats the item as genuinely both-at-once must either refuse
(read as decline → B) or force one reading and discard the other's content (read as over-commit →
A). The graded-mapping option (Q2-ii) is held in reserve as the weaker fallback, because it
re-imports the unfalsifiability the essay diagnoses.

## Q3 — The scoring rule / reading rule (frozen before any probe call)

**The question.** How do model responses map to the (A)-commit vs (B)-decline verdict, and how is
that mapping protected from being tuned after results are seen?

**Reading rule (provisional, to be sha256-frozen before the first probe call — inheriting the freeze
discipline of the sibling gates,
[`decisions/resolved/cross-level-shared-instrument-operationalization`](../resolved/cross-level-shared-instrument-operationalization.md)
condition C2 and
[`decisions/resolved/matched-ambiguity-kind-cross-level`](../resolved/matched-ambiguity-kind-cross-level.md)
Q3):**

1. **Response classes → verdict.** On the forced-single-application instrument, map each response to
   one of: *refuse-task* (declines to apply a single reading) → **decline (B)**; *force-one-reading*
   (applies a single sense and thereby loses the other's content) → **commit (A)**; *answer-both*
   (attempts to satisfy the task under both readings, where the task admits it) → reported as its own
   class, **not** silently folded into either pole; *answer-cleanly* (a single defensible
   application with no sign the item was treated as both) → **commit (A)**. The exact class
   definitions, item ids, and the commit-vs-decline threshold are frozen and sha256'd **before** any
   model output. No instrument-shopping and no per-item re-certification after any output is seen.
2. **Clear-class precondition (inherited C3).** Before any forced-both reading is interpreted, the
   instrument must read cleanly on **unambiguous control items** (single-sense uses on the same
   frame): clear-class decline below a frozen cap and confidence above a frozen floor, per-model, or
   that model's leg is a **NO-GO** — exactly the C3 guard inherited from
   [`decisions/resolved/cross-level-shared-instrument-operationalization`](../resolved/cross-level-shared-instrument-operationalization.md)
   (clear-class precondition → per-level NO-GO). A precondition failure defers the model's verdict;
   it never relaxes a band.
3. **Symmetric reporting, higher bar on commit.** Commit and decline are reported symmetrically. But
   **commit carries the HIGHER anti-cheat bar**: it is the burden-discharging surprise for (A) (the
   essay places the burden on A to beat B), and a spurious commit is the named failure mode (a
   leaning homonym mis-certified as forced-both), so any commit verdict must additionally survive the
   clean-subset check (commit holds on items certified forced-both *without* a disclosed lean) and
   the higher bar that the SURVIVAL result already applied to a result that "would partly revive a
   defeated unified conjecture" — here, that would credit the layer.
4. **Inherit the decline-is-load-bearing rule (C1) and the self-report guard (C4).** As in the
   shared-instrument gate, the categorical task-outcome (refuse / force-one / answer-cleanly), not a
   self-reported confidence number, is load-bearing for the verdict (C1); a confidence shift
   unaccompanied by a task-outcome shift is a self-report note, not evidence for either pole (C4).

## Q4 — Anchor posture

**The question.** Does the forced-both lexical class make a human-comparison claim, and if so on
what resource?

**Provisional default = `internal-contrast-only`** (a within-model contrast; **no human number
enters**) — exactly as the sibling gate held its disjunctive arm
([`decisions/resolved/matched-ambiguity-kind-cross-level`](../resolved/matched-ambiguity-kind-cross-level.md),
Q2-b) — **UNLESS** a resource that certifies sense **co-activation** (both senses *jointly required*,
not merely both *licensed*) is separately, cross-session ratified as its own anchor decision, exactly
as the matched-ambiguity gate held its Q2-a open. **No anchor is invented here.** A forced-both item
asserts a *stronger* human-grounding demand than even the balanced-homonym class: not "two senses
co-present and equally licensed" but "two senses jointly *required*." Nothing in-repo silently
certifies that. [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) records
that DWUG "does not tag pairs as polysemy vs. homonymy" (the resolved sibling gates cite this as the
reason no DWUG-derived resource certifies sense distinctness, let alone co-activation), so no in-repo
DWUG-derived resource can stand in for a co-activation anchor. Under the **weakest-common-strength**
rule, any contrast that includes an `internal-contrast-only` arm is stated at the
`internal-contrast-only` floor for that arm. The essay confirms this posture is owed, not dodged:
"The discriminating probe it motivates *would* carry a per-leg anchor obligation for any new
genuinely-unresolvable lexical class — surfaced here, not dodged."

## Anti-cheat note

The provisional defaults make a spurious **positive** (a manufactured layer-specialness win, i.e. a
spurious (A)) **harder, not easier**:

- **The forced-single-application instrument (Q2-i) closes the unfalsifiability trap.** It removes
  the "it means both" response that, scored either way, could be tuned until the desired pole
  appears. With "both" structurally unavailable as a task completion, neither (A) nor (B) can be made
  unfalsifiable by a scoring choice — the operationalization-tuning failure the essay and
  [`PROTOCOL.md`](../../../PROTOCOL.md) §B warn against is foreclosed at the instrument level rather
  than patched at the scoring level.
- **The sha256 freeze (Q3) blocks instrument-shopping.** The item set, class definitions, and
  commit-vs-decline threshold are frozen before the first probe call, so no one can re-pick which
  items count as forced-both, or re-draw the commit/decline line, after seeing which way the models
  lean — the same freeze the sibling gates rely on.
- **The higher bar on commit (Q3.3) prevents manufacturing a layer win.** Because commit is the
  burden-discharging surprise for (A), it must clear the higher anti-cheat bar and survive the
  clean-subset check, so a commit verdict cannot rest on items that are really leaning homonyms.
- **The named failure mode and how Q1 forecloses it.** The danger is an **under-certified pun that
  is really a leaning homonym**: per caveat 2 of
  [`result/within-lexical-scalar-vs-disjunctive-v1`](../../findings/results/within-lexical-scalar-vs-disjunctive-v1.md)
  a lean *suppresses* `UNCLEAR`, so such an item presents as commit and biases spuriously toward (A).
  Q1's two-part certification (the zeugma / co-predication structural frame **plus** an independent
  balance check, both frozen) is exactly what forecloses it; and where that certification cannot be
  made independent of model output, the honest outcome is "cannot cleanly certify" (trigger (c),
  fork stays at R1), **not** a relaxed criterion that lets a leaning item through.

Nothing here may be used to *avoid* a result. If a session ratifying this page finds itself wanting a
particular pole (commit or decline), that is the anti-cheat violation — stop
([`PROTOCOL.md`](../../../PROTOCOL.md) §2).

## What a later session must do to ratify

This page is **opened session 89 and is not eligible for ratification this session**. To ratify, a
*later* session must:

1. Launch an **independent fresh-agent adversarial review** ([`PROTOCOL.md`](../../../PROTOCOL.md)
   §2) — not the agent that drafted this page — that reads the four questions, the options, the
   provisional defaults, and the dependency pages, spot-checks the verbatim quotes against their
   source pages, and returns a verdict with written rationale (adopt the defaults / adopt another
   option / keep open with what is missing), recorded `resolved-by: autonomous (adversarial review)`.
2. Confirm the verdict is **not result-motivated** (no probe has run; ratifying fixes the yardstick,
   never the result — [`CLAUDE.md`](../../../CLAUDE.md) rule 6).

**Even after ratification the run is NOT automatic.** It remains gated by a fresh, independent
**pre-run critic GO/NO-GO** against the *frozen* design and a **budget** check
([`CLAUDE.md`](../../../CLAUDE.md) rule 8); a NO-GO defers the run rather than relaxing any band. The
honest expectation — stated by the essay's trigger (c) — is that a first attempt may not cleanly
certify a forced-both item, in which case the fork stays at R1 and no verdict is licensed.
