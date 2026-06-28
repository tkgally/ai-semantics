---
type: result
id: vwsd-grounding-headroom-nlbaseline-audit-v1
title: "VWSD NL-baseline magnitude run — BUILT + FROZEN, then DEFERRED at the adequacy-audit gate (pre-run-critic NO-GO): the fluent referent-naming NL channel was authored (1158 descriptions, competent on inspection) and the TEXT-NL arm is not saturated (under-det 18 / sat 77), but the held-out adequacy audit reads OUT OF BAND (two-auditor mean high-recovery 0.342 < the [0.60,0.95] floor) for a reason an independent critic verified is a SCORER-VALIDITY artifact, not a degenerate channel — the ratified deterministic scorer needs the literal target-word lemma, but VWSD target words are mostly technical/variant/proper-noun forms a competent description names by common name (~64/70 'none' items are faithful category recoveries mis-scored). Magnitude read deferred; IMAGE arm NOT read; the narrow-headroom (prediction 3) bet stays UNTESTED. No magnitude result. $3.115."
meaning-senses:
  - grounded.perceptual
  - distributional
  - referential.sense
status: proposed
anchor: internal-contrast-only
contingent-on:
  - []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: resource/vwsd-semeval-2023
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/polysemy
---

# Result: the VWSD NL-baseline magnitude run was built and frozen, then deferred at the adequacy-audit gate (pre-run-critic NO-GO) — a scorer-validity wall, not a finding about grounding

> **Status: proposed (2026-06-28, session 127).** A **build + freeze + audit attempt** of the
> natural-language-baseline magnitude probe owed by
> [`result/vwsd-grounding-headroom-v2`](vwsd-grounding-headroom-v2.md)'s first-class Limitation 1
> ("a natural-language-baseline run is owed to test magnitude"). Built under the ratified competence
> standard [`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../decisions/resolved/vwsd-nlbaseline-competence-dv.md)
> (Q1-C) with the three audit numbers ratified s127
> [`decisions/resolved/vwsd-nlbaseline-audit-params`](../../decisions/resolved/vwsd-nlbaseline-audit-params.md)
> (ADOPT-DEFAULTS). Frozen design:
> [`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md).
> **The magnitude read was DEFERRED by a fresh independent pre-run-critic NO-GO — the reused IMAGE arm
> was not read, no magnitude result was produced, and the conjecture's "narrow headroom" bet (prediction
> 3) remains UNTESTED.** This page records the attempt and the methodological wall it hit, as a
> first-class outcome; it makes **no** human-comparison claim (the magnitude vs human gold was never
> read), hence `anchor: internal-contrast-only`.

## What this run is, and why it stopped here

