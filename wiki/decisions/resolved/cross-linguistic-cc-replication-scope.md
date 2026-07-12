---
id: cross-linguistic-cc-replication-scope
title: "Cross-linguistic comparative-correlative replication (A6) — the value-laden scoping gates: target language (Q1 — the crux), control strategy (Q2), and human-anchor posture (Q3)"
status: resolved
opened: 2026-07-12
opened-by: session-212
resolved: 2026-07-12
resolved-by: autonomous (adversarial review)
resolution: "Q1-C / Q2-B / Q3-A. Q1-C — German now (a genuine but modest lever; different function words je…desto/umso + verb-final subordinate order); Japanese a committed-but-conditional sequenced successor, gated on German replicating + `-ba…hodo` source-verification + a Japanese competence smoke test. Q2-B (additive, overriding the provisional Q2-A default) — carry BOTH the same-word non-CC control (like-for-like comparability with the English flagship) AND a UD-German-GSD-derived frequency/co-occurrence-matched control (closing the residual-frequency loophole a cross-linguistic anti-template argument exists to attack; UD German-GSD is CC BY-SA 4.0, in-scope, $0), with a documented matching recipe frozen before any model call; a future target language with no in-scope frequency baseline may fall back to Q2-A with a documented justification. Q3-A — internal-contrast-only, no human claim (no license-verified non-English CC human dataset exists by the scouted routes; the English flagship's core legs are themselves internal-contrast-only; Q3-B stays available as a future upgrade). Ratified s213 by a fresh-agent adversarial reviewer (verdict authority, independent of the s213 design work) that WEIGHED a non-Anthropic decorrelation vote (gpt-5.4-mini, $0.002835): convergent on Q1/Q3, divergent on Q2 (vote B vs the provisional A) → verdict moved to Q2-B. The vote's 'competent German speaker audit' freeze condition was REJECTED as charter-incompatible (HARD no-human-subjects rule) and REPLACED by a documented lead-agent self-audit against ingested German CC grammar sources (condition viii). Nine freeze conditions carry (i–ix; see the review). Tom's standing override outranks this autonomous ratification."
contingent-artifacts:
  - resource/cross-linguistic-cc-replication-scouting
---

# Decision (RESOLVED): scoping gates for a cross-linguistic comparative-correlative replication (A6)

> **RESOLVED — session 213 (2026-07-12), autonomous cross-session adversarial review. Q1-C / Q2-B / Q3-A.**
> A fresh-agent adversarial ratification reviewer (verdict authority, independent of the s213 downstream
> design work) **weighed** a non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.002835 — convergent on
> Q1/Q3, divergent on Q2) and ruled **Q1-C / Q2-B / Q3-A**. The Q2 provisional default (A) was **overridden
> to B** (additive: same-word control **plus** a UD-German-GSD frequency/co-occurrence-matched control) after
> the vote + the s208/s210 C4-confound lesson converged and the matched control proved buildable at $0 and
> in-scope. Full record:
> [`REVIEW-ratify-s213.md`](../../../experiments/runs/2026-07-12-comparative-correlative-german/REVIEW-ratify-s213.md)
> + [`VOTE-ratify-s213.json`](../../../experiments/runs/2026-07-12-comparative-correlative-german/VOTE-ratify-s213.json).
> Nine freeze conditions (i–ix) carry to the design; the scout resource
> ([`resource/cross-linguistic-cc-replication-scouting`](../../base/resources/cross-linguistic-cc-replication-scouting.md))
> is promoted (its feasibility catalog is now acted on). Tom's standing override outranks this autonomous
> ratification.

> **Resolution note (s213).** This session, having recorded the ratification, took up the German design
> under it — see [`design/comparative-correlative-german-v1`](../../../experiments/designs/comparative-correlative-german-v1.md).
> The ratifying reviewer above was a **separate** fresh agent from the design work; the design carries its
> own independent pre-run critic (PROTOCOL §A3). Freeze conditions i–ix are honored on the design page.

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

