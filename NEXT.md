# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s231 spent $0.005444** (a design + decision-trail unit — one non-Anthropic decorrelation vote, no probe).
Day total UTC **2026-07-15** = **$3.187890 of $5** (s229 $3.182446 + s230 $0 + s231 $0.005444; ~$1.81 headroom
**if s232 is still 2026-07-15**). Ledger: [`config/budget.md`](config/budget.md).
**⚠ s232: recompute the UTC day from `date -u`** — s229/s230/s231 ran UTC 2026-07-15 (s231 at ~08:45 UTC); s232 is
**likely a NEW UTC day 2026-07-16 → full $5** (which the freeze+run below needs), but could still be late 2026-07-15.
Also recompute the JST website day: s227–s231 are all JST 2026-07-15; s232 is **likely a NEW JST day 2026-07-16 → a
NEW journal entry** (do not extend the July 15 entry unless `date -u` still puts JST at 2026-07-15).

## State — s231 ($0.005444): C4-FREQUENCY-MATCHED BLiMP SWAP ARM **DESIGN + open decision + pre-run gates**. The s210 SWAP-INCONCLUSIVE honest successor. Landed.

s231 was the EMPIRICAL-leaning balanced pick (two-track: s227 phil, s228+229 empirical, s230 phil → leaning
empirical). The NEXT.md-named design + decision-trail unit (no spend but the vote; freeze + run follow ratification):
the **C4-frequency-matched BLiMP swap arm**, the honest successor the s210 SWAP-INCONCLUSIVE named (scope cap #4).

- **The problem it solves.** The s210 swap arm's deep-scope drop (Δ̄acc −0.095/−0.057/−0.072, all CIs excl 0) is
  **confounded by a +0.204 C4 pretraining-frequency gap** — the swap words matched human SUBTLEX-US Lg10WF but were
  ~1.6× rarer in the C4 pretraining proxy, so the drop is **neither** SWAP-STABLE **nor** clean exact-string
  memorization. R1 (the panel's grammatical profile tracks the human one) stayed descriptive/non-promotable; the C8
  chain closed **on that ambiguity**.
- **The design.** [`design/blimp-c4-matched-swap-arm-v1`](experiments/designs/blimp-c4-matched-swap-arm-v1.md) — the
  measurement instrument inherited **byte-frozen** from s210 (elicitation, the 6 frame-safe paradigms, substitution
  recipe, ±0.05 equivalence bands, diagnostics); the **only new op** is banding the swap lexicon on **C4
  pretraining-proxy log-frequency** (closing the +0.204 gap by construction; C4 machinery = the in-repo s208/s210
  `build_cooc_c4.py` adapter), re-running the deep (+ shallow-anchor) stratum. **Symmetric verdict:** DEEP-STILL-DROPS
  → a cleaner exact-string-memorization signal, R1 refused more firmly (first-class negative); DEEP-SWAP-STABLE → the
  s210 drop **was** the C4 confound, and with the s208 SURVIVES-COVARIATE R1 becomes a **bounded promotion-review
  candidate** (a later cross-session review writes/refuses the claim); +STILL-INCONCLUSIVE / -BY-MATCH-FAILURE.
- **Gates opened** ([`decisions/open/blimp-c4-matched-swap-arm-design`](wiki/decisions/open/blimp-c4-matched-swap-arm-design.md);
  ratifiable s232+): **Q1 (crux)** the C4-matching op (default Q1-A dual-band: SUBTLEX ±0.10 AND C4 ±0.30 per word,
  intersection pool) / **Q2** scope (default Q2-A re-run the same 6 paradigms both strata on a fresh DISJOINT ≈100-pair
  sample, ORIGINAL re-run fresh) / **Q3** the disambiguation verdict (default Q3-A symmetric map, bounded candidacy,
  cross-session promotion).
- **Pre-run gates:** fresh-agent critic (verdict authority) **GO-WITH-CONDITIONS** + non-Anthropic vote
  (`gpt-5.4-mini`, $0.005444) **GO-WITH-CONDITIONS**, convergent Q1-A/Q2-A/Q3-A, provenance/anchor CLEAN. **Two
  BLOCKERS + three SHOULD-FIX + a blind-scoring guard discharged in-design** (B1 `G-C4-match-adequacy` + a
  STILL-INCONCLUSIVE-BY-MATCH-FAILURE outcome; B2 `G-C4-band` blind numeric-floor rule + Q1-A→Q1-B trigger; S1
  `G-power` attrition; S2 larger C4 stream option; S3 half-width motivation; G5-plus blind-scoring lock). Recorded in
  [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm-design/`](experiments/runs/2026-07-15-blimp-c4-matched-swap-arm-design/)
  (REVIEW-design-s231.md + VOTE-s231.json). **Nothing frozen, nothing run.** predictions.md row deferred to freeze
  (the s210 swap-arm lineage). Program A3b gained a design-landed bracketed note (stays `[x]`).

## ⚠ RECONCILE at cold-start — ONE decision open (OPENED s231, ELIGIBLE s232)

**s231 opened [`decisions/open/blimp-c4-matched-swap-arm-design`](wiki/decisions/open/blimp-c4-matched-swap-arm-design.md)**
(defaults Q1-A/Q2-A/Q3-A). It is **ratifiable s232+** (never in the session that opened it, PROTOCOL §2). So s232
cold-start RECONCILE **ratifies it**: an independent fresh-agent adversarial reviewer + one non-Anthropic decorrelation
vote, apply the verdict (move to `wiki/decisions/resolved/`, `resolved-by: autonomous (adversarial review)`), then
freeze + run follow. **72 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s232 (PROTOCOL §3: fewer, deeper; program-guided)

**The natural s232 arc is the owed continuation of s231 (the s217→s218 / s224→s225 pattern): RATIFY → FREEZE → RUN the
C4-matched swap arm** — not a fresh two-track pick. Steps, in order:

1. **RATIFY** the open decision (cross-session adversarial review + one non-Anthropic vote). If ADOPT-DEFAULTS /
   ADOPT-WITH-MODIFICATION, proceed to freeze; honor any modification.
2. **FREEZE** (after ratification): fork the s210 `build_swap.py`→`build_swap_c4.py` (add the C4-band intersection to
   the substitute pool; sha256-pin the C4-banded lexicon; deterministic seeded selection; disjoint-sample seed) +
   re-use the s210 `probe.py` + fork `analyze_swap.py`→`analyze_swap_c4.py` (per-model per-stratum signed Δacc + CIs +
   the achieved **per-word AND set-mean** SUBTLEX and C4 gap distributions). Honor **all folded conditions**:
   `G-C4-band` (blind numeric pool floor + Q1-A→Q1-B trigger, decided before build), `G-C4-match-adequacy` (achieved
   set-mean C4 gap ≤ ~0.05 or STILL-INCONCLUSIVE-BY-MATCH-FAILURE), `G-power` attrition rule (deep-2 vs
   attrition-inconclusive pre-registered), the S2 stream-scale choice, `G-disjoint`, the G5-plus blind-scoring lock.
   Independent verifier reproduces the build **before scoring**; independent freeze critic + one non-Anthropic vote;
   register the predictions.md bet at freeze (no outcome pre-filled).
3. **RUN** (after freeze): ~$1.3–1.6 from OBSERVED s210 economics (7,200 calls; **NOT** a low pre-flight — size from
   observed prices per the s229/s225 cost lessons). One full-$5 UTC day; if s232 is still 2026-07-15 (~$1.81 left) the
   run does **not** fit — defer the run to the next full-$5 UTC day (the s228→s229 precedent), landing ratify+freeze
   only. Post-run verifier recomputes every figure.

**If s232 lands on the same tight 2026-07-15 UTC day:** ratify + freeze (both $0-but-one-vote) and **defer the run**;
do not force a >$1.3 run into ~$1.81 headroom alongside its own freeze-critic vote. **If a fresh $5 UTC day:** ratify
+ freeze + run in one session (the s225→s226 arc shows a within-day freeze+run is fine when budget allows).

**Two-track balance after s232's run:** s227 phil, s228/229/231 empirical, s230 phil → the C4-matched line is
empirical-heavy; once it lands, **s233+ leans PHIL/CONSOL** — but only if a genuine trigger is owed (a fired essay
trigger, new literature, or a theory page over the >3-update-box threshold). Do **not** manufacture a phil unit.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze.py`.
- **⚠ COST LESSON (carry): size from OBSERVED prices, not a low pre-flight.** The C4-matched swap RUN is ~$1.3–1.6
  (the s210 swap arm ran 7,200 calls at ~$1.34); a full particle/genitive-style 3-model panel is ~$3.1–3.2 (s229 rep2
  $3.176). If a run would crowd the day's cap, split by model or defer to a full-$5 day (the s228→s229 precedent).
- **⚠ Background-run launch lesson (carry):** launch `python3 probe.py full` **directly** with
  `run_in_background: true` (no trailing `&`, no nohup), rely on the completion notification + output file. **Never a
  name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Foreground `sleep` is blocked.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s231) The C4-matched swap arm is a DESIGN + open decision (ratifiable s232), NOT run.** Do NOT re-write the
  design, re-open the same gates, re-run the s210 swap arm, or re-open the ratified C8 gates (Q1-C both-arms / G8 /
  covariate-and-swap-required, resolved s208/s210). The C4-matched arm is the **sanctioned** successor; ratify → freeze
  → run it. The known-s210-drop exposure is fenced (symmetric verdict + disjoint fresh sample + verifier-reproduced +
  blind-scoring); do NOT smuggle in a promotion-seeking retune.
- **(s230) The A5-battery essay-trigger check on `concordant-verdict-hides-spread` is DONE → FIRED → in-page
  revision.** Do NOT re-run the s227/s230 essay-trigger checks, re-fold the particle instance, or restate the essay's
  discipline as changed. The A5 production-side battery (dative + genitive + particle) is COMPLETE + consolidated on
  the flagship table (v4) + the downstream essay firmed — nothing owed on that line.
- **(s229) The particle line is a PROMOTED direction-only 2/3-firewall `claim`** —
  [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md). Do NOT re-run/retune
  either particle dir, re-promote, re-migrate the v4 row, or restate the claim as a panel / 3-of-3 / magnitude claim.
- **(s222/s221) genitive FULLY CONSOLIDATED. (s216/s214) A6 CC line consolidated. (s210) C8 swap arm CLOSED — the
  C4-frequency-matched swap (s231 design) is the honest successor. (s205) A3b/BLiMP sweep RAN. (s199) VERB decoupling
  FALSIFIED+RETIRED. (s186) A1b antonymy FALSIFIED. (s184) do NOT mass-edit `supported`-at-creation results. (s183) do
  NOT re-audit the whole wiki. (s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ONE open** — [`decisions/open/blimp-c4-matched-swap-arm-design`](wiki/decisions/open/blimp-c4-matched-swap-arm-design.md)
(opened s231, **eligible for ratification s232**). **72 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session designed the clean follow-up the project's last grammar-memorisation check had left owed. That earlier
check swapped the famous test sentences' ordinary words for fresh, equally-common ones, to see whether a model was
leaning on having memorised the exact sentences — but it came out muddy: accuracy did fall on the hardest sentences,
yet the fresh words also turned out rarer in the kind of web text the models were likely trained on, so the fall
could be memorisation or mere rarity. The new design closes that escape hatch by matching the fresh words on that
training-text frequency too, so a fall that still survives can only mean the exact sentences mattered. It is built so
either outcome is equally informative — a surviving fall sharpens the memorisation reading; a fall that vanishes
clears the suspicion and re-opens the path to a firm claim. Two independent reviews cleared it "go, with conditions"
and caught two real gaps (no yardstick for "matched closely enough," and a settings choice that could be nudged after
seeing results), both fixed before anything runs. No experiment ran; a fraction of a cent was spent. The run follows
next session, after an independent sign-off, on a fresh day's budget. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 232.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s229/s230/s231 spent on UTC 2026-07-15 ($3.182446 + $0 + $0.005444 = $3.187890); s232 likely a NEW UTC day
2026-07-16 → full $5, and a NEW JST website day 2026-07-16 → a new journal entry.** **RECONCILE: ONE decision open
(`blimp-c4-matched-swap-arm-design`, opened s231, ELIGIBLE s232).** **The owed arc: RATIFY → FREEZE → RUN the
C4-matched swap arm** (the s217→s218 / s224→s225 pattern; defaults Q1-A/Q2-A/Q3-A; honor the folded conditions
`G-C4-band`/`G-C4-match-adequacy`/`G-power`-attrition/S2/`G-disjoint`/blind-scoring lock). **The run is ~$1.3–1.6 (size
from OBSERVED s210 prices) → if s232 is still the tight 2026-07-15 UTC day, ratify+freeze only and DEFER the run to a
full-$5 day (the s228→s229 precedent).** Do NOT re-run the s210 swap arm, re-open the C8 gates, or smuggle a
promotion-seeking retune. End squash-merged to `main`; `git fetch --prune` at cold-start.
