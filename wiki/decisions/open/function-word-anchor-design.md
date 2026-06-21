---
id: function-word-anchor-design
title: How to operationalize the function-word-vs-content-word swap probe — what counts as a "frequency-matched" pair, which logprob-free indicator, and which (if any) human anchor?
status: open
opened: 2026-06-21
opened-by: autonomous (session opening the function-word empirical line)
contingent-artifacts:
  - conjecture/function-word-substitutability
---

# Decision: matched-set, indicator, and anchor for the function-word swap probe

## Why this exists

This session opens the empirical line for
[`conjecture/function-word-substitutability`](../../findings/conjectures/function-word-substitutability.md)
— the claim that, for **matched minimal pairs**, swapping a *function word*
(*the* → *a*; *will* → *would*; *because* → *although*; *some* → *every*) shifts
LLM behavior **more** than swapping a *content word* of comparable surface
frequency. It is the most *general* of the project's constructional conjectures
(any model, any matched corpus, any inferential probe) and, by the conjecture's
own admission, the most *abstract* and therefore "the most vulnerable to
operationalization tuning."

The conjecture itself flags the chief cheat-surface: "what counts as a
'frequency-matched' pair is the place a loop can quietly cheat by selecting items
that bias the result," and it instructs: "Lock the matched-pair set **before**
seeing model outputs." This decision is the gate that makes those instructions
binding before any spend. It interlocks three value-laden choices a session must
not auto-take (CLAUDE.md rule 5): **what "matched" means** (Q1), **which
logprob-free indicator stands in for the conjecture's predictions** (Q2), and
**which human resource (if any) backs the result** — i.e. whether the result can
make a human-comparison claim at all, or is most honestly an internal within-model
contrast (Q3).

Two facts constrain the whole space and are stated up front so no option smuggles
them past the reviewer:

- **The logprob blocker is binding.** OpenRouter exposes no prompt/echo-logprobs
  on the panel models
  ([`decisions/resolved/aann-panel-logprob-blocker`](../resolved/aann-panel-logprob-blocker.md)).
  The conjecture's **prediction 1** — "KL divergence on continuation
  distributions is larger after function-word swaps" — is therefore **not runnable
  as written**. Any indicator must be **behavioral / logprob-free**; a true
  continuation-distribution KL is unavailable and only a behavioral *proxy* for it
  can be offered (Q2).
- **The resources this probe wants are not yet in-repo.** There is **no BLiMP
  resource page, no SyntaxGym resource page, and no frequency-norm (SUBTLEX /
  COCA / BNC) resource page** in
  [`base/resources/index.md`](../../base/resources/index.md). Every anchor or
  matching norm below that names one of these is **fetch-and-catalogue-first** —
  it must be fetched, license-checked, inspected, and promoted to a typed
  `resource` page *before* it can be cited. None is asserted as available here.

**This page was opened 2026-06-21 and may be ratified, at the earliest, by a later
session's independent adversarial-review pass. No probe runs before that
ratification.**

## The three sub-questions

### Q1 — On what is "matched" defined, and what counts as matched?

This is the cheat-surface the conjecture explicitly names. The function-swap
condition and the content-swap (control) condition must be made comparable along
the dimension that, if uncontrolled, would *manufacture* the predicted asymmetry —
above all unigram frequency, since the whole point is "comparable behavior for
comparable frequency."

- **Option A — frequency-matched on a corpus frequency norm** (SUBTLEX-US / COCA /
  BNC). The swapped words are matched on log unigram frequency drawn from a single
  human-derived norm. **Design constraint that must be stated, not hidden:**
  function words are overwhelmingly *high*-frequency, while content words are
  mostly *mid-to-low* frequency. A genuinely frequency-matched content control is
  therefore forced toward **high-frequency content words** (very common nouns/verbs
  like *thing*, *make*, *day*), which is a real and narrowing constraint on the
  content-swap inventory — and a place a biased selection could quietly drift into
  unusually contentful or unusually bleached high-frequency items. Whichever norm
  is chosen is **fetch-and-catalogue-first** (no frequency-norm resource exists
  in-repo).
- **Option B — match additionally (or instead) on surface/processing covariates.**
  Beyond unigram frequency, match on **word length, orthographic form / number of
  orthographic neighbors, and local context-predictability** (e.g. cloze /
  bigram-conditioned predictability of the slot). Rationale: two words of equal
  unigram frequency can still differ sharply in how *predictable* they are in the
  carrier sentence, and an unmatched predictability gap could drive a behavior
  shift mistaken for a function-vs-content effect. Cost: each added matching
  constraint shrinks the admissible item pool (already narrow under Option A) and
  raises the build cost; over-matching can leave too few items to reach the
  conjecture's ≥200-pair target.
