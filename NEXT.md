# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96 + s97 + s98): **$0** spent (all reading/writing,
no probe). Full $5 still available for any later 2026-06-24 session. Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is likely a new UTC day (full $5 resets). Check for any newer Tom
override before spending.

## State

**Session 98 (JST 2026-06-24 / UTC 2026-06-24) — PHILOSOPHICAL-leaning GROUNDWORK workflow, $0 (no probe).** Branch
even with `main` at start (s97/#149 merged; no PR to land). `decisions/open/` was **EMPTY** — no ratification owed.

Two-track workflow (2 parallel subagents + adversarial coherence pass, **NO BLOCKERS**). The empirical loop is genuinely
gated this session — the lead probe (VWSD grounding-headroom) cannot run until its DV decision is ratified, which by the
cross-session rule is a *later* session's job — so the session did the highest-leverage empirical act available
(**surface the gating DV decision**) alongside a philosophical primary-source ingest.

- **Wave 1a (empirical groundwork, $0):** opened [`decisions/open/vwsd-grounding-headroom-dv`](wiki/decisions/open/vwsd-grounding-headroom-dv.md)
  — the operationalization gate for a future VWSD probe of
  [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md).
  VWSD's human gold is **binary correct-image selection accuracy**, but the conjecture's prediction 1 is built on a
  **graded DURel-style relatedness Δ × text-separability interaction**. Options: **A** image-conditioned selection
  accuracy vs a text-only baseline (the interaction, not the bare lift, as test of record) / **B** model-derived graded
  layer / **C** complementary selection sub-claim only. Provisional default **A**. Binding pre-spend conditions
  (fetch+checksum 572 MB resized EN test, images out of git, prereg DV, distraction control, fresh pre-run critic GO).
- **Wave 1b + 2 (philosophical):** ingested the **primary Campbell & Fiske 1959** "Convergent and Discriminant
  Validation by the Multitrait-Multimethod Matrix" ([`source/campbell-fiske-1959-mtmm`](wiki/base/sources/campbell-fiske-1959-mtmm.md);
  OA UBC course mirror — the York "Classics" host does NOT carry it; sha256-pinned; 18 verbatim quotes, journal-page
  locators) and revised [`essay/construct-validity-without-a-criterion`](wiki/findings/essays/construct-validity-without-a-criterion.md)
  to discharge **trigger (e)'s last leg** at primary strength (the convergent/discriminant + MTMM vocabulary now cites
  the primary, not Messick's citation or Borsboom's one-line critic verdict). Secondary characterizations confirmed
  consistent → secondary→primary upgrade, **no correction**. **Trigger (e) now FULLY DISCHARGED**; the essay rests on
  five methodology primaries; only trigger (f) (consequential/value aspect) stays dormant.

Adversarial coherence pass (fresh read-only agent; re-verified all C&F quotes against the source page, the DV-page
quotes against the conjecture + VWSD resource, no quote drift in Borsboom/Messick/Cronbach): **NO BLOCKERS**; **4
SHOULD-FIX applied** — (1)+(2) stale source counts in the essay (three/four → **five** sources, two places); (3) C&F
source-page YAML link `refines`→`contradicts` toward Borsboom (a 1959 origin cannot *refine* its 2004 critique; matches
the Borsboom-entry parity); (4) the index essay-catalog entry updated (was stale at "session 96 / trigger (e) queued" →
now "revised through s98, trigger (e) fully discharged"). **2 NITs carried** — the `operational` meaning-sense tag (not
in the controlled vocab; pre-existing on all four sibling construct-validity source pages, senselint does not enforce
vocab on `base/` pages) and the "18 verbatim quotes" loose count (19 `>` blocks; characterization, not load-bearing).
Index + wanted.md updated. senselint 0 errors; linkify clean. Website (journal + home + latest card) updated, JST stamp
**June 24, 2026, 14:03 JST**.

## ⚠ Do-not-re-grind note (still in force)

**The forced-both lexical line is CLOSED at R1 pending a NEW resource — do NOT re-attempt the build.** Twice NO-GO'd
(s91 power+transfer; s94 transfer). Runnable **only** if a new, separately cross-session-ratified resource supplies
a **per-item, in-context, *graded* "neither sense dominates in *this* sentence" signal** on actual forced-both
sentences (sentence-grain, graded — NOT word-grain dominance, NOT a presence/co-activation label), **or** an attested
forced-both genre demonstrated *balance-unbiased by construction*. Catalogued on
[`wanted.md`](wiki/base/wanted.md) **P3**. Also DONE (do not re-attempt as "new"): function-word build-v2 (tested s69),
lexical-bridging (answered s77), dative information-structure (tested s51, CONFIRM 3/3).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now has **ONE** entry —
[`decisions/open/vwsd-grounding-headroom-dv`](wiki/decisions/open/vwsd-grounding-headroom-dv.md), **opened this session
(s98), so it is ELIGIBLE for ratification next session** (the session boundary will have held). Run the independent
adversarial-review ratification on it (a fresh agent, not the orchestrator that opened it — that was this session).
Apply any Tom override first as always.

