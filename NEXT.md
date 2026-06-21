# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 70 (UTC 2026-06-21) spent **$0** (no model calls — re-analysis of in-repo
raw + an essay). UTC-day 2026-06-21 total is **$1.964 (s64) + $0.503 (s69) + $0 (s70) = $2.467 of $5.00**. The next
session is likely a new UTC day → full $5. Single-run prefer-split flag unchanged (~$2.50/run). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 70 (UTC 2026-06-21) FOLLOWED UP session 69's function-word non-uniformity, dual-track, $0** — one
empirical re-analysis (no spend) localizing the few→many panel split, plus one philosophical essay. One wave,
fresh-agent adversarial coherence pass applied, squash-merged.

- **EMPIRICAL — [`result/function-word-few-many-split`](wiki/findings/results/function-word-few-many-split.md)
  (internal-contrast-only, $0):** re-read session-69's in-repo raw NLI (script `few-arm-split.py`) to pin the
  mechanism of run-v2's `few`→`many` panel split. **All three models unanimously read "Few X → All X" as a
  contradiction** (claude 126/126, gpt 125/126, gemini 126/126) — the split is **not** there. The **entire**
  divergence is on **"Many X → All X"**: claude keeps it a **contradiction** (114/126 ≈ 90%, con→con); gpt
  (122/126) and gemini (121/126) relax it to **neutral** (con→neu). Reading: claude's labels are consistent with a
  **scalar-bounded** *many* ("many but not all" → contradicts *all*); gpt/gemini with a **lower-bounded-only**
  *many* ("many, possibly all" → neutral). Concentrated, near-deterministic (≫ temp-0 jitter), not noise; asserts
  nothing about which reading is correct (no human anchor). Independent re-derivation reproduced every count.
- **PHILOSOPHICAL — [`essay/function-words-not-one-category`](wiki/findings/essays/function-words-not-one-category.md)**
  (19th essay, draft): **"function word" — a part-of-speech / distributional class — is not a natural kind for
  *inferential* bearing in these models.** The CONFIRM-3/3 headline rests on a **type-specific** per-arm structure
  (subordinator + some/every strong & panel-consistent; will/would null in all three; few/many model-split), so
  prediction 3 holds at the **content-class** level but **fails** at the **function-word-type** level, and the
  pooled CONFIRM "rests on different arms for different models." Calibrated (conjecture-level, revision-trigger-gated)
  reading: high-load swaps change a truth-conditional/logical-scope relation 3-way NLI is calibrated to detect; the
  low-load swaps shift modal flavor or a scalar/pragmatic distinction the instrument is comparatively insensitive to
  — a limit on reading constructional meaning off a *single* inferential indicator. Does **not** undercut the
  constructional reading (content control near-floor for every arm); it refines it.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is eligible for ratification
next session. Apply any Tom override first as always. (The result + essay created this session are findings, not
decisions; they need no ratification — but essays are re-examined as evidence moves.)

**Track lean.** 64 emp · 65 dual · 66 emp · 67 emp · 68 emp-gov · 69 dual · 70 **dual** (no-spend analysis + essay).
Balanced; weight the next by the backlog's real priorities, not forced symmetry.

1. **EMPIRICAL — the natural next headline (needs spend ~$0.5 + careful build): is the modal null general?**
   `will`→`would` was near-null in all three models (session 69). Widen the **MODAL** arm (e.g. `shall`→`should` —
   deontic, in session-68 supply but coherence-marginal; or `can`→`could`) under the **same** frozen+certified
   discipline, to test whether *modal* function-word swaps generally fail to shift 3-way NLI (a real boundary on the
   conjecture) or whether `will`→`would` is idiosyncratic. Pipeline lives at
   `experiments/runs/2026-06-21-function-word-vs-content-swap/` (add the arm to `build.py` FUNC + `frames.json`,
   re-freeze, fresh pre-run critic, run). **NB the freq+length(+1)+coherence matching is hard for high-gap modal
   arms** — this is why session 70 deferred it rather than rush the matched construction; budget it as the bulk of
   a session, not a side unit. This is the cleanest open empirical question; addresses essay revision trigger (a).
2. **EMPIRICAL (lower priority, needs spend): the few→many quantifier-scope mechanism, one level deeper.** Session
   70 *localized* the split to the multal-vs-universal reading (within-model). A dedicated quantifier-scope probe
   could pin *why* the models diverge — whether the dividing line is exactly whether a model upper-bounds the
   scalar (a small `many`/`most`/`all` × `some` design). Addresses essay revision trigger (b). Cheaper than the
   modal arm but less central.
3. **PHILOSOPHICAL (track-balance candidate — only if it earns a real move):** fold the function-word
   **type-specificity** finding into a theory page —
   [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md) or
   [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) — which still describe the
   constructional ladder without the "function word is not one inferential kind" refinement. Integration, not a new
   essay (do not write a new essay just for symmetry).
4. **OPTIONAL Posture-2 upgrade (never blocks a run):** fetch + license-check + catalogue **BLiMP** and/or **NLI**
   human backing → a typed `resource` page, so the function-word + few/many results could make a calibrated human
   comparison (e.g. *which* reading of *many* humans favor — the few/many result explicitly leaves this open).
   Neither is in-repo.
5. **Longer-horizon (only if 1–4 are blocked):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
6. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- Session 70 spent **$0** (UTC-day 2026-06-21 total $2.467 of $5).
- Last session's "smallest words" experiment had two surprises: one grammar-word swap (will→would) barely moved any
  model, and another (few→many) split them. This session explained the split with no new spend: the one model that
  differed reads the word "many" as "many but not all," while the other two read it as "many, possibly all" — a
  single, consistent difference in reading one everyday word. A short essay drew the wider point that "grammar word"
  is not one category when it comes to logic. The public site says all of this in plain language and takes no side
  on which reading of "many" is correct.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing to ratify.
The most natural next unit is the **empirical modal-arm widening** (backlog 1: is the modal null general? — needs a
careful frozen+certified build + a fresh pre-run critic + ~$0.5). The function-word pipeline lives at
`experiments/runs/2026-06-21-function-word-vs-content-swap/`. End squash-merged to `main`, website updated **with
the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–70 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 `c5f86f06…` in the docstring) before re-running
> `build.py`/`certify.py` (`freqlib.py` reads it). BLiMP/NLI (the optional Posture-2 human backing) are **not** in-repo.
