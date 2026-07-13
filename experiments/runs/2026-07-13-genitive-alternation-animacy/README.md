# 2026-07-13 — genitive-alternation possessor-animacy probe (program A5, session 218)

The second production-side sibling of program A5 (after the dative information-structure line). Tests
whether the panel's **genitive-alternation** preference (s-genitive *the judge's decision* vs
of-genitive *the decision of the judge*) shifts in the **human-rated possessor-animacy direction**
(animate → s-genitive; Dubois et al. 2023), and whether that shift **survives a surface-frequency
shadow control**.

## Pipeline

1. `build_items.py` → `stimuli.json` (frozen; sha in `PREREG.md`) + `certification.json`. 36 typical
   frames (animate/collective/inanimate) + 24 nonce frames (animate/inanimate, orthographically
   neutralized). Certifies within-frame length/sibilancy/definiteness matching ⇒ surface shortcut
   readers yield within-frame shift 0.
2. `build_cooc_gen.py` → `freq_control.json` (frozen; sha in `PREREG.md`). The B2 covariate:
   per-possessor-lemma marginal s-genitive propensity from UD English-EWT (CC BY-SA 4.0, license
   verified firsthand). Corroboration arm — sparse per lemma (honest power note in-file / PREREG).
3. `ratify_vote.py` → `VOTE-ratify-s218.json` (non-Anthropic decorrelation vote for the ratification).
4. `probe.py liveness` (format gate) → `probe.py full` (936 calls; refuses unless both shas are in
   `PREREG.md`) → `raw/probe-<model>.jsonl`.
5. `analyze.py` → `analysis.json`: within-frame animacy shifts (typical + nonce arms), covariate-
   adjusted intercept + covariate predictive validity, graded monotonicity, pre-registered verdict.

## Ratification (s218, cross-session adversarial review)

Decision [`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../../wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md)
→ **ADOPT DEFAULTS** (Q1-A / Q2-i / Q3 human-anchored on direction). Fresh reviewer verdict:
[`REVIEW-ratify-s218.md`](REVIEW-ratify-s218.md); weighed non-Anthropic vote [`VOTE-ratify-s218.json`](VOTE-ratify-s218.json)
(ADOPT-WITH-MODIFICATION, convergent). Freeze conditions R1–R5 honored in `PREREG.md`.

## The shadow control (the crux)

- **Nonce arm = the shortcut-immune PRIMARY control (carries the CONFIRM).** Rare/nonce possessors,
  animacy carried only by a gloss, string forms balanced/neutralized across arms — no per-lemma corpus
  statistic and no orthographic cue for a no-animacy reader to exploit.
- **Covariate = corroboration (weak).** UD-EWT marginal propensity is sparse (~8/36 animate, ~7/36
  inanimate lemmas have any corpus genitive); `analyze.py` reports its own predictive validity (b1,
  R²). Per R2/R5, CONFIRM rests on the nonce arm; the covariate leg is weak corroboration, not a
  definitive shadow-defeat.

## Result

→ [`result/genitive-alternation-animacy-v1`](../../../wiki/findings/results/genitive-alternation-animacy-v1.md).
Post-run fresh-agent verifier record in that page. Frozen run dir — do not re-run/retune.
