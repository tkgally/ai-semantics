# PREREG — relational-reference-game-v1 (frozen before any finding-bearing model call)

**Frozen: 2026-05-31** (probe design revised the same day in response to the independent pre-run
critic — see "Pre-run critic revisions" below — before ANY finding-bearing model call). Builds and
runs the two-AI iterated dyadic reference-game pilot ratified GO in
`decisions/resolved/relational-pilot-go` ("Decision 9"), per the design in
`open-question/relational-meaning-pilot`. Operationalization choices surfaced (not auto-resolved)
in `decisions/open/relational-pilot-operationalization`; the result is `contingent-on` it.

## Pre-run critic revisions (before any finding-bearing call)

An independent pre-run critic flagged one BLOCKER: the original probe showed the matcher the
director's *final full description*, which self-describes the grid, so the history (and its order)
was unnecessary to solve the probe — a forced, uninterpretable null. Fixed before running:
1. The coined term is now an **elicited opaque nickname (≤3 words)**, not a self-describing sentence.
2. A **`coined_only` diagnostic arm** (nickname, no history) gates interpretability: `history_lift =
   ordered − coined_only`. If lift ≈ 0 the history is not load-bearing and the order contrast is a
   *methodological* null (probe could not test order), reported as such — NOT a substantive
   relational null.
3. A **`reversed` (reverse-chronological) control arm** guards against a generic "canonical order
   parses better" position/coherence artifact being mistaken for trajectory-dependence.
4. Power and monologue-floor caveats added (below).

**Stimuli freeze.** `figures.json` (6 abstract referents, canonical ids F0–F5), generated
deterministically by `build_figures.py` (SEED=20260531). **sha256 of `figures.json` content =
`a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4`.** No model call that bears on a
finding was made before this hash was committed.

## What is being tested (the load-bearing contrast)

**Trajectory-dependence.** Does a fresh matcher's interpretation of a coined term depend on the
**ordered** interaction history, holding the **content** of the prior turns byte-identical and
destroying only their **order**? Order-sensitivity that survives content-matching is the operational
signature of a convention constituted *between* agents rather than recomputed from a content bag
(`open-question/relational-meaning-pilot` §"The hard part"). The deflationary null — two next-token
predictors converging from co-occurrence content alone — predicts **ordered ≈ shuffled** and is a
**first-class relational null** to be written, not retuned (charter §5.4).

## Panel & dyad structure (frozen)

- Agents = the standard 3-family panel (`config/models.md`): `claude` (anthropic/claude-sonnet-4.6),
  `gpt` (openai/gpt-5.4-mini), `gemini` (google/gemini-3.5-flash).
- **Homogeneous dyads first**: the same model fills BOTH roles, so a gap cannot be an artifact of two
  different systems talking past each other. Cross-family is a deferred later arm.
- All agent memory is serialized into prompt text (stateless calls) so the shuffle is **exact**:
  the shuffled condition reorders the very same history lines. Temperature 0 throughout.
- Gemini reasoning is REQUIRED on this endpoint (cannot be disabled) → capped to `effort:"minimal"`
  (verified to answer correctly at ~$3e-5/call) to control the ledger's dominant cost driver.

## Stimuli (frozen `figures.json`)

6 referents on an 8×8 `#`/`.` grid, as **3 confusable near-twin pairs** (`pair` field; within-pair
Hamming ≈4, cross-pair ≈16–26). Organic random-accretion blobs → no conventional single-word label
(hard-to-name, the tangram dynamic). A **director word budget (≤12 words)** blocks exhaustive
cell-listing, forcing a holistic coined label; confusable twins make that label ambiguous within a
pair, so *which* figure a coined term settles on can depend on the interaction trajectory.

## Procedure (frozen; `game.py`)

Per model, **N_GAMES=2** independent seeded games. Each game:

1. **LIVE dyad game** — K=6 figures × **R=5** repetitions (each figure once per repetition block).
   Director sees its private D-array + its own per-figure history (prior descriptions + hit/miss) and
   writes a ≤12-word description; Matcher sees its independent P-array + the running per-figure
   history and picks. Real hit/miss feedback accrues → entrainment + repair trajectories. Director
   and matcher have **independent random label orders**, so reference is forced onto figure *content*.
2. **Nickname elicitation** — the director gives each figure its shortest (≤3-word) **opaque coined
   nickname** based on the rounds so far. This nickname (not a self-describing sentence) is the
   coined term the probe tests.
