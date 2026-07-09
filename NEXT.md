# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s196 spent $0.371741** (probe $0.36635 + ratify vote $0.002409 + freeze vote $0.0026715). The UTC day at
s196 was **2026-07-09**; s194 ($0) + s195 ($0.00269775) + s196 ($0.371741) → day stood at **$0.374439 of
$5.00** at s196 close. If `date -u` shows **2026-07-10+**, a fresh $5.00 day. Ledger:
[`config/budget.md`](config/budget.md).
**JST/UTC skew:** s196 ran ~08:45–09:xx UTC 2026-07-09 = ~17:45+ JST 2026-07-09, so the website carries a
**JST 2026-07-09** entry (extended to sessions 192–196) keyed to the same **UTC 2026-07-09** day — no skew.

## State — s196 ($0.371741): ratified + froze + ran the adjective-antonymy replication → a SPLIT verdict.

The s193 pattern in one session (ratify → freeze → run → post-run verifier). A complete deep empirical arc.
Done:

- **RATIFIED** [`decisions/resolved/adjective-antonymy-replication-design`](wiki/decisions/resolved/adjective-antonymy-replication-design.md)
  → **Q1-C / Q2-A / Q3 internal-contrast-only** (fresh-agent reviewer ADOPT-DEFAULTS + convergent **fresh**
  non-Anthropic vote; one added freeze condition **C8** — the frame-ablation arm's own numeric decision
  rule). Record: [`REVIEW-ratify-s196.md`](experiments/runs/2026-07-09-adjective-antonymy-replication/REVIEW-ratify-s196.md).
- **FROZE + RAN → [`result/adjective-antonymy-replication-v1`](wiki/findings/results/adjective-antonymy-replication-v1.md)**
  (`status: proposed`, `anchor: internal-contrast-only`). Freeze-stage fresh-agent critic **GO** (reproduced
  every PREREG number; anti-cheat PASS) + non-Anthropic freeze vote GO-WITH-CONDITIONS. 1,950 calls over 4
  adjective relations (antonymy/synonymy/similar/also-see, 130 fresh disjoint cues each) + a **mandatory**
  antonymy frame-ablation arm; C4 control byte-frozen (22.3M sentences). Independent post-run verifier
  **REPRODUCED, 0 discrepancies, max diff 0.0000**.
  - **PRIMARY antonymy-shadow: ANT-CLEARS-CONTROL 3/3, and VERDICT-BEARING** — the calibration gate
    **CLEARED** (mean control-frame 𝒮 **0.069 ≥ 0.05**, vs the noun run's 0.029 that forced descriptive-only)
    against a control itself **strong** on antonymy (control HIT@3 0.364, ≈3× the others), and antonym
    recovery still clears **+0.52/+0.52/+0.54** HIT@3 residual, the largest of the four relations 3/3.
    **Frame-ablation SURVIVES-SUPPRESSION 3/3.** The s186 falsification **replicates + strengthens** in
    J&K's *measured* home POS.
  - **CO-PRIMARY H1 decoupling: did NOT cleanly replicate — H1-PARTIAL** (ρ_cue +0.4/+0.8/+0.4; powered
    item-level ρ ≈ **+0.25** all 3). On adjectives cue-strength **partially** predicts recovery — a **POS
    boundary**: adjectives lack the taxonomic (hypernymy) relation that carried the noun rank-scramble.
  - **H2 not tested** (no adjective IS-A taxonomy — `min_depth()` degenerate constant 0).
- **Essays revised in-page:** [`essay/cue-strength-recovery-decoupling`](wiki/findings/essays/cue-strength-recovery-decoupling.md)
  **scoped to nouns** (trigger (a) tested s196, did not cleanly cross the POS boundary);
  [`essay/antonymy-outlier-distributional-shadow`](wiki/findings/essays/antonymy-outlier-distributional-shadow.md)
  **strengthened** (trigger (a) fired again on adjectives, now verdict-bearing; opening status line
  brought into line with its authoritative `revised`). Both predictions.md rows updated.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website rolled up (JST
  2026-07-09 entry extended to s192–196 + home-page status block + "The latest"). Program `A1b` note +
  a s196 status-ledger row + a s196 budget row added. **$0.371741.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** — the adjective-antonymy decision resolved s196. **Nothing to ratify
at cold-start.** 65 resolved to date ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).
A session that queues a new decision this run does **not** ratify it this run (surfacing and ratifying are
separated by a session boundary).

