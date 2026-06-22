---
type: design
id: cross-level-shared-instrument-v1
title: cross-level shared-instrument probe v1 — one frozen graded-decline + confidence instrument applied identically at the lexical, constructional, and relational levels, to test whether the "graded-in-the-aggregate, discrete-in-the-moment" shape is one cross-level property or three rhyming facts
meaning-senses:
  - distributional
  - constructional
  - relational
  - referential
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-22
updated: 2026-06-22
links:
  - rel: operationalizes
    target: conjecture/cross-level-gradience-aggregate-not-moment
  - rel: depends-on
    target: open-question/gradience-population-not-moment
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
  - rel: refines
    target: essay/preference-without-commitment
  - rel: refines
    target: essay/aggregation-not-constitution
  - rel: depends-on
    target: essay/cross-level-convergence-ladder
---

# Experiment design v1 — cross-level shared-instrument probe

> **Status: BUILT + FROZEN, NOT RUN (2026-06-22, build session).** No probe was run and no
> spend was opened. The single shared instrument is frozen and sha256'd
> ([`cross-level-shared-instrument-v1/instrument.json`](cross-level-shared-instrument-v1/instrument.json),
> sha `3cdfe178…`, [`instrument.sha256`](cross-level-shared-instrument-v1/instrument.sha256));
> the fresh synthetic item sets are frozen and build-certified (17/17 no-API checks PASS,
> [`certification_report.json`](cross-level-shared-instrument-v1/certification_report.json)).
> The probe is run-ready ([`probe.py`](cross-level-shared-instrument-v1/probe.py), refuses to
> run without an explicit critic-GO flag; `ABORT_USD=0.60`) and the frozen cross-level reading
> rule is encoded ([`analyze.py`](cross-level-shared-instrument-v1/analyze.py)). **What remains
> is the run itself**, deferred to a later session under a fresh independent **pre-run critic
> GO/NO-GO** against the frozen instrument and a **budget** check — see
> [`README.md`](cross-level-shared-instrument-v1/README.md). Pre-flight estimate ≈ **$0.10–0.25**.

This operationalizes the conjecture
[`conjecture/cross-level-gradience-aggregate-not-moment`](../../wiki/findings/conjectures/cross-level-gradience-aggregate-not-moment.md)
under its **resolved** gate
[`decisions/resolved/cross-level-shared-instrument-operationalization`](../../wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md),
which ratified **Option A** + the binding build-session conditions **C1–C4** + the bound
sub-questions **Q2/Q3/Q4**. The gate is this design's full spec; this document records how the
build encodes it, the comparability analysis, the verdict map, the anchor posture, and the
honest limits.

## 0. The bet, in one sentence

A SINGLE commitment instrument — an explicit graded categorical decline (`SAME/DIFFERENT/
UNCLEAR`-shaped) **plus** a 0–100 confidence rating — applied **identically** at a lexical
bridging item, a constructional ambiguous item, and a relational mid-record item, frozen and
sha256'd before any run, to ask whether the **same model** shows the two-axis dissociation
(graded across the **aggregate**, discrete/uncommitted on the single **moment**) under that one
frozen instrument at **≥2** levels (CONFIRM), or whether the shape **dissolves** under
equalization (the first-class null), or is **WEAK**.

## 1. The single shared instrument (Option A, frozen)

The instrument is one elicitation per item: the model gives a three-way categorical call
(two committing poles + an explicit `UNCLEAR` decline) **and** a 0–100 confidence integer, on
one line. Both C1 components ride in one call. The level-specific poles are
`SAME`/`DIFFERENT` (lexical), `READING1`/`READING2` (constructional), `FIGURE1`/`FIGURE2`
(relational); the decline token `UNCLEAR` and the 0–100 confidence frame are identical across
levels. Full text in [`instrument.json`](cross-level-shared-instrument-v1/instrument.json).

This generalizes the **already-existing Option-A instrument at the lexical leg**
([`lexical-bridging-context-v1/instrument.json`](lexical-bridging-context-v1/instrument.json):
the `b_conf` SAME/DIFFERENT-plus-confidence framing and the `c_third` categorical `UNCLEAR`
decline with its verbatim wording) to the constructional and relational levels, holding the
elicitation shape as identical as the three stimulus types allow.

