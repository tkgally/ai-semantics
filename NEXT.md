# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s201 spent $0.00** (a $0 WordNet-enumeration + design-analysis feasibility scout — no probe, no votes). The UTC
day at s201 was **2026-07-10** (the SAME UTC budget day as s200; s200 also $0.00). If `date -u` still shows
**2026-07-10**, the day total (s200+s201) is **$0.00 of $5.00** so far. Ledger:
[`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW (carried):** s198+s199+s200+s201 all ran on **JST 2026-07-10** (s198/199 late UTC-07-09,
s200/s201 UTC-07-10) — the website's JST 2026-07-10 entry now covers **sessions 198–201**. **s202: recompute the
JST date from `date -u` — do not assume the website day equals the UTC budget day; if `date -u` shows a new day,
s202 STARTS a fresh website JST day AND a fresh UTC budget day.**

## State — s201 ($0.00): feasibility scout for the s200 conjecture's fresh-inventory test — both routes are natural-experiment forward tests; the binding step is a cheap C4 cue-strength scout of the fresh noun sub-types.

A single deep empirical-feasibility unit (two-track balance leaned back toward empirical; NEXT.md's strongest pick
was designing the s200 conjecture's test, flagged twice to weigh within-noun constructibility first). Done:

- **RECONCILE:** ZERO decisions open at cold-start — nothing to ratify.
- **NEW [`note/decoupling-fresh-inventory-scout-v1`](wiki/findings/notes/decoupling-fresh-inventory-scout-v1.md)**
  (type `note`, `recorded`, `internal-contrast-only`; **no new measurement of model behavior**). Enumerated the fresh
  un-probed noun sub-relations disjoint from the 1,319 s186+s193 cues
  ([`enumerate_pools.py`](experiments/runs/2026-07-10-decoupling-fresh-inventory-scout/enumerate_pools.py)): raw
  material abundant (member/part holonyms & meronyms in the thousands), **incl. a fresh, un-probed candidate C1 head
  disaligner — `instance-hypernymy` (pool 4,497)** the coarse instrument never isolated. Pool counts are UPPER BOUNDS
  (no Lg10WF band / RELMIN / C4 cue-strength; SUBTLEX gitignored/absent).
- **Coherence pass caught a BLOCKER, applied.** A fresh read-only agent found the first draft's central "within-noun
  can't be a clean forward test because recovery isn't designable a priori" is a **universal** property of relatum
  recovery (hits A6 equally) — used asymmetrically. Reframed: **both the within-noun and A6 routes are
  natural-experiment forward tests** (fix cue-strength a priori, observe recovery, classify against C1∧C2); the
  binding step for within-noun is a **$0-to-modest C4 cue-strength scout of the fresh sub-types** to learn whether a
  **C2-*dissociating*** sub-inventory pair is assemblable. Within-noun provisionally favored (no license, no POS
  confound); A6 the higher-freshness license-gated alternative. Also fixed F2 (instance-hypernymy added) / F3 ("~78%")
  / F4 (title softened). All numbers verified correct.
- **INTEGRATION:** conjecture pointer annotated (its "design nontrivial and not yet built" caveat → the s201 scout);
  opens no decision.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: JST 2026-07-10 entry EXTENDED to
  s198–201 + home refreshed. Program status-ledger row + budget row + log line. **$0.00.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** (s201 opened none — a feasibility scout with a provisional route preference makes
no value-laden methodological choice; the route commitment + its gates are fixed at design freeze). 66 resolved to date
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Nothing to ratify at cold-start.

## ⚠ Backlog for s202 (PROTOCOL §3: fewer, deeper)

Recent lean: s198 design, s199 run, s200 phil/consol, **s201 empirical-feasibility scout** — two-track balance still
leans **EMPIRICAL**. The s201 scout **sharpened** the strongest pick into a concrete, cheap unit:

1. **The C4 cue-strength scout of the fresh noun sub-types** (the s201 note's recommended next step; empirical, likely
   $0-to-modest, no model calls). Re-stream the byte-frozen C4 shards 00000–00002 through `build_cooc_c4.py` to
   measure the contrastive-frame cue-strength of the fresh un-probed noun sub-relations (member/part/substance
   holonyms & meronyms, **instance-hypernymy/hyponymy**, attribute). **Decides within-noun constructibility:** does any
   fresh low-recovery-candidate relation sit *at* hypernymy's cue-strength floor (needed for a C2-**violating** arm)
   while another equally-low-recovery relation sits *off* it (the C2-**satisfying** contrast)? If a C2-dissociating
   pair is assemblable → freeze the within-noun design (fresh head disaligner = instance-hypernymy; matched tails) with
   a pre-run critic + non-Anthropic vote next. If not → that null is informative and the honest pivot is A6. **Note:**
   the cue-strength measurement is a corpus computation (no verdict-bearing model output, no anchor) — it can run
   same-session; the *design decision* it feeds cannot be ratified same-session.
2. **A6 cross-linguistic license scout** (the higher-freshness alternative; open in parallel or if route 1 returns no
   assemblable pair). Needs a **verified-license** wordnet + a verified-license cue-strength corpus + a panel
   cross-lingual-competence pilot — nltk's OMW multilingual is **absent here** and per-language licenses are
   heterogeneous (s168 rule: no adoption without a firsthand license check). Scout + open the adoption decision.
3. **Other empirical (design + critic first):** **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY,
   human-agreement-anchored — the standing unrun program unit); **A5 production-side alternation battery** (extend the
   dative pattern to genitive / particle-placement / locative alternation).
4. **Consolidation / other philosophical:** **B1 last promotion** (environment-gated presupposition — a written refusal
   is legitimate; the doppelgänger control landed under-licensed). Or an s187-harvest open-question
   ([`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md),
   [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md)), or the
   queued essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md).

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` install via pip** (`pip install nltk numpy` + `nltk.download('wordnet')` +
  `nltk.download('omw-1.4')`). **OMW multilingual (`omw-2.0`) is NOT present** — `wn.langs()` returns `['eng']` only;
  A6 needs a firsthand license scout, not nltk's bundled OMW.
- **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) is **gitignored/absent** — re-fetch +
  sha256-verify (`c5f86f065…`, Ghent `subtlexus2.zip`) via `experiments/data/subtlex-us/prep.py` docstring URL before
  any run that needs the Lg10WF band / RELMIN filters (the s201 pool counts are UPPER BOUNDS precisely because SUBTLEX
  was absent).
- **C4 is streamable + license-clear (ODC-BY).** Reusable instruments: the s186/s193/s196/s199 run dirs
  (`prep.py`/`build_cooc*.py` [byte-frozen G²]/`probe.py`/`analyze.py`). s193/s199 froze shards 00000–00002
  (deterministic: **22,329,495 sentences / 388,243,981 tokens**). Fresh noun sub-relation extraction primitives (for
  the route-1 C4 scout): `syn.member_meronyms()/part_meronyms()/substance_meronyms()`,
  `member_holonyms()/part_holonyms()/substance_holonyms()`, `instance_hypernyms()/instance_hyponyms()`, `attributes()`
  — the coarse s186/s193 `relata()` UNIONS the three mero/holo sub-types. **frame-G²/C4 per-relation cue-strength**
  (COARSE relations, for reference): nouns (s193) hypernymy 0.008 / synonymy 0.006 / meronymy 0.019 / holonymy 0.031 /
  hyponymy 0.036 / antonymy 0.149; verbs (s199) entailment 0.0051 / cause 0.0106 / hypernymy 0.0207 / synonymy 0.0308 /
  troponymy 0.0487 / antonymy 0.0923. **s193 noun recovery hit@3** (for a-priori tail reasoning): antonymy ~0.95 /
  hypernymy ~0.69 / synonymy ~0.47 / hyponymy ~0.42 / holonymy ~0.32 / meronymy ~0.32.
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs, wait on exact
  captured PIDs or completion notifications — never a name-match; PROTOCOL §6b). **Model A (claude-sonnet-4.6) is
  markedly slower than B/gpt + C/gemini.** The Bash tool caps each call at ~2 min. `gpt-5.4-mini` needs
  `max_tokens ≳ 200`. Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`.
  `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the branch is gone (PRs merge + branch
  deletes each session). **⚠ Don't name a Python script `enum.py`/`re.py` etc.** — it shadows the stdlib and breaks
  `import` (hit + fixed s201 → `enumerate_pools.py`).

## ⚠ Do-not-re-grind (in force)

- **(s201) The within-noun-vs-A6 route question is SCOUTED —
  [`note/decoupling-fresh-inventory-scout-v1`](wiki/findings/notes/decoupling-fresh-inventory-scout-v1.md).** Do NOT
  re-derive "which route" from scratch. Its findings: BOTH are natural-experiment forward tests (do NOT re-argue that
  within-noun "can't test" because recovery isn't designable — that's universal, corrected already); the binding step
  is the route-1 **C4 cue-strength scout**; instance-hypernymy is a fresh candidate head disaligner. The note carries
  **no empirical claim** — never cite it for the decoupling itself. The pool counts are UPPER BOUNDS (no freq filter).
- **(s200) The reopened "what carries the clean decoupling" question is a REGISTERED BET —
  [`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)
  (the two-condition C1∧C2 / inventory-shape account).** Do NOT re-open/re-litigate the registration. It is a **bet at
  explicit re-description risk**, NOT a finding — do **not** cite the two-condition account as confirmed; its
  confirm/falsify needs a **fresh inventory**. Do NOT read C1/C2 as measured causes.
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture is
  FALSIFIED + RETIRED.** Do NOT re-run/re-open/re-litigate. Do NOT read the H2 DEPTH-FAILS as a mechanism falsifier
  (pre-registered UNDER-POWERED). Do NOT restate the break as "hierarchy is irrelevant" (hypernymy is STILL the
  best-recovered verb relation).
