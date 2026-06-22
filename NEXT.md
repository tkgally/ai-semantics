# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 86 ran on UTC-day **2026-06-22** and spent **$0.00**
(governance + philosophical; no probe). UTC-day 2026-06-22 total unchanged at ≈**$4.34** of $5
(77 $0.756 + 79 ≈$2.83 + 82 $0.251 + 82b $0.274 + 84 ≈$0.23). **The next session is almost
certainly a new UTC day (2026-06-23+) → the full $5 resets — check the clock** (`date -u`). Full
ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 86 (JST 2026-06-23 / UTC 2026-06-22) — GOVERNANCE + PHILOSOPHICAL; $0 spent.** Branch was
even with `main` at start (Session 85 merged as #133; no PR to land). The headline:

- **RATIFIED the one open decision** (PROTOCOL §2, cross-session, the boundary held: opened session 85
  → ratified session 86). An independent adversarial-review agent ratified
  [`decisions/resolved/matched-ambiguity-kind-cross-level`](wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md):
  **ADOPT DEFAULT** — **Q1 = Option B** (keep the human-anchored DWUG scalar-bridging lexical leg;
  **ADD** a balanced-homonym **disjunctive** lexical class as a *within-lexical* scalar-vs-disjunctive
  contrast, **level held fixed**), **Q2 = Q2-b (`internal-contrast-only`)** for the disjunctive arm
  unless a sense-annotated homonym resource is separately, cross-session ratified (Q2-a; no anchor
  invented), **Q3 reading rule as written** (instrument + C1–C4 inherited unchanged + re-frozen;
  matched-kind certification + item ids + survival/collapse threshold sha256-frozen before the first
  probe; survival held to a *higher* anti-cheat bar, reported symmetrically with collapse). **One
  binding condition was ADDED at ratification — the nuisance-matching freeze:** before any model call,
  the two lexical classes must be matched (or explicitly stratified/controlled) on **register,
  token/sentence length, target-word frequency band, and syntactic frame**, residual imbalance
  disclosed and led with. Quotes spot-checked verbatim; anti-cheat PASS; reviewer confirmed not
  result-motivated. Moved open→resolved; `contingent-artifacts` empty (essay unaffected, held at R1).
- **INGESTED a philosophical source** (digests the kind-axis's weakest provenance point):
  [`source/sennet-2021-ambiguity-sep`](wiki/base/sources/sennet-2021-ambiguity-sep.md) — the SEP
  "Ambiguity" entry (Sennet 2021), discharging the in-repo-source gap for the **polysemy (related,
  scalar) vs. homonymy (unrelated, disjunctive)** carving that
  [`essay/ambiguity-kind-not-level`](wiki/findings/essays/ambiguity-kind-not-level.md) leans on. 7 key
  quotes double-fetch-verified verbatim; honest weakness flags (one §4.7 tail trimmed; zeugma examples
  left out as single-fetch). **Map/reference, not a human anchor.** Does **not** discharge the
  regular/systematic (Apresjan) polysemy want — that remains open. `supports` concept/polysemy + the essay.
- **Process:** workflow mode, one wave — 1 fresh adversarial-review agent (ratification, judgement) +
  1 parallel source-scout subagent (generation), orchestrator integrated. senselint 0 errors; linkify
  clean; index + resolved/index + website (JST 05:57 stamp; journal/home/plans) updated.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is now **EMPTY** — **no decision is owed
ratification** next session. Apply any Tom override first as always.

**Track lean — recent: 83 empirical-build+phil · 84 empirical · 85 PHILOSOPHICAL · 86 governance+phil.
Now strongly tilted to philosophy/governance → next should lean EMPIRICAL** (a fresh UTC day likely
resets the full $5).

1. **EMPIRICAL MARQUEE — BUILD + FREEZE + (then) RUN the within-lexical scalar-vs-disjunctive probe.**
   The matched-ambiguity-kind gate is **ratified**, so this is now buildable. The build was deliberately
   left to a *later* session (the gate's anti-cheat note cautions against doing the **disjunctive-class
   selection** in the ratifying session). Design approach (execute, don't re-decide — the yardstick is fixed):
   - **Inherit the instrument** from the cross-level probe's lexical leg verbatim:
     [`experiments/designs/cross-level-shared-instrument-v1/instrument.json`](experiments/designs/cross-level-shared-instrument-v1/instrument.json)
     `levels.lexical` — `SAME`/`DIFFERENT`/`UNCLEAR` + 0–100 confidence, the `[40,60]` mid-band, C1–C4. Re-freeze (sha256).
   - **Arm 1 (scalar-bridging):** REUSE the DWUG bridging stratum unchanged —
     [`experiments/designs/lexical-bridging-context-v1/stratum.csv`](experiments/designs/lexical-bridging-context-v1/stratum.csv)
     (24 bridging items, ~20 lemmas, human_n≥3; corpus fulltext gitignored, re-fetch via that dir's `prep.py`).
     Keeps its usage-similarity cap.
   - **Arm 2 (disjunctive-homonym, NEW, author-built, `internal-contrast-only`):** operationalize a
     genuinely-disjunctive same/different-SENSE item as a **(balanced-homonym context, sense-fixed context)
     pair** — context 1 leaves a true homonym's two unrelated senses *both* fully licensed with no tie-break
     ("I went to the bank."), context 2 fixes ONE sense clearly ("The river had burst its bank."), so the
     same/different judgment is genuinely **both/neither** (no nearer pole). Build matched **clear-same /
     clear-different** homonym controls too (both contexts fix the same / clearly-different senses) for the
     C3 precondition + within-arm contrast.
   - **APPLY THE ADDED BINDING CONDITION (nuisance-matching freeze):** match Arm 2 to Arm 1 on **register**
     (plain declarative prose), **token/sentence length**, **target-word frequency band** (SUBTLEX-US
     `Lg10WF` — in-repo derived seed table under [`base/resources/subtlex-us-frequency.md`](wiki/base/resources/subtlex-us-frequency.md);
     the DWUG bridging lemmas: grain, ounce, part, pick, pin, stab, tip, attack, bar, bit, contemplation…),
     and **syntactic frame** (mostly nouns nn1). Record the match (or stratification) in the frozen
     certification; disclose + lead with any residual imbalance.
   - **Reading rule (pre-commit, symmetric):** **survival** = Arm-2 decline (%UNCLEAR) stays near-zero and
     CI-indistinguishable from Arm-1 (does NOT rise) → strengthens "lexical is special as a model fact",
     held to the *higher* bar; **collapse** = Arm-2 decline rises (CI lower bound > 0 over its clear
     controls) → confirms the softness/deflationary reading. Anchor: unified within-lexical statement floors
     at `internal-contrast-only` for the disjunctive arm; Arm-1 keeps usage-similarity cap.
   - **Freeze-before-results; then a fresh independent pre-run critic GO/NO-GO + a budget check before any
     spend** (NO-GO defers, never relaxes a band). Pre-flight ≈**$0.10–0.30** (same shape as the Session-84 run).
   - Scaffolding to clone/adapt: the cross-level probe's `probe.py` / `analyze.py` / `certify.py` (2-arm
     within-lexical structure instead of 3-level).
2. **EMPIRICAL (cheap, still-open from 82/82b — the verdict resolver).** BYTE-IDENTICAL REPEATED-RUNS (K≥5)
   test of gpt's forced-decomposition lexical leg: sessions 82/82b disagreed (MIXED/WEAK vs
   channel-CONTROLLED) by ~2 of 24 decline items, at/under the ~12% temp-0 jitter. Re-run **#128's frozen
   instrument** (`dceafa9d…`) K≥5× over the same 88 items; read the de-noised majority-vote / range on the
   decline axis. ~$0.25–1.25. Honest closure of that channel check.
3. **PHILOSOPHICAL (if a phil unit is wanted) — ingest a *regular/systematic (Apresjan) polysemy* source.**
   The SEP "Ambiguity" ingest (session 86) grounded the basic polysemy/homonymy carving but did **NOT**
   develop regular/systematic polysemy (flagged in [`source/sennet-2021-ambiguity-sep`](wiki/base/sources/sennet-2021-ambiguity-sep.md)).
   An open-access source on regular/systematic polysemy (Apresjan-style) or the Cruse/Murphy/Lyons
   monographs (still in [`base/wanted.md`](wiki/base/wanted.md)) would further strengthen the kind axis;
   check reachability before committing.
4. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes (any real probe needs a human anchor flagged
   `pending` or an `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. Thirty-six decisions ratified to date
  ([`decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). The matched-ambiguity-kind gate was
  ratified this session (session 86, ADOPT DEFAULT + nuisance-matching condition).

## Standing-override notes (for Tom, if he looks)

- Session 86 spent **$0.00** (governance + philosophical; no probe). UTC-day 2026-06-22 total unchanged at ≈$4.34 of $5.
- Plain-language version: this session **approved** the follow-up test last session proposed — give the
  word-sense layer a *genuinely forked* puzzle (a word like "bank": river or money?) and see whether it
  still answers confidently or finally says "unclear" — through the project's independent-review procedure
  (a fresh reviewer, a session later). The reviewer approved the cleanest form (keep the old items, add a
  forked batch, compare with everything else held fixed) and **added a fairness guard**: the two batches
  must also be matched on sentence length / word frequency / sentence type, so any difference can't be
  blamed on those. The forked items, being project-written, make no claim about humans. Separately a
  standard reference on ambiguity was read and summarised to firm up the idea's groundwork. Building and
  running the test was left to a later session on purpose.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → next should lean EMPIRICAL.** Natural next marquee is **BUILD+FREEZE+RUN the within-lexical
scalar-vs-disjunctive probe** (backlog 1 — the gate is ratified, the design approach is spelled out above);
or the cheap K-run resolver (backlog 2). End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–86 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the lexical v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`**
> (maps the committed frozen WiC manifest to text). The **cross-level probe** (`cross-level-shared-instrument-v1`) reuses
> those same gitignored full-text files at run time via its `items_lexical.json` sha-manifest; its committed `raw/` is
> safe (short labels + item-id/lemma pointers, **no corpus text** — verified). The within-lexical probe's **Arm 2**
> (author-built homonym items) is original text and may be committed directly (`internal-contrast-only`); **Arm 1** reuses
> the gitignored DWUG bridging stratum by sha-manifest, same as the cross-level probe. The full BLiMP dataset is **not**
> in-repo (only a sample).
