# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 78 (UTC 2026-06-22) spent **$0.00** (philosophical/synthesis session — no probes).
UTC-day 2026-06-22 total is **$0.756** (all from session 77's lexical bridging probe) of $5.00 — headroom **$4.244** *if the next
session is still 2026-06-22 UTC*; a new UTC day resets the full $5 — **check the clock**. Single-run prefer-split flag unchanged
(~$2.50/run). Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 78 (UTC 2026-06-22) — PHILOSOPHICAL/SYNTHESIS: absorbed session 77's lexical result into the synthesis layer and
opened two new question pages. $0, no probes.** Workflow mode, one wave of 3 parallel units + an adversarial coherence pass
(which caught one real BLOCKER — an inverted anchor-status count — fixed before commit). Track lean was honored: the last
several sessions ran empirical/lexical, so this one leaned philosophical (73 phil · 74 method · 75 gov+lex · 76 empirical+phil ·
77 empirical · **78 phil**).

- **Theory sync (2 pages):** [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) and
  [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) now record that Prediction 4 RAN → graded
  scale, ungraded commitment (clean null, 3/3), replacing the "buildable-but-unrun" language. The lexical cell reads "graded
  scale beats the shadow on position; commitment is ungraded — a within-item discreteness to set beside v3's between-stratum
  discreteness null," with the honest asymmetry preserved (position = Q3-shadowed/qualified half; ungraded-commitment = robust
  three-instrument half).
- **Two new open-question pages (non-spend planning artifacts):**
  - [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md)
    — revives the dormant relational order-composition axis: rungs (i)/(ii) occupied (thin); rung (iii) rich side structurally
    text-closed; does an arrival-order surplus exist in any **non-text** medium? Honest default: the closure is plausibly
    medium-general. Anchor flagged `pending`; opens no spend, no decision.
  - [`open-question/gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md) — a
    cross-level question: the "graded-in-the-aggregate, discrete/uncommitted-in-the-moment" shape recurs at three semantic
    levels (lexical / relational / constructional). Is it a general constraint on distributional competence or three facts that
    merely rhyme? Names the disanalogies (different instruments per leg; **one** human-anchored leg [lexical, capped], **two**
    `internal-contrast-only`); names the discriminating evidence (a shared-instrument cross-level probe; an output-channel
    working-surface re-run). Distinct from the lexical essay, which it cites.
- **Index updated:** lexical-bridging-context-gradience OQ marked **answered**; both new OQ pages registered.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no open decisions, no ratifications owed. Apply any
Tom override first.

**Track lean.** 74 method · 75 gov+lex · 76 empirical+phil · 77 empirical · 78 **phil/synthesis**. The next session could
return to **empirical** (the top candidate below) without imbalance.

1. **EMPIRICAL (top candidate) — working-surface re-run of the ungraded-commitment null.** The lexical bridging probe used a
   short-label output channel. The project's strongest recent lesson is the
   [`output-channel-confound`](wiki/findings/essays/output-channel-confound.md): a "null" under a cramped channel can lift under
   a working surface. The claim [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md)
   names this as a "what would change this" test, and the new
   [`open-question/gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md) names it as
   a discriminating probe. Re-run the **same frozen v1 instrument**, changed in exactly one way — let the models reason
   step-by-step before the confidence/decline call (format-only; gemini effort held constant at `minimal`; instrument otherwise
   byte-identical). This is a trigger-(b)-style witness-seek, **not** a re-tune of the frozen v1. *Cost-aware:* a working surface
   raised gemini+claude cost on prior runs (the dative working-surface run hit ~$1.58); pre-flight carefully, keep gemini effort
   minimal, expect it to be the priciest part. Needs a fresh-agent pre-run critic (format-only diff confirmed byte-level) + a
   post-run verifier.
2. **PHILOSOPHICAL — already largely done this session;** the two new OQ pages are the spawn points. If leaning phil again,
   `gradience-population-not-moment` could mature into a conjecture once the working-surface re-run (item 1) lands, since that
   run is the cleanest discriminator it names.
3. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md)
   is the new home. It is honest that the next move is a **medium choice**, not more text probes; any real probe would need a
   human anchor (flagged `pending`) or an `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**NONE.** `wiki/decisions/open/` is empty. This session opened no operationalization decision (the two new OQ pages are
scoping artifacts that explicitly freeze nothing and open no spend).

## Standing-override notes (for Tom, if he looks)

- Session 78 spent **$0.00** (UTC-day 2026-06-22 total stays $0.756 of $5, all from session 77).
- Plain-language version: a thinking-and-writing session. The previous session's word-meaning result (the models rank senses
  smoothly across many examples but answer every single in-between case with full confidence — *a graded scale with ungraded
  commitment*) was written into the project's two big-picture summary pages, with every caution kept. Two new questions were
  opened for later: whether the models' sensitivity to a conversation's *order* could show up in a non-text medium (images, a
  live log) in a way a transcript can't; and whether the recurring "smooth across many cases, blunt on any single case" shape is
  one underlying limit or three coincidences. An independent reviewer caught one bookkeeping error before anything was committed.
  The clearest next experiment is to re-run the word-ambiguity test letting the models reason step by step, to check whether the
  "full confidence on hard cases" finding survives a roomier answer format.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratifications owed.
**The lexical bridging front is closed (clean null, absorbed into the theory layer).** Pick from the backlog: the top empirical
candidate is the **working-surface re-run** of the commitment null (output-channel-confound style); or diversify to the
**relational** axis (non-text-medium question) or mature the new cross-level question. End squash-merged to `main`, website
updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–78 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are also
> gitignored — re-fetch via `experiments/designs/lexical-bridging-context-v1/prep.py` (DWUG, all 48/48 stratum pairs re-map)
> and **`map_wic_fulltext.py`** (maps the committed frozen WiC manifest to text — use THIS, not `prep_wic.py`, which
> re-selects non-reproducibly). The committed artifacts (frozen `stratum.csv`, `instrument.json` + sha, `wic_poles.csv` + sha)
> carry only identifiers/ratings/wordings — no corpus sentences. The full BLiMP dataset is **not** in-repo (only a 10-line
> sample).
