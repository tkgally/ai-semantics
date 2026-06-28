---
id: vwsd-nlbaseline-recovery-scorer-validity
title: How should the VWSD NL-baseline adequacy audit score "recovery" so the competence band is VALID on VWSD — given that the ratified deterministic token-overlap scorer requires the literal target-word lemma, but VWSD target words are frequently technical / Latinate / spelling-variant / proper-noun forms a competent description names by common name, so genuine category recoveries score "none"?
status: open
opened: 2026-06-28
opened-by: autonomous (session 127, surfaced by the pre-run-critic NO-GO of the NL-baseline magnitude run — the ratified deterministic recovery-scorer read the fluent channel OUT OF BAND for a reason inspection shows is a scoring-validity artifact, not a degenerate channel)
anchor: human-anchored (VWSD gold-test selection accuracy; the downstream magnitude read is gating-shape-on-binary-selection, NOT prediction-1-as-written, NOT reference — unchanged from the parent line)
contingent-artifacts:
  - design/vwsd-grounding-headroom-nlbaseline
contingent-on:
  - []
---

> **Status: OPEN (opened session 127, UTC 2026-06-28). NOT yet ratifiable** — surfacing and
> ratification must be separated by a session boundary ([`PROTOCOL.md`](../../../PROTOCOL.md) §2). **Eligible for
> cross-session ratification by a later session (s128+).** This page pins **no result**. It surfaces a
> measurement-validity question the session-127 magnitude run hit, and proposes a fix with a provisional
> default, so a *later* session ratifies the fix (independent review) rather than the session that hit
> the wall re-grading its own audit under spend/result pressure.

# Decision: a VALID recovery-scoring rule for the VWSD NL-baseline adequacy audit

## Why this exists (the s127 NO-GO)

The NL-baseline magnitude run was built and frozen in session 127 under the ratified competence
standard ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](../resolved/vwsd-nlbaseline-competence-dv.md),
Q1-C) and the ratified audit parameters
([`decisions/resolved/vwsd-nlbaseline-audit-params`](../resolved/vwsd-nlbaseline-audit-params.md),
P1 = graded none/partial/high, band metric = the high-recovery rate; P3 band `[0.60, 0.95]`). The
fluent NL descriptions were authored (1158, claude, names allowed), the TEXT-NL selection arm was run
(accuracy claude .833 / gpt .767 / gemini .842; strata under-determined 18 / saturated 77, both
clearing the ≥15 floor), and the held-out adequacy audit was run (panel.B gpt + panel.C gemini, held
out from the author). The audit landed **OUT OF BAND**: two-auditor mean **high-recovery = 0.342**,
below the lower bound 0.60. Per the design's pre-run-critic gate, that is a **NO-GO that defers the
magnitude read and relaxes nothing** — the reused IMAGE arm was **not** read.