The grounding-headroom conjecture
[`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
has its gating **shape** supported by v2 (3/3 models, distraction-controlled), but its **magnitude**
sub-bet — prediction 3, that the residual a *fluent* text channel leaves under-determined is **narrow**
— is untested, because v2's text channel *deliberately stripped* the referent name (so "text-failed"
was partly an artifact). This run authored the missing **fluent middle**: a competent natural-language
description that **names** the depicted referent plainly (v1 named + saturated; v2 barred naming +
manufactured headroom; this is neither). The whole magnitude read hinges on certifying that channel is
neither an **oracle** (so complete it trivially makes the residual narrow) nor **degenerate-weak** (so
vague it manufactures a wide residual) — the ratified two-sided **adequacy audit** with band
`[0.60, 0.95]` on the held-out high-recovery rate. The audit gate fired **NO-GO**, so the run stopped
before the magnitude was read. That is the design working as intended (the gate "defers the run and
relaxes nothing").

## What was built and frozen (all reusable; no re-authoring spend owed)

- **1158 fluent NL descriptions** (author = panel.A `claude-sonnet-4.6`, names allowed per Q1-C) over
  the unique candidate images of the **reused** frozen N=120 (`run_items.json` sha `7f9e52fa…`,
  verbatim). `frozen/nl_descriptors.json` sha `35ec1a4e…`. 0 empty, 0 missing cost; on inspection the
  descriptions are competent and plainly referent-naming (e.g. *"A kumquat tree heavily laden with ripe
  orange kumquats…"*).
- **TEXT-NL selection arm** (120 × 3 models): accuracy **claude .833 / gpt .767 / gemini .842** — **not
  saturated** (unlike v1's .86–.88 captions), so the fluent channel leaves real per-item variation. The
  separability covariate `sep_nl_i` strata are **under-determined 18 / intermediate 25 / saturated 77**,
  and **both reported bins clear the ≥15 floor** — i.e. had the channel been certified, the binned
  magnitude read would have been creditable. `raw/text_nl.json` sha `cff671e6…`, 0 parse-fails.
- **Held-out adequacy audit** (panel.B `gpt-5.4-mini` + panel.C `gemini-3.5-flash`, both held out from
  the claude author; 120 gold descriptions each): graded none/partial/high via the **ratified
  deterministic recovery scorer** (v2's leak-audit scheme, reused verbatim — token overlap of the
  recovered phrase with the target word). Raw guesses stored (`raw/audit_calls.json` sha `3e79cfe3…`).
- **Reused verbatim by sha (NOT re-run):** the IMAGE arm (`raw/image.json` sha `6884eea0…430870`) and
  the clean DISTRACT control (`raw/distract.json` sha `f8fbb6be…`). The IMAGE arm was **not read** —
  the NO-GO came first.

## The gate that fired (the test of record for *admissibility*, before any magnitude read)

Adequacy audit, **two-auditor mean high-recovery = 0.342** (gpt 41/120 = .342; gemini 41/120 = .342),
against the ratified band **`[0.60, 0.95]`** → **OUT OF BAND, below the lower bound** → a pre-run-critic
**NO-GO that defers the magnitude read and relaxes nothing**.

**But the NO-GO is a scorer-validity wall, not a degenerate channel** (a fresh independent critic
verified this by hand-reading all 70 "none"-scored items, [run-dir `PRERUN-CRITIC.md`](../../../experiments/runs/2026-06-28-vwsd-grounding-headroom-nlbaseline/PRERUN-CRITIC.md)).
The deterministic scorer counts "high" only when the **literal target-word lemma** appears in the
recovered phrase; it has no semantic/category match. On VWSD the target words are overwhelmingly
**technical / Latinate / spelling-variant / synonym / proper-noun** forms a competent describer and a
competent auditor name by **common name**, so genuine category recoveries score "none." **Roughly 64 of
the ~70 "none" items are faithful category recoveries mis-scored** — e.g. `thymus`→"thyme",
`ara`→"macaw", `aquila`→"eagle", `mescal`→"mezcal" (spelling variant), `disk`→"vinyl record",
`supporter`→"jockstrap", `nan`→"Nan River" (proper noun). This is **exactly the validity gap the v2
design flagged** (B.4: "the leak-audit's validity is itself a later-session ratification … raw guess
stored for a later model re-grade"). The channel is, on inspection, naming referents competently; the
literal-lemma scorer cannot see it.

## What this does and does NOT establish

- **Does NOT** test prediction 3 ("narrow headroom"): the magnitude was never read. The bet is
  **untested** — neither supported nor refuted. The conjecture stays **`proposed`**.
- **Does NOT** make any human-comparison claim: the reused IMAGE arm's rescue rate against human gold
  was not computed (`anchor: internal-contrast-only`).
- **Does** establish a methodological result about the *instrument*: under the ratified deterministic
  recovery scorer, the fluent NL channel cannot be **validly certified** on VWSD, because VWSD's
  polysemous target words are mostly not the common name a competent description uses. A valid audit
  needs a **category-match** scoring rule (a held-out model re-grade of the stored guesses), surfaced as
  [`decisions/open/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/open/vwsd-nlbaseline-recovery-scorer-validity.md)
  (opened s127; provisional default Q-A; eligible s128+). The frozen descriptions, TEXT-NL arm, raw
  audit guesses, and reused IMAGE/DISTRACT arms are all **reusable verbatim** — the re-attempt owes a
  cross-session-ratified re-grade and a fresh critic GO, **no re-authoring spend**.

## Anti-cheat record

The audit numbers were ratified (s127, independent review) **before any NL description was authored**;
the descriptions + audit + `sep_nl_i` were frozen + checksummed **before** the IMAGE arm was touched;
the band `[0.60, 0.95]` was **not** relaxed despite the scorer-artifact diagnosis (the NO-GO stands
regardless of cause — the artifact reading informs only the *new* decision, never this session's gate);
the IMAGE arm was **not** read; no magnitude artifact exists. A fresh independent pre-run critic
(distinct from the build orchestrator) returned the NO-GO with anti-cheat PASS and formed no narrow/wide
preference. A valid re-grade is itself a re-derivation of the freeze and must clear its **own**
cross-session ratification + fresh critic before any future magnitude read.

## Spend

$3.11492 billed (UTC 2026-06-28): desc-preflight $0.01395 + NL descriptors $2.69918 + TEXT-NL arm
$0.36326 + adequacy audit $0.03853. No spend on the reused IMAGE/DISTRACT arms (verbatim reuse). Under
the $5/day cap. The spend bought the **durable frozen channel**; only the audit *certification* is
deferred pending a valid scorer.
