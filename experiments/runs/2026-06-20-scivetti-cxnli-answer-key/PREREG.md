# PRE-REGISTRATION (FROZEN) — Scivetti CxNLI answer-key probe

**FROZEN 2026-06-20 after independent pre-run critic GO (fresh agent, verdict GO on points A-E).** Instrument, stimuli sha `1c5cffb18c5ef78e`, and analysis are now fixed; no edits past this point.

## 1. What this run is

The long-deferred **answer-key** test the resource page
[`resource/scivetti-2025-cxnli-dataset`](../../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)
has flagged since 2026-05-29 ("the next step is to actually run a probe… compare
panel-model NLI labels against the per-item gold labels and report against the
aggregate ≈0.90 human baseline"). Every prior CxG probe (caused-motion, conative,
way, comparative-correlative) used the project's **own synthetic minimal pairs** and
internal contrasts; **none** has ever been scored against the dataset's actual
human-annotated items. This run does exactly that.

- **Task.** Zero-shot 3-way NLI (0 entailment / 1 neutral / 2 contradiction) on the
  **full** Experiment-1 test set (`CxNLI_3_examples_test.tsv`), 390 items, balanced
  130/130/130 across the three gold labels, 8 constructions.
- **Panel.** A = claude-sonnet-4.6, B = gpt-5.4-mini, C = gemini-3.5-flash (the frozen
  panel). Temperature 0; gemini reasoning `effort: minimal`.
- **Score.** Per-item accuracy vs the released gold label; per-construction accuracy +
  Wilson 95% CI; overall accuracy vs the human native-speaker baseline **0.90**.

## 2. Anchor & governance — why no new decision is owed

- **Human anchor RATIFIED 2026-05-29 (Tom)** for the four CxG conjectures, as a
  per-item **answer key** (human-licensed gold labels over those exact constructions)
  plus the aggregate ≈0.90 native-speaker accuracy. This run *is* that ratified
  comparison; it does not introduce a new anchor or a new conjecture.
- **Indicator REUSED VERBATIM.** `NLI_SYS` + `parse_nli` are byte-identical to
  `conative-cancel-probe-v2` / `conative-preference-commitment-v1`, and the dataset's
  own 0/1/2 scheme matches the instrument exactly. No indicator is invented or tuned.
- **No item-selection latitude.** The full released test set is used; we do not select,
  filter, or re-weight items, so the operationalization gate's chief cheat-surface
  (item selection) is structurally absent.
- **Gold labels are NOT shown to the model.** Only premise + hypothesis are sent.
- Therefore **no `decisions/open/` entry is owed** — the yardstick is already fixed.
  (An independent pre-run critic confirms this is an honest read, GO/NO-GO.)

## 3. Frozen stimuli

- Source: `github.com/melissatorgbi/beyond-memorization` @ commit `82699473`, file
  `data/CxNLI/CxNLI_3_examples_test.tsv` (no upstream license file → recipe-not-corpus:
  gitignored under `experiments/data/scivetti/`; only the hash-manifest is committed).
- `stimuli-manifest.json` sha256[:16] = **`1c5cffb18c5ef78e`** (390 items; per-label
  130/130/130; per-construction causative-with 54 / caused-motion 36 /
  comparative-correlative 30 / conative 78 / intransitive-motion 69 / let-alone 24 /
  resultative 66 / way-manner 33). `python3 prep.py --check` reproduces this hash;
  `probe.py` re-verifies it against the manifest before any spend.

## 4. Pre-specified analysis (frozen in `analyze.py`, `--selftest` PASS)

1. **Headline (human-anchored, the four ratified constructions + overall).** Per-model
   overall accuracy + Wilson 95% CI vs the human 0.90 baseline → verdict
   {ABOVE / MATCHES / BELOW the human baseline}. Per-construction accuracy + CI for all
   8, with the four ratified-anchor constructions flagged. The human-comparison **claim**
   is scoped to the four ratified constructions + the dataset-level overall accuracy;
   the other four are reported descriptively (same human-annotated release, no
   individually-ratified conjecture).
2. **Confusion + parse integrity.** 3×3 gold-vs-pred confusion; unparseable/missing
   count reported, never silently dropped (a None is scored WRONG and counted).
3. **Add-vs-cancel (descriptive only; for `conjecture/constructional-monotonicity-
   asymmetry`).** Accuracy on ADD (caused-motion ∪ way-manner) vs CANCEL (conative),
   per model. **Explicitly CONFOUNDED by baseline difficulty** — this is *not* the
   matched-difficulty/ceiling-controlled confirm test the conjecture requires; it bears
   as **suggestive** evidence at most, and a gap in the predicted direction is reported
   as consistent-with, never as confirmation.

## 5. What would count as what (stated before the run)

- **Headline finding** is purely descriptive-comparative: *does the panel reach the
  human native-speaker NLI accuracy on these constructions, and where does it fall
  short?* There is no "hoped-for" direction; a BELOW result and an ABOVE result are
  equally reportable. The four-construction scoping and the 0.90 yardstick are fixed
  here and not re-touched after seeing data.
- **Contamination caveat (recorded now).** The items derive from public corpora and the
  dataset is on GitHub, so panel models may have seen them. Contamination would
  **inflate** model accuracy, so a *shortfall* below 0.90 is the robust signal; a match
  cannot by itself distinguish competence from memorization. This caveat is load-bearing
  and will appear on the result page.

## 6. Cost

Pre-flight: 390 × 3 = 1170 single-label NLI calls. Measured single-label cost ≈
$0.00015/call (AANN inferential runs) → **≈ $0.18–0.25** (premises are full sentences,
a touch longer). `ABORT_USD = 0.60`. Under the $2.50 single-run flag; day headroom ample.

## 7. Post-run verification

An independent fresh-agent verifier re-parses `raw/`, recomputes the accuracies + Wilson
CIs from the labels, confirms the billed `usage.cost` sum, and checks for any material
discrepancy before the result page is finalized.
