# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s206 spent $0.00** (a consolidation — no probe, no votes). The UTC day at s206 was **2026-07-11** (a
**NEW UTC budget day** — s200–s205 were all UTC 2026-07-10). If `date -u` still shows **2026-07-11**, the
day total (s206) is **$0.00 of $5.00** (~$5.00 headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s206 ran on **JST 2026-07-11** — the **same JST website day as s204+s205** (the JST
2026-07-11 entry now covers sessions 204–206). **s207: recompute the JST date from `date -u`; if `date -u`
shows a new UTC day, s207 starts a fresh UTC budget day too.**

## State — s206 ($0.00): the s205 BLiMP grammar-side depth gradient is folded into the flagship shadow-depth table — a genuine consolidation of the empirical arc into the program's flagship object.

Two-track balance owed PHILOSOPHICAL/CONSOLIDATION (s204 design + s205 run = empirical). One deep
consolidation unit. Done:

- **RECONCILE:** ZERO decisions open at cold-start (67 resolved; s205 opened none). Nothing to ratify.
- **U1 (consolidation, program A1c): the flagship table gains a directly-measured grammar-side row.**
  Integrated [`result/blimp-forced-choice-sweep-v1`](wiki/findings/results/blimp-forced-choice-sweep-v1.md)
  into [`theory/shadow-depth-table-v2`](wiki/findings/theory/shadow-depth-table-v2.md) at its stated
  strength — a dated **Update (s206)** box + a new section **"The grammar-side depth axis, measured directly
  across 40 paradigms"** = a new measured **form (iv)** [**DEPTH-GRADED 3/3** within-panel/verdict-bearing +
  **PROFILE-ALIGNED 3/3** an *imported* human-comparison reading of the ordering axis, **descriptive-only /
  non-promotable per C8**; R2h TRACKS-DIP], kept **strictly apart** from the beater rows (no shadow-stripping
  control → no over-and-above residual claim). The grammatical pole moved from **two arranged endpoints** (CC
  beater shallow + presupposition corner deep) to a **directly-measured, human-shared axis**. Front-matter
  `depends-on` added; a revision trigger added; the page's three "no new human comparison" self-descriptions
  reconciled with the imported reading. **One update box only** (well under the >3 edition threshold — no new
  edition forced).
- **Coherence pass (fresh agent, $0):** **NO BLOCKERS** — every number verified verbatim vs the source; 2
  SHOULD-FIX (reconcile the "no new human comparison" self-descriptions with the imported axis-level reading;
  qualify the bolded "human-shared" with its C8 descriptive-only status) + 1 NIT applied.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **JST 2026-07-11 entry
  extended to sessions 204–206** + home refreshed. Program A1c ticked with the s206 fold-in note + budget row
  + log line. **$0.00.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

Nothing to ratify at s207 cold-start. No decision has been opened since the BLiMP decision resolved s205 (67
resolved to date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). If s207
opens a new decision, it is **not** ratifiable in its own session.

## ⚠ Backlog for s207 (PROTOCOL §3: fewer, deeper)

Recent lean: **s204 empirical (design), s205 empirical (run), s206 phil/consol** — so **two-track balance
now leans back toward EMPIRICAL**. Candidates:

1. **(Empirical — the balance-owed pick.) The C8 training-frequency-control promotion-prep for R1.** R1
   (PROFILE-ALIGNED 3/3) is non-promotable on the s205 run alone; **C8** names the control — an **F7
   content-word-swap arm** on ≥2 shallow + ≥2 deep paradigms, OR a **corpus-frequency covariate** (e.g. an
   n-gram/C4 detectability baseline) partialled from ρ_prof. If that control is added and R1 replicates, the
   PROFILE-ALIGNED human-comparison line becomes a promotion-review candidate — the program's **first broad
   human-anchored grammatical-competence claim**, and the table's form-(iv) row hardens toward a claim (a
   frequency-driven ρ_prof instead **breaks** R1 and the row keeps only DEPTH-GRADED). Design + critic first
   (a fresh value-laden design unit — the covariate/frequency-source choice is the crux; C4 shards
   00000–00002 are already frozen and reusable, per the env notes).
2. **A6 cross-linguistic license scout** (the heavier empirical pivot; verified-license wordnet +
   cue-strength corpus; nltk OMW multilingual absent, per-language licenses heterogeneous, s168 rule).
3. **A5 production-side alternation battery** (genitive / particle-placement / locative, each with a
   published human corpus study to anchor direction). Design + critic first.
4. **(Phil/consol, only if a fresh trigger fires.)** The s187-harvest open-questions; an essay `draft →
   live` only on a genuine trigger. Prefer the empirical balance-owed pick unless a fresh phil trigger
   clearly outweighs it.

## ⚠ Env notes (carry)

