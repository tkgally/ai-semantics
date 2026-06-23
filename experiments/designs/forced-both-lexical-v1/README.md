# forced-both-lexical-v1 — build attempt (terminated at certification; trigger (c))

**What this is.** A *build attempt* for the discriminating test named by
[`essay/layer-specialness-vs-always-resolvability`](../../../wiki/findings/essays/layer-specialness-vs-always-resolvability.md),
under the resolved gate
[`decisions/resolved/forced-both-lexical-operationalization`](../../../wiki/decisions/resolved/forced-both-lexical-operationalization.md)
(ADOPT DEFAULTS: Q1-iii zeugma/co-predication frame **+** an independent balance check, frozen;
Q2-i forced-single-application instrument; Q3 frozen reading rule; Q4 `internal-contrast-only`).

**Outcome: trigger (c) — *cannot cleanly certify*. No model was ever queried. $0 spent.** The
fork stays at **R1**. This directory is the reproducible record of *why*, so a later session does
not re-attempt the same dead end blindly.

## What was attempted, gate question by question

- **Q1-i (structural forced-both frame): BUILDABLE.** `candidate_items.json` holds 8 author-built
  co-predication / zeugma frames over **homonyms** (unrelated senses), each yoking one token to two
  complements that demand a different sense (e.g. *"The bank was slick with mud and badly short on
  cash"* — `slick with mud` selects river-edge, `short on cash` selects finance; a single-sense
  reading makes one complement anomalous). The structural criterion can be checked before any model
  call, so this half is satisfiable.
- **Q2-i (forced-single-application instrument): BUILDABLE.** Each item carries a downstream task
  that *only one reading licenses* (e.g. *"treat the bank as a physical place — can a person walk
  along its edge?"*), so "it means both" cannot complete the task. This is the strongest part of
  the gate and it is constructible; it is **not** the blocker.
- **Q3 (frozen reading rule): INHERITABLE.** The response-class map (refuse → decline (B);
  force-one-reading → commit (A); answer-both → own class; answer-cleanly → commit (A)), the
  clear-class precondition (C3), the higher anti-cheat bar on commit, and C1/C4 are all inherited
  verbatim from the sibling gates. Not the blocker.
- **Q1-ii (independent, *not-model-based* balance check that neither sense dominates): NOT
  SATISFIABLE from reachable resources. This is the wall, exactly where the gate and the essay said
  it would be.**

## Why Q1-ii fails (the load-bearing finding)

The gate requires certifying — *independent of model output* — that neither sense **dominates**,
because a lean suppresses `UNCLEAR` and biases spuriously toward commit / reading (A)
(within-lexical caveat 2). Two routes exist, and both are closed under autonomy:

1. **An independent annotator judgement on the constructed sentence.** Closed: the project takes
   **no human subjects** (`CLAUDE.md` rule 4); all human bearing comes from *existing* resources,
   none of which rate these author-constructed sentences.

2. **A corpus/frequency check that the two senses are comparably available.** The only reachable
   corpus signal that decomposes word frequency **by sense** is the SemCor sense-tagged corpus via
   WordNet lemma tag counts ([`resource/wordnet-sense-inventory`](../../../wiki/base/resources/wordnet-sense-inventory.md);
   SUBTLEX is word-level only; DWUG "does not tag pairs as polysemy vs. homonymy"). `balance_check.py`
   applies it (output `balance_check.json`). Result:

   | word | sense-A tags | sense-B tags | balance (min/total) | powered (≥5 each)? |
   |------|---:|---:|---:|:--:|
   | bank | 25 | 20 | 0.444 | **yes** |
   | club | 3 | 9 | 0.250 | no |
   | pen | 1 | 8 | 0.111 | no |
   | file | 17 | 1 | 0.056 | no |
   | pitch | 0 | 3 | 0.000 | no |
   | seal | 1 | 3 | 0.250 | no |
   | bark | 1 | 4 | 0.200 | no |
   | spring | 4 | 25 | 0.138 | no |

   **Only 1/8** candidates (bank) has ≥5 SemCor tags on *both* senses (the rest are statistically
   powerless — SemCor is a ~200k-word corpus and most homonym senses are tagged 0–4 times), and
   that **same 1/8 (bank)** is also the only one to fall in a generous balanced band [0.40, 0.60].
   This reflects a real
   regularity, not bad luck: WordNet orders senses by frequency, and homonyms characteristically
   have a **dominant** sense — so a frequency-balanced homonym is the rare exception, and the corpus
   has too few tags to certify even those.

**The deeper, structural defect (holds even for `bank`).** A SemCor balance ratio measures
**general-usage** sense balance across the whole corpus. It does **not** measure the balance of the
*specific constructed co-predication sentence*. And a co-predication frame forces both senses
precisely by yoking **each sense to its own complement**, so the in-item balance is set by the
*relative pull of the two complements* (`slick with mud` vs `short on cash`) — a property of the
constructed item that no general-frequency statistic can see. The only instruments that could
measure the *constructed item's* balance directly are (i) a human annotator on that sentence
(closed — no human subjects) or (ii) the model's own response (forbidden — that is the circular,
operationalization-tuning failure mode the gate exists to prevent). So even a perfectly
frequency-balanced homonym would leave Q1-ii's *in-item* balance uncertified.

**Net:** at most **N=1** candidate (bank) clears even the wrong (general-frequency) balance proxy,
and *no* candidate's constructed-sentence balance can be certified without a human annotator
(unavailable) or model output (forbidden). N=1 is also far too thin to read a per-model pattern.
All three clauses of the essay's trigger (c) are met: the item **cannot be certified forced-both
rather than a leaning homonym** without leaning on model output, **and** N is too thin. No verdict
on (A) vs (B) is licensed; the fork **stays at R1**.

## Anti-cheat note

This is a **NO-GO at certification**, not a result, and it makes a spurious (A) win *harder*, not
easier: the honest move on an uncertifiable item is to *declare it uncertified* (the gate's
fail-safe), never to relax the balance band to manufacture a runnable item. No band was relaxed; no
model was queried; no spend opened. The outcome is the essay's pre-registered honest expected first
outcome, reached by actually attempting the build rather than asserted in advance.

## Reproduce

```
pip install nltk && python3 -c "import nltk; nltk.download('wordnet')"
python3 balance_check.py    # writes balance_check.json ; no API, no model call
```

Files: `candidate_items.json` (8 co-predication frames + Q2-i tasks), `balance_check.py` +
`balance_check.json` (the Q1-ii SemCor check), this `README.md`. Writeup:
[`result/forced-both-lexical-build-attempt-v1`](../../../wiki/findings/results/forced-both-lexical-build-attempt-v1.md).