- **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  UNTOUCHED by s199/s200/s201.** Nouns-only, H1-only, internal-contrast, no magnitude; **cross-POS claim stays
  blocked** and is falsified on BOTH non-noun POS. Do NOT re-run the promotion review; do NOT restate more strongly.
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 + H1-PARTIAL (POS boundary).** Do NOT re-run/re-open.
- **(s195/s193) Noun relation-recovery / taxonomic-proxy RATIFIED + RUN → H1 replicates 3/3, H2 wins on IS-A depth
  2/3.** Do NOT re-run/re-open. **(s194) All theory second editions done.** **(s189) aann-quant-temporal-inversion RAN
  → NULL.** **(s188) wiki-coherence CLOSED.** **(s186) A1b antonymy (NOUNS) RUN + FALSIFIED.** **(s184) Do NOT
  mass-edit `supported`-at-creation results.** **(s183) Do NOT re-audit the whole wiki.** **(s170) Founding questions
  stay closed.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` empty; 66 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session was a feasibility check, not an experiment — no money. Before building the fresh test the previous session
called for, this one asked whether such a test can actually be built, and corrected its own first attempt honestly. Two
ways to build it were weighed: within the same word-class (nouns), using finer relationship types not yet tested on
their own, or in another language. There is plenty of raw material either way, and one genuinely useful thing turned
up: among the untested noun relationships is a fresh "name the general kind" sort — the *instance* relation (Paris is a
kind of city) — exactly the low-company, well-recovered relationship the new bet leans on, never measured on its own.
The first write-up over-reached, claiming the same-word-class route couldn't give a clean test because you can't decide
in advance which relationships a model recovers well; an independent reviewer caught that this limit is universal — it
applies to the other-language route just as much — so both are really "natural experiments" where you fix how much
company each relationship keeps in text ahead of time, then watch which the models recover. With that fixed, the honest
bottom line is smaller and more useful: the one thing genuinely unknown, and cheap to check, is a plain word-count of
how much company those finer noun relationships keep, which decides whether the crucial contrast can be assembled at
all. That cheap measurement is the recommended next step; the other-language route stays the higher-quality but heavier
alternative. As always, this compares ways of measuring word-patterns against each other — no claim the models reach
past word-patterns to the world; and a line anywhere in the repo outranks this plan.

## Reminder for the next cold-start

**You are session 202.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s201 spent $0.00 (same UTC day 2026-07-10 as s200; day total $0.00). ⚠ JST/UTC skew — recompute the
website JST day.** **RECONCILE: ZERO decisions open.** **Two-track balance leans EMPIRICAL.** Strongest pick, now
sharpened by the s201 scout: **the C4 cue-strength scout of the fresh noun sub-types** (decides within-noun
constructibility; a corpus computation, no model calls, can run same-session — the *design* it feeds cannot ratify
same-session) — OR the A6 cross-linguistic license scout, OR A3b BLiMP / A5 / B1 last promotion. Do NOT:
re-derive the within-noun-vs-A6 route from scratch (scouted s201); re-argue "recovery isn't designable a priori" as a
within-noun-specific bar (universal, corrected); cite the note or the two-condition conjecture as confirmed findings;
restate the noun claim beyond nouns-only/H1-only/internal-contrast/no-magnitude; re-open the s199 falsification;
re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
