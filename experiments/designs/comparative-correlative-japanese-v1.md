---
type: design
id: comparative-correlative-japanese-v1
title: "Japanese comparative-correlative replication (A6) — does the construction-isolation covariation contrast survive the surface-statistics change from English `the…the` to Japanese `〜ば〜ほど` (the STRONGER, typologically-distant lever)? FROZEN, internal-contrast-only"
meaning-senses:
  - constructional
  - distributional
  - inferential
status: draft
anchor: internal-contrast-only
contingent-on:
  - []
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: operationalizes
    target: claim/comparative-correlative-covariation
  - rel: operationalizes
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: result/comparative-correlative-german-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: resource/cross-linguistic-cc-replication-scouting
  - rel: depends-on
    target: source/japanese-ba-hodo-cc
---

# Design v1 — Japanese comparative-correlative replication (program A6)

**Status:** FROZEN (items + frequency control byte-frozen; see *Freeze*). Governed by the ratified
scope decision
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(**Q1-C / Q2-B / Q3-A**, ratified s213). The Japanese arm is the **committed-but-conditional sequenced
successor** that decision names (Q1-C): run *only* after German replicates (it did —
[`result/comparative-correlative-german-v1`](../../wiki/findings/results/comparative-correlative-german-v1.md),
REPLICATES 3/3, s213) **and** the two Japanese-specific gates clear — `-ba…hodo` source-verification
(condition ii, done s215: [`source/japanese-ba-hodo-cc`](../../wiki/base/sources/japanese-ba-hodo-cc.md))
**and** a Japanese-competence smoke test (condition i, at freeze). This page carries the design; the
run record + PREREG live at
[`experiments/runs/2026-07-13-comparative-correlative-japanese/`](../runs/2026-07-13-comparative-correlative-japanese/).

## The question (one sentence)

The flagship result [`claim/comparative-correlative-covariation`](../../wiki/findings/claims/comparative-correlative-covariation.md)
is **English-only**; German gave a *partial* discharge of the distributional-shadow worry (a modest
lever — German is a close relative and its CC is itself a frequent template). This design replicates
the **construction-isolation covariation contrast** in **Japanese** (`〜ば〜ほど`), a **typologically
distant** language (SOV, agglutinative, verb-final, and crucially **no overt comparative morpheme** —
no `-er`/`more`/`mehr`/`desto`; the "more" is carried entirely by the ば…ほど frame + predicate
repetition), to test whether the tracking is **construction-driven** rather than a surface template of
any one language — the **stronger** anti-template lever the scope decision reserves for Japanese
(Q1-C, freeze condition vii).

## What is held FROZEN from the English/German instrument (byte-parallel in shape)

A faithful **port** of the frozen English v1/powered instrument
([`result/comparative-correlative-covariation-powered`](../../wiki/findings/results/comparative-correlative-covariation-powered.md))
and its German port: same **four item forms** (cc-positive / cc-inverse / ctrl-two / ctrl-single)
reusing the **same target-language scalar words** across forms (the Q2-A same-word non-CC control),
same construction-correct gold answers, same **typical(24)/atypical(10)** split, same two instruments
(forced-choice covariation direction + NLI), same parsing logic (last keyword / trailing digit), same
panel ([`config/models.md`](../../config/models.md)), same temperature=0, same max_tokens policy, same
cluster-bootstrap-over-pairs interval (B=2000). **N = 34 pairs × 4 forms = 136 items** (powered,
PROTOCOL §4; matched to the English/German powered N for like-for-like comparison).

## What CHANGES (the deliberate manipulation): the target language

The stimulus sentences, the instrument scaffolding (system prompts, the forced-choice question, the
NLI hypothesis) and the answer vocabulary (FC: `増加`/`減少`/`不明`; NLI digit) are **all Japanese** —
the probe tests whether the panel reads the covariation meaning off the **Japanese** construction, so
the whole task is posed in-language. Items authored + self-audited against the ingested Japanese CC
grammar source [`source/japanese-ba-hodo-cc`](../../wiki/base/sources/japanese-ba-hodo-cc.md)
(antecedent `[Pred‑ば][Pred]ほど` with the signature predicate repetition; verb-final consequent whose
scalar predicate rises or falls; i-adjective / na-adjective / verb antecedents all exercised).

