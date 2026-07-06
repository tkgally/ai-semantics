# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s184+s185+s186 together spent ≈ $0.4768**, booked to **UTC 2026-07-06** (s184 $0.002774 + s185
$0.00303375 + **s186 $0.4710** — the A1b probe $0.4661 + 4 review votes $0.00442 + smoke/liveness
~$0.0005). So if `date -u` still shows **2026-07-06**, the day stands at **≈$0.4768 of $5.00**
(~$4.52 headroom); if **2026-07-07+**, a **fresh $5.00**. Ledger: [`config/budget.md`](config/budget.md).

## State — s186 ($0.4661 probe): A1b antonymy shadow-saturation RAN → conjecture FALSIFIED

Single deep-unit session (workflow-mode's blessed fallback for one gated powered probe). Froze +
ran the A1b antonymy shadow-saturation probe
([`experiments/runs/2026-07-06-antonymy-shadow-saturation/`](experiments/runs/2026-07-06-antonymy-shadow-saturation/);
[`result/lexical-relation-shadow-saturation-v1`](wiki/findings/results/lexical-relation-shadow-saturation-v1.md)).
Built the frozen 6-WordNet-noun-relation item set (N=130/relation, freq-matched) + a
**contrastive-frame G² distributional control from a fetched Simple English Wikipedia dump**
(CC BY-SA 4.0, 21.3M sentences — the corpus lift the design flagged). **Two full pre-run review
rounds** (fresh critic + non-Anthropic vote each): **round 1 both NO-GO** (caught a stale-control
bug — 322 cues missing after a gold-rule change — + a gold-size confound); corrected (rebuilt
control; **hit@3** co-primary + size-matched + relation-agnostic **sent** control + calibration gate;
operationalized the verdict); **round 2 both GO-WITH-CONDITIONS**, honored. Ran the panel (2,730
calls, 6 empty/0 error, $0.4661, 3× parallel per-model); **post-run verifier reproduced every
figure**.

**VERDICT: FALSIFIED (both clauses).** Antonymy is **not** the least-separable relation — its HIT@3
residual (+0.61–0.67) is among the *largest*; **meronymy** is smallest 3/3. Raw recovery does **not**
track corpus cue-strength (Spearman −0.086; antonymy tops cue-strength but **hypernymy** tops
recovery; meronymy 2nd-most-cued yet worst-recovered). Residual arm **descriptive-only** per the
pre-registered calibration gate (control 𝒮 0.029 explains ~nothing), so the sharp finding is the
**cue-strength–recovery decoupling**, not a precise residual magnitude. Frame-ablation: antonym
recovery **survives** frame suppression. Fired essay
[`antonymy-outlier-distributional-shadow`](wiki/findings/essays/antonymy-outlier-distributional-shadow.md)
trigger (a) (surviving direction, scoped local-shadow per s151; `status: revised`); moved the
[`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) antonymy corner (did
NOT saturate); [`predictions.md`](wiki/predictions.md) bet a **loss**; conjecture `proposed → tested`.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**No decisions were opened this session** (the A1b run's value-laden choices were all ratified s185;
the s186 freeze corrections were mechanical/scoring fixes surfaced by pre-run review, not new
value-laden gates). Nothing to reconcile at s187 cold-start. 62 resolved to date
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Campaign state (Tom-directed; read `continue-prompt.md` §5 + `wiki/maintenance.md` before campaign work)

- **P1 `[x]` (s183); P2 `[x]` (s184); P3 `[x]` (s185). P4 STILL OWED** — the A1b deep unit took the
  whole of s186, so campaign P4 did **not** advance. **P4 next:** concept on-ramp deepening (each of
  the 17 concepts points at the current findings bearing on it) + **ideas-harvest triage** (Tier-1
  audit seeds in [`wiki/maintenance.md`](wiki/maintenance.md) → open-question pages / backlog rows;
  Tiers 2–3 kept with one-line dispositions). P5 = close-out (light spot re-audit, close ledger,
  delete continue-prompt §5). P4 is a light-to-medium phase — a good deep unit for a session, or it
  can share with a cheap empirical scout.

## ⚠ Empirical backlog (A1b now DONE — pick the next-most-owed)

- **NEW (from A1b): adjective-antonymy replication.** The A1b run is **noun-scoped** (WordNet's
  taxonomic relations are nominal). J&K's contrastive-frame signature is *adjectival*; a 2-relation
  (antonymy vs synonymy) adjective replication of the frame-ablation + residual arm would test
  whether the noun-scoped falsification holds where the contrastive frame is strongest. Cheap
  (reuse the frozen pipeline; adjectives have 996 antonym cues; the Wikipedia control already built).
  A natural, well-scoped next empirical unit.
- **NEW (from A1b): the cue-strength–recovery decoupling** — the most-cued relation (antonymy) is
  not the best-recovered (hypernymy); the 2nd-most-cued (meronymy) is worst-recovered. Logged in the
  result as a seed; could spawn an essay or a follow-up conjecture (what *does* predict relation-wise
  recovery, if not corpus cue-strength?).
- **A2b grounding magnitude** = external-resource **SCOUT only** (un-instrumentable in-repo;
  [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
  Ledger Tier-1 seed #4 (RAW-C/SAW-C license scout) is the adjacent text-side scout.
- **A3b BLiMP forced-choice sweep** — 67k human-validated minimal pairs, CC-BY, cataloged; a
  selected-paradigm sweep is cheap + human-agreement-anchored. Design + critic first.
- **A5 production-side alternation battery** (genitive / particle / locative, each with human
  corpus direction anchors); **A6 cross-linguistic replication scout** (UD in-scope).
- **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is
  legitimate (the s173 doppelgänger left it under-licensed).

## ⚠ Env notes (carry)

- `nltk`/WordNet + `numpy` install via `pip install nltk numpy` + `nltk.download('wordnet')` (used
  s186). **SubTLEX-US is unigram-only**; the A1b co-occurrence control came from a **fetched Simple
  English Wikipedia dump** (`experiments/runs/2026-07-06-antonymy-shadow-saturation/build_cooc.py` is
  the recipe; dump gitignored, re-fetchable; `control.json` committed, `counts.json` [27MB]
  gitignored). Corpus streaming: ~5 min for 21.3M sentences. **Run long probes with harness
  `run_in_background: true`; parallelize per-model (`probe.py --model A/B/C`) for ~3× wall-clock** —
  shell `&`-backgrounding gets killed when the Bash tool returns (learned s186); never name-match
  waits (PROTOCOL §6b). openrouter MCP flaky — use the probe REST path for votes
  (`experiments/lib/openrouter.py`, `max_tokens≈500`). Commit signing impossible: set `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s186) A1b antonymy is RUN + FALSIFIED — do NOT re-run it.** Do NOT re-open its ratified gates
  (Q1-C/Q2-A/Q3). The Simple English Wikipedia control is built and committed (control.json); do NOT
  re-scout the corpus license (Wikipedia CC BY-SA verified s185). An **adjective** replication is new
  work, not a re-run. The result is noun-scoped by design (WordNet taxonomy is nominal).
- **(s185) note-sweep P3 done — do NOT re-run.** **(s184) Do NOT mass-edit `supported`-at-creation
  results; do NOT flip theory to `live` off a non-substantive touch.** **(s183) Do NOT re-audit the
  whole wiki** — work from [`wiki/maintenance.md`](wiki/maintenance.md). Do NOT mass-retarget
  theory-v1 refs. **(s182) No B3 destructive essay merges.** **(s181) A2a re-runs DONE.** **(s179)
  Cite theory -v2s.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset
  adoption without a verified license.

## Next concrete actions — backlog for session 187 (PROTOCOL §3: fewer, deeper)

1. **CONSOLIDATION — campaign P4 (owed, deferred from s186):** concept on-ramp deepening + ideas
   triage (from [`wiki/maintenance.md`](wiki/maintenance.md)). A good deep consolidation unit.
2. **EMPIRICAL — adjective-antonymy replication** (cheap, reuses the s186 pipeline + control) OR an
   A2b/A3b/A6 scout. Keeps the empirical track moving; pairs well with P4.
3. **PHILOSOPHICAL — the cue-strength–recovery decoupling** could spawn an essay or conjecture (what
   predicts relation-wise recovery if not corpus cue-strength?) — a fired-observation seed from s186.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md): a substantive session → extend **today's** JST
   entry (check `TZ=Asia/Tokyo date`).

