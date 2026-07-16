---
type: result
id: particle-placement-givenness-mag
title: The verb-particle placement object-givenness FIREWALL effect now carries a within-model MAGNITUDE for the two confirming models — a third disjoint firewall-only arm (48 fresh-blind frames, session 238) pooled with v1+rep2 = 136 firewall frames gives a pooled within-frame given−new-mentioned split-preference shift of +0.037 (claude) / +0.055 (gemini), both bootstrap CI lower bounds above zero AND both fresh-48 blind arms independently clearing CI-LB>0 (gate 1 ∧ gate 2); gpt is a PERSISTENT, replicated SHADOW that does NOT lift at pooled N=136 (pooled +0.007, CI includes 0); the magnitude is SMALL (≈3.7–5.5 points out of 100, consistent with the claim's small-vs-end-weight fence) and firewall-specific (the shortcut-immune referential effect); this lifts the promoted claim's fence (j) from magnitude-absent to magnitude-attached (within-model, claude+gemini), the 2/3 scope + direction-only anchor unchanged
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-16
updated: 2026-07-16
links:
  - rel: depends-on
    target: conjecture/particle-placement-givenness
  - rel: depends-on
    target: design/particle-placement-givenness-v1
  - rel: refines
    target: result/particle-placement-givenness-rep2
  - rel: supports
    target: claim/particle-placement-givenness
  - rel: anchors
    target: resource/particle-placement-givenness-human-anchor
  - rel: depends-on
    target: source/kim-2016-particle-placement
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/shadow-depth-table-v4
---

# Result: the particle-placement object-givenness FIREWALL effect carries a within-model MAGNITUDE (powered pooled arm, 2/3)

> **Status: proposed (2026-07-16, session 238).** The **powered magnitude re-run** the s237
> instrument-line-continuation review named as the best available marginal dollar — *"a powered magnitude
> re-run on an already-promoted direction-only claim … a real strengthening, not a bar-placement tweak"* —
> for the one flagship production-side alternation genuinely lacking a magnitude. The promoted
> [`claim/particle-placement-givenness`](../claims/particle-placement-givenness.md) is `supported` but
> **direction-only** with **no within-model magnitude at all** (its fence **(j)**: *"no powered/pooled
> magnitude arm was run … A magnitude would be a future powered arm"*) — unlike the genitive (fence (i)
> attached s222) and the dative (attached s175). This run attaches it the genitive-mag way: a **third
> disjoint FIREWALL-ONLY arm** of **48 fresh frames**, every (verb,particle,noun) triple and object noun
> certified disjoint from **both** prior runs (48 fresh nouns, 0 of the 88 prior triples / 86 prior nouns),
> authored **blind**, then **pooled** with v1+rep2 → **136 firewall frames** for a bootstrap
> magnitude+interval. The instrument is byte-frozen (`probe.py`/`freq_control.json` sha-identical; the
> firewall context template-triple re-used byte-identical; `common.py` differs only in the documented
> budget constant); the pooling analysis (`analyze_merged.py`) was frozen in
> [`PREREG.md`](../../../experiments/runs/2026-07-16-particle-placement-givenness-mag/PREREG.md) before any
> model call, with a **fresh-agent pre-run critic GO** (verdict authority) that **weighed and over-ruled a
> non-Anthropic decorrelation vote NO-GO** on the merits (the double-gate defeats pooling inflation; the
> firewall is the *conservative* estimand, not the easiest; gpt handled first-class).
>
> **Outcome: MAGNITUDE ATTACHED (2/3).** For the two firewall-confirming models (claude, gemini), both the
> **fresh-48 blind arm** clears CI-LB>0 (gate 1) **and** the **pooled-136 interval** clears CI-LB>0 (gate
> 2). **gpt is a persistent, replicated SHADOW that does NOT lift at pooled N=136** (pooled +0.0067, CI
> includes 0) — the fence (b) SHADOW is **confirmed, not weakened**. This is a **reading-bearing** result
> and rests at `proposed`; the magnitude **support migrates to the claim layer**, where fence (j) is lifted
> from magnitude-absent to **magnitude-attached (within-model, claude+gemini)**.

## Why the FIREWALL, and why firewall-only

The magnitude the claim owes is on its **load-bearing, shortcut-immune referential effect** — the
byte-identical discourse-givenness **firewall** shift `shift2(frame) = mean(split-pref | GIVEN) −
mean(split-pref | NEW-MENTIONED)`, scored on **byte-identical** object strings (`the {noun}`) across
conditions so that any string-frequency / determiner-collocation / lexical-recency reader yields **zero by
construction** (certification check (2): all seven enumerated scored-string readers give within-frame shift
exactly 0). Arm 1 (definiteness) is confoundable — it is exactly where gpt shows a determiner shift that
does **not** survive the firewall — and Arm 3 (length) is a secondary convergent leg. So this run is
**firewall-only**, the exact inverse of the genitive-mag precedent (there the *typical* arm carried the
magnitude and the already-twice-replicated *firewall* was dropped; here the *firewall* carries it and the
already-twice-replicated *definiteness/length* arms are dropped). Reporting the firewall magnitude gives
the **smallest, most conservative** estimand — the confoundable definiteness arm would give a *larger*
number, and it is deliberately not the reported magnitude.

## The magnitude (the new content)

Per model, the within-frame firewall shift `shift2`, pooled across the three **mutually disjoint** firewall
arms (resampling unit = the frame, keyed by (run, frame_id)): v1 (40) + rep2 (48) + mag (48 fresh-blind) =
**136 pooled firewall frames**. Read with the pre-registered labels: **the pooled column is a magnitude
UPDATE conditional on the already-established direction — tighter by construction because 88/136 frames are
the data that set the direction — and the FRESH-48 blind column is the genuine fresh check** (foregrounded
per the non-Anthropic vote's condition).

| model | **FRESH-48 (blind check)** | prior-88 (v1+rep2) | **POOLED-136 (magnitude, conditional update)** | gate |
|---|---:|---:|---:|---|
| `claude-sonnet-4.6` | **+0.0351** [0.0211, 0.0487], 35/48, sign-p 0.0010 | +0.0372 [0.0252, 0.0497] | **+0.0365** [0.0272, 0.0459], 93/136 | ✅ ATTACH |
| `gemini-3.5-flash` | **+0.0385** [0.0135, 0.0635], 28/48, sign-p 0.156 | +0.0636 [0.0463, 0.0807] | **+0.0548** [0.0404, 0.0689], 94/136 | ✅ ATTACH (fresh-arm sign-p weak) |
| `gpt-5.4-mini` | −0.0006 [−0.0210, 0.0220], 18/48, sign-p 0.970 | +0.0107 [−0.0126, 0.0341] | +0.0067 [−0.0104, 0.0242], 60/136 | ❌ SHADOW (not gated; does not lift) |

- **Gate 1 (standalone fresh blind arm — the pre-registered attach bar).** Both confirming models' fresh-48
  arms independently clear **CI-LB > 0** (claude +0.0351 LB 0.021; gemini +0.0385 LB 0.014). So the attach
  does **not** rest on reusing the direction-establishing data.
- **Gate 2 (pooled interval).** Both confirming models' pooled-136 intervals clear CI-LB > 0 (claude
  +0.0365 [0.027, 0.046]; gemini +0.0548 [0.040, 0.069]).
- **The magnitude is SMALL — ≈3.7 (claude) / 5.5 (gemini) points out of 100.** This is the honest size of
  the shortcut-immune referential-givenness effect on the split-order preference, and it directly quantifies
  the claim's fence (c): *small vs the strongly-tracked end-weight/length constraint* (≈+0.31–0.40, 3/3). The
  panel tracks referential givenness **weakly but detectably**, end-weight **robustly**.
- **claude is clean and stable; gemini attaches with two honest caveats.** claude's fresh, prior, and pooled
  estimates coincide (+0.0351 / +0.0372 / +0.0365) with a decisive fresh sign test (35/48, p 0.0010). gemini
  meets the pre-registered CI-LB>0 gate on the fresh arm, but its fresh **frame-level sign test is not
  significant** (28/48, p 0.156) and its fresh magnitude (+0.0385) is **attenuated** below its prior
  (+0.0636); the pooled (+0.0548) sits between. Read gemini's magnitude as **attached but softer than
  claude's** — the CI-LB clears, the frame-consistency is weaker, shown not smoothed.
- **Modest cross-model decorrelation (~1.5×).** Pooled +0.0365 (claude) vs +0.0548 (gemini) — a ~1.5× spread
  between the two confirming models, milder than the genitive nonce firewall's ~3.6–4× (claim fence b) but
  real; displayed, never averaged into a panel scalar.

## gpt: the SHADOW does NOT lift at pooled N (a first-class disclosure)

The non-Anthropic pre-run vote flagged that *if* gpt's pooled firewall lifted at the larger N, the fence
(b) "SHADOW" framing would weaken and it must be reported first-class rather than as an afterthought. **It
did not lift.** gpt's fresh-48 firewall shift is essentially zero (**−0.0006**, 18/48, sign-p 0.970), and
its pooled-136 interval **includes zero** (+0.0067 [−0.0104, 0.0242]). So the pre-named, twice-replicated
gpt SHADOW is confirmed a **third** time and even at 136 pooled frames does not clear CI-LB>0 — the
determiner effect that gpt shows on the confoundable definiteness arm remains a surface/lexical shadow, not
information-structure tracking (claim fence b, **strengthened**). gpt is **not** part of any gate; its
estimate is reported as a displayed SHADOW, never folded into the 2/3 headline.

## The reviewers' gate (over-ruled vote, honoured conditions)

The two pre-run gates split — the fresh-agent critic (verdict authority) **GO**, the non-Anthropic vote
**NO-GO** — and are recorded in full at
[`REVIEW-critic-s238.md`](../../../experiments/runs/2026-07-16-particle-placement-givenness-mag/REVIEW-critic-s238.md)
(vote `gpt-5.4-mini` $0.002630,
[`VOTE-critic-s238.json`](../../../experiments/runs/2026-07-16-particle-placement-givenness-mag/VOTE-critic-s238.json)).
The vote objected on **presentation discipline**: (1) the pooled CI reuses 88 direction-establishing frames
→ misleadingly tight *if* the pooled is the headline; (2) dropping Arms 1 & 3 "narrows the estimand to the
easiest surviving leg"; (3) gpt's non-gated behaviour must be first-class. Per [`PROTOCOL.md §2`](../../../PROTOCOL.md)
the vote is signal to weigh, not a tiebreak; the critic weighed and **over-ruled on the merits**, and the
frozen PREREG already embedded the substantive asks — honoured verbatim here:

- **On (1):** the PRIMARY gate is the **FRESH-48 standalone blind arm** (gate 1); the pooled is reported as
  a **conditional update, tighter by construction**, with fresh-48-only and prior-88-only shown alongside.
  The magnitude is led by the fresh-48 blind estimate, not the pooled.
- **On (2):** the premise is **inverted** — the firewall is the *hardest, smallest, load-bearing* leg (the
  reported magnitude is ≈+0.037/+0.055, where the confoundable definiteness arm runs larger). Firewall-only
  is the **most conservative** estimand, the opposite of selective magnification.
- **On (3):** granted and delivered — gpt's non-lift is reported as a first-class section above, never
  folded into the headline.

## Method + provenance

- **Items** ([`build_items.py`](../../../experiments/runs/2026-07-16-particle-placement-givenness-mag/build_items.py),
  **certification PASS**, sha `181461b2…`): 48 fresh firewall-only frames — a subject name (none the
  monitor's), a separable transitive phrasal verb (past tense) + particle from the frozen 38-pair set, a
  concrete inanimate count-noun object; every (verb,particle,noun) triple and object noun **disjoint from
  both v1 AND rep2** (check (D), extended to v1 ∪ rep2: 0 shared triples, 0 shared nouns, 48 distinct
  nouns); the firewall context template-triple re-used **byte-identical** (certified parallel: 2 clauses,
  1 comma, 14 words, object noun 1/1/0 in given/newment/new, no verb-particle / heavy-NP leak); all seven
  enumerated scored-string shortcut readers give within-frame firewall shift **exactly 0** (check (2)).
- **Instrument:** byte-frozen `probe.py` (`eb50f881…`) and `freq_control.json` (`cd472475…`, carried only
  to satisfy the freeze gate — the firewall-only analysis never reads the Arm-1 covariate); `common.py`
  differs only in `HARD_STOP_USD` (a budget constant).
- **Run:** 288 firewall trials × 3 models = **864 calls, $1.658902 billed, 0 NA, 0 missing** (liveness
  $0.003389 separate; run total $1.662291). The run **halted once** at the initial `HARD_STOP_USD = 1.60`
  partway through gpt (claude billed pricier than the pre-flight: $1.021 vs ~$0.71); the budget-only
  constant was raised **1.60 → 2.00** (frozen shas unchanged, **blind through the halt** — no analyze run,
  no raw peeked; the s225→s226 precedent) and gpt resumed crash-safe. Panel = the standing ratified roster
  (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`).
- **Post-run verification:** an independent fresh-agent verifier recomputed the fresh-48, prior-88, and
  pooled-136 firewall magnitudes from the raw jsonl with its own script and a different bootstrap seed
  (12345), and re-checked the row counts, disjointness, verdict logic, sign tests, and billed cost →
  **REPRODUCED** (all nine per-model point estimates match to 4 dp; every CI-LB sign agrees; the
  MAGNITUDE-ATTACHED verdict + gate logic + gpt-does-not-lift confirmed; 288 firewall-only rows/model, 0
  NA; blind-scoring confirmed — `analyze_merged.py` committed only in the pre-run freeze, no post-run
  edits).

## What this result does and does not say

- **Does:** attach a **within-model magnitude** to the particle-placement discourse-givenness **firewall**
  effect for the two confirming models — a pooled within-frame given−new-mentioned split-preference shift of
  **+0.0365 [0.027, 0.046]** (claude) and **+0.0548 [0.040, 0.069]** (gemini), each independently clearing
  CI-LB>0 on 48 fresh blind frames. This **lifts claim fence (j)** from magnitude-absent to
  magnitude-attached (within-model, 2/3).
- **Does NOT:** change the **2/3 scope** (gpt is a persistent, replicated SHADOW that does not lift at
  pooled N — fence b, strengthened); change the **direction/anchor scope** (the human anchor is a
  restatement of the native-speaker direction only; the magnitude is a **within-model** contrast, not a
  human comparison of sizes — Kim/Gries give no model-scale effect size); make the effect large (it is
  **small vs end-weight**, fence c); defeat the distributional-shadow explanation (the firewall excludes
  scored-string shortcuts + object-noun recency, nothing stronger — fence i); or make the replication
  temporally/version-robust (fence h). The 2/3 direction remains the promoted claim; this run **sizes** the
  shortcut-immune effect for the two members that carry it.
