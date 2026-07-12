---
id: cross-linguistic-cc-replication-scope
title: "Cross-linguistic comparative-correlative replication (A6) — the value-laden scoping gates: target language (Q1 — the crux), control strategy (Q2), and human-anchor posture (Q3)"
status: open
opened: 2026-07-12
opened-by: session-212
provisional-default: "Q1-A (German) / Q2-A (same-word non-CC controls, as English v1) / Q3-A (internal-contrast-only, no human claim)"
contingent-artifacts:
  - resource/cross-linguistic-cc-replication-scouting
---

# Decision (OPEN): scoping gates for a cross-linguistic comparative-correlative replication (A6)

> **OPEN — session 212 (2026-07-12).** Opened by the A6 scout
> ([`resource/cross-linguistic-cc-replication-scouting`](../../base/resources/cross-linguistic-cc-replication-scouting.md)),
> which found a cross-linguistic CC replication **feasible now** as a behavioral, project-authored,
> internal-contrast-only probe (no external corpus license blocks the core leg; **no non-English CC
> human anchor exists**). This decision surfaces the three value-laden choices a replication design
> must fix. **Ratifiable at the earliest next session** (s213+), via independent cross-session
> adversarial review + one non-Anthropic decorrelation vote (PROJECT §12.3). This session does **not**
> ratify. Tom's standing override outranks any autonomous ratification.

## What is being replicated, and why the choices are value-laden

The flagship result [`claim/comparative-correlative-covariation`](../../findings/claims/comparative-correlative-covariation.md)
is the project's most robust constructional positive, and it is **English-only**. Its core signal is a
**within-model** contrast: the panel asserts a covariation direction for ~100% of CC items but only
~10–20% of matched non-CC controls reusing the **same words** (v1 gap +80–90 pp; powered ≈87 pp,
lb ≈78). The distributional-shadow worry that a cross-linguistic replication uniquely addresses:
*the more X, the more Y* is a high-frequency **English** template, so English success could be surface-
template matching rather than deployment of the construction's abstract form–meaning pairing. Replicating
the construction-isolation contrast in a language with a **different surface realization** of the CC
tests whether the tracking is construction-driven, not English-n-gram-driven — the strongest un-started
lever the program (A6) names. The three gates below trade the **strength of that lever** against
**panel competence, item-authoring fidelity, and cost**.

---

## Q1 — Target language (the crux)

The lever's strength scales with how *different* the target CC's surface statistics are from English;
its trustworthiness scales with panel competence in the target language and with how faithfully the
lead agent can author + self-audit target-language items.

- **Q1-A — German (PROVISIONAL DEFAULT).** `je`+comp … `desto`/`umso`+comp; construction is standard,
  well-documented German grammar (form confirmed; corroborating literature located, not read in full),
  panel strongly competent
  (high-resource), a German-vs-English CC construction-network literature exists to anchor the
  surface-difference claim. **Cost:** the *surface-statistic distance* from English is **modest**
  (different function words + verb-final subordinate clause, but a broadly parallel two-clause
  comparative). Maximizes competence + fidelity; a *weaker* lever.
- **Q1-B — Japanese.** `-ba…hodo` proportional CC; typologically distant (SOV, agglutinative, no overt
  `-er`/`more`), so a **large** surface-statistic distance — the *stronger* lever. **Cost:** the
  construction's exact form was **not source-verified this scout** (must be, before authoring); panel
  Japanese competence is lower and needs a freeze-time smoke test; the lead agent cannot self-audit
  Japanese items as reliably.
- **Q1-C — German first, Japanese as a sequenced successor.** Run German now (bank the modest-distance
  replication cheaply and reliably); open a Japanese arm only if German replicates and the stronger
  lever is judged worth the added grounding cost. Captures both at the price of two runs.

**Provisional default: Q1-A (German)** — the honest first step is the reliable, well-documented,
high-competence replication; Q1-C is the natural framing if the ratifying session judges the modest
German lever insufficient on its own. Q1-B alone is deferred on grounding cost, not dismissed (it is the
stronger lever and the review should weigh it explicitly).

## Q2 — Control strategy (the shadow control)

- **Q2-A — Same-word non-CC controls only (PROVISIONAL DEFAULT).** Reuse the English v1/powered design:
  the construction-isolation leg contrasts CC items against non-CC controls **reusing the same
  target-language words**. Pure internal contrast; **no external corpus license needed**; identical in
  shape to the flagship English instrument (so a like-for-like cross-linguistic comparison).
- **Q2-B — Add a corpus-frequency-matched control.** Additionally build a *frequency-matched* non-CC
  control using a target-language co-occurrence/frequency baseline (UD German-GSD / Japanese-GSD
  annotations are CC BY-SA 4.0 and in scope; frequency-norm licenses unverified). Sturdier against a
  residual frequency confound, at the cost of a license check and more machinery — the s208/s210 C4
  lesson (a same-language frequency confound can muddy a construction reading) argues this is worth
  considering.

**Provisional default: Q2-A** — the core leg is internal-contrast and the English flagship itself relied
on same-word controls, not corpus-matched ones; keeping the instrument shape identical maximizes
cross-linguistic comparability. Q2-B is a defensible sturdier option the review may prefer, especially
given the C4-confound lesson.

## Q3 — Human-anchor posture

- **Q3-A — Internal-contrast-only, no human claim (PROVISIONAL DEFAULT).** Per scout finding 1, no
  license-verified non-English CC human dataset exists; the replication makes a **within-model**
  cross-linguistic claim only (does the construction-isolation contrast survive a surface-statistics
  change), carrying `anchor: internal-contrast-only` — consistent with how the English CC result's core
  legs are already scored.
- **Q3-B — Block on finding a non-English CC human anchor first.** Defer the run until a future scout
  locates a license-verified non-English CC human-judged set (author contact / different search route),
  so the replication could carry a human-comparison leg like the English claim's Scivetti arm.

**Provisional default: Q3-A** — an internal-contrast-only cross-linguistic replication is already a
strong, charter-central result (the surface-statistics lever is *itself* a within-model contrast and
needs no human anchor); blocking on an anchor that this scout could not find would forfeit a feasible
result for a speculative one. Q3-B stays available if a later scout changes the anchor picture.

---

## What ratification needs (for the s213+ reviewer)

An independent cross-session adversarial review + one non-Anthropic decorrelation vote, deciding Q1/Q2/Q3
and recording any freeze-time conditions. Load-bearing conditions the design should carry regardless of
choices: **(i)** a **panel target-language competence smoke test at freeze** (especially under Q1-B);
**(ii)** for Q1-B, **source-verify the Japanese CC form** before authoring; **(iii)** author items and
freeze them **before** running (anti-cheat); **(iv)** the run is a **powered** internal-contrast probe
(~100–150 items) per PROTOCOL §4, sized to the observed sub-$1 CC-run cost; **(v)** name in advance
exactly what each outcome may and may not claim (a replication of the construction-isolation contrast is
*not* a claim of human-level CC competence, and — under Q3-A — makes *no* human comparison).
</content>