## 2. Encoding the binding conditions C1–C4 (quoted from the gate)

The gate's four conditions are quoted verbatim into
[`instrument.json`](cross-level-shared-instrument-v1/instrument.json) (`binding_conditions_quoted`)
and enforced as follows.

- **C1 — categorical decline, not confidence, is load-bearing for the moment pole.** "The
  categorical DECLINE (not the confidence rating) is the load-bearing instrument for the
  moment/commitment pole at EVERY level. Confidence may corroborate but may NOT, on its own,
  flip a moment-axis verdict." Encoded in [`analyze.py`](cross-level-shared-instrument-v1/analyze.py):
  the moment-pole verdict (`DISCRETE/UNCOMMITTED-ON-MOMENT` vs `GRADED-ON-MOMENT`) is decided
  solely on whether the **decline rate** (`%UNCLEAR`) is elevated on the ambiguous class; the
  confidence gap is reported but never flips the verdict. This faithfully ports the lexical
  gate's "position by B alone; commitment by both B and C" with the moment leg keyed to the
  decline, matching [`result/lexical-bridging-context-v1`](../../wiki/findings/results/lexical-bridging-context-v1.md)'s
  finding that the ungraded-commitment null was carried by near-zero categorical decline, not
  by confidence.
- **C2 — numeric/wording freeze + sha256.** All four pinned in `instrument.json`: (i) the
  confidence scale `[0,100]` + mid-band `[40,60]`; (ii) the verbatim per-level decline wording;
  (iii) the per-level `aggregate`/`moment` operational definitions (Q3), relational labelled
  the weaker within-record notion; (iv) the cross-level CONFIRM/DISSOLVE/WEAK thresholds.
  The file is sha256'd ([`instrument.sha256`](cross-level-shared-instrument-v1/instrument.sha256));
  `certify.py` re-checks the live hash matches the freeze.
- **C3 — clear-class precondition → NO-GO, per level (RUN-TIME).** A level is interpretable
  only if its clear classes show **high confidence and low decline** under the shared
  instrument. Encoded as a precondition gate in `analyze.py` (`CLEAR_DECLINE_MAX = 0.20`,
  `CLEAR_CONF_MIN = 70`); a level failing it collapses to weak / `internal-contrast-only` and
  contributes no moment verdict. This is checked **on data, not at build** — `analyze.py`
  documents it, and the synthetic clear controls give every level mass on both poles to make
  the check meaningful.
- **C4 — channel-sensitivity guard.** A confidence shift on the ambiguous class **without** a
  matching categorical-decline shift is flagged as a **self-report effect, not graded-moment
  evidence** (`analyze.py` `C4_confidence_only_self_report`). This neutralizes the
  channel-sensitivity caught at the lexical working surface
  ([`result/lexical-bridging-context-working-surface-v1`](../../wiki/findings/results/lexical-bridging-context-working-surface-v1.md)).

## 3. The three levels and their items (Q3 comparability slot, frozen)

Per Q3, "aggregate" and "moment" are pre-registered per level in `instrument.json`
(`levels.*.aggregate_operational` / `moment_operational`):

| level | aggregate (frozen) | moment (frozen) | items | anchor |
|---|---|---|---|---|
| lexical | ordering across a **population** of bridging-vs-clear items | posture (decline+conf) on the single bridging item | MANIFEST → frozen DWUG stratum (48) + WiC poles (40), by sha | usage-similarity (capped) |
| constructional | graded paraphrase/interpretation-**preference** shift across items | posture on the single ambiguous item | 30 fresh synthetic (10 sets × 1 ambiguous + 2 clear) | `internal-contrast-only` |
| relational | convention-recoverability from the **content-set of one record** (DISCLOSED: weaker within-record / single-reader-recoverable) | posture on the single mid-record binding | 30 fresh synthetic (10 sets × 1 ambiguous-midrecord + 2 clear) | `internal-contrast-only` |

