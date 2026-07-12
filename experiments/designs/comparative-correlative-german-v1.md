---
type: design
id: comparative-correlative-german-v1
title: "German comparative-correlative replication (A6) — does the construction-isolation covariation contrast survive a surface-statistics change from English `the…the` to German `je…desto/umso`? FROZEN, internal-contrast-only"
meaning-senses:
  - constructional
  - distributional
  - inferential
status: draft
anchor: internal-contrast-only
contingent-on:
  - []
created: 2026-07-12
updated: 2026-07-12
links:
  - rel: operationalizes
    target: claim/comparative-correlative-covariation
  - rel: operationalizes
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: resource/cross-linguistic-cc-replication-scouting
  - rel: depends-on
    target: source/meinunger-2023-je-desto
---

# Design v1 — German comparative-correlative replication (program A6)

**Status:** FROZEN (items + frequency control byte-frozen; see *Freeze*). Governed by the ratified
scope decision
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(**Q1-C / Q2-B / Q3-A**, ratified s213). This page carries the design; the run record + PREREG live at
[`experiments/runs/2026-07-12-comparative-correlative-german/`](../runs/2026-07-12-comparative-correlative-german/).

## The question (one sentence)

The flagship result [`claim/comparative-correlative-covariation`](../../wiki/findings/claims/comparative-correlative-covariation.md)
is **English-only**; *the more X, the more Y* is a high-frequency **English** template, so English
success could be surface-template matching. This design replicates the **construction-isolation
covariation contrast** in **German** (`je`+comp … `desto`/`umso`+comp — different function words,
verb-final subordinate clause), a language with a **different surface realization** of the CC, to test
whether the tracking is **construction-driven, not English-n-gram-driven**.

## What is held FROZEN from the English instrument (byte-parallel in shape)

A faithful **port** of the frozen English v1/powered instrument
([`result/comparative-correlative-covariation-powered`](../../wiki/findings/results/comparative-correlative-covariation-powered.md)):
same **four item forms** (cc-positive / cc-inverse / ctrl-two / ctrl-single) reusing the **same
target-language scalar words** across forms (the Q2-A same-word non-CC control), same
construction-correct gold answers, same **typical(24)/atypical(10)** split, same two instruments
(forced-choice covariation direction + NLI), same parsing logic (last keyword / trailing digit), same
panel ([`config/models.md`](../../config/models.md)), same temperature=0, same max_tokens policy, same
cluster-bootstrap-over-pairs interval (B=2000). **N = 34 pairs × 4 forms = 136 items** (powered,
PROTOCOL §4; matched to the English powered N for like-for-like comparison).

## What CHANGES (the deliberate manipulation): the target language

The stimulus sentences, the instrument scaffolding (system prompts, the forced-choice question, the
NLI hypothesis) and the answer vocabulary (FC: `ZUNAHME`/`ABNAHME`/`UNBESTIMMT`; NLI digit) are **all
German** — the probe tests whether the panel reads the covariation meaning off the **German**
construction, so the whole task is posed in-language. Items authored + self-audited against the
ingested German CC grammar source [`source/meinunger-2023-je-desto`](../../wiki/base/sources/meinunger-2023-je-desto.md)
(`je`-clause verb-final subordinate; `desto`/`umso`-clause verb-second main; `desto`≡`umso`).

**Instrument-language choice (documented, for the critic).** An all-German instrument was chosen over
a mixed German-stimulus / English-question instrument because (a) "does the CC work in German" is most
naturally posed in German; (b) it avoids a code-switching confound within the item; (c) freeze
condition (i) — a German-competence smoke test — explicitly guards the metalanguage-competence risk an
all-German instrument introduces. The alternative (English scaffolding, isolating stimulus
comprehension from German metalanguage production) is the natural sensitivity check if the smoke test
or the main run raises a competence doubt.

## Q2-B frequency/co-occurrence control (freeze condition vi)

The same-word controls already hold **lexis identical** between CC and control (no lexical-frequency
difference in the core contrast). The residual loophole a frequency control can still close — named by
the ratifying reviewer + the non-Anthropic vote — is whether the covariation reading tracks the
**corpus frequency/association** of the scalar words rather than the construction. Operationalized as a
**frozen covariate**, not a separate item arm: [`build_cooc_de.py`](../runs/2026-07-12-comparative-correlative-german/build_cooc_de.py)
derives, per scale pair, the **UD German-GSD** (CC BY-SA 4.0, in-scope) content-word (ADJ+NOUN) lemma
frequency and in-corpus co-occurrence — resolved automatically from the treebank's own form→lemma /
form→UPOS maps (no hand-specified lemmas) — frozen to `freq_control.json` **before** any model call.
`analyze.py` reports whether the CC covariation-assertion rate and the construction-isolation gap are
**independent of** corpus frequency/co-occurrence. **The PRIMARY co-occurrence control remains the
typical-vs-atypical split** (absurd pairs whose scalar words essentially never co-occur — mean UD-GSD
co-occurrence 3.4 sentences, and 1.5 words/pair are outright OOV — must get their direction from the
construction alone); the UD-GSD covariate is a **corroboration** arm whose power is bounded by the
treebank's size (co-occurrence is sparse; this is stated honestly, not hidden).

