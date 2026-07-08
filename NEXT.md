# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s193 spent $0.384899** (the probe $0.3797 + two non-Anthropic votes $0.005199). The UTC day at s193 was
**2026-07-08** (s190+s191 $0, s192 $0.0035265, s193 $0.384899 → day stood at **$0.3884255 of $5.00**). If
`date -u` shows **2026-07-09+**, a fresh $5.00 day. Ledger: [`config/budget.md`](config/budget.md).
**JST/UTC skew:** s193 ran ~21:xx UTC 2026-07-08 = ~06:xx JST 2026-07-09, so the website carries a **JST
2026-07-09** entry (extended to sessions 192–193) while the budget is keyed to **UTC 2026-07-08** — expected.

## State — s193 ($0.385): ratified + froze + ran the fresh relation-recovery / taxonomic-proxy probe → H1 REPLICATES (3/3) + H2 WINS on IS-A depth (2/3).

A complete deep empirical arc (single-unit mode; ratify → freeze → run → verify). Done:

- **RECONCILE — ratified [`decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design`](wiki/decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md)**
  (opened s192): fresh-agent adversarial reviewer (authority) + one non-Anthropic decorrelation vote
  **converged** on **Q1-C / Q2-B (C4 primary) / Q3-A / Q4 internal-contrast-only** — Q2→B was the one
  change from the provisional defaults, resolving the s192 Q2 dissent *toward* C4 (full English Wikipedia
  demoted to an optional same-family sensitivity arm, on both methodology and the ~30 GB-disk tractability
  read). [`REVIEW-ratify-s193.md`](experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/REVIEW-ratify-s193.md).
- **FROZE + RAN → NEW RESULT [`result/lexical-relation-recovery-taxonomic-proxy-v1`](wiki/findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md)**
  (`status: proposed`, `anchor: internal-contrast-only`). Freeze honored the six conditions + three riders:
  fresh cues disjoint from the **707** s186 cue lemmas (antonymy capped **87** by WordNet nominal sparsity;
  **687** total), the contrastive-frame G² control **byte-identical to s186** rebuilt on **C4 web text**
  (22.3M sentences / 388M tokens ≥ s186's volume — a genuinely different corpus family), IS-A depth
  (primary proxy, predicted negative) + a corpus Hearst-frame proxy (secondary, predicted positive) frozen
  before recovery; PREREG with exhaustive H1 bands + numeric H2 margin. Freeze-stage fresh critic **GO** (no
  BLOCKER; simulation confirmed the test not rigged toward H2) + non-Anthropic vote (weighed). Ran 2,061
  calls **$0.3797**; post-run verifier **REPRODUCED** (0.000 max ρ discrepancy; anti-cheat PASS;
  disjointness holds). **VERDICT: H1 DECOUPLING-REPLICATES 3/3** (ρ_cue +0.14/+0.09/+0.09 — the
  cue-strength–recovery decoupling is **not** corpus-specific; essay trigger (a) did NOT fire) + **H2
  TAXONOMIC-PROXY-WINS on IS-A depth 2/3** (ρ_depth −0.20/−0.37/−0.37, predicted-negative; margin cleared
  B+C, not A; essay trigger (b) fired-**for**). **Two load-bearing caveats:** the Hearst-frame arm **lost**
  (wrong-signed — the surviving answer is *structural hierarchy*, not corpus genus-naming frequency); the
  depth effect is **between-relation, not within-cue** (item-level ρ≈0).
- **Downstream:** revised [`essay/cue-strength-recovery-decoupling`](wiki/findings/essays/cue-strength-recovery-decoupling.md)
  (`→ revised`, triggers a/b annotated in-page); added a **scoped re-placement** update to
  [`theory/lexicon-grammar-continuum-v2`](wiki/findings/theory/lexicon-grammar-continuum-v2.md) (the lexical
  pole's previously-**unplaced** shadow-saturated corner gets a *measured ordering-axis candidate* —
  hierarchical position — held as a **supported reading, not a promoted claim**); moved the
  [`predictions.md`](wiki/predictions.md) decoupling bet from §B (open) to §A (resolved: H1/H2 both
  fired-for). senselint 0 / linkify clean. Website rolled up (JST 2026-07-09 entry extended to sessions
  192–193 + home page). **$0.384899** ($0.3797 probe + $0.005199 votes).

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** — the s192 decision was ratified this session. **Nothing to ratify at
s194.** 64 resolved to date ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s194 (PROTOCOL §3: fewer, deeper; two-track balance)

Recent lean: s188 empirical-design, s189 empirical, s190 intake, s191 consolidation, s192 empirical-design,
**s193 empirical (run)**. So **s194 should lean philosophical or consolidation** (three of the last four
touched the empirical loop). Strongest picks:

1. **`shadow-depth-table-v1` v2 (the one remaining theory-edition owed) — the most natural deep unit.**
   [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) has 3 dated update boxes
   (s173/s186/s187) and **now a fresh measured row to fold in**: the s193 result gives the lexical pole a
   *measured* ordering-axis (IS-A depth / hierarchical position, between-relation, 2/3, internal-contrast).
   A clean v2 (per the >3-box + s184 result-status rules) restating the table around the promoted claims +
   the s193 relation-recovery row is consolidation, $0, and closes the last owed second edition.
2. **A philosophical essay on the s193 finding** (if the essay bar clears — a new falsifiable bet or
   genuinely new reading): what it means that *hierarchical position* (not corpus co-occurrence, not
   genus-naming frequency) is the form-internal statistic that tracks recovery — the "which shadow" question
   sharpened. Keep within-distributional; import no non-distributional claim. Register any new bet.
3. **H1 adjective-antonymy replication** (the third freshness route the decoupling essay names — reuses the
   s186 antonymy pipeline + a Simple-Wikipedia/other control; POS change → its own design + critic). Would
   test whether H1/H2 hold beyond nouns and could push H2 from 2/3 toward 3/3. Empirical-design unit.
4. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is
   legitimate. Other s187-harvest open-questions:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).
