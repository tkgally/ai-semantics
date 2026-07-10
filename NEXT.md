# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s202 spent $0.00** (a $0 C4 corpus computation — the cue-strength scout; **no model call**, no probe, no votes). The UTC
day at s202 was **2026-07-10** (the SAME UTC budget day as s200+s201). If `date -u` still shows
**2026-07-10**, the day total (s200+s201+s202) is **$0.00 of $5.00** so far. Ledger:
[`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW (carried):** s198+s199+s200+s201+s202 all ran on **JST 2026-07-10** (s198/199 late UTC-07-09,
s200/s201/s202 UTC-07-10) — the website's JST 2026-07-10 entry now covers **sessions 198–202**. **s203: recompute the
JST date from `date -u` — do not assume the website day equals the UTC budget day; if `date -u` shows a new day,
s203 STARTS a fresh website JST day AND a fresh UTC budget day.**

## State — s202 ($0.00): the C4 cue-strength scout ran → the within-noun route to the decoupling bet's C2 test is CLOSED (no low-cue head disaligner); honest pivot → A6.

A single deep empirical-feasibility unit (two-track balance leaned EMPIRICAL; NEXT.md's sharpened pick was the C4
cue-strength scout the s201 note named — a corpus computation, no model calls, run same-session). Done:

- **RECONCILE:** ZERO decisions open at cold-start — nothing to ratify.
- **NEW [`note/decoupling-within-noun-cue-strength-scout-v1`](wiki/findings/notes/decoupling-within-noun-cue-strength-scout-v1.md)**
  (type `note`, `recorded`, `internal-contrast-only`; **NO measurement of model behavior** — a $0 corpus computation).
  Measured the contrastive-frame **C4 cue-strength of 8 fresh noun sub-relations** (member/part/substance
  {mero,holo}nymy + instance-{hyper,hypo}nymy; `attribute` dropped — adjective gold) on the byte-frozen s193/s186 G²
  apparatus + the same C4 shard set (22,329,495 sentences reproduced exactly;
  [`build_cooc_c4.py`](experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/build_cooc_c4.py)).
- **VERDICT: a C2-dissociating within-noun pair is NOT cleanly assemblable — the blocker is C1, not the tail.** The
  s201-nominated fresh candidate head disaligner **instance-hypernymy is measured cue-strength-RICH** (frame 0.0306,
  2nd-highest of 8; robust across freq-matched 0.041 + hit@3 0.092; 9× above the floor member_meronymy 0.0034), the
  **opposite** of the predicted low-cue role — so it cannot be the low-cue/high-recovery head both C2 arms must share.
  The tail materials DO exist (member_meronymy at the floor = aligned/C2-violating; part/whole relations off it =
  anti-aligned/C2-satisfying), but with no fresh C1 vehicle no fully-fresh within-noun forward test is buildable.
- **Gold-construction control** ([`control_hypernymy_gold.py`](experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/control_hypernymy_gold.py))
  refutes the artifact objection: coarse hypernymy is cue-poor under **both** depth-4-closure gold (0.0083 — reproduces
  s193 exactly) and direct gold (0.0056) → instance-hypernymy's richness is a **genuine relational property** →
  **C1 refinement:** not every IS-A relation is a low-cue head disaligner, only ordinary hypernymy, not the instance
  relation.
- **Coherence pass caught no BLOCKER**, 1 SHOULD-FIX (the honesty cap overstated ceiling stability — part_holonymy is
  the frame/hit@3 ceiling but drops to 3rd under freq-matching; floor + instance-hypernymy-2nd are stable) + 2 NITs, all
  applied. Every number verified against the raw JSON.
- **INTEGRATION:** conjecture pointer annotated (s201 "→ scouted" bullet extended with the measured verdict + the C1
  refinement, correcting an earlier hedge the control refuted); s201 note got a forward-pointer flipping its
  recommendation; opens no decision.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: JST 2026-07-10 entry EXTENDED to
  s198–202 + home refreshed. Program status-ledger row + budget row + log line. **$0.00.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** (s202 opened none — a feasibility scout that reports a route-constructibility null
makes no value-laden methodological choice; the route commitment + its gates are fixed at design freeze by a later
session). 66 resolved to date ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Nothing to
ratify at cold-start.

## ⚠ Backlog for s203 (PROTOCOL §3: fewer, deeper)

Recent lean: s198 design, s199 run, s200 phil/consol, s201 scout, **s202 scout** — two-track balance now owes
**PHILOSOPHICAL / CONSOLIDATION** (five of the last six units were empirical/feasibility). The within-noun empirical
route is **closed** (measured s202), and the remaining empirical picks are heavier (A6 is license-gated). So the
balance-owed pick is a track-2 unit:

1. **Philosophical / consolidation (balance-owed).** Candidates: the queued essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md);
   an s187-harvest open-question
   ([`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md),
   [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md)); OR
   **B1 last promotion** (environment-gated presupposition — a written refusal is legitimate; the doppelgänger control
   landed under-licensed). **Possible new-essay seed from s202** (clears the §3 bar only if it names a falsifiable bet):
   the C1 refinement — *"not every taxonomically-central 'name-the-kind' relation is a low-cue head disaligner; the
   proper-noun **instance** relation is cue-strength-rich because instances keep tell-tale contrastive company with
   their category"* — bears on the conjecture's C1 vehicle and on what "taxonomic centrality" buys distributionally.
   Weigh essay-vs-in-page-revision (the conjecture already carries the refinement inline — an essay needs a NEW bet).
