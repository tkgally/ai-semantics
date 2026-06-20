# 2026-06-20 — let-alone forced-decomposition (uptake-inducing) probe

**Uptake-inducing follow-up** to `2026-06-20-scivetti-let-alone-working-surface` (session
58). Session 58 *offered* a working surface and 2/3 models lifted to the human ≈0.90
baseline on the near-chance phrasal-scalar **let-alone** items — but gpt-5.4-mini largely
**declined** the offer (16/24 bare one-token answers, median 8 completion tokens), so its
persistence was **channel-not-taken-up**, not a clean channel-controlled survival
([`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md),
body §"Offering a channel is not exercising it"). This run **forces** uptake.

## Design (single manipulated variable: offered → forced working surface)

The ONLY change vs session 58 is the trailing output instruction: a free-form "think it
through step by step" → a **mandatory, construction-neutral, answer-blind 3-step
decomposition** (1. PREMISE paraphrase / 2. HYPOTHESIS paraphrase / 3. LINK: does the
premise force the hypothesis true / open / false) that *requires* the working before the
`FINAL: <0,1,2>` tag. The scaffold names no construction and no scale; step 3 only restates
the same 0/1/2 trichotomy already in the verbatim definitions, so it adds no information —
it forces the general entailment check to be **externalized**. There are **no
demonstration items** (forced decomposition, not few-shot → lowest governance risk).

Held byte-identical to sessions 57/58: the same 24 let-alone + 30 comparative-correlative
items (subset sha `9be31a8fea8d7f16`; full-set sha `1c5cffb18c5ef78e`), the 0/1/2 label
definitions (verbatim), the gold (not shown), the panel, temperature 0, gemini `effort:
minimal` (held constant → isolates the output channel / uptake, not the reasoning budget).
No new decision owed (format/instrument extension under the ratified Scivetti answer-key
anchor; fresh independent pre-run critic GO).

## Result (verdict: uptake INDUCED for all 3; all UNCHANGED vs offered; gpt PARTIAL recovery, stays below baseline)

| | forced (s57) | offered ws (s58) | **forced-decomp** | paired vs offered | verdict | vs human 0.90 |
|---|---:|---:|---:|---:|---|---|
| claude | 0.542 | 0.792 | **0.833** [0.641,0.933] | +0.04 (g2/l1, p=0.50) | UNCHANGED | MATCHES |
| gpt | 0.458 | 0.375 | **0.583** [0.388,0.755] | +0.21 (g7/l2, p=0.090) | UNCHANGED | **BELOW** |
| gemini | 0.667 | 0.917 | **0.875** [0.690,0.957] | −0.04 (g2/l3, p=0.81) | UNCHANGED | MATCHES |

**The manipulation worked.** All three models "worked" 24/24 let-alone items (≥40 pre-`FINAL`
chars + ≥2 numbered steps). The crux: **gpt now genuinely took up the channel** — median
completion tokens **8 → 120** (min 101), where session 58 it emitted bare one-token answers.
So the session-58 "channel-not-taken-up" hole is **closed**: gpt's wide channel was actually
exercised this time.

**The answer is a PARTIAL channel effect, not a full artifact and not a clean survival.**
With uptake forced, gpt's let-alone rose +0.21 over the offered surface (7 gains / 2 losses)
— **directional but underpowered** (sign test p = 0.090, does not clear the pre-registered
0.05 bar → UNCHANGED) — and it **stays below the human baseline** (0.583, CI hi 0.755 <
0.90), where claude and gemini sit. So part of gpt's let-alone gap is channel-bounded
(uptake helps) and part **survives a genuinely-exercised wide channel** (it does not reach
baseline). This is the closest the record has come to the `output-channel-confound`
**trigger-(b)** contrast case, but n=24 leaves it a *candidate*, not a clean firing.

**claude/gemini are the manipulation check, and it passes.** Both already lifted under the
offered surface and **stay at baseline** under forced decomposition (UNCHANGED, no DROP),
with the comp-correlative ceiling control PRESERVED for all three (1.000) — so the forced
scaffold is a *valid, benign* instrument, not a degrading one.

## Cost & integrity

- Billed `usage.cost`: **$0.3342** (claude $0.2019 / gpt $0.0373 / gemini $0.0951; the
  working-surface CoT makes claude the driver; gpt rose from session 58's $0.015 because it
  now writes the working it skipped). 162 finding-bearing calls
  (54×3). 0 missing, **162/162 parsed via the FINAL tag** (0 fallbacks), 0 missing
  `usage.cost`. Pre-flight $0.35–0.50; came in just under.
- Cadence: PREREG (frozen) → fresh independent pre-run critic **GO** (8/8 checks; byte-level
  single-variable diff; no demo items; no new decision) → probe → fresh independent post-run
  verifier (every number + uptake check + CoT genuineness + content_sha256↔CoT binding +
  no gold-leak).

## Files

- `prep.py` — freeze recipe (subset + full-set sha; recipe-not-corpus); identical to s58.
- `probe.py` — the forced-decomposition NLI probe (only API caller); records an `uptake`
  field (pre-FINAL char length + numbered-step markers; lengths/booleans only, NO text).
- `analyze.py` — per-construction acc + Wilson CI vs 0.90 + within-item paired sign test
  vs session 58 (offered) + uptake manipulation check.
- `PREREG.md` — frozen pre-registration (GO'd).
- `stimuli-manifest.json` — sha-pinned counts (NO item text).
- `raw/{A,B,C}-labels.json` — committed: item_id + cxn + gold + label + parse_mode +
  uptake + content sha256 + usage (NO text). `raw/cot/` — gitignored full CoT.
- `results.json` — analysis output.

Reproduce: re-clone upstream `@82699473` into `experiments/data/scivetti/`, then
`python3 prep.py --check && python3 analyze.py`. To re-collect labels, `python3 probe.py`.

Finding: [`result/scivetti-let-alone-forced-decomposition-v1`](../../../wiki/findings/results/scivetti-let-alone-forced-decomposition-v1.md).