3. **REPLAY probe** — for each figure, a FRESH matcher is given the nickname under four arms, with
   the per-figure convention record (descriptions + hit/miss) held byte-identical and only its order
   varied: **coined_only** (no history), **ordered** (chronological), **reversed**
   (reverse-chronological control), **shuffled** (SHUF_PERMS=3 random permutations — the
   deflationary "averaged-within" control).
4. **SINGLE-AGENT monologue baseline** — same model labels each figure over R passes with **no
   partner / no feedback**; nickname elicitation + the same four-arm probe are re-run on these
   monologue records.

## Measures (frozen)

- **Entrainment / convergence** (scaffolding, expected even under the null): live success rate and
  description word-count by repetition, calibrated against the human curve in
  `resource/hawkins-tangrams` (length 7.73→4.10 words, accuracy 0.78→0.94 over 6 reps). **Anchored**
  to Hawkins — human comparison.
- **INTERPRETABILITY GATE — `history_lift = ordered_acc − coined_only_acc`:** does the history help
  the matcher beyond the opaque nickname alone? If `lift ≈ 0`, the order contrast is untestable
  (methodological null), reported as such.
- **PRIMARY — trajectory-dependence (load-bearing):** `ordered_acc − shuffled_acc` on **dyadic**
  convention records (fresh one-shot matchers; only order differs), **interpretable only where
  `history_lift > 0`**, and required to survive the **chronology guard** `ordered > reversed` (a
  coherent-order effect equally present in reverse order is a position/coherence artifact, not a
  trajectory effect). This is the de-confounded, order-isolating form of the design's named "live vs
  shuffled" contrast. **Internal within-model contrast — NOT anchored by Hawkins** (the pilot's own
  contribution).
- **Named "live vs shuffled" (reported, confounded):** live-online accuracy vs shuffled-replay. Live
  online accuracy confounds order with incremental self-generated exposure, so it is reported for
  completeness, not as the headline.
- **Bar (b) — intra-agent floor:** the same ordered−shuffled gap on **monologue** records. A
  relational reading requires the **dyadic** gap to *exceed* the monologue gap; if the gap is as large
  for solo monologue, it is a bare intra-agent regularity, not relational (`open-question` bar b).

## Pre-registered decision rule (no retuning after seeing data)

- **Relational POSITIVE** iff, for ≥1 model: dyadic `history_lift > 0` (gate) **AND** dyadic
  `ordered_acc − shuffled_acc` CI (clustered bootstrap over coined terms) excludes 0 **AND**
  `ordered > reversed` (chronology-specific, not a coherence artifact) **AND** the order gap exceeds
  that model's monologue order gap. → promote a `conjecture` (bottom rung of the relational second
  ladder), held contingent on `relational-pilot-operationalization`.
- **Relational NULL** iff `history_lift > 0` but ordered ≈ shuffled (order-gap CI includes 0) and/or
  the gap is not chronology-specific / not above the monologue floor. → first-class negative:
  coordination/convergence without constitution; the deflationary story survives order-scrambling.
- **UNDER-POWERED / METHODOLOGICAL** iff `history_lift ≈ 0` (history not load-bearing — opaque
  nickname self-sufficient or history uninformative) OR ceiling/floor on both arms. The order test
  could not be run; reported as such, NOT as a substantive relational null.
- **Power caveat (pre-registered):** with ~12 coined terms/model and a binary ordered arm the pilot
  detects only **large, consistent** order effects; an order gap with a positive point estimate whose
  CI includes 0 is **inconclusive/under-powered**, not a clean null.
- **Monologue-floor caveat:** dyadic records carry hit/miss outcomes that monologue records (no
  feedback) cannot — that *is* the interactive signal, so a dyadic > mono gap reflects the feedback
  loop, the relational mechanism itself, not merely extra record content. Stated, not stripped.

## Scope limits stated up front (honest under-claim)

- Pilot scale: 6 figures, 5 reps, 2 games/model, n≈12 coined terms/condition/model. Orderings and
  effect-direction, not precise effect sizes.
- The **optional history-perturbation arm** (condition 4 of the open question — swap which figure a
  coined term first attached to, test position-sensitivity) is **deferred to v2**. v1 tests the
  ordered-vs-shuffled contrast + the monologue floor only.
- Text-grid referents (not images) — see `decisions/open/relational-pilot-operationalization`. If the
  reference task runs at ceiling in the live game (figures too easy to literally describe within the
  budget), the trajectory test loses sensitivity and the result is flagged under-powered.
- Cross-family dyads deferred. Homogeneous only.