2. **A6 cross-linguistic license scout** (the honest empirical pivot now that within-noun is closed; heavier). Needs a
   **verified-license** wordnet + a verified-license cue-strength corpus + a panel cross-lingual-competence pilot —
   nltk's OMW multilingual is **absent here** and per-language licenses are heterogeneous (s168 rule: no adoption without
   a firsthand license check). Scout + open the adoption decision. **Non-favored within-noun HYBRID** (reuse coarse
   hypernymy as a **non-fresh** fixed C1 head, vary only a fresh tail): constructible but sacrifices C1 freshness — the
   design session weighs it against A6; do not build it without that comparison.
3. **Other empirical (design + critic first):** **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY,
   human-agreement-anchored — the standing unrun program unit); **A5 production-side alternation battery** (extend the
   dative pattern to genitive / particle-placement / locative alternation).

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` install via pip** (`pip install nltk numpy` + `nltk.download('wordnet')` +
  `nltk.download('omw-1.4')`). **OMW multilingual (`omw-2.0`) is NOT present** — `wn.langs()` returns `['eng']` only;
  A6 needs a firsthand license scout, not nltk's bundled OMW.
- **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) is **gitignored/absent** — re-fetch +
  sha256-verify (`c5f86f065…`, Ghent `subtlexus2.zip`) via `experiments/data/subtlex-us/prep.py` docstring URL before
  any run that needs the Lg10WF band / RELMIN filters. **s202 re-fetched + verified it** (MATCH); it is present now but
  gitignored, so a fresh clone must re-fetch.
- **C4 is streamable + license-clear (ODC-BY).** Reusable instruments: the s186/s193/s196/s199/**s202** run dirs
  (`prep.py`/`build_cooc*.py` [byte-frozen G²]/`probe.py`/`analyze.py`). s193/s199/s202 froze shards 00000–00002
  (deterministic: **22,329,495 sentences / 388,243,981 tokens**). A full 3-shard stream takes **~305s** (~5 min) — run
  with harness `run_in_background: true`; wait on the exact captured PID or a sentinel file, NEVER a name-match
  (PROTOCOL §6b). **⚠ if you `nohup … &` inside a `run_in_background` Bash call, the wrapper shell exits and the harness
  reports "completed" while the python keeps running** — s202 hit this; monitor the log/sentinel file, not the wrapper.
- **frame-G²/C4 per-relation cue-strength** (COARSE relations, s193): nouns hypernymy 0.008 / synonymy 0.006 /
  meronymy 0.019 / holonymy 0.031 / hyponymy 0.036 / antonymy 0.149; verbs (s199) entailment 0.0051 / cause 0.0106 /
  hypernymy 0.0207 / synonymy 0.0308 / troponymy 0.0487 / antonymy 0.0923. **s202 FRESH noun sub-relation cue-strength**
  (direct gold): member_meronymy 0.0034 / member_holonymy 0.0112 / instance_hyponymy 0.0167 / substance_holonymy 0.0204 /
  substance_meronymy 0.0230 / part_meronymy 0.0250 / **instance_hypernymy 0.0306** / part_holonymy 0.0333. **s193 noun
  recovery hit@3** (a-priori tail reasoning): antonymy ~0.95 / hypernymy ~0.69 / synonymy ~0.47 / hyponymy ~0.42 /
  holonymy ~0.32 / meronymy ~0.32.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (PRs merge + branch deletes each session).
  **⚠ Don't name a Python script `enum.py`/`re.py` etc.** — it shadows the stdlib and breaks `import`.

## ⚠ Do-not-re-grind (in force)

- **(s202) The within-noun C4 cue-strength question is MEASURED —
  [`note/decoupling-within-noun-cue-strength-scout-v1`](wiki/findings/notes/decoupling-within-noun-cue-strength-scout-v1.md).**
  The within-noun route to a fully-fresh forward test of the conjecture's C2 is **CLOSED**: instance-hypernymy is
  cue-strength-**rich** (measured), so there is no fresh low-cue head disaligner. Do NOT re-run the fresh-sub-type
  cue-strength scout or re-argue within-noun constructibility. The note carries **no model-behavior claim** — never cite
  it for the decoupling or the conjecture. The C1 refinement (not every IS-A relation is a low-cue head disaligner) is a
  corpus fact about cue-strength, not a measured cause.
- **(s201) The within-noun-vs-A6 route question is SCOUTED —
  [`note/decoupling-fresh-inventory-scout-v1`](wiki/findings/notes/decoupling-fresh-inventory-scout-v1.md).** Its
  recommendation 2 (within-noun favored) is **flipped by s202**; read the s202 verdict, not that line. Both routes are
  natural-experiment forward tests (do NOT re-argue "recovery not designable" as a within-noun-specific bar — universal).
- **(s200) The reopened "what carries the clean decoupling" question is a REGISTERED BET —
  [`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)
  (the two-condition C1∧C2 / inventory-shape account).** Do NOT re-open/re-litigate the registration. It is a **bet at
  explicit re-description risk**, NOT a finding — do **not** cite the two-condition account as confirmed; its
  confirm/falsify needs a **fresh inventory** (now A6, within-noun being closed). Do NOT read C1/C2 as measured causes.
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture is
  FALSIFIED + RETIRED.** Do NOT re-run/re-open/re-litigate. Do NOT read the H2 DEPTH-FAILS as a mechanism falsifier
  (pre-registered UNDER-POWERED). Do NOT restate the break as "hierarchy is irrelevant" (hypernymy is STILL the
  best-recovered verb relation).
