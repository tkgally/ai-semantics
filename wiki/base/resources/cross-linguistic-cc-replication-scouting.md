---
type: resource
id: cross-linguistic-cc-replication-scouting
title: "Cross-linguistic comparative-correlative replication scouting — feasibility catalog for replicating the flagship CC construction result in a non-English language"
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: scouting
contingent-on: []
created: 2026-07-12
updated: 2026-07-12
links:
  - rel: depends-on
    target: claim/comparative-correlative-covariation
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: source/weissweiler-2022-comparative-correlative
---

# Cross-linguistic comparative-correlative replication scouting — replicating the flagship CC construction result in a non-English language

> **Update — s213 (2026-07-12): the scope decision this scout opened is RESOLVED.**
> [`decisions/resolved/cross-linguistic-cc-replication-scope`](../../decisions/resolved/cross-linguistic-cc-replication-scope.md)
> ratified **Q1-C / Q2-B / Q3-A** (autonomous cross-session adversarial review + non-Anthropic vote):
> German now (Japanese a committed-but-conditional successor); **both** a same-word non-CC control **and**
> a UD-German-GSD frequency/co-occurrence-matched control; internal-contrast-only. The design acting on this
> catalog is [`design/comparative-correlative-german-v1`](../../../experiments/designs/comparative-correlative-german-v1.md).

