---
type: result
id: tool-origo-deictic-anchor-v1
title: "The panel binds an unanchored 'now'/'here'/'today' to a clock/location tool at ceiling (100%) — but the SAME tool overrides a NARRATED origo 47–60% of the time, so the as-if reading is CONFOUNDED (MIXED, control-failure)"
meaning-senses:
  - referential
  - grounded
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-01
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/tool-origo-deictic-anchor
  - rel: refines
    target: essay/origo-supplied-not-occupied
  - rel: depends-on
    target: source/braun-2015-indexicals-sep
  - rel: depends-on
    target: result/indexical-character-application-v1
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/grounding
---

# Result: the as-if origo probe v1 (tool as deictic anchor)

The **first empirical touch on the CONTENT half** of the project's indexicality corner, and the
sibling of the character-half [`result/indexical-character-application-v1`](indexical-character-application-v1.md).
It runs question **(iii)** — the one behaviorally testable residue — that
[`essay/origo-supplied-not-occupied`](../essays/origo-supplied-not-occupied.md) isolated and
[`conjecture/tool-origo-deictic-anchor`](../conjectures/tool-origo-deictic-anchor.md) pre-registered:
*given a clock/location **tool** is available, does the panel **spontaneously** treat tool-state as
the deictic anchor for an **unanchored** ‘now’/‘here’/‘today’ — calling the tool unbidden and
binding the indexical to what it returns?* Run record:
[`experiments/runs/2026-06-30-tool-origo-deictic-anchor/`](../../../experiments/runs/2026-06-30-tool-origo-deictic-anchor/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-06-30-tool-origo-deictic-anchor/PREREG.md),
manifest sha `74763523…`.