- **Option C — the level at which matching is enforced.** Either **pair-level**
  (the swapped-*out* and swapped-*in* word within each minimal pair are matched to
  *each other*, so the swap itself is frequency-neutral) **or** **condition-level**
  (the function-swap *set* and the content-swap *set* are matched in *aggregate*
  distribution — same mean/variance of frequency — without per-pair matching).
  Pair-level is the stronger control (it removes within-pair confounds item by
  item) but is the harder to satisfy for function words, whose swap partners
  (*the*↔*a*, *some*↔*every*) have fixed, sometimes very unequal frequencies.
  Condition-level is achievable but lets a within-pair confound survive if the
  aggregate happens to balance.

**Binding across all of Q1:** the matched set is **frozen before any model output
is seen** (the conjecture's own instruction). Item selection, the norm, the
covariates, and the matching level are recorded and hashed at the build session;
no item is added, dropped, or re-binned after the first probe call. This is the
condition that turns "lock the set before seeing outputs" from advice into a gate.

### Q2 — Which behavioral, logprob-free indicator?

The conjecture's three predictions were written assuming a continuation-likelihood
/ KL instrument. That instrument is dead on the panel
([`decisions/resolved/aann-panel-logprob-blocker`](../resolved/aann-panel-logprob-blocker.md)).
A behavioral substitute is required, and which one is a choice. The indicator must
be one on which **a content-word swap moving behavior as much as (or more than) a
function-word swap is cleanly recordable as a falsification** (the conjecture's
falsify arm is a *positive* result for the distributional position).

- **Option (i) — graded forced-choice / entailment-flip rate on minimal pairs**
  (mirrors prediction 2, "entailment behavior flips more often"). For each minimal
  pair, present the pre-swap and post-swap sentence in a controlled
  entailment/acceptability frame and record whether the model's inferential
  judgment (entails / contradicts / neutral, or a graded naturalness preference)
  **flips** between the two. The condition contrast is *flip rate after
  function-swap* vs *flip rate after content-swap*. **Strength:** directly tracks
  prediction 2, runs logprob-free on the panel, and the falsification is legible (a
  content-swap flip rate ≥ the function-swap flip rate after matching). **Weakness:**
  a forced-choice/acceptability frame can collapse into shallow *form*-acceptability
  that is not inference-tracking (the validity guard carried from
  [`decisions/resolved/aann-panel-logprob-blocker`](../resolved/aann-panel-logprob-blocker.md));
  the inferential frame must be load-bearing, with a manipulation-check baseline
  showing the judgment moves *because* the relation changed.
- **Option (ii) — behavioral continuation-divergence proxy** standing in for
  prediction 1's KL (which is unavailable). Sample N continuations per sentence at
  fixed temperature and measure **divergence between the pre-swap and post-swap
  continuation sets** by a behavioral surrogate — e.g. sampled-continuation
  agreement / overlap, or paraphrase-preference shift (does the model still rank
  the same paraphrase as best after the swap?). The condition contrast is the
  function-swap divergence vs the content-swap divergence. **Strength:** it is the
  nearest honest stand-in for the abstract "downstream distribution moved" claim
  prediction 1 was about. **Weakness — flag it loudly:** a sampled-overlap proxy is
  *not* a continuation-distribution KL; it is noisy, temperature-sensitive, and
  conflates surface lexical overlap with inferential divergence, so it is the
  weaker and more tunable of the two. It should be at most a *secondary* indicator,
  never the sole confirm/falsify-bearing test.

### Q3 — Stimulus source and the human backing (the anchor proper)

Two interlocking choices: where the minimal pairs come from, and whether any
human-labeled resource grounds the comparison.

**Stimulus source.**
- **Synthetic minimal pairs** built to the chosen frequency norm and matching
  scheme (Q1), as the AANN and dative lines did to defend against training-data
  contamination. The norm anchors the *matching*, not the specific items.
- **Lifted from an existing minimal-pair resource** — e.g. BLiMP's function-word /
  grammatical minimal pairs, which come with human acceptability backing. This
  buys a human signal but risks contamination (published, widely-trained items) and
  ties the inventory to BLiMP's coverage. **BLiMP is fetch-and-catalogue-first** (no
  BLiMP resource page exists in-repo).

**The human anchor — and the result posture.** The honest question is whether this
conjecture's result can make a **human-comparison claim** at all. Two postures,
both laid out so the reviewer chooses rather than inherits one:

- **Posture 1 — `internal-contrast-only` (within-model contrast).** The conjecture's
  three predictions are all about **differences in model behavior** between two swap
  conditions (function-swap shift vs content-swap shift), both measured on the same
  models with no human number entering. Read this way the result is a clean
  *within-model contrast* and, per CLAUDE.md's anchor rule (state b), needs **no
  resource anchor** — but only after a later session *ratifies* it as
  internal-contrast-only (the terminal state must never be used to dodge a genuine
  anchor obligation). This is the most defensible *minimal* posture and the one the
  predictions, as literally written, support.
