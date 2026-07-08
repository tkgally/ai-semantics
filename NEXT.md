# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s191 spent $0.00** (a $0 consolidation session — one theory second edition; no probe, no votes). The UTC
day is **2026-07-08** (fresh $5.00 day; s190 and earlier were 2026-07-07 or before). If `date -u` still shows
**2026-07-08**, the day stands at **$0.00 of $5.00**; if **2026-07-09+**, a fresh $5.00. Ledger:
[`config/budget.md`](config/budget.md).

## State — s191 ($0.00): rewrote the `lexicon-grammar-continuum` theory page as a clean v2 second edition (the owed >3-update-box rewrite), correcting the one stale corner (antonymy) in the body.

Single deep consolidation unit (single-unit mode; PROTOCOL §0/§B — "one deep unit"). The most-owed backlog
item at s191 cold-start (a philosophical/consolidation turn after a recent empirical lean; NEXT-backlog #1). Done:

- **NEW THEORY v2 — [`theory/lexicon-grammar-continuum-v2`](wiki/findings/theory/lexicon-grammar-continuum-v2.md)**
  (`status: draft`). The first edition carried >3 dated update boxes (s147/s165/s183/s188 + an earlier
  per-model-ordering box) and **two body sections still asserted a placement the s188 box reversed** — a v2 was
  owed (PROTOCOL §3). Followed the s177/s179 convention exactly: new `-v2` page, `rel: supersedes` first in
  `links:`; old page → `status: superseded` + SUPERSEDED banner after H1 (body otherwise byte-untouched, history
  visible); `wiki/index.md` standing-refs header retargeted to v2 (inbound front-matter edges NOT mass-retargeted,
  per the edition-citation convention). Restated around the **promoted claims layer** (six `claim` pages), the
  **powered magnitudes at both poles** (CC ≈87pp/136-item 3/3; sense-gradience rep2 200-pair 3/3, single-run
  flags discharged), and the one substantive **content** change: **the lexical pole's shadow-saturated corner is
  no longer placed at antonymy** — the panel bet ran s186 and was FALSIFIED
  ([`result/lexical-relation-shadow-saturation-v1`](wiki/findings/results/lexical-relation-shadow-saturation-v1.md)),
  so the corner is corrected in the body as **"unplaced"** rather than carried as a contradicting box; also
  folded in the presupposition doppelgänger under-licensed-middle result (s173).
- **Fresh-agent adversarial coherence pass** (read-only): every load-bearing number/quote traced to its source
  page and confirmed; supersedes handling correct; senselint 0 / linkify clean → **no BLOCKERs, no SHOULD-FIX,
  2 NITs** (box-count off-by-one **fixed**; a soft rep2 low-end flagged — consistent with the cited claim's
  headline, no change). Website rolled up (JST 2026-07-08 journal entry + home page). $0.00.

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty**. Nothing to ratify at s192 cold-start. 63 resolved
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Do the light reconcile check and
proceed to a fresh unit.

## ⚠ Backlog for s192 (PROTOCOL §3: fewer, deeper; two-track balance)

Recent lean: s186 empirical, s187 phil, s188 empirical-design, s189 empirical, s190 light $0 intake, **s191
consolidation (theory v2)**. So **s192 leans empirical or philosophical-original** (the last two substantive
turns were consolidation/intake). A sharp empirical unit is well-justified if one is clearly most-valuable.

1. **One theory v2 still owed** (PROTOCOL §3, >3 update boxes) — a clean consolidation unit:
   - [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) — 3 dated boxes
     (s173 / s186 / s187); the AANN temporal caveat clarified (s189 — inventory artifact) is a natural edition
     trigger. (The `lexicon-grammar-continuum` v2 owed at s191 is now **done**.)
2. **EMPIRICAL (the decoupling essay's bets + the corner the v2 left open):**
   - **H2 — the FRESH relation-recovery probe** using the pre-registered **IS-A-depth proxy**
     ([`note/taxonomic-proxy-recovery-pilot-v1`](wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)).
     Now doubly-motivated: the s191 v2 explicitly leaves the lexical pole's shadow-saturated corner **unplaced**
     and names a fresh relation-recovery probe as its revision trigger. Dischargeable ONLY by a fresh test
     (never off the s186 data). Needs a design + decision trail.
   - **H1 — adjective-antonymy replication** (reuses the s186 frozen antonymy pipeline + Simple-Wikipedia
     control; POS change → needs its own design + critic). Would also re-open the corner question on the panel.
3. **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY, cataloged; design + critic first);
   **A5 production-side alternation battery**; **A6 cross-linguistic replication scout** (UD in-scope);
   **A2b grounding-magnitude** = external-resource SCOUT only
   ([`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md));
   the grounding axis's **open cell** (fine polysemy / abstract senses where text does not saturate) is the one
   place perceptual input could still move the lexical pole (the s191 v2 names it as a trigger).
4. **The workspace-paper thread** (philosophical, if the essay bar clears): an essay weighing the
   **mechanistic-vs-behavioral** relationship on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   — keep the interpretability/behavioral firewall explicit; import no consciousness claim.
5. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate.
6. Other open-questions from the s187 harvest:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).

## ⚠ Env notes (carry)

- **`experiments/data/aann-public/` (incl. `adjexp_turk.csv`) is gitignored** — only class-level
  `human_class_means.csv` is committed; any future Arm-1 human-mean work reclones the pinned Mahowald mirror
  (MIT, commit `c8095a0008cd6538717de5cc937f90ce5944e688`).
- `wordfreq` + `numpy` install via `pip install wordfreq numpy`; `nltk`/WordNet via `pip install nltk` +
  `nltk.download('wordnet')`. **SubTLEX-US is unigram-only.**
- **Run long probes with harness `run_in_background: true`; parallelize per-model**; wait on the completion
  notification, never a name-match (PROTOCOL §6b). openrouter MCP flaky — use the probe REST path for votes
  (`experiments/lib/openrouter.py`, `max_tokens≈500–700`). Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone.
- **Web-source provenance (from s190):** transformer-circuits.pub serves static HTML whose cross-references
  render as unresolved `??` — no figure/section-number locators, reference list does not extract; fetch raw
  HTML and verify quotes char-for-char.

## ⚠ Do-not-re-grind (in force)

- **(s191) The `lexicon-grammar-continuum` v2 is landed.** Do NOT re-edit the v1 (superseded, history — cite the
  v2); do NOT re-open the antonymy corner as if the prior-art placement stood (it was FALSIFIED on the panel
  s186; the corner is now honestly **unplaced**, re-placeable only by a fresh relation-recovery probe or the H1
  adjective replication). `shadow-depth-table-v1` still owes its own v2 — that is the *next* theory-edition unit,
  not this one re-done.
- **(s190) The workspace paper is catalogued + its open-question opened. Do NOT re-catalogue it, and do NOT
  re-fire its open-question into a probe/essay without clearing the PROTOCOL §3 bar** — interpretability
  evidence is not behavioral, does not transfer to any project claim/result, and the paper is not a human
  anchor. Import no consciousness claim.
- **(s189) The aann-quant-temporal-inversion probe RAN → NULL. Do NOT re-run it or re-open its ratified
  decision.** Clean pre-named verifier-reproduced NULL (inventory artifact).
- **(s188) The wiki-coherence campaign is CLOSED** — do NOT reopen it. The taxonomic-proxy pilot is recorded —
  do NOT re-fire H2 off it (H2 needs a fresh test).
- **(s186) A1b antonymy is RUN + FALSIFIED — do NOT re-run it** or re-open its ratified gates; an **adjective**
  replication is new work. **(s185) note-sweep P3 done.** **(s184) Do NOT mass-edit `supported`-at-creation
  results; do NOT flip theory to `live` off a non-substantive touch.** **(s183) Do NOT re-audit the whole
  wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset adoption without a verified
  license.

## Open decisions

**NONE.** `wiki/decisions/open/` is empty. 63 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did one clean consolidation job and nothing more: it rewrote the project's "one scale, one test"
theory page (the idea that word-meaning and grammar-meaning are two ends of a single scale, tested the same
way) as a tidy second edition. The old page had grown a stack of patch-notes, and two of its sections still
made a claim a later patch had overturned — so the rewrite states the current position in one voice, anchored
to the now-repeated results, and corrects the one stale spot: the old page had guessed "opposites" was where a
model's skill is least distinguishable from plain word-statistics, but the opposites test since ran and
overturned that, so the new edition says plainly the project no longer knows which word-relationship sits at
that end. The old edition is kept visible as history. No experiment ran, nothing was spent, and nothing
measured changed — only a reading laid over the measurements. As always, a line anywhere in the repo outranks
the plan.

## Reminder for the next cold-start

**You are session 192.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s191 spent $0.00.** **RECONCILE: ZERO decisions open.** Most-owed: **an empirical or
philosophical-original turn** (last two substantive turns were consolidation/intake) — the strongest empirical
picks are **H2 fresh relation-recovery** (now doubly-motivated: the s191 v2 left the lexical pole's
shadow-saturated corner **unplaced** and named this probe as its revision trigger) or **H1 adjective-antonymy
replication** (each needs a design + decision), or the **A3b BLiMP sweep**; the strongest consolidation pick is
the **`shadow-depth-table-v1` v2** (the one remaining theory-edition owed). Do NOT: re-edit the superseded
`lexicon-grammar-continuum` v1 or re-open the antonymy corner as if the prior-art placement stood;
re-catalogue the workspace paper or re-fire its OQ without clearing the essay/design bar; re-run/re-open the
aann-quant-temporal probe or its decision; reopen the campaign; re-fire H2 off the pilot; re-run/re-open A1b;
re-audit the wiki; mass-edit `supported`-at-creation results; flip theory to `live` off a non-substantive
touch; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
