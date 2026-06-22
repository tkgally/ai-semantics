---
type: result
id: cross-level-shared-instrument-v1
title: "Cross-level shared-instrument probe — the 'graded-aggregate / discrete-moment' shape DISSOLVES under instrument-equalization (3/3 models): the discrete-on-the-moment posture holds only at the lexical level; at the constructional and relational levels the same models take the UNCLEAR option elevated on the genuinely-ambiguous item. The deflationary default (three rhyming instrument-specific facts, not one cross-level property) stands."
meaning-senses:
  - distributional
  - referential
  - constructional
  - relational
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-22
updated: 2026-06-22
links:
  - rel: contradicts
    target: conjecture/cross-level-gradience-aggregate-not-moment
  - rel: depends-on
    target: open-question/gradience-population-not-moment
  - rel: refines
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: essay/cross-level-convergence-ladder
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: cross-level shared-instrument probe v1 — dissolution under instrument-equalization

> **Status: proposed (2026-06-22, session 84).** The first **run** of the shared-instrument
> cross-level probe built and frozen session 83, under the resolved gate
> [`decisions/resolved/cross-level-shared-instrument-operationalization`](../../decisions/resolved/cross-level-shared-instrument-operationalization.md)
> (Option A + binding conditions C1–C4, ratified session 82 — fixing the *yardstick*, never the
> result). It applies **one** frozen shared commitment instrument — a graded categorical
> decline (SAME/DIFFERENT/UNCLEAR-style) **plus** a 0–100 confidence integer — **identically**
> at three semantic levels (lexical word-sense / constructional sentence-reading / relational
> mid-record referent). Frozen `instrument.json` sha256 `3cdfe178…` (unchanged through the run).
> **Two independent fresh-agent pre-run critic GOs** (one on the design+instrument, one on a
> pre-flight parser fix — see §Parser fix); **444 calls (148 items × 3 models), $0.20656 billed,
> 0 missing cost, 0 errors, 444/444 parsed.** Independent fresh-agent **post-run verifier
> reproduced** every cell from raw.

## Lead with the cap (binding, read first)

This result makes **NO human-comparison claim**. Per the gate's Q4 it is an **internal,
within-model contrast at the weakest common strength**:

- The **lexical** leg's items are human-rated (DWUG/WiC) but the result uses them only as one
  arm of a *within-model* cross-level contrast; the lexical leg is **capped to
  usage-similarity** intermediacy (a DWUG mid-scale "bridging" pair is a human-rated
  usage-similarity midpoint, **not** a certified within-sense bridge), inherited from
  [`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md).
- The **constructional** and **relational** legs are author-constructed synthetic minimal sets
  (`internal-contrast-only`); no human-annotation claim.
- **Behavioral, not representational.** "Decline" / "commitment" means the categorical posture
  of a behavioral verdict, never a window into representation.
- **Small, clustered N**, 3 commercial 2026 models, direction-of-effect with wide
  per-cluster bootstrap CIs — **no coverage claim**.

## Headline

**The "graded-across-the-aggregate / discrete-or-uncommitted-on-the-single-moment" shape
DISSOLVES when the instrument is equalized — 3/3 models.** Under the one frozen shared
instrument, the *discrete-on-the-moment* posture (meeting a genuinely-ambiguous item with
clear-item-level commitment, near-zero explicit "UNCLEAR") holds **only at the lexical level**.
At the **constructional** and **relational** levels the *same models* take the UNCLEAR option
**elevated** on the genuinely-ambiguous item — i.e. they are **graded-on-the-moment** there.
So the moment-pole discreteness that the lexical bridging work documented is **lexical-specific,
not a cross-level property**: it does **not** survive instrument-equalization.

This is the conjecture's **pre-registered dissolution outcome** — the **first-class null**, as
reportable as a confirm. It is positive evidence for the **deflationary default** the open
question recorded: the cross-level parallel is **three rhyming, instrument-specific facts**, not
one shared property unified only by a turn of phrase. The conjecture
[`conjecture/cross-level-gradience-aggregate-not-moment`](../conjectures/cross-level-gradience-aggregate-not-moment.md)
bet *against* that default and **loses the bet**.

Per-model cross-level verdict (Q2 frozen map):

| model | interpretable levels | discrete-on-moment | graded-on-moment | verdict |
|---|---|---|---|---|
| claude | lexical, constructional, relational | **lexical only** | constructional, relational | **DISSOLVE** |
| gpt | lexical, relational (constructional NO-GO, C3) | **lexical only** | relational | **DISSOLVE** |
| gemini | lexical, constructional, relational | **lexical only** | constructional, relational | **DISSOLVE** |

## The moment axis, per level (C1: the load-bearing signal is %UNCLEAR, not confidence)

Decline rate (%UNCLEAR) on the **ambiguous** class vs the pooled **clear** classes; the 95% CI
is a clustered bootstrap of the gap (ambiguous − clear; cluster = lemma for lexical, item-set
for constructional/relational; seed 20260622, 10000 reps). "Elevated" (CI lower bound > 0) =
**graded-on-moment**; "not elevated" = **discrete/uncommitted-on-moment**.

### Lexical (bridging vs clear; n: bridging 24, clear 64) — DISCRETE 3/3

| model | clear %UNCLEAR | **bridging %UNCLEAR** | decline-gap CI | moment verdict |
|---|---|---|---|---|
| claude | 0.0% | **0.0%** | [0.00, 0.00] | **discrete** |
| gpt | 1.6% | **0.0%** | [−0.05, 0.00] | **discrete** |
| gemini | 0.0% | **0.0%** | [0.00, 0.00] | **discrete** |

Every model commits on the bridging item and **almost never** takes "UNCLEAR" — replicating the
ungraded-commitment null of [`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md)
under this shared instrument (the lexical leg reads the same way the dedicated lexical probes
did, so the dissolution is **not** an instrument artifact at the lexical end).

