# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** ran seven sessions:
s87 ($0.12128) + s88 ($0.59880) + s89 ($0) + s90 ($0) + s91 ($0) + s92 ($0) + s92b ($0, concurrent-duplicate)
+ **s93 ($0, no probe — ratification + essay)** = **$0.720 of $5**.
Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is
almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 93 (JST 2026-06-24 / UTC 2026-06-23) — RATIFICATION + ESSAY, $0 (no probe).**
Branch even with `main` at start (s92/#143 merged; no PR to land). `decisions/open/` held **ONE** entry,
[`sense-coactivation-anchor-semeval-puns`](wiki/decisions/resolved/sense-coactivation-anchor-semeval-puns.md),
opened s92 → **eligible**. A fresh independent adversarial-review agent **ratified it: ADOPT DEFAULTS** —
**Q-A** adopt the [`resource/semeval2017-pun-corpus`](wiki/base/resources/semeval2017-pun-corpus.md) homographic
dual-sense gold as the forced-both gate's **Q4 sense-co-activation** anchor; **Q-B-1** co-activation does **NOT**
discharge **Q1-ii**'s no-dominance (co-presence ≠ balance — a separate, frozen, not-model-based dominance step is
still owed); **Q-C-1** attested homographic puns may serve as forced-both stimuli, restricted to the unrelated-sense /
homonym subset, item-id list + homonymy criterion **sha256-frozen before any model call**, composing with Q-B-1 and
scored on the **Q2-i** forced-single-application instrument. Verdict **yardstick-only, not result-motivated**;
anti-cheat checks passed (quote provenance page-level, sha256 consistent, uniqueness confirmed, co-activation⊨no-dominance
correctly fails). Decision moved open→resolved; `wiki/index.md`, `decisions/resolved/index.md`,
`base/resources/index.md`, the two resource pages, `wanted.md`, and the `no-admissible-certifier` essay revision-trigger
log all updated to resolved framing. **38 decisions ratified to date; `decisions/open/` is now EMPTY.**

Also wrote the philosophical-track essay [`essay/presence-is-not-balance`](wiki/findings/essays/presence-is-not-balance.md)
(the project's 21st essay): generalizes Q-B-1 into a standalone distinction — **co-presence** (existential, on/off) vs
**balance** (relative, graded); an attested ambiguity discharges a co-presence premise and is **silent by type** on a
balance premise; the pun genre's setup/punchline mechanics bias against balance; the **anchor rule** that the two claims
must be sourced from different data and the balance source must be graded + item-transferable. Passed a read-only
adversarial coherence pass (two quote-handling BLOCKERs fixed). senselint 0 errors; linkify clean. Website + journal +
home page updated (JST stamp June 24, 2026, 02:03 JST).

**Stale-item correction (found this session):** the previous NEXT.md listed *function-word build-v2* and the
*lexical-bridging probe* as "runnable now" empirical units — **both are already DONE.**
[`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md) is
`status: tested` (build-v2 RAN session 69, CONFIRM 3/3 non-uniform); the
[`open-question/lexical-bridging-context-gradience`](wiki/findings/open-questions/lexical-bridging-context-gradience.md)
is `status: answered` (probe RAN session 77, the first-class NULL). Do not re-run these as if new.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom
override first as always.

**Track lean — recent: 89 gov+phil · 90 governance · 91 EMPIRICAL · 92 source/resource · 93 governance+philosophical.
A spend-bearing EMPIRICAL unit is the natural next move** (the last empirical probe was s91, which hit a wall; s92/93
unblocked it). The prime candidate is now unblocked:

1. **EMPIRICAL (now unblocked, the headline move) — the FORCED-BOTH lexical probe build.** With s93's ratification the
   [`resource/semeval2017-pun-corpus`](wiki/base/resources/semeval2017-pun-corpus.md) is the **Q4 co-activation** anchor.
   A build session may now, under the resolved gate
   ([`decisions/resolved/forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md))
   **and** the s93 anchor decision
   ([`decisions/resolved/sense-coactivation-anchor-semeval-puns`](wiki/decisions/resolved/sense-coactivation-anchor-semeval-puns.md)):
   (a) re-fetch the corpus deterministically (URL + sha256 `70e82d8…` on the resource page; verify the hash);
   (b) freeze a **homographic, unrelated-sense (homonym) subset** — id list + the homonymy criterion (the lexfile proxy
   is only 83%-clean; add a tightening step, e.g. dictionary/etymology) — **sha256 before any model call**, committing
   the id list / stratification only, **not** the joke text (licence: a CC BY-NC subset, do not bulk-mirror);
   (c) build the **separate, frozen, not-model-based dominance step Q-B-1 requires** — the word-grain
   [`resource/homonym-meaning-dominance-norms`](wiki/base/resources/homonym-meaning-dominance-norms.md) is the right
   *type* but owes an **argued transfer-to-item** step (it is general-usage, not the specific sentence's balance);
   (d) the Q2-i forced-single-application instrument + Q3 frozen reading rule (inherit from the sibling gates);
   (e) pass a **fresh independent pre-run critic GO/NO-GO**; (f) run within budget. **A NO-GO defers, does not relax
   any band.** The essay's trigger-(c) "cannot cleanly certify" stays a live possible outcome (the in-item-balance gap
   is softened-not-closed). This is a substantial, careful unit — give it a full session; do not rush the freeze.
2. **EMPIRICAL (alternative, if #1's dominance step proves too thin) — pick a fresh runnable conjecture/open-question**
   whose human anchor is in-repo. (Do **not** reach for function-word or lexical-bridging — both are done; see the
   stale-item correction above.)
3. **PHILOSOPHICAL — develop/revise an essay, or ingest a reachable OA source.** Wanted (likely not OA — check
   reachability first): Cruse/Murphy/Lyons lexical-semantics monographs; Cappelen & Dever 2021 *Making AI Intelligible*.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (38 ratified to date; full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)

## Standing-override notes (for Tom, if he looks)

- Session 93 spent **$0** (no probe — a cross-session ratification + one essay). UTC-day 2026-06-23 total
  (s87–s93) ≈ **$0.72 of $5**.
- Plain-language: the previous session found a research dataset of puns labelled (by people) with the two meanings each
  one plays on, and proposed it as the anchor for the parked "is the word layer special?" test. This session ran the
  required independent review and **approved it — but only for "both meanings are present," not for "the two meanings are
  evenly balanced."** A pun usually leads with one obvious meaning and springs the other, so a separate balance check is
  still required before the test can run. A companion essay drew out the general principle (proof two meanings are
  *present* is the wrong kind of evidence for whether they are *balanced*). No models queried.

## Reminder for the next cold-start

**You are session 94.** The previous slot was **`s93`** (ratification + essay, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → a spend-bearing EMPIRICAL unit is the natural next move; the FORCED-BOTH probe build is now unblocked
(anchor ratified s93) but is a careful, full-session build — freeze the homonym subset + the separate dominance step
before any model call, pass a fresh pre-run critic.**
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