- **Posture 2 — human-anchored.** If a human-labeled backing is fetched and
  catalogued, a *calibrated human comparison* becomes possible: e.g. **BLiMP**
  acceptability for the function-word minimal pairs (does the model's flip-rate
  asymmetry track where humans find the swap most disruptive?), or an **NLI
  dataset** to ground the entailment-flip indicator of Q2(i) against human
  entailment labels. Both are **fetch-and-catalogue-first** — naming them here is a
  to-fetch list, not a claim that any is in-repo or that any human number is known.
  This posture is strictly an *upgrade*: it is available only if the fetch clears
  the license/inspection/promotion bar, and it must never be a *precondition* that
  blocks the within-model contrast from running.

## Provisional default (to be adopted, modified, or rejected next session)

Chosen so that a spurious **positive** is *harder*, never easier, and the falsify
arm stays live:

- **Q1 — matched set:** Option A (frequency-matched on a single fetched corpus norm)
  **as the floor**, tightened toward Option B (add length + context-predictability
  matching) and enforced at the **pair level** (Option C, pair-level) wherever the
  function-word swap partners permit; condition-level aggregate matching only where
  pair-level is impossible, reported as such. The high-frequency-content-word
  constraint is stated openly and the content-swap inventory is drawn to *span*
  semantic classes (not cherry-picked). **The full set is frozen and hashed before
  the first probe call.** (Adding matching constraints and freezing the set both
  make a spurious asymmetry harder to manufacture.)
- **Q2 — indicator:** Option (i), entailment-flip / graded forced-choice rate, as
  the **sole confirm/weak/falsify-bearing** indicator (it mirrors prediction 2,
  runs logprob-free, and makes the falsification legible). Option (ii)
  sampled-continuation divergence is **secondary only**, reported as a weak proxy
  for the unavailable prediction-1 KL, and may *characterize* but never *decide* a
  result. A manipulation-check baseline is required so a form-only shallow judgment
  is detectable.
- **Q3 — stimuli + anchor:** **synthetic** minimal pairs (contamination defense),
  built to the Q1 scheme. **Result posture:** start **`internal-contrast-only`** —
  the predictions are a within-model contrast and that is the honest minimal claim —
  with a queued **fetch-and-catalogue-first** attempt at a human backing (BLiMP
  acceptability and/or an NLI dataset) that, *if and only if* it clears the
  promotion bar, upgrades the result to a calibrated human-comparison. The within-
  model contrast never waits on the fetch.

**Anti-cheat (binding falsify arm).** After matching and freezing, a result where
the **content-word swap shifts behavior at least as much as the function-word
swap** is a **clean falsification of the conjecture and a positive result for the
distributional position** — recorded as such, with no re-matching, no item
re-selection, and no indicator re-tuning after seeing outputs. A build-session
pre-run critic certifies the frozen matched set against the frequency norm *before*
any spend; a NO-GO defers the run rather than relaxing the matching. Every joint of
this default makes a spurious positive harder, not easier.

## What the reviewer should weigh

1. Is **frequency-matching on a single unigram norm (Q1 Option A)** an honest floor,
   or does the function-word/content-word frequency mismatch force the content
   control into so narrow a high-frequency band that the comparison is confounded
   regardless — making length + predictability matching (Option B) a *precondition*
   rather than a tightening?
2. Should matching be enforced **pair-level or condition-level (Q1 Option C)**, given
   that several function-word swap partners (*the*↔*a*, *some*↔*every*) have fixed,
   unequal frequencies that pair-level matching cannot satisfy without dropping the
   most diagnostic items?
3. Is the **entailment-flip / forced-choice indicator (Q2 i)** a faithful stand-in
   for predictions that were written around continuation-distribution KL, or does
   demoting prediction 1 to a behavioral proxy (Q2 ii) change what the conjecture
   can be said to have tested — and should the conjecture's prediction-1 wording be
   amended to the behavioral reality before any run?
4. Is the **`internal-contrast-only` posture (Q3 Posture 1)** the honest default, or
   does opening the line *imply* a human-comparison ambition that should make a
   fetched human anchor (BLiMP / NLI) a goal rather than an optional upgrade — and
   if anchored, which human label (acceptability vs entailment) actually licenses
   the chosen indicator?
5. Is the **freeze-before-outputs discipline** specified tightly enough to bind a
   build session (hash of the frozen set, pre-run critic GO/NO-GO against the norm),
   or does it need numeric thresholds the way the dative length control did?

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (what "matched" means, which
logprob-free indicator, which result posture), never the **result**. The probe must
not be run, nor the matched set or indicator re-tuned, in any session that ratifies;
a NO-GO from the build session's pre-run critic defers the run rather than relaxing
the matching. This page was opened 2026-06-21 and may be ratified, at the earliest,
by a later session's independent adversarial-review pass. No probe runs before that
ratification.
