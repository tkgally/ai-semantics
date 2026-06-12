---
id: aann-panel-logprob-blocker
title: The ratified AANN indicator needs token logprobs the ratified panel does not expose — substitute the panel, the indicator, or the instrument?
status: resolved
opened: 2026-05-29
opened-by: orchestrator
resolved: 2026-06-12
resolved-by: autonomous (adversarial review)
resolution: RETIRE the logprob instrument-class for AANN (unexecutable under pure autonomy); do NOT retire the probe — successor decision opened at decisions/open/aann-behavioral-operationalization
contingent-artifacts:
  - design/aann-construction-v1
  - conjecture/aann-construction
---

# Decision: AANN probe is logprob-blocked on the ratified panel

## Resolution (2026-06-12, autonomous cross-session ratification — PROJECT.md §12.3)

**RETIRE the logprob instrument-class for AANN entirely — Options A and B of the ratified
[`aann-operationalization`](aann-operationalization.md), and the narrowed B1/B2 sub-options, are
all declared unexecutable under pure autonomy. Do NOT retire the AANN probe. A new
operationalization decision is opened the same session:
[`decisions/open/aann-behavioral-operationalization`](../open/aann-behavioral-operationalization.md)
(ratifiable, per Ruling 1, only by a later session's adversarial pass; the probe must not run
before that ratification).** Reviewer's rationale:

The blocker's premise is dead three ways at once. Option A of the ratified indicator (per-token
surprisal of a provided string) was verified uncomputable on OpenRouter for any model (no
echo/prompt-logprobs anywhere); Option B survives only on a 2-family panel Tom already declined as
degraded; B2 (self-hosted small-model lane) requires local GPU/torch this sandbox verifiably
lacks; and the one remaining route — a Together/Fireworks key — is constitutionally closed by
Ruling 3 of [`autonomous-era-governance`](autonomous-era-governance.md) ("the project uses only
what it can reach itself"). The logprob path is therefore not blocked but *terminated*, and an
honest record says so. Integrity note: nothing here retunes a yardstick after seeing results — no
AANN result of any kind exists. Replacing an instrument that can never be applied is not the
charter-§8 failure mode; *leaving the decision open on a premise the constitution voids* would be
the defect.

Against retiring the probe, three considerations are decisive. (1) AANN is not marginal: of the
project's 21 results, none is on AANN — the canonical CxG construction, with the repo's best
item-level human anchor (Mahowald's MTurk ratings), is the one construction whose *meaning-side*
question (gradient tracking + held-out productivity) is genuinely open in-repo. The Tier-0 ceiling
claim makes the form question uninteresting; it makes the meaning question *more* interesting.
(2) The conjecture is fully anchored and fully designed; the only casualty was the instrument —
retiring a designed, anchored, ~$1–3 conjecture because its first-choice instrument died fails the
evidential-value-per-dollar test and would look suspiciously like the less-work resolution.
(3) Refusing behavioral instruments for AANN alone would be incoherent: the project's entire
grammatical evidence ladder is built on parse-from-text behavioral instruments on this exact
panel. Both prior HOLDs were premised on a key or local compute possibly arriving later — the
premise Ruling 3 kills; the HOLDs do not bind beyond their dead premise.

Binding constraints carried into the successor decision: the primary indicator must sit in the
gradient carve-out [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md)
names (adjective-class gradient / noun-class sensitivity / frequency-controlled held-out
productivity — Mahowald Exp 2/3 ratings as anchor), with plain licit/illicit forced choice demoted
to a Tier-0 manipulation check; lock-before-run discipline (thresholds + held-out adjective list)
carries forward; and the new page must carry its own validity argument —
[`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md)
explicitly does **not** warrant a behavioral instrument. The terminated logprob path is preserved
as a bounded methodological record (this page + the feasibility note); no new `result` page is
created for it. The panel ([`config/models.md`](../../../config/models.md)) is unchanged.

## The blocker (verified 2026-05-29)

The AANN probe was the session's priority-1 target and is ratified end-to-end (anchor = Mahowald 2023, [`decisions/resolved/aann-stimulus-source`](aann-stimulus-source.md); operationalization = continuation-likelihood logprob contrast, Option A, with a prompted-`p("good")` logprob fallback, Option B, [`decisions/resolved/aann-operationalization`](aann-operationalization.md)). The Mahowald repo is MIT-licensed and was cloned and inspected — no licensing obstacle.

**The obstacle is the API.** Both ratified indicators require token log-probabilities:
- Option A scores per-token log-probability of the licit AANN string vs. four degenerate variants.
- Option B reads the response-token logprob of "good" vs "bad".

The ratified panel ([`config/models.md`](../../../config/models.md)) exposes **no token logprobs on OpenRouter**. Verified against the live model catalog on 2026-05-29:

| Panel slot | Model | `logprobs` supported? |
|---|---|---|
| panel.A | `anthropic/claude-sonnet-4.6` | **No** |
| panel.B | `openai/gpt-5.4-mini` | **No** |
| panel.C | `google/gemini-3.5-flash` | **No** |

(All Anthropic and Google models on OpenRouter return `logprobs=False`; among OpenAI models only legacy `gpt-4o`-class and a few image models expose logprobs, not the `gpt-5.x` chat line.) So neither ratified indicator can be computed on the ratified panel. The probe is **blocked, not failed** — nothing about the AANN conjecture is settled by this.

This is exactly the contingency the operationalization gate and [`config/budget.md`](../../../config/budget.md) anticipated ("If a probe demands a model not currently in the panel … flag and let Tom approve the substitution"), and the contingency the AANN design's own §2 Option-B fallback was meant to cover — but the fallback *also* needs logprobs, so it does not rescue the case here.

## Why this is a gate, not a thing the loop may quietly fix

Three ways to unblock, each a value-laden change to a *ratified* measurement (charter §8 / CLAUDE.md rule 5). The autonomous loop must not pick one silently — choosing the instrument after the panel is fixed is precisely where a loop can bias toward whatever is convenient or whatever it expects to pass.

### Option A — Substitute logprob-capable panel models (keep the ratified indicator)

Swap one or more panel slots for decorrelated, logprob-exposing models so the continuation-likelihood contrast can run as ratified. Live, family-decorrelated, logprob-capable candidates on OpenRouter (2026-05-29): `deepseek/deepseek-v4-flash` and `deepseek/deepseek-v4-pro` (DeepSeek), `x-ai/grok-4.3` / `grok-4.20` (xAI), `qwen/qwen3.7-max` and several `qwen3.5/3.6` sizes (Alibaba), `mistralai/ministral-*` (Mistral), legacy `openai/gpt-4o`/`gpt-4o-mini` (OpenAI).
- **Pro:** keeps the ratified indicator and threshold exactly; the surprisal contrast is the cleanest, most quantitative AANN measure and the one the design and [`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md) are written around. Aligns with the charter's small-model/surprisal lane (§5).
- **Con:** changes the *subjects*. The panel was chosen (config/models.md) for family decorrelation across Anthropic/OpenAI/Google; a logprob-driven swap trades that specific decorrelation for a different one. Cross-probe comparability with the comparative-correlative run (which used the original panel) is reduced. Needs a budget re-estimate (logprob scoring is still cheap, but the panel is different).

### Option B — Self-host a small open-weight model for the surprisal lane

Run the continuation-likelihood contrast on a small open-weight model locally (the charter's "small-model lane", §5: direct next-token probabilities). 
- **Pro:** true surprisal, no API logprob dependence, reusable for every future surprisal probe; cleanest realization of the ratified indicator.
- **Con:** it is then a *single* model, not the decorrelated panel — a different evidential profile (no cross-family convergence/divergence signal); needs compute and a model choice (itself a small decision); slower to stand up.

### Option C — Re-operationalize AANN to a logprob-free instrument (keep the ratified panel)

Replace the indicator with a behavioral, parse-from-text one the current panel can run — e.g. a forced-choice acceptability judgment ("Which sounds more natural, A or B?") or a prompted 1–7 rating parsed from the completion (no logprob), scored against the Mahowald degenerate-variant contrasts and MTurk gradient. (This is what the comparative-correlative probe did successfully for NLI/forced-choice.)
- **Pro:** runs today on the ratified, decorrelated panel; comparable in style to the CC run that just succeeded.
- **Con:** it is a **different ratified measurement** — `aann-operationalization` specifically ratified the logprob contrast over the prompted alternatives, and re-opening that is re-litigating a closed gate. A prompted rating also conflates "rates as good" with "is sensitive to" (the con the operationalization page already recorded for Option B), and forced-choice acceptability is closer to the Tier-0 form-acceptability that [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md) warns is *not* meaning-tracking.

## Provisional default (in force until Tom ratifies — used only to keep non-AANN work moving; the AANN probe stays UNRUN)

**Option A** (substitute logprob-capable, family-decorrelated panel models, keep the ratified surprisal indicator and T1 threshold), because it preserves the ratified *measurement* and only changes the *subjects* — the smaller of the two integrity costs — and because the surprisal contrast is the indicator the whole AANN line (conjecture predictions, the surprisal-validity claim, the held-out-adjective design) was built around. But this default is **not acted on**: no AANN probe runs and no panel is swapped until Tom rules, because changing the subjects is itself a value-laden choice the loop should not make alone.

## Update 2026-05-29 — Tom ratified "swap in models", but a live-API re-check voided the premise (re-surfaced)

Tom ratified **Option A (swap in logprob-capable models)** to keep the ratified surprisal indicator. Before running, the candidate models were tested against the **live OpenRouter API** — and the result contradicts the (2026-05-29) capability list this page was written from:

| candidate | exposes logprobs (live)? |
|---|---|
| `deepseek/deepseek-v4-pro` | **No** (`logprobs=False`) |
| `deepseek/deepseek-v4-flash` | **No** |
| `x-ai/grok-4.3` | **No** (HTTP 400, rejects the argument) |
| `qwen/qwen3.7-max` | **Yes** |
| `openai/gpt-4o`, `openai/gpt-4o-mini` | **Yes** |
| meta-llama / mistral / microsoft-phi / cohere / z-ai-glm / moonshot-kimi / amazon-nova / nvidia / perplexity | **No** or error |

**Two consequences that change the decision:**
1. **Only two decorrelated families expose logprobs** (Alibaba/Qwen + OpenAI/gpt-4o). A **3-family decorrelated logprob panel is not available** — the charter's family-decorrelation rationale can't be met for a logprob probe right now.
2. **The *primary* ratified indicator (Option A of `aann-operationalization`: per-token surprisal of a *provided* AANN string vs. degenerate variants) is uncomputable on OpenRouter at all** — no model offers echo / prompt-logprobs (gpt-4o-mini echo returns no token_logprobs; gpt-3.5-turbo-instruct errors; the qwen completions endpoint 404s). Only the **Option-B fallback** (next-token logprob of a prompted judgment token) is feasible, and only on the 2 families above.

So "swap in models" does **not** deliver what its ratification intended (the ratified surprisal indicator on a decorrelated panel). The honest narrowed choice, re-surfaced to Tom 2026-05-29:
- **B1 — run AANN now with Option B (prompted `p("good")`/`p("bad")` logprob) on the 2-family logprob panel** (qwen3.7-max + gpt-4o + gpt-4o-mini; note 4o/4o-mini share a family). Fastest; gets a result; but degraded (fallback indicator, 2-family decorrelation) — and Option B is close to the Tier-0 acceptability [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md) warns is not meaning-tracking.
- **B2 — small-model lane** (Tom's original Option B): self-host one small open-weight model for **true Option-A surprisal**. Now the *only* way to get the primary ratified indicator; single model, no cross-family signal.
- **B3 — re-operationalize to a logprob-free forced-choice** on the full 3-family behavioral panel (best comparability with the other own-design probes; weaker, re-opens the operationalization gate).

This is exactly the "don't let the loop pick the instrument after the panel is fixed" case, so it was not auto-resolved — awaiting Tom's corrected ruling.

**Tom's response 2026-05-29: HOLD AANN, do other work.** Presented the narrowed B1/B2/B3 choice; Tom chose to hold the AANN run rather than accept a degraded fallback-on-2-families probe, and redirected the session to now-unblocked work (off-ceiling v2 probe + the DWUG/CoSimLex lexical-anchor follow-through). **AANN stays UNRUN and this decision stays OPEN** — the clean way to run it (B2, the small-model lane for true Option-A surprisal) needs local compute stood up, deferred to a future session. No AANN result is fabricated or implied in the interim.

## What downstream is contingent on this

- [`design/aann-construction-v1`](../../../experiments/designs/aann-construction-v1.md) — unrunnable as written until this resolves; §2/§3.2 (indicator + panel) are the affected sections.
- [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md) — stays `designed`, untested.
- Any future AANN `result`/`claim`.

## Notes for the resolver

Tom: a one-line ratification is enough — "swap to [name 1–3 logprob-capable models]", "stand up the small-model lane (Option B), use [model]", or "re-operationalize to forced-choice (Option C)". If Option A, naming the substitute models (or just "pick three decorrelated logprob-capable ones") lets the next run update [`config/models.md`](../../../config/models.md) and run the probe. Reminder: this only fixes *how AANN is measured*; it does not pre-judge whether AANN comes out positive or null. The comparative-correlative probe already ran on the original panel without logprobs (forced-choice/NLI parse), so the panel is fine for *that* instrument — AANN is special only because its ratified indicator is logprob-based.