**Scouted:** 2026-07-12 (session 212, program item A6). **Purpose:** a $0 license-check and
construction-documentation feasibility catalog for the strongest un-started lever the program names
against the distributional-shadow null — a **same-construction / different-surface-statistics
replication** of the project's most robust constructional positive, the English comparative correlative
(CC), in a non-English language. This is a **scouting** note in the mould of
[`base/resources/presupposition-projection-human-anchor-scouting.md`](presupposition-projection-human-anchor-scouting.md)
and [`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md); it **adopts
nothing** and ratifies nothing. It records what was checked, honestly, including where documentation or
a license could not be verified this session. The value-laden design choices it surfaces are opened —
not decided — in [`decisions/resolved/cross-linguistic-cc-replication-scope`](../../decisions/resolved/cross-linguistic-cc-replication-scope.md).

**Honesty up front (two findings that shape everything below).**
1. **No non-English CC human-judged inference/acceptability dataset surfaced this scout.** The two
   strong CC-evaluation resources the project already knows —
   [`source/weissweiler-2022-comparative-correlative`](../sources/weissweiler-2022-comparative-correlative.md)
   (the encoder-PLM CC probe) and the Scivetti CxNLI CC subset
   ([`resource/scivetti-2025-cxnli-dataset`](scivetti-2025-cxnli-dataset.md), the English CC human
   anchor for [`claim/comparative-correlative-covariation`](../../findings/claims/comparative-correlative-covariation.md))
   — are **English-only** for the CC. Web scouting for a released, human-annotated non-English CC
   inference set (German, Japanese, or other) returned nothing citable. So a cross-linguistic CC
   replication would, on current evidence, carry **no human-comparison leg** and would be
   `internal-contrast-only` — which matches how the flagship CC result's **core** shadow-beater leg is
   already scored (see next).
2. **The core CC leg is internal-contrast and needs no external corpus to replicate.** The flagship
   claim's load-bearing signal is a **within-model** contrast: the panel asserts a covariation
   direction for ~100% of CC items but for only ~10–20% of matched **non-CC controls that reuse the
   same words** (v1 forced-choice gap +80–90 pp, 3/3; powered ≈87 pp, lb ≈78). Replicating **that**
   in another language needs only **project-authored items in the target language** (as the English v1
   used 80 project-authored items) — no human subjects, no external corpus license. The external
   resources below matter only for two optional add-ons: a *corpus-frequency-matched* control (a
   sturdier shadow control than same-word controls) and a *human-comparison* leg (absent, per finding 1).

---

## Why this is the strongest lever, stated precisely

The distributional-shadow worry for the English CC claim is concrete: *the more X, the more Y* is a
high-frequency English template, so the panel's success could be surface-template pattern-matching on a
frequent English string rather than deployment of the construction's abstract form–meaning pairing
(a two-clause proportional-covariation dependency). The English controls already guard against the
*lexical* version of this (same scalar words in non-CC syntax; absurd scale pairs against memorization).
What they cannot do is vary the **surface realization of the construction itself**.

A non-English replication does exactly that. If the panel isolates the covariation inference to the
target-language CC — vs matched non-CC controls reusing the **same target-language words** — in a
language whose CC surface form is **different** (different function words, often different word order),
then the construction-driven reading survives a surface-statistics change the English design cannot
manipulate. That is a genuinely new axis of evidence for "tracks the construction, not the English
n-gram," and it is charter-central (lexical/grammatical meaning; distributional-shadow discipline).
The prize is a **cross-linguistic internal-contrast replication**; its strength is bounded by two
things the decision must weigh — the target language's panel competence, and how *different* its
surface statistics actually are.

---

## Candidate target language 1: German — the well-documented, high-competence default

**The construction (standard German grammar; corroborating literature located, not read in full).**
German expresses the CC with the paired **`je` + comparative … , `desto`/`umso` + comparative** frame,
e.g. *je mehr du übst, desto besser wirst du* ("the more you practice, the better you get"). The
structure is standard, well-documented German grammar: the **`je`-clause is a subordinate clause
(verb-final)** and the
**`desto`/`umso`-clause is a main clause (verb-second)**; `desto` and `umso` are interchangeable in the
second clause; `je` introduces the first. There is a dedicated analytic literature — e.g. *"Je-Desto,
Je-Umso: An Analysis of the German Comparative Correlative Construction"* (Journal of Germanic
Linguistics) and *"Comparing Comparative Correlatives: The German vs. English construction network"* —
so the construction is documented well enough to **author faithful minimal-pair items** (CC vs
same-word non-CC controls) without fabricating its form. *(Titles/venues located via web search this
session; not ingested as `source` pages — do so if a design cites specific claims from them.)*

**Why German is the safe default.** (a) The panel models (`claude-sonnet-4.6`, `gpt-5.4-mini`,
`gemini-3.5-flash`) are strongly competent in German (high-resource); (b) the construction is
richly documented, lowering item-authoring fabrication risk; (c) an established German-vs-English CC
*construction-network* literature exists to anchor claims about how the two surface realizations differ.

**Why German is a weaker lever than a distant language.** The German CC is itself frequent, and German
is typologically close to English — so the "different surface statistics" gain is real but **modest**
(different function words `je…desto` and verb-final subordinate order, but a broadly parallel
two-clause comparative structure). German maximizes *competence + documentation*; it does not maximize
*surface-statistic distance*.

**Distributional-control resources (optional, for a corpus-matched control).**
- **UD German-GSD** — annotations **CC BY-SA 4.0** (verified this session via the UD treebank
  registry). **In scope** under the standing rule that UD treebanks are adoptable (s168). Usable for a
  German co-occurrence / frequency baseline to build a *corpus-frequency-matched* non-CC control, the
  way the s208/s210 C4 work built matched controls for BLiMP.
- **German frequency norms** (e.g. SUBTLEX-DE, dlexDB) exist but their **data licenses were not
  verified this scout** — treat as license-unverified, exactly as the project treats SUBTLEX-US
  (recipe-not-corpus; [`resource/subtlex-us-frequency`](subtlex-us-frequency.md)). Not needed for the
  core internal-contrast leg (same-word controls suffice, as in English v1).

---

## Candidate target language 2: Japanese — the stronger lever, higher grounding cost

**The construction (NOT fully verified this scout — flagged).** Japanese expresses a proportional CC
with a **`-ba … hodo`** frame (verb in provisional/conditional `-eba` form + repeated predicate +
`hodo`), schematically *X すればするほど Y* ("the more one does X, the more Y"). This is a real,
textbook Japanese construction, but this scout **did not pin its exact form and constraints to a
citable linguistics source** the way it did for German (the search surfaced Japanese *comparatives* work
— e.g. an arXiv logic-of-Japanese-comparatives paper — but not a clean CC-construction analysis).
**Do not author Japanese items until the construction's form is verified against a source** (a
freeze-time condition on any Japanese arm).

**Why Japanese is the stronger lever.** Typologically distant from English (SOV, agglutinative,
no overt comparative morpheme like *-er*/*more*); its CC surface realization shares almost no surface
statistics with the English template. If the panel still isolates the covariation inference there, the
construction-driven reading is far better insulated from an English-n-gram explanation than a German
replication achieves.

**Why Japanese costs more to run honestly.** (a) Panel Japanese competence is lower than German and
**must be smoke-tested at freeze** before any inference is read as constructional rather than
comprehension noise; (b) the construction's form needs source-verification first (above); (c) matched
same-word non-CC controls are harder to author faithfully in a language the lead agent cannot
self-audit as reliably.

**Distributional-control resources (optional).**
- **UD Japanese-GSD** — annotations **CC BY-SA 4.0** (verified this session; Google permitted dropping
  the NC restriction on the annotations). **In scope** (s168). **UD Japanese-PUD** also exists.
- Japanese frequency norms exist (various); **licenses not verified this scout.**

---

## What a replication design would look like (for the decision, not decided here)

The natural instrument is a **port of the English v1/powered forced-choice design** to the target
language:
- author N≈100–150 target-language CC items (scale pairs × {positive, inverse} forms) + **matched
  non-CC controls reusing the same target-language words** (the construction-isolation leg) + inverse
  items (direction-tracking, against an increase-bias readout) + absurd/atypical scale pairs (against
  memorization);
- run the ratified 3-model panel forced-choice (both orders, position-bias-netted), as in English;
- read the **construction-isolation assertion gap** and the **inverse-flip** as the primary
  internal-contrast signals; **no human-comparison claim** (finding 1) unless a license-verified
  non-English CC human set is later found.

This is a **behavioral, project-authored, internal-contrast** probe — the same shape as the English CC
runs, so no new machinery and no human-subjects exposure. Estimated cost is in line with the English CC
runs (v1: 80 authored + 30 Scivetti items, 570 calls, **$0.124** actual; the powered re-run was 136
items) — **well under $1**, so it fits a single day's headroom.

---

## What this scout could and could not establish

**Could establish (verified this session):**
- The German CC construction is documented well enough to author faithful items; its `je…desto/umso`
  form and clause structure are confirmed from the analytic literature.
- UD German-GSD and UD Japanese-GSD annotations are **CC BY-SA 4.0** and in scope for an optional
  corpus-matched control.
- A cross-linguistic CC replication is **instrumentable now** as an internal-contrast-only behavioral
  probe needing only project-authored items — no external corpus license blocks the core leg.

**Could NOT establish (honest gaps):**
- **No non-English CC human anchor.** No released, license-verified, human-judged non-English CC
  inference/acceptability dataset surfaced. The human-comparison upgrade the English claim has
  (Scivetti CxNLI) has **no cross-linguistic counterpart** located this scout; a non-English arm is
  `internal-contrast-only` unless one is later found. *(Absence of a found dataset is not proof of
  non-existence — a future scout with author contact or a different search route may locate one.)*
- **Japanese construction form unverified.** The `-ba…hodo` form was not pinned to a citable
  linguistics source this session; verify before authoring Japanese items.
- **Frequency-norm licenses (DE/JA) unverified.** Not needed for the core leg; flagged for any
  corpus-matched-control add-on.
- **Panel target-language competence unmeasured.** No smoke test was run this scout (a freeze-time
  gate, especially for Japanese).

---

## Recommendation

**A cross-linguistic CC replication is feasible now and is the strongest charter-compatible lever the
program has left un-started against the distributional-shadow null.** The honest, calibrated shape is:
a **behavioral, project-authored, internal-contrast-only** forced-choice port of the English CC design
to a non-English language, reading the construction-isolation and direction-flip legs, with **no
human-comparison claim** (no non-English CC human anchor exists this scout).

The load-bearing choice — surfaced, not decided, in
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../decisions/resolved/cross-linguistic-cc-replication-scope.md)
— is the **target language**: **German** maximizes panel competence and construction documentation but
offers a *modest* surface-statistic distance from English; **Japanese** offers a *large* surface-statistic
distance (the stronger lever) but needs construction-form verification and a panel-competence smoke test
first. A provisional default and the full option set live in that decision.

---

## Verification ledger for this scout

| Item checked | What / unit | Verdict | How checked / what stays unverified |
|---|---|---|---|
| German CC construction form | `je`+comp … `desto`/`umso`+comp; je-clause verb-final (subordinate), desto-clause verb-second (main) | **Documented** (standard grammar) | standard German grammar; corroborating analytic literature (Journal of Germanic Linguistics *Je-Desto, Je-Umso*; *Comparing Comparative Correlatives* DE vs EN) located by title/venue via search, **not read in full or ingested as `source` pages** |
| Japanese CC construction form | `-ba…hodo` (`すればするほど`) proportional CC | **UNVERIFIED (form)** | search surfaced Japanese *comparatives* work, **not** a clean CC-construction analysis; verify before authoring |
| UD German-GSD license | dependency/POS annotations | **CC BY-SA 4.0** (in scope, s168) | UD treebank registry (web search); underlying source-text terms not separately audited |
| UD Japanese-GSD license | dependency/POS annotations | **CC BY-SA 4.0** (in scope, s168) | UD registry; Google permitted dropping NC on annotations; underlying content terms not audited |
| Non-English CC human dataset | released human-judged CC inference/acceptability set | **NONE FOUND** | web search (multilingual CxG / NLI benchmarks); Weissweiler 2022 + Scivetti CxNLI are English-only; absence-of-found, not proof-of-absence |
| DE/JA frequency norms | SUBTLEX-DE / dlexDB / JA norms | **license UNVERIFIED** | existence noted; licenses not checked (not needed for the core internal-contrast leg) |
| Panel target-language competence | claude/gpt/gemini in DE/JA | **not measured** | no smoke test this scout; a freeze-time gate (esp. Japanese) |

**Facts NOT verified this scout (stated honestly):**
- The German-CC analytic sources were located by title/venue via search; their specific analytic claims
  were **not** read in full or ingested as `source` pages. A design that cites them must ingest them.
- The Japanese CC construction's exact form/constraints were **not** confirmed against a linguistics
  source.
- No DE/JA frequency-norm data license was verified; none is required for the core leg.
- No non-English CC human-judged dataset was located; this is evidence of *not finding one by these
  routes*, not proof that none exists.
</content>
</invoke>
