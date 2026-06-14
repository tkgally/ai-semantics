---
type: result
id: relational-history-perturbation-v4
title: The history-perturbation arm (v4) — the within-arm decoupling works, and the answer is TEXT POSITION, not stamped chronology; the first defensible position-following reading the v3 instrument could not earn
meaning-senses:
  - relational
  - distributional
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-14
updated: 2026-06-14
links:
  - rel: refines
    target: result/relational-history-perturbation-v3
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the history-perturbation arm (v4) — chronology and text-position decoupled within one arm; both models follow position

> **Status: proposed (2026-06-14).** The decisive within-arm decoupling named by the v3
> post-run verifier as "the real next step." v3 found a forward chronology elevation that
> vanished under direction reversal but **could not separate "chronologically last" from
> "physically last in the text"** — they were collinear inside every arm. v4 dissolves that
> confound: chronology is carried by an explicit per-line **round stamp**, and the decisive
> (most-recent-round) line is deliberately placed **non-terminally**, so a single arm crosses
> *chronologically-latest twin* against *physically-last-line twin* orthogonally. The result:
> **both models track physical text-position, not stamped chronology.**
> **claude → TEXT-POSITION ARTIFACT** (Δ_pos CI-clean, Δ_chron null); **gemini →
> INCONCLUSIVE/MIXED**, same direction (strongly position-dominant, with a small chronology
> residual that leaves both CIs off 0.5). **460 finding-bearing calls, $0.630 billed ($0.942
> all phases this session), 0 NA, 0 retried, strict-compliance 1.000, 0 missing costs.**
> Independent pre-run critic (**GO-after-fixes**; the stamp-as-chronology indicator ruled
> **inside-class hygiene, no decision page** — so the run was not blocked) + independent
> post-run verifier (**every headline number re-derived from raw from scratch with an
> independent bootstrap, 0 mismatches**; it sharpened the gemini reading — the ρ_chron
> elevation is a pure position-gradient artifact with zero residual chronology signal — see
> §"Reading it honestly"). Run record:
> [`experiments/runs/2026-06-14-relational-history-perturbation-v4/`](../../../experiments/runs/2026-06-14-relational-history-perturbation-v4/README.md);
> frozen PREREG:
> [`PREREG.md`](../../../experiments/runs/2026-06-14-relational-history-perturbation-v4/PREREG.md).
> **`anchor: internal-contrast-only`** (within-model contrast; no human-comparison claim).

## What v4 changed, and why it is still the same instrument

v4 keeps the ratified v1/v2/v3 instrument class — text-grid referents on the frozen v1
figures (harvest route, not new figures), near-twin pairs, byte-identical content multisets,
nonce coined terms, fresh-matcher forced-format elicitation, within-model contrast — and
makes exactly the one structural change v3's verifier prescribed, plus the v3 fix-list:

1. **Chronology is an explicit stamp, not physical position.** Each evidence line reads
   "- Round k: …"; the INTRO states **neutrally** that the round number (not the line order)
   carries recency and that the lines are not necessarily in round order. It does **not**
   instruct the model to weight recency — whether it spontaneously weights the stamp, the
   line order, or treats the evidence as an order-free set is what the probe measures.
2. **A non-adjacent perturbation point.** The decisive (most-recent-round, R4) line is placed
   either physically last (DPOS=late → physically-last twin = the chronologically-latest
   twin) or non-terminally with chronologically-earlier lines after it (DPOS=early →
   physically-last twin = the *other* twin). Crossing DPOS with which twin owns the latest
   stamp makes **chronologically-latest twin** and **physically-last-line twin** balanced and
   **orthogonal within one arm** (cov 0; asserted at build, re-derived by the verifier with 0
   mismatches).