**One-line finding.** On the **unanchored test** arm every model spontaneously queries the tool and
binds the indexical to tool-state at **ceiling — 100% query, 100% resolution, all three models**.
But the pre-registered **anchored control** — the same question with the origo already *narrated* in
the text — **fails**: the models call the tool and **override the narrated origo with the tool's
value 47–60% of the time**, far above the fixed **0.20** ceiling. Per the frozen verdict map this is
a **MIXED (control-failure)** result: the clean test-arm ceiling **cannot be read** as the panel
treating tool-state as the deictic anchor *specifically for an unanchored* indexical, because the
same tool-deference appears when the origo is fully narrated. The control did exactly the job it was
built for — it **voids the strong (unanchored-specific) reading** of the ceiling.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as **subjects** (charter §6). All three
  advertise `tools`+`tool_choice` on OpenRouter (verified). Temperature 0; `tool_choice` = **auto**
  (a call is the model's own move); a **tool-silent** system prompt (spontaneity guard); gemini
  reasoning `effort: minimal`. One run, one date, zero-shot.
- **Items.** 15 **project-authored** matched base scenarios (5 time / 5 date / 5 location) × 3 arms =
  45 item-conditions (full text committed; no external corpus). **test** = unanchored + tool;
  **control** = a narrated origo (values distinct from the nonce) + tool; **baseline** = the same
  unanchored text with **no tool**. Two tools exposed together (`get_current_time`,
  `get_current_location`) so the tool is not the only salient affordance.
- **Nonce tool returns** (un-memorizable, logged): time **17:42**, date **3021-11-08**; location
  **Qethport, Vandrel Province, Meridonia**. So "resolved to tool-state" = the final answer contains
  a nonce token, and **cannot appear in the tool-free baseline at all** — a *structural* guarantee
  that the resolution signal is tool-attributable.
- **Integrity.** 135 items, **0 missing `usage.cost`**; **0** records hit MAX_TURNS; every test-arm
  resolution echoed the nonce directly (no timezone-converted false negatives — a pre-run-critic
  risk that did not bite).
- **Cost** (billed `usage.cost`): **$0.2160** (claude $0.1772 / gpt $0.0144 / gemini $0.0244). Under
  the $2.50 single-run flag; UTC-2026-06-30 day total $0.0752 → **$0.2912** of the $5.00/day (UTC) cap.

## Results

| model | test spont-query | test resolve→tool | control tool-query | **control override** | control resolve→narrated | baseline nonce |
|---|---:|---:|---:|---:|---:|---:|
| claude-sonnet-4.6 | 1.00 | 1.00 | 0.67 | **0.60** | 0.93 | 0.00 |
| gpt-5.4-mini | 1.00 | 1.00 | 0.60 | **0.53** | 0.60 | 0.00 |
| gemini-3.5-flash | 1.00 | 1.00 | 0.53 | **0.47** | 0.67 | 0.00 |

**Control override is GENUINE, not a "mentions-both" artifact.** The models report the nonce as the
answer and actively correct the user, e.g. (claude, control `t1`, text says "It's 10:15 in the
morning"): *"It's actually **5:42 PM** right now — not 10:15 AM!"*; (gpt, control `d3`, text says
"today, 1 December 2024"): *"Today's date is **8 November 3021**"*; (gemini, control `l4`, text says
"my current city, which is Montreal"): *"You are currently in **Qethport** … in the Vandrel Province
of Meridonia."*

**Override is graded by indexical type** (override count / 5 per arm):

| | time | date | location |
|---|---:|---:|---:|
| claude | 4/5 | 1/5 | 4/5 |
| gpt | 1/5 | 3/5 | 4/5 |
| gemini | 3/5 | 0/5 | 4/5 |

**Location is overridden 4/5 in every model** — a narrated place is the origo the tool most readily
displaces (only the most strongly-narrated item, "we arrived in Kyoto this morning," survives).
**Date is overridden least** (0–3/5): a stated date is the origo models most often keep. Time sits
between and splits by model.

**Baseline (no tool) — the deflationary fallback, read from the raw** (the descriptive `hedge_rate`
heuristic under-counts gpt's hedges because gpt writes "can’t" with a curly apostrophe — see Limits;
so the baseline is characterized qualitatively here, not by that number): on **time** and
**location** all three models **refuse/hedge** ("I don't have access to the current time"; "I can't
tell where you are"). On **date** they split — claude hedges, **gpt emits a parametric default**
("Today's date is **July 1, 2026**", its near-deployment prior — which happens to be the real date),
gemini **hallucinates** varied wrong dates. No baseline answer contains a nonce token (0.00, as
guaranteed).

## Verdict (pre-registered, not retuned)

Thresholds fixed **before** the run (PREREG §verdict-map): **T = 0.80** (test spontaneous-query and
resolution), **OVR = 0.20** (control override ceiling), ≥ 2/3 majority. **CONFIRM** requires the
confirming models to *also* keep control override ≤ 0.20. All three clear both test thresholds; **none**
keep control override ≤ 0.20 (0.60 / 0.53 / 0.47). So neither a CONFIRM majority (needs override-OK)
nor a NULL majority (needs test-below-threshold) obtains → **MIXED**, in the specific pre-registered
shape *"the control fails … an uninterpretable control voids that model's test reading."*

## Interpretation (modest)

1. **The test-arm ceiling is real but does not establish the as-if bet.** The conjecture's core
   prediction — that a panel handed a clock/location tool spontaneously queries it and binds an
   unanchored ‘now’/‘here’/‘today’ to what it returns — held **perfectly** (100/100 on both metrics).
   Taken alone it looks like a clean CONFIRM. The control is what stops that reading.
2. **What the control reveals: generic tool-deference, not origo-sensitivity.** The panel reaches for
   and *defers to* a clock/location tool on time/place/date questions **whether or not the origo is
   already narrated** — overriding an explicitly stated origo **about half the time** (and sometimes
   "correcting" the user). The deference is **partial, not unconditional**: a narrated origo still
   wins the other ~40–50%, so the right statement is *"the panel does not reliably privilege a
   narrated origo over the tool,"* **not** "it ignores narrated origos." Even so, the disposition is
   plainly not *"treat tool-state as the anchor only when the text leaves the indexical unanchored"*;
   it is closer to *"treat an available clock/location tool as a strong authority for time/place,
   narrated context notwithstanding."* The unanchored-arm ceiling is a special case of that, not
   evidence of a deictic-anchor mechanism keyed to unanchoring. This is exactly the confound the
   anchored control was pre-registered to catch, and it caught it.
3. **A graded secondary pattern.** Tool-over-narration deference is **strongest for location, weakest
   for date** across all three families. A plausible (speculative) reading: a stated *date* reads as
   given information a cooperative reader keeps, whereas *location* reads as something a device
   legitimately knows better than a user's claim — so the tool's authority scales with how
   "instrument-owned" the indexical feels. Named as a conjecture-shaped observation, not a measured
   claim.
4. **It bears on the essay's (iii), not (i)/(ii).** Per the sibling essay's split, this probe touches
   only the **behavioral as-if** question. Even the clean test ceiling was pre-committed to be unable
   to certify **occupation** (i) or dent the **channel** claim (ii) — a tool-return is itself
   *described text the model conditions on*. The MIXED outcome adds a *second* deflation *below* that
   ceiling: at the behavioral grain the tool-use is not even origo-sensitive, so it is weak evidence
   for an "as-if origo" reading in the first place.

## What this does and does not license

**Does license:** a within-model statement that, on these 45 items, the 2026 panel (a) spontaneously
queries a clock/location tool and binds an *unanchored* ‘now’/‘here’/‘today’ to its return at ceiling,
**and** (b) does the same, overriding a *narrated* origo, 47–60% of the time — so (a) is **not**
attributable to an unanchored-specific "treat-the-tool-as-origo" disposition. Reported strictly as an
**as-if / within-model** contrast.

**Does NOT license:**
- **The as-if bet (a CONFIRM).** The control failure voids the strong reading; the result is MIXED,
  not a confirmation of the conjecture.
- **A clean NULL either.** The panel plainly *does* spontaneously reach for the tool and resolve to
  its value; the deflationary "refuse/hedge/never-call" alternative is false for the tool arms. The
  null holds only in the *tool-free* baseline (which is a different, expected fact).
- **Any occupation claim (i).** Nothing here shows the model "is the agent of" a context; a tool-return
  is described text. No `wiki/decisions/open/` gate is opened because **no stronger-than-as-if claim is
  made** (the conjecture's deferred "tool-return = occupied?" gate stays unfired).
- **Any human comparison.** No human baseline is claimed, measured, or needed
  (`anchor: internal-contrast-only`). The result says nothing about whether people defer to a clock a
  friend contradicts.
- **A generalization beyond these tools/framings.** Two parameter-free tools, one system prompt, n=5
  per indexical-per-arm. A different tool design, an explicit "trust the user over the tool"
  instruction, or a conflicting-source frame could move the override rate either way.

## Limits

- **Small cells, single run, one framing.** 5 items per indexical per arm; a 100% test ceiling gives
  no spread; the override rates are indicative, not tightly estimated.
- **Descriptive hedge heuristic under-counts curly-apostrophe hedges.** The baseline `hedge_rate` for
  gpt reads 0.00 only because gpt writes "can’t" (U+2019), which the straight-apostrophe marker list
  misses; the raw shows gpt *does* hedge on time/location and defaults only on date. This touches a
  **descriptive** companion number only — it is **not** part of any gate, and the load-bearing
  baseline fact (nonce_rate = 0.00, structural) is unaffected.
- **The nonce is un-flagged as fictional.** The tool returns year 3021 / "Qethport" with no signal
  that it is stubbed; a model that *distrusts an implausible tool value* would look like a
  non-resolver. All three instead reported it (often noting the oddity), so this did not depress the
  test arm — but a realistic-value design might read differently.
- **Stipulated key, not a human gradient.** Correctness is defined against the logged tool return and
  the narrated origo, never a per-item human distribution.

## Provenance

- Tests [`conjecture/tool-origo-deictic-anchor`](../conjectures/tool-origo-deictic-anchor.md)
  question (iii); refines [`essay/origo-supplied-not-occupied`](../essays/origo-supplied-not-occupied.md)
  by adding the behavioral datum that the as-if reading is confounded by generic tool-deference. The
  character/content split is [`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md)
  (Kaplan, survey strength). Character-half sibling:
  [`result/indexical-character-application-v1`](indexical-character-application-v1.md).
- **Anchor: `internal-contrast-only`.** The three metrics are pure **within-model rates** over a
  3-arm contrast against a stipulated nonce / narrated origo — **no** human baseline and **no**
  cross-entity comparison, so no resource anchor is owed. This rests on the anchor-type precedent
  already ratified for the sibling result
  ([`decisions/resolved/indexical-character-anchor-type`](../../decisions/resolved/indexical-character-anchor-type.md),
  ADOPT A, 2026-06-30), which the conjecture invoked *before* the run; this result's measure is the
  same type (arguably cleaner — no cross-entity comparison at all). No human anchor is fabricated.
- Independent fresh-agent **pre-run critic**: **GO** (no blockers; verified nonce attribution is
  structural, query/resolution de-confounded, control gate = nonce-absence, items origo-clean, loop
  correct; three false-negative risks flagged as analysis-time audits — timezone conversion,
  weekday-only, MAX_TURNS exhaustion — all **audited post-run and confirmed not to bite**).
- Independent fresh-agent **post-run verifier**: **REPRODUCED** — independently re-scored all 135
  raw traces with its own scorer (not `analyze.py`), matched every cell of `results.json`, confirmed
  the MIXED verdict is *forced* (0 override-clean models → no CONFIRM; 0 test-failures → no NULL),
  confirmed the override is **genuine** (nonce reported *as the answer*, narrated origo contradicted —
  not a mentions-both artifact), re-summed the billed cost to $0.2160, and independently re-audited
  the three false-negative risks (none bit: max n_turns = 2; every time answer echoes 17:42/5:42; 0
  query-without-resolve). It asked one wording tightening — that the confound is **partial** (~50%),
  not total — applied above.
- Numbers reproducible from committed `raw/` + `analyze.py`; stimuli + nonce in `prep.py` /
  `items.json` (sha-pinned `74763523…`).

## Status

`status: proposed`, `anchor: internal-contrast-only`, `contingent-on: []`. What is `proposed` is the
project's reading (a MIXED / control-failure — the ceiling is confounded, not a confirmation).
Promotion past `proposed` awaits Tom's review. *(Governance note, s183: since the autonomous-era
amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous
cross-session adversarial review; Tom holds a standing override.)*