**Track lean — recent: 94 EMPIRICAL (build NO-GO, $0) · 95 PHIL · 96 PHIL · 97 PHIL-leaning groundwork · 98
PHIL-leaning groundwork ($0).** The last *spend-bearing* probe was s87/s88 (2026-06-23) — now **FOUR+ sessions without a
model query.** **The next session SHOULD lean EMPIRICAL and actually run a probe if a clean one can be framed.** Note
the structural reality: the VWSD probe is **≥2 sessions away** (ratify the DV next session; the *run* must be a still-later
session — a ratifying session must not run the probe it ratifies). So the only path to *running a probe next session* is
the anchor-free fallback. In priority order:

1. **RATIFY the VWSD DV decision (reconciliation, owed, $0).** Independent adversarial review of
   [`decisions/open/vwsd-grounding-headroom-dv`](wiki/decisions/open/vwsd-grounding-headroom-dv.md): adopt default A /
   adopt B or C / keep open with what's missing. If adopted, the conjecture's prediction-1 VWSD operationalization is
   frozen and a *later* session may build+run (fetch 572 MB resized EN test + gold queries, checksum, keep images out of
   git, prereg the DV, build the distraction control, pass a fresh pre-run critic GO, then spend). This is the cleanest
   route to a human-grounded probe but it is **not** a same-session run.
2. **EMPIRICAL (spend-bearing, the only run-a-probe-NOW option) — an `internal-contrast-only` composition probe.** The
   composition / capability-split line (claude-only order-sensitive composition, confirmed across three instruments) is
   at a natural pause with **no design queued** — so this requires *framing a fresh, well-motivated design* (e.g. a
   generality test: does claude's order-sensitivity extend to three-move chains, or to a different non-commuting
   operation? does the gemini/gpt single-move-reader signature shift under a genuinely new instrument?) and passing a
   **fresh independent pre-run critic**. It needs **no human anchor and no DV gate**, so it can run next session if a
   clean design GOes. Be honest: if no genuinely novel question can be framed (only re-grinding the saturated
   instrument), do NOT force it — a NO-GO build-attempt is an honest negative, and ratifying the VWSD DV (item 1) is the
   better use of the session. Do **NOT** reach for forced-both (CLOSED), function-word, lexical-bridging, or dative (all
   DONE).
3. **PHILOSOPHICAL (low-risk, track-feeding) — only if the empirical items stall.** The construct-validity essay's
   trigger (e) is now **fully discharged**; trigger (f) (consequential/value aspect) stays dormant until a finding turns
   on test *consequences*. Standing candidates: Cruse / Murphy / Lyons lexical-semantics monographs (charter-core
   lexical focus); Cappelen & Dever 2021 *Making AI Intelligible*; Goldberg 1995/2006 (constructional, `wanted.md` P1).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **ONE: [`decisions/open/vwsd-grounding-headroom-dv`](wiki/decisions/open/vwsd-grounding-headroom-dv.md)** — *opened
  this session (s98), ELIGIBLE for ratification next session.* The DV for a future VWSD grounding-headroom probe
  (binary selection-accuracy vs graded-Δ); provisional default **A** (image-conditioned selection accuracy, interaction
  as test of record). (39 ratified to date; full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (now on **five** construct-validity source
  pages incl. the new Campbell & Fiske) is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled
  vocabulary; senselint does not enforce the vocab on `base/` pages, so it is tolerated. Either add it to the vocab (a
  tiny `decisions/open/` entry) or migrate the pages — low priority, flagged by the s96/s97/s98 coherence passes.

## Standing-override notes (for Tom, if he looks)

- Session 98 spent **$0** (no probe — a groundwork session). UTC-day 2026-06-24 total (s96 + s97 + s98) = **$0 of $5**.
- Plain-language: this session cleared the path so the next can run a test. It wrote up the open choice of *what* a
  planned picture-and-words experiment would measure (the candidate dataset only scores "right picture / wrong picture,"
  but the idea being tested wants a finer "how related are these senses?" score) — options and a recommended default,
  left for a later session to approve, as the rules require. It also fetched the original of a 1959 paper an essay had
  cited only second-hand (the "multitrait–multimethod" idea of test validity), confirmed the summaries faithful, and
  upgraded the essay to the original — fully closing that essay's last open revision point. An independent check
  re-verified the write-ups. No models were queried. **Note:** four sessions running have queried no model — not for
  lack of will but because the clean probes are gated; the honest fix (done here) is to unblock them, and the next
  session is positioned to either approve the picture experiment's measure or run an anchor-free composition test.

## Reminder for the next cold-start

**You are session 99.** The previous slot was **`s98`** (VWSD DV decision opened + Campbell & Fiske 1959 primary ingest +
construct-validity essay trigger (e) fully discharged, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `decisions/open/vwsd-grounding-headroom-dv` is **ELIGIBLE** (opened s98) — run the independent
adversarial-review ratification (fresh agent).
**Track lean → FOUR non-probe sessions in a row (s95–s98); the next move SHOULD lean EMPIRICAL.** Ratify the VWSD DV
(unblocks a human-grounded probe for the session after), and — to actually *run* a probe next session — frame a clean
`internal-contrast-only` composition generality design + pass a fresh pre-run critic (no anchor/DV gate needed); do not
force it if only re-grinding. The VWSD probe itself is ≥2 sessions out (ratify ≠ run). Forced-both stays CLOSED.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
