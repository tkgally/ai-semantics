# PREREG — within-verbal cancel-default B2 calibration survey (2026-06-28, session 139)

**Frozen before any API call.** This pre-registers path (ii) of
[`open-question/within-verbal-cancel-at-ceiling`](../../../wiki/findings/open-questions/within-verbal-cancel-at-ceiling.md):
a small structured **survey** that triages candidate NEW *verbal* cancel defaults
through cheap **B2 default-at-ceiling calibrations**, *before* any matched asymmetry
battery is built. It is a **calibration only**, `internal-contrast-only` (no
human-comparison claim, no human label invented). It does **not** test
[`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md).

## The question this addresses

The conjecture is `tested` on a **weak** confirm bought across the M2 verbal-add /
nominal-cancel domain mismatch: the only B2-passing cancel default to date is **nominal**
(C2 taxonomic "a gun" ⊨ "a weapon", 1.00/1.00/1.00). Both *verbal* cancel defaults tried
floored B2 — s135 for-durative single-occurrence (0.00/0.00/0.00, a Gricean **implicature**;
structural NO-GO) and C1 telic completion (0.25/0.375/0.75, a defeasible **aspectual**
default; 0/3 at ceiling). So the **clean within-verbal generalization confirm** the conjecture
wants is un-obtained. The binding scarcity: a *verbal* lexical default the strict-NLI panel
holds as a **categorical entailment at ceiling** (B2), which a construction could then suppress.

**This survey measures whether any NEW verbal default family is held at ceiling at all** —
the empirical test of the open-question's central worry (is the matched within-verbal cancel
arm a near-**principled limit** because the panel reads natural verbal defaults as defeasible?).

## Frozen design

- **Frozen item set:** `experiments/data/monotonicity-verbal-cancel-survey/items.csv`,
  sha256[:16] **`f6f11a985f47dc89`**, committed before any API call. 18 items, 3 families × 6:
  - **implicative** — positive implicative matrix verb ⊨ infinitival complement: "Sam managed
    to open the door." ⊨ "Sam opened the door." (manage, remember, bother, happen, dare, get).
  - **factive** — factive verb ⊨ that-complement: "Sam realized that the door was open." ⊨ "The
    door was open." (realize, discover, regret, admit, notice, forget).
  - **causative-inchoative** — transitive change-of-state ⊨ inchoative result: "Sam broke the
    vase." ⊨ "The vase broke." (break, shatter, melt, tear, crack, dissolve) — chosen **distinct
    from the original conative contact-by-motion verbs** to avoid re-reading the conative.
- **Instruments:** behavioral NLI (primary) + forced-choice, temperature 0, panel
  claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. 18 × 2 × 3 = **108 calls**.
- **Indicator:** affirm-the-default rate per family (NLI label 0 = entailment; FC YES).

## Frozen B2 gate per family (NOT relaxable — same bar as C1/C2 STEP 1b)

> default affirm ≥ **0.80 in ≥ 2/3 models**, strict NLI (NLI primary, label 0 = entailment),
> temperature 0, the ratified panel.

- **A family that PASSES** is a candidate B2-passing NEW verbal default. The result then
  scrutinizes whether it admits a clean **constructional** cancel (a coercion of the conative
  type that suppresses the held entailment) **vs** a mere **lexical swap** (e.g. "managed to" →
  "tried to") or scopal/polarity flip — which would *not* be a constructional add-vs-cancel and
  would *not* license the within-verbal battery. Only a family that both passes B2 **and** admits
  a clean constructional cancel is flagged for a next-session matched battery (reusing the frozen
  B2-passing resultative ADD arm, sha `80bd4b60b55a3e60`).
- **A family that FLOORS** feeds the principled-limit closure.
- **No gate is relaxed after data** (the standing s135/C1 lesson: measure, don't assume).

## Anti-cheat

- The CSV (items + golds) is frozen and sha256-hashed before any API call.
- No cancel arm is run, so no asymmetry magnitude is computable at this gate.
- The B2 threshold (0.80, ≥2/3) is the decision's own STEP-1b bar, unchanged — **not** tuned to
  these data. A NO-GO does not relax it; a GO does not by itself confirm anything (it unblocks a
  *design* question, not a result).
- **Do-not-re-grind (binding):** this survey does **not** re-run the ruled-out s135 for-durative
  / C1 completion arms; the three families are genuinely new directions. The causative-inchoative
  family's natural cancel (imperfective/progressive) overlaps C1's aspectual territory — this is
  flagged in the result, and the calibration measures only the *result-state* entailment (a
  different inference than C1's aspectual completion).

## Procedure

1. `python3 build_items.py` — freeze + hash the CSV. ✅ (sha `f6f11a985f47dc89`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO on the frozen set + this PREREG vs the
   open-question's path (ii) and the C1/C2 calibration precedent.
3. On critic GO: `OPENROUTER_API_KEY=… python3 probe.py` (108 calls), then
   `python3 analyze_calib.py` → `raw_calib/gate.json`.
4. Independent fresh-agent **post-run verifier** recomputes every per-family cell from
   `raw_calib/*.json`.
5. Write [`result/monotonicity-verbal-cancel-survey-v1`](../../../wiki/findings/results/monotonicity-verbal-cancel-survey-v1.md).

## Human anchor

None. Within-model feasibility calibration, `internal-contrast-only`; no human-comparison claim.