3. **Panel: claude + gemini only** (gpt dropped per the v3 fix-list — two harvest+
   certification attempts showed it cannot supply solo-decodable near-twin descriptions at
   this difficulty), both at raised power (12 / 11 clusters vs v3's 9).

The pre-run critic ruled change 1 **inside-class indicator hygiene**: the construct is
unchanged (does interpretation track *where in the chronology* conflicting evidence lands, or
only the content set?); the stamp changes *how cleanly*, not *what* is measured, and a pure
position reader lands in the relational-claim-free TEXT-POSITION ARTIFACT terminal — the v3
over-claim is not smuggled back in. No `decisions/open/` page was opened.

## The two headline statistics (frozen pre-run; verdict mapper is code)

Over gated, parsed, in-pair mixed trials, both centered at 0.5:

- **Δ_chron = ρ(pick = chronologically-latest twin) − 0.5** — a stamp/chronology reader gives
  CI off 0.5; a content-only or position reader gives CI including 0.5.
- **Δ_pos = ρ(pick = physically-last-line twin) − 0.5** — a text-position reader gives CI off
  0.5; this is the diagnostic v3 could obtain only by reversing the whole record, here got
  **within one arm**.

Because the two twins are crossed orthogonally, a pure chronology reader gives Δ_pos ≈ 0 and a
pure position reader gives Δ_chron ≈ 0 (verified on idealized-reader fixtures), so the joint
reading separates them.

| model | gate (control acc) | gated clusters | ρ_chron (CI) | ρ_pos (CI) | min cell n | verdict |
|---|---|---|---|---|---|---|
| **claude** | 0.917 (consistent 0.917, stamp-respect 0.917) | 10/12 | **0.509 [0.465, 0.556]** (null) | **0.698 [0.594, 0.804]** (clean) | 39 (≥36) | **TEXT-POSITION ARTIFACT** |
| **gemini** | 0.909 (consistent 0.955, stamp-respect 0.864) | 8/11 | **0.562 [0.516, 0.609]** (excludes 0.5) | **0.812 [0.695, 0.930]** (clean) | 32 (<36) | **INCONCLUSIVE/MIXED** |

The decoupling cells tell the story directly (by DPOS level; in LATE cells ρ_chron ≡ ρ_pos
because the latest-stamp line *is* the last line):

| model | LATE ρ_chron = ρ_pos | EARLY ρ_chron | EARLY ρ_pos |
|---|---|---|---|
| claude | 0.709 | **0.312** | **0.688** |
| gemini | 0.875 | **0.250** | **0.750** |

In the EARLY (conflict) cells — where the most-recent-round line sits early and an older line
sits last — **both models pick the physically-last twin ~0.69–0.75 of the time, i.e. they
pick the chronologically-*earlier* twin against the stamp.** That is text-position following.

## Reading it honestly

**claude is a clean TEXT-POSITION ARTIFACT.** Δ_pos's CI excludes 0.5 (last-line-following)
while Δ_chron's CI includes 0.5, with ≥24 (indeed ≥36) gated in-pair trials in every
(clast×dpos) cell. Per the frozen decision rule this is a **methodological finding about
prompt geometry; it says nothing relational.**

**gemini is position-dominant; its INCONCLUSIVE/MIXED is a statistical artifact of position
bleeding into the chronology statistic, not a competing chronology signal.** Its Δ_pos is
strong and clean (0.812), and in the conflict cells it follows position exactly as claude does
(early ρ_pos 0.750 vs ρ_chron 0.250). Its *pooled* ρ_chron (0.562) does have a CI marginally
above 0.5, which trips the "both CIs excluded → channels confounded" final-else clause — but
the post-run verifier showed that elevation carries **zero residual chronology signal**: a
**pure-position reader** with gemini's own late/early ρ_pos (late 0.875, early 0.750) is
*forced* to produce ρ_chron = (0.875 + (1 − 0.750)) / 2 = **0.5625 — identical to the observed
value to the digit** — and early ρ_chron (0.250) equals 1 − early ρ_pos (0.750) **exactly**.
The entire ρ_chron > 0.5 is the mechanical consequence of gemini following position *more
strongly in late cells than early cells* (a serial-position/recency-of-reading gradient)
interacting with the fact that chronology and position coincide in late cells by construction.
So gemini is **position-dominant, full stop**; "INCONCLUSIVE/MIXED" here means "position bled
into the chron statistic," **not** "two genuine competing signals." (gemini's ≥36 null floor
was also unmet — min cell 32 after 3 of 11 clusters gated out, exactly the attrition the
pre-run critic flagged — so a null could not have been certified regardless of the CIs; but
the null clause is moot since gemini is position-driven, not content-only.)

