---
type: conjecture
id: aann-construction
title: LLMs treat the AANN ("a beautiful three days") construction as a unit, not a syntactic accident
meaning-senses:
  - constructional
  - functional-vs-formal
status: tested
contingent-on: []
created: 2026-05-28
updated: 2026-06-12
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: refines
    target: open-question/relational-meaning-pilot
  - rel: operationalizes
    target: design/aann-construction-v2
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
---

# Conjecture: LLMs treat the AANN construction as a productive unit

## Statement

The **AANN construction** — *a* + Adjective + Numeral + Plural-Noun, as in *a beautiful three days*, *a remarkable five miles*, *a long six months* — is a marked English construction where the indefinite article scopes over a plural NP, and it carries a characteristic meaning: the measured quantity is presented as a coherent, unified, often evaluated stretch. This is the canonical CxG-probing target in the Weissweiler / Tayyar Madabushi line.

The conjecture: current LLMs treat AANN as a **productive construction** in Goldberg's sense — they generalize it to held-out lexical material in a way that tracks the construction's characteristic semantics (unification + evaluation), not merely the surface pattern.

## Why this is interesting

- AANN is the cleanest existing CxG-probing target, and the recent literature gives a ready-made human-anchor inventory of licit and illicit AANN instantiations.
- It splits cleanly along `functional-vs-formal`: the *form* (a + Adj + Num + N.PL) is learnable from a small number of training examples; the *function* (unification + evaluation) is what would make this `constructional` meaning rather than memorized template.
- It is the right size for a first-pass loop turn: one construction, one probe family, multiple panel models.

## Predictions

1. LLMs assign higher continuation likelihood to AANN with **evaluatively-loaded** adjectives (*beautiful*, *gruelling*, *remarkable*) than with **neutral measure-modifying** adjectives (*approximate*, *roughly*), even controlling for unigram frequency — because the construction's meaning is partly evaluative.
2. LLMs distinguish licit AANN from minimally-different illicit variants (*a three beautiful days*; *the beautiful three days*) at a level consistent with construction-specific learning rather than n-gram coverage.
3. Panel divergence: models with more code/structured-text in training will show *less* AANN sensitivity (it's a marked colloquial construction); this is itself informative about whether constructional meaning is uniformly recoverable from text.

## What would confirm / falsify

- **Confirm:** AANN-licit vs. illicit surprisal contrast on held-out lexical items tracks the human-rated acceptability gradient in [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md), in ≥2 of 3 panel models. Concrete threshold per [`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md) (ratified 2026-05-29: continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1).
- **Weak:** contrast exists for items that appeared in training (memorization) but does not generalize to held-out adjectives.
- **Falsify:** flat or inverse contrast pattern; or contrast that tracks unigram frequency of adjective alone, not the construction.

## Human anchor

Catalogued as [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) (status: `external-only` until a future run mirrors the released repo). Mahowald 2023 (EACL) — templatic AANN stimulus generator plus MTurk acceptability ratings — supersedes the earlier "Weissweiler line" pointer in the bootstrap version of this conjecture; the Weissweiler CxG-probing papers remain a candidate secondary anchor. The anchor question was resolved 2026-05-29: Mahowald 2023 is the ratified AANN anchor (see [`decisions/resolved/aann-stimulus-source`](../../decisions/resolved/aann-stimulus-source.md)).

→ Anchor and operationalization decisions (both ratified 2026-05-29):

- [`decisions/resolved/aann-stimulus-source`](../../decisions/resolved/aann-stimulus-source.md) — ratified: Mahowald 2023 is the primary AANN anchor (Weissweiler retained as candidate secondary).
- [`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md) — ratified: continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1 + held-out adjectives, locked before the run.

## Status note

**Updated 2026-06-12: status reverted `designed` → `proposed`.** The v1 design's ratified
indicator (the logprob/surprisal contrast, Options A and B of
[`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md))
was declared **unexecutable under pure autonomy** by the cross-session adversarial review that
resolved [`decisions/resolved/aann-panel-logprob-blocker`](../../decisions/resolved/aann-panel-logprob-blocker.md)
(no OpenRouter logprobs, no local GPU, no key will be provisioned), so "designed" would be false —
[`experiments/designs/aann-construction-v1.md`](../../../experiments/designs/aann-construction-v1.md)
is retired unrun. The indicator question was **reopened** as
[`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md)
(provisional default: gradient-primary behavioral instrument on the existing panel, Mahowald
Exp 2/3 ratings as anchor). The predictions and falsification *substance* above stand; only the
indicator clause ("surprisal contrast", "continuation likelihood") is reopened — read those
through whatever instrument the new decision ratifies. The conjecture returns to `designed` when
a frozen v2 design exists under a ratified instrument.

**Updated 2026-06-12 (later session): status `proposed` → `designed`.** The instrument decision
was **ratified** by the cross-session adversarial-review procedure
([`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md),
ADOPT DEFAULT with nine binding conditions), the Mahowald repo was mirrored and verified (MIT;
Exp-2 item-level ratings usable), and the frozen behavioral v2 design now exists:
[`experiments/designs/aann-construction-v2.md`](../../../experiments/designs/aann-construction-v2.md)
(gradient-primary, dual-framing, frequency-controlled held-out arm, Tier-0 manipulation check;
read predictions 1–2 above through that instrument — "continuation likelihood" becomes "prompted
graded acceptability", with the gradient scored against the **empirical** Exp-2 MTurk cell means,
never a stipulated ordering). `contingent-on` cleared accordingly.

**Updated 2026-06-12 (same session, post-run): status `designed` → `tested` — SUPPORTED.**
The probe ran the same session (permitted: the ratification preceded the design — the decision
was opened in an earlier session) → [`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md):
all three models pass every pre-registered gate (anchored gradient ρ 0.68–0.75 at cell grain;
frequency and noun-class guards clean; held-out class-gradient replication 0.75–0.83 on the
locked frequency-matched adjective list; Tier-0 23–24/24; $0.3125, 0 missing). Read it through
the instrument's bounds: this supports the **productive-gradient** half of the conjecture
(behavior tracks the human acceptability gradient and generalizes it to novel adjectives); the
**inferential half** (does the model *use* the unification/evaluation meaning?) remains untested
— the natural v3. Prediction 3 (gpt underperforms on the gradient) was **not** borne out — a
small disconfirmed expectation, recorded on the result page. Held-out replication is uneven by
noun class (temporal stratum negative; see the result's caveat 2).

**Update 2026-06-13: the inferential-half v3 is now gated** by the open decision
[`decisions/open/aann-inferential-operationalization`](../../decisions/open/aann-inferential-operationalization.md)
(indicator choice + the anchor sub-question — Mahowald's acceptability ratings do not anchor an
inference measure); no v3 design may be frozen or run until it is ratified in a later session.
The gradient half's `tested` status is unaffected. The companion temporal held-out widening
(v2 caveat 2; same ratified instrument, no new decision) **ran the same session** →
[`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md): widening the
temporal stratum 5× (16 → 80 items) confirms caveat 2 was real — the temporal stratum is
**uniformly negative at every grain** for all three models, so held-out AANN *productivity*
(generalizing the gradient to novel adjectives) is **noun-class-dependent** (strong for
object/distance, absent for temporal). This refines, and does not overturn, the v2 overall
SUPPORTED verdict.

## Notes / caveats

- Memorization is the main confound; the held-out lexical-item check is the main defense.
- The Weissweiler line has done a version of this; the project's contribution is the **meaning-sense tagging** and the **cross-model decorrelation** angle, not novel probing of AANN per se.
