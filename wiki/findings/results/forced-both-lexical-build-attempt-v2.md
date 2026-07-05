---
type: result
id: forced-both-lexical-build-attempt-v2
title: "Forced-both lexical probe — BUILD ATTEMPT v2 under the ratified SemEval co-activation anchor terminates again at certification (trigger (c)): power is solved (43 attested balanced-homonym pun items) but the Q-B-1 transfer-to-item dominance step is not satisfiable and a pun is not the fork's 'no-reading-to-pick' object. Fresh pre-run critic NO-GO; no model run; $0."
meaning-senses:
  - distributional
  - referential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-23
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/forced-both-lexical-build-attempt-v1
  - rel: depends-on
    target: essay/layer-specialness-vs-always-resolvability
  - rel: depends-on
    target: essay/presence-is-not-balance
  - rel: depends-on
    target: resource/semeval2017-pun-corpus
  - rel: depends-on
    target: resource/homonym-meaning-dominance-norms
  - rel: depends-on
    target: result/within-lexical-scalar-vs-disjunctive-v1
---

# Result: forced-both lexical probe — build attempt v2 terminates again at certification (trigger (c))

> **Status: proposed (2026-06-23, session 94).** The **second** build attempt for the discriminating
> test of [`essay/layer-specialness-vs-always-resolvability`](../essays/layer-specialness-vs-always-resolvability.md),
> now under the session-93 anchor ruling
> [`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../decisions/resolved/sense-coactivation-anchor-semeval-puns.md)
> (the SemEval-2017 pun corpus adopted as the gate's **Q4 sense-co-activation** anchor; **Q-B-1** a
> separate, frozen, not-model-based dominance step with an *argued transfer-to-item* still owed).
> **Outcome: a fresh independent pre-run critic returned NO-GO → trigger (c), *cannot cleanly
> certify*. No model was queried; $0 spent. The fork stays at R1.** v2 *removes* v1's power problem
> (43 attested balanced-homonym pun items, vs v1's N=1) and so **isolates the transfer-to-item
> problem** — which is not satisfiable, for two compounding reasons plus a data-integrity finding.
> Build artifacts: [`experiments/designs/forced-both-lexical-v2/`](../../../experiments/designs/forced-both-lexical-v2/).

## Lead with the cap (binding, read first)

- **No probe ran.** This is a **certification NO-GO**, not a measurement of any model. It makes **no
  human-comparison claim** and **no within-model claim** (`anchor: internal-contrast-only` is carried
  as the terminal "no human number enters" declaration; here it is stronger — no model number enters
  either).
- **It does not move the (A)/(B) fork.** Neither layer-specialness (A) nor always-resolvability (B)
  is supported or weakened. The fork remains at **R1**, the deflationary **(B)** still holding the
  burden — exactly as before the attempt.
- **What it *is*:** a sharper localization of the v1 wall. v1 hit the Q1-ii balance check two ways —
  no power **and** no transfer. v2 shows the **power problem is solved** by the ratified co-activation
  anchor + the human dominance norms, and that the **transfer-to-item problem remains and is in fact
  structural** for the pun genre. The most-obvious "lift it off R1" route v1 named (a dense enough
  balance resource) is therefore closed with a reason, not merely unmet.

## Headline

**With the SemEval pun corpus (Q4 co-activation, ratified) and human word-grain dominance norms in
hand, a forced-both lexical item *still* cannot be cleanly certified — but the blocker has moved from
power to transfer.** There are now **43 attested, human-co-activation-certified, homonym pun items
(23 words) whose pun-word is balanced in *general usage*** by a human norm — ample power. The
remaining, undischarged step is **Q-B-1's argued transfer-to-item**: general-usage word-grain balance
does not defensibly transfer to *in-item* balance on the specific pun sentences, the pun genre
*systematically* installs an in-item lean the dominance step cannot detect, and an attested pun is not
the fork's "no-reading-to-pick" object. A fresh independent critic ruled **NO-GO**.

## What was attempted, gate question by question

| gate question | status this attempt |
|---|---|
| **Q4** sense co-activation anchor | **DISCHARGED** — SemEval-2017 homographic subtask-3 gold, ratified session 93; 43 items human-certified two-sense-co-active |
| **Q-C-1** attested puns as forced-both stimuli, homonym subset, frozen | **BUILT** — 1105/1298 homographic items pass the frozen different-lexfile homonymy proxy; subset sha256-frozen (see below) |
| **power** (v1's first wall) | **SOLVED** — 43 balanced-homonym pun items / 23 words (vs v1's 1/8 powered) |
| **Q2-i** forced-single-application instrument | inheritable as in v1; **not built** (the build terminated upstream, as v1 did) |
| **Q3** frozen reading rule | inheritable verbatim from the sibling gates; not the blocker |
| **Q-B-1 / Q1-ii** separate not-model-based dominance step, *argued* transfer-to-item | **NOT SATISFIABLE** — the wall |

### The frozen candidate subset (reproducible, license-clean)

`build_frozen_subset.py` re-fetched the corpus, **re-verified its sha256**
(`70e82d89…b4f4d0a`, HTTP 200, 748,424 bytes — identical to the session-92 hash, deterministic
re-fetch confirmed), applied the frozen homonymy proxy, and intersected the homographic pun-word
vocabulary with two **CC BY 4.0** human dominance-norm sets fetched firsthand from OSF this session
([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)):
British eDom (Maciejewski & Klepousniotou 2016) and the Rodd & Gilbert spoken-ambiguity norms
(*J. Cognition* 10.5334/joc.194). Balanced = eDom `min(Freq1,Freq2)/(Freq1+Freq2) ≥ 0.40` **or**
spoken `D ≤ 0.20`.

- homographic subtask-3 total **1298** → homonym subset **1105** → homonym items in a dominance-norm
  set **220** → **balanced-homonym items 43** (23 words).
- `frozen_subset.json` sha256 **`a066dfbc…b5c9c9fd`** — committed; contains item-ids, lemmas, WordNet
  sense keys, and CC BY 4.0 dominance values **only** (no joke text; the SemEval data includes a CC
  BY-NC 4.0 subset, so the sentences are never mirrored — re-fetch deterministically).

## Why Q-B-1 fails — the load-bearing finding (three compounding parts)

**1. The transfer-to-item is asserted, not arguable — the dominance signal is the wrong grain.** The
eDom and Rodd & Gilbert norms rate a word's balance "in the absence of any biasing, pre-determined
context"
([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)).
A pun sentence *is* a biasing context. v1's structural finding generalizes exactly: in-item balance
"is set by the *relative pull of the two complements* … a property of the constructed item no
general-frequency statistic can see"
([`result/forced-both-lexical-build-attempt-v1`](forced-both-lexical-build-attempt-v1.md)) — for a
pun, the relative pull of setup vs punchline, invisible to a per-word norm. The dominance norms
"soften but do not eliminate the Q1-ii gap; they re-supply, with a better anchor, the general-balance
proxy that attempt already judged insufficient"
([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)).
Q-B-1 demands an *argued* transfer; selecting general-usage-balanced words and asserting in-item
balance is not one.

**2. The pun genre installs the lean systematically and directionally.** This is worse than residual
noise. [`essay/presence-is-not-balance`](../essays/presence-is-not-balance.md): "A homographic pun
works by leading the reader down a salient default reading and then springing a second, less-expected
sense" — so the in-item lean is **directional** (toward the surface/setup sense) and present *by
construction in the genre*. A directional, same-signed bias **cannot be averaged away** across 43
items, so the one move that might rescue a noisy word-grain proxy (aggregate over items) is
unavailable. Per [`result/within-lexical-scalar-vs-disjunctive-v1`](within-lexical-scalar-vs-disjunctive-v1.md)
caveat 2, a lean "*suppresses* `UNCLEAR`" → biases toward **commit** → manufactures a spurious **(A)**
— exactly the failure mode Q1-ii exists to foreclose, now installed by the genre itself.

**3. A pun is not the fork's "no-reading-to-pick" object.** The discriminating stimulus must be the
lexical analogue of the relational dual-binding — "*literally unresolvable* … there is no reading to
pick" ([`result/within-lexical-scalar-vs-disjunctive-v1`](within-lexical-scalar-vs-disjunctive-v1.md),
caveat 1). An attested pun *affords* a pickable surface reading — that is the setup; picking it merely
misses the joke, it does not make the sentence anomalous. So the Q2-i forced-single-application task
is **completable** on a pun by reading the surface sense, and the expected response is
*commit-to-surface*. A pun therefore sits on the *resolvable* side of the very cut the fork tries to
cross — re-importing the SURVIVAL confound rather than dissolving it.

**Data-integrity finding (new this session).** Of the 11 frozen items present in **both** norm sets
(5 words: `calf`, `fan`, `mail`, `plot`, `pupil`), **all 11 disagree** on the balanced/biased
classification (e.g. `calf` eDom 0.476 = balanced but spoken D 0.605 = biased; `fan` 0.459 vs 0.646).
The OR-rule admits an item if *either* norm flags it, so several items enter on one norm while the
*other available human norm contradicts the balance claim*. If two **word-grain** human instruments
cannot agree on a word's isolated balance, the claim that this signal certifies *in-item* balance on a
pun sentence is contradicted at its own grain before the transfer step is even reached.

## The asymmetric-interpretability design, considered and rejected

The strongest case for GO was an asymmetric reading rule: since a lean only biases toward commit
(never decline), pre-register **decline → supports (B)** (robust to any uncontrolled lean) and
**commit → "cannot certify"**. The critic took this seriously and rejected it: (i) by part 3 above the
*expected* response is commit-to-surface, which this rule scores as a non-verdict — so the design
would spend budget to produce mostly "cannot certify", with a (B) decline the *less* likely outcome;
(ii) it conflicts with the gate's symmetric-reporting requirement (Q3.3), in which commit carries a
*higher* bar but must remain *interpretable* — a design where commit is uninterpretable by
construction is a different yardstick than the one ratified; and (iii) it does not discharge Q-B-1 —
it *renames* the unsolved transfer problem as a feature. The lean stays uncontrolled; the design just
declines to read the pole the lean would corrupt.

## Independent adversarial review — fresh pre-run critic (VERDICT: NO-GO)

A fresh independent critic (not the builder) read the gate, the anchor ruling, the v1 result, the two
essays, the dominance resource, the within-lexical caveat, and the build artifacts, spot-checked the
load-bearing quotes, and ruled **NO-GO → trigger (c)**:

- **Transfer-to-item not defensible** — general-usage balance is a word property, in-item balance a
  sentence property; the genre installs a systematic directional lean; the cross-norm disagreement
  (11/11) contradicts even the word-grain signal.
- **A pun is not the fork's discriminating object** — it affords a pickable surface reading; the Q2-i
  task is completable by reading the surface sense (commit-to-surface expected).
- **The asymmetric design is not a legitimate GO** — mostly non-verdicts for real spend; commit
  uninterpretable by construction; renames rather than discharges Q-B-1.
- **Q3.3 commit bar cannot be cleared** — commit must "hold on items certified forced-both *without*
  a disclosed lean" ([`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md),
  Q3.3); we can certify no-*general-usage*-lean (and even that is contradicted across norms) but not
  no-*in-item*-lean.
