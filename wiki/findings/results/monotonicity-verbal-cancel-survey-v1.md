---
type: result
id: monotonicity-verbal-cancel-survey-v1
title: "B2 survey of NEW verbal cancel defaults — implicative, factive AND causative-inchoative entailments all clear the ceiling gate (NLI 1.00, 3/3 each); held-at-ceiling verbal defaults are findable, so the within-verbal limit is a cancel-CONSTRUCTION design problem, not a missing held default"
meaning-senses:
  - constructional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: open-question/within-verbal-cancel-at-ceiling
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: refines
    target: result/monotonicity-c2-privative-calibration-v1
  - rel: refines
    target: result/monotonicity-c1-completion-calibration-v1
  - rel: depends-on
    target: concept/coercion
---

# Result: B2 calibration survey of NEW within-verbal cancel defaults — three families, three GOs

> **Calibration survey, `internal-contrast-only`.** Path (ii) of
> [`open-question/within-verbal-cancel-at-ceiling`](../open-questions/within-verbal-cancel-at-ceiling.md):
> a small structured triage of candidate **NEW verbal cancel defaults** through cheap
> **B2 default-at-ceiling calibrations**, before any matched battery is built. It measures,
> per family, whether the panel holds the **default** entailment as a categorical entailment
> at ceiling — it builds **no** cancel arm and runs **no** asymmetry battery, so it does
> **not** test [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).
> Makes **no** human-comparison claim. Pre-registration, frozen items, every number:
> [`experiments/runs/2026-06-28-monotonicity-verbal-cancel-survey/`](../../../experiments/runs/2026-06-28-monotonicity-verbal-cancel-survey/README.md).

## Why this ran