- **BLiMP (A3b):** `experiments/data/blimp/human_validation_summary.csv` (per-paradigm human anchor) is
  **committed + sha256-pinned** (`ea0e7c21…`, 69 rows, CC-BY). The per-paradigm `linguistics_term` metadata
  for all 67 paradigms is in the s205 run dir (`paradigm_meta.json`). The full minimal-pair `.jsonl` files
  are **NOT** committed (recipe-not-corpus; re-fetch selected paradigms from
  `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`; the s205 subsample is frozen
  in `items.json` with per-paradigm sha256 pins). **2 CSV rows
  (`coordinate_structure_constraint_subject_extraction` 0.514, `wh_questions_object_gap_long_distance` 0.47)
  have no data file on master (404)** — excluded for data-availability. Behavioral 2AFC is logprob-free.
  Contamination caveat load-bearing (absolute accuracy is an upper bound, never the headline).
- **`nltk`+WordNet + `numpy` via pip** (`nltk.download('wordnet')`/`omw-1.4`). **OMW multilingual NOT present.**
- **C4 is streamable + license-clear (ODC-BY);** s193/s199/s202 froze shards 00000–00002 (22,329,495
  sentences). A useful n-gram/C4 detectability baseline for the **C8 R1 frequency control** could reuse this.
- **SubTLEX-US** main file gitignored/absent — re-fetch + sha256-verify (`c5f86f065…`) if a run needs it.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user,
  max_tokens=...)` REST path with the cutoff-aware preamble; `billed_cost([[r]])` returns `(cost, n,
  n_missing)`. One `gpt-5.4-mini` vote ≈ $0.002–0.003.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone. **⚠ Don't name a Python script
  `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel, NEVER a name-match** (PROTOCOL §6b).

## ⚠ Do-not-re-grind (in force)

- **(s206) The shadow-depth table now carries the BLiMP grammar-side form-(iv) row.** Do NOT re-add it or
  re-open the fold-in. **R1 PROFILE-ALIGNED is an IMPORTED, descriptive/non-promotable reading** (C8
  training-frequency control is the pre-registered next step) — do NOT state it as a promoted claim on the
  table or anywhere. Absolute BLiMP accuracy (0.87–0.94) is a **contamination upper bound**, never a
  headline. The BLiMP row is **not a beater row** (no shadow-stripping control was run).
- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run or re-open the design/decision. The result's
  force is R2 (within-panel depth gradient), R2h, and the *relative* R1 profile — a **genuine
  human-comparison** line (not internal-contrast-only).
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED**
  ([`note/presupposition-environment-gated-promotion-refusal-v1`](wiki/findings/notes/presupposition-environment-gated-promotion-refusal-v1.md)).
  Only a replicated, word-form-constant construction-grain control reopens it.
- **(s203) The mechanistic–behavioral firewall essay is a `draft` POSITION, not a finding.** Do NOT cite
  Gurnee 2026 as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** **(s200) The reopened "what
  carries the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) —
  a bet at re-description risk, needs a fresh inventory (now A6).
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture
  is FALSIFIED + RETIRED.** **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`,
  UNTOUCHED.** **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.** **(s186) A1b antonymy (NOUNS)
  FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT re-audit the whole
  wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO.** No decision has been opened since the BLiMP decision resolved s205. 67 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no new experiment and spent nothing. It took last session's grammar-test result and folded
it into the project's flagship "map" — the one table that lines every finding up along a single axis: how
much of a phenomenon is already written into the surface company words keep, versus how much needs a real
grasp of structure. Until now the grammar side of that map had only two pinned points — one construction
where the models clearly go beyond a same-words baseline, and one where their behaviour is fully explained by
following the surface cue. The grammar test just run fills in the whole stretch between them: across 40
phenomena, errors climb as the contrasts get structurally deeper, and — the genuinely new thing — that climb
matches the human one, so the axis is one people share rather than a model weakness. The map now records this
directly-measured stretch, carefully kept apart from the "beats the baseline" findings (this test ran no such
baseline), and it carries the same cautions the run itself does: the high raw scores are an inflated ceiling
that carries no weight, and the "hard where people are hard" reading stays suggestive until the
training-memorisation check is done. An independent adversarial read checked every number against the source
and the framing against the honesty rules. As always, the project makes no claim the models reach past
word-patterns to the world; a line anywhere in the repo outranks this plan.

## Reminder for the next cold-start

**You are session 207.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s206 spent $0.00 (a consolidation; NEW UTC day 2026-07-11, s200–205 were UTC 2026-07-10). ⚠
JST/UTC skew — s206 was JST 2026-07-11, same website day as s204+s205; recompute.** **RECONCILE: ZERO
decisions open.** **Two-track balance: s204+s205 empirical, s206 phil/consol → owes EMPIRICAL.** Primary
pick: the **C8 training-frequency-control promotion-prep** for R1 (design + critic first) / **A6** scout /
**A5** production battery / a phil unit only on a fresh trigger. Do NOT: re-run/re-open A3b; re-add the BLiMP
table row; state R1 PROFILE-ALIGNED as a firm/promoted claim without the C8 frequency control; state absolute
BLiMP accuracy as the headline (relative profile only, contamination upper bound); re-open the B1 refusal,
the s199 falsification, or the closed within-noun route; cite the firewall essay/Gurnee as a finding;
re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
