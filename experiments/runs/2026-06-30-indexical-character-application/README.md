# Run: indexical CHARACTER-application probe (2026-06-30, session 154)

Tests essay [`essay/indexical-character-learnable-content-supplied`](../../../wiki/findings/essays/indexical-character-learnable-content-supplied.md)
**trigger (c)** — does a panel model *systematically mis-apply* an indexical's convention-fixed
rule (its Kaplanian **character**) when the origo is fully **described** in the text? Frozen
design + verdict map: [`PREREG.md`](PREREG.md). Manifest sha
`503d907bc3f681f0992f8f53ad2b7252ae8ab7eecf711755518dee4a4b1301c8`.

## What ran

- **40 items**, 4 conditions × 10 (prep.py / items.json): C1 plain, C2 origo-shift, C3
  embedded-reported-speech (resolve to the embedded origo over a salient narrator distractor),
  C4 temporal-arithmetic. Single resolution target per item; project's own synthetic stimuli
  (full text committed). Date golds computed (datetime) + weekday-asserted.
- **Panel as subjects** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A),
  gpt-5.4-mini (B), gemini-3.5-flash (C). Temperature 0; brief reasoning + marked `FINAL:` line;
  gemini reasoning `effort: minimal`. One run, one date, zero-shot.
- **Integrity:** 120/120 calls, **0 missing usage.cost**, **all parse_mode = "final"** (no
  empty/fallback), 0 unparseable.
- **Cost (billed usage.cost):** **$0.0752** (claude $0.0358 / gpt $0.0072 / gemini $0.0322).
  Far under the $2.50 single-run flag and the $5.00/day (UTC) cap.

## Result

| model | C1 | C2 | C3 | char (C1–C3) | C4 | overall |
|---|---:|---:|---:|---:|---:|---:|
| claude-sonnet-4.6 | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |
| gpt-5.4-mini | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |
| gemini-3.5-flash | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |

**VERDICT (pre-registered): NON-FALSIFICATION.** Every model applies indexical character to a
described context at ceiling (120/120 items correct), including the hard C3 embedding (e.g.
'here' → the embedded speaker's Cairo / the Alps, not the narrator's location; embedded 'tomorrow'
→ the letter's date+1, not the reading date) and the C4 multi-step date arithmetic. Trigger (c)
does **not** fire. This is **consistent with** the essay's "character is distributionally native"
**affordance** half and **does not prove** it (an affordance is not provable from a ceiling; a
failure would have falsified it — the result is asymmetric by construction).

## Reproduce

```
python3 prep.py --check      # frozen manifest sha intact
python3 analyze.py           # re-scores raw/{A,B,C}.json -> results.json + the table above
```

Independent fresh-agent **pre-run critic**: GO-WITH-NOTES (no blockers; two analysis-layer
date-format SHOULD-FIXes applied to analyze.py before the run — they only widen acceptance of
correct date surface forms; frozen manifest sha unchanged). Independent fresh-agent **post-run
verifier**: see the result page's *Provenance*.

## Files

`PREREG.md` (frozen design + verdict), `prep.py` (items + key + freeze guard, sha-pinned),
`items.json` (dumped stimuli), `probe.py` (the only API caller), `analyze.py` (frozen scoring +
verdict), `raw/{A,B,C}.json` (per-item answers + usage), `results.json` (scored output).
