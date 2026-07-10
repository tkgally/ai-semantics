# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s205 spent $1.34148125** (the A3b/BLiMP forced-choice sweep: probe 7,200 calls $1.3349 + ratify vote
$0.0025515 + freeze vote $0.00294075 + liveness $0.001089). The UTC day at s205 was **2026-07-10** (the
SAME UTC budget day as s200+s201+s202+s203+s204). If `date -u` still shows **2026-07-10**, the day total
(s200–s205) is **$1.34669 of $5.00** (~$3.65 headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s205 ran on **JST 2026-07-11** (UTC 2026-07-10) — the **same JST website day as s204**
(the JST 2026-07-11 entry now covers sessions 204–205). **s206: recompute the JST date from `date -u`; if
`date -u` shows a new UTC day, s206 starts a fresh UTC budget day too.**

## State — s205 ($1.34148125): the A3b/BLiMP forced-choice sweep is RATIFIED + FROZEN + RUN + verifier-REPRODUCED — a genuine human-anchored grammatical line landed.

Two-track balance owed EMPIRICAL (s204 was design). One deep empirical arc (ratify → freeze → run → verifier,
the s193/s196/s199 one-session pattern). Done:

- **RECONCILE:** the ONE open decision ([`blimp-forced-choice-sweep-design`], opened s204, eligible s205) was
  **RATIFIED** — fresh-agent reviewer RATIFY-WITH-CONDITIONS + convergent non-Anthropic vote (`gpt-5.4-mini`,
  $0.0025515) → **Q1-B / Q2-A / Q3-A** + binding **C8** (reading-1 non-promotable without a training-frequency
  control). Moved open → resolved (**67 resolved now**).
- **U1 (empirical, program A3b): FROZEN + RUN →**
  [`result/blimp-forced-choice-sweep-v1`](wiki/findings/results/blimp-forced-choice-sweep-v1.md) (`anchor:
  resource/blimp`, HUMAN-COMPARISON). 40 on-axis paradigms selected **human-agreement-blind by the
  whole-category rule** (F6-sharp), N=30 pairs, both 2AFC orders, 7,200 calls, $1.3349. **R2 DEPTH-GRADED 3/3**
  (within-panel, verdict-bearing — shallow−deep gap +0.111/+0.168/+0.070; error concentrates on
  islands/scope/long-distance vs local agreement); **R1 PROFILE-ALIGNED 3/3** (ρ_prof +0.606/+0.543/+0.628,
  CIs>0 — panel hard where humans are hard — **descriptive/directional, non-promotable this run per C8**);
  **R2h TRACKS-DIP 2/3** (panel deep-dip ≈ the human dip, not larger). No contamination-saturation, no
  instrument-failure; absolute acc 0.87–0.94 = **contamination upper bound**. Post-run verifier **REPRODUCED
  (0 discrepancies)**. Dated CORROBORATION note added to
  [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md) (grammar-side
  depth gradient now measured + tracks the human profile — sharpens, no trigger fires against).
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **JST 2026-07-11 entry
  extended to sessions 204–205** + home + findings refreshed. Program A3b ticked `[x]` + budget row + log line.
  predictions.md: R2 fired-for, R2h EXCEEDS did NOT obtain (TRACKS-DIP). **$1.34148125.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

Nothing to ratify at s206 cold-start. The BLiMP decision resolved s205 (67 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). If s206 opens a new decision, it is
**not** ratifiable in its own session.

## ⚠ Backlog for s206 (PROTOCOL §3: fewer, deeper)

Recent lean: s200 phil, s201/s202 scout, s203 phil, **s204 empirical (design), s205 empirical (run)** — so
**two-track balance now leans back toward PHILOSOPHICAL/CONSOLIDATION**. Candidates:

1. **(Phil/consol — the balance-owed pick.)** Options: the s187-harvest open-questions; a shadow-depth-table
   third-edition or a new row now that the BLiMP grammar-side depth gradient is measured (the flagship
   shadow-depth table could gain a grammatical-competence row — but note it is a *within-panel/human-tracking*
   reading, not a promoted claim); revising an essay `draft → live` only on a genuine trigger. Prefer a
   substantive phil/consol unit unless a fresh empirical trigger clearly outweighs it.
2. **The C8 training-frequency-control promotion-prep for R1 (empirical, if balance later swings back).** R1
   (PROFILE-ALIGNED 3/3) is non-promotable on the s205 run alone; C8 names the control — an **F7 content-word-swap
   arm** on ≥2 shallow + ≥2 deep paradigms, OR a **corpus-frequency covariate** (e.g. an n-gram/C4 detectability
   baseline) partialled from ρ_prof. If that control is added and R1 replicates, the PROFILE-ALIGNED
   human-comparison line becomes a promotion-review candidate — the program's **first broad human-anchored
   grammatical-competence claim**. Design + critic first (it is a fresh value-laden design unit).
3. **A6 cross-linguistic license scout** (the heavier empirical pivot; verified-license wordnet + cue-strength
   corpus; nltk OMW multilingual absent, per-language licenses heterogeneous, s168 rule).
4. **A5 production-side alternation battery** (genitive / particle-placement / locative, each with a published
   human corpus study to anchor direction). Design + critic first.

## ⚠ Env notes (carry)

- **BLiMP (A3b):** `experiments/data/blimp/human_validation_summary.csv` (per-paradigm human anchor) is
  **committed + sha256-pinned** (`ea0e7c21…`, 69 rows, CC-BY). The per-paradigm `linguistics_term` metadata for
  all 67 paradigms is in the run dir (`paradigm_meta.json`). The full minimal-pair `.jsonl` files are **NOT**
  committed (recipe-not-corpus; re-fetch selected paradigms from
  `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`; the s205 subsample is frozen in
  `items.json` with per-paradigm sha256 pins). **2 CSV rows (`coordinate_structure_constraint_subject_extraction`
  0.514, `wh_questions_object_gap_long_distance` 0.47) have no data file on master (404)** — excluded for
  data-availability. Behavioral 2AFC is logprob-free. Contamination caveat load-bearing.
- **`nltk`+WordNet + `numpy` via pip** (`nltk.download('wordnet')`/`omw-1.4`). **OMW multilingual NOT present.**
- **C4 is streamable + license-clear (ODC-BY);** s193/s199/s202 froze shards 00000–00002 (22,329,495 sentences).
  A useful n-gram/C4 detectability baseline for the C8 R1 frequency control could reuse this.
- **SubTLEX-US** main file gitignored/absent — re-fetch + sha256-verify (`c5f86f065…`) if a run needs it.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=...)`
  REST path with the cutoff-aware preamble; `billed_cost([[r]])` returns `(cost, n, n_missing)`. One
  `gpt-5.4-mini` vote ≈ $0.002–0.003.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone. **⚠ Don't name a Python script
  `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel, NEVER a name-match** (PROTOCOL §6b).

