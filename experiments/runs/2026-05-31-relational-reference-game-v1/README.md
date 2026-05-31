# relational-reference-game-v1 — run record

The two-AI iterated dyadic reference-game pilot (Decision 9 = GO). Builds + runs the design in
`wiki/findings/open-questions/relational-meaning-pilot.md` under
`wiki/decisions/resolved/relational-pilot-go.md`. Frozen design + decision rule: `PREREG.md`.
Operationalization surfaced in `wiki/decisions/open/relational-pilot-operationalization.md`.
Finding: `wiki/findings/results/relational-reference-game-v1.md`.

## Headline — a first-class RELATIONAL NULL (deflationary), across all three models

History **content** helps a fresh matcher resolve an opaque coined nickname (coined_only→ordered
lift **+0.25 to +0.42**, load-bearing), but the **order** of that history does **not**
(ordered−shuffled gap **+0.06 to +0.11**, no model's clustered-bootstrap CI excludes 0; `reversed`
is no better than — slightly *below* — `shuffled` in every dyadic cell, so the tiny ordered edge is
not chronology-specific). The coined convention is recovered from the **set** of prior
turns, not their **ordered trajectory** → coordination, not constitution. The deflationary
distributional story survives order-scrambling. Written as a first-class negative, not retuned.

Secondary (anchored to `resource/hawkins-tangrams`): the LLM dyads converge on referential
**success** (accuracy → ~1.0 over reps) but do **not compress expression length** like humans
(words flat ~8.5–10.8 across reps vs the human curve 7.73→4.10) — convergence without entrainment.

## Files

- `build_figures.py` → `figures.json` — 6 hard-to-name 8×8 grid referents, 3 confusable near-twin
  pairs, deterministic (seed 20260531). **sha256 of figures.json content =
  `a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4`** (pinned in PREREG; frozen +
  committed before any finding-bearing call).
- `game.py` — engine: live homogeneous-dyad game, opaque-nickname elicitation, four-arm replay probe
  (`coined_only`/`ordered`/`reversed`/`shuffled`×3), single-agent monologue baseline. `liveness` /
  `preflight` / `full` modes. Stateless calls (all memory serialized to prompt text) → exact shuffle.
- `analyze.py` → `analysis.txt` — entrainment vs Hawkins; per-coined-term cluster accuracies;
  history_lift interpretability gate; ordered−shuffled gap (clustered bootstrap CI); chronology guard
  (ordered vs reversed); monologue floor; pre-registered verdict.
- `raw/results.json` — every call (prompt-derived fields, raw reply, parsed pick, billed usage).

## Run facts

- Panel (homogeneous dyads): claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash (`config/models.md`).
- 3 models × 2 games × (K=6 figures, R=5 reps) + nicknames + 4-arm probe + monologue baseline.
- **864 records, $0.94544 billed** (claude $0.583 / gpt $0.117 / gemini $0.245; `usage.cost` summed,
  0 missing). Under the $5 single-run flag and the $20/week cap.
- **14 pick-parse-fails, ALL claude** — chatty replies that overran the 64-token matcher cap before
  emitting a label; scored as wrong. Spread across arms (shuffled 5 / live 4 / ordered 2 /
  coined_only 2 / reversed 1) roughly in proportion to trial counts, so they add noise but do **not**
  bias the ordered-vs-shuffled contrast (and the headline is a null, not a fragile positive). 0 NA
  for gpt/gemini.
- Gemini ran at `reasoning: effort=minimal` (required on this endpoint; the ledger's dominant cost
  driver), constant across all gemini calls → a within-gemini condition, not a cross-arm confound.

## Reproduce

```
python3 build_figures.py     # regenerate figures.json (deterministic) + print sha256
python3 game.py full         # re-run (temp 0; provider non-determinism may perturb a few cells)
python3 analyze.py           # recompute every figure in analysis.txt
```

## Discipline

Independent pre-run critic (caught the self-describing-coined-term BLOCKER → forced the opaque
nickname + `coined_only` diagnostic + `reversed` control before any finding-bearing call) +
independent post-run verifier (reproduced every figure from raw). Stimuli frozen + committed
(sha256) before the run. Trajectory measure is the pilot's own **internal within-model contrast**
(NOT anchored by Hawkins, per `decisions/resolved/relational-fetchable-anchor`); the entrainment
curve is the only Hawkins-anchored (human-comparison) measure.