- **Quote-integrity PASS; anti-cheat PASS** — a GO would make a spurious (A) win *easier* (route a
  genre-manufactured commit toward (A)); NO-GO is the anti-cheat-positive direction; no band relaxed;
  verdict yardstick-only, not result-motivated.

## What this resolves

- **For [`essay/layer-specialness-vs-always-resolvability`](../essays/layer-specialness-vs-always-resolvability.md):**
  its **revision trigger (c)** fires **again**, now sharper — *cannot cleanly certify*, with the
  blocker localized to transfer-to-item rather than power. The essay's conceptual contribution
  survives; its empirical resolution stays **deferred**. The fork stays at **R1**; (B) keeps the
  burden. Logged in-page.
- **For [`essay/presence-is-not-balance`](../essays/presence-is-not-balance.md):** its **trigger (b)**
  (a *demonstrated argued transfer-to-item* would discharge balance) was **attempted and not met** —
  the transfer cannot be argued for the pun genre, and the cross-norm disagreement is fresh
  corroboration of the essay's core (presence ≠ balance; word-grain norms are the wrong grain for
  in-item balance). The essay is strengthened, not retired. Logged in-page.
- **It does not revive, weaken, or strengthen any prior result.** The SURVIVAL result and its caveat 1
  stand unchanged.

