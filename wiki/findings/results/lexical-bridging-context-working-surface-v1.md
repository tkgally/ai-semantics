---
type: result
id: lexical-bridging-context-working-surface-v1
title: "Working-surface re-run of the lexical bridging-context probe — the ungraded-commitment null is largely channel-CONTROLLED, not a channel artifact: it survives a genuinely-used working surface for gemini, partially cracks on claude's self-reported confidence only, and is inconclusive for gpt (declined the surface)"
meaning-senses:
  - distributional
  - referential
  - human-comparison
  - functional-vs-formal
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-06-22
updated: 2026-07-05
links:
  - rel: refines
    target: result/lexical-bridging-context-v1
  - rel: supports
    target: claim/lexical-graded-scale-ungraded-commitment
  - rel: depends-on
    target: essay/output-channel-confound
  - rel: depends-on
    target: open-question/gradience-population-not-moment
  - rel: depends-on
    target: essay/graded-scale-ungraded-commitment
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: supports
    target: claim/output-channel-working-surface
---

# Result: working-surface re-run of the lexical bridging-context probe

> **Status: proposed (2026-06-22, session 79).** A trigger-(b)-style witness-seek, **not**
> a re-tune of the frozen v1. It re-runs the lexical bridging-context probe
> ([`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md)) changed in exactly
> one way — the **output channel**: v1 forbade a working surface ("Answer with X and nothing
> else"); this variant **permits step-by-step working** and parses a `FINAL:` tag, with the
> reasoning-effort knob **held constant** (claude/gpt suppressed, gemini `effort: minimal`),
> so the surface is opened only in the *visible* output channel. The task text is
> **byte-identical** to v1 (enforced by construction; audited by `verify_format_only.py`).
> The motive: v1 read the ungraded-COMMITMENT null off a constrained single-label channel, and
> [`essay/output-channel-confound`](../essays/output-channel-confound.md) holds a forced-format
> negative is **channel-bounded** until the channel is varied;
> [`open-question/gradience-population-not-moment`](../open-questions/gradience-population-not-moment.md)
> names this exact re-run as the discriminating test. Independent fresh-agent pre-run critic
> **GO** (format-only diff confirmed byte-level). **1056 calls (4 temp-0 framings × 88 items ×
> 3 models; the characterizing-only A dispersion dropped for cost per the instrument's own
> sanction), $2.412 billed, 0 missing cost, 100% FINAL-tag parse, 0 fallbacks.**

> **Update (2026-07-05, session 183 — wiki-coherence pass).** gpt's inconclusive non-uptake leg
> was later closed: [`result/lexical-bridging-context-forced-decomposition-v1`](lexical-bridging-context-forced-decomposition-v1.md)
> (session 82) forced uptake with a mandatory answer-blind 3-step decomposition (0% bare) and read
> a weak MIXED/WEAK softening at the jitter floor, and the K=5 byte-identical resolver
> [`result/lexical-bridging-context-forced-decomposition-repeated-runs-v1`](lexical-bridging-context-forced-decomposition-repeated-runs-v1.md)
> (session 88) de-noised it to the channel-controlled null, like gemini's.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## Lead with the cap (binding, read first)

Every human comparison below is **about usage-similarity intermediacy ONLY** (anchor condition
6, inherited from v1). A DWUG mid-scale (DURel 2–3, ≥3-rater) "bridging" pair is a **human-rated
usage-similarity midpoint**, **not** a certified within-sense bridge. This is **behavioral, not
representational**, and small, lemma-clustered N (24 bridging pairs / 17 lemmas). "Commitment"
means the confidence/decline posture of a behavioral verdict, never a window into representation.

## Headline

**The v1 "ungraded commitment" null is, in the main, channel-CONTROLLED — it is not a forced-
format artifact — but the panel splits by uptake and by instrument, so the clean 3/3 of v1 does
*not* cleanly replicate under a working surface.** Reading the three models against
[`essay/output-channel-confound`](../essays/output-channel-confound.md)'s three-state grid
(channel-bounded / channel-not-taken-up / channel-controlled):

- **gemini took up the surface fully and the commitment null SURVIVED** (confidence not lower on
  bridging, decline 0%) — **channel-controlled**: for gemini the ungraded commitment is real, not
  a denial-of-surface artifact.
- **claude took up the surface fully and the null PARTIALLY cracked** — only on the *self-reported
  confidence* axis (bridging confidence 82.6 → 75.2, now CI-strict lower than both clear classes),
  **not** on the *categorical-decline* axis (it does not take "UNCLEAR" more on bridging than on
  clear items). B and C now disagree → a **MIXED/WEAK** result, not a flip to graded commitment.
- **gpt DECLINED the surface** (90.9% of b_conf answers were a bare one-token `FINAL: …`, median
  15 completion tokens, 0% reasoning) → **channel-not-taken-up**: its unchanged null is
  **inconclusive** as a channel test (it effectively re-ran v1's narrow channel).

The **categorical-decline instrument** — the one designed to be robust to self-report — shows
**ungraded** commitment on bridging for *every model that took up the channel*. The graded
**scale** (position) replicates throughout. So the within-moment discreteness is, for the most
part, **not** an aperture the wide channel removes; the one place it softens is claude's
*self-reported number*, which drifts down under reflection while its categorical commitment holds.

## Uptake first (the control's precondition)

[`essay/output-channel-confound`](../essays/output-channel-confound.md)'s uptake clause: "vary
the channel" means vary the channel *actually used*; a declined surface is channel-not-taken-up
(inconclusive), never a survival. Median completion tokens / % bare (<40 chars) per model,
across all four framings (100% emitted a parseable `FINAL:` tag):

| model | b_rel | b_conf | c_third | topic | uptake verdict |
|---|---|---|---|---|---|
| claude | 284 tok / 0% bare | 243 / 0% | 243 / 0% | 223 / 0% | **took up** (full CoT) |
| gemini | 257 / 0% | 206 / 0% | 212 / 0% | 223 / 0% | **took up** (full CoT) |
| gpt | 14 / 85% | 15 / 91% | 8 / 99% | 14 / 99% | **declined** (bare answers) |

So claude and gemini genuinely externalized their reasoning; gpt mostly did not. gpt's results
are reported but read as **channel-not-taken-up**, not as a survival of the null.

## Panel and design (frozen; format-only change)

- **Panel:** [`config/models.md`](../../../config/models.md) — claude-sonnet-4.6, gpt-5.4-mini,
  gemini-3.5-flash.
- **Items (88):** the **same** 48 DWUG within-period stratum pairs (clear-same 9 / **bridging 24**
  / clear-different 15; ≥3-rater) + 40 WiC clear-pole supplement as v1 (DWUG archive sha
  `64eef477…`, WiC `f1a2fb67…`, both matching their pins; frozen stratum/instrument shas re-checked).
- **Change (the only one):** output channel. Each framing's system prompt keeps v1's task text
  byte-identical and replaces only the trailing answer clause ("Answer with X and nothing else" →
  "Think step by step …, then give your answer on a final line: FINAL: …"); `max_tokens` raised so
  the visible channel can carry the working. **Reasoning-effort held constant** at v1's setting.
  The A dispersion (characterizing-only, never in the verdict) was dropped for cost — v1's own
  `cost_control` sanctions this; it leaves the two verdict-bearing commitment instruments (B
  confidence, C decline) intact.
- Probe + auditor: [`experiments/designs/lexical-bridging-context-working-surface-v1/`](../../../experiments/designs/lexical-bridging-context-working-surface-v1/)
  (`instrument.json` provenance; `verify_format_only.py` proves the byte-level format-only diff;
  `probe.py` builds the working-surface prompts *from* the v1 instrument by suffix-replacement).

## Clear-class precondition: MET (3/3), dwug+wic scope

| model | clear-same b_rel | clear-diff b_rel | clear-same b_conf | clear-diff b_conf | clear %UNCLEAR |
|---|---|---|---|---|---|
| claude | 73.9 | 24.4 | 83.9 | 88.4 | ≤13.8% |
| gpt | 75.4 | 35.2 | 93.9 | 93.7 | 0% |
| gemini | 81.8 | 26.4 | 91.2 | 97.4 | 0% |

Poles saturated, clear-class confidence high, clear-class decline low. So the result is
**DWUG-anchored** (capped to usage-similarity), not `internal-contrast-only`. (On the DWUG-only
scope, claude's clear-same b_rel pole falls below the 70 floor, so claude's headline uses the
dwug+wic scope, exactly as in v1.)

## The axes (dwug+wic; n: clear-same 29, bridging 24, clear-different 35)

### Position axis (B/`b_rel`) — GRADED, replicates 3/3

| model | clear-diff | **bridging** | clear-same | in [40,60]? | between (CI-strict)? |
|---|---|---|---|---|---|
| claude | 24.4 | **46.2** | 73.9 | yes | **yes** |
| gpt | 35.2 | **46.9** | 75.4 | yes | pointwise yes (CI grazes) |
| gemini | 26.4 | **52.3** | 81.8 | yes | **yes** |

The graded scale survives the channel change for all three (claude's between-gap even firms to
CI-strict under the surface).

### Confidence axis (B/`b_conf`) — splits

| model | clear-diff | **bridging** | clear-same | bridging lower than BOTH (CI-strict)? | Δ bridging vs v1 |
|---|---|---|---|---|---|
| claude | 88.4 | **75.2** | 83.9 | **yes** (the crack) | **−7.4** |
| gpt | 93.7 | **92.3** | 93.9 | no | −3.4 (but declined surface) |
| gemini | 97.4 | **93.8** | 91.2 | no (above clear-same) | −1.0 |

Only claude — which took up the surface — lowers its self-reported confidence on bridging enough
to clear CI-strictness. gemini took up the surface and did **not** (its bridging confidence stays
at clear-item level). gpt's small drop is not interpretable (it declined the surface).

### Decline axis (C/`c_third` %UNCLEAR) — UNGRADED for every model that took up the channel

| model | clear-diff | **bridging** | clear-same | elevated on bridging? |
|---|---|---|---|---|
| claude | 2.9% | **12.5%** | 13.8% | **no** (bridging ≈ clear-same; both rose) |
| gpt | 0% | **0%** | 0% | no (declined surface) |
| gemini | 0% | **0%** | 0% | **no** |

The working surface made claude take "UNCLEAR" more *in general* (clear-same also rose to 13.8%),
**not preferentially on bridging** — so the categorical-commitment null holds: no model that used
the surface declines more on the genuinely-ambiguous item than on a clear one.

### Verdict (frozen v1 rule, per model)

- **gemini — PARTIAL (graded scale, ungraded commitment), channel-CONTROLLED.** Took up the
  surface; confidence not lower, decline 0%. The v1 null survives a genuinely-used wide channel.
- **claude — MIXED/WEAK.** Took up the surface; position graded **and** confidence CI-strict lower,
  but decline not elevated → B and C disagree (per modification 3, reported as mixed/weak, *not*
  the null and *not* a clean graded-commitment positive). The self-report softened; the categorical
  commitment did not.
- **gpt — inconclusive (channel-not-taken-up).** Its CLEAN-NULL reading reproduces v1 but under a
  surface it declined, so it neither confirms nor tests the channel question.

## What this resolves

- **The channel-artifact alternative named in [`claim/lexical-graded-scale-ungraded-commitment`](../claims/lexical-graded-scale-ungraded-commitment.md)
  ("what would change this") is, in the main, ruled out.** The commitment null is **not** simply
  an artifact of the cramped output channel: it survives a genuinely-used working surface for
  gemini and survives on the categorical-decline instrument for every model that took it up. The
  claim stands, with a sharpened scope — claude's *self-reported confidence* component is partly
  channel-sensitive (it drops under reflection), while the *categorical-decline* component (and
  gemini's confidence) is channel-controlled.
- **For [`essay/output-channel-confound`](../essays/output-channel-confound.md):** a clean
  application of the three-state grid to a **non-serial** capability. The essay scopes the confound
  to *serial, externalizable* computation; a same/different-sense **commitment** is not that kind of
  computation, and the result is consistent with the scope holding — widening a taken-up channel
  does **not** dissolve the commitment posture (it is not a masked serial computation). It does
  **not** fire trigger (a) (no dissolution into panel-concordance) and is not a clean trigger-(b)
  serial-computation survival (the capability is not serial); it **does** independently reproduce
  the **channel-not-taken-up** state (gpt) on a fresh instrument family, corroborating the uptake
  clause's necessity (had gpt's null been read as a survival, the panel would look "3/3 channel-
  controlled" — false; gpt simply declined the surface).
- **For [`open-question/gradience-population-not-moment`](../open-questions/gradience-population-not-moment.md):**
  the lexical "discrete-moment" leg is **firmer**, not dissolved — its categorical commitment is
  channel-controlled — with two honesty caveats the OQ should carry: claude's confidence self-report
  is partly channel-sensitive, and gpt's leg is untested (non-uptake). The cross-level pattern keeps
  its lexical leg, now channel-checked.

## Scope and limits (lead with these)

- **Behavioral, not representational; usage-similarity, not sense co-presence** (the v1 caps,
  unchanged).
- **Small, lemma-clustered N** (24 bridging / 17 lemmas), 3 commercial 2026 models;
  direction-of-effect with wide per-lemma bootstrap CIs; no coverage claim.
- **Two of three models took up the channel; one (gpt) declined it.** The channel question is
  answered only for the sub-panel that exercised the surface (claude, gemini); gpt is inconclusive.
- **A dispersion dropped for cost** — the verdict rests on B (confidence) and C (decline), exactly
  the two instruments that carried the v1 verdict; A never entered it.
- **Q3 context control** (bridging `b_rel` vs the model's own `topic` rating) stays bound-but-weak
  under the surface (Pearson r 0.39 / 0.48 / 0.48), qualifying the *position* reading as in v1; it
  bears little on the commitment finding.
- **claude's confidence drop is a self-report shift**, observed only on the numeric confidence axis,
  not corroborated by the categorical instrument — so "claude carries graded commitment" is **not**
  licensed; "claude's self-reported confidence softens under a working surface while its categorical
  commitment holds" is.

## Reproduce

- Stage corpus (gitignored, recipe-not-corpus): the v1 `prep.py` (DWUG, 48/48 remap) +
  `map_wic_fulltext.py` (frozen WiC manifest → text).
- `python3 verify_format_only.py` (confirms the byte-level format-only diff; no API),
  then `OPENROUTER_API_KEY=… PROBE_WORKERS=8 python3 probe.py --no-a`, then `python3 analyze.py`,
  then `python3 sanitize_raw.py` before committing (strips the CoT `raw` field, which can quote
  the licensed corpus text — unlike v1's short-label outputs).
- Raw outputs (sanitized: item ids, parsed preds, uptake metrics, usage — **no** corpus text and
  **no** verbatim CoT):
  [`experiments/designs/lexical-bridging-context-working-surface-v1/raw/`](../../../experiments/designs/lexical-bridging-context-working-surface-v1/);
  analysis `analysis.json` (same 10000-rep lemma-clustered bootstrap, seed 20260622, as v1).

## Verifier note

A post-run verifier should re-derive: the format-only diff (`verify_format_only.py`), the per-model
verdicts and the bridging deltas vs v1's `analysis.json`, the uptake table (gpt's ≥85% bare across
framings; claude/gemini 0% bare), parse integrity (100% FINAL tag, 0 fallback), billed cost
re-summed to the penny ($2.412), and confirm no corpus text or verbatim CoT survives in the
committed raw.
