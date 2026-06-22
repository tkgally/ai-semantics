# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-22** total ≈ **$4.11** of $5.00 (77 $0.756 + 79 ≈$2.83 + 82
$0.251 + 82b $0.274; **session 83 spent $0** — build-only, no probe). Leaving ≈$0.89 on 2026-06-22.
**If the next session is a new UTC day (2026-06-23+), the full $5 resets — check the clock** (`date -u`). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 83 (UTC 2026-06-22) — EMPIRICAL build + PHILOSOPHICAL balance (workflow mode: 1 deep wave + adversarial
coherence pass; no spend, no probe run).** Branch was even with `main` at start (no PR to land). `wiki/decisions/open/`
was EMPTY — no ratification owed. Two landed pieces:

- **BUILT + FROZE the shared-instrument cross-level probe** under the resolved gate
  [`decisions/resolved/cross-level-shared-instrument-operationalization`](wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md)
  (ratified s82, ADOPT DEFAULT + C1–C4). New directory **`experiments/designs/cross-level-shared-instrument-v1/`**:
  one Option-A shared elicitation (graded **SAME/DIFFERENT/UNCLEAR + 0–100 confidence**) applied **identically** at a
  lexical bridging item, a constructional ambiguous item, and a relational mid-record item. `instrument.json` pins
  **C2 (i)–(iv)** (scale + `[40,60]` mid-band, verbatim per-level decline wording, per-level aggregate/moment defs with
  the relational aggregate labelled the weaker within-record notion, Q2 confirm/dissolve/weak thresholds) and is frozen
  at **sha256 `3cdfe17871a1669e690fe0f6c46ba66a5af594d48c7aa83e90538faf7a35e28f`**. `analyze.py` encodes **C1** (categorical
  decline load-bearing, not confidence), **C3** (clear-class precondition → NO-GO per level), **C4** (confidence-only shift
  = self-report guard), and the Q2 reading rule. Lexical items = sha-manifest of the frozen DWUG/WiC stratum (no corpus
  text); constructional + relational = 30 fresh synthetic items each (10 sets × ambiguous + 2 controls),
  `internal-contrast-only`. `probe.py` **refuses to run** without `--run --i-have-pre-run-critic-go`; `certify.py` **17/17
  PASS** (no API). **NOT RUN, no spend.** No new `wiki/decisions/open/` entry owed (reused the gate's already-fixed
  choices). Fresh-agent coherence pass: **no BLOCKERS**; 2 SHOULD-FIX + 1 NIT applied (probe.py lemma-carry so analyze
  clusters lexical by lemma — `instrument.json` unchanged, freeze intact; cx09 swapped to a clean gerund/participle set;
  "a anchor"/"a hourglass" fixed); re-certified 17/17.
- **MORE FULLY DISCHARGED** essay [`cross-level-convergence-ladder`](wiki/findings/essays/cross-level-convergence-ladder.md)
  **trigger (e)** by ingesting NEW [`source/heesen-bright-zucker-2019-triangulation`](wiki/base/sources/heesen-bright-zucker-2019-triangulation.md)
  (Heesen, Bright & Zucker 2019, *Synthese*, CC BY 4.0; **abstract-level provenance** — body PDFs image-based). Grounds the
  ladder's R1→R2 step from the **variety-of-evidence / triangulation** angle (a second external confirmation alongside
  Reichenbach screening-off); relocates the bar more permissively; ladder unchanged. Quotes verbatim, double-fetch-confirmed.
- senselint 0 errors; linkify clean; index + budget(=$0 row not added; day total note only) + website updated (JST 22:53 stamp). Merged **PR #130 → main `ce09c0f`**.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is open, so **no ratification is owed**
next session (unless this/a later session opens one). Apply any Tom override first.

**Track lean — recent: 80 phil · 81 phil-review · 82 empirical · 83 empirical-build + phil.** Balanced. The marquee next
unit is empirical (RUN the cross-level probe); pair with a philosophical unit only if budget/time allow.

