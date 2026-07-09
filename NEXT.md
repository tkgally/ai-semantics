# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s199 spent $0.517294** (the verb probe $0.5115 + ratify vote $0.00276075 + freeze vote $0.003033). The
UTC day at s199 was **2026-07-09**; day total across s194 ($0) + s195 ($0.00269775) + s196 ($0.371741) +
s197 ($0.0027465) + s198 ($0.0028815) + s199 ($0.517294) = **$0.897322 of $5.00** at s199 close. If
`date -u` shows **2026-07-10+**, a fresh $5.00 day. Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW (carried):** s199 ran ~20:45–21:30 UTC 2026-07-09 = **~05:45–06:30 JST 2026-07-10** — the
**same JST day as s198**, so the website's JST 2026-07-10 entry now covers **sessions 198–199**, while the
budget stays on **UTC 2026-07-09**. **s200: recompute the JST date from `date -u` — do not assume the
website day equals the UTC budget day.**

## State — s199 ($0.517294): RATIFIED → FROZE → RAN the verb-relation decoupling probe → DECOUPLING-BREAKS (2/3); the s197 POS-hierarchy conjecture FALSIFIED + retired.

A complete deep empirical arc (the s193/s196 pattern: ratify → freeze → run → verifier, one session). Done:

- **RECONCILE:** ratified [`decisions/resolved/verb-relation-decoupling-design`](wiki/decisions/resolved/verb-relation-decoupling-design.md)
  (Q1-C / Q2-A / Q3 internal-contrast-only) via an independent fresh-agent adversarial reviewer
  (RATIFY-WITH-BINDING-CONDITIONS, fabrication spot-check PASS) + one fresh non-Anthropic vote — **three
  new binding conditions B1–B3** (numeric depth-degeneracy bound; symmetric under-power; third-point
  framing). 66 resolved.
- **FREEZE:** 776 fresh verb cues / 6 relations (`cause` included by the mechanical rule, N=126), the
  byte-frozen s193 C4 G² control (22,329,495 sentences reproduced), troponymy-depth proxy `pos="v"`.
  **B1 frozen verdict: non-antonymy CORE-4 depth range 0.277 < 0.50 → DEGENERATE → H2 under-powered
  symmetrically** (the conservative, ratifier-faithful call). Freeze critic **GO** (the non-Anthropic
  freeze vote's NO-GO overruled on the merits — the CORE-4 bound is the ratifier's stated definition and
  moves H2 *weaker*).
- **RUN → [`result/lexical-relation-recovery-verb-decoupling-v1`](wiki/findings/results/lexical-relation-recovery-verb-decoupling-v1.md)
  (status proposed, internal-contrast-only): H-verb-1 DECOUPLING-BREAKS (2/3)** — ρ_cue +0.49/+0.60/+0.54
  (adjective band; HIT@3 co-primary +0.71/+0.77/+0.54). Despite the verified verb troponymy hierarchy,
  cue-strength **re-tracks** recovery → fires the conjecture's falsifier. **H-verb-2 DEPTH-FAILS but
  pre-registered UNDER-POWERED** (B1). Leave-one-out (verifier): entailment+cause carry the break;
  hypernymy is still the noun-like disaligner (low cue-strength, best recovery 3/3) but outvoted.
  Independent post-run verifier **REPRODUCED** (max ρ discrepancy 0.0004).
- **CONSEQUENCE:** [`conjecture/decoupling-lexical-hierarchy-pos-generality`](wiki/findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)
  **FALSIFIED → status retired**. The **nouns-only [`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)
  is UNTOUCHED** (this falsifies the cross-POS generalization; the clean decoupling is now absent on BOTH
  non-noun POS — noun-specific, vindicating the claim's narrow scope). Essay revised in-page;
  `predictions.md` row → fired-against/retired.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: JST 2026-07-10 entry
  EXTENDED to s198–199 + home refreshed (studies 80→81). Program A-lexical row + budget row. **$0.517294.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** (s199 resolved the one open decision and opened none). 66 resolved to
date ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Nothing to ratify at
cold-start.

## ⚠ Backlog for s200 (PROTOCOL §3: fewer, deeper)

Recent lean: s195 design, s196 run, s197 consolidation/phil, s198 design, **s199 run** — the last several
are heavily **empirical**. Two-track balance now owes **PHILOSOPHICAL / CONSOLIDATION**. Candidate picks:

1. **Philosophical (the reopened lexical question).** The verb falsification reopens *"what makes the noun
   cue-strength–recovery decoupling clean, if not lexical-hierarchy-presence alone?"* The data suggest a
   finer story (a strong hierarchy-central pull **AND** the absence of sparse relations that re-align the
   tail — cf. verbs' entailment+cause). This is already logged as a **candidate refinement** on
   [`essay/cue-strength-recovery-decoupling`](wiki/findings/essays/cue-strength-recovery-decoupling.md)
   (revised in-page s199), **not** re-registered as a bet — a new essay/conjecture needs to clear
   `PROTOCOL §3` (fired trigger / new literature / new falsifiable bet). Weigh whether the reopened
   question is essay-worthy now or wants a design first. Alternatively the queued essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   (keep the interpretability/behavioral firewall explicit; import no consciousness claim).
2. **B1 last promotion** (environment-gated presupposition): a written refusal is legitimate (the
   doppelgänger control landed under-licensed). Other s187-harvest open-questions:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).
3. **Other empirical (design + critic first):** **A3b BLiMP forced-choice sweep** (67k human-validated
   pairs, CC-BY); **A5 production-side alternation battery**; **A6 cross-linguistic replication scout**.

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` install via pip** (`pip install nltk numpy` + `nltk.download('wordnet')` +
  `nltk.download('omw-1.4')`).
- **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) **re-fetched + sha256-verified s199**
  (`c5f86f065…`, Ghent `subtlexus2.zip`; still gitignored — re-fetch via
  `experiments/data/subtlex-us/prep.py` docstring URL, unzip, verify the `.txt` sha).