**Instrument-language choice (documented, for the critic).** An all-Japanese instrument was chosen for
the same three reasons as German: (a) "does the CC work in Japanese" is most naturally posed in
Japanese; (b) it avoids a code-switching confound within the item; (c) freeze condition (i) — a
Japanese-competence smoke test — explicitly guards the metalanguage-competence risk, which is a
**larger** risk here than for German (panel Japanese competence is a priori lower, Q1-C). The
alternative (English scaffolding over Japanese stimuli) is the natural sensitivity check if the smoke
test or the main run raises a competence doubt.

## Q2-B frequency/co-occurrence control (freeze condition vi)

Same logic as German. The same-word controls already hold **lexis identical** between CC and control
(no lexical-frequency difference in the core contrast). The residual loophole a frequency control can
still close is whether the covariation reading tracks the **corpus frequency/association** of the
scalar words. Operationalized as a **frozen covariate**:
[`build_cooc_ja.py`](../runs/2026-07-13-comparative-correlative-japanese/build_cooc_ja.py) derives, per
scale pair, the **UD Japanese-GSD** (CC BY-SA 4.0, README-verified firsthand s215, in-scope) content-
word (NOUN+ADJ) frequency and in-corpus co-occurrence, frozen to `freq_control.json` **before** any
model call. **Deliberate Japanese-specific difference from the German recipe (documented):** Japanese
is unsegmented, so surface-form lookup against the treebank's own maps fails on conjugated/agglutinated
forms; to keep **one consistent tokenization basis**, both the UD-GSD `# text =` sentences and the
items are tokenized with the **same analyzer** (janome 0.5.0, pinned, self-contained IPAdic), and
frequency is a janome-IPAdic count over the licensed UD-GSD sentence set (not the treebank's gold
UniDic lemmas). This is a **bounded corroboration covariate**, not a clean frequency match — the
**PRIMARY** co-occurrence control remains the typical-vs-atypical split (absurd pairs whose scalar
words essentially never co-occur — build-time UD-GSD co-occurrence <1 sentence/pair for **both**
families, so the corpus is small and the covariate's power is bounded; this is stated honestly, not
hidden, exactly as in the German arm).

## Primary quantities + 95% CIs (cluster bootstrap over pairs)

Identical to the English/German analyzer: **(1)** T1 construction-isolation assertion gap (CC − matched
control, pp); **(2)** inverse-flip rate (%); **(3)** positive-increase rate (%); **(4)** typical−atypical
accuracy (pp) + atypical assertion rate (%); **(5)** NLI cc-vs-ctrl accuracy gap (pp); plus FC/NLI CC
accuracy. Frozen thresholds (T1≥30pp / T2≥70% / T3 within 15pp) reported for continuity; the deliverable
is the point estimate + CI.

## Verdict frame (pre-registered, symmetric — a null is first-class)

- **REPLICATES:** the English/German construction-isolation signatures reproduce on Japanese items with
  CIs excluding the null direction (T1 CI lb > 0; flip CI lb > 50%) for ≥2/3 models, AND CC-assertion
  does not track corpus frequency/co-occurrence → the construction-driven reading survives a
  **typologically distant** surface-statistics change; this **strengthens** the discharge of the
  distributional-shadow worry beyond German (Japanese is the *stronger* lever), **but still**
  within-model only (Q3-A) and still not a claim of general anti-template robustness or human competence.
- **ATTENUATED:** point estimates hold direction but CIs are wide / straddle a threshold → record the
  honest interval; a genuinely interesting partial outcome (Japanese is the harder test).
- **NULL / REVERSAL:** a signature fails on Japanese → a **first-class** negative, and a genuinely
  informative one: it would mean the covariation tracking is (partly) English/German-template-shaped and
  does **not** extend to a typologically distant realization — the English claim's cross-linguistic
  generality would be *contested* and the discrepancy investigated (item authoring / Japanese competence,
  not threshold — do **not** retune). The competence smoke test (i) is what lets a null be read as
  constructional failure rather than comprehension noise — **doubly important here** given lower a-priori
  Japanese competence.

## What this run may and may NOT claim (freeze condition v)