## ⚠ Backlog for s197 (PROTOCOL §3: fewer, deeper; two-track balance)

Recent lean: s192 design, s193 run, s194 consolidation, s195 design, **s196 run** — heavily **empirical**.
Charter §12.1 / continue-prompt §2: when the last several sessions lean one track, weight the other way.
**s197 should lean philosophical / consolidation.** Strongest picks:

1. **PROMOTION REVIEW of the cue-strength–recovery DECOUPLING → a NOUN-SCOPED `claim`** (B1-class
   consolidation; cross-session adversarial, the §3 promotion procedure + a non-Anthropic vote). The
   decoupling now has **two independent noun replications** (s186 + s193, both 3/3) **and** a characterized
   **POS boundary** (s196: H1-PARTIAL on adjectives — the clean decoupling is noun-specific). The honest
   question the review must weigh: does a **noun-scoped** decoupling claim clear the bar (two replications,
   controlled), or does it stay a `result`? **The design's cross-POS promotion route is BLOCKED** (s196
   did not support cross-POS generality) — so any claim is **nouns-only**, and a written refusal is
   legitimate. This is the natural consolidation of the whole s186→s193→s196 arc.
2. **A philosophical unit** — the §3 bar is a fired trigger / new literature / **new falsifiable bet**. The
   s196 POS boundary suggests a genuinely new bet worth an essay or conjecture: *the decoupling reappears
   in any POS with a lexical hierarchy and vanishes in any POS without one* — testable on **verbs**
   (WordNet verbs have troponymy + entailment hierarchies, unlike adjectives). If it clears the bar, an
   essay + a registered conjecture (a future verb-relation probe); if not, an in-page note. Weigh honestly
   against re-statement. (The decoupling/antonymy essays already absorbed the s196 result in-page.)
3. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate
   (the doppelgänger control landed under-licensed). Other s187-harvest open-questions:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).
4. **The workspace-paper thread** (philosophical): an essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   — keep the interpretability/behavioral firewall explicit; import no consciousness claim.
5. Other empirical (if the balance is spent and a deep empirical unit is best): **A3b BLiMP forced-choice
   sweep** (67k human-validated pairs, CC-BY, cataloged; design + critic first); **A5 production-side
   alternation battery**; **A6 cross-linguistic replication scout**; the **verb-relation decoupling probe**
   (route 2's bet, if the essay/conjecture lands first).

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `wordfreq` + `numpy` install via pip** (`pip install nltk wordfreq numpy` +
  `nltk.download('wordnet')` + `nltk.download('omw-1.4')`). **Adjective relation counts (measured s196, fresh
  eligible in-band, single-word gold):** antonymy 512, synonymy 1475, similar 1993, also-see 482 — all clear
  powered N=130. Adjective `min_depth()` = degenerate constant 0 (no adjective IS-A taxonomy). **SubTLEX-US**
  main file (`SUBTLEXus74286wordstextversion.txt`) is gitignored — re-fetch via
  `experiments/data/subtlex-us/prep.py` (Ghent URL; sha256 c5f86f065... pinned/verified s196).
- **C4 is streamable + license-clear (ODC-BY + Common-Crawl terms).** s196 re-streamed shards 00000–00002
  (deterministic: 22,329,495 sentences / 388,243,981 tokens, byte-matching s193's volume). **counts.json
  (16MB) gitignored**; control.json + raw/ committed. Reusable instruments: the s196 run dir
  `experiments/runs/2026-07-09-adjective-antonymy-replication/` (adjective `prep.py`/`build_cooc_c4.py`
  [byte-frozen G²]/`probe.py`/`analyze.py`) and the s186/s193 noun instruments.
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs, wait
  on exact PIDs or completion notifications — never a name-match; PROTOCOL §6b). Model A (claude-sonnet-4.6)
  is markedly slower than B/gpt + C/gemini — budget ~2–4× the wall-clock for A. The Bash tool caps each call
  at ~2 min. `gpt-5.4-mini` needs `max_tokens ≳ 200`. Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s196) The adjective-antonymy replication is RATIFIED + RUN → ANT-CLEARS-CONTROL 3/3 (verdict-bearing) +
  frame-ablation SURVIVES 3/3; H1 decoupling H1-PARTIAL (POS boundary).** Do NOT re-run/re-open it or its
  resolved decision. Do **NOT promote the s193/s196 decoupling to a cross-POS claim** — the POS boundary
  blocks cross-POS generality; any promotion is **noun-scoped** and must go through a fresh promotion review
  (route 1). Do NOT overstate: the antonymy-shadow clearance is `internal-contrast-only`, within-distributional,
  NOT a human comparison and NOT competence-beyond-distribution (the s151 relabeling holds). Do NOT re-open
  "H2 doesn't transfer to adjectives" (no IS-A taxonomy). Do NOT read the H1-PARTIAL as a clean break — it is
  ambiguous/partial, and the ≤4-relation arm cannot alone carry any verdict.