- **Lexical** reuses the lexical leg's frozen items (no re-authoring, no corpus text in-repo):
  [`items_lexical.json`](cross-level-shared-instrument-v1/items_lexical.json) references
  `stratum.csv` (sha `e7d36773…`) and `wic_poles.csv` (sha `b8b1a7aa…`).
- **Constructional** items
  ([`items_constructional.json`](cross-level-shared-instrument-v1/items_constructional.json))
  are author-constructed genuine two-reading ambiguities (PP-attachment, coordination scope,
  quantifier scope, argument structure, pronoun binding, comparative ellipsis), each paired
  with two minimal-pair controls forcing one reading each. They draw on the project's
  constructional sense of "graded preference vs categorical commitment"
  ([`essay/preference-without-commitment`](../../wiki/findings/essays/preference-without-commitment.md);
  [`theory/constructional-meaning-in-llms`](../../wiki/findings/theory/constructional-meaning-in-llms.md)).
- **Relational** records
  ([`items_relational.json`](cross-level-shared-instrument-v1/items_relational.json)) follow
  the [`relational-spontaneous-recency-v5-optionA`](relational-spontaneous-recency-v5-optionA.md)
  format: a 4-figure grid, a stamped history binding a nonce term, and a query about the
  referent at one moment. The ambiguous class binds the term to **two** figures with the
  **same round stamp** (no recency/frequency tie-break → genuinely underdetermined); the clear
  controls bind exactly one. The within-record "aggregate" caveat is disclosed per Q3.

## 4. The comparability analysis (the crux — honest)

