# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 88 ran on UTC-day **2026-06-23** and spent **$0.59880**
(calib $0.00518 + the K=5 repeated-runs resolver $0.59362). With session 87 ($0.12128), the UTC-day
2026-06-23 total is **$0.720 of $5**. Full ledger in [`config/budget.md`](config/budget.md). **Check the
clock (`date -u`)** — a later session may be a new UTC day (full $5 resets). Check for any newer Tom
override before spending.

## State

**Session 88 (JST 2026-06-23 / UTC 2026-06-23) — MIXED workflow, 2 waves, $0.599 spent.** Branch was even
with `main` at start (session 87 merged as #135; no PR to land). Two waves landed:

- **Wave 1 (philosophical):** NEW
  [`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md)
  — takes the within-lexical SURVIVAL result's **load-bearing caveat 1** and forks the surviving lexical
  commit into **(A) layer-specialness** vs **(B) always-resolvability**; shows the SURVIVAL design can't
  separate them (a balanced homonym is *both* lexical *and* resolvable); names the discriminating test — a
  **genuinely-unresolvable lexical item** (a forced-both pun/zeugma, the lexical analogue of the relational
  same-round dual binding), with the asymmetric prediction commit-under-(A)/decline-under-(B); held at R1,
  deflationary (B) holds the burden. + NEW
  [`source/falkum-vicente-2015-polysemy`](wiki/base/sources/falkum-vicente-2015-polysemy.md) (green-OA
  *Lingua* editorial) discharging the **regular/systematic (Apresjan) polysemy** want flagged by
  `ambiguity-kind-not-level` + `sennet-2021-ambiguity-sep`. Coherence pass clean (0 BLOCKERs; 3 SHOULD-FIX
  applied).
- **Wave 2 (empirical):** the cheap **K=5 byte-identical repeated-runs resolver** of the s82/82b decline
  disagreement →
  [`result/lexical-bridging-context-forced-decomposition-repeated-runs-v1`](wiki/findings/results/lexical-bridging-context-forced-decomposition-repeated-runs-v1.md):
  **de-noised NULL/CHANNEL-CONTROLLED (s82b vindicated).** gpt's bridging decline is at the jitter floor
  (per-run 1–2/24; majority-vote **1/24**) and **not** elevated over clear-same (majority-vote **3/29**); no
  robust confidence crack (bridging−clear-same diff CI **[−4.64,+1.68] ∋ 0**). The s82 MIXED/WEAK 2/24 was a
  high jitter draw; gpt's ungraded-commitment null is channel-controlled too, **like gemini's**. Disclosed
  cross-session shift (clear-same decline 3.4 %→10.3 %) — a lower-bound datum for
  [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md). 880 calls,
  $0.59362, 0 missing, 440/440 + 440/440 parsed. Independent pre-run critic GO + post-run verifier
  REPRODUCED. Parent forced-decomp result's discrepancy box now carries a RESOLVED note.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no decision owed ratification**
next session. Apply any Tom override first as always.

**Track lean — recent: 85 PHIL · 86 gov+phil · 87 EMPIRICAL · 88 MIXED (phil essay+source + empirical
resolver). Balanced → next can lean either; a runnable empirical unit is welcome if one exists.**

1. **GOVERNANCE/PHILOSOPHICAL (natural next) — OPEN the forced-both / genuinely-unresolvable-lexical-item
   operationalization decision.**
   [`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md)
   names the one probe that separates **layer-specialness (A)** from **always-resolvability (B)**: a lexical
   item where **both senses are required at once** (a pun/zeugma), scored by a **forced-single-application**
   instrument on which "it means both" is **not** a dodge. Building/running it needs a ratified
   operationalization — what certifies "forced-both" vs a *leaning* homonym (leans suppress UNCLEAR → spurious
   commit), how to score "both," the instrument, and the anchor posture (`internal-contrast-only` unless a
   resource certifies co-activation). Surface it as a `wiki/decisions/open/` page with options + a provisional
   default (the essay's certification-difficulty section sketches the shape). Ratifiable a *later* session;
   **NOT runnable until ratified.**
2. **MAINTENANCE (cheap) — fold the de-noised gpt leg into
   [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md).**
   The repeated-runs resolver de-noised gpt's leg from "weak softening (MIXED/WEAK)" to "channel-controlled
   null, like gemini"; **claude is now the lone CI-strict (confidence) crack**. Update the claim page to the
   sharpened three-model picture (gemini + de-noised gpt channel-controlled; claude's confidence crack only).
3. **EMPIRICAL (reserve) — Option A cross-level matched-kind.** A *full* cross-level matched-kind statement
   (the matched-ambiguity-kind gate's Option A, held in reserve) needs a reachable **Q2-a homonym
   sense-anchor** (a separate cross-session anchor decision) — not buildable until such a resource is found +
   ratified. Don't open without checking reachability.
4. **PHILOSOPHICAL (source) — the Cruse/Murphy/Lyons lexical-semantics monographs remain wanted** (likely
   not OA; the regular-polysemy want was discharged this session). Check reachability before committing time.
5. **RELATIONAL (dormant axis)** —
   [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes.
6. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (The matched-ambiguity-kind gate was ratified s86 and its probe
  ran s87 → SURVIVAL 3/3; the s82/82b forced-decomposition channel-check disagreement was resolved
  empirically this session → de-noised NULL/channel-controlled.)

## Standing-override notes (for Tom, if he looks)

- Session 88 spent **$0.59880** (calib $0.00518 + the K=5 resolver $0.59362). UTC-day 2026-06-23 total
  (s87 + s88) ≈ **$0.72 of $5**.
- Plain-language: the project (1) turned last session's surprise into a **sharper question** — is the
  word-sense layer genuinely *special*, or do forked words just always leave *some* meaning to pick? — and
  named the one experiment that could settle it (a word that means two things at once, like a pun); and (2)
  **settled an old disagreement** by running the same word test five times and averaging: a small "2-of-24"
  difference was just run-to-run randomness, so the models commit cleanly on the in-between words (no real
  hedging). Two independent reviewers; about 60 cents.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → balanced; next can lean either.** Top backlog = OPEN the forced-both operationalization
decision (the new essay's named discriminating test) / fold the de-noised gpt leg into the lexical claim /
dormant relational.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first**
> (`git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** SUBTLEX-US, DWUG (CC BY-ND), and WiC (CC BY-NC) are all gitignored. The K=5
> resolver re-runs the frozen forced-decomposition instrument (sha `dceafa9d…`), which needs DWUG + WiC staged
> via the v1 `prep.py` + `map_wic_fulltext.py` (both **reachable**: DWUG Zenodo 14028531 ~16 MB sha `64eef477…`;
> WiC pilehvar.github.io sha `f1a2fb67…`; both match pins). Use `map_wic_fulltext.py` (NOT `prep_wic.py`, which
> re-selects and overwrites the frozen manifest). Committed raw is sanitized (labels/counts only, no corpus text/CoT).