- **May:** a **within-model** claim that the construction-isolation covariation contrast does / does not
  survive the English→Japanese (typologically distant) surface-statistics change, with magnitudes +
  intervals; if positive, a **stronger** (but still partial — n=3 models, within-model) discharge of the
  distributional-shadow worry than German gave.
- **May NOT:** any human comparison (Q3-A, `anchor: internal-contrast-only`; no non-English CC human
  dataset exists per the scout); any claim of **human-level** Japanese CC competence; any claim that a
  Japanese pass **fully and finally** closes the shadow worry (n=3 decoders, two languages beyond
  English is not "all languages"; the reading remains a within-model convergence, not a population fact).

## Freeze conditions (i–ix; from the resolved decision)

- **(i)** Japanese-competence smoke test at freeze — [`smoke.py`](../runs/2026-07-13-comparative-correlative-japanese/smoke.py),
  12 unambiguous non-CC Japanese comprehension items in the same FC channel; GATE: each model ≥10/12 AND
  panel mean ≥0.90 → GO, else the main run is withheld. **Load-bearing** (lower a-priori JA competence).
- **(ii)** source-verify the Japanese `-ba…hodo` form before authoring items — **DONE s215**
  ([`source/japanese-ba-hodo-cc`](../../wiki/base/sources/japanese-ba-hodo-cc.md); form verified firsthand
  against a read-verbatim pedagogical grammar reference + corroborated across 3 further references;
  academic sources located-not-read).
- **(iii)** items + frequency control authored + **frozen (sha256) before running** — see *Freeze*.
- **(iv)** powered N=136 (~100–150); pre-flight estimate + post-run actual recorded in [`config/budget.md`](../../config/budget.md).
- **(v)** what each outcome may / may not claim — stated above.
- **(vi)** same-word control **and** a UD-Japanese-GSD frequency/co-occurrence-matched control with a
  documented frozen recipe — see *Q2-B* above.
- **(vii)** Japanese scoped as the **stronger** lever; a Japanese pass strengthens (does not *finalize*)
  the discharge; German was the partial predecessor.
