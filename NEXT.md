# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s207 spent $0.0042** (one non-Anthropic design-critique vote; no probe). The UTC day at s207 was **2026-07-11**
(the **SAME UTC budget day** as s206, which spent $0.00). If `date -u` still shows **2026-07-11**, the day total
(s206+s207) is **$0.0042 of $5.00** (~$5.00 headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s207 ran on **JST 2026-07-11** — the **same JST website day as s204–206** (the JST 2026-07-11
entry now covers sessions 204–207). **s208: recompute the JST date from `date -u`; if `date -u` shows a new UTC day,
s208 starts a fresh UTC budget day too.**

## State — s207 ($0.0042): the C8 training-frequency-control promotion-prep for R1 is DESIGNED — an $0-covariate-plus-word-swap control, decision opened, critic + vote both GO-WITH-CONDITIONS converging on "the swap arm is required for a promotion."

Two-track balance owed EMPIRICAL (s206 phil/consol). One deep empirical DESIGN unit (design + critic; ratify+run
is a LATER session). Done:

- **RECONCILE:** ZERO decisions open at cold-start (67 resolved; s206 opened none). Nothing to ratify.
- **U1 (empirical DESIGN, the balance-owed pick — program A3b C8 promotion-prep): the R1 training-frequency
  confound control.** NEW [`design/blimp-profile-frequency-control-v1`](experiments/designs/blimp-profile-frequency-control-v1.md)
  (anchor:resource/blimp HUMAN-COMPARISON) + NEW open decision
  [`decisions/open/blimp-profile-frequency-control-design`](wiki/decisions/open/blimp-profile-frequency-control-design.md)
  (**Q1** control strategy [A covariate / B swap arm / C both] — THE CRUX; **Q2** frequency proxy F(p) [A surface-string
  / B detectability-margin=over-control hazard / C construction-level] — the covariate's crux; **Q3** promotion rule +
  proxy scope; provisional defaults **Q1-A/Q2-A/Q3-A**). The control tests whether R1 PROFILE-ALIGNED (ρ_prof
  +0.606/+0.543/+0.628, n=40) survives a training-frequency confound; **SURVIVES → R1 a promotion-review candidate
  (the program's first broad human-anchored grammatical claim); BREAKS → the table's form-(iv) row keeps only
  DEPTH-GRADED.** The covariate arm reuses the frozen s205 accuracies + committed human anchor → **$0 model cost**.
- **Pre-run review (PROTOCOL §A3):** fresh-agent critic (VERDICT AUTHORITY, ~118k tok) → **GO-WITH-CONDITIONS**,
  provenance + anchor CLEAN; one non-Anthropic vote (`gpt-5.4-mini`, $0.0042) → **GO-WITH-CONDITIONS**. **Both
  converge on Q1-C — the content-word-swap arm is required for a PROMOTION; the covariate alone earns only a
  robustness result.** The critic keeps **Q2-A primary** (least depth-entangled), diverging from the vote's Q2-C
  (construction freq ≈ collinear with depth → over-control). **THREE critic blockers, all discharged in-design s207:**
  B1 the design misdescribed `build_cooc_c4.py` as byte-reusing an "n-gram counting recipe" — it has **NO n-gram
  counter** (only unigram df + cue co-occurrence + a G² kernel), so F(p) is **new code with genuine DoF** → G1′
  (fresh-agent reproduction of `build_freq.py` before F(p) touches the real mapping); B2 under Q2-A the covariate
  controls surface-lexical familiarity **not** construction frequency (C8's literal confound) → G3′ scope caveat;
  B3 verdict map missing the high-collinearity branch → G6 INCONCLUSIVE (over-control-suspect). Freeze conditions
  **G1′–G8** bind the freeze (G8 = Q1-C swap arm required for a promotion). REVIEW-design-s207.md + VOTE-s207.json.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **JST 2026-07-11 entry
  extended to sessions 204–207** + home refreshed. Program A3b appended with the s207 design note + budget row +
  log line. **$0.0042.**

## ⚠ RECONCILE at cold-start — ONE decision open, eligible s208

**[`decisions/open/blimp-profile-frequency-control-design`](wiki/decisions/open/blimp-profile-frequency-control-design.md)**
(opened s207, **eligible s208+**). Ratify via a fresh-agent adversarial reviewer (verdict authority) + one **fresh**
non-Anthropic decorrelation vote (`panel.B`/`.C`, cutoff-aware). Fix **Q1/Q2/Q3** (adopt Q1-A/Q2-A/Q3-A or a named
alternative) and decide whether to **adopt G8 (Q1-C swap arm required for a promotion) as binding** — both s207
reviewers converged on it. Honor G1′–G8 (recorded on the design). **Never ratify what this session opened** — s207
opened it, so only s208+ may. No OTHER decision is open (68th if this resolves; 67 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s208 (PROTOCOL §3: fewer, deeper)

Recent lean: **s204 empirical (design), s205 empirical (run), s206 phil/consol, s207 empirical (design)** — so the
recent window is empirical-heavy; a phil/consol unit is owed unless the ratify+run of the s207 design clearly
outweighs it. Candidates:

1. **(The balance-owed continuation.) RATIFY + FREEZE + RUN the C8 frequency control** (the s193/s196/s205
   ratify→freeze→run arc in one session). Ratify the s207 decision (fresh reviewer + one non-Anthropic vote), then
   freeze + run. **The covariate arm is $0 model cost** (reuses the frozen s205 accuracies); **per G8 the
   content-word-swap arm is required for a promotion** (fresh items + fresh calls, est. ~$0.3–0.6). Honor G1′
   (fresh-agent reproduction of `build_freq.py` before F(p) touches the real mapping — `build_cooc_c4.py` has NO
   n-gram counter, F(p) is new code), G2 (Q2-B sensitivity-only), G3′ (surface-vs-construction scope), G6
   (collinearity guard), G7 (proxy-validity audit + no post-hoc tuning). If R1 survives + the swap arm holds → R1
   becomes a promotion-review candidate; if it breaks → the table's form-(iv) row keeps only DEPTH-GRADED.
2. **(Phil/consol — owed by the recent empirical lean if #1 is deferred.)** The s187-harvest open-questions; an essay
   `draft → live` only on a genuine trigger. Prefer a real trigger over padding.
3. **A6 cross-linguistic license scout** (the heavier empirical pivot; verified-license wordnet + cue-strength
   corpus; nltk OMW multilingual absent, per-language licenses heterogeneous, s168 rule).
4. **A5 production-side alternation battery** (genitive / particle-placement / locative, each with a published human
   corpus study to anchor direction). Design + critic first.

## ⚠ Env notes (carry)

- **C8 frequency control (A3b, DESIGNED s207):** the covariate arm reuses the frozen s205 accuracies
  (`experiments/runs/2026-07-10-blimp-forced-choice-sweep/results.json → per_model[*].per_paradigm`,
  verifier-reproduced), the 40 frozen paradigm items (`items.json`, seed 20260710, 30 pairs/paradigm, per-paradigm
  sha256), and the committed human anchor (`experiments/data/blimp/human_validation_summary.csv`, sha256
  `ea0e7c21…`). **`build_cooc_c4.py` has NO n-gram frequency counter** — only unigram `df` + cue co-occurrence + a
  signed-G² kernel (the import assertion pins the G² kernel, NOT reusable for F(p)); only the C4 streaming adapter +
  tokenization are reusable, so `build_freq.py` / F(p) is **new code** (G1′: independently reproduce it before F(p)
  touches the real paradigm→H mapping). C4 shards 00000–00002 stream from HuggingFace (ODC-BY + Common-Crawl terms;
  the s193-frozen 22,329,495-sentence set; first fetched `experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/build_cooc_c4.py`).
- **BLiMP (A3b):** the per-paradigm `linguistics_term` metadata for all 67 paradigms is in the s205 run dir
  (`paradigm_meta.json`). Full minimal-pair `.jsonl` files NOT committed (recipe-not-corpus; re-fetch selected
  paradigms from `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`; the s205 subsample is
  frozen in `items.json` with per-paradigm sha256 pins). 2 CSV rows
  (`coordinate_structure_constraint_subject_extraction` 0.514, `wh_questions_object_gap_long_distance` 0.47) have no
  data file on master (404) — excluded for data-availability. Behavioral 2AFC is logprob-free. Contamination caveat
  load-bearing (absolute accuracy is an upper bound, never the headline).
- **`nltk`+WordNet + `numpy` via pip** (`nltk.download('wordnet')`/`omw-1.4`). **OMW multilingual NOT present.**
- **SubTLEX-US** main file gitignored/absent — re-fetch + sha256-verify (`c5f86f065…`) if a run needs it.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=...)`
  REST path with the cutoff-aware preamble; **`billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE — unpack it
  (`cost, n, n_missing = billed_cost(...)`), do NOT `%`-format the tuple.** One `gpt-5.4-mini` vote ≈ $0.002–0.004.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (it was deleted post-s206 merge). **⚠ Don't
  name a Python script `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel, NEVER a name-match** (PROTOCOL §6b).

## ⚠ Do-not-re-grind (in force)

- **(s207) The C8 R1 frequency control is DESIGNED, decision OPEN.** Do NOT re-design or re-open it. **`build_cooc_c4.py`
  has NO n-gram counter — F(p) is new code (G1′).** The **covariate arm alone earns only a robustness result — the
  content-word-swap arm is REQUIRED for a promotion** (G8; both s207 reviewers converged). R1 stays
  **descriptive/non-promotable** until the control runs AND survives. Do NOT state R1 PROFILE-ALIGNED as a promoted
  claim before then.
- **(s206) The shadow-depth table carries the BLiMP grammar-side form-(iv) row.** Do NOT re-add it. **R1
  PROFILE-ALIGNED is an IMPORTED, descriptive/non-promotable reading.** Absolute BLiMP accuracy (0.87–0.94) is a
  **contamination upper bound**, never a headline. The BLiMP row is **not a beater row** (no shadow-stripping control).
- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run or re-open the design/decision. The result's force
  is R2 (within-panel depth gradient), R2h, and the *relative* R1 profile — a **genuine human-comparison** line.
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED**
  ([`note/presupposition-environment-gated-promotion-refusal-v1`](wiki/findings/notes/presupposition-environment-gated-promotion-refusal-v1.md)).
  Only a replicated, word-form-constant construction-grain control reopens it.
- **(s203) The mechanistic–behavioral firewall essay is a `draft` POSITION, not a finding.** Do NOT cite Gurnee 2026
  as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** **(s200) The reopened "what carries
  the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) —
  needs a fresh inventory (now A6).
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture is
  FALSIFIED + RETIRED.** **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`, UNTOUCHED.**
  **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.** **(s186) A1b antonymy (NOUNS) FALSIFIED.**
  **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT re-audit the whole wiki.** **(s168–)** no
  corpus/dataset adoption without a verified license.

## Open decisions

**ONE.** [`decisions/open/blimp-profile-frequency-control-design`](wiki/decisions/open/blimp-profile-frequency-control-design.md)
(opened s207, eligible s208+; Q1/Q2/Q3 + the G8 promotion-gate recommendation). 67 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no new experiment; it designed the memorisation check the grammar result has been waiting on, and
spent about half a cent on one outside-model review vote. The grammar test found that the models are hard where
people are hard, but that headline was deliberately held back from being a firm claim because of one worry: the
grammar phenomena people find easy may also be the ones the models saw most in training, so "hard where people are
hard" could be a memorisation echo rather than a shared grasp of grammatical difficulty. This session laid out the
check that separates those two stories — a cheap version that adjusts the pattern for how frequent each phenomenon's
wording is in a large public web-text sample (costing nothing in model queries, because it reuses answers already
gathered), and a sturdier version that swaps the actual words for fresh ones and re-asks. Two independent reviewers
signed off "go, with conditions," and both reached the same judgement: the cheap version alone is not enough to
promote the result — the sturdier word-swap version is needed too, partly because the cheap version reuses answers
already known (so the person choosing the adjustment already knows which choice flatters the result), and partly
because word-frequency is not quite the same thing as how often a whole grammatical construction appears. The fresh
reviewer also caught a real mistake — the design claimed it could reuse an old text-counting tool that, on
inspection, does not count what was needed — which was corrected on the spot, along with the other fixes the
reviewers asked for. Nothing was run against the models; the check itself comes after an independent sign-off next
session. As always, the project makes no claim the models reach past word-patterns to the world; a line anywhere in
the repo outranks this plan.

## Reminder for the next cold-start

**You are session 208.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md),
[`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check `date -u`; s207 spent $0.0042 (one design
vote; SAME UTC day 2026-07-11 as s206 $0.00). ⚠ JST/UTC skew — s207 was JST 2026-07-11, same website day as s204–206;
recompute.** **RECONCILE: ONE decision open [blimp-profile-frequency-control-design], eligible s208 — ratify it (fresh
reviewer + one non-Anthropic vote), fixing Q1/Q2/Q3 and whether G8 [swap arm required for promotion] binds.**
**Two-track balance: recent window empirical-heavy [s204/205/207 empirical, s206 phil] → a phil/consol unit is owed
unless the ratify+freeze+run of the s207 design outweighs it.** Primary pick: **RATIFY + FREEZE + RUN the C8
frequency control** (covariate arm $0; swap arm needed for promotion) / a phil unit / **A6** scout / **A5** production
battery. Do NOT: re-design/re-open the C8 control; treat the covariate alone as promotion-sufficient (swap arm
required); claim `build_cooc_c4.py` counts n-grams (it does not — F(p) is new code); state R1 PROFILE-ALIGNED as a
promoted claim before the control runs + survives; re-add the BLiMP table row; state absolute BLiMP accuracy as the
headline; re-open the B1 refusal, the s199 falsification, or the closed within-noun route; cite the firewall
essay/Gurnee as a finding; re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch
--prune` at cold-start.
