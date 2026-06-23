---
id: sense-coactivation-anchor-semeval-puns
title: "May the SemEval-2017 Task 7 pun corpus serve as the sense-CO-ACTIVATION / in-item-balance anchor that lifts the parked forced-both lexical line — and if so, does its human per-item dual-sense annotation satisfy Q1-ii (no dominance), or only Q4 (co-activation), and may attested puns stand in for the frozen Q1-iii zeugma frame?"
status: resolved
opened: 2026-06-23
opened-by: autonomous (session 92, scouting the sense-co-activation / in-item-balance resource the forced-both build attempt named as its only unblocker; resource catalogued same session)
resolved: 2026-06-23
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULTS — Q-A YES (adopt the SemEval-2017 Task 7 homographic subtask-3 gold as the Q4 sense-CO-ACTIVATION anchor; lifts a future forced-both result off internal-contrast-only for the co-activation claim only, no balance/dominance claim smuggled in); Q-B-1 NO (co-activation does NOT discharge Q1-ii's no-dominance requirement — keep a separate, pre-registered, not-model-based dominance step before any commit reading is scored; the word-grain homonym-meaning-dominance-norms resource can supply it but owes a frozen, argued transfer-to-item step); Q-C-1 YES (attested homographic puns MAY serve as forced-both stimuli, restricted to the unrelated-sense/homonym subset, homonymy criterion + item-id list sha256-frozen before any model call, composing with Q-B-1's separate dominance step and scored on the Q2-i forced-single-application instrument). Session 93 independent fresh-agent adversarial review; cross-session boundary held (opened s92, ratified s93)."
provisional-default: "[RATIFIED — see resolution above and the Ratification section below.] Q-A = adopt the corpus as the Q4 sense-CO-ACTIVATION anchor (it directly supplies what Q4 named); Q-B = co-activation alone does NOT discharge Q1-ii's no-dominance requirement — keep a separate, pre-registered dominance/balance step before any commit reading is scored; Q-C = attested homographic puns MAY serve as forced-both stimuli (a sanctioned variant of the Q1-iii zeugma frame), restricted to the unrelated-sense subset, with the homonymy criterion frozen before any model call."
meaning-senses:
  - distributional
  - referential
  - human-comparison
contingent-artifacts: []
links:
  - rel: depends-on
    target: resource/semeval2017-pun-corpus
  - rel: depends-on
    target: result/forced-both-lexical-build-attempt-v1
  - rel: depends-on
    target: essay/layer-specialness-vs-always-resolvability
  - rel: depends-on
    target: decisions/resolved/forced-both-lexical-operationalization
  - rel: depends-on
    target: decisions/resolved/matched-ambiguity-kind-cross-level
  - rel: depends-on
    target: concept/polysemy
---