1. **EMPIRICAL (marquee, spend-bearing) — RUN the now-built+frozen shared-instrument cross-level probe.** The instrument is
   built and frozen at `experiments/designs/cross-level-shared-instrument-v1/` (sha `3cdfe178…`, certify 17/17). To run:
   (a) **stage the gitignored lexical corpus** exactly as the lexical leg does (`experiments/designs/lexical-bridging-context-v1/prep.py`
   for DWUG, `map_wic_fulltext.py` for WiC — confirm the frozen-file shas in `items_lexical.json` still match); (b) a
   **fresh independent pre-run critic GO/NO-GO against the frozen `instrument.json`** (a NO-GO defers the run, never relaxes
   a band) — the critic should scrutinize the **comparability residual** (stimulus bodies unavoidably differ across the
   three levels; C3 is a guard not a proof — disclosed in the design doc §4 / README), whether the synthetic
   constructional/relational ambiguous items are genuinely two-reading and the controls genuinely one-reading, and the
   relational leg being the weakest (within-record) one (a ≥2-level confirm excluding it is only a 2-level R2 regularity);
   (c) **budget check** (pre-flight ≈$0.10–0.25 for the full 3-model run; tiny) + `--run --i-have-pre-run-critic-go`;
   (d) **post-run verifier**. C3 is checked on data: any level whose clear classes don't show high-confidence/low-decline
   collapses to weak/`internal-contrast-only` and contributes no moment verdict. **Anchor: internal-contrast-only at the
   weakest common strength** (lexical capped to usage-similarity). If an uncovered operationalization choice surfaces at
   run, **open a `wiki/decisions/open/` entry**, do not decide it in-session.
2. **EMPIRICAL (small, cheap, HIGH-VALUE — the 82/82b verdict resolver, still open) — BYTE-IDENTICAL REPEATED-RUNS (K≥5)
   test of gpt's forced-decomposition leg.** Sessions 82 and 82b disagreed on the gpt verdict (MIXED/WEAK vs
   channel-CONTROLLED) by ~2 of 24 decline items — at/under the documented ~12% temp-0 jitter. Re-run **one frozen
   instrument K≥5 times** at temp 0 over the same 88 items and read the **de-noised majority-vote / range** on the decline
   axis. Pick #128's frozen instrument (`dceafa9d…`) as canonical, freeze it, fresh pre-run critic, run K×88×(1–4 framings).
   Cheap (~$0.25–1.25 depending on K/framings). The honest closure of the channel check.
3. **PHILOSOPHICAL (balance unit; low priority) — convergence-ladder trigger (e) is now "more fully discharged"** with two
   open-access methodology sources (Reichenbach screening-off + Heesen et al. triangulation). The honest residual: still no
   *robustness-analysis-proper* / consilience formal derivation, and the triangulation source rests on abstract-level
   provenance (body PDFs image-based). A future fully-text-readable robustness source would close it further. *No spend.*
4. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes (any real probe needs a human anchor flagged `pending` or an
   `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **None.** `wiki/decisions/open/` is empty. Thirty-five decisions ratified to date
  ([`decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Session 83 opened none (the cross-level probe build
  reused the resolved gate's fixed choices throughout).

## Standing-override notes (for Tom, if he looks)

- Session 83 spent **$0** (build-only, no model queried; UTC-day 2026-06-22 total stays ≈$4.11 of $5).
- Plain-language version: this session **built and locked** the fair-test experiment whose design was approved last session
  — one single question, asked in identical wording at three layers of meaning (word senses, grammar patterns, conversation
  reference), with all its safeguards written into runnable form and sealed with a checksum so nothing can be quietly
  adjusted later. No models were queried; the test still needs an independent green light and a budget check before it can
  run (it should cost only cents). It also strengthened the project's reasoning standard with a second outside source on
  combining methods ("triangulation"), confirming the standard's logic from a new angle.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed (unless one is opened).
**Track lean → balanced (82+83 empirical-leaning).** The marquee next unit is the **RUN of the now-built+frozen cross-level
probe** (stage corpus → fresh pre-run critic GO → budget check → run → verify); or the cheap byte-identical K-run resolver
of the 82/82b gpt discrepancy. End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–83 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the lexical v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`**
> (maps the committed frozen WiC manifest to text). The **cross-level probe** (`cross-level-shared-instrument-v1`) reuses
> those same gitignored full-text files at run time via its `items_lexical.json` sha-manifest. The lexical working-surface
> and forced-decomposition probes' committed `raw/` is **sanitized** (`sanitize_raw.py` strips the chain-of-thought, which
> can quote the licensed corpus). The full BLiMP dataset is **not** in-repo (only a sample).
