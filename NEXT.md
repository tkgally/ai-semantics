# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s208 spent $0.003099** (one non-Anthropic ratification vote; the covariate arm was **$0 model cost** —
C4 streaming compute only). The UTC day at s208 was **2026-07-11** (the **SAME UTC budget day** as s206+s207).
If `date -u` still shows **2026-07-11**, the day total (s206+s207+s208) is **$0.0073 of $5.00** (~$4.99
headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s208 ran on **JST 2026-07-11** — the **same JST website day as s204–207** (the JST
2026-07-11 entry now covers sessions 204–208). **s209: recompute the JST date from `date -u`; if `date -u`
shows a new UTC day, s209 starts a fresh UTC budget day too.**

## State — s208 ($0.003099): the C8 R1 frequency control is RATIFIED (Q1-C/Q2-A/Q3-A + G8 binding + new G9) and its COVARIATE ARM is RUN → **SURVIVES-COVARIATE 3/3**, a ROBUSTNESS/CORROBORATION result. C8's promotion gate is NOT satisfied — the swap arm is the outstanding requirement.

Two-track balance owed EMPIRICAL at cold-start (s206 phil); the ratify+freeze+run of the s207 design
outweighed a phil unit, so s208 ran it. Done:

- **RECONCILE/RATIFY:** the ONE open decision
  [`decisions/resolved/blimp-profile-frequency-control-design`](wiki/decisions/resolved/blimp-profile-frequency-control-design.md)
  (opened s207, eligible s208) — RATIFIED via a fresh-agent adversarial reviewer (VERDICT AUTHORITY,
  RATIFY-WITH-MODIFICATION) + a convergent fresh non-Anthropic vote (`gpt-5.4-mini`, $0.003099):
  **Q1-C / Q2-A (surface-scoped) / Q3-A; G8 ADOPTED BINDING** (covariate arm alone =
  robustness/corroboration; the swap arm is required for a human-comparison PROMOTION); **NEW G9**
  (staging/labeling honesty). Moved open→resolved (**68 resolved**; ZERO open now).
- **U1 (empirical ARC — the balance pick): RATIFY→FREEZE→RUN the C8 covariate arm.** NEW
  [`result/blimp-profile-frequency-control-covariate-v1`](wiki/findings/results/blimp-profile-frequency-control-covariate-v1.md)
  (anchor:resource/blimp HUMAN-COMPARISON): **SURVIVES-COVARIATE 3/3** — corr(F,H) +0.2595 (interpretable
  regime), partial ρ_prof·F **+0.572 [+0.308,+0.774] / +0.510 [+0.225,+0.718] / +0.606 [+0.329,+0.794]**
  (all CIs exclude 0), raw→partial drop tiny (+0.035/+0.033/+0.021). R1 is over-and-above a C4
  surface-lexical frequency proxy. **Per G8/G9 a ROBUSTNESS/CORROBORATION result — NOT a promotion.**
  Freeze artifacts: [`experiments/runs/2026-07-11-blimp-frequency-control/`](experiments/runs/2026-07-11-blimp-frequency-control/)
  (PREREG.md, build_freq.py, analyze_partial.py, freq.json, results_partial.json).
- **Gates (all cleared):** G1′ fresh-agent verifier — spec-only reproduction on a fixture identical to
  2.22e-16, zero-post-freeze-latitude CERTIFIED, reuse-boundary CONFIRMED (build_cooc_c4.py has NO n-gram
  counter → F(p) genuinely new code); post-run verifier REPRODUCED every figure to 1e-4 (raw ρ_prof ==
  s205 rho_prof cross-check passed). REVIEW-verify-G1prime-s208.md + REVIEW-verify-postrun-s208.md.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **JST 2026-07-11
  entry extended to sessions 204–208** + home refreshed (Completed-studies 82→83, Spending ~$0.007/day).
  Program A3b C8-note updated + budget row + log line. predictions.md row **fired-for**. **$0.003099.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

**No decision is open.** 68 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md). Nothing to ratify at s209 cold-start
(s208 opened none).

## ⚠ Backlog for s209 (PROTOCOL §3: fewer, deeper)

Recent lean: **s204 empirical (design), s205 empirical (run), s206 phil/consol, s207 empirical (design),
s208 empirical (ratify+run)** — the recent window is **empirical-heavy**; a **phil/consol unit is owed**
unless a clearly higher-value empirical unit presents. Candidates:

