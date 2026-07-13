# 2026-07-13 — genitive-alternation possessor-animacy probe, REP2 (fresh-item replication, program A5, session 220)

The **fresh-item replication** of the s218 genitive-animacy probe, the A2a powered-re-run pattern the
s219 promotion review named as the exact path that would earn a `claim`
([`note/genitive-alternation-animacy-promotion-refusal-v1`](../../../wiki/findings/notes/genitive-alternation-animacy-promotion-refusal-v1.md)).
s218 was **CONFIRM 3/3** but a **single run**; PROTOCOL §3 promotes only REPLICATED ∧ controls-survived.
This run re-tests the animate→s-genitive direction + the nonce-firewall survival on **disjoint items**.

## What is frozen from s218 (byte-identical, sha-verified) vs new

- **Byte-identical:** `probe.py`, `analyze.py`, `build_cooc_gen.py` (the indicator, prompt, parser,
  resampling unit, verdict rule, covariate recipe). `common.py` differs only in `HARD_STOP_USD`
  (1.30 → 1.90, documented in-file — the item count grew).
- **New:** `build_items.py` builds the fresh, disjoint item set. 36 typical + **36 nonce** frames
  (nonce arm enlarged 24→36 to power the marginal gpt firewall leg). All 108 typical possessor lemmas
  + all 36 nonce strings **certified disjoint** from s218 (`certification.json` check (D)).

## Pipeline

1. `build_items.py` → `stimuli.json` (frozen, sha in `PREREG.md`) + `certification.json` (checks
   (1)–(4), (N), and the new (D) disjointness-from-s218).
2. `build_cooc_gen.py` → `freq_control.json` (frozen, sha in `PREREG.md`). The B2 covariate on the
   fresh typical lemmas from UD English-EWT (CC BY-SA 4.0). Again near-vacuous (4/36 animate, 2/36
   inanimate lemmas with any corpus genitive) — CONFIRM rests on the nonce arm, as pre-registered.
3. `critic_vote.py` → `VOTE-critic-s220.json` (non-Anthropic pre-run decorrelation vote). Plus a
   fresh-agent pre-run critic (GO/NO-GO authority) — verdict recorded in `REVIEW-critic-s220.md`.
4. `probe.py liveness` (format gate) → `probe.py full` (1080 calls; refuses unless both shas are in
   `PREREG.md`) → `raw/probe-<model>.jsonl`.
5. `analyze.py` → `analysis.json`: within-frame animacy shifts (typical + nonce arms), covariate-
   adjusted intercept + predictive validity, graded monotonicity, pre-registered verdict.

## No new decision

The design is already ratified ([`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../../wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md),
s218). This is a within-session powered re-run under that resolved design — the dative-s175 /
sense-gradience-s181 pattern — carrying a fresh-agent pre-run critic + one non-Anthropic vote, not a
new cross-session ratification.

## Result

→ [`result/genitive-alternation-animacy-rep2`](../../../wiki/findings/results/genitive-alternation-animacy-rep2.md)
(written after the run + post-run fresh-agent verifier). Frozen run dir — do not re-run/retune.
