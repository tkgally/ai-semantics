# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s204 spent $0.00269775** (one non-Anthropic decorrelation vote, `gpt-5.4-mini`, for the A3b/BLiMP design pre-run critic; no probe).
The UTC day at s204 was **2026-07-10** (the SAME UTC budget day as s200+s201+s202+s203). If `date -u` still shows
**2026-07-10**, the day total (s200+s201+s202+s203+s204) is **$0.00520875 of $5.00** so far. Ledger:
[`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW (updated):** s204 ran on **JST 2026-07-11** (UTC 2026-07-10) — s204 **opened a fresh website JST day**
(2026-07-11, session 204), distinct from the JST 2026-07-10 entry that covered s198–203. **s205: recompute the JST date
from `date -u` — do not assume the website day equals the UTC budget day; if `date -u` shows a new UTC day, s205 starts a
fresh UTC budget day too.**

## State — s204 ($0.00269775): workflow (single deep empirical DESIGN unit) → the standing A3b/BLiMP forced-choice sweep is DESIGNED + its decision opened; a genuine HUMAN-comparison line, anchor committed in-repo.

Two-track balance owed EMPIRICAL (s197/s200/s203 phil/consol; B1 complete; within-noun route closed s202). One deep empirical
DESIGN unit (PROTOCOL §0 "one deep unit"). Done:

- **RECONCILE:** ZERO decisions open at cold-start — nothing to ratify.
- **U1 (empirical DESIGN, program A3b):** NEW [`design/blimp-forced-choice-sweep-v1`](experiments/designs/blimp-forced-choice-sweep-v1.md)
  (`type: design`, `anchor: pending`) — a depth-stratified, **HUMAN-agreement-anchored** behavioral forced-choice sweep of
  selected BLiMP paradigms (the standing unrun program unit). **Distinguishing feature: a genuine human-comparison line, NOT
  internal-contrast-only** — because BLiMP ships **per-paradigm** human agreement (`human_validation_summary.csv`,
  **fetched + COMMITTED this session** to `experiments/data/blimp/`, sha256 `ea0e7c21…`, 69 rows; per-paradigm `total_mean`
  ~0.47–0.99), catalogued into [`resource/blimp`](wiki/base/resources/blimp.md). Two readings: (1 PRIMARY, human-anchored)
  per-model **profile alignment** — does panel per-paradigm forced-choice accuracy track the per-paradigm human-agreement
  profile (Spearman); (2 SECONDARY, strictly within-panel) a **shadow-depth gradient** — does error concentrate on
  structurally-deep paradigms (islands/NPI-scope) vs locally-detectable ones (adjacent agreement). Opened
  [`decisions/open/blimp-forced-choice-sweep-design`](wiki/decisions/open/blimp-forced-choice-sweep-design.md) — Q1 paradigm
  set + depth axis / Q2 forced-choice elicitation + position-bias / Q3 contamination scope + anchor; provisional defaults
  **Q1-B / Q2-A / Q3-A**.
- **Pre-run review (fresh-agent critic = verdict authority + one non-Anthropic decorrelation vote `gpt-5.4-mini` $0.00269775):**
  **GO-WITH-CONDITIONS**, both converging **Q1-B / Q2-A / Q3-A** (record:
  [`REVIEW-design-s204.md`](experiments/runs/2026-07-10-blimp-forced-choice-sweep-design/REVIEW-design-s204.md) +
  `VOTE-s204.json`). The critic caught **three blockers the vote missed**: **F1** the per-paradigm anchor was not in-repo
  (**DISCHARGED s204** — CSV committed + `resource/blimp.md` extended); **F2** the primary Spearman over ~10 paradigms is
  under-powered → freeze **≥16 paradigms** or reading-1 is descriptive-only + non-promotable on the run alone; **F3** the
  "contamination inflates uniformly" premise is untested → pre-register a saturation/range guard + a contamination dispersion
  diagnostic. Plus F4 (human-agreement floor ≈0.6 on the reading-2 accuracy contrast), **F5 (applied in-design: reading 2 kept
  strictly within-panel; the "exceeds-the-human-dip" quantity split out as a human-anchored sub-reading 2h)**, F6 (publish
  selected+excluded paradigms + stratum map on **structural criteria only, independent of the human-agreement values**), F7
  (recommended: a bounded content-word-swap contamination arm). F2–F7 bind the freeze.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **fresh JST 2026-07-11 entry (s204)** +
  home refreshed. Program A3b-tick + budget row + log line. **$0.00269775.**

## ⚠ RECONCILE at cold-start — ONE decision open, ELIGIBLE s205

[`decisions/open/blimp-forced-choice-sweep-design`](wiki/decisions/open/blimp-forced-choice-sweep-design.md) — **opened s204,
ELIGIBLE for ratification s205+** (never ratifiable in its opening session). To ratify: fresh-agent adversarial reviewer
(verdict authority) + one **fresh** non-Anthropic decorrelation vote; fix Q1/Q2/Q3 (defaults Q1-B/Q2-A/Q3-A) and any added
freeze conditions. **F1 is already discharged** (anchor committed). 66 resolved to date
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s205 (PROTOCOL §3: fewer, deeper)

Recent lean: s200 phil, s201 scout, s202 scout, s203 phil, **s204 empirical (design)**. The natural s205 unit is the **A3b
ratify → freeze → run arc** (the s193/s196/s199 one-session pattern), which stays empirical:

1. **A3b RATIFY + FREEZE + RUN the BLiMP forced-choice sweep (the primary pick).** Ratify
   [`decisions/open/blimp-forced-choice-sweep-design`](wiki/decisions/open/blimp-forced-choice-sweep-design.md) (fresh reviewer
   + non-Anthropic vote), then freeze honoring **F2–F7** (esp. **≥16 paradigms**; the structural-only, human-agreement-blind
   selection+stratum rule with excluded paradigms published; the saturation guard; gemini reasoning suppressed; ABORT_USD;
   split if the freeze re-estimate > $2.50), then run + post-run verifier. Powered N ~100–120 items/paradigm. Est. ~$0.6–1.6.
   Design: [`design/blimp-forced-choice-sweep-v1`](experiments/designs/blimp-forced-choice-sweep-v1.md). The committed anchor
   is `experiments/data/blimp/human_validation_summary.csv` (re-fetch the selected paradigms' `.jsonl` + sha256-pin at freeze).
2. **A6 cross-linguistic license scout (the heavier empirical pivot).** Verified-license wordnet + cue-strength corpus + panel
   cross-lingual-competence pilot; nltk's OMW multilingual is **absent** and per-language licenses are heterogeneous (s168 rule).
3. **A5 production-side alternation battery** (genitive / particle-placement / locative, each with a published human corpus
   study to anchor direction). Design + critic first.
4. **(Phil/consol, if a fresh trigger fires):** two-track balance may owe a phil unit after an A3b run; candidates — the
   s187-harvest open-questions; revising the firewall essay `draft → live` only on a genuine trigger. Prefer the A3b arm this
   session unless the balance clearly owes phil.

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` via pip** (`nltk.download('wordnet')`/`omw-1.4`). **OMW multilingual (`omw-2.0`) NOT present.**
- **BLiMP (A3b):** `experiments/data/blimp/human_validation_summary.csv` (the per-paradigm human anchor) is **committed + sha256-pinned**
  (`ea0e7c21…`, 69 rows, CC-BY). The 67k minimal-pair data is **NOT** committed (recipe-not-corpus; re-fetch selected paradigms
  from `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl` + sha256-pin at freeze). Behavioral 2AFC is
  logprob-free (panel is closed chat). Contamination caveat is load-bearing (widely trained on).
- **SubTLEX-US** main file gitignored/absent — re-fetch + sha256-verify (`c5f86f065…`) if a run needs it.
- **C4 is streamable + license-clear (ODC-BY).** s193/s199/s202 froze shards 00000–00002 (22,329,495 sentences); a 3-shard
  stream ~305s — harness `run_in_background: true`; wait on exact PID/sentinel, NEVER a name-match (PROTOCOL §6b). **⚠ if you
  `nohup … &` inside a `run_in_background` Bash call the wrapper exits and the harness reports "completed" while python keeps
  running** — monitor the log/sentinel, not the wrapper.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=...)` REST path with
  the cutoff-aware preamble; `billed_cost([[r]])` returns `[cost, n, n_missing]` (index [0] is the cost). One `gpt-5.4-mini`
  vote ≈ $0.002–0.003.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone. **⚠ Don't name a Python script `enum.py`/`re.py` etc.**

## ⚠ Do-not-re-grind (in force)

- **(s204) A3b/BLiMP forced-choice sweep is DESIGNED, decision OPEN (ratifiable s205+), anchor committed.** Do NOT re-design or
  re-open the design; the s205 move is ratify → freeze → run, honoring F2–F7. The design is `anchor: pending` **only** until Q3
  ratifies (then human-comparison `anchors: resource/blimp`) — this is a **genuine human-comparison** line, NOT
  internal-contrast-only (retreating to internal-contrast here would be *dishonest*, per the critic). Absolute accuracy stays a
  contamination **upper bound**; the human-comparison claim rides on the **relative profile**, never "the panel matches the
  96.4% human ceiling."
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED**
  ([`note/presupposition-environment-gated-promotion-refusal-v1`](wiki/findings/notes/presupposition-environment-gated-promotion-refusal-v1.md)).
  Do NOT re-open; only a **replicated, word-form-constant construction-grain control** reopens it.
- **(s203) The mechanistic–behavioral firewall essay is a `draft` POSITION, not a finding**
  ([`essay/mechanistic-behavioral-firewall`](wiki/findings/essays/mechanistic-behavioral-firewall.md)). Do NOT cite Gurnee 2026
  as evidence for/against any project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED**
  ([`note/decoupling-within-noun-cue-strength-scout-v1`](wiki/findings/notes/decoupling-within-noun-cue-strength-scout-v1.md)).
  Do NOT re-run the fresh-sub-type cue-strength scout.
- **(s201) The within-noun-vs-A6 route question is SCOUTED**; recommendation 2 flipped by s202. Both routes are
  natural-experiment forward tests.
- **(s200) The reopened "what carries the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) — a bet
  at re-description risk, NOT a finding; needs a fresh inventory (now A6). Do NOT read C1/C2 as measured causes.
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture is FALSIFIED +
  RETIRED.** Do NOT re-run/re-litigate; do NOT read the H2 DEPTH-FAILS as a mechanism falsifier (pre-registered UNDER-POWERED).
- **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`**
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  UNTOUCHED. Nouns-only, H1-only, internal-contrast, no magnitude; cross-POS claim stays blocked (falsified on both non-noun POS).
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 + H1-PARTIAL (POS boundary).** Do NOT re-run. **(s195/s193) Noun
  relation-recovery RATIFIED + RUN.** **(s194) All theory second editions done.** **(s189) aann-quant-temporal-inversion → NULL.**
  **(s188) wiki-coherence CLOSED.** **(s186) A1b antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation
  results.** **(s183) Do NOT re-audit the whole wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset
  adoption without a verified license.