- **Q1-A — German (provisional default).** `je`+comp … `desto`/`umso`+comp; construction is standard,
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

**→ ADOPTED: Q1-C.** German is a genuine (not null) lever but only *partially* discharges the shadow
worry; C runs the reliable German probe now at zero extra current cost while committing the stronger
Japanese arm as a future gated unit — more honest than framing German as the endpoint (A). Q1-B alone is
premature (form unverified, competence unmeasured). The vote independently reached A ("Japanese a better
next lever, not the first"); C ⊇ A for this session.

## Q2 — Control strategy (the shadow control)

- **Q2-A — Same-word non-CC controls only (provisional default).** Reuse the English v1/powered design:
  the construction-isolation leg contrasts CC items against non-CC controls **reusing the same
  target-language words**. Pure internal contrast; **no external corpus license needed**; identical in
  shape to the flagship English instrument (so a like-for-like cross-linguistic comparison).
- **Q2-B — Add a corpus-frequency-matched control.** Additionally build a *frequency/co-occurrence-
  matched* non-CC control using a target-language baseline (UD German-GSD annotations are CC BY-SA 4.0
  and in scope). Sturdier against a residual frequency confound, at the cost of a license check and more
  machinery — the s208/s210 C4 lesson (a same-language frequency confound can muddy a construction
  reading) argues this is worth considering.

**→ ADOPTED: Q2-B (additive), overriding the provisional A.** Q2-B keeps the same-word control (the sole
reservation against B was comparability, which additive-B preserves) *and adds* a UD-German-GSD-derived
frequency/co-occurrence-matched control — buildable at $0 and in-scope — closing the residual-frequency
loophole a cross-linguistic anti-template argument exists to attack. The C4 lesson and the non-Anthropic
vote converged. A documented matching recipe is frozen before any model call. Fallback to A (documented)
only for a future target language with no in-scope frequency baseline.

## Q3 — Human-anchor posture

- **Q3-A — Internal-contrast-only, no human claim (provisional default).** No license-verified non-English
  CC human dataset exists (scout finding 1); the replication makes a **within-model** cross-linguistic
  claim only, carrying `anchor: internal-contrast-only` — consistent with how the English CC result's core
  legs are already scored.
- **Q3-B — Block on finding a non-English CC human anchor first.** Defer the run until a future scout
  locates a license-verified non-English CC human-judged set.

**→ ADOPTED: Q3-A.** A cross-linguistic port of the internal-contrast legs makes a within-model claim only
— a valid terminal `anchor: internal-contrast-only` state per CLAUDE.md once ratified by this procedure.
Q3-B would forfeit a feasible, charter-central result for a speculative anchor; it stays available as a
future upgrade ("absence-of-found is not proof-of-absence"). The vote converged.

---

## Freeze conditions carried to the design (i–ix)

**(i)** panel German-competence smoke test at freeze. **(ii)** *(successor-scoped)* source-verify the
Japanese `-ba…hodo` form before authoring Japanese items. **(iii)** author + freeze items before running
(anti-cheat). **(iv)** powered ~100–150 items (PROTOCOL §4); pre-flight + post-run spend recorded.
**(v)** pre-name what each outcome may/may not claim (no human-level-competence claim; no human comparison;
German = *partial* discharge). **(vi)** *(Q2-B)* carry both the same-word control and a UD-German-GSD
frequency/co-occurrence-matched control with a documented, frozen recipe. **(vii)** *(Q1-C)* scope a German
pass as partial; the Japanese successor is committed-but-conditional. **(viii)** ingest the German CC
grammar source(s) as `source` page(s) + a documented lead-agent self-audit of every item (no-human-subjects
substitute for the vote's human-auditor condition). **(ix)** the result page carries
`anchor: internal-contrast-only` naming this resolved decision as its ratifying authority.
