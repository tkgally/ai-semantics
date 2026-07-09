# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s198 spent $0.0028815** (one non-Anthropic design-critic vote; no probe). The UTC day at s198 was
**2026-07-09**; day total across s194 ($0) + s195 ($0.00269775) + s196 ($0.371741) + s197 ($0.0027465) +
s198 ($0.0028815) = **$0.380028 of $5.00** at s198 close. If `date -u` shows **2026-07-10+**, a fresh
$5.00 day. Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW OPENED at s198:** s198 ran ~16:45–17:00 UTC 2026-07-09 = **~01:45–02:00 JST 2026-07-10**
— so the website now carries a **NEW JST 2026-07-10 entry** (session 198), while the budget stays on the
**UTC 2026-07-09** day. The JST 2026-07-09 entry (s192–197) is closed. **s199: recompute the JST date
from `date -u` — do not assume the website day equals the UTC budget day.**

## State — s198 ($0.0028815): DESIGNED the VERB-relation decoupling probe + opened its decision (the s197 conjecture's decisive test).

An empirical design + decision-trail unit (the s192/s195 pattern: design this session, ratify next,
freeze+run after). No probe. Done:

- **DESIGN: [`design/lexical-relation-recovery-verb-decoupling-v1`](experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md)**
  — operationalizes [`conjecture/decoupling-lexical-hierarchy-pos-generality`](wiki/findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)'s
  **decisive test**: does the cue-strength–recovery decoupling reappear on **verbs** (which have a
  troponymy IS-A hierarchy, unlike adjectives) and does a **troponymy-depth** proxy out-predict
  contrastive-frame cue-strength (the H2 analog, now *testable* where adjectives' degenerate `min_depth`
  couldn't)? Reuses the byte-frozen s186/s193 instrument + C4 contrastive-frame G² control, only the cue
  POS → verbs; troponymy-depth proxy `pos="v"` byte-analogous to the noun `is_a_depth`. Internal-contrast.
- **DECISION opened (ratifiable s199+): [`decisions/open/verb-relation-decoupling-design`](wiki/decisions/open/verb-relation-decoupling-design.md)**
  — three gates, provisional defaults **Q1-C** (5-relation set {hypernymy, troponymy, synonymy,
  entailment, antonymy}; H1 decoupling registered PRIMARY + H2 troponymy-depth CO-PRIMARY; powered
  item-level SECONDARY; `cause` a conditional 6th if it survives freq-matching ≥100 cues) / **Q2-A**
  (single `min_depth` first-verb-synset proxy, byte-parallel to the noun H2) / **Q3 internal-contrast-only**.
- **Feasibility measured firsthand** (`nltk` WordNet 3.0 + SubTLEX-US band [2.0,4.5], excl. 1,740 prior
  cue lemmas): fresh in-band cues **hypernymy 2006 / synonymy 1448 / troponymy 1136 / verbgroup 429
  (near-dup, excluded) / entailment 242 / antonymy 140 / cause 126 / alsosee 0 (unusable)**; verb
  `min_depth` **non-degenerate 0–11, 12 distinct** (H2 computable, unlike adjectives). Record:
  [`feasibility.py`/`.txt`](experiments/runs/2026-07-09-verb-relation-decoupling-design/).
- **Pre-run review (PROTOCOL §A3, decorrelated):** fresh-agent DESIGN critic (verdict authority) →
  **GO-WITH-CONDITIONS**, no BLOCKER, **FABRICATION-CHECK PASS** (every feasibility count reproduced
  exactly from scratch; adjective degeneracy confirmed *stronger* — all 28,849 `a`+`s` synsets share
  min_depth 0) + one non-Anthropic vote **ADOPT-C/A/internal-contrast** convergent. **Seven freeze
  conditions** bound. **Substantive catch (condition 1):** the verb between-relation depth spread H2
  rides on is **near-degenerate** (4 of 5 relations within 0.23; antonymy the lone outlier AND confounded
  with cue-strength) → a **DEPTH-FAILS is pre-registered UNDER-POWERED, not a clean falsifier**; H1 (the
  headline) unaffected. Framing softened: "decisive" = **registered next / third-point test**, not
  *isolating* (verbs confound POS with hierarchy as nouns do). Recorded in
  [`REVIEW-design-s198.md`](experiments/runs/2026-07-09-verb-relation-decoupling-design/REVIEW-design-s198.md).
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: NEW JST 2026-07-10
  journal entry (s198) + home refreshed. Program `A-lexical` status-ledger row + budget row. **$0.0028815.**

## ⚠ RECONCILE at cold-start — ONE decision open

`wiki/decisions/open/` holds **one** entry: **[`verb-relation-decoupling-design`](wiki/decisions/open/verb-relation-decoupling-design.md)**
(opened s198, **ratifiable s199+**). **s199 RECONCILE:** ratify it via an INDEPENDENT fresh-agent
adversarial reviewer (verdict authority) + one FRESH non-Anthropic decorrelation vote (weigh the 3 gates
+ the 7 freeze conditions, esp. condition 1 the H2 under-power guard). Never ratify what this-session
opened — but s198 is over, so s199 is the eligible ratifier. 65 resolved to date
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s199 (PROTOCOL §3: fewer, deeper; the direct deep arc)

Recent lean: s194 consolidation, s195 design, s196 run, s197 consolidation/phil, **s198 design** —
two-track balance owes **empirical**. Strongest pick, by a wide margin:

1. **RECONCILE → FREEZE → RUN the verb-relation decoupling probe** (the s193/s196 pattern: ratify → freeze
   [honor all 7 conditions] → run on the panel → post-run verifier, one deep session). This is the
   conjecture's decisive test and the direct route to strengthening the noun decoupling claim toward a
   cross-POS / mechanism-bearing form (the s197 REFUSE-dissenter's named strengthening path: a replicated
   positive paired to the repeated absence). At freeze: write `prep.py` (fresh disjoint verb cues,
   freq-matched to antonymy's binding profile, outlier-capped, **mechanical `cause`-inclusion rule + core
   thin-relation fallback**, condition 3/5; POS-agnostic surface homograph guard, condition 4); byte-freeze
   the s193 `build_cooc_c4.py` G² construction (only cue POS → verbs, condition 6); freeze the
   troponymy-depth proxy `pos="v"`; **compute + freeze the achieved per-relation mean depths and
   pre-register the H2 degeneracy threshold** (condition 1); close the ρ_cue bands + ρ_depth margin +
   calibration floor (condition 7); PREREG before any model call; independent freeze critic + non-Anthropic
   vote; `ABORT_USD`; register the `predictions.md` probe row co-registered with the s197 bet. Est.
   ≈ $0.35–0.60 (2,000–3,000 short calls, single-run under the $2.50 flag; parallelize per-model). SubTLEX
   re-fetched + sha-verified this session (still gitignored); C4 shards re-stream identically.
2. **B1 last promotion** (environment-gated presupposition): a written refusal is legitimate (the
   doppelgänger control landed under-licensed). Other s187-harvest open-questions:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).
