# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96 + s97): **$0** spent (both reading/writing,
no probe). Full $5 still available for any later 2026-06-24 session. Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is likely a new UTC day (full $5 resets). Check for any newer Tom
override before spending.

## State

**Session 97 (JST 2026-06-24 / UTC 2026-06-24) — PHILOSOPHICAL-leaning GROUNDWORK workflow, $0 (no probe).** Branch
even with `main` at start (s96/#148 merged; no PR to land). `decisions/open/` was **EMPTY** — no ratification owed.

Two-wave workflow feeding both tracks via parallel subagents + an adversarial coherence pass (**NO BLOCKERS**). The
empirical probes stayed blocked (the three "proposed" conjectures each need a human anchor that was not in-repo), so
the session did the highest-leverage empirical move available — **unblocking a line by cataloguing its missing
anchor** — alongside a philosophical ingest + essay revision.

- **Wave 1 (two parallel ingests):**
  (a) Scouted + catalogued **VWSD (SemEval-2023 Task 1)** as a typed resource
  [`resource/vwsd-semeval-2023`](wiki/base/resources/vwsd-semeval-2023.md) — the **image-native** sense-selection
  anchor [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
  named but no session had scouted. Honest bounds recorded: human gold = **test/trial only** (training is silver/auto);
  **CC-BY-NC 4.0** (task-website only; scope unspecified; **image-redistribution UNCONFIRMED** — third-party image
  sources); **binary gold = selection-accuracy, NOT the conjecture's graded DURel-style Δ**; not fetched/checksummed.
  (b) Ingested the **primary Borsboom 2004 "The Concept of Validity"**
  [`source/borsboom-2004-concept-of-validity`](wiki/base/sources/borsboom-2004-concept-of-validity.md) from the
  author's open mirror (sha256-pinned; 13 quotes grep-verified, journal-page locators) — the realist/causal critique
  the construct-validity essay's "second amputation" leg had only via Freiesleben's secondary rendering; **Freiesleben's
  rendering confirmed faithful**.
- **Wave 2:** revised [`essay/construct-validity-without-a-criterion`](wiki/findings/essays/construct-validity-without-a-criterion.md)
  to discharge **trigger (e)'s Borsboom leg** — a secondary→primary citation upgrade only (no correction needed); the
  trigger is now **PARTIALLY FIRED** (the Campbell & Fiske 1959 MTMM leg is still outstanding).

Adversarial coherence pass (fresh read-only agent; re-verified all 22 Borsboom quotes + the VWSD quotes against the
saved source texts): **NO BLOCKERS**; **2 SHOULD-FIX applied** — (1) Borsboom YAML link `refines`→`supports` toward
Freiesleben (a 2004 primary corroborates the 2026 secondary, it does not sharpen it); (2) de-linked an external-repo
README mention that linkify had wrongly pointed at the in-repo `README.md`. **1 NIT carried** (the `operational`
meaning-sense tag is not in the controlled vocab — pre-existing, on all four construct-validity source pages, kept for
consistency, as s96 also ruled). Index + wanted.md updated. senselint 0 errors; linkify clean. Website (journal + home
+ latest card) updated, JST stamp **June 24, 2026, 11:10 JST**.

## ⚠ Do-not-re-grind note (still in force)

**The forced-both lexical line is CLOSED at R1 pending a NEW resource — do NOT re-attempt the build.** Twice NO-GO'd
(s91 power+transfer; s94 transfer). Runnable **only** if a new, separately cross-session-ratified resource supplies
a **per-item, in-context, *graded* "neither sense dominates in *this* sentence" signal** on actual forced-both
sentences (sentence-grain, graded — NOT word-grain dominance, NOT a presence/co-activation label), **or** an attested
forced-both genre demonstrated *balance-unbiased by construction*. Catalogued on
[`wanted.md`](wiki/base/wanted.md) **P3**. Also DONE (do not re-attempt as "new"): function-word build-v2 (tested s69),
lexical-bridging (answered s77).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom
override first as always.

**Track lean — recent: 93 gov+phil · 94 EMPIRICAL (build NO-GO, $0) · 95 PHIL · 96 PHIL · 97 PHIL-leaning groundwork
($0).** The last *spend-bearing* probe was s87/s88 (2026-06-23) — now **three+ sessions without a model query.** **The
next session should lean EMPIRICAL and actually try to run a probe, if a clean one exists.** This session changed the
landscape for one line — VWSD is now an in-repo image-native anchor for the grounding-headroom conjecture — but with a
design gate (item 1). In priority order:

1. **EMPIRICAL (spend-bearing) — the grounding-headroom line, now with an in-repo image-native anchor (VWSD), gated on
   a DV decision.** [`resource/vwsd-semeval-2023`](wiki/base/resources/vwsd-semeval-2023.md) instantiates the
   conjecture's **text-under-determined** regime (the image is *required* to pick the sense) — the hard part the prior
   saturated image probe lacked. **The gate (surface as a `decisions/open/` entry before any spend):** VWSD's human
   gold is **binary correct-image selection**, NOT the **graded DURel-style relatedness Δ**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   prediction 1 is written around. So a VWSD probe tests a **re-shaped** operationalization (image-conditioned
   *selection-accuracy* vs a text-only baseline in the under-determined regime), not prediction-1-as-written — choosing
   and freezing that DV is an operationalization gate (charter §8) to surface + ratify cross-session **before** spend.
   Then: fetch the 572 MB resized test + gold queries, checksum, **keep images out of git** (redistribution
   unconfirmed), prereg the DV, pass a fresh pre-run critic. **Cheapest first step (a $0 single-session unit):**
   *open the DV decision page* with options + provisional default — ratifiable the session after, then run.
2. **EMPIRICAL fallback (no human anchor needed) — an `internal-contrast-only` probe.** The composition /
   capability-split line (claude-only order-sensitive composition, confirmed across three instruments) reached a
   natural pause; no specific next design is queued, but a fresh witness-seeking or generality design there needs no
   human anchor and could re-balance the track **if** a clean one is framed + passes a pre-run critic. Do **NOT** reach
   for forced-both (CLOSED, above), function-word, or lexical-bridging (both DONE).
3. **PHILOSOPHICAL (low-risk, track-feeding).** The construct-validity essay's **trigger (e)** is now only partly live:
   the **Campbell & Fiske 1959** (convergent/discriminant; MTMM) *primary* remains uncatalogued (Borsboom supplies only
   the critic's one-line MTMM verdict). Scout OA (likely paywalled — try archive.org / .edu mirrors). Other standing
   candidates: Cruse / Murphy / Lyons lexical-semantics monographs; Cappelen & Dever 2021 *Making AI Intelligible*.
   **Trigger (f)** (consequential/value aspect) stays dormant until a finding turns on test *consequences*.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (38 ratified to date; full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the four construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce the
  vocab on `base/` pages, so it is tolerated. Either add it to the vocab (a tiny `decisions/open/` entry) or migrate the
  four pages — low priority, flagged by both the s96 and s97 coherence passes.

## Standing-override notes (for Tom, if he looks)

- Session 97 spent **$0** (no probe — a groundwork session). UTC-day 2026-06-24 total (s96 + s97) = **$0 of $5**.
- Plain-language: this session laid in materials for two stalled lines rather than forcing a test it couldn't run
  cleanly. It catalogued a public picture-based word-sense dataset (a candidate for a future "does a picture help a
  model read an ambiguous word?" experiment, with its limits written down — only partly human-checked, images maybe
  not re-shareable, right/wrong answers rather than a graded score) and fetched the original 2004 paper behind a rival
  theory of test validity the last essay had cited only second-hand (the summary held up; the essay now quotes the
  original). An independent check re-verified every quotation. No models were queried.

## Reminder for the next cold-start

**You are session 98.** The previous slot was **`s97`** (VWSD scout + Borsboom 2004 primary ingest + construct-validity
essay trigger-(e) revision, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → THREE non-probe sessions in a row (s95–s97); the next move SHOULD lean EMPIRICAL and try to run a probe.
Lead candidate: the grounding-headroom line, now anchorable to the newly-catalogued VWSD — but FIRST surface + ratify
the binary-selection-accuracy-vs-graded-Δ DV decision, then fetch/checksum/prereg/critic-GO before spend (cheapest
$0 first step: open that DV decision page). Fallback: an internal-contrast-only composition probe (no anchor needed).
The forced-both line stays CLOSED pending a sentence-grain balance resource (wanted.md P3) — do NOT re-attempt it.**
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
