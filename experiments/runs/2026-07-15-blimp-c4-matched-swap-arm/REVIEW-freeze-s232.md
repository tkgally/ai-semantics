# REVIEW — freeze of blimp-c4-matched-swap-arm (s232, independent adversarial freeze critic)

> Independent freeze critic; did not author the recipe. Verdict authority. Read PREREG.md, build_swap_c4.py,
> build_disjoint_sample.py, analyze_swap_c4.py, probe.py, the ratified decision + REVIEW-ratify-s232.md, and
> the s210 build_swap.py/analyze_swap.py this forks byte-frozen. Verified disjoint_sample.json (sha + counts)
> and the C4 adapter scale firsthand. No models called; RUN deferred. One non-Anthropic decorrelation vote
> (`gpt-5.4-mini`, VOTE-freeze-s232.json, $0.004198 → GO-WITH-CONDITIONS, convergent) is QA input.

**VERDICT: GO-WITH-CONDITIONS** — one BLOCKER (a dead-code attrition-exclusion bug that mis-implemented the
ratified S7) + four SHOULD-FIX; every value-laden number is correctly pinned, blind, and non-promoting.

## 1. Overall — GO-WITH-CONDITIONS
The ratified gates (Q1-A dual-band / Q2-A / Q3-A) are implemented blindly and, with one exception, correctly.
Every load-bearing constant is a module-level literal before any model call (`C4_BAND=0.30`, `POOL_FLOOR=5`,
`TRIGGER_FRAC=0.25`, `C4_NUM_SHARDS=3`, `MAX_SETMEAN_C4_GAP=0.05`, `USABLE_FLOOR=60`, `MARGIN=0.05`,
`SEED=20260715`). No accuracy can enter any build-time quantity (novel words, fresh disjoint ORIGINAL, probe
unrun). The disjoint sample is certified + byte-verified. One genuine correctness bug in the analyzer's
attrition exclusion must be fixed before the RUN; the rest are non-blocking. None of the defects is
promotion-seeking; all are symmetric or conservative (push toward the inconclusive/refusing pole).

**Conditions the RUN must honor:**
- **BLOCKER F1** — Fix `analyze_swap_c4.py` `stratum_deltas`: `uid not in keep` is dead code (always False,
  since `keep` is keyed by every uid) and never drops a below-floor paradigm from the pooled stratum delta.
  Change to `not keep[uid]`. This makes the code match the already-ratified S7 (no re-ratification needed).
- **SHOULD-FIX F2** — Surface `g_C4` (the B3 adequacy set-mean) at BUILD time in `build_swap_c4.py`, not only
  in the post-run analyzer, so a MATCH-FAILURE is caught before spending $1.3–1.6.
- **SHOULD-FIX F3** — Align the PREREG/analyzer prose "CI excluding 0" with the operative (inherited) code,
  which requires the whole CI ≤ −0.05.
- **SHOULD-FIX F4** — The det-noun carve-out records an adequacy gap on a form it did not band-match;
  harmless/conservative, worth a one-line note.
- **SHOULD-FIX F5** — INSTRUMENT-FAILURE is reported as a flag, not auto-voided in the verdict string
  (inherited from s210); the run-verifier attestation must state explicitly that a fired flag voids the read.

## 2. B1 — one blind switch: PASS
C4 half-width a single fixed literal `C4_BAND=0.30`, used identically in eligibility, re-validation, and the
adequacy report — does not float on feasibility. `POOL_FLOOR=5` / `TRIGGER_FRAC=0.25` pinned literals, both
accuracy-independent (`pick_c4` reads only pool SUBTLEX freqs, C4 counts, band constants; probe unrun). The
Q1-A→Q1-B fallback is fully deterministic (`below_frac = below_floor / n_eligible_positions`;
`below_frac > TRIGGER_FRAC` re-runs `build_for_mode(..., "c4_primary")`). No residual knob.

## 3. B2 — anti-seed-shopping: PASS
Only RNG seed is `SEED=20260715`, appearing only in `build_disjoint_sample.py` (disjoint draw). `build_swap_c4.py`
has no SEED constant; substitute selection shuffles from `sha256(f"{uid}|{pid}|{i}|{tag}")` — item-hash, no
global seed to scan. Recomputed the disjoint-sample sha (payload minus `sample_sha256`, sort_keys) →
reproduces `1f90050c94…7da4e7`, 160 unique pairIDs/paradigm across all 6. No shoppable DoF.