**What is held identical across levels** (the comparability claim): the *elicitation question*
— a three-way categorical commit/decline (`SAME/DIFFERENT/UNCLEAR`-shaped) plus a 0–100
confidence rating, the same `[40,60]` mid-band descriptor, the same answer format ("one line,
the token, a space, an integer, and nothing else"), the same temperature (0), and the same
per-axis reading rule (decline load-bearing for the moment pole). The ONLY things that vary are
(a) the level-specific noun naming what same/different is asked of (`sense` / `reading` /
`referent`) and (b) the level-specific gloss after the `UNCLEAR` token.

**What unavoidably differs**: the stimulus *body*. A lexical bridging item is two sentences
sharing a marked target word; a constructional ambiguous item is one sentence plus two
candidate readings; a relational mid-record item is a stamped record plus a queried binding.
These are not the same text and cannot be made so without changing what each level *is*.

**Why the difference does not change what is asked — and where that argument has a limit
(disclosed).** The instrument asks the same *shape* of question at each level: "are the two
candidate readings of the queried item the SAME/one or DIFFERENT/the-other, or is the case
genuinely UNCLEAR, and how confident are you?" The decline option means the same thing at each
level (the case is genuinely in-between / both-at-once / left-open). The **residual risk** is
that the body difference *itself* — its length, its surface form — could drive a decline or
confidence difference independent of indeterminacy. The guard is **C3**: the instrument must
read cleanly (high confidence, low decline) on each level's **unambiguous control items**
before any ambiguous-class reading is interpreted; a level whose clear classes do not clear C3
contributes no moment verdict. C3 mitigates but does not eliminate the residual; this is stated
plainly in [`README.md`](cross-level-shared-instrument-v1/README.md) as the load-bearing risk a
pre-run critic should scrutinize. It is a **disclosed residual within Q3's frozen comparability
slot**, not a new undecided operationalization knob (so no `decisions/open/` entry was opened —
see §8).

## 5. The cross-level reading rule (Q2, frozen before data)

Encoded in [`analyze.py`](cross-level-shared-instrument-v1/analyze.py) `cross_level_verdict`
and in `instrument.json` `reading_rule_frozen.cross_level_verdict_map_Q2`:

- **CONFIRM** iff the **same model** shows the two-axis dissociation (graded across the
  aggregate **and** discrete/uncommitted on the moment, i.e. **decline not elevated** on the
  ambiguous class) under the one frozen instrument at **≥2** C3-passing levels. A confirm
  resting on lexical+constructional and **excluding the relational leg** is scoped as a
  **2-level instrument-equalized regularity (R2 over levels tested)**, not a 3-level mechanism
  — per the gate's reporting nuance and [`essay/cross-level-convergence-ladder`](../../wiki/findings/essays/cross-level-convergence-ladder.md).
- **DISSOLVE** (first-class null, reported as cleanly as a confirm) iff the shape holds under
  each level's native instrument (as documented today) but fails under the equalized one — the
  moment pole becomes **graded** (elevated decline) at some level, or the levels diverge with
  no coherent per-model pattern.
- **WEAK** iff the instrument cannot express both axes at a level, a model declines the channel,
  ≥1 level fails its C3 precondition, or N is too small.

**Per-level instrument-shopping is forbidden by construction**: one frozen instrument, this
pre-committed map, dissolution reported as dissolution. No instrument may be added, dropped,
re-worded, or re-thresholded per level after any output is seen.

## 6. Anchor posture (Q4) and claim scope

This design **licenses no human-comparison claim**. The lexical leg is **capped to
usage-similarity** (inherited from
[`result/lexical-bridging-context-v1`](../../wiki/findings/results/lexical-bridging-context-v1.md);
a DWUG mid-scale pair is a human-rated usage-similarity midpoint, **not** a certified
sense bridge). The constructional and relational legs are **`internal-contrast-only`** (synthetic,
author-constructed items; no human-annotation data). **No anchor is invented.** Any unified
cross-level result is stated only as an **internal, within-model contrast at the weakest common
strength** (`instrument.json` `claim_scope_cap`).

## 7. Cost and run discipline

One temp-0 call per item per model (decline + confidence in one elicitation). ≈ 444 short-label
calls worst case (88 lexical + 30 constructional + 30 relational, × 3). Pre-flight ≈
**$0.10–0.25**; `ABORT_USD = 0.60`; gemini `reasoning:{effort:"minimal"}` (its endpoint rejects
suppression as of 2026-06-22). Well inside the $5/day cap and the $2.50 single-run flag. The run
is gated on a fresh independent pre-run critic GO/NO-GO against the frozen instrument and a
budget pre-flight (a NO-GO defers the run, never relaxes a band). The lexical arm needs the
gitignored DWUG/WiC fulltext staged via the lexical leg's `prep.py`/`prep_wic.py`, or run
`--skip-lexical` for the two synthetic arms.

## 8. Build state and the no-new-decision judgement

Built this session, no run: instrument frozen + sha256'd; fresh synthetic items frozen +
build-certified (17/17 PASS); `probe.py` run-ready and refusing-by-default; `analyze.py`
encoding C1/C3/C4 + the Q2 map; `README.md` with the honest not-run statement and the run
handoff. **No new `wiki/decisions/open/` entry was opened**: the build reused the resolved
gate's already-fixed choices throughout (Option A, C1–C4, Q2/Q3/Q4), and the one judgement call
the build faced — the cross-level comparability residual (§4) — was treated as a *disclosed
residual within Q3's frozen comparability slot*, not as an operationalization choice the gate
left undecided. A pre-run critic who judges otherwise has the standing to open one and mark this
build contingent.

## 9. Scope and limits (lead with these)

- **Behavioral, not representational.** Every level is about what models *do* on ambiguous
  items, not about graded *representations*.
- **No human comparison** (Q4): lexical capped to usage-similarity; constructional + relational
  `internal-contrast-only`.
- **Comparability residual** (§4): the stimulus body differs across levels; C3 mitigates but
  does not eliminate the risk that body form, not indeterminacy, drives a decline/confidence
  difference.
- **Synthetic ambiguity is author-judged.** `certify.py` checks structure/balance/leak, not
  human-rated ambiguity strength; the `internal-contrast-only` cap bounds the claim.
- **Relational "aggregate" is the weakest leg** (within-record, single-reader-recoverable); a
  confirm excluding it is only a 2-level R2 regularity.
- **Small, clustered N** (~10 sets/level; ~20 lexical lemmas): direction-of-effect with wide
  clustered CIs, no coverage claim, n=3 commercial models.
- **A cross-level pattern is the pattern most at risk of being a phrasing artifact** (the
  conjecture's own caution); the deflationary DISSOLVE null is first-class and reported as
  cleanly as a confirm.
