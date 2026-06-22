# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 82 (PR #128) spent **$0.25059**; a **concurrent duplicate session 82b (PR #129,
disclosed below)** independently ran the same unit and spent **$0.27404** of REAL OpenRouter money on the same UTC day.
**Corrected UTC-day 2026-06-22 total ≈ $4.11** (77 $0.756 + 79 ≈$2.83 + 82 $0.251 + 82b $0.274) of $5.00, leaving ≈$0.89.
**If the next session is a new UTC day (2026-06-23+), the full $5 resets — check the clock** (`date -u`). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

> **⚠ Concurrent-session collision (disclosed).** Two routine sessions were launched for the same slot and ran the gpt
> forced-decomposition unit in parallel; **#128 (session 82) merged first** (verdict MIXED/WEAK, decline 8.3%=2/24); **#128b
> (session 82b) lost the race** but reached the **opposite** verdict (PARTIAL/channel-CONTROLLED, decline 0.0%=0/24) with a
> *different* scaffold. The whole gap is ~2 of 24 items — at/under the documented ~12% temp-0 jitter → **the gpt-leg verdict is
> fragile and not robust.** 82b's wiki/website duplicates were discarded; its spend + the discrepancy are preserved in the
> budget ledger, the result page's reconciliation note, and `experiments/designs/lexical-bridging-context-forced-decomposition-v1/concurrent-run-82b/`.

## State

**Session 82 (UTC 2026-06-22) — EMPIRICAL + GOVERNANCE (workflow mode: reconcile/ratify + a spend-bearing empirical unit + an
independent pre-run critic and post-run verifier).** Two landed pieces:

- **RATIFIED the cross-level shared-instrument gate** [`decisions/resolved/cross-level-shared-instrument-operationalization`](wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md)
  (opened 80, reviewed-and-strengthened 81, **ratified 82**). A **fresh independent adversarial-review agent** returned **ADOPT
  DEFAULT** — Option A (graded "unsure/both/unclear" + 0–100 confidence, applied identically across the lexical/constructional/
  relational legs) with the four binding conditions **C1–C4** load-bearing (it verified C1's and C4's factual basis verbatim
  against both lexical result pages; anti-cheat PASS — every condition makes a spurious positive harder; no probe ran in the
  ratifying session). Moved open→resolved; promoted the contingent
  [`conjecture/cross-level-gradience-aggregate-not-moment`](wiki/findings/conjectures/cross-level-gradience-aggregate-not-moment.md)
  **`proposed → designed`** (`contingent-on` cleared). **No decisions are now open.**
- **RAN the gpt forced-decomposition lexical-channel follow-up** (ungated; under the resolved lexical gates, **no new decision
  owed** per the Scivetti forced-decomp precedent) →
  [`result/lexical-bridging-context-forced-decomposition-v1`](wiki/findings/results/lexical-bridging-context-forced-decomposition-v1.md).
  Forcing a mandatory 3-step decomposition **induced uptake decisively** (gpt median ~10→~110 completion tokens; 85–99%→**0%
  bare**; 100% worked), completing the three-model channel check. With the channel genuinely exercised: gpt's **graded SCALE
  replicates** (position CI-strict between, in [40,60]) but its ungraded **COMMITMENT is MIXED/WEAK** (confidence pointwise-softer
  *not* CI-strict; categorical decline 8.3%=2/24 weakly elevated amid a general rise) — **not** gemini's clean channel-controlled
  null, **not** a clean positive, **not** "gpt has graded commitment" (non-robust, under a structured scaffold that conflates
  uptake with structure). Independent **pre-run critic GO** (6 binding disclosure/process conditions, all honored) + independent
  **post-run verifier REPRODUCED** every number. Sharpens [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md)
  (graded-scale channel-robust; ungraded-commitment **model-specific & uptake-sensitive**: gemini clean, claude + gpt weak
  softening on *different* instruments).
- senselint 0 errors; linkify clean; index + budget + website updated (JST stamp).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is open, so **no ratification is owed** next
session (unless this/a later session opens one). Apply any Tom override first.

**Track lean — recent: 79 emp · 80 phil · 81 phil/review · 82 emp.** Roughly balanced; the marquee next unit (cross-level probe)
is empirical and large, so a **philosophical balance unit** alongside it is healthy if the budget/time allow.

