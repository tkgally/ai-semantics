# within-lexical-scalar-vs-disjunctive-v1 — run handoff

**BUILT + FROZEN, NOT RUN (2026-06-23).** No probe was run and no spend was opened in the build.

One frozen lexical commitment instrument (`SAME/DIFFERENT/UNCLEAR` + 0–100 confidence, inherited
verbatim from the cross-level lexical leg) applied identically to two within-lexical arms that
differ only in ambiguity **kind**, level held fixed:

- **Arm 1 (scalar)** — DWUG bridging vs clear controls (usage-similarity-capped). MANIFEST →
  `items_arm1.json` → `../lexical-bridging-context-v1/stratum.csv` (sha `e7d36773…`).
- **Arm 2 (disjunctive)** — author-built balanced-homonym vs clear controls
  (`internal-contrast-only`). `items_arm2.json` (committed; original text).

Gate: [`wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md`](../../../wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md)
(ADOPT DEFAULT: Option B + Q2-b + nuisance-matching freeze). Design doc:
[`../within-lexical-scalar-vs-disjunctive-v1.md`](../within-lexical-scalar-vs-disjunctive-v1.md).

## To run (a later, spend-bearing session)

1. **Fresh independent pre-run critic GO/NO-GO** against the frozen `instrument.json`
   (`instrument.sha256`) + `freeze_manifest.json`. A NO-GO **defers** the run; it does not relax
   any band. The critic should scrutinize, especially, the **balance** of each Arm-2 disjunctive
   context (no hidden tie-break) and the nuisance-match record.
2. **Budget pre-flight** per [`config/budget.md`](../../../config/budget.md): est. **$0.10–0.25**;
   `ABORT_USD=0.60`.
3. **Stage Arm-1 fulltext** (gitignored, recipe-not-corpus):
   `python3 ../lexical-bridging-context-v1/prep.py` (DWUG EN, archive sha `64eef477…`, 48/48
   stratum remap → `experiments/data/dwug/lexical_bridging_v1_fulltext.jsonl`). Or run Arm 2 alone
   with `--skip-scalar`.
4. `python3 certify.py` (no API; expect 15/15 PASS), then
   `OPENROUTER_API_KEY=… python3 probe.py --run --i-have-pre-run-critic-go`, then
   `python3 analyze.py`.

## Reading rule (frozen, `analyze.py`)

Per model, on the **disjunctive** arm:

- **COLLAPSE** = disjunctive within-arm decline-gap CI lower bound > 0 (decline elevated over its
  own clear controls). Within-arm → robust to the register residual. Supports the kind-reading.
- **SURVIVAL** = within-arm gap not elevated **and** cross-arm gap (disjunctive − scalar bridging)
  CI includes 0 **and** disjunctive decline near-zero (≤ 0.10). **Higher bar** (the register
  residual cuts toward survival). Supports the layer-reading.
- **MIXED/INCONCLUSIVE** = otherwise, or C3 fails for an arm, or N too thin.

## Files

- `instrument.json` (+ `.sha256`) — the C2-frozen shared instrument (inherited verbatim).
- `items_arm2.json` — author-built disjunctive-homonym items (committed).
- `items_arm1.json` — manifest → frozen DWUG bridging stratum (no corpus text).
- `nuisance_match.json` — the frozen register/length/frequency/frame match record.
- `freeze_manifest.json` — sha256 freeze of instrument + items_arm2 + nuisance_match + Arm-1 stratum.
- `build_arm2.py` — author + freeze Arm 2 (deterministic, no API).
- `certify.py` — build-time structure/balance/leak/nuisance checks (no API).
- `probe.py` — refuses without `--run --i-have-pre-run-critic-go`; `ABORT_USD=0.60`.
- `analyze.py` — the frozen survival/collapse reading rule (10000-rep clustered bootstrap, seed 20260623).
- `raw/` — created at run time (Arm-1 raw carries NO DWUG corpus text: item-id + class + cluster only).