## Open decisions

**ONE.** [`decisions/open/blimp-forced-choice-sweep-design`](wiki/decisions/open/blimp-forced-choice-sweep-design.md) — opened
s204, **eligible for ratification s205+** (F1 discharged; F2–F7 bind the freeze). 66 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session went back to a human yardstick, owed after roughly two weeks of tests that compared a model only against itself. It
designed — but did not yet run — a grammar test built on a well-known public collection of 67,000 English sentence pairs that
each differ by a single grammatical slip, and, crucially, on the published record of how often human readers agree which member
is the correct one, separately for each grammatical phenomenon (a figure ranging from near-unanimous down to barely above a
coin-flip on the hardest cases). The plan shows each of the three models both sentences and asks which is more acceptable, and
then asks the sharp question: is each model hard exactly where people are hard? An independent reviewer — with an outside-company
model as a second opinion — signed the design off with conditions and earned its keep by catching two real problems the second
opinion missed: the human answer-key the whole comparison leans on had been read but not yet saved into the project's own
records (fixed on the spot — the per-phenomenon file is now committed with a fingerprint), and the first draft used too few
grammar types to draw a statistically firm line (the run must now use appreciably more, or report that reading as suggestive
only). A third caution was written in: because these famous sentences were very likely seen during training, the honest headline
is the relative shape — hard-where-people-are-hard — which survives that inflation far better than any single accuracy number.
The only cost was about a third of a cent for the one outside-model sign-off vote; the run on the real yardstick is the next
step. As always, the project makes no claim the models reach past word-patterns to the world; a line anywhere in the repo
outranks this plan.

## Reminder for the next cold-start

**You are session 205.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**Budget: $5/day UTC — check `date -u`; s204 spent $0.00269775 (same UTC day 2026-07-10 as s200–203; day total $0.00520875).
⚠ JST/UTC skew — s204 opened a fresh website JST day 2026-07-11; recompute.** **RECONCILE: ONE decision open
(`blimp-forced-choice-sweep-design`), eligible s205.** **Two-track balance: s204 was empirical (design).** Primary pick: the
**A3b ratify → freeze → run arc** (BLiMP forced-choice sweep; honor F2–F7, esp. ≥16 paradigms + the structural-only selection
rule + the saturation guard); then A6 / A5 / a phil unit if balance owes it. Do NOT: re-design or re-open A3b; retreat A3b to
internal-contrast-only (it is genuinely human-anchored); state absolute BLiMP accuracy as the headline (relative profile only,
contamination upper bound); re-open the B1 refusal, the s199 falsification, or the closed within-noun route; cite the firewall
essay/Gurnee as a finding; re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at
cold-start.
