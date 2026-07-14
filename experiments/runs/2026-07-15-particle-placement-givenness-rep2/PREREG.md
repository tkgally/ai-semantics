# PREREG — verb-particle placement object-givenness probe, REP2 (fresh-item powered replication; A5; s228)

**Frozen 2026-07-15 (session 228; JST 2026-07-15 / UTC 2026-07-14), after the build + certification and
the pre-run gates, before any finding-bearing model call. THE RUN IS DEFERRED** — see the DEFERRAL note
at the foot. This is a **within-design powered re-run** under the already-ratified decision
[`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
(s225) — **no new decision**, the dative-s175 / genitive-rep2-s220 pattern. Conjecture:
[`conjecture/particle-placement-givenness`](../../../wiki/findings/conjectures/particle-placement-givenness.md).
Human anchor: [`resource/particle-placement-givenness-human-anchor`](../../../wiki/base/resources/particle-placement-givenness-human-anchor.md)
(Kim et al. 2016, CC BY 4.0, a **direction restatement** via Gries 1999) — **direction/sign only**
(definite/given object → split).

## Why this replication (PROTOCOL §3)

v1 ([`result/particle-placement-givenness-v1`](../../../wiki/findings/results/particle-placement-givenness-v1.md),
s225/s226) was **PANEL CONFIRM** — the byte-identical discourse-givenness firewall (GIVEN−NEW-MENTIONED)
cleared CI-LB>0 in **2/3** (claude +0.040 [0.022,0.059], gemini +0.072 [0.049,0.095]), Arm-1 definiteness
directionally consistent 3/3 — but a **SINGLE run**, so it earned no `claim` (PROTOCOL §3 promotes only
REPLICATED ∧ controls-survived). **gpt was the pre-named SHADOW** (firewall +0.018, CI [−0.017,0.055],
18/40 frames). This rep2 re-tests the direction + firewall survival on **disjoint items** and **enlarges
the load-bearing firewall arm (40 → 48 frames)** to power that marginal gpt leg (the genitive-rep2 24→36
nonce-enlargement move). A second independent run + surviving controls is the exact input a cross-session
promotion review needs to write a direction-only particle `claim` and migrate the shadow-depth-table-v4
row **result-cited → claim-cited**.

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`      : `3544656488431d15eb15dada53b46b2b7573ef647a4c9499f81bece2f2d29826`
- `freq_control.json` : `cd472475cfae6f03862cd12ffc9421cd085d8abca831e2cccf1edd7a42da20d7`  (**byte-identical to v1** — the covariate is unchanged; every rep2 verb+particle pair is drawn from v1's frozen 38-pair set)

## Byte-frozen instrument (sha-verified identical to v1)

`probe.py` `eb50f881…`, `analyze.py` `fd77c639…`, `build_cooc_particle.py` `0dba61b2…`,
`freq_control.json` `cd472475…` are **byte-identical** to
`2026-07-14-particle-placement-givenness/` (the prompt, parser, graded forced-choice, resampling unit,
the CONFIRM/SHADOW/WEAK/FALSIFY verdict rule, the covariate recipe + data). `common.py` differs in
**exactly one line** — `HARD_STOP_USD` 3.50 → **3.80** (the item count grew 40→48, so the panel grew
1,680→2,016 calls; documented in-file; a pure budget gate, never touching measurement). **NEW** here:
`build_items.py` (the fresh disjoint items) and its certification check **(D)**.

## Design (one paragraph)

Graded forced-choice (byte-frozen dative/genitive/particle-v1 instrument): hold verb + particle + object
head-noun fixed, distribute 100 points by naturalness between the **JOINED** order (*Kai picked up the
barrel*) and the **SPLIT** order (*Kai picked the barrel up*); split-pref = split_pts/(split_pts+joined_pts).
Resampling unit = the **frame** (a fixed verb+particle+object-head-noun triple). **48 fresh disjoint
frames**, three arms: Arm 1 definiteness (2 conditions), Arm 2 discourse-givenness firewall (3
conditions), Arm 3 length (2 conditions); each × A/B counterbalance. **672 trials × 3 models = 2,016
calls.** Arm 2 (firewall) is the enlarged, load-bearing arm.

## Disjointness + covariate coverage (the rep2 gates — certification.json check (D))

- **(D1)** No rep2 (verb, particle, noun) triple equals any v1 triple; **(D1b)** all 48 rep2 triples
  distinct within rep2; **(D2)** no rep2 object noun appears in v1's noun set — i.e. **all 48 items are
  fresh** (stronger than triple-disjointness). Certified against v1's frozen `stimuli.json` directly.
- **(D3)** Every rep2 verb is in the byte-frozen `analyze.py` `VERB_LEMMA`, and every rep2
  (verb_lemma, particle) pair is a key in the byte-frozen `freq_control.json` — so the covariate and
  analysis cover every frame with **no** re-freeze of either. 38 distinct pairs reused (10 recur with a
  second fresh noun to reach 48 frames — a new noun makes a new frame/triple).

## The three arms + the shadow control (unchanged from v1 — R1–R4)

- **Arm 1 — definiteness (anchor-exact, CONFOUNDABLE, NOT decisive).** *a {noun}* vs *the {noun}*;
  shift1 = split-pref(definite) − split-pref(indefinite); human dir shift1 > 0. Role (R4): a
  consistency check only (a reversal blocks CONFIRM), NOT a hard CI gate.
- **Arm 2 — discourse-givenness FIREWALL (byte-identical scored strings; LOAD-BEARING; carries the
  CONFIRM).** Object string held **byte-identical** (*the {noun}*) across **GIVEN / NEW-MENTIONED / NEW**;
  information status manipulated only in one preceding discourse sentence. Because the two scored
  order-strings are byte-identical across the three conditions, any scored-string reader yields shift = 0
  **by construction** (certified, check (2)). **DECISIVE = GIVEN − NEW-MENTIONED** (Option A), holding
  object-noun lexical priming/recency constant → isolates **referential** information structure; the
  descriptive GIVEN − NEW is also reported. Context template **byte-identical to v1** (given/newment/new),
  parallelism re-certified (14/14/14 words, noun 1/1/0, one comma, declarative, no particle-adjacent leak).
- **Arm 3 — length (convergent-validity leg, SECONDARY, NON-GATING — R5).** *the {noun}* vs *the {noun}
  {heavy postmodifier}*; shift3 = split-pref(short) − split-pref(long); human dir shift3 > 0 (end-weight).
  Feeds the WEAK adjudication only.
- **Frozen surface-collocation covariate (corroboration, near-vacuous — R1/R7).** Per-(verb+particle)
  marginal SPLIT-order rate from UD-EWT (`freq_control.json`, byte-identical to v1). Sparse (16/38 pairs
  any token). `analyze.py` reports the covariate's own predictive validity (b1, R²); CONFIRM rests on Arm 2.

## Pre-registered ASYMMETRIC verdict (R4 — byte-identical to v1; a null is first-class)

Per model: **cond_fw** (firewall shift2 GIVEN−NEW-MENTIONED > 0 AND bootstrap 95% LB > 0 — necessary +
primary); **arm1_consistent** (shift1 > 0); **arm1_reversal** (shift1 < 0 — blocks CONFIRM);
**cond_fw_strong** (shift1 > 0 AND 95% LB > 0); **cond_len** (shift3 > 0 AND 95% LB > 0). Panel (≥2/3):
**CONFIRM** = cond_fw (≥2/3) AND arm1_consistent (≥2/3) AND not arm1_reversal (≥2/3) — "full" if
cond_fw_strong (≥2/3), else "firewall-borne". **SHADOW** = shift1 > 0 (≥2/3) but cond_fw < 2/3.
**WEAK** = cond_fw (≥2/3) but cond_len < 2/3. **FALSIFY** = cond_fw fails AND shift1 not > 0 at ≥2/3
(or Arm-1 reverses ≥2/3). **Replication reading:** rep2 REPLICATES v1 iff PANEL CONFIRM again and the
firewall leg clears CI-LB>0 in ≥2/3; whether the **enlarged** arm pulls the gpt leg over CI-LB>0 is the
targeted secondary question (a gpt SHADOW again is a first-class, honestly-reported outcome — the
enlargement powers, it does not guarantee).

## What this run may / may NOT claim (R1, R6 — unchanged from v1)

- **May:** a within-model, human-direction claim that the panel's particle-placement preference does /
  does not shift toward split for given/definite objects, with magnitudes + intervals, and whether it
  survives the byte-identical firewall; and whether v1's CONFIRM **replicates** on disjoint items.
- **May NOT:** human-level particle-placement competence; "distributional shadow defeated" (the firewall +
  NEW-MENTIONED exclude scored-string shortcuts + lexical recency, not pretraining joint-distribution
  mimicry); any per-item human-gradient claim (no openly-licensed per-item gradient in-repo — deferred to
  a scout); cross-linguistic claims; no "as strong as a rating anchor" rhetoric (Kim et al. = a direction
  restatement, sign only — R6). A single rep2 run does not itself write the `claim`; it enables the
  cross-session promotion review.

## N and power (PROTOCOL §4)

Bootstrap unit = the **frame**; **48 frames** (v1: 40 — a 1.2× enlargement concentrated in the
load-bearing firewall arm, targeting the marginal gpt leg). Arm 2 (firewall) has 6 trials/frame (3
conditions × A/B) ≥ Arm 1 (definiteness) 4 trials/frame — the load-bearing arm ≥ the confoundable arm
(R7 / freeze (iv)). N reported in frames, not trials.

## Budget (pre-flight from the v1 REALITY, not a fresh guess)

2,016 calls, short forced-choice. At the v1 panel's **observed** per-call prices (v1 full panel $2.581 /
1,680 calls: claude ~$0.00248, gemini ~$0.00173, gpt ~$0.00039) the rep2 full panel projects **~$3.1**
(claude ~$1.67 + gemini ~$1.16 + gpt ~$0.26). Pre-registered hard stop **$3.80** (`common.HARD_STOP_USD`)
— above that projection, below the $5/day UTC cap. **⚠ This is the correction to the v1 mistake** (v1's
$0.35–0.65 pre-flight was ~4× too low and halted s225): the estimate here is calibrated to v1's actual
billed cost. The run day must have ≳$3.8 UTC headroom, or split by model (claude arm first).

## Anti-cheat

Item set frozen (sha above), covariate byte-identical to v1, before any finding-bearing call; no retuning
after seeing outputs. A null / SHADOW / WEAK / FALSIFY is a first-class result. The predictions.md bet is
registered at this freeze, before the run (never pre-filled with an outcome). A FALSIFY/reversal triggers
a pre-registered v2, never a re-run of a frozen dir.

## ⚠ DEFERRAL (s228) — FROZEN THIS SESSION, RUN DEFERRED TO A FULL-$5 UTC DAY

The freeze + all pre-run gates (build, certification incl. (D), independent parallelism certification,
fresh-agent pre-run critic, one non-Anthropic decorrelation vote) were done in **session 228**, but the
**finding-bearing run was NOT executed this session**: at freeze time the UTC budget day was **still
2026-07-14** with only **~$2.41** of the $5.00 cap remaining (s224 $0.003934 + s225 $1.394751 + s226
$1.189992 already spent), and the rep2 full panel projects **~$3.1** — over the remaining headroom. Per
CLAUDE.md rule 8 (pre-flight before any probe; the cap is a ceiling) and the s225-halt lesson (do not
start a probe you cannot finish cleanly), the run is deferred to the next session on a **fresh UTC day
(full $5 headroom)**. **No finding-bearing call has been made; `raw/` is empty; nothing has been peeked.**

**Resume protocol (the next full-$5 UTC session).** The instrument is byte-frozen and `probe.py full` is
crash-safe. (1) Confirm `date -u` is a fresh UTC day with ≳$3.8 headroom (else split by model — claude
arm first). (2) `probe.py liveness` (format gate, 3 calls). (3) `probe.py full` (2,016 calls; refuses
unless both shas above are in this file). (4) `python3 analyze.py` (needs `pip install
--break-system-packages numpy`). (5) post-run fresh-agent verifier (independent recompute from `raw/`).
(6) write `result/particle-placement-givenness-rep2` **honoring the 4 pre-run-critic disclosure conditions
below** + the cross-session promotion review that, if CONFIRM replicates, writes the direction-only
particle `claim` and migrates the shadow-depth-table-v4 row. Do **not** re-author items, re-freeze the
shas, or lower the hard stop.

## POST-FREEZE PRE-RUN GATES (s228) — all cleared; RUN AS-IS (no item change)

The freeze passed all pre-run gates this session; **no change to the frozen instrument was required or
permitted**:

- **Build certification** (`certification.json`) — **PASS**, incl. the rep2 disjointness/coverage checks
  (D1) no triple shared with v1, (D1b) all 48 distinct, (D2) all 48 nouns fresh, (D3) every pair covered
  by the byte-frozen covariate + `VERB_LEMMA`.
- **Independent non-authoring parallelism/disjointness certification** ([`REVIEW-certify-s228.md`](REVIEW-certify-s228.md))
  → **CERTIFY-B** (clean; = v1's CERTIFY-A standard; only non-blocking advisory noun notes, byte-identity
  means none can bias the decisive contrast).
- **Non-Anthropic decorrelation vote** (`gpt-5.4-mini`, [`VOTE-critic-s228.json`](VOTE-critic-s228.json))
  → **NO-GO**, on pair-reuse. Weighed as input, **not a veto**.
- **Fresh-agent pre-run critic** (verdict authority, [`REVIEW-critic-s228.md`](REVIEW-critic-s228.md)) →
  **GO-WITH-CONDITIONS**, declining the NO-GO on the merits: the decisive firewall is a **within-frame**
  contrast holding the verb+particle pair AND the entire scored string byte-identical across GIVEN/
  NEW-MENTIONED/NEW, so pair identity is **differenced out by construction** (certification check (2): 7
  scored-string readers each yield within-frame shift2 = 0); the pairs **must** be reused to preserve the
  byte-frozen covariate (the A2a standard genitive-rep2/dative-powered met); the only residual — mild
  anti-conservative frame-bootstrap clustering from the 10 recurring pairs — is small, present already in
  v1's replicated method, and handled by **post-run disclosure**, not by a fix that would gut the
  enlargement.

**The 4 post-run disclosure conditions (carry into `result/particle-placement-givenness-rep2`):**
1. Disclose the pair-reuse structure (48 frames / 38 distinct pairs / 10 pairs twice with a fresh
   noun+context) and its variance implication — the frame bootstrap is mildly anti-conservative under
   intra-pair correlation, more so than v1 (10 vs 2 recurrences) → affects interval **width** only, not
   point estimates; CONFIRM rests on the within-frame firewall where pair identity differences out.
2. Report a supplementary **non-decisive** robustness read from `raw/` (e.g. firewall shift2 restricted to
   the 38 unique-pair frames, or a pair-clustered resample) — a disclosed sensitivity note that does **not**
   replace the pre-registered frame-bootstrap verdict and must not relabel the outcome.
3. State the duplicate-pair selection criterion ("flexible/both-orders-natural," **not** v1-outcome-based)
   and that the firewall differences out pair identity, so pair-selection cannot import v1 firewall magnitude.
4. Keep the byte-frozen covariate caveat (near-vacuous, R²≤0.02, duplicated x for recurring pairs, non-gating).