## What would lift it off R1 (sharper than v1)

The blocker is no longer power; it is **transfer-to-item**. The missing resource is a **per-item,
in-context, *graded* "neither sense dominates in *this* sentence" signal on the actual forced-both
sentences** — *sentence*-grain, not word-grain; *graded*, not a presence/co-activation label —
separately and cross-session ratified. (Catalogued on [`wanted.md`](../../base/wanted.md).) **Or** an
attested forced-both genre *demonstrated to be balance-unbiased by construction*
([`essay/presence-is-not-balance`](../essays/presence-is-not-balance.md) trigger (c)) — which puns,
by the setup/punchline mechanic, are not. Do **not** relax the balance band to force a runnable item.

## Scope and limits

- **No model run, no spend, no human comparison.** A build-feasibility outcome, not a measurement.
- **The blocker is specific to Q-B-1's transfer-to-item under no-human-subjects** — not a claim that
  forced-both items are impossible in principle, only that they cannot be *cleanly certified* from
  reachable resources today, and that the pun route in particular is structurally blocked by the
  genre's balance bias.
- **n/a on models** — nothing here bears on any model's behavior.

## Reproduce

```
# re-fetch corpus (verify sha256 70e82d89…b4f4d0a) + the two CC BY 4.0 norm files, then:
cd experiments/designs/forced-both-lexical-v2 && python3 build_frozen_subset.py   # no API
```

Artifacts: [`experiments/designs/forced-both-lexical-v2/`](../../../experiments/designs/forced-both-lexical-v2/)
([`README.md`](../../../README.md); `build_frozen_subset.py`; `frozen_subset.json` + `.sha256` — 43 items, no joke text;
`dominance_transfer_analysis.md` — the both-sides Q-B-1 analysis put to the critic).