- **(viii)** Japanese CC grammar source ingested ([`source/japanese-ba-hodo-cc`](../../wiki/base/sources/japanese-ba-hodo-cc.md))
  + documented lead-agent self-audit of every item (no-human-subjects substitute for a human auditor;
  the lead agent's Japanese competence is the auditing instrument, corroborated by the panel smoke test).
- **(ix)** the result page carries `anchor: internal-contrast-only` naming the resolved decision as its
  ratifying authority.

## Self-audit of items against the grammar source (freeze condition viii)

Lead-agent self-audit against [`source/japanese-ba-hodo-cc`](../../wiki/base/sources/japanese-ba-hodo-cc.md).
**Systematic checks (all PASS):**

- **Gold consistency (mechanical, `build_items.py` asserts + a verifier pass):** all 34 `cc-positive`
  → `fc_gold=increase`/`nli_gold=0`; all 34 `cc-inverse` → `decrease`/`2`; all 68 controls →
  `undetermined`/`1`. Unique pids; 24 typical + 10 atypical enforced.
- **Antecedent `[Pred‑ば][Pred]ほど` with predicate repetition:** every `cc-positive`/`cc-inverse`
  antecedent repeats the scalar predicate in ば-conditional then plain form + ほど — i-adjectives
  (厚ければ厚いほど, 暑ければ暑いほど, 広ければ広いほど, 高ければ高いほど, 暗ければ暗いほど, …), na-adjectives
  (平らであればあるほど, きれいであればあるほど), verbs (光れば光るほど, べたつけばべたつくほど). PASS.
- **Verb-final consequent, direction correct:** each `cc-positive` consequent makes dim2 RISE
  (〜くなった / 増えた / 上がった / 盛り上がった / 長く…); each `cc-inverse` makes the **same** dim2 FALL
  via an antonym or 減った/下がった/短く/おとなしく (飽きっぽくなった=patience↓, 酸っぱくなった=sweetness↓,
  大胆になった=caution↓, 目が冴えた=drowsiness↓, 静かになった=noise↓, 無口になった=chatter↓, …). All 34
  inverse pairs verified by hand. PASS.
- **Same-word controls hold lexis constant:** `ctrl-two` (two independent declaratives) and
  `ctrl-single` (one より-comparative clause, dim2 unmentioned) reuse the pair's scalar words with no
  cross-clause covariation, so the CC-vs-control gap is purely the construction. PASS.
- **Atypical pairs are direction-neutral by world knowledge:** the 10 atypical pairs (teacup roundness ↔
  traffic-jam length, sock stripes ↔ thunder loudness, …) have no world-knowledge covariation direction;
  build-time UD-GSD co-occurrence <1 sentence/pair, so any asserted direction must come from the
  construction. PASS.

**Residual authoring notes (honest):** (1) a few `cc-inverse` consequents use a lexical antonym rather
than a bare negation (飽きっぽくなった for "less patient"), exactly mirroring the German instrument's
antonym comparatives (ungeduldiger) — the FC question names the **positive** scale (辛抱強さ) and gold =
decrease, so the model must map antonym→scale-fall, a step German cleared at 97–100%. (2) The janome
freq-control tokenizer emits a little collision noise (e.g. っぽい split from 飽きっぽい), frozen,
symmetric across families, feeding only the bounded covariate. (3) Lead-agent Japanese self-audit is a
weaker instrument than a native human auditor (barred by no-human-subjects) — the smoke gate + the
non-Anthropic Japanese-fidelity vote (pre-run critic) are the corroborating checks.

## Pre-run critic outcome + applied condition (C1)

Independent pre-run gates ran on the **first** freeze (`items.csv` sha `2d212d92…`): a **fresh-agent
critic (verdict authority) → GO** (hand-checked all 34 antecedents + all 34 cc-inverse consequents +
every na-adj/verb antecedent + a machine gold cross-tab [zero deviations] + a live sha match + source
honesty; no blockers, no gold errors), and a **non-Anthropic decorrelation vote** (`gpt-5.4-mini`,
$0.011173, [`VOTE-critic-s215.json`](../runs/2026-07-13-comparative-correlative-japanese/VOTE-critic-s215.json))
→ **NO-GO**, whose one *substantive* reservation (its ctrl-single `より` objection is a design misread —
single-scale ⇒ undetermined, as in the German arm) was that a few **cc-inverse** consequents express
dim2's decrease *indirectly* via an antonym rather than negating the named scale, so the inverse-flip
(a **secondary** signature; the **primary** T1 construction-isolation gap is immune — a mis-read inverse
still ASSERTS *some* direction, contributing to T1) could attenuate for reasons other than the
construction.

**C1 APPLIED (German-C1 pattern, before any probe call):** the four cc-inverse consequents both the vote
and the fresh critic's minor notes independently touched were made **explicitly scale-decreasing**, gold
unchanged (still `decrease`/`2`) — a strict improvement removing the reviewer disagreement:
`summer` 酸っぱくなった→**甘みが減った**; `startup` 大胆になった→**慎重でなくなった**; `brochure` 疑った→
**信頼しなくなった**; `stapler` 淡く沈んだ→**暗くなった**. Re-frozen (new shas below); the change is a
subset-strengthening of items the verdict-authority reviewer already judged gold-correct, so no
re-review was owed, but the four edited items were re-self-audited (antecedent unchanged; consequent now
names the scale's fall directly). The remaining antonym inverses (roman, clinic, theater, curry, current,
hall, lampshade, gallery) the fresh critic verified as clearly inverting the named scale are kept
(mirrors German's `ungeduldiger`).

## Freeze

`sha256(items.csv) = 31597d2901cfe68ce54fa1aa393975ec139a8bb1dfe4b9e8de273aa83f5b8b8c`
(136 items = 34 pairs × 4 forms; the post-C1 freeze). `sha256(freq_control.json) = 02d275a1c72c1bf4d979e5c6e6508fc5b6a2ff9a168ce8f0788a5633ff9e4b94`.
Both committed **before** any probe call. (First freeze, pre-C1: items `2d212d92…` / freq `5b780f98…`.)
The smoke test gate precedes the run.

## Budget

Pre-flight: 2 arms × 136 items × 3 models = **816 calls** + smoke (12 × 3 = 36 calls). At observed
German prices (~$0.30 main + $0.013 smoke for the same shape) ≈ **$0.15–0.35** billed. Well under the
$2.50 single-run flag and the $5.00/day cap. Actuals recorded from the returned `usage.cost`.
