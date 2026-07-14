# 2026-07-15 — verb-particle placement object-givenness probe, REP2 (fresh-item replication, A5, s228)

The **fresh-item powered replication** of the s225/s226 particle-placement probe — the A2a pattern the
project uses to discharge a single-run flag and let a promotion review write a `claim`. v1 was **PANEL
CONFIRM** but a single run; this re-tests the given/definite-object → SPLIT direction + the byte-identical
discourse-givenness firewall survival on **disjoint items**, and **enlarges the load-bearing firewall arm
(40 → 48 frames)** to power the marginal **gpt** firewall leg (v1: gpt firewall +0.018, a pre-named SHADOW).

## What is frozen from v1 (byte-identical, sha-verified) vs new

- **Byte-identical:** `probe.py` (`eb50f881…`), `analyze.py` (`fd77c639…`), `build_cooc_particle.py`
  (`0dba61b2…`), `freq_control.json` (`cd472475…`) — the indicator, prompt, parser, resampling unit,
  verdict rule, covariate recipe **and data**. `common.py` differs only in `HARD_STOP_USD` (3.50 → 3.80,
  documented in-file — the item count grew).
- **New:** `build_items.py` builds the fresh, disjoint item set — **48 frames**, all 48 (verb, particle,
  noun) triples and all 48 object nouns **certified disjoint from v1** (`certification.json` checks
  (D1)/(D1b)/(D2)). Every verb+particle pair is drawn from v1's frozen 38-pair set so the byte-frozen
  covariate + `VERB_LEMMA` cover every frame (check (D3)).

## Pipeline

1. `build_items.py` → `stimuli.json` (frozen, sha `3544656488…` in `PREREG.md`) + `certification.json`
   (checks (1)–(4), (N), and the rep2 disjointness/coverage (D1)/(D1b)/(D2)/(D3)) — **CERTIFICATION PASS**.
2. `freq_control.json` reused **byte-identical** from v1 (the B2 covariate; near-vacuous, 16/38 pairs any
   token) — CONFIRM rests on the firewall arm, as pre-registered.
3. `critic_vote.py` → `VOTE-critic-s228.json` (non-Anthropic pre-run decorrelation vote). Plus a
   fresh-agent pre-run critic (GO/NO-GO authority) → `REVIEW-critic-s228.md`, and an independent
   non-authoring parallelism/disjointness certification.
4. **[DEFERRED to a full-$5 UTC day]** `probe.py liveness` → `probe.py full` (2,016 calls; refuses unless
   both shas are in `PREREG.md`) → `raw/probe-<model>.jsonl`.
5. **[DEFERRED]** `analyze.py` → `analysis.json`; post-run fresh-agent verifier; then
   `result/particle-placement-givenness-rep2` + the promotion review.

## No new decision

The design is ratified ([`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md),
s225). A within-design powered re-run under that resolved design (the dative-s175 / genitive-rep2-s220
pattern), carrying a fresh-agent pre-run critic + one non-Anthropic vote, not a new cross-session
ratification.

## ⚠ Run deferred (s228)

Frozen + fully pre-run-gated in s228, but the run was **NOT executed**: the UTC budget day was still
2026-07-14 with only ~$2.41 of $5 remaining, and the rep2 panel projects ~$3.1. No finding-bearing call
made; `raw/` empty; nothing peeked. See `PREREG.md` → "DEFERRAL" for the resume protocol. Frozen run
dir — do not re-author/retune.
