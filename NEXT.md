# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 71 (UTC 2026-06-21) spent **$0.280** (the modal-arm-widening probe).
UTC-day 2026-06-21 total is **$1.964 (s64) + $0.503 (s69) + $0 (s70) + $0.280 (s71) = $2.747 of $5.00**
(headroom **$2.253** *if the next session is still 2026-06-21 UTC*; a new UTC day resets to the full $5 — check
the clock). Single-run prefer-split flag unchanged (~$2.50/run). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 71 (UTC 2026-06-21) — dual-track, $0.280 — ran the modal-arm-widening probe; the will→would modal
null does NOT generalize.** One empirical headline (frozen+certified+pre-run-critic-GO'd probe, independent
post-run verifier REPRODUCED) + the philosophical re-examination it triggered (essay revised, theory updated).
One wave, fresh-agent adversarial coherence pass applied, squash-merged.

- **EMPIRICAL — [`result/function-word-modal-widening`](wiki/findings/results/function-word-modal-widening.md)
  (internal-contrast-only, $0.280):** widened the modal arm of run-v2 to fire essay revision trigger (a).
  Per-arm flip_fn (claude/gpt/gemini): **`must`→`might` (necessity→possibility) flips at CEILING 3/3**
  (1.0/1.0/1.0); **`shall`→`should` (deontic obligation→advisory) SPLITS the panel** (gemini 0.778 reads
  *should*≠*required*; claude/gpt 0.056 collapse *should*≈*required*); **`will`→`would` replicates the null**
  (0/0/0.15). Base-label agreement HIGH for every modal arm (shall 1.0/1.0/0.889), so the nulls and split are
  interpretable. **The modal null is future→conditional-specific, not a modal fact.** The instrument registers a
  modal swap in proportion to its truth-conditional "loudness" (loud category-mismatch > within-deontic-strength,
  partly model-dependent > subtle irrealis). **Caveats (both load-bearing):** must→might crosses
  deontic→epistemic flavor (the easy non-entailment — claude flips it to *contradiction* 20/20), so it is NOT
  clean within-scale necessity-vs-possibility evidence; the `shall` arm rests on **one** content pair
  (`buy`→`give`). Independent post-run verifier reproduced every cell to the digit.
- **PHILOSOPHICAL — [`essay/function-words-not-one-category`](wiki/findings/essays/function-words-not-one-category.md)
  revised (draft→revised):** trigger (a) FIRED in the "narrows" direction. The blanket "modal flavor is the kind
  of shift this instrument is insensitive to" gloss is **retracted** (kept visible); the deeper §"A calibrated
  reading" thesis ("the instrument's calibration co-determines the result") is **vindicated and sharpened**. The
  type-specificity thesis survives; its diagnosis changed. Also folded the modal result into
  [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is eligible for ratification
next session. Apply any Tom override first as always. (The result + essay revision created this session are
findings, not decisions; no ratification owed.)

**Track lean.** 64 emp · 65 dual · 66 emp · 67 emp · 68 emp-gov · 69 dual · 70 dual · 71 **dual** (emp probe +
essay revision + theory). Balanced; weight the next by real priorities, not forced symmetry.

1. **EMPIRICAL — the sharpest open lever (essay trigger c, needs spend ~$0.3–0.5 + careful build): a SECOND
   inferential instrument on the surviving `will`→`would` null.** The modal result leaves one decisive question:
   is the `will`→`would` null the *instrument's* insensitivity (3-way NLI specifically) or the *relation's*
   subtlety (future→conditional is genuinely inferentially inert here)? Re-run `will`→`would` (and ideally
   `shall`→`should`) under a DIFFERENT indicator — a graded paraphrase-preference forced-choice, or a
   continuation-preference — holding the stimuli's modal swap fixed. If the second instrument registers what NLI
   missed, the effect relocates from "the relation" to "the instrument" (vindicating §"A calibrated reading" in
   the strongest form); if it also nulls, the future→conditional inertness is instrument-independent. Pipeline to
   fork: `experiments/runs/2026-06-21-modal-arm-widening/` (reuse the frozen `will`/`shall` items; swap the
   instrument; fresh pre-run critic; the NLI instrument is at `probe.py` `NLI_SYS`).
2. **EMPIRICAL — a CLEAN within-scale necessity↔possibility modal test (needs spend + harder build):** this
   session's `must`→`might` ceiling flip is confounded by the deontic→epistemic flavor cross. A clean test keeps
   both modals on the SAME scale — e.g. epistemic `must be`→`might be` (stative carriers, "is certainly" hypothesis)
   — to isolate whether models read necessity-vs-possibility *strength* as inferential. NB session 71 deferred the
   stative-epistemic design because concrete-noun content at the modal frequency is supply-thin (see the modal-arm
   README); budget the matched-construction build as the bulk of a session.
3. **EMPIRICAL (lower priority, still open from session 70): the few→many quantifier-scope mechanism one level
   deeper.** A dedicated quantifier-scope probe (`some`/`many`/`most`/`all` × scalar upper-bounding) could pin
   *why* the models diverge — and session 71 added a data point (claude AND gemini upper-bound *some*→all as
   contradiction; gemini did NOT upper-bound *many* in s70, so upper-bounding is scalar-specific). Addresses essay
   trigger (b).
4. **OPTIONAL Posture-2 upgrade (never blocks a run; network confirmed available this session):** fetch +
   license-check + catalogue **BLiMP** and/or an **NLI** human-annotated set → a typed `resource` page, so the
   modal/quantifier results could make a calibrated human comparison (e.g. *which* reading of *should* or *many*
   humans favor — the modal result explicitly leaves this open). Neither is in-repo. The function-word probes are
   `internal-contrast-only`; this would be a genuine human anchor.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- Session 71 spent **$0.280** (UTC-day 2026-06-21 total $2.747 of $5).
- Plain-language version: a recent experiment found that swapping a small grammar word for a related one usually
  changes a model's logical verdict more than swapping an ordinary word — but one swap (a future verb for its
  conditional cousin) barely mattered, and an essay guessed the test was simply blind to that family of words.
  This session widened the test and found the guess was too sweeping: a different swap (roughly "has to" for
  "may") changed the verdict every time, and another ("required" for "ought to") split the models. So the
  earlier "no effect" was about one specific word, not the family. The public site says all of this plainly,
  with the honest caveats, and takes no side on which reading is "correct."

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing to ratify.
The most decisive next unit is the **second-instrument test of the `will`→`would` null** (backlog 1, essay
trigger c — is the null the instrument or the relation? ~$0.3–0.5, careful build, fresh pre-run critic). The
modal pipeline lives at `experiments/runs/2026-06-21-modal-arm-widening/`. End squash-merged to `main`, website
updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–71 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 `c5f86f06…` in the docstring; the fetch worked this
> session) before re-running `build.py`/`certify.py` (`freqlib.py` reads it). BLiMP/NLI (the optional Posture-2
> human backing) are **not** in-repo.