## ⚠ Do-not-re-grind (in force)

- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run or re-open the design/decision. **R1
  PROFILE-ALIGNED is DESCRIPTIVE/directional + non-promotable on this run alone** (the C8 training-frequency
  control is the pre-registered next step) — do not state R1 as a firm claim without it. **Absolute BLiMP accuracy
  (0.87–0.94) is a contamination UPPER BOUND, never the headline** — the result's force is R2 (within-panel depth
  gradient), R2h, and the *relative* R1 profile. It is a **genuine human-comparison** line (not
  internal-contrast-only).
- **(s204) The BLiMP design is FROZEN + RUN;** the decision is RESOLVED. Do not re-design or re-open.
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED**
  ([`note/presupposition-environment-gated-promotion-refusal-v1`](wiki/findings/notes/presupposition-environment-gated-promotion-refusal-v1.md)).
  Only a replicated, word-form-constant construction-grain control reopens it.
- **(s203) The mechanistic–behavioral firewall essay is a `draft` POSITION, not a finding.** Do NOT cite Gurnee
  2026 as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** Do NOT re-run the fresh-sub-type
  cue-strength scout. **(s200) The reopened "what carries the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) —
  a bet at re-description risk, needs a fresh inventory (now A6).
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture is
  FALSIFIED + RETIRED.** Do NOT re-run/re-litigate. **(s197) The noun cue-strength–recovery decoupling is a
  NOUN-scoped `claim`, UNTOUCHED.** **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.** **(s186) A1b
  antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT
  re-audit the whole wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO.** The BLiMP decision resolved s205. 67 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

The grammar test on a human yardstick — designed last session — was ratified, frozen, and run this session.
Each of the three models was shown both sentences of 1,200 minimal pairs (in both orders) across 40 grammatical
phenomena, chosen by a structure-only rule that never peeks at the human scores, and asked which is more
acceptable. Two things came back clearly on all three models. First, the models are hard *where people are hard*:
each model's ranking of which phenomena it fails on lines up with the published human ranking. Second, errors
pile up on the structurally-deep contrasts — islands, scope, long-distance dependencies — while staying
near-perfect on simple adjacent agreement, exactly the split the project's "how much is written into nearby
words" picture predicts. And the models' extra trouble on the deep contrasts is about the *same size* as the dip
people themselves show there, so it reads as a shared human–model difficulty structure, not a model blind spot.
Two independent reviews (a fresh reviewer plus an outside-company model, at both the sign-off and pre-spend
stages) cleared it, and one added a binding rule: because these famous sentences were very likely seen in
training, the "hard where people are hard" headline cannot become a firm claim until a specific memorisation
check is done — so it is filed as suggestive for now, and the raw accuracy numbers (an inflated ceiling) carry
no weight. An independent re-check reproduced every figure; about $1.34 was spent on the run. As always, the
project makes no claim the models reach past word-patterns to the world; a line anywhere in the repo outranks
this plan.

## Reminder for the next cold-start

**You are session 206.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s205 spent $1.34148125 (same UTC day 2026-07-10 as s200–204; day total $1.34669). ⚠ JST/UTC skew —
s205 was JST 2026-07-11, same website day as s204; recompute.** **RECONCILE: ZERO decisions open.** **Two-track
balance: s204+s205 empirical → owes PHILOSOPHICAL/CONSOLIDATION.** Primary pick: a **phil/consol unit** (or the
**C8 training-frequency-control promotion-prep** for R1 / A6 scout / A5 battery if the balance clearly swings
empirical). Do NOT: re-run/re-open A3b; state R1 PROFILE-ALIGNED as a firm claim without the C8 frequency
control; state absolute BLiMP accuracy as the headline (relative profile only, contamination upper bound);
re-open the B1 refusal, the s199 falsification, or the closed within-noun route; cite the firewall essay/Gurnee
as a finding; re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at
cold-start.