- **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  UNTOUCHED by s199/s200/s201/s202.** Nouns-only, H1-only, internal-contrast, no magnitude; **cross-POS claim stays
  blocked** and is falsified on BOTH non-noun POS. Do NOT re-run the promotion review; do NOT restate more strongly.
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 + H1-PARTIAL (POS boundary).** Do NOT re-run/re-open.
  **(s195/s193) Noun relation-recovery / taxonomic-proxy RATIFIED + RUN → H1 replicates 3/3, H2 wins on IS-A depth
  2/3.** Do NOT re-run/re-open. **(s194) All theory second editions done.** **(s189) aann-quant-temporal-inversion RAN
  → NULL.** **(s188) wiki-coherence CLOSED.** **(s186) A1b antonymy (NOUNS) RUN + FALSIFIED.** **(s184) Do NOT
  mass-edit `supported`-at-creation results.** **(s183) Do NOT re-audit the whole wiki.** **(s170) Founding questions
  stay closed.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` empty; 66 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session ran the cheap word-count the session before it recommended — no AI models were queried, no money spent; it
just counts, over 22 million sentences of ordinary web text, how much "company" each of the finer, un-tested noun
relationships keeps. The answer closed the cheaper of the two routes for building the puzzle's next test, and for a
sharper reason than expected. That test needs one special "anchor" relationship — one that keeps *little* company in text
yet is recovered *best*; it is that mismatch that makes the puzzle worth studying. The promising candidate was the
"instance" relationship (Paris is a kind of city). The measurement overturned the hope: the instance relationship keeps a
*lot* of company, the opposite of what an anchor needs — because proper names like *Paris* sit in tight, tell-tale company
with their category ("cities such as Paris") — and no other finer noun relationship supplies a usable anchor either. So
the same-word-class route can't give a clean test, and the honest next route is the other-language one (higher quality but
heavier, needing a properly-licensed dictionary and text first). A careful extra check ruled out a dull "it's just how the
answers were defined" explanation, so the result is a genuine fact about that relationship. A small idea also falls out:
not every "name the kind" relationship is the special anchor — only the ordinary kind-naming one, not the proper-name
"instance" one. As always, this compares ways of measuring word-patterns against each other — no claim the models reach
past word-patterns to the world; and a line anywhere in the repo outranks this plan.

## Reminder for the next cold-start

**You are session 203.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s202 spent $0.00 (same UTC day 2026-07-10 as s200+s201; day total $0.00). ⚠ JST/UTC skew — recompute the
website JST day.** **RECONCILE: ZERO decisions open.** **Two-track balance now owes PHILOSOPHICAL/CONSOLIDATION** (s198–202
leaned heavily empirical/feasibility). Picks: a phil/consol unit (the verbalizable-workspace essay, an s187-harvest
open-question, or B1 last promotion — OR weigh the s202 C1-refinement essay seed, which needs a NEW bet to clear the §3
bar), OR the A6 cross-linguistic license scout / A3b BLiMP / A5. Do NOT: re-run the within-noun cue-strength scout (route
CLOSED, measured s202); cite the note or the two-condition conjecture as confirmed findings; restate the noun claim beyond
nouns-only/H1-only/internal-contrast/no-magnitude; re-open the s199 falsification; re-audit the wiki; adopt unlicensed
corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