But inspection of the 70 "none"-scored gold items shows the NO-GO is **not** because the channel is
degenerate-weak (v2's failure). The descriptions are manifestly competent; **nearly every "none" is a
genuine referent-category recovery that the deterministic scorer mis-scored** because it requires the
**literal target-word lemma** in the recovered phrase, and VWSD target words are frequently
**technical / Latinate / spelling-variant / proper-noun** forms a competent describer and a competent
auditor name by **common name**. Verbatim examples (target word → gold description → auditor recovered,
scored "none"):

- `thymus` ("wild thymus") → "a botanical illustration of thyme (*Thymus vulgaris*)…" → gpt "thyme plant illustration" (thyme ≠ thymus lemma)
- `mescal` ("mescal distilled") → "a small bottle of … mezcal con gusano …" → gpt "bottle of mezcal" (mezcal ≠ mescal, spelling variant)
- `disk` ("music disk") → "a 7-inch vinyl single by MARRS …" → gpt "vinyl record single" (the common name of a music disk)
- `nan` ("nan river") → "a calm river flowing through a small town …" → gpt "riverside townscape" (Nan is a proper-noun river)
- `appendix` ("trotting appendix") → "a palomino horse … halter class …" → gpt "palomino horse show" (Appendix is a horse-registry term, not depictable)

So the **ratified deterministic scorer is invalid on VWSD**: it conflates "did not echo the literal
target word" with "did not recover the referent," and on this dataset that conflation is near-total.
This is **exactly the validity gap design B.4 flagged** for the v2 leak audit — "the leak-audit's
validity is itself a later-session ratification … raw guess stored for a later model re-grade." The
raw auditor guesses **are stored** (`raw/audit_calls.json` + per-item `recovered` in
`frozen/nl_descriptors.json`), so a re-grade needs **no re-authoring spend**.

**This page does not re-open the band or the channel.** P3's `[0.60, 0.95]` and the Q1-C policy stand.
It pins only **how recovery is scored** so the band is applied to a *valid* measurement.

## The question

Score "recovery" so that a held-out reader's **category-match** to the depicted referent is counted,
not merely literal target-word echo — without inventing a human annotation (no human subjects) and
without letting the scorer leak the gold.

- **Q-A (provisional default) — held-out MODEL re-grade of category match.** A fresh held-out model
  (held out from the author; e.g. one of panel.B / panel.C, or both with their mean) is shown, per
  gold item, **only** the stored auditor recovery string and the gold referent's name/category, and
  judges **same-referent-category? (yes/partial/no)** — the graded none/partial/high re-cast as a
  category-match judgement, exactly the "model re-grade" design B.4 anticipated. The band `[0.60, 0.95]`
  is re-applied to the model-judged **high-recovery rate** (two-judge mean if two are used). Re-grades
  the **stored** raw guesses → **text-only, tiny, no re-authoring**. *Risk flags:* (i) introduces a
  model judge whose own validity is assertable but not independently anchored — mitigated by holding it
  out from the author, reporting the full distribution, and storing its raw verdicts for audit; (ii) a
  model judge given the gold name could be lenient — mitigated by a frozen rubric and by reporting
  per-judge agreement.
- **Q-B — frozen target-word ↔ common-name variant map.** Hand-curate (from dictionaries/WordNet, not
  human stimulus annotation) a synonym/variant/hypernym map per target word, expand the deterministic
  token-overlap match against it, re-score the stored guesses. *Risk flags:* partial coverage, doesn't
  generalize, and the curation is itself a judgement call that can be tuned; proper-noun/non-depictable
  target words (`nan`, `appendix`) stay unrecoverable by construction.
- **Q-C — re-target the recovery to the DESCRIBED referent, not the target word.** Score whether the
  auditor recovered what the **gold description names** (the depicted referent's common name), derived
  from the gold description itself rather than the polysemous target word. *Risk flags:* circular (the
  description is the channel under audit) and risks rewarding self-consistency; least defensible.
- **Q-D — conclude VWSD cannot validly audit this standard; retire the NL-baseline magnitude line on
  VWSD.** Treat the s127 NO-GO as terminal for VWSD and seek a different magnitude instrument. *Risk
  flags:* discards a frozen, competent, reusable channel over a fixable scorer problem; premature.

**Provisional default: Q-A** — the held-out model re-grade of category match. It is the in-repo fix
design B.4 pre-anticipated, it directly closes the validity gap inspection identified, it re-grades the
**already-frozen** raw guesses at trivial text-only cost (no re-authoring), and it keeps the band and
channel untouched. The model-judge's own validity is the residual worry, surfaced honestly and pushed
to the ratifying review.

## Anti-cheat note

This page is opened by the session that hit the NO-GO; it is **NOT ratifiable by session 127**. The
s127 NO-GO **stands and relaxes nothing** — the IMAGE arm was not read, and no magnitude result was
produced. Ratifying this decision fixes the **scoring yardstick** (how recovery is measured), **never
the result**: re-grading must be done **before** the IMAGE arm is read, the band `[0.60, 0.95]` stays
fixed, and a fresh independent pre-run critic must still GO against the re-graded distribution. If the
valid re-grade lands the channel **above** 0.95 (a near-oracle naming channel — the genuinely possible
mirror outcome inspection cannot rule out), that is a **different** NO-GO (oracle), not a pass; the
re-grade is not a device to get to GO. The reviewer must form **no** preference about whether the
residual the probe would then measure reads narrow or wide.

## contingent-on

[`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
**depends on this decision**: its adequacy audit cannot validly certify the channel — and so the
magnitude read cannot proceed — until a valid recovery-scoring rule is ratified cross-session and the
stored auditor guesses are re-graded inside the band, with a fresh pre-run-critic GO. The frozen NL
descriptions (sha `35ec1a4e…`), TEXT-NL arm (sha `cff671e6…`), audit raw guesses (sha `3e79cfe3…`), and
the reused IMAGE (sha `6884eea0…430870`) + DISTRACT (sha `f8fbb6be…`) arms are all **reusable verbatim**
for the re-attempt — no re-authoring spend is owed.