## Primary quantities + 95% CIs (cluster bootstrap over pairs)

Identical to the English powered analyzer: **(1)** T1 construction-isolation assertion gap (CC − matched
control, pp); **(2)** inverse-flip rate (%); **(3)** positive-increase rate (%); **(4)** typical−atypical
accuracy (pp) + atypical assertion rate (%); **(5)** NLI cc-vs-ctrl accuracy gap (pp); plus FC/NLI CC
accuracy. Frozen thresholds (T1≥30pp / T2≥70% / T3 within 15pp) reported for continuity; the deliverable
is the point estimate + CI.

## Verdict frame (pre-registered, symmetric — a null is first-class)

- **REPLICATES:** the English construction-isolation signatures reproduce on German items with CIs
  excluding the null direction (T1 CI lower bound > 0; flip CI lower bound > 50%) for ≥2/3 models, AND
  CC-assertion does not track corpus frequency/co-occurrence → the construction-driven reading survives
  a surface-statistics change; a **partial** discharge of the distributional-shadow worry (Q1-C: German
  is a *modest* lever; not a claim of general anti-template robustness, not a human-competence claim).
- **ATTENUATED:** point estimates hold direction but CIs are wide / straddle a threshold → record the
  honest interval.
- **NULL / REVERSAL:** a signature fails on German → a first-class negative; the English claim's
  cross-linguistic generality is *contested* and the discrepancy investigated (item authoring / German
  competence, not threshold — do **not** retune). The competence smoke test (i) is what lets a null be
  read as constructional failure rather than comprehension noise.

## What this run may and may NOT claim (freeze condition v)

- **May:** a **within-model** claim that the construction-isolation covariation contrast does / does not
  survive the English→German surface-statistics change, with magnitudes + intervals.
- **May NOT:** any human comparison (Q3-A, `anchor: internal-contrast-only`; no non-English CC human
  dataset exists per the scout); any claim of **human-level** German CC competence; any claim that a
  German pass **fully** discharges the shadow worry (it is *partial* — German is typologically close and
  its CC is itself frequent; the typologically-distant **Japanese** arm is the committed-but-conditional
  stronger successor, Q1-C).

## Freeze conditions (i–ix; from the resolved decision)

- **(i)** German-competence smoke test at freeze — [`smoke.py`](../runs/2026-07-12-comparative-correlative-german/smoke.py),
  12 unambiguous non-CC German comprehension items in the same FC channel; GATE: each model ≥10/12 AND
  panel mean ≥0.90 → GO, else the main run is withheld.
- **(ii)** *(successor)* source-verify the Japanese `-ba…hodo` form before any Japanese items — N/A this run (German).
- **(iii)** items + frequency control authored + **frozen (sha256) before running** — see *Freeze*.
- **(iv)** powered N=136 (~100–150); pre-flight estimate + post-run actual recorded in [`config/budget.md`](../../config/budget.md).
- **(v)** what each outcome may / may not claim — stated above.
- **(vi)** same-word control **and** a UD-German-GSD frequency/co-occurrence-matched control with a
  documented frozen recipe — see *Q2-B* above.
- **(vii)** German pass scoped as **partial**; Japanese successor committed-but-conditional.
- **(viii)** German CC grammar source ingested ([`source/meinunger-2023-je-desto`](../../wiki/base/sources/meinunger-2023-je-desto.md))
  + documented lead-agent self-audit of every item (no-human-subjects substitute for a human auditor).
- **(ix)** the result page carries `anchor: internal-contrast-only` naming the resolved decision as its
  ratifying authority.

## Freeze

`sha256(items.csv) = 2c2301c8bdc1eebe068cbf6fe60a17c56d4a5ec0b0030b01c83936ab573d3c92`
(136 items = 34 pairs × 4 forms). `sha256(freq_control.json) = cae2d144b2f189996a2bcbf9a94fdaf1cc4f10b095e324942f68c0712c36f823`.
Both committed **before** any probe call. Independent pre-run critic (fresh agent + one non-Anthropic
decorrelation vote) + the smoke test gate precede the run.

## Budget

Pre-flight: 2 arms × 136 items × 3 models = **816 calls** + smoke (12 × 3 = 36 calls). At observed
English CC prices (~$0.12 for 570 calls; the powered re-run ~$0.15–0.25) ≈ **$0.15–0.30** billed. Well
under the $2.50 single-run flag and the $5.00/day cap. Actuals recorded from the returned `usage.cost`.
