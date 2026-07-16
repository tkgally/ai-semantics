# REVIEW — Post-run verification, BLiMP R1 C4-frequency-matched content-word-swap arm (A3b, s235)

*Independent fresh-agent post-run verifier. Recomputed every headline figure from `raw/` with my OWN
script (independent bootstrap seed **20260716**, ≠ the run's frozen 20260715); did NOT import
`analyze_swap_c4.py` — I re-derived correctness as `(choice == good_pos)` from every raw row. $0
verification, no model calls.*

## VERDICT: **REPRODUCED**

All headline point estimates reproduce **exactly to 4 dp**; all bootstrap CIs match to within seed
jitter (≤ 0.002); the four-outcome call reproduces as **STILL-INCONCLUSIVE**; adequacy gate, attrition,
coverage, cancellation flag, and instrument-failure guard all reproduce.

### Per-model Δ̄ / CI — reported vs my independent recompute (seed 20260716, BOOT=5000)

| Model | Stratum | Reported Δ̄ / CI | My recompute Δ̄ / CI | n |
|---|---|---|---|---|
| A (claude) | shallow | −0.0294 [−0.0484, −0.0121] | −0.0294 [−0.0502, −0.0121] | 289 |
| A (claude) | deep | −0.0717 [−0.0950, −0.0483] | −0.0717 [−0.0967, −0.0483] | 300 |
| B (gpt) | shallow | −0.0329 [−0.0536, −0.0156] | −0.0329 [−0.0536, −0.0156] | 289 |
| B (gpt) | deep | −0.0567 [−0.0917, −0.0233] | −0.0567 [−0.0900, −0.0217] | 300 |
| C (gemini) | shallow | −0.0260 [−0.0450, −0.0104] | −0.0260 [−0.0450, −0.0104] | 289 |
| C (gemini) | deep | −0.0417 [−0.0633, −0.0217] | −0.0417 [−0.0633, −0.0200] | 300 |

Point estimates identical to 4 dp (deterministic); CI endpoints differ only in the 3rd–4th decimal from
the independent seed, as expected. ans1 / poslock reproduce exactly: A 0.3909 / 0.2217, B 0.4868 / 0.1570,
C 0.4380 / 0.1358. Deep n=300, shallow n=289 per model — confirmed. Call accounting: 2356/model (7068
total); `determiner_noun_agreement_1` carries 356 rows (89 usable pairs × 4), all other paradigms 400.

### The crux — deep CI-upper vs the strict −0.05 drop rule (why INCONCLUSIVE, not DROPS)

The frozen s210 drop rule requires the **whole** deep CI ≤ −0.05, i.e. **both** Δ̄ ≤ −0.05 **and**
CI-upper ≤ −0.05. Per model:

| Model | deep Δ̄ | Δ̄ ≤ −0.05? | deep CI-upper | CI-upper ≤ −0.05? | drops? |
|---|---|---|---|---|---|
| A | −0.0717 | YES | −0.0483 | **NO** (−0.048 > −0.05) | False |
| B | −0.0567 | YES | −0.0217 | **NO** | False |
| C | −0.0417 | **NO** | −0.0200 | NO | False |

**0/3 satisfy the strict drop rule** (< 2/3 needed for DEEP-STILL-DROPS). A's point estimate is a real
deep drop (−0.072) but its CI-upper (−0.048) creeps just above −0.05; B's upper is far above; C fails even
the point-estimate leg. For DEEP-SWAP-STABLE, every model's deep CI reaches below −0.05, so no model has
deep within ±0.05 → 0/3 (< 2/3). Neither pole fires ⇒ **STILL-INCONCLUSIVE** is the correct, conservative
landing. Reproduced.

## B4 attestation — BLIND-SCORING LOCK (BLOCKER 4): PASS

I attest, from code + git, that the scorer was frozen before any model call and was not tuned on outputs:

- `analyze_swap_c4.py` (scoring + exclusion criteria + the four-outcome decision table) was committed at
  the **s232 freeze** (commit `162a0bf`, alongside `PREREG.md`, `build_swap_c4.py`,
  `build_disjoint_sample.py`, `probe.py`) — **before** any build or probe existed.
- The scorer is **byte-identical** between the s232 freeze (`162a0bf`) and the s235 run commit
  (`6e208ab`): `git diff 162a0bf 6e208ab -- analyze_swap_c4.py` is **empty**, and `git diff HEAD` on the
  working copy is empty. The build outputs (`items_swap_c4.json`, `selection_c4.json`) were added only at
  `6e208ab`, i.e. **after** the scorer + decision table were frozen.
- The four-outcome table in code (adequacy-gate-first → DROPS → STABLE → INCONCLUSIVE) matches the PREREG
  Q3-A map verbatim, with symmetric ±0.05 bands on the refusing (DROPS) and candidacy (STABLE) poles.
- **FV2 bundle integrity:** current shas match the recorded `postrun_shas.txt` exactly —
  `items_swap_c4.json` `8bc762…`, `selection_c4.json` `cf396b…`, `analyze_swap_c4.out` `c857af…`; the
  raw/ per-file-sha digest reproduces the recorded `6ba6f5…`. `disjoint_sample.json` carries the
  PREREG-certified `sample_sha256 1f90050c…` under `SEED=20260715`. No after-the-fact edits.
- No sign of any post-hoc scorer tuning: no accuracy targets in the build, no seed to scan (per-position
  substitute selection is seed-free by construction; the only seed 20260715 is the pre-announced disjoint
  draw), and the interpretive prose is uniformly deflationary. **No human-readable intermediate output
  needed to have been inspected to fix any figure — nothing was retuned.** Attestation: PASS.

## F5 attestation — INSTRUMENT-FAILURE guard: DID NOT FIRE (read is valid)

I independently computed the s205 guard (poslock > 0.50 **AND** |ans1 − 0.5| > 0.40, on ≥ 2/3):

| Model | poslock | poslock > 0.50? | |ans1 − 0.5| | > 0.40? | guard? |
|---|---|---|---|---|---|
| A | 0.2217 | NO | 0.1091 | NO | no |
| B | 0.1570 | NO | 0.0132 | NO | no |
| C | 0.1358 | NO | 0.0620 | NO | no |

The guard fires on **0/3** — neither leg of the AND is met for any model. `instrument_failure = False`,
reproduced. I attest that had the flag fired (2AFC collapsed to position-answering), it would **VOID** the
accuracy read regardless of the Δ̄ verdict; it did not, so the STILL-INCONCLUSIVE read stands.

## Unparsed-answer handling — symmetric, non-cheating, immaterial

5 unparsed answers, all model A, all in the **swap** condition of deep paradigms
(`sentential_negation_npi_scope` pair 22 ×1; `only_npi_scope` pairs 271/17/683/816 ×1 each; B and C have
0 unparsed). Handling: an unparsed row (`choice=None`) is dropped from that pair's **order-average only**;
the pair survives whenever any order remains in both conditions. All 100 deep pairs/paradigm survive
(deep n=300, not reduced). The rule is applied identically to every trial irrespective of
condition/correctness — non-cheating. **Materiality:** A deep Δ̄ as scored (order-drop) = −0.07167;
recomputed dropping the 5 affected pairs entirely = −0.06949 — a 0.00218 shift, within bootstrap jitter,
changing no verdict (and if anything the retained handling makes A's deep drop marginally *larger*, still
short of the strict CI-upper ≤ −0.05 rule).

## cancellation_flag (S6) — confirmed, and correctly a REPORT not a gate

Reproduced from the build's per-sub `sub_c4` records (n_subs=1276): signed set-mean C4 gap **+0.0106**
(|·| ≤ 0.05 → **ADEQUATE**, so the B3 hard gate passes and a DROPS/STABLE read is licensed); per-word
mean|gap| **0.1539** (> 2×0.05); frac_swap_rarer **0.5251**, frac_swap_commoner **0.4483** (min 0.4483 >
0.30) ⇒ `directional_cancellation_flag = True`. Confirmed. Per PREREG S6 + the freeze disposition, S6 is a
**visibility/caution flag, not a gate**: the small set-mean is achieved partly by within-band per-word gaps
of both signs, but the hard adequacy verdict (B3) is the signed set-mean alone (+0.0106) → the flag does
**not** change the ADEQUATE call. Correctly disclosed, correctly non-gating.

## Coverage / attrition / adequacy — reproduced

Coverage all ≥ 0.50 floor (min 0.683 `regular_plural_subject_verb_agreement_1`) → 0 exclusions. All 6
paradigms kept; deep-3 all ≥ USABLE_FLOOR 60 (usable-min-over-slots = 100/100/100 deep) →
attrition_inconclusive=False. C4 stream 22,329,495 sentences (3 shards), mode dual — all as reported.

## Cost / provenance

Authoring-session billed spend reproduces from raw `usage.cost`: A $0.8170, B $0.2104, C $0.2842, **total
$1.3116** (≈ reported $1.312). **This verification made $0 in model calls** (pure recompute from committed
`raw/` + frozen instrument).

## Bottom line

**REPRODUCED.** Every headline figure recomputes exactly (points to 4 dp; CIs within seed jitter), the
STILL-INCONCLUSIVE four-outcome call is correct, the crux is the strict whole-CI ≤ −0.05 drop rule (0/3
deep CI-uppers reach −0.05, so no DROPS; every deep CI reaches below −0.05, so no STABLE), the B4
blind-scoring lock and F5 instrument-failure attestations both PASS, unparsed handling is symmetric and
immaterial (0.002 shift), and the S6 cancellation flag is a correctly-disclosed non-gating caution. No
discrepancies.