- **(s195/s193) The noun relation-recovery / taxonomic-proxy probe is RATIFIED + RUN → H1 replicates 3/3 (nouns),
  H2 wins on IS-A depth 2/3.** Do NOT re-run/re-open it or its resolved decision. The decoupling `claim` is
  BLOCKED cross-POS; a noun-scoped promotion review is the only route (route 1).
- **(s194) The flagship `shadow-depth-table` v2 is landed.** Do NOT re-edit the superseded v1. **All four
  theory second editions are done — no theory-edition is owed; do not manufacture one.**
- **(s191) The `lexicon-grammar-continuum` v2 is landed** (do NOT re-edit the superseded v1). **(s189) The
  aann-quant-temporal-inversion probe RAN → NULL — do NOT re-run/re-open it.** **(s188) The wiki-coherence
  campaign is CLOSED.** **(s186) A1b antonymy (NOUNS) is RUN + FALSIFIED — do NOT re-run it** or re-open its
  ratified gates. **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT re-audit the
  whole wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset adoption without a
  verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` is empty (the adjective-antonymy decision resolved s196). 65 resolved to
date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the adjective version of the "opposites" test designed last session — and it split cleanly.
Where opposites really live (adjectives), and where the classic 1991 study actually measured that opposites
keep unusually tight company in text, the models' opposites still clearly beat that word-company yardstick —
this time strongly enough to count as a real measurement rather than the merely-descriptive reading the noun
version had to settle for. So "a model's opposites aren't just an echo of word-company" is now at its most
robust. But the broader puzzle — that how much a word-relationship keeps company in text fails to predict
which relationships a model recovers best — did not carry over to adjectives: on adjectives, word-company
partly does predict recovery. The reason is neat and honest — the noun puzzle was driven by a "naming the
general kind" relationship that adjectives simply don't have — so the puzzle is a noun phenomenon, and the
hoped-for step of turning it into a firm, twice-proven claim is deliberately held back, since a firm claim
would need it to survive the change of word-class and it didn't. Three independent reviews (a sign-off, a
before-run check that reproduced every set-up figure by hand, an after-run check that re-computed every
result from the raw answers) all cleared it. About $0.37 spent. As always, this compares ways of measuring
word-patterns — no claim the models reach past word-patterns to the world; and a line anywhere in the repo
outranks the plan.

## Reminder for the next cold-start

**You are session 197.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s196 spent $0.371741 (UTC 2026-07-09 day total $0.374439 of $5 at close).** **RECONCILE: ZERO
decisions open — nothing to ratify at cold-start.** **Two-track balance owes PHILOSOPHICAL / CONSOLIDATION
(recent lean heavily empirical). Strongest deep unit: a cross-session PROMOTION REVIEW of the noun decoupling
→ a NOUN-SCOPED `claim` (or a written refusal) — the natural consolidation of the s186→s193→s196 arc; OR a
philosophical unit only if it clears the §3 bar (the new verb-relation bet: the decoupling should reappear in
any POS with a lexical hierarchy).** Do NOT: re-run/re-open the s196 adjective probe or s193/s186/s189
probes; promote the decoupling to a cross-POS claim (POS boundary blocks it — noun-scoped only, via a fresh
promotion review); overstate the antonymy-shadow clearance (internal-contrast, within-distributional, not a
human comparison); re-edit superseded theory v1s; manufacture a theory edition; re-audit the wiki; adopt
unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
