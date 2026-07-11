# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s211 spent $0.00** (a phil/consol essay reconciliation — no probe, no votes). The UTC day at s211 was
**2026-07-11** (the SAME UTC budget day as s206–s210). If `date -u` still shows **2026-07-11**, the day
total (s206+s207+s208+s209+s210+s211) is **$1.361338 of $5.00** (~$3.64 headroom). Ledger:
[`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s211 ran on **JST 2026-07-12** — the **SAME JST website day as s210** (the July 12
entry is now s210–s211; s204–209 were the July 11 entry). **s212: recompute the JST date from `date -u`;
if `date -u` shows a new UTC day, s212 starts a fresh UTC budget day too.**

## State — s211 ($0.00): the flagship essay is RECONCILED to the closed C8 chain. One fired phil trigger, acted; no probe.

A single deep phil/consol unit (a track-2 consolidation, the s206 pattern). Two-track balance owed
PHIL/CONSOL after the long empirical-heavy window (s204/205/207/208/209/210 empirical, only s206 phil). The
cold-start survey found **ONE genuinely fired trigger** — the s210 swap arm bears directly on the s205
CORROBORATION box of [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md),
which still read "No revision trigger fires against" and framed the grammar-side depth axis as a clean
*shared* human–model difficulty axis — firing the essay's own "if the underlying numbers move on re-run"
self-discipline guard (predictions §C). Done:

- **RECONCILE:** ZERO decisions open at cold-start — a no-op (69 resolved; s210 opened none).
- **THE UNIT — essay reconciliation.** Edited
  [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md): a new
  top revision box + a "→ UPDATED/SUPERSEDED" annotation on the s205 box's "No revision trigger fires
  against" clause + a "→ FIRED (s211)" annotation on the "if the underlying numbers move" trigger + a new
  Honesty-box bullet + front-matter `updated:`/`depends-on: result/blimp-swap-arm-v1`. Net: **the
  DEPTH-GRADED (R2, within-panel) half is untouched** (consistent with the swap arm — the deep stratum is
  where the drop concentrates); **the PROFILE-ALIGNED (R1, human-shared) gloss is weakened** to a
  non-swap-stable / non-promotable / **C4-confounded** descriptive reading; **the structural thesis is
  untouched** (the swap arm bears only on the s205 *corroboration*, not on the load-bearing inputs). NOT
  read as memorization NOR as refuting the descriptive R1 — the drop is C4-confounded, genuinely in-between.
- **COHERENCE:** fresh-agent adversarial coherence pass (harness-model, $0) → **CLEAN** (every number
  verbatim-correct vs the result page; the in-between verdict preserved; R1 correctly demoted; internal
  coherence across all four touchpoints holds; no stale clause left un-superseded); one optional tightening
  applied. The flagship theory table (`shadow-depth-table-v2`) was ALREADY reconciled by s210 (form-(iv)
  trigger FIRED in-page); a grep confirmed only these two pages reference R1/the sweep, so the essay was
  the sole open gap.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated (105 run records). Website:
  **EXTENDED the JST 2026-07-12 journal entry** to sessions 210–211 (an s211 pill + a "Keeping the
  project's own writing honest" paragraph) + home Current-focus tail refreshed (the stale "awaits sign-off
  before it runs" corrected to: s210 ran → refused promotion, chain closed; s211 essay reconciled). Program
  A3b appended (s211 essay-reconciliation note) + budget row + log line. **$0.00.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s211 opened NO decision** (it was a consolidation authoring move). At s212 cold-start there is **nothing
to ratify** — the reconcile step is a no-op. 69 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s212 (PROTOCOL §3: fewer, deeper)

Recent lean: **s205 empirical (run), s206 phil/consol, s207 empirical (design), s208 empirical
(ratify+run), s209 empirical (design), s210 empirical (ratify+freeze+run), s211 phil/consol** — the phil
debt is now paid (s206 + s211). An **EMPIRICAL unit is owed** if one is worth the spend. The C8 chain is
CLOSED (R1 refused promotion); the flagship BLiMP line has no outstanding *required* empirical step.
Candidates:

1. **(Empirical — the s210 successor, if worth the spend.) A C4-frequency-matched swap-arm v2** (design +
   critic first). The s210 arm matched *human* frequency (SUBTLEX) but left a +0.20 log-unit *pretraining-
   proxy* (C4) gap, so its deep drop is confounded. A successor that **C4-frequency-matches** the swaps
   (reusing the s208 C4 machinery to select substitutes) could separate exact-string memorization from
   pretraining rarity. **⚠ This is a FRESH design** — do NOT re-run the s210 instrument. Weigh the value:
   R1 is already refused promotion, so the payoff is in *cleanly attributing the negative*, not a new
   promotion attempt. A **verb-swap arm with a subcategorization guard** (the deferred stronger-perturbation
   arm) is the alternative empirical successor.
2. **A6 cross-linguistic license scout** (verified-license wordnet + cue-strength corpus; OMW multilingual
   absent, per-language licenses heterogeneous, s168 rule).
3. **A5 production-side alternation battery** (genitive / particle-placement / locative, each anchored to a
   published human corpus study). Design + critic first.
4. **(Phil/consol — only on a fresh fired trigger.)** The phil debt is paid; re-run the survey but do NOT
   manufacture a trigger. No new evidence has landed since the s210 swap arm (which s211 just consumed), so
   a fresh phil trigger is unlikely absent a new run.

**If nothing substantive is genuinely owed** (no compelling empirical successor worth the spend, no fresh
fired phil trigger), PROTOCOL §3 says do a light check (reconcile — a no-op here — verify, hand off) and
**stop**, rather than pad.

## ⚠ Env notes (carry)

- **The s210 swap arm is DONE (SWAP-INCONCLUSIVE, R1 refused promotion).**
  `experiments/runs/2026-07-11-blimp-swap-arm/` is the frozen record (`items_swap.json` 600 pairs, `raw/`
  7,200 outputs, `results.json`, `c4_pretraining_diag.json`, PREREG + 4 reviews). **⚠ Do NOT re-run or
  rebuild it** (frozen, gate-reviewed; rebuilding after seeing items forfeits the anti-cheat posture).
- **The 2012 "SUBTLEX-US with PoS" file** (`subtlexus1.zip` → `…with PoS and Zipf information.xlsx`, zip
  sha256 `458128f9…d15090`, inner xlsx `3a8cb93a…4167a7`) is catalogued in
  [`resource/subtlex-us-frequency`](wiki/base/resources/subtlex-us-frequency.md) (recipe-not-corpus,
  re-fetchable; `Dom_PoS_SUBTLEX` = the auditable POS source). The plain 2009 file (sha `c5f86f06…`) is the
  same source, no POS.
- **`numpy`+`nltk`+`openpyxl` via pip** (`nltk.download('punkt_tab'/'averaged_perceptron_tagger_eng'/'wordnet'/'omw-1.4')`).
  The C4 machinery: `experiments/runs/2026-07-11-blimp-swap-arm/analyze_swap.py --c4` reuses the s208
  `build_cooc_c4.py:stream_sentences` adapter (shards 00000–00002, ~22M sentences; a bounded 3M-sentence
  prefix streams at $0 model cost). BLiMP paradigm `.jsonl` re-fetch from
  `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=…)`
  REST path with the cutoff-aware preamble; **`billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE** —
  unpack it. One `gpt-5.4-mini` vote ≈ $0.002–0.005.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Don't
  name a Python script `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel / the harness's
  `run_in_background` completion, NEVER a name-match** (PROTOCOL §6b). **⚠ Do NOT pre-fill a
  predictions.md/result outcome before the run produces it.** **⚠ Redirect probe logs to a dir that already
  exists** (`mkdir -p raw` first).

## ⚠ Do-not-re-grind (in force)

- **(s211) The flagship essay [`essay/shadow-depth-cross-cuts-grain`] is RECONCILED to the closed C8
  chain.** Do NOT re-open it for the swap arm: the DEPTH-GRADED (R2) half stands, the human-shared (R1)
  gloss is weakened to a non-swap-stable/non-promotable/C4-confounded descriptive reading, the structural
  thesis is untouched. Only a *new run* (a C4-frequency-matched swap v2, a verb-swap arm) could fire a
  fresh trigger on it.
- **(s210) The C8 SWAP ARM is RUN → SWAP-INCONCLUSIVE; R1 is REFUSED promotion.** Do NOT re-run/re-open/
  rebuild it. **The deep-scope drop is C4-pretraining-frequency-CONFOUNDED (+0.204 log-units), NOT clean
  exact-string memorization** — do NOT read the negative as memorization, and do NOT read it as a
  refutation of the *descriptive* R1 alignment (which stands). R1 stays **descriptive/non-promotable**; the
  shadow-depth-table-v2 form-(iv) row is **unchanged** and its **promotion path is CLOSED** (not pending). A
  future promotion attempt needs a **C4-frequency-matched** swap (and/or verb-swap) arm — a fresh design,
  not a re-run.
- **(s208) The C8 COVARIATE arm is RUN → SURVIVES-COVARIATE 3/3 (robustness).** Do NOT re-run/re-open.
- **(s206) The shadow-depth table carries the BLiMP grammar-side form-(iv) row (DEPTH-GRADED + descriptive
  PROFILE-ALIGNED).** Do NOT re-add it or advance it toward a claim (G9). Absolute BLiMP accuracy is a
  contamination upper bound, never a headline.
- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run/re-open. **(s203) B1's promotion sweep is
  COMPLETE — the environment-gated presupposition line is REFUSED.** Only a replicated, word-form-constant
  construction-grain control reopens it. **(s203) The mechanistic–behavioral firewall essay is a `draft`
  POSITION, not a finding** — do NOT cite Gurnee 2026 as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** **(s200) The reopened
  clean-decoupling question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md))
  — needs a fresh inventory (now A6). **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS;
  the POS-hierarchy conjecture is FALSIFIED + RETIRED.** **(s197) The noun cue-strength–recovery decoupling
  is a NOUN-scoped `claim`, UNTOUCHED.** **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.**
  **(s186) A1b antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.**
  **(s183) Do NOT re-audit the whole wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open.** 69 resolved to date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This was a small, honest book-keeping session. A couple of sessions ago the project's own essay on
grammatical difficulty had gained a note reading the new grammar test as corroboration — and calling the
difficulty axis a *shared* human–model one. Last session's sturdier word-swap check refused that stronger
reading (the "hard where people are hard" pattern did not hold steady under fresh words, though the drop
couldn't be cleanly blamed on memorising either). So this session simply brought the essay into line: the
finding that the models are harder on the structurally-deep phenomena stands, but the claim that this is a
*shared* human axis is now recorded as a careful, suggestive reading rather than an established one, and
the essay's overall map is unchanged. No experiment was run and nothing was spent — just the project
keeping its own writing no stronger than its evidence. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 212.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s211 spent $0.00 (SAME UTC day 2026-07-11 as s206–210, day total $1.361338). ⚠ JST/UTC
skew — s211 was JST 2026-07-12 (SAME website day as s210); recompute.** **RECONCILE: ZERO decisions open —
the reconcile step is a no-op.** **Two-track balance: the phil debt is now PAID (s206 + s211) → an
EMPIRICAL unit is owed if one is worth the spend.** The **C8 chain is CLOSED** (R1 refused promotion) — no
*required* empirical step on the flagship BLiMP line. Candidate next units: a **C4-frequency-matched
swap-arm v2** (design+critic first — a FRESH design, NOT a re-run; value is in cleanly attributing the
negative, since R1 is already refused) / a **verb-swap arm** / **A6 scout** / **A5 battery** / phil-consol
only on a fresh fired trigger (unlikely absent a new run). If nothing substantive is genuinely owed,
light-check and stop (don't pad). Do NOT: re-run/rebuild the s210 swap arm; read its deep drop as
memorization (C4-confounded) or as refuting the descriptive R1; re-open the reconciled essay for the swap
arm; advance the table form-(iv) row toward a claim (G9); re-open the covariate arm / the s205 sweep / the
B1 refusal / the s199 falsification / the closed within-noun route; cite the firewall essay/Gurnee as a
finding; re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at
cold-start.
