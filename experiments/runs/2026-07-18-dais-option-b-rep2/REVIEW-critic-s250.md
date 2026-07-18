# Fresh-agent pre-run critic — DAIS Option-B REP2 (s250), VERDICT AUTHORITY

Independent general-purpose subagent, no paid model calls; reviewed the frozen rep2 build
(`stimuli.json` `5b87f4c0…`, R3-as-CI-overlap), the byte-frozen instrument, both firewalls, the
fidelity audit, the replication predicate, and the budget arithmetic firsthand. Verbatim verdict:

---

**1. Byte-identity of the instrument — PASS.** `probe.py` = `7826bbca…` and `analyze.py` = `14065ab2…`
sha256-identical to s248 and to PREREG; `common.py` differs only in the docstring + the two budget
hard-stop constants (1.70→1.30, 3.40→2.60). No measurement-affecting difference.

**2. Freeze gate — PASS (reproducible).** Re-ran `build_trials.py`; all five artifacts rebuilt
byte-identical; on-disk `stimuli.json` sha matches PREREG; `probe.py::_require_frozen` refuses to run
unless the sha appears in PREREG.

**3. Fresh-item firewalls — PASS (both real).** vs DAIS: 0 verbatim over 10,000 strings; recipients,
10 theme heads, subject `Priya` all disjoint. vs v1: 0 verbatim; subject/recipients/theme heads
disjoint. `human_targets.json` `human_arma_matched` byte-equal to v1's (same human anchor). [At review
time] 16/40 Arm-B verbs coincided with v1's subset by chance, but each produced a fresh sentence, so
verb-overlap ≠ item-overlap.

**4. Fidelity — PASS.** The 5 recipient realizations match DAIS's factor levels exactly on word-count
(1/2/2/4/4) and definiteness; theme held fixed per verb, appears in both DOC and PD, cancels, no DOC/PD
asymmetry.

**5. Replication predicate — SOUND; R3 is not degenerately lax.** Stress-tested the "two wide CIs
always overlap" worry against v1's actual CIs (claude [+0.501,+0.700], gemini [+0.683,+0.825], gpt
[+0.542,+0.702]): a simulated **null** rep2 at n=200 yields CI-upper ≈ +0.14 (max ≈ +0.39), which
**cannot reach** v1's lowest CI-LB (+0.50). So R1 ∧ R2 ∧ R3 jointly force a moderate positive ρ; a
null-ish/weak result **cannot** satisfy the predicate. R3 is a legitimate consistent-magnitude test.

**6. Promotion scoping — SOUND.** VERB-BIAS-REPLICATES only licenses a separate cross-session promotion
review; the S1 contamination caveat + B2 alternating-only control + Q1-A firewall + "direction not
competence" scoping are adequate to keep a replicated-but-memorizable ρ from being over-read.

**7. Anti-cheat / budget — PASS.** Prior UTC-2026-07-18 spend $1.826368; + $2.60 cap = $4.43 < $5.00;
expected ~$1.82 → ~$3.65 day total. Liveness trial (`The courier handed the tenant a package.`) is
genuinely held out (subject absent from `stimuli.json`). Nothing looks chosen to make the replication
succeed; yardstick byte-inherited from s248.

**Non-binding observation.** The gate counts each conjunct independently across models
(`n(R1)≥2 ∧ n(R2)≥2 ∧ n(R3)≥2`); the per-model `all_three` field is computed but not used, so in
principle a different pair of models could carry each conjunct. This faithfully implements the frozen
predicate and mirrors the s248 `decide()` structure and creates no null-passing path — no tightening
required, but worth a one-line acknowledgment in the result page if the counts ever split across models.

**No binding conditions. `VERDICT: GO`.**

---

## Reconciliation of the two gates (recorded s250)

The fresh-agent critic (verdict authority) returned **GO** with no binding conditions and an explicit
proof that R3 (even as CI-overlap) cannot be satisfied by a null. The non-Anthropic decorrelation vote
(`gpt-5.4-mini`, QA input) returned **NO-GO** with three **tightening** FIX conditions. Per the
decorrelation rule (`config/models.md`; PROTOCOL §2) the fresh reviewer keeps verdict authority; the
vote's concerns are weighed on their merits. All three were **folded pre-data** (no model call had been
made) because each only tightens the yardstick — the s248 C1 precedent for folding a pre-data condition:

1. **FRESHNESS** (16/40 Arm-B verbs shared with v1) → Arm-B verbs now sampled from the 60 alternating
   verbs **not** in v1's subset → **0/40 shared**. `stimuli.json` re-frozen `5b87f4c0…` → `a5779f04…`.
2. **PREDICATE** (R3 CI-overlap gameable) → R3 tightened to **rep2 point estimate ∈ v1's 95% CI** (the
   documented sense-gradience-rep2 standard, strictly tighter than overlap). CI-overlap kept descriptive.
3. **PROMOTION** (should not auto-unlock) → PREREG + `replication_check.py` now state the promotion
   review is a **separate, precommitted, independent adjudication that MAY DECLINE** even when
   VERB-BIAS-REPLICATES holds; replication never auto-unlocks a claim.

The critic reviewed the pre-fold build and R3-as-overlap and gave GO; the folds only strengthen the
firewall and tighten the predicate, so the GO holds a fortiori. Net effect: a stricter instrument than
either gate reviewed. **Combined pre-run verdict: GO (yardstick tightened).**