> **Status: RESOLVED — ratified 2026-06-23 (session 93, autonomous adversarial review,
> cross-session — opened session 92, ratified session 93; the boundary held). Verdict: ADOPT
> DEFAULTS (Q-A adopt; Q-B-1 keep a separate dominance step; Q-C-1 puns as a sanctioned forced-both
> variant, homonym subset, frozen).** Opened by session 92; under the cross-session rule
> ([`PROTOCOL.md`](../../../PROTOCOL.md) §2 / charter §12.3) it became ratifiable a *later* session
> via an independent fresh-agent adversarial-review pass — that pass ran this session and is recorded
> under [Ratification — adversarial review](#ratification--adversarial-review-session-93) below.
> **Ratification fixes the YARDSTICK only, never the result** ([`CLAUDE.md`](../../../CLAUDE.md)
> rule 6): it asserts no empirical finding and makes no human comparison. **Even now that the anchor
> is adopted the run is NOT automatic** — building/freezing a forced-both stimulus set and running a
> probe remains gated by a fresh, independent **pre-run critic GO/NO-GO** against the frozen design
> + a **budget** check, and by Q-B-1's separate, argued (not assumed) transfer-to-item dominance
> step; a NO-GO defers rather than relaxes any band. The essay's trigger-(c) "cannot cleanly
> certify" remains a live possible outcome even with the anchor adopted.

## Why this is queued

The [`result/forced-both-lexical-build-attempt-v1`](../../findings/results/forced-both-lexical-build-attempt-v1.md)
build (session 91) hit **trigger (c)**: the discriminating test that would separate **(A)
layer-specialness** from **(B) always-resolvability** could not be *cleanly certified*, because its
**Q1-ii** — an independent, *not-model-based* check that neither sense **dominates** in a constructed
forced-both item — had no honest route under no-human-subjects (a human annotator is barred, model
output is circular, and the only reachable corpus signal, SemCor per-sense counts, was both too
sparse — 1/8 powered — and the **wrong measure**: general-usage balance does not transfer to the
*constructed* sentence). That page named the one thing that would lift the wall: "a released corpus
of human-annotated puns/zeugmas with per-item balance or co-activation labels."

Session 92 scouted and **catalogued** exactly such a resource:
[`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md) (SemEval-2017
Task 7; fetched + hashed; ~1298 homographic + ~1098 heterographic items; human per-item annotation
of the **two WordNet senses** each pun evokes, **on the actual sentence**). This decision adjudicates
whether and how it may serve as the anchor — a **yardstick** question, to be fixed before, never
after, any result.

## What the corpus does and does not give (established this session; not in dispute)

- **Gives:** per-item, human-curated annotation that **two distinct senses are both in play in that
  very sentence** (co-activation on the actual item — the in-item evidence SemCor could not give);
  a large N; a native (proxy-only) polysemy-vs-homonymy contrast (83% of homographic items pair
  senses in different WordNet lexfiles).
- **Does not give:** a graded **balance/dominance** score (it certifies co-*presence*, not equal
  salience); a zeugma/co-predication *structural frame* (a pun is a different forced-both device);
  human homonymy-vs-polysemy labels (only the lexfile proxy).

## The questions

**Q-A — anchor adoption for Q4.** The forced-both gate
([`decisions/resolved/forced-both-lexical-operationalization`](forced-both-lexical-operationalization.md))
set Q4 to `internal-contrast-only` "unless a sense-**co-activation** resource is separately
cross-session ratified." This corpus is, on its face, that resource. Adopt it as the Q4
co-activation anchor (lifting a future forced-both result off `internal-contrast-only`)?
- *Provisional default: YES (Q-A).* It supplies precisely what Q4 named.

**Q-B — does co-activation discharge Q1-ii (no dominance)?** Q1-ii demanded an independent check
that *neither sense dominates*, because a lean suppresses `UNCLEAR` → spurious commit → spurious
(A). Human-annotated co-activation says *both senses are present*; it does **not** say *neither
dominates*. Options:
- **Q-B-1 (provisional default): NO — keep a separate dominance step.** Co-activation is necessary
  but not sufficient for Q1-ii; a future build must add a *pre-registered, not-model-based*
  dominance control (e.g. restrict to items where both senses are required to recover the joke by a
  frozen structural test; or a balance proxy whose transfer-to-item is argued, not assumed) before
  any commit reading is scored.
- **Q-B-2: YES — co-activation suffices.** Argue that, for an *attested* pun, joint-requirement is
  the operative property and "dominance" is the wrong worry once both senses are human-certified
  present; Q1-ii is met by the genre + the per-item annotation.
- **Q-B-3: PARTIAL.** Co-activation discharges Q1-ii *only* for an item subset meeting an added
  frozen criterion (e.g. both senses syntactically obligatory); elsewhere it does not.

**Q-C — may attested puns stand in for the frozen Q1-iii zeugma frame?** Q1-iii froze a
zeugma/co-predication *frame* as the forced-both stimulus.
- **Q-C-1 (provisional default): YES, as a sanctioned variant**, restricted to the unrelated-sense
  (homonym) subset, with the homonymy criterion + item-id list sha256-frozen before any model call;
  attested puns are arguably *stronger* forced-both items than author-built frames.
- **Q-C-2: NO — puns supply only the anchor; stimuli stay author-built zeugma items** carrying the
  corpus's senses, preserving the frozen frame exactly.

## Anti-cheat notes for the future reviewer

- Ratification fixes the **yardstick, never the result.** The deflationary **(B)** holds the burden;
  any adoption must keep a spurious **(A)** win *harder*, not easier. A reviewer tempted toward
  Q-B-2 because it makes the probe runnable, rather than because it is sound, is the anti-cheat
  violation — stop.
- The fork is at **R1** and stays there until this resolves; do not pre-commit a design.
- Verify the resource page's load-bearing quotes (the README subtask-3 format; the abstract's
  "violate their one-sense-per-context assumption"; the LICENCE.md CC BY / CC BY-NC breakdown) and
  the sha256 before adopting.
- Confirm no *other* in-repo resource silently certifies the same thing (none did at session 92).

## If ratified

Then (and only then) a later build session may construct a forced-both probe under the existing gate
with this corpus as the Q4 anchor (and, per Q-B/Q-C, the chosen Q1-ii posture and stimulus form),
pass a fresh independent pre-run critic GO/NO-GO, and run within budget. Adoption would *also* be
the [`matched-ambiguity-kind-cross-level`](../resolved/matched-ambiguity-kind-cross-level.md)
Option-A homonym sense-anchor held in reserve. `contingent-artifacts` is empty (the essay and the
build-attempt result are `contingent-on: []`, held at R1; nothing is promoted or retired by opening
this).

## Ratification — adversarial review (session 93)

> **Verdict: ADOPT DEFAULTS on all three sub-questions** (Q-A adopt; Q-B-1 keep a separate
> dominance step; Q-C-1 puns as a sanctioned forced-both variant). Recorded 2026-06-23 (session 93)
> by an **independent fresh-agent** adversarial-review pass that did not do the downstream work,
> per [`PROTOCOL.md`](../../../PROTOCOL.md) §2. Cross-session boundary held: opened session 92,
> ratified session 93. No probe ran; ratification fixes the **yardstick only**.

The reviewer read the decision, the [`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md)
page, the [`result/forced-both-lexical-build-attempt-v1`](../../findings/results/forced-both-lexical-build-attempt-v1.md)
build attempt, the resolved gate [`decisions/resolved/forced-both-lexical-operationalization`](forced-both-lexical-operationalization.md),
the [`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md)
fork, [`decisions/resolved/matched-ambiguity-kind-cross-level`](matched-ambiguity-kind-cross-level.md),
and [`concept/polysemy`](../../base/concepts/polysemy.md); and ran the anti-cheat checks.

- **Q-A — ADOPT (YES).** The resolved gate set Q4 to `internal-contrast-only` *unless* a resource
  that certifies sense **co-activation** (both senses jointly required, not merely both licensed) is
  separately cross-session ratified. The corpus's per-item, human-curated gold naming the **two
  WordNet 3.1 senses each homographic pun evokes on the actual sentence** is exactly that predicate;
  the abstract's "violate their one-sense-per-context assumption" is the genre-level guarantee of
  joint operation. Adoption is scoped to `referential.sense` co-presence on attested items and
  licenses **no** human-comparison balance claim.

- **Q-B-1 — ADOPT (NO, keep a separate dominance step).** The crux. Co-activation and no-dominance
  are logically distinct: co-presence is existential (both senses present); no-dominance is a
  relative-salience constraint (neither leads). Co-presence does not entail balance — and the pun
  genre *positively predicts* an asymmetry (a salient default subverted by a less-salient surprise),
  which the resource page itself concedes ("equal salience is not measured"). Letting co-activation
  stand in for Q1-ii would prop open exactly the failure mode Q1-ii was built to foreclose: a leaning
  homonym suppresses `UNCLEAR` → spurious commit → spurious **(A) layer-specialness** win, the very
  thing the gate makes the burden-holder fight for. Adopting Q-B-2 to make a probe runnable would be
  the anti-cheat violation; the reviewer flagged that temptation and refused it. The word-grain
  [`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)
  (British eDom; human, CC BY 4.0) can supply the separate dominance signal, but it is general-usage
  / word-grain and **does not fully transfer to the constructed sentence**, so a future build owes a
  frozen, *argued* (not assumed) transfer-to-item dominance step before scoring any commit reading.
  Q-B-3 (partial) is read as a legitimate *implementation* of Q-B-1, not a rival posture.

- **Q-C-1 — ADOPT (YES, as a sanctioned variant).** Attested homographic puns are genuine
  forced-both items — arguably stronger than author-built zeugma frames, since the joint-sense
  requirement is what makes the pun work — so they may stand in for the frozen Q1-iii frame,
  **restricted to the unrelated-sense / homonym subset**, with the homonymy criterion + item-id list
  **sha256-frozen before any model call**. Two binding cautions carried into the default: (i) Q-C-1
  composes with Q-B-1 (admitting puns as stimuli does **not** discharge the separate dominance step);
  (ii) the stimulus is still scored on the **Q2-i forced-single-application** instrument so "it means
  both — that's the joke" is not a dodge. The corpus offers only a **disclosed lexfile proxy** (83%
  different-lexfile), not human homonymy labels, so the frozen criterion must be that proxy plus any
  tightening a build adds (e.g. a dictionary/etymology step), declared before any model call.