**Crucial scope limit (pre-run critic calibration): position-following here is
indistinguishable from stamp-blindness.** The stamp-respect control is a single-twin record;
passing it (claude 0.917, gemini 0.864, both ≥ the 0.75 floor) shows only that a model is
**not derailed by non-monotonic stamp layout** — it does **not** prove the model reads the
stamp *values* as recency. So this result must **not** be read as "the models chose to ignore
recency." The defensible statement is narrower: **when stamped chronology and physical
position conflict, both models' picks are governed by physical position; whether they parse
the round numbers as recency at all is not established by this design.**

## What it means for the conjecture — stays `proposed`, neither falsified nor certified

For [`conjecture/commutative-convention`](../conjectures/commutative-convention.md):

- **Not falsified.** The falsification clause is *chronology-tracking* (Δ_chron clean, Δ_pos
  null). Neither model tracks the stamped chronology; if anything, in the conflict cells they
  move *against* it (toward the physically-last, chronologically-earlier line). So the
  conjecture's invariance-of-content bet is **not** overturned by a constituted, path-dependent
  convention.
- **Not certified.** The commutative null requires both channels null (a content-only,
  order-and-position-insensitive reader). The models are **not** content-only — they are
  strongly **position-driven** (Δ_pos clean in both). So the null is **not** certified either;
  v4 does not strengthen the deflationary bet.

The conjecture therefore **stays `proposed`** — but the inconclusiveness is now fully
*located*, and located somewhere new. v3's post-run verifier explicitly **refused** to assert
"physical position, not chronology," because v3's collinear forward arm could not earn it
(a pure position account predicted a reversed-arm signal that collapsed to chance instead).
**v4's within-arm decoupling earns exactly that reading cleanly**: the models' picks, when the
two cues conflict, are governed by where the text sits, not by the stamped chronology. The
relational/commutativity question the conjecture cares about is **not answered** by a
position-following model — a probe geometry that conflates "the latest convention" with "the
last line of the prompt" cannot, even in principle, see a chronology-based relational
convention. That is the methodological lesson v4 converts from v3's unprovable suspicion into a
clean result.

## The methodological achievement (what v4 *did* settle)

The decoupling itself worked, and that is a real, reusable gain:

- **Chronology and text-position were separated within a single presentation arm**, so the
  verdict no longer hinges on the direction-fragile cross-arm comparison that left v3
  inconclusive. The orthogonality is exact (cov 0 per cluster, asserted at build and
  re-derived by the verifier).
- The instrument **fails safe**: cluster attrition (claude 10/12, gemini 8/11) can only cost a
  null-certification, never manufacture a false chronology positive — a position-follower is
  routed into Δ_pos, not Δ_chron, by the orthogonal design.
- The clean outcome **names a confound for the whole relational line**: any future
  chronology/recency probe over a *linear* prompt must decouple stamped recency from physical
  position, or it cannot distinguish "tracks the latest convention" from "reads the last
  line." v4 is the template.

## Caveats and scope limits (carried from v2/v3, plus the v4 stamp shift)

1. **`anchor: internal-contrast-only`** — Δ_chron/Δ_pos are within-model contrasts over
   byte-identical-content records differing only in stamp and line order. **No human-comparison
   claim.** No in-repo human resource anchors order- or position-sensitivity (Brennan & Clark
   anchors historicity/partner-specificity and reports an order-*insensitive* statistic;
   Hawkins anchors the convergence baseline only). Per the ratified relational-line posture
   ([`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md),
   [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md);
   terminal-state mechanics
   [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)).
2. **Position-following ≡ stamp-blindness here** (the critic calibration above): the result is
   methodological, about prompt geometry / stamp-value neglect, not a claim that the models
   *decline* to use recency.
3. **Forced-label elicitation:** the verdicts hold under the forced single-label format;
   suppressing visible deliberation could change the pick mechanism, so they do not
   automatically transfer to free-form settings.
4. **Harvested-and-certified, not live-game, stimuli**, and certification **selects for
   individually decodable lines** — the result says nothing about conventions whose lines are
   only interpretable in context. The disclosed stimulus bias sharpens the X-vs-Y conflict,
   i.e. biases *against* the ~0.5-noise null, not toward the conjecture's bet.
5. **Pilot scale**, homogeneous per-model probes, text grids (the v1-scoped yardstick), gpt
   dropped, gemini's null floor unmet. No pooling or numeric comparison with v2/v3 (v4
   supersedes them at the **verdict level only**).
6. **Image referents, cross-family dyads, and live (non-constructed) reassignment** remain the
   conjecture's named scope extensions, untouched here.