## Open decisions

**ZERO.** 62 resolved to date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- This session built and ran the "opposites" experiment planned over the two prior sessions, and the
  project's own advance guess turned out **wrong** — in an informative way. The idea was that a
  model's fluency with opposites (hot/cold) might be nothing more than an echo of how often opposites
  keep company in text. Against a word-company baseline built from ~21 million sentences of openly
  licensed Wikipedia text, the models' opposites **clearly beat** that baseline (so not a mere echo),
  opposites weren't even the relationship the models handled best (naming a general category was), and
  how much a relationship keeps company in text didn't predict how well the models recovered it at
  all. One honesty note kept the claim modest: the baseline was a weak yardstick, so the crisp result
  is that mismatch, not a precise "how far beyond" figure. Before any money was spent the plan was
  double-checked by two independent reviewers twice over, who caught two real bugs that were fixed
  first; an independent reviewer re-checked the final numbers against the raw outputs. About $0.47
  spent. If you want the maintenance campaign (now at phase 4) paced differently, a line anywhere in
  the repo outranks the plan.

## Reminder for the next cold-start

**You are session 187.** Entry [`continue-prompt.md`](continue-prompt.md) (note its **§5 campaign
section**, at **P4 — still owed**); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC
— check `date -u`; s184+s185+s186 spent ≈$0.4768** (2026-07-06). **RECONCILE: ZERO decisions open.**
Most-owed: **campaign P4** (concept on-ramps + ideas triage, deferred from s186), pairing with a
cheap empirical unit — the new **adjective-antonymy replication** (reuses the s186 pipeline) or an
A2b/A3b/A6 scout; or develop the **cue-strength–recovery decoupling** seed. Do NOT: re-run/re-open
A1b (RUN + falsified), re-scout its corpus, re-run the note-sweep, re-audit the wiki, mass-edit
`supported`-at-creation results, flip theory to `live` off a non-substantive touch, B3 merges, A2a
re-runs, founding-question re-opens, unlicensed corpus adoption. End squash-merged to `main`;
`git fetch --prune` at cold-start.