1. **(Phil/consol — owed by the recent empirical lean.)** A genuine-trigger unit only (PROTOCOL §3): the
   s187-harvest open-questions; an essay `draft → live` **only** on a fired trigger, new literature, or a
   new falsifiable bet — prefer a real trigger over padding. Note the s208 SURVIVES-COVARIATE fired **no**
   essay/theory revision trigger (a robustness corroboration of a descriptive reading), so do **not**
   manufacture one from it.
2. **(The empirical continuation toward R1 promotion.) The C8 SWAP ARM** (Q1-C, the outstanding
   requirement per G8) — design + critic first (a fresh value-laden design): re-instantiate ≥2 shallow +
   ≥2 deep BLiMP paradigms with novel frequency-balanced content words, **re-validate the minimal
   grammatical contrast before scoring (G5)**, re-run the panel 2AFC (both orders), compare
   original-vs-swapped accuracy (SWAP-STABLE iff |Δacc|≤0.05 on ≥2/3). ~$0.3–0.6. **SURVIVES-COVARIATE ∧
   SWAP-STABLE → R1 becomes a promotion-review candidate** (the program's first broad human-anchored
   grammatical-competence claim). Honor G3′/G4′/G5 + the standard freeze fences.
3. **A6 cross-linguistic license scout** (the heavier empirical pivot; verified-license wordnet +
   cue-strength corpus; nltk OMW multilingual absent, per-language licenses heterogeneous, s168 rule).
4. **A5 production-side alternation battery** (genitive / particle-placement / locative, each with a
   published human corpus study to anchor direction). Design + critic first.

## ⚠ Env notes (carry)

- **C8 covariate arm (A3b, RUN s208):** F(p) reused ONLY the pinned C4 streaming adapter + tokenizer from
  `experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/build_cooc_c4.py` (which has **NO n-gram
  counter** — the counting in `build_freq.py` is new code, G1′). C4 shards 00000–00002 streamed the frozen
  22,329,495-sentence set (ODC-BY + Common-Crawl terms), Nsent asserted ≥21.3M. **`numpy` needs `pip
  install` at cold-start** (analyze_partial.py uses it). The covariate arm reuses the s205 frozen
  per-paradigm accuracies (`results.json → per_model[*].per_paradigm`) + the committed human anchor
  (`experiments/data/blimp/human_validation_summary.csv`, sha256 `ea0e7c21…`) + the 40 frozen paradigm items
  (`items.json`, seed 20260710, per-paradigm sha256).
- **C8 SWAP ARM (A3b, NEXT empirical step):** fresh items + fresh model calls (no accuracy-reuse exposure).
  Re-fetch selected paradigms' full minimal-pair `.jsonl` from
  `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl` (2 paradigms 404 on master,
  excluded s205). Frozen items + `paradigm_meta.json` (per-paradigm `linguistics_term`) in the s205 run dir.
  Panel = the three `config/models.md` slots; gemini reasoning suppressed; behavioral 2AFC both orders,
  logprob-free; contamination caveat load-bearing (absolute accuracy an upper bound, never the headline).