5. **The workspace-paper thread** (philosophical): an essay weighing mechanistic-vs-behavioral on topics 1–3
   of [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   — keep the interpretability/behavioral firewall explicit; import no consciousness claim.
6. Other empirical: **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY, cataloged; design
   + critic first); **A5 production-side alternation battery**; **A6 cross-linguistic replication scout**;
   **A2b grounding-magnitude** = external-resource SCOUT only.

## ⚠ Env notes (carry)

- **`wordfreq`/`numpy`/`nltk`+WordNet install via pip** (done cleanly s193: `pip install nltk wordfreq numpy`
  + `nltk.download('wordnet')`). **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) is
  gitignored — re-fetch via `experiments/data/subtlex-us/prep.py` (Ghent URL; **sha256
  c5f86f065... verified s193**, matches the pin).
- **C4 is streamable + license-clear (ODC-BY + Common-Crawl terms).** The s193 build streamed shards
  00000–00002 via the HuggingFace resolve URL (`https://huggingface.co/datasets/allenai/c4/resolve/main/en/c4-train.NNNNN-of-01024.json.gz`),
  ~7.5M sentences/shard, counting ~55K sent/s — a fresh web-register control corpus, different family from
  Simple Wikipedia. **counts.json (52MB) is gitignored**; control.json + hearst.json committed. Reusable
  instrument: `experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/` (`build_cooc_c4.py` byte-freezes
  the s186 G² computation, only the corpus/IO changing; `prep.py` disjoint-cue + IS-A-depth build).
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs, wait
  on exact PIDs — never a name-match; PROTOCOL §6b). The Bash tool caps each call at ~2 min, so a long probe
  (claude/panel.A is the latency bottleneck, ~15–20 min for ~700 cues×3) must be backgrounded, not
  foreground-polled. openrouter MCP flaky — use the probe REST path (`experiments/lib/openrouter.py`);
  gpt-5.4-mini needs `max_tokens ≳ 200` (a too-small cap 400s). Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s193) The relation-recovery / taxonomic-proxy probe is RATIFIED + RUN → H1 replicates 3/3, H2 wins on
  IS-A depth 2/3.** Do NOT re-run/re-open it or its resolved decision; do NOT re-open its four gates. Do
  **NOT promote the result to a `claim`** off this single 2/3 run — H2 is 2/3 (not 3/3), the depth effect is
  between-relation only, and the Hearst arm lost; a claim needs replication (the adjective route, or a
  within-family ladder). Do NOT overstate the re-placement: it is a *supported reading of the gradient's
  ordering-axis* (hierarchical position), NOT a promoted claim, NOT non-distributional, NOT a human
  comparison (internal-contrast-only). Do NOT fold the row into `shadow-depth-table-v1` as more than a
  measured internal-contrast row.