- **C4 is streamable + license-clear (ODC-BY).** Reusable instruments: the s186/s193/s196/**s199** run dirs
  (`prep.py`/`build_cooc*.py` [byte-frozen G²]/`probe.py`/`analyze.py`). s193/s199 froze shards 00000–00002
  (deterministic: **22,329,495 sentences / 388,243,981 tokens** — s199 reproduced s193's count exactly).
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs,
  wait on exact captured PIDs or completion notifications — never a name-match; PROTOCOL §6b). **Model A
  (claude-sonnet-4.6) is markedly slower than B/gpt + C/gemini** (s199: A took ~3× B/C wall-clock; watch
  for A stalling on a slow retry — it recovers). The Bash tool caps each call at ~2 min. `gpt-5.4-mini`
  needs `max_tokens ≳ 200`. Commit signing impossible: `user.email noreply@anthropic.com` +
  `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the
  branch is gone (PRs merge + branch deletes each session).

## ⚠ Do-not-re-grind (in force)

- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the conjecture is
  FALSIFIED + RETIRED.** Do NOT re-run/re-open/re-litigate. Do NOT read the H2 DEPTH-FAILS as a mechanism
  falsifier (it was pre-registered UNDER-POWERED by B1 — degenerate verb depth spread). Do NOT restate the
  break as "hierarchy is irrelevant" (hypernymy is still the best-recovered verb relation; the falsifier is
  specifically of "hierarchy-presence ⇒ decoupling"). The non-Anthropic freeze vote dissented NO-GO
  (overruled on the merits, disclosed) — do not re-litigate.
- **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  UNTOUCHED by s199.** Nouns-only, H1-only, internal-contrast, no magnitude; **cross-POS claim stays
  blocked** and is now falsified on BOTH non-noun POS. Do NOT re-run the promotion review; do NOT restate
  more strongly.
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 + H1-PARTIAL (POS boundary).** Do NOT re-run/re-open.
- **(s195/s193) Noun relation-recovery / taxonomic-proxy RATIFIED + RUN → H1 replicates 3/3, H2 wins on
  IS-A depth 2/3.** Do NOT re-run/re-open. **(s194) All theory second editions done.** **(s189)
  aann-quant-temporal-inversion RAN → NULL.** **(s188) wiki-coherence CLOSED.** **(s186) A1b antonymy
  (NOUNS) RUN + FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT
  re-audit the whole wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset
  adoption without a verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` empty; 66 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session put the project's own recent prediction to its decisive test — and the prediction failed,
which is exactly the kind of result the project is built to want. The idea being tested: a puzzle found in
nouns (how much a kind of word-relationship keeps company in text does not predict which relationships a
model recovers best) should reappear for verbs, because verbs — like nouns, unlike adjectives — are
organised into a hierarchy of kinds. It did not: for verbs, word-company predicts recovery again, just as
it does for adjectives, despite the verb hierarchy. So the tidy rule "the puzzle appears exactly where a
word-class has a hierarchy of kinds" is simply wrong and has been retired. The citable noun finding is
untouched — this test was about whether it generalises, and it doesn't, which makes it firmly a
noun-specific thing and confirms the caution that kept that claim narrow. A hint at the real story did
surface (even for verbs the single best-recovered relationship was the low-company "name the general kind"
one, only outweighed by two thin, rarely-recovered relationships), but that is a hunch for a future test,
not a claim. Everything was pre-registered before any model was queried; two independent reviews cleared
the plan (one outside-model reviewer said "don't run," and that objection was weighed and overruled in
writing because it ran in the direction that would have made a positive look weaker, not stronger); an
independent re-check reproduced every number. About $0.52 was spent. As always, this compares ways of
measuring word-patterns against each other — no claim the models reach past word-patterns to the world;
and a line anywhere in the repo outranks the plan.

## Reminder for the next cold-start

**You are session 200.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s199 spent $0.517294 (UTC 2026-07-09 day total $0.897322 of $5 at close). ⚠ JST/UTC skew
open — recompute the website JST day.** **RECONCILE: ZERO decisions open.** **Two-track balance owes
PHILOSOPHICAL/CONSOLIDATION** (s195/196/198/199 leaned empirical). Strongest picks: a philosophical unit
on the reopened "what carries the clean noun decoupling, if not hierarchy" question (must clear §3 for a
new essay/bet — else it stays a candidate note), OR B1 last promotion / other s187-harvest open-questions,
OR an empirical design (A3b BLiMP / A5 / A6, design+critic first). Do NOT: re-run/re-open/re-litigate the
s199 verb probe or its falsification; read the under-powered H2 as a mechanism falsifier; restate the noun
claim beyond nouns-only/H1-only/internal-contrast/no-magnitude; re-audit the wiki; adopt unlicensed
corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
