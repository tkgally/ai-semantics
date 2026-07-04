# AANN behavioral gradient — rep2 (second-date, fresh-item powered replication)

**Session 178, 2026-07-04.** The A2a owed cross-date powered re-run of the AANN anchored
acceptability gradient — the "overall positive" whose only gap in
`wiki/findings/claims/aann-behavioral-gradient.md` was "no second-date replication."

## What it is

The **byte-identical frozen v2 instrument** (`probe.py` sha `ec8f7334…`, `analyze.py` sha
`4ce5a709…`, both `diff`-identical to `../2026-06-12-aann-behavioral-probe-v2/`) on a **fresh,
disjoint** sample:

- Seed 20260612 → **20260704**.
- Anchored arm drawn **disjoint from v2**: v2's two items per (adjective × noun-class) cell are
  removed from the candidate pool before the seeded pick → **408 anchored items, 0 shared surface
  items with v2** (asserted in `prep.py`; every cell retained ≥4 candidates).
- Human anchor (`human_cell_means.csv`, `human_class_means.csv`) computed from ALL 3,600 Exp-2
  ratings → **byte-identical to v2** (same yardstick, verified by `diff`).
- Held-out (60) and Tier-0 (24) arms are lexically frozen → byte-identical items to v2 (a
  same-items second-date re-run; A/B Tier-0 positions reseed, scored via `aann_position`).

Mirror: MIT `github.com/mahowak/aann-public`, commit `c8095a0`, re-cloned + verified this session
(regenerating v2's stimuli with the OLD seed reproduces the committed `stimuli.json` byte-identically).

## Result

`analyze.py` → **SUPPORTED** (via A + C; B Tier-0-excluded at 18/24). 1,782 calls, **$0.3092
billed**, **0 missing in every arm**. The anchored gradient replicates cross-date on fresh items for
all three models (cell ρ 0.692 / 0.702 / 0.735; every CI overlaps v2). See
`wiki/findings/results/aann-behavioral-gradient-rep2.md` for the full read, including the honest
wrinkle that gpt's Tier-0 formal preference dropped below threshold on the marginal objects/evaluative
items while its graded gradient stayed undiminished.

## Files

- `PREREG.md` — frozen before any model call.
- `prep.py` — data prep (no model calls); seed 20260704, disjoint-from-v2 anchored draw.
- `probe.py`, `analyze.py` — byte-identical copies of the v2 instrument.
- `stimuli.json`, `human_cell_means.csv`, `human_class_means.csv` — frozen inputs.
- `raw/` — per (model, arm) responses + `run.log` + `cost-log.txt`.
- `results.json` — analysis output.
- `prerun_vote.json`, `vote_script.py` — the non-Anthropic decorrelation pre-run vote.

## Gates

Pre-run critic **GO**; non-Anthropic vote (`openai/gpt-5.4-mini`) **GO-WITH-CONDITIONS** ($0.002071,
all conditions honored); liveness 3 calls $0.000495; post-run verifier (see result page).
