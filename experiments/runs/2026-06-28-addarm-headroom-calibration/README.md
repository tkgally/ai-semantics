# Run record — add-arm headroom calibration (2026-06-28, session 133)

**Pre-registration (frozen):** [`PREREG.md`](PREREG.md)
**Frozen items:** `experiments/data/addarm-headroom-calibration/items.csv`, sha256[:16] **`471a5940ba8f65ff`** (built + committed before any probe call).
**Discharges the s132 BLOCKER (prerequisite 1)** on [`decisions/open/constructional-monotonicity-generalization-operationalization`](../../../wiki/decisions/open/constructional-monotonicity-generalization-operationalization.md); design-level companion [`open-question/constructional-monotonicity-addarm-headroom`](../../../wiki/findings/open-questions/constructional-monotonicity-addarm-headroom.md).
**Result page:** [`result/addarm-headroom-calibration-v1`](../../../wiki/findings/results/addarm-headroom-calibration-v1.md).
**Human anchor:** none — `internal-contrast-only` (a within-model construction-vs-control feasibility measurement; no human-comparison claim).

## What ran

For two candidate ADD constructions, the no-cue **licensing gap** per verb: a `construction` arm (sentence WITH the construction) and a `control` arm (bare verb + same arguments, construction removed), both asked the **same** added-entailment hypothesis. `affirm` = NLI label 0 (entailment) | FC YES. 48 items × {NLI, FC} × 3 models = **288 calls**, temperature 0, the 3-family panel (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash; gemini `reasoning:{effort:minimal}`).

## Frozen gate (PREREG)

A verb is **headroom-clean** (panel aggregate, NLI primary) iff construction affirm ≥ 0.80 AND control affirm ≤ 0.40. A construction **demonstrates headroom** iff ≥ 4/12 verbs are clean AND ≥ 1 is clean in ≥ 2/3 models. Frozen before data; read mechanically by `analyze.py`; falsify arm live.

## Result

**Both candidate constructions DEMONSTRATE HEADROOM** — the s132 degeneracy worry is **not** borne out (for the resultative it is refuted), and the trap it warned of is real but **verb-specific and avoidable**.

| construction | mean construction affirm (NLI) | mean control affirm (NLI) | headroom-clean (aggregate) | clean in ≥2/3 models | trap verbs (control at/near ceiling) | demonstrates headroom |
|---|---|---|---|---|---|---|
| resultative | **1.000** | **0.250** | **10/12** (beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe) | 10 | freeze (1.00), sharpen (1.00) | **YES** |
| intrans-motion | **0.972** | **0.333** | **7/12** (bob, float, rock, roll, spin, twirl, wobble) | 8 (+sway) | drift (1.00), slide (1.00), swing (1.00), bounce (0.67) | **YES** |

- **Resultative is not degenerate.** Construction licensing is at ceiling (1.0) and the bare-transitive control is *off* ceiling for 10/12 verbs (e.g. "hammered the metal" does NOT entail "the metal became flat"; "kicked the door" does NOT entail "the door became open"). Even `wipe`/`scrub` — predicted as plausible traps — came back off-ceiling (control 0.00 / 0.33). Only the genuinely telic `freeze→solid` and `sharpen→sharp` had controls already at ceiling (the trap end of the spectrum, present by design).
- **Intrans-motion also works** as an alternative add arm (7–8/12 clean). Trap verbs are the displacement-encoding ones (drift, slide, swing, bounce); the pure manner verbs (spin, float, bob, wobble, rock, twirl) have full headroom. `sway` missed on the *construction* side (0.67) — the "swayed toward the door" weakness the pre-run critic flagged (a conservative miss, not a control-trap).
- **FC tracks NLI and is marginally cleaner** (resultative ctl 0.111; intrans ctl 0.306), so the NLI verdict is conservative — no instrument fragility flips the headroom call.

## Cost

**$0.06833 billed** (API `usage.cost`, 288/288 priced, 0 missing): claude $0.04198, gpt $0.01031, gemini $0.01605. **0 parse failures** (0 NA on NLI or FC, all 3 models). Elapsed ≈ 184 / 114 / 116 s.

## Discipline

- Items frozen + sha256-hashed (`471a5940ba8f65ff`) + committed **before** the first call; hash re-verified at launch.
- Independent fresh-agent **pre-run critic → GO** (no BLOCKERs; two `toward`-PP SHOULD-FIX items [im-sway, im-drift] + a `sharpen…sharp` NIT, all judged to only conservatively understate headroom; ran as frozen and reported as caveats — borne out: sway missed on construction side exactly as predicted).
- Independent fresh-agent **post-run verifier → PASS**: every headline number recomputed from `raw/*.json` by a separate route, exact match; cost re-summed to $0.06833; 0 parse fails; no stuck-model pathology.

## Files

- `build_items.py` — emits + hashes the frozen item set.
- `probe.py` — runner (NLI + FC × 3 models) using `experiments/lib/openrouter.py` (records billed `usage.cost`).
- `analyze.py` — affirm rates per arm/verb/construction; applies the frozen gate; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`; `raw_run.log` the console transcript.

## What this does and does not license

- **Does:** demonstrate that a non-degenerate add arm with genuine licensing-no-cue headroom **can be built** for both candidate constructions (verb-selected away from the telic/displacement trap verbs) — discharging the s132 review's load-bearing blocker. It also gives the operationalization decision a concrete usable verb pool and a verified trap-verb exclusion list.
- **Does not:** test the monotonicity conjecture (it measures only feasibility, not add-vs-cancel); make any human comparison (`internal-contrast-only`); or ratify the operationalization decision (that remains a later session's independent adversarial review, which still owes prerequisites 2–4). Small-N (12 verbs/construction), single run, panel-as-instrument; bare-transitive is one control framing.