The conjecture is `tested` on a **weak** confirm bought across the M2 **verbal-add /
nominal-cancel domain mismatch**: the only B2-passing cancel default to date was *nominal*
(C2 taxonomic "a gun" ⊨ "a weapon", [`result/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md)),
while both *verbal* cancel defaults tried floored B2 — s135 single-occurrence (a Gricean
implicature, 0.00/0.00/0.00) and C1 telic completion (a defeasible aspectual default,
0.25/0.375/0.75, [`result/monotonicity-c1-completion-calibration-v1`](monotonicity-c1-completion-calibration-v1.md)).
The open-question framed the worry that this is a **near-principled limit**: maybe the verbal
defaults the project can reach for are *disproportionately* implicatures/defeasible defaults,
so a clean within-verbal generalization confirm is un-instrumentable for want of a
categorically-held verbal default to cancel. This survey is the empirical test of that worry:
**measure** — across three NEW verbal families — whether *any* clears the ceiling gate.

## What was measured

Frozen set (items.csv sha256[:16] **`f6f11a985f47dc89`**, committed before any API call):
**18 items, 3 candidate verbal families × 6**, each a bare-frame DEFAULT entailment —

| family | default (premise ⊨ hypothesis) | verbs |
|---|---|---|
| **implicative** | "Sam managed to open the door" ⊨ "Sam opened the door" | manage, remember, bother, happen, dare, get |
| **factive** | "Sam realized that the door was open" ⊨ "The door was open" | realize, discover, regret, admit, notice, forget |
| **causative-inchoative** | "Sam broke the vase" ⊨ "The vase broke" | break, shatter, melt, tear, crack, dissolve |

NLI primary + forced-choice, temperature 0, panel claude-sonnet-4.6 / gpt-5.4-mini /
gemini-3.5-flash. 18 × 2 × 3 = **108 calls**. The causative-inchoative verbs were chosen
**distinct from the original conative contact-by-motion verbs** to avoid re-reading the
conative, and the survey does **not** re-run the ruled-out s135/C1 arms (the families are new
directions; do-not-re-grind respected — see *What this does and does not license*).

**Frozen gate (per family, not relaxable — same 0.80 / ≥2-of-3 bar as C1/C2 STEP 1b):**
default NLI affirm ≥ **0.80 in ≥2/3 models**. An independent fresh-agent **pre-run critic**
returned GO-WITH-NOTES (hash verified, no re-grind, threshold un-tuned, scope honest); an
independent fresh-agent **post-run verifier** recomputed all 18 cells from `raw_calib/*.json`
(exact match; 108/108 priced, 0 errors, 0 parse failures, cost matched).

## One-line finding

**All three NEW verbal families clear the B2 ceiling gate — NLI affirm = 1.00 in 3/3 models
for every family (every one of the 54 NLI default judgements is "entailment"). Held-at-ceiling
verbal lexical defaults are findable: implicative, factive, and causative-inchoative
entailments are all categorical at ceiling for the panel.** This refutes the **un-findability**
reading of the open-question's scarcity worry — the earlier verbal floors (s135, C1) were
specific to *aspectual/quantity* defaults the panel reads as Gricean/defeasible, **not** a
general property of all verbal defaults. (It does **not** settle the stronger *distributional*
form of the worry — these three families were chosen as a-priori near-categorical inference
types, so the result shows held verbal defaults *exist*, not that they are *common* among the
defaults a construction might naturally cancel.) Either way, the missing within-verbal confirm
is **not** un-instrumentable for want of a held verbal default; the binding constraint moves to
the **cancel-construction** side (below).

## Numbers (verified)

Default-affirm rate (n = 6 items per family per model); independently recomputed by the
post-run verifier — exact match to `raw_calib/gate.json`, 108/108 priced, 0 missing, 0 parse
failures, 0 errors.

| family | model | NLI affirm | FC affirm | gate (NLI) | pass? |
|---|---|---|---|---|---|
| implicative | A claude-sonnet-4.6 | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| implicative | B gpt-5.4-mini | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| implicative | C gemini-3.5-flash | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| factive | A claude-sonnet-4.6 | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| factive | B gpt-5.4-mini | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| factive | C gemini-3.5-flash | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| causative-inchoative | A claude-sonnet-4.6 | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| causative-inchoative | B gpt-5.4-mini | **1.00** | 0.833 | ≥ 0.80 | ✓ |
| causative-inchoative | C gemini-3.5-flash | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| | | | | **3/3 families** | **GO ×3** |

NLI label distribution: **label 0 (entailment) = 6/6 for every (family, model)**; no neutral,
no contradiction anywhere across all 54 NLI default judgements. The single non-affirm in all
108 calls is gpt-5.4-mini's **forced-choice** on one causative item (NLI on the same item is
entailment) — irrelevant to the NLI-primary gate. Even the pre-run critic's three flagged
"could-be-neutral" items (*dared to enter*, *got to taste*, *forgot that*) drew entailment from
**all three models** — the verifier confirmed `pred="0"`, no parse artifact.

## The ladder this extends (bears on the conjecture's framing)

This adds three rungs to the cancel-default ladder the C2 calibration began. The ladder now
separates cleanly by **inference type**, not by verbal-vs-nominal:

| cancel default | inference type | affirm (NLI, 3 models) | held at ceiling? | domain |
|---|---|---|---|---|
| single-occurrence ("flashed" → "only once"), s135 | Gricean quantity **implicature** | 0.00 / 0.00 / 0.00 | no | verbal |
| completion ("built the house" → "finished building"), C1 | defeasible **aspectual** default | 0.25 / 0.375 / 0.75 | no | verbal |
| category membership ("a gun" → "a weapon"), C2 | taxonomic **lexical entailment** | 1.00 / 1.00 / 1.00 | **yes** | nominal |
| **implicative** ("managed to V" → "V-ed"), this survey | **implicative-verb entailment** | **1.00 / 1.00 / 1.00** | **yes** | **verbal** |
| **factive** ("realized that P" → "P"), this survey | **factive presupposition→entailment** | **1.00 / 1.00 / 1.00** | **yes** | **verbal** |
| **causative-inchoative** ("broke the vase" → "the vase broke"), this survey | **lexical result entailment** | **1.00 / 1.00 / 1.00** | **yes** | **verbal** |

(s135/C1/C2 **numbers** quoted verbatim from [`result/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md),
§"The contrast this sharpens"; row labels lightly reworded for this table's columns; the bottom
three rows are this survey's measured result.) The
pattern that emerges: **what the panel holds at ceiling is the *categorical-entailment* defaults
(taxonomic, implicative, factive, lexical-result) and what it declines is the *defeasible*
defaults (Gricean implicature, aspectual completion) — and this cut runs orthogonal to the
verbal/nominal domain split.** There are now three held-at-ceiling *verbal* defaults, so the
M2 domain mismatch was a contingent feature of which defaults the project happened to try, not
a forced one.

## What this does and does not license

- **Does:** establish, with a verified gate, that **held-at-ceiling verbal lexical defaults are
  available** on this strict-NLI panel — three families clear B2 cleanly. This **refutes the
  un-findability reading of the open-question's "scarcity" horn**: a clean within-verbal
  generalization confirm of the conjecture is **not** blocked by the absence of a
  categorically-held verbal default. (The stronger *distributional* worry — that such defaults
  are rare among the ones a construction can cancel — is not settled, since the three families
  were picked as a-priori categorical inference types.)
- **Does not** test [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md):
  no cancel arm ran, no asymmetry was read, the conjecture's `tested` status and its weak,
  domain-mismatched confirm are unchanged by this calibration.
- **Does not** by itself unblock a within-verbal battery — that turns on whether a B2-passing
  family admits a clean **constructional** cancel (a coercion of the conative type that
  suppresses the held entailment), as opposed to a mere **lexical swap** or scopal/polarity
  flip. The design scrutiny (next section) finds that **two of the three families do not**, and
  one does — so a battery is **flagged, not licensed** here.
- **Does not** re-grind: the s135 for-durative and C1 completion arms are not re-run. The
  causative-inchoative family's eventual cancel (progressive/imperfective) is *aspectual* and
  thus near C1's territory, but the **default measured here is the lexical result-state
  entailment**, a different inference than C1's incremental-theme completion — and it holds at
  ceiling (1.00) exactly where C1's completion default floored (0/3). So this is a contrast with
  C1, not a repeat of it.
- **Does not** make a human comparison (`internal-contrast-only`), nor re-tune any threshold.

## Constructional-cancellability scrutiny (which B2-passer can actually serve a battery)

A B2-passing default helps the conjecture only if a **construction** (not a lexical swap)
suppresses it, so the held arm and a matched ADD arm can be compared at one task structure.
Reading off standard lexical semantics:

- **Implicative** — the natural "cancel" is a non-/negative-implicative matrix verb ("tried to",
  "failed to") or negation. "Failed to V" is a **lexical-class swap** (a different verb), and
  "didn't manage to V" is a **polarity flip** that still *entails* (¬V-ed), not a suppression to
  neutral. **No clean constructional cancel of the conative type.** Held, but does not serve.
- **Factive** — the "cancel" is a non-factive verb ("believed that P", "claimed that P"), again
  a **lexical-class swap**; the factive presupposition otherwise *projects* through negation and
  questions. **No clean constructional cancel.** Held, but does not serve.
- **Causative-inchoative** — here the natural cancel is **constructional and genuine**: the
  **progressive/imperfective** ("Sam was breaking the vase" ⊭ "the vase broke" — the imperfective
  paradox) suppresses the result-state entailment while keeping the *same verb*. This is the one
  family of the three that supplies both a held-at-ceiling verbal default **and** a same-verb
  constructional coercion that cancels it. **The strongest within-verbal battery candidate.**

## What happens next (a candidate unit, not a commitment)

The survey **flags** — it does not run — a concrete next empirical unit that could deliver the
clean within-verbal confirm the conjecture wants and discharge the M2 caveat:

1. **B2-calibrate the causative-inchoative progressive *cancel* suppression** off-ceiling, in
   the matched conflicting-cue paradigm of [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md)
   — i.e. *measure* that "was breaking the vase" actually suppresses "the vase broke" (the
   standing s135/C1 lesson: do not assume the construction cancels; measure it). The progressive
   is aspectual, so this is the leg most exposed to the C1-style finding that the panel treats
   aspectual coercion as weak — it must be measured, not presumed to work.
2. **Only on a clean cancel-suppression signal**, build a matched within-verbal battery pairing
   the frozen B2-passing resultative ADD arm (sha `80bd4b60b55a3e60`, reused verbatim) with the
   causative-inchoative progressive CANCEL arm, read by the frozen s134 thresholds. A positive
   asymmetry there would be the **clean within-verbal generalization confirm** — no domain
   mismatch — strengthening the conjecture beyond its current weak leg.

This is a legitimate future unit; it is not forced, and the conjecture's status does not move
until such a battery runs.

## Provenance

- Every figure is reproduced verbatim from `raw_calib/gate.json` and independently recomputed
  from the per-call `raw_calib/*.json` by a read-only post-run verifier (exact match; 108/108
  priced, 0 missing, 0 parse failures, 0 errors).
- The s135 / C1 / C2 ladder **numbers** are quoted verbatim from
  [`result/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md)
  and [`result/monotonicity-c1-completion-calibration-v1`](monotonicity-c1-completion-calibration-v1.md)
  (their row labels lightly reworded to fit this table's columns).
  The within-verbal limit and its two resolution paths are stated in
  [`open-question/within-verbal-cancel-at-ceiling`](../open-questions/within-verbal-cancel-at-ceiling.md).
- Spend: **$0.02482 billed** (UTC 2026-06-28), the survey calibration only; no battery run.