### Constructional (ambiguous vs clear-reading1/2; n: ambiguous 10, clear 20) — GRADED (claude, gemini); gpt NO-GO

| model | clear %UNCLEAR | **ambiguous %UNCLEAR** | decline-gap CI | moment verdict |
|---|---|---|---|---|
| claude | 15% | **80%** | [0.30, 0.95] | **graded** |
| gpt | **35%** | 100% | [0.50, 0.80] | **NO-GO (C3 fail)** |
| gemini | 10% | **80%** | [0.40, 1.00] | **graded** |

On the *same* instrument that produced near-zero lexical decline, claude and gemini take
"UNCLEAR" on 8/10 structural ambiguities (telescope-attachment, "old men and women", quantifier
scope, …) — strongly elevated over their disambiguated controls. **gpt fails the C3 clear-class
precondition** here: it declines on 35% of its *disambiguated* controls (> the 20% cap), so the
instrument does not read cleanly on gpt's clear constructional items and its constructional
level is **uninterpretable** (excluded from gpt's cross-level verdict — the C3 guard working as
designed).

### Relational (ambiguous-midrecord vs clear-determinate; n: ambiguous 10, clear 20) — GRADED 3/3

| model | clear %UNCLEAR | **ambiguous %UNCLEAR** | decline-gap CI | moment verdict |
|---|---|---|---|---|
| claude | 0% | **100%** | [1.00, 1.00] | **graded** |
| gpt | 0% | **100%** | [1.00, 1.00] | **graded** |
| gemini | 0% | **100%** | [1.00, 1.00] | **graded** |

Maximally elevated: on a stamped record where a coined term was bound to **two** figures in the
**same round** (no recency/frequency tie-break), all three models take "UNCLEAR" **every time**,
and commit cleanly (0% UNCLEAR) on the determinate controls. A clean *within-model* track of
relational indeterminacy (`internal-contrast-only`). It is exactly the posture the lexical leg
**lacks**: here the models *do* decline the genuinely-ambiguous item.

## The confidence axis (C1: corroborates, never flips a verdict; C4: a confidence-only shift is a self-report note)