1. **EMPIRICAL (marquee, spend-bearing) — BUILD the shared-instrument cross-level probe** now that its gate is **resolved**
   ([`decisions/resolved/cross-level-shared-instrument-operationalization`](wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md)).
   This is the natural next empirical unit (it could **not** run in session 82 — the ratifying session). Build + **freeze
   (sha256, C2)** the single Option-A commitment instrument (graded "unsure/both/unclear" + 0–100 confidence) applied
   **identically** at a lexical bridging item, a constructional ambiguous item, and a relational mid-record item, with: the
   per-level "aggregate"/"moment" operational definitions frozen (C2; relational aggregate disclosed as the weaker
   within-record notion, Q3); **categorical decline load-bearing for the moment pole, not confidence** (C1); per-level
   **clear-class precondition → NO-GO** (C3); a **confidence-shift-without-decline-shift = self-report effect** guard (C4).
   Anchor: **internal-contrast-only at the weakest common strength** (lexical leg capped to usage-similarity; constructional +
   relational `internal-contrast-only`) — invent no anchor (Q4). Then **fresh pre-run critic GO/NO-GO → run**; a NO-GO defers,
   never relaxes a band. **Pre-flight the cost** (three-level probe is larger than the 352-call lexical run; reuse the staged
   DWUG/WiC full-text + add constructional + relational items). If a per-leg anchor or an uncovered operationalization choice
   surfaces during the build, **open a new `wiki/decisions/open/` entry** rather than deciding it in-session.
2. **EMPIRICAL (small, cheap, HIGH-VALUE — resolve the 82/82b verdict discrepancy) — a BYTE-IDENTICAL REPEATED-RUNS (K≥5) test
   of gpt's forced-decomposition leg.** Sessions 82 and 82b disagreed on the gpt verdict (MIXED/WEAK vs channel-CONTROLLED) by
   ~2 of 24 decline items — at/under the documented ~12% temp-0 jitter. The clean resolver is exactly the session-64 move: re-run
   **one frozen instrument K≥5 times** at temp 0 over the same 88 items and read the **de-noised majority-vote / range** on the
   decline axis (`essay/point-estimate-is-a-draw` trigger (a)). Pick #128's frozen instrument (`dceafa9d…`) as the canonical one,
   freeze it, fresh pre-run critic, run K×88×(1–4 framings). Cheap (~$0.25–1.25 depending on K and framings). This turns a
   fragile single-run verdict into a measured one and is the **honest closure** of the channel check. *(A separate FREE-FORM
   MIN-LENGTH uptake-forcer — no step structure, to isolate uptake from scaffold structure — remains a distinct, lower-priority
   residual; the structured 3-step scaffold conflates uptake with structure per the Scivetti Limits.)*
3. **PHILOSOPHICAL (the balance unit; low priority but track-balancing) — finish discharging convergence-ladder essay trigger
   (e).** Only [`source/hitchcock-redei-2020-reichenbach-cc`](wiki/base/sources/hitchcock-redei-2020-reichenbach-cc.md)
   (SEP-Reichenbach) is ingested; the robustness/triangulation/consilience literature proper (Wimsatt, Weisberg, or a reachable
   PhilSci-Archive item — Keyser 2016 was unreachable) remains un-ingested. A second open-access source moves trigger (e) from
   *partial* to fuller discharge. **Open-access only** (charter §12.4); verbatim quotes; route around honestly if unreachable.
   *No spend.*
4. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes (any real probe needs a human anchor flagged `pending` or an
   `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **None.** `wiki/decisions/open/` is empty. The cross-level shared-instrument gate (opened 80) was **resolved session 82**
  (ADOPT DEFAULT). Thirty-five decisions ratified to date ([`decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- Session 82 spent **$0.25** (UTC-day 2026-06-22 total ≈$3.84 of $5).
- Plain-language version: this session did two things. (1) An independent reviewer **approved** the fair-test design proposed two
  sessions ago for the "one trait or three coincidences?" question — fixing the measuring stick (the same question asked
  identically at three layers of meaning, locked before any data, with four safeguards), which clears the way to build that
  experiment later; approving a measuring stick never decides the result. (2) A small experiment forced a model that had been
  giving one-word answers on the word-ambiguity task to actually reason through each case; once it did, its "graded scale but
  firmly committed" pattern held on the scale and its commitment softened only weakly — completing a three-model check (one model
  firm, two softening slightly, on different measures). Every number was independently re-derived and checked.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed (unless one is opened).
**Track lean → balanced (82 was empirical).** The marquee next unit is the **shared-instrument cross-level probe build** (its gate
is now resolved; it could not run in the ratifying session); pair it with the philosophical trigger-(e) discharge for balance, or
do the cheap free-form-min-length uptake-forcer residual. End squash-merged to `main`, website updated **with the JST clock-time
stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–82 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`** (maps the
> committed frozen WiC manifest to text). The lexical **working-surface** and **forced-decomposition** probes reuse those same
> gitignored full-text files; their committed `raw/` is **sanitized** (`sanitize_raw.py` strips the chain-of-thought, which can
> quote the licensed corpus — run it before committing any working-surface/forced-decomposition raw). The full BLiMP dataset is
> **not** in-repo (only a sample).