## 4. B3 — adequacy gate: PASS (implementation), with F2
`c4_adequacy` computes `signed = c4log(orig) − c4log(swap)` from the build-recorded `sub_c4` (written at
build, pre-model), `adequate = abs(set_mean) <= 0.05` — exact `<=`, the `~` is gone; sign convention matches
PREREG. The four-outcome table evaluates MATCH-FAILURE first, so `|gap|>0.05` forces it with no DROPS/STABLE
read. C4 scale pinned 22.5M (`C4_NUM_SHARDS=3`; the monkeypatch on the adapter global takes effect). F2: the
quantity is build-determined but only *evaluated* in the post-run analyzer — compute/print `g_C4` in
`build_swap_c4.py:main` so the gate can abort pre-run.

## 5. B4 — blind-scoring lock + four-outcome ordering: PASS
Scoring code, exclusions, four-outcome table frozen; thresholds literals. If/elif order correct: (0) adequacy
MATCH-FAILURE → (1) ATTRITION-INCONCLUSIVE → (2) DEEP-STILL-DROPS → (3) DEEP-SWAP-STABLE → (4)
STILL-INCONCLUSIVE. Adequacy genuinely first; the S7 attrition fallback correctly ordered after adequacy and
before the substantive reads. `drops` (deep-only) and `stable` (both strata) mutually exclusive. F5:
`instr_fail` computed + reported but not injected into the verdict string (as in s210) — the verifier
attestation must state a fired flag voids the read.

## 6. Correctness / determinism bugs
**BLOCKER F1** — `stratum_deltas`: `keep` is keyed by every uid (`keep[uid] = mins >= USABLE_FLOOR`), so
`uid not in keep` is always False; a below-`USABLE_FLOOR` paradigm is never excluded from the pooled stratum
delta. Intended: `not keep[uid]`. Impact: when ≥2 deep clear the floor (not ATTRITION-INCONCLUSIVE) but a
third deep/shallow paradigm falls below 60, PREREG S7 requires the deep verdict re-read on the kept deep-2;
the bug instead pools the below-floor paradigm's pairs. `deep_kept`/`attrition_inconclusive` use `keep[u]`
correctly — only `stratum_deltas` used the wrong idiom, so they disagreed. One-line, deterministic, symmetric
across drops/stable — not promotion-seeking.
Everything else sound: `pick_c4` (eligibility + re-validation use the same surface form for C4 and the same
`g`/`lex[form]` for SUBTLEX as s210's `pick`; deterministic per-position shuffle; below-floor→None counted
once); the copied s210 helpers byte-faithful (only substantive edits: `pick`→`pick_c4` dual-band + `sub_c4`
recording); C4 target vocab includes every looked-up form; adapter lowercases matching `.lower()` lookups;
`boot_ci` seeded `default_rng(20260715)`; the four-outcome if/elif otherwise correct. `drops` narrowed
shallow-OR-deep → deep-only is a correct four-outcome adaptation, not a bug.
**F3** — the inherited `drops` requires the whole CI ≤ −0.05 (byte-identical to s210), stricter than the
PREREG/docstring prose "CI excluding 0"; the code is stricter than its prose (conservative), reconcile the
wording. **F4** — det-noun carve-out C4-band-matches on the *plural* form vs `c4t=c4log(singular good)` but
records/places the singular; affects only the shallow det-noun control, blind + symmetric, makes adequacy
harder to pass; one-line note. 

## 7. Promotion-seeking retune check — NONE
Bands literally symmetric (±0.05 both poles). The two real defects both cut against promotion (F3 makes the
negative harder to declare; F1 symmetric). DEEP-SWAP-STABLE earns only bounded cross-session candidacy — the
reading text hard-codes "a later cross-session review writes/refuses the claim," no code path ratifies. No
accuracy enters any build-time quantity. Successor motivation (s210 scope-cap #4) kept visible, leans toward
the refusing pole. No place aimed at re-opening R1's promotion.

**Bottom line:** Freeze is sound. Fix F1 before the RUN; address F2–F5 at the same touch. On F1's correction
the recipe faithfully implements the ratified Q1-A/Q2-A/Q3-A gates, blindly and deterministically, and may run.
