# 2026-06-20 — let-alone working-surface format probe

**Format-only follow-up** to `2026-06-20-scivetti-cxnli-answer-key` (session 57). Tests
whether the phrasal-scalar **let-alone** near-chance failure (claude 0.542 / gpt 0.458 /
gemini 0.667 under a forced single-token NLI channel) is a competence-absence or an
**output-channel artifact** ([`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)).

## Design (single manipulated variable: response format)

The ONLY change vs session 57 is the response format: forced single token → a **working
surface** (step-by-step reasoning permitted, a `FINAL: <0,1,2>` tag parsed). Held
byte-identical: the same 24 let-alone + 30 comparative-correlative test items (subset sha
`9be31a8fea8d7f16`; full-set sha `1c5cffb18c5ef78e` == session 57's), the 0/1/2 label
definitions (verbatim), the gold (not shown), the panel, temperature 0, and gemini
`reasoning effort: minimal` (held constant → isolates the output channel, not the
reasoning budget). comparative-correlative is a ceiling control (forced-format
1.0/0.9/1.0). No new decision owed (instrument extension under the ratified Scivetti
answer-key anchor; fresh independent pre-run critic GO).

## Result (verdict: 2/3 LIFTS; control PRESERVED)

| | let-alone forced | let-alone ws | Δ | gains/losses | verdict | comp-corr ws (control) |
|---|---:|---:|---:|---:|---|---:|
| claude | 0.542 | **0.792** | +0.25 | 7/1 (p=0.035) | **LIFTS** | 1.000 PRESERVED |
| gpt | 0.458 | 0.375 | −0.08 | 2/4 | UNCHANGED* | 0.967 PRESERVED |
| gemini | 0.667 | **0.917** | +0.25 | 7/1 (p=0.035) | **LIFTS** | 1.000 PRESERVED |

claude & gemini reach the human ≈0.90 baseline on the *same items* once given a working
surface → the failure was largely an output-channel artifact (refines
`output-channel-confound`'s scope: a *scalar* single-premise NLI item DOES carry masked
serial working). **\*gpt largely DECLINED the surface** (16/24 bare one-token answers, 0
reasoning tokens) — so its persistence is **channel non-uptake**, not a clean
channel-controlled survival; trigger (b) stays open.

## Cost & integrity

- Billed `usage.cost`: **$0.3164** (claude $0.164 / gpt $0.015 / gemini $0.138). 162
  finding-bearing calls (54×3) + 0 liveness (freeze guard only). 0 missing, 162/162 parsed
  via the FINAL tag (0 fallbacks).
- Cadence: PREREG (frozen) → fresh independent pre-run critic **GO** → probe →
  fresh independent post-run verifier **REPRODUCED** (all numbers + CoT genuineness +
  content_sha256↔CoT binding + no gold-leak).

## Files

- `prep.py` — freeze recipe (subset + full-set sha; recipe-not-corpus).
- `probe.py` — the working-surface NLI probe (only API caller).
- `analyze.py` — per-construction acc + Wilson CI vs 0.90 + within-item paired sign test.
- `PREREG.md` — frozen pre-registration (GO'd).
- `stimuli-manifest.json` — sha-pinned counts (NO item text).
- `raw/{A,B,C}-labels.json` — committed: item_id + gold + label + parse_mode + content
  sha256 + usage (NO text). `raw/cot/` — gitignored full CoT (restates source text).
- `results.json` — analysis output.

Reproduce: re-clone upstream `@82699473` into `experiments/data/scivetti/`, then
`python3 prep.py --check && python3 analyze.py`. To re-collect labels, `python3 probe.py`.

Finding: [`result/scivetti-let-alone-working-surface-v1`](../../../wiki/findings/results/scivetti-let-alone-working-surface-v1.md).
