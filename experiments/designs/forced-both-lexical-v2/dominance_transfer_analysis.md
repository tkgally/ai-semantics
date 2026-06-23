# Q-B-1 transfer-to-item analysis — does general-usage balance transfer to these 43 pun items?

This document states, **neutrally and both ways**, the one question a fresh independent pre-run
critic must rule on before any model call: **is the Q-B-1 "argued transfer-to-item dominance step"
satisfiable for the 43 frozen balanced-homonym pun items, such that a *commit* verdict on the Q2-i
instrument could be certified non-spurious?** GO → build the instrument and run within budget;
NO-GO → trigger (c) again, fork stays at R1. The builder records a tentative lean at the end but does
**not** decide; the critic decides.

## What is established (not in dispute)

1. **Co-activation: anchored.** Each of the 43 items is a SemEval-2017 homographic pun whose gold
   names two WordNet 3.1 senses jointly evoked *on that sentence* — the ratified **Q4 co-activation**
   anchor (session 93). Both senses are human-certified *present*.
2. **Homonymy: frozen proxy.** All 43 pass the different-lexfile proxy (the two meanings share no
   `(ss_type, lexfile)` pair) — the disclosed Q-C-1 homonymy criterion, frozen pre-call. (A proxy,
   not a human homonymy label; over/under-counts at the margin.)
3. **General-usage balance: human-anchored.** Each word is balanced in **general usage** by a human,
   model-independent norm set — eDom `min(Freq1,Freq2)/(Freq1+Freq2) ≥ 0.40` (13 words) or Rodd &
   Gilbert spoken `D ≤ 0.20` (10 words), CC BY 4.0. This is a *real* dominance anchor, and a strict
   upgrade over v1's SemCor proxy (which had power for only 1 word). **Power is no longer the
   blocker.**

So v2 has cleared everything v1 lacked *except* the one thing v1 also flagged as structural: the
transfer from **general-usage** balance to **in-item** balance.

## The case FOR GO

- **Asymmetric interpretability protects (B).** Per
  [`result/within-lexical-scalar-vs-disjunctive-v1`](../../../wiki/findings/results/within-lexical-scalar-vs-disjunctive-v1.md)
  caveat 2, an in-item lean **suppresses `UNCLEAR`** — it biases toward **commit**, never toward
  decline. So any uncontrolled in-item lean works *against* a decline. One could pre-register, before
  any call: **decline → supports (B)** (robust to lean, which could only have hurt it); **commit →
  "cannot certify"** (an in-item lean is uncontrolled, so commit cannot clear Q3.3's "holds on items
  with no disclosed lean" bar). This makes the *surprising (A) win literally unreachable* from the
  design — exactly the anti-cheat-positive direction the gate wants — while a **(B) decline remains a
  real, readable result** at N=43.
- **Attested > author-built (Q-C-1).** The session-93 reviewer judged attested puns "arguably
  stronger than author-built zeugma frames, since the joint-sense requirement is what makes the pun
  work." The 43 items are genuine forced-both devices, not stipulations.
- **A decline would be a genuine finding.** If the models meet attested puns with the same abstention
  the relational dual-binding drew (3/3 `UNCLEAR`), that confirms the deflationary **(B)
  always-resolvability** and discharges the essay's caveat-1 residual — the headline payoff, reached
  honestly.

## The case FOR NO-GO

- **Transfer-to-item is still unproven — and the resource cannot measure it.** General-usage balance
  is a property of the *word*; in-item balance is a property of the *sentence*. v1's load-bearing
  finding: in-item balance "is set by the *relative pull of the two complements* … a property of the
  constructed item no general-frequency statistic can see"
  ([`result/forced-both-lexical-build-attempt-v1`](../../../wiki/findings/results/forced-both-lexical-build-attempt-v1.md)).
  The eDom / Rodd & Gilbert norms rate the **word in isolation** (Rodd & Gilbert verbatim: word
  association "in the absence of any biasing, pre-determined context"). They do **not** rate the 43
  sentences. So no-general-usage-lean ≠ no-in-item-lean; the Q1-ii gap is *softened, not closed*
  ([`resource/homonym-meaning-dominance-norms`](../../../wiki/base/resources/homonym-meaning-dominance-norms.md)).
- **The pun genre positively installs the lean.** [`essay/presence-is-not-balance`](../../../wiki/findings/essays/presence-is-not-balance.md)
  (session 93): a pun's setup/punchline mechanics bias *against* in-item balance — a salient default
  reading is subverted by a less-salient surprise. So the 43 items are expected to lean in-item
  **systematically**, toward the surface/setup sense, and selecting general-usage-balanced *words*
  removes none of this *sentence-level* asymmetry. The directional, non-averaging lean defeats even
  an aggregate-over-items argument.
- **A pun is not "no reading to pick."** The fork's discriminating stimulus needs an item where
  committing to one reading *loses the communicative point* **and** there is *no reading to pick* —
  the lexical analogue of the relational dual-binding ("bound to two figures at once, so there is no
  reading to pick"). A pun **affords** a pickable surface reading — that *is* the setup; picking it
  merely misses the joke, it does not make the sentence anomalous. So the Q2-i forced-single-
  application task is **completable** on a pun by reading the surface sense → the expected response is
  *commit-to-surface* → which, under the asymmetric rule above, scores as **"cannot certify."** The
  design would therefore be expected to spend budget to produce mostly **non-verdicts**, with a
  (B) decline the less likely outcome — not the clean asymmetric test the fork needs.
- **Commit cannot clear Q3.3.** The higher bar requires commit to "hold on items certified
  forced-both *without a disclosed lean*." We can certify no-*general-usage*-lean but **not**
  no-*in-item*-lean, so a commit verdict is uninterpretable by construction — and a commit is the
  expected response (surface reading). The one verdict the items most readily produce is the one the
  design cannot certify.

## The crux

The transfer-to-item step is **the** owed step (Q-B-1), and the only honest way to discharge it is a
signal that reads *in-item* balance on the actual sentence. Two such signals exist — a human
annotator on the 43 sentences (barred: no human subjects) or the model's own output (forbidden:
circular). The newly-anchored word-grain norms are a genuine improvement but are the *wrong grain*;
and the pun genre makes the residual in-item lean **systematic and directional**, not noise that
averages out. Whether the asymmetric decline-only design is nonetheless a legitimate GO (a real
chance at a clean (B) decline) or a NO-GO (an instrument that mostly produces "cannot certify" for
real spend, with commit uninterpretable by construction) is the judgement the critic must make.

## Builder's tentative lean (NOT a decision)

The builder leans **NO-GO / trigger (c)**: power is solved but transfer is not, and the pun genre
appears to guarantee the in-item lean the dominance step cannot detect, so a commit is uninterpretable
and a decline is the less-likely outcome — the clean asymmetric verdict the fork needs is unlikely to
materialize, and the honest expected outcome is again "cannot cleanly certify," now sharper: the
blocker is *no longer power, but transfer-to-item*, and the specific missing resource is **per-item,
in-context graded balance on the actual pun sentences**. But this is exactly the kind of call the
gate routes to a *fresh* critic, and the builder defers.
