# PREREG — relational-history-perturbation-v2 (frozen before any finding-bearing model call)

**Frozen: 2026-06-12**, after an independent pre-run critic pass whose revisions are logged
below — all applied **before any finding-bearing call**. The **decisive test** named by
`conjecture/commutative-convention` and recommended as the v2 arm by the ratified
`decisions/resolved/relational-pilot-operationalization` (2026-06-12, autonomous adversarial
review): perturb which twin a record's evidence supports across the record's chronology, and
test whether a fresh matcher's interpretation tracks *where* in the order the conflicting
evidence lands. Design page: `experiments/designs/relational-history-perturbation-v2.md`.

## Pre-run critic revisions (logged before any finding-bearing call)

An independent pre-run critic reviewed the frozen draft (stimuli sha256 `5cbebd1d…`) and flagged
two BLOCKERS + five SHOULD-FIXes; all are applied and the stimuli regenerated (new hash below):

1. **B1 — chronology/position confound (the central trap).** In the draft, the
   chronologically-last line was always the physically-last line, adjacent to the question — a
   CI-clean recency effect would be indistinguishable from a bare positional-attention artifact,
   and the draft's decision rule would have wrongly "retired" the conjecture on it. **Fix
   applied (preferred option): a presentation-direction control arm** — every mixed trial runs
   both "fwd" (earliest first) and "rev" (most recent first; lines physically reversed,
   chronology identical). Genuine chronology-tracking follows the *stated* chronology in both
   arms; an attention artifact follows the *physically*-last line in both. The decision rule
   below requires **both arms to agree** before the falsification clause fires, and adds an
   explicit PHYSICAL-POSITION ARTIFACT verdict (methodological, not relational).