Confidence is reported but is **not** load-bearing for the moment verdict (C1). The one place it
moves CI-strictly without a matching decline shift is **claude's lexical bridging confidence**
(84.9 vs clear 88.5; gap CI [−7.2, −0.01]) — flagged by **C4 as a self-report effect, not
graded-moment evidence**, consistent with [`result/lexical-bridging-context-working-surface-v1`](lexical-bridging-context-working-surface-v1.md)
(claude's self-reported confidence softens under reflection while its categorical commitment
holds). At the constructional/relational levels confidence **co-moves with** the decline (e.g.
claude relational ambiguous confidence drops to 50.0 alongside 100% decline) — corroborating, not
carrying, the graded-moment reading.

## Clear-class precondition (C3), per cell

| level | claude | gpt | gemini |
|---|---|---|---|
| lexical | PASS (clear conf 88.5, decline 0.0%) | PASS (96.5, 1.6%) | PASS (97.2, 0.0%) |
| constructional | PASS (91.2, 15%) | **FAIL (96.3, 35% > 20%)** | PASS (99.8, 10%) |
| relational | PASS (97.3, 0%) | PASS (99.1, 0%) | PASS (100.0, 0%) |

8/9 cells pass; the one failure (gpt/constructional) is reported as a precondition failure, not
rescued by re-wording (C3).

## The load-bearing caveat — what the dissolution does and does not show

The gate's **comparability crux** (Q3, disclosed before the run) is the load-bearing reading
qualifier here, and it cuts in the **deflationary** direction. The elicitation *question* is held
byte-identical across levels (same SAME/DIFFERENT/UNCLEAR + confidence frame; only the level noun
and decline gloss change), but the stimulus **body** — and with it the **kind of "in-between"** —
unavoidably differs:

- a lexical **bridging** pair is a human-rated **usage-similarity midpoint** (DURel ≈ 2–3): a
  *graded* similarity the model can still lean on and resolve to same/different;
- a constructional **ambiguous** item is a *genuine structural* two-reading (both readings fully
  available);
- a relational **ambiguous-midrecord** item is a *genuine underdetermination* (a same-round dual
  binding with no tie-break — both/neither).

So the discrete-vs-graded split tracks, at least in part, **what kind of indeterminacy each level
presents**: the models commit through a graded *similarity* but decline a genuine *both/neither*.
Whether the lexical discreteness reflects a deep model fact or merely that a usage-similarity
midpoint is a *softer* kind of ambiguity than a structural one is **not separable in this design**
(C3 guards that the instrument reads cleanly on each level's clear controls, but it cannot
neutralize the body difference — disclosed in the design doc §comparability / README). **Either
way the unified "one cross-level property" conjecture loses:** the moment-pole discreteness does
not survive equalization, and the most natural explanation of *why* (different kinds of
indeterminacy at different levels) is itself the deflationary "three instrument-specific facts"
reading. The cross-level parallel was, in the project's own prior words, "a family resemblance
among phrasings, not a demonstrated mechanism"; the cleanest discriminator now says so.

## What this resolves

- **For [`conjecture/cross-level-gradience-aggregate-not-moment`](../conjectures/cross-level-gradience-aggregate-not-moment.md):**
  its **falsify (dissolution)** criterion fires — "the shape appears under each level's own native
  instrument but dissolves when the instrument is equalized … evidence for three
  instrument-specific facts that rhyme, and the deflationary default stands confirmed." The
  conjecture moves `designed → tested`; outcome **dissolution (deflationary default stands)**.
- **For [`open-question/gradience-population-not-moment`](../open-questions/gradience-population-not-moment.md):**
  the shared-instrument cross-level probe it named as "the cleanest discriminator" has now run and
  returns **dissolution**. The OQ's own deflationary default — "three rhyming facts until a
  shared-instrument probe says otherwise" — is now **evidenced**, not merely assumed.
- **For [`essay/cross-level-convergence-ladder`](../essays/cross-level-convergence-ladder.md):**
  a candidate cross-level regularity tested at the R2 rung (one frozen instrument, survival of
  equalization) **fails to clear it** — the regularity does not survive equalization, so it does
  not earn an R2 assertion. The ladder's symmetric standard did its job (dissolution reported as
  dissolution).