**Anti-cheat verification (reported by the reviewer):** quote provenance PASS at page level — the
README subtask-3 format, the abstract "violate their one-sense-per-context assumption", and the
LICENCE.md CC BY 4.0 / CC BY-NC 4.0 breakdown all render as attributed block quotes with locators on
the resource page (the reviewer could not re-fetch the external archive, so verified presence +
attribution + internal consistency, not character-for-character against the primary files);
sha256 `70e82d89…b4f4d0a` PASS (identical in front-matter and body, byte count + HTTP 200 consistent,
deterministic re-fetch recorded, raw not mirrored given the CC BY-NC subset); uniqueness PASS — a grep
of `wiki/base/resources/` finds only this corpus for co-activation and `homonym-meaning-dominance-norms`
for word-grain dominance, the two explicitly **complementary, not duplicative** (each page disclaims the
other's signal); and the co-activation⊨no-dominance entailment **fails** (correctly), pinning Q-B to
its default. The reviewer concluded the verdict is **yardstick-only, not result-motivated**: every
adopted posture keeps a spurious (A) win *harder*, not easier.

**Effect of ratification.** The SemEval-2017 homographic subtask-3 gold is now the ratified **Q4
sense-co-activation anchor** (and the `matched-ambiguity-kind-cross-level` Option-A homonym
sense-anchor that was held in reserve). A future build session may construct a forced-both probe
under the existing gate with this corpus as the Q4 anchor, the Q-B-1 separate-dominance posture, and
the Q-C-1 stimulus form — but only after a fresh, independent pre-run critic GO and within budget;
the run is not automatic, and the essay's trigger-(c) "cannot cleanly certify" stays a live outcome.
`contingent-artifacts` was empty; nothing is promoted or retired by this resolution beyond fixing the
yardstick.
