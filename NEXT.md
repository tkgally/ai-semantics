# NEXT.md

## State

The project **ran its first probes of its own design** (charter §5.4 "Run") — it has moved from designing to running. Two probes landed this session (2026-05-29, workflow mode, 3 waves), both read-only against the ratified panel, both cleanly parsed (0 NA), total OpenRouter spend ≈ **$0.29** (ledger in [`config/budget.md`](config/budget.md); cap $20/mo soft — ample headroom):

1. **Comparative-correlative covariation probe** → [`result/comparative-correlative-covariation-v1`](wiki/findings/results/comparative-correlative-covariation-v1.md). The panel deploys the CC's covariation meaning **at ceiling** — construction-driven (T1 +80–90 pp over matched controls), direction-tracking (T2 inverse-flip 95–100%), n-gram-robust (T3), matching the Scivetti ≈0.90 baseline. A *positive* Tier-4 result that **overshoots** the conjecture's "narrows-but-not-closes" bet. **Lead caveat: ceiling on an easy instrument is weak evidence for the strong reading.** [`conjecture/comparative-correlative-construction`](wiki/findings/conjectures/comparative-correlative-construction.md) → `tested`; the "not closing" clause is flagged unsupported (softened, not retired).
2. **CxNLI base-vs-distinction probe** → [`result/cxnli-distinction-divergence-v1`](wiki/findings/results/cxnli-distinction-divergence-v1.md). The panel run as subjects on Scivetti's own items: the divergent-form generalization gap **reproduces** (base 84–96% ≈ human; distinction 39–64% well below human; drop 30/45/41 pp, mean ≈39, convergent across all 3 families; **conative collapses hardest, 55–75 pp**). The *off-ceiling, discriminating* negative complement to the CC ceiling positive. This is the cash-out of [`open-question/constructional-divergence-probe`](wiki/findings/open-questions/constructional-divergence-probe.md) (→ `answered`) and gives [`claim/constructional-divergent-form-generalization-gap`](wiki/findings/claims/constructional-divergent-form-generalization-gap.md) the project's **own** evidence.

Also landed: the project's **first lexical (non-grammatical) conjecture** [`conjecture/lexical-sense-gradience`](wiki/findings/conjectures/lexical-sense-gradience.md) + candidate anchor [`resource/wic-graded-usage-similarity`](wiki/base/resources/wic-graded-usage-similarity.md); the [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md) page revised to absorb both own-design results (its "first own-design probe" revision trigger fired).

**Big picture the two results sketch:** current decoders handle the *easy* direction of the upper evidence ladder (unambiguous construction → its core inference) at ceiling, and fail the *hard* direction (surface-identical form → divergent meaning). All findings stay `proposed`/modest — small N, single run, behavioral only, shared-priors caveat.

## Next concrete action (workflow-mode backlog)

1. **The headline blocker for Tom: AANN.** The AANN probe is the one priority-1 target that did **not** run — its ratified indicator needs token logprobs the ratified panel does not expose (verified against the live OpenRouter catalog). This is a queued decision, [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) (default: substitute logprob-capable, family-decorrelated panel models, keep the ratified surprisal indicator). **Once Tom rules, run the AANN probe** ([`design/aann-construction-v1`](experiments/designs/aann-construction-v1.md)) — Mahowald repo is MIT, cloneable; lock the held-out adjectives before running.
2. **The project's own conative minimal-pair probe.** The distinction probe surfaced the conative as the sharpest construction-specific failure (55–75 pp). [`conjecture/conative-construction`](wiki/findings/conjectures/conative-construction.md) is anchored (Scivetti) and its design space is ratified-adjacent; build the project's *own* verb-held-constant minimal-pair stimuli (not Scivetti's items) and run it — the cleanest next own-design probe, no new decision needed if it reuses the ratified divergence operationalization.
3. **CC v2 (escape the ceiling).** [`design/comparative-correlative-v2`](experiments/designs/comparative-correlative-v2.md) is written (conflicting-cue, multi-step, near-miss controls). Gated on [`decisions/open/cc-v2-difficulty-operationalization`](wiki/decisions/open/cc-v2-difficulty-operationalization.md) (non-urgent).
4. **Lexical wedge → runnable.** [`conjecture/lexical-sense-gradience`](wiki/findings/conjectures/lexical-sense-gradience.md) needs its anchor inspected/ratified ([`decisions/open/lexical-sense-gradience-anchor`](wiki/decisions/open/lexical-sense-gradience-anchor.md)) — a future run should fetch+inspect the Usim release (license/scale/counts unverified this run), then design the monotonicity probe with the context-similarity control.

Run `senselint.py` (0 errors) + `linkify.py` before every commit. Keep claims modest; write nulls as first-class.

## Blocked pending Tom (4 open decisions)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — **blocks the AANN probe** (the priority-1 target). Substitute the panel (default) / small-model lane / re-operationalize. Opened 2026-05-29.
- [`decisions/open/relational-anchor-shortlist`](wiki/decisions/open/relational-anchor-shortlist.md) — human dyadic-interaction anchor for the relational-meaning pilot (default: Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004). Carried over; "Decision 9" (the two-AI relational experiment) still not taken.
- [`decisions/open/lexical-sense-gradience-anchor`](wiki/decisions/open/lexical-sense-gradience-anchor.md) — anchor for the first lexical conjecture (default: Usim + WiC, pending Usim inspection). Non-blocking.
- [`decisions/open/cc-v2-difficulty-operationalization`](wiki/decisions/open/cc-v2-difficulty-operationalization.md) — difficulty axes/thresholds for CC v2. Non-urgent.

None was resolved by the loop (surfacing is the job, not ratifying).

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md` (rule 6); run discipline `PROTOCOL.md` ("continue working" ⇒ workflow mode). Read `wiki/index.md` before opening pages; **reconcile `wiki/decisions/open/` first** (4 open). The project now has 2 own-design `result` pages and a lexical axis. **The single highest-value unblock is the AANN logprob decision** — it's the only ratified-end-to-end probe still unrun. Datasets (Mahowald=MIT, Scivetti=no-license) are reachable on GitHub; mirror Mahowald, read Scivetti in place (redact dataset text from committed outputs). The panel exposes **no logprobs** on OpenRouter — any logprob/surprisal probe needs a panel substitution or the small-model lane.