- **The lexical leg is re-confirmed** under a third instrument context (ungraded commitment via
  ≈0% bridging decline; claude's confidence the lone C4 self-report softening) —
  [`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md) refined, not disturbed.

## Scope and limits (lead with these)

- **No human comparison** (gate Q4); lexical capped to usage-similarity; constructional +
  relational `internal-contrast-only`. **Behavioral, not representational.**
- **Comparability residual is load-bearing** (above): the three levels' "ambiguous" classes are
  not the same *kind* of indeterminacy; the dissolution is real under the frozen instrument but
  its mechanism is not isolated.
- **Small, clustered N** — synthetic legs are 10 sets/level (10 ambiguous + 20 controls); the
  lexical leg is 24 bridging pairs / ≈20 lemmas + 64 clear (DWUG + WiC). Direction-of-effect
  only; wide per-cluster CIs.
- **gpt's constructional leg is uninterpretable** (C3 fail) — its DISSOLVE rests on lexical
  (discrete) + relational (graded), a 2-level read.
- **Shared priors are not independent witnesses** — three decoders are not three independent
  confirmations, and three *levels* read off one model under one instrument are not three
  independent witnesses either; the *pattern* is the signal, bounded accordingly.
- **n=3 commercial 2026 models**; no claim about other models, sizes, or training regimes.

## Parser fix (disclosed; pre-flight, before any verdict was read)

At the measured budget pre-flight, live outputs exposed a **confidence-parser bug in the runner**
(`probe.py`): the original `re.findall(r"\d+", content)[0]` captured the digit **inside** the
pole tokens `READING1`/`READING2`/`FIGURE1`/`FIGURE2` (so `"READING1 99"` parsed to confidence
**1**) and leaked record stamps from reason-then-answer replies (`"…Round 5…\n\nUNCLEAR 50"` →
**5**). Unfixed, this would have spuriously failed the C3 precondition (≥70) at the
constructional/relational levels and forced a parser-driven WEAK. **Fix:** confidence is the
integer that **follows** the matched call token — faithfully implementing the frozen output
format (`"<TOKEN> <integer 0-100>, and nothing else"`). The call/decline axis is **unchanged**;
`instrument.json` is **byte-identical** (C2 sha unchanged); `analyze.py` unchanged. A **fresh
independent pre-run critic re-GO** confirmed the fix is faithful and **anti-cheat-neutral** (it
only lets a level *pass C3 and be read*; DISCRETE-vs-GRADED stays decline-driven per C1, so the
first-class null stays exactly as reachable as a confirm). The fix is committed separately and
documented in the runner docstring; the instrument.json `parse:` shorthand reconciliation is a
future re-freeze cleanup (editing it now would break the C2 hash). 444/444 records parsed; the
verifier re-derived (call, conf) from raw and matched all 444.

## Reproduce

- Stage gitignored corpus (recipe-not-corpus): the lexical leg's `prep.py` (DWUG EN, archive sha
  `64eef477…` matches pin, 48/48 stratum remap) + `map_wic_fulltext.py` (frozen WiC manifest sha
  `b8b1a7aa…` → text, archive `f1a2fb67…`). Constructional + relational items are synthetic
  (committed in the design dir).
- `python3 certify.py` (no API, 17/17 PASS), then
  `OPENROUTER_API_KEY=… python3 probe.py --run --i-have-pre-run-critic-go`, then `python3 analyze.py`.
- Design + frozen instrument + analysis:
  [`experiments/designs/cross-level-shared-instrument-v1/`](../../../experiments/designs/cross-level-shared-instrument-v1/)
  (`instrument.json` sha `3cdfe178…`; `analyze.py` 10000-rep clustered bootstrap, seed 20260622).
  Raw outputs (`raw/` — short labels + item-id/lemma pointers, **no corpus text**; synthetic-leg
  prose is about author-constructed figures only) and `analysis.json` are committed.

## Verifier note

A post-run verifier should re-derive, from raw: per-cell decline/confidence rates and the
decline-gap CI directions (lexical discrete 3/3; constructional graded for claude/gemini, gpt
C3-fail; relational graded 3/3); the three DISSOLVE cross-level verdicts; parse integrity
(444/444, the digit-in-token and "Round N" cases parse correctly); billed cost re-summed
($0.20656, 0 missing); and that no DWUG/WiC corpus text survives in committed raw.