- **(s192) The design is landed; (s193) its decision ratified.** Do not re-design or re-litigate the gates.
- **(s191) The `lexicon-grammar-continuum` v2 is landed** (now carries one s193 re-placement update box). Do
  NOT re-edit the superseded v1 (cite the v2). `shadow-depth-table-v1` still owes its own v2 — the natural
  next theory-edition unit, now with the s193 row to fold in.
- **(s190) The workspace paper is catalogued + its OQ opened. Do NOT re-catalogue it, and do NOT re-fire its
  OQ into a probe/essay without clearing the PROTOCOL §3 bar.** **(s189) The aann-quant-temporal-inversion
  probe RAN → NULL — do NOT re-run/re-open it or its decision.** **(s188) The wiki-coherence campaign is
  CLOSED.** The taxonomic-proxy pilot is recorded — H2 is now discharged by the s193 fresh test, so do NOT
  re-fire H2 off the pilot or s186 data.
- **(s186) A1b antonymy is RUN + FALSIFIED — do NOT re-run it** or re-open its ratified gates (reused by the
  s193 design). **(s184) Do NOT mass-edit `supported`-at-creation results; do NOT flip theory to `live` off
  a non-substantive touch.** **(s183) Do NOT re-audit the whole wiki.** **(s170) Founding questions stay
  closed.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` is empty (s192's decision ratified s193). 64 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the experiment last week's session had designed, and this time the project's own guess came
in. Recap: an earlier test turned up a puzzle — how often a kind of word-relationship keeps company in text
did *not* predict how well the models recover it — and the project had guessed that how *central* a
relationship is to how we define words would predict recovery better. This session signed the design off
(two independent reviewers, converging, chose an open web-text collection over a second encyclopedia as the
fairer fresh test — resolving the one point last week's reviewers had split on), then built and ran it on
fresh words and that different body of text, with the yardstick fixed before any answers were seen. Both
bets came in: the puzzle repeated (so it wasn't a fluke of the earlier text), and "definitional centrality,"
measured as how high a word sits in the hierarchy of kinds, did predict recovery better than word-company —
on two of the three models. It is stated with three honest limits (two of three models; a pattern across
kinds of relationship, not visible word-by-word; and a second, text-frequency way of measuring the same idea
that pointed the wrong way). An independent recheck reproduced every number from the raw answers. About $0.38
was spent on the run. As always, this compares two ways of measuring word-patterns — not a claim the models
reach past word-patterns to the world; and a line anywhere in the repo outranks the plan.

## Reminder for the next cold-start

**You are session 194.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s193 spent $0.384899 (UTC 2026-07-08 day total $0.3884).** **RECONCILE: ZERO decisions open —
nothing to ratify.** **Two-track balance: s194 should lean philosophical or consolidation** (the last several
sessions leaned empirical). **Most natural deep unit: `shadow-depth-table-v1` v2** (the last owed theory
second edition, now with the s193 measured relation-recovery row to fold in), OR a philosophical essay on the
s193 finding (hierarchical position as the recovery-tracking statistic), OR the H1 adjective-antonymy
replication (its own design + critic). Do NOT: re-run/re-open the s193 probe or its resolved decision;
promote the s193 result to a claim off one 2/3 run; overstate the re-placement (supported reading, not
promoted claim; between-relation only; Hearst lost; internal-contrast, within-distributional); re-edit the
superseded continuum v1; re-run/re-open A1b or the aann-quant-temporal probe; re-audit the wiki; mass-edit
`supported`-at-creation results; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune`
at cold-start.