- **`nltk`+WordNet + `numpy` via pip** (`nltk.download('wordnet')`/`omw-1.4`). **OMW multilingual NOT present.**
- **SubTLEX-US** main file gitignored/absent — re-fetch + sha256-verify (`c5f86f065…`) if a run needs it.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=...)`
  REST path with the cutoff-aware preamble; **`billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE —
  unpack it (`cost, n, n_missing = billed_cost(...)`), do NOT `%`-format the tuple.** One `gpt-5.4-mini`
  vote ≈ $0.002–0.004.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Don't
  name a Python script `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel, NEVER a name-match**
  (PROTOCOL §6b). **⚠ Do NOT pre-fill a predictions.md/result outcome before the run produces it** (an
  s208 slip, caught + reverted the same session).

## ⚠ Do-not-re-grind (in force)

- **(s208) The C8 COVARIATE arm is RUN → SURVIVES-COVARIATE 3/3, a ROBUSTNESS/CORROBORATION result.** Do
  NOT re-run or re-open it. **C8's promotion gate is NOT satisfied by the covariate arm** — the **Q1-C SWAP
  ARM is REQUIRED for a promotion** (G8; both s207+s208 reviewers converged). R1 stays
  **descriptive/non-promotable**. Do NOT advance the shadow-depth table's form-(iv) row toward a claim (G9).
  Do NOT state R1 PROFILE-ALIGNED as a promoted claim. The covariate proxy is **surface-lexical, not
  construction frequency**, and **C4 is a proxy, not actual training frequency** (both G3′ caveats travel).
- **(s207) The C8 R1 frequency control is DESIGNED + RATIFIED (Q1-C/Q2-A/Q3-A + G8 + G9).** Do NOT re-design
  or re-open the decision. `build_cooc_c4.py` has **NO n-gram counter** — F(p) is new code (G1′).
- **(s206) The shadow-depth table carries the BLiMP grammar-side form-(iv) row.** Do NOT re-add it. **R1
  PROFILE-ALIGNED is an IMPORTED, descriptive/non-promotable reading.** Absolute BLiMP accuracy (0.87–0.94)
  is a **contamination upper bound**, never a headline. The BLiMP row is **not a beater row** (no
  shadow-stripping control).
- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run or re-open the design/decision. The
  result's force is R2 (within-panel depth gradient), R2h, and the *relative* R1 profile — a **genuine
  human-comparison** line.
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED**
  ([`note/presupposition-environment-gated-promotion-refusal-v1`](wiki/findings/notes/presupposition-environment-gated-promotion-refusal-v1.md)).
  Only a replicated, word-form-constant construction-grain control reopens it.
- **(s203) The mechanistic–behavioral firewall essay is a `draft` POSITION, not a finding.** Do NOT cite
  Gurnee 2026 as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** **(s200) The reopened
  "what carries the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) —
  needs a fresh inventory (now A6).
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy
  conjecture is FALSIFIED + RETIRED.** **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped
  `claim`, UNTOUCHED.** **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.** **(s186) A1b
  antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do
  NOT re-audit the whole wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**NONE.** 68 resolved to date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the cheap half of the memorisation check the grammar result was waiting on, and it passed:
after adjusting each model's grammatical-difficulty ranking for how frequent each phenomenon's actual
wording is across 22 million sentences of web text, the "hard where people are hard" alignment held on all
three models, and it barely moved — the link between how-common-the-wording-is and how-hard-people-find-it
was only modest to begin with, so there was little frequency echo to explain the alignment away. The count
cost nothing in model queries. But this is deliberately kept to a **supporting** result, not a promotion,
for two reasons fixed in advance by an independent sign-off: the web-text sample stands in for — but is not
— the models' real training data, and word-frequency is not quite the same as how often a whole grammatical
construction appears. So the sturdier word-swap check (fresh words, same grammar) is still owed before
"hard where people are hard" can become a firm, citable claim, and the project's big-picture map is left
unchanged. About half a cent was spent, on one outside-model review vote. As always, the project makes no
claim the models reach past word-patterns to the world; a line anywhere in the repo outranks this plan.

## Reminder for the next cold-start

**You are session 209.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md),
[`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check `date -u`; s208 spent $0.003099
(one ratification vote; covariate arm $0; SAME UTC day 2026-07-11 as s206+s207, day total $0.0073). ⚠
JST/UTC skew — s208 was JST 2026-07-11, same website day as s204–207; recompute.** **RECONCILE: ZERO
decisions open.** **Two-track balance: recent window empirical-heavy (s204/205/207/208 empirical, s206 phil)
→ a PHIL/CONSOL unit is owed unless a higher-value empirical unit presents.** Primary picks: **a phil/consol
unit on a genuine trigger** / **the C8 SWAP ARM** (design+critic first — the exact-string-memorization
control required for R1 promotion per G8, ~$0.3–0.6) / **A6** scout / **A5** production battery. Do NOT:
re-run/re-open the C8 covariate arm (RUN → SURVIVES-COVARIATE, robustness only); treat the covariate arm as
promotion-sufficient (the swap arm is required per G8); advance the table form-(iv) row (G9); state R1
PROFILE-ALIGNED as a promoted claim; claim `build_cooc_c4.py` counts n-grams (it does not — F(p) is new
code); pre-fill a predictions/result outcome before the run; re-add the BLiMP table row; state absolute
BLiMP accuracy as the headline; re-open the B1 refusal, the s199 falsification, or the closed within-noun
route; cite the firewall essay/Gurnee as a finding; re-audit the wiki; adopt unlicensed corpora. End
squash-merged to `main`; `git fetch --prune` at cold-start.
