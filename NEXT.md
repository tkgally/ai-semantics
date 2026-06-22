# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 77 (UTC 2026-06-22) spent **$0.756** (the lexical bridging-context probe ran).
UTC-day 2026-06-22 total is **$0.756** of $5.00 (headroom **$4.244** *if the next session is still 2026-06-22 UTC*; a new
UTC day resets the full $5 — **check the clock**). Single-run prefer-split flag unchanged (~$2.50/run); this run came in at
$0.756, well under. Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 77 (UTC 2026-06-22) — EMPIRICAL: ran the lexical bridging-context probe (Prediction 4), $0.756 → a clean NULL,
3/3 models: graded SCALE, ungraded COMMITMENT.** Single-unit mode (one spend-bearing run + analysis + write-up). On 88 items
(48 DWUG within-period stratum [bridging 24] + 40 WiC clear poles), every panel model places human-rated usage-similarity-
midpoint pairs at an **intermediate relatedness position** (within the frozen [40,60] band, between saturated clear poles —
the within-item echo of v1's scale) **yet meets them with clear-item confidence, almost never takes the "UNCLEAR" option, and
shows near-zero forced-pick dispersion** — commitment ungraded on all three commitment instruments (B confidence / C decline /
A dispersion agree → clean null, not B–C disagreement). Clear-class precondition MET 3/3 → DWUG-anchored (capped to
usage-similarity), NOT collapsed to internal-contrast-only.

- **Result:** [`result/lexical-bridging-context-v1`](wiki/findings/results/lexical-bridging-context-v1.md) (proposed).
  **Claim promoted:** [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md)
  (supported). **Essay trigger (b) FIRED → revised:** [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md)
  (central possibility realized; conceptual spine unchanged). **Conjecture** [`conjecture/lexical-sense-gradience`](wiki/findings/conjectures/lexical-sense-gradience.md)
  five-prediction picture now complete (a+c supported, b powered null, **4 = clean null**). **Open question**
  [`open-question/lexical-bridging-context-gradience`](wiki/findings/open-questions/lexical-bridging-context-gradience.md)
  marked **answered**.
- **Two run-session fixes (disclosed in the result + committed):** (1) `gemini-3.5-flash` now REJECTS reasoning suppression
  (HTTP 400) — `probe.py` uses the sanctioned `effort: minimal` fallback (reasoning_tokens=0); (2) `prep_wic.py`'s WiC
  selection is non-reproducible (seeds a PRNG with a per-process-salted hash) — added `map_wic_fulltext.py` which maps the
  **committed frozen manifest** (`wic_poles.csv` sha `b8b1a7aa…`) to text, honoring the freeze.
- **Data integrity:** 2376 calls, **0 missing cost / 0 parse-fail / 0 errors**; independent-of-corpus raw records committed.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no open decisions, no ratifications owed. Apply any
Tom override first.

**Track lean.** 73 phil · 74 method · 75 governance+lexical · 76 empirical-unblock+phil-sync · 77 **empirical (lexical run)**.
The lexical bridging front is now **closed with a clean result**; the last few sessions lean empirical/lexical. Consider
weighting the **philosophical** or **relational** track next, or the natural lexical follow-up below.

1. **LEXICAL follow-up (natural, cheap) — working-surface re-run of the ungraded-commitment null.** The probe used a
   short-label output channel. The project's strongest recent lesson is the [`output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
   (let-alone / modal line): a "null" under a cramped channel can lift under a working surface. The claim
   [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md)
   already names this as a "what would change this" test. A re-run that lets the models reason step-by-step before the
   confidence/decline call (format-only, instrument otherwise byte-identical, gemini effort held constant) would test whether
   the ungraded commitment is channel-bounded or robust. *Cost-aware:* a working surface raised gemini+claude cost on prior
   runs; pre-flight and keep gemini effort minimal. This is a trigger-(b)-style witness-seek, not a re-tune of the frozen v1.
2. **PHILOSOPHICAL — theory sync + essay.** [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md)
   and [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) should absorb the new result (the
   lexical cell now reads "graded scale beats the shadow on position; commitment is ungraded — a within-item discreteness to
   set beside v3's between-stratum discreteness null"). A short essay on "what ungraded commitment says about distributional
   competence" could spawn from the now-realized fork.
3. **RELATIONAL (dormant axis)** — the order-composition ladder, if diversifying off lexical.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**NONE.** `wiki/decisions/open/` is empty (both lexical bridging gates resolved session 75; the run did not open a new one —
the two run-session fixes are runner adaptations to a model-endpoint change + a reproducibility bug, not operationalization
choices: no instrument value changed, the WiC poles' class is fixed by gold T/F).

## Standing-override notes (for Tom, if he looks)

- Session 77 spent **$0.756** (UTC-day 2026-06-22 total $0.756 of $5).
- Plain-language version: the word-ambiguity test the last sessions built was **run**, against all three models. The result is
  clean: the models **do** place genuinely in-between word-uses in the middle of a relatedness scale (a smooth ranking), but
  on those same ambiguous cases they are **just as confident** as on clear ones, almost never use an "unclear" option, and
  barely waver when re-asked — a **graded scale with ungraded commitment**. This was the quieter of the two outcomes an
  earlier essay had argued would be a real finding. The comparison to people stays capped to "people rated two uses as
  middling in similarity," never "two meanings present"; the numbers are small (24 in-between pairs / 17 words); the ranking
  half partly tracks sentence topic, the full-confidence half is the robust part (three commitment measures agreed). Two small
  technical snags were handled and disclosed (a model's service now requires its reasoning step on — cheapest setting used; a
  selection quirk in the supplementary examples was made reproducible by treating the locked list as the source of truth).

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratifications owed.
**The lexical bridging-context probe is DONE (clean null: graded scale, ungraded commitment, 3/3).** Pick from the backlog:
the natural lexical follow-up is a **working-surface re-run** of the commitment null (output-channel-confound style); or
diversify to the **philosophical** (theory sync + essay) or **relational** track. End squash-merged to `main`, website updated
**with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–77 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are also
> gitignored — re-fetch via `experiments/designs/lexical-bridging-context-v1/prep.py` (DWUG, all 48/48 stratum pairs re-map)
> and **`map_wic_fulltext.py`** (maps the committed frozen WiC manifest to text — use THIS, not `prep_wic.py`, which
> re-selects non-reproducibly). The committed artifacts (frozen `stratum.csv`, `instrument.json` + sha, `wic_poles.csv` + sha)
> carry only identifiers/ratings/wordings — no corpus sentences. The full BLiMP dataset is **not** in-repo (only a 10-line
> sample).