2. **B2 — uncertified description content biases toward the null (unfalsifiability risk).**
   15/60 harvested descriptions failed live at least once in v1 (concentrated: gpt pair-2
   sample-0 4/4, sample-1 3/4; gpt pair-0 sample-0 3/4; claude pair-1 sample-0 2/4, one a
   near-duplicate of its twin's descriptions). Ambiguous records inject ~0.5 noise into ρ —
   *toward* the conjecture's own bet. **Fixes applied:** consistent controls now cover **every**
   (pair × sample) cluster (not just sample 0); the analysis **gates each cluster on its own
   controls** (both twins correctly identified) — gated ρ is primary, ungated reported; the
   per-description live-success census is frozen into `stimuli.json`
   (`live_quality_census`) as the stimulus-quality disclosure.
3. **S1** — one matcher figure-array permutation per (model × pair × sample) cluster, constant
   across all 6 orders × 2 directions + that cluster's controls (v1 discipline restored).
4. **S2** — preflight runs gpt's consistent controls only; liveness (3 calls) and preflight raw
   are **never analyzed**; the `full` run is the only finding-bearing dataset.
5. **S3** — transport-error/parse-fail calls retried once; persistent failures recorded NA and
   reported separately; out-of-pair is computed over **parsed** picks only.
6. **S4** — gemini has only 3 clusters: its bootstrap CI is **descriptive only** (pre-registered;
   its verdict line is capped accordingly). `analyze.py` guards the empty-CI crash.
7. **S5** — decision rule harmonized: explicitly **two-sided** (recency *or* primacy both count
   as non-commutative, direction reported).
8. **N3** — framing tightened: the record is a **constructed contradictory description-set**
   asserted about "ONE target" (the mid-trajectory "reassignment" is simulated by composition,
   not a live repair; the nonce never appears inside the history). A contradiction-detecting
   matcher may go out-of-pair — captured by the out-of-pair measure.
9. **N4** — ρ is precisely the **last-*line*-twin** rate (for interleaved orders the final
   "block" is one line).

## Stimuli freeze

`stimuli.json`, generated deterministically by `build_stimuli.py` (SEED=20260612) from the
**committed v1 raw** (each model's own live-game descriptions; v1 figures unchanged, original
sha256 `a2709582…`). **sha256 of `stimuli.json` =
`0e4d315c662f1a9bd92c2392652dbf2a3cba1551bd73ec1aecbca8a2660cd483`.**
No finding-bearing model call before this hash is committed.

- Per model, per near-twin pair (X, Y): MIXED records = 2 distinct descriptions of X + 2 of Y
  (that model's own v1 live-game descriptions), uniform positive feedback ("you FOUND it"),
  presented under **all 6 distinct orders** of the multiset {X,X,Y,Y} — `XXYY, XYXY, YXXY`
  (Y-chron-last) and `YYXX, YXYX, XYYX` (X-chron-last) — **× 2 presentation directions**
  (fwd/rev). The content multiset is **byte-identical across the 12 cells within a
  (pair, sample)**; only chronological position and physical layout vary, independently.
- Coined term = a **frozen nonce nickname** per pair (`ZIMVOR`, `QUEXTAL`, `DRUBNIK`) — carries
  zero descriptive content, so the record is the only signal (v1's `coined_only` lift gate is
  replaced by construction: a nonce cannot self-describe).
- 2 disjoint description samples where the v1 pool allows (claude, gpt), 1 where it is thin
  (gemini: 2 distinct descriptions/figure in v1). Trials/model: claude 84, gpt 84, gemini 42
  (72/72/36 mixed + 12/12/6 consistent controls) = **210 calls**.
- CONSISTENT control records (all four lines describing the same twin, same nonce, fwd
  direction) for **every** (pair × sample) = the per-cluster **manipulation gate**.

## One deliberate prompt change vs v1 (pre-registered, disclosed)

v1's history lines carried `round k:` labels, so its shuffled arm was **in principle
reconstructible** (a matcher could re-sort by label). v2 lines carry **no round numbers**; order
is conveyed purely by position plus the stated direction. This makes the order manipulation
strictly cleaner; it is logged as an honest limitation note for the v1 record (it makes the v1
null *less* surprising, not more).

## Measures (frozen)

- **MANIPULATION GATE (per cluster):** a (pair × sample) cluster enters the primary analysis
  only if **both** of its consistent controls identify the described twin. Per-model control
  accuracy and the gated-cluster list are reported; ungated ρ is reported alongside. (Known
  weakness, acknowledged: 2 trials/cluster is a coarse gate; chance pass ≈ (1/6)² per cluster.)
- **PRIMARY — chronological recency-pick rate ρ_chron, per presentation direction:** among
  gated mixed trials whose parsed pick lands **in the pair**, the fraction picking the
  **chronologically-last-line twin**. Commutative ⇒ ρ_chron ≈ 0.5 in both directions (per-twin
  salience bias is constant across orders and cancels; the critic verified the cancellation
  algebra). CI: clustered bootstrap (10,000 resamples) over (pair × sample) clusters — 6/model
  for claude+gpt; gemini's 3-cluster CI is descriptive only.
- **ARTIFACT DIAGNOSTIC — ρ_phys:** same, for the **physically-last-line** twin (= ρ_chron in
  fwd; = the chron-*first* twin in rev). Separates attention/adjacency bias from
  chronology-tracking.
- **NA and out-of-pair:** parse-fail/transport NA reported separately (after one retry);
  out-of-pair rate over parsed picks; if out-of-pair > 0.5 the model is flagged under-powered.
- **SECONDARY (descriptive, no decision weight):** clean-switch orders (`XXYY`/`YYXX`) vs
  interleaved — a settled-repair reading predicts the recency effect concentrates where the
  change lands as a clean late block. Point estimates only.

## Pre-registered decision rule (no retuning after seeing data)

Per model (gemini capped at descriptive):

- **NON-COMMUTATIVE (chronology-tracking) — the falsification clause** iff: ≥1 cluster passes
  the gate AND out-of-pair ≤ 0.5 AND ρ_chron's CI excludes 0.5 **on the same side in BOTH
  presentation directions** (two-sided: recency *or* primacy; direction reported). → the
  conjecture's behavioral invariance bet is **falsified** for that model; the positive is
  surfaced (not auto-promoted) as a candidate non-commutative effect under the usual
  contingency discipline.
- **PHYSICAL-POSITION ARTIFACT** iff ρ_phys's CI excludes 0.5 on the same side in both
  directions while ρ_chron does not meet its clause. → a **methodological** finding about
  prompt-position bias; says nothing relational; the conjecture is untouched.
- **COMMUTATIVE NULL** iff the gate passes, out-of-pair ≤ 0.5, and all four CIs (ρ_chron and
  ρ_phys, both directions) include 0.5. → extends the v1 null from "order of a static record"
  to "position of conflicting convention evidence"; the conjecture stays `proposed`
  (strengthened, not proven).
- **INCONCLUSIVE / MIXED** iff the arms disagree (one CI-clean, the other not, or opposite
  sides without the artifact pattern). Reported with point estimates, no substantive label.
- **METHODOLOGICAL NULL** iff no cluster passes the gate. **UNDER-POWERED** iff out-of-pair
  > 0.5.
- **Power caveat (pre-registered):** 36 gated-maximum mixed trials per direction over ≤6
  clusters (claude/gpt; gemini 18 over 3) detect only **large, consistent** effects; CI-includes-
  0.5 is *inconclusive-leaning-null*, not a precise zero. **Multiplicity acknowledged:** the
  "≥1 model" framing over 3 models at 95% CIs carries ≈14% family-wise false-positive risk
  under the global null (inherited from v1's framing; the both-arms requirement tightens it).

## Anchor discipline (frozen)

The recency/commutativity measure is the probe's own **internal within-model contrast**
(`anchor: internal-contrast-only` posture per the ratified relational line): **no
human-comparison claim**. Hawkins anchors nothing here (no live game, no entrainment measure).
The human side of the conjecture's predicted contrast (conceptual pacts) stays a characterized
prediction — Brennan & Clark 1996 is still not in-repo.

## Cost pre-flight

210 calls (plus ≤210 retries worst-case), probe-shaped prompts (6 grids + 4 short history
lines ≈ v1 probe calls; v1 billed $0.945/864 calls, claude ≈ $0.002/call). Estimate:
**≈ $0.35; ≤ $0.80 upper bound** — under the $2.50 single-run flag and today's full $5.00
headroom. Actual billed `usage.cost` recorded after each phase; liveness/preflight billed
costs recorded but their raw is never analyzed.

## Scope limits stated up front

- Records are **constructed**, not live: a contradictory description-set composed from real v1
  descriptions and asserted about "ONE target" (all lines marked "FOUND", which is logically
  impossible across twins — the conflict is the manipulation). This isolates the order variable
  exactly (byte-identical multisets) at the cost of ecological fidelity to a live mid-game
  repair; a live perturbation arm is a further design.
- Uniform positive feedback removes outcome information by design; a mixed-feedback arm
  (early-X-failed / late-Y-succeeded — the fuller "repair" texture) is deferred.
- Homogeneous per-model probes; text grids (the ratified v1 yardstick, v1-scoped); n is pilot
  scale. Orderings and effect-direction, not effect sizes.
- 15/60 descriptions failed live at least once in v1 (census frozen in `stimuli.json`); the
  per-cluster gate is the defense, and gated-vs-ungated divergence will be reported.