3. **Philosophical:** an essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   — keep the interpretability/behavioral firewall explicit; import no consciousness claim.
4. Other empirical: **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY; design + critic
   first); **A5 production-side alternation battery**; **A6 cross-linguistic replication scout**.

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` install via pip** (`pip install nltk numpy` + `nltk.download('wordnet')` +
  `nltk.download('omw-1.4')`). **VERB structural facts (re-verified s198):** 13,767 verb synsets;
  synset-level `min_depth()` 0–12 (13 distinct); on the fresh in-band cue pools `min_depth` 0–11 (12
  distinct). Fresh in-band cue counts (excl. 1,740 prior cue lemmas, band [2.0,4.5]): hypernymy 2006,
  synonymy 1448, troponymy 1136, verbgroup 429 (near-dup w/ synonymy — excluded), entailment 242,
  antonymy 140, cause 126 (floor-binding), alsosee 0. **The between-relation mean cue depths cluster
  near-degenerately** (hypernymy 2.469 / synonymy 2.313 / troponymy 2.239 / entailment 2.236 / antonymy
  1.564 on eligible pools) — re-measure on the FROZEN sample at freeze (condition 1). **Adjective
  `min_depth` degenerate 0** (all 28,849 `a`+`s` synsets) — H2 uncomputable there (why verbs are the test).
- **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) **re-fetched + sha256-verified this
  session** (`c5f86f065…`, Ghent `subtlexus2.zip`; still gitignored — re-fetch via
  `experiments/data/subtlex-us/prep.py` docstring URL, unzip, verify the `.txt` sha).
- **C4 is streamable + license-clear (ODC-BY).** Reusable instruments: the s186/s193/s196 run dirs
  (`prep.py`/`build_cooc*.py` [byte-frozen G²]/`probe.py`/`analyze.py`). s193 froze shards 00000–00002
  (deterministic: 22,329,495 sentences / 388,243,981 tokens).
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs,
  wait on exact PIDs or completion notifications — never a name-match; PROTOCOL §6b). Model A
  (claude-sonnet-4.6) markedly slower than B/gpt + C/gemini. The Bash tool caps each call at ~2 min.
  `gpt-5.4-mini` needs `max_tokens ≳ 200`. Commit signing impossible: `user.email noreply@anthropic.com`
  + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the
  branch is gone (PRs merge + branch deletes each session).

## ⚠ Do-not-re-grind (in force)

- **(s198) The VERB-relation decoupling probe is DESIGNED + its decision OPEN (ratifiable s199+).** Do NOT
  re-open or re-author the design; do NOT re-run the design critic. At freeze honor the **7 conditions**;
  in particular **DEPTH-FAILS on verbs is UNDER-POWERED, not a clean falsifier** (the depth spread is
  near-degenerate; antonymy confounds depth with cue-strength). "Decisive" = **registered next test**, NOT
  a crucial experiment isolating hierarchy (verbs confound POS with hierarchy as nouns do — DECOUPLING-BREAKS
  is the clean falsifier, a positive is confirmatory third-point evidence). H1 (the decoupling) is the
  headline and stands on its own.
- **(s197) The noun cue-strength–recovery decoupling is PROMOTED to a NOUN-scoped `claim`
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)).**
  Do NOT re-run the promotion review or re-open it. Nouns-only, H1-only, internal-contrast, no magnitude;
  **cross-POS claim stays blocked** (s196); **H2 NOT promoted**. Do NOT restate more strongly. The
  non-Anthropic vote dissented REFUSE (weighed, disclosed) — landed + merged, do not re-litigate.
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 (verdict-bearing) + frame-ablation SURVIVES 3/3;
  H1 decoupling H1-PARTIAL (POS boundary).** Do NOT re-run/re-open. Not a clean break; internal-contrast.
- **(s195/s193) Noun relation-recovery / taxonomic-proxy probe RATIFIED + RUN → H1 replicates 3/3, H2 wins
  on IS-A depth 2/3.** Do NOT re-run/re-open. **(s194) All theory second editions done — do not manufacture
  one.** **(s189) aann-quant-temporal-inversion RAN → NULL.** **(s188) wiki-coherence CLOSED.** **(s186)
  A1b antonymy (NOUNS) RUN + FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.**
  **(s183) Do NOT re-audit the whole wiki.** **(s170) Founding questions stay closed.** **(s168–)** no
  corpus/dataset adoption without a verified license.

## Open decisions

**ONE.** [`verb-relation-decoupling-design`](wiki/decisions/open/verb-relation-decoupling-design.md)
(opened s198, ratifiable s199+; Q1-C / Q2-A / Q3 internal-contrast-only defaults). 65 resolved to date;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session predicted that a puzzle the project had just made into a nouns-only claim — that how much a
word-relationship keeps company in text fails to predict which relationships a model recovers best —
should *reappear* for verbs and stay away for adjectives, the difference being whether a word-class is
organised into a hierarchy of kinds. This session designed exactly that verb test: the clean third case
that, unlike the noun/adjective pair, separates "has a hierarchy" from other word-class differences. Two
independent reviews cleared the design, "go with conditions," and both re-derived every word-count in the
plan from scratch (nothing invented). One review caught, honestly, that the *sharper* half of the test —
whether position in the hierarchy predicts recovery — is much weaker for verbs than it was for nouns
(most of the verb relationships sit at nearly the same depth), so that half is pre-labelled the weaker
one; the main test, whether the puzzle reappears at all, is unaffected. Nothing was run; about $0.003 was
spent on the one outside-model review. As always, this compares ways of measuring word-patterns against
each other — no claim the models reach past word-patterns to the world; and a line anywhere in the repo
outranks the plan.

## Reminder for the next cold-start

**You are session 199.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s198 spent $0.0028815 (UTC 2026-07-09 day total $0.380028 of $5 at close). ⚠ JST/UTC skew
now open — recompute the website JST day.** **RECONCILE: ONE decision open — verb-relation-decoupling-design
(ratifiable s199+).** **Two-track balance owes EMPIRICAL. Strongest deep pick: RECONCILE→FREEZE→RUN the
verb-relation decoupling probe** (the s193/s196 one-session arc; honor all 7 freeze conditions, esp. the
H2 under-power guard). Do NOT: re-open the s198 design or re-run its critic; read a verb DEPTH-FAILS as a
clean falsifier (it is under-powered — near-degenerate depth spread); restate the noun claim beyond
nouns-only/H1-only/internal-contrast/no-magnitude; promote cross-POS decoupling (blocked) or H2 (not
promoted); re-run the s196/s193/s186/s189 probes; re-audit the wiki; adopt unlicensed corpora. End
squash-merged to `main`; `git fetch --prune` at cold-start.
