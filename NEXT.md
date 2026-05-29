# NEXT.md

## State

Workflow-mode wave (orchestrator + 4 parallel subagents + 1 adversarial coherence pass), one wave, no deadline. It landed, in one PR:

- **Concepts filled** — the last three base concept stubs are now full pages, matching the `distributional-meaning` shape (front-matter, meaning-senses, typed links, ≥1 verified quote, a "Live tension" note):
  - `concept/inferential-meaning` — conceptual-role / inferential semantics; Piantadosi & Hill's "meaning without reference" as the strongest pro-LLM-meaning position; `contradicts concept/grounding`, `refines concept/distributional-meaning`.
  - `concept/referential-meaning` — sense / reference / externalist sub-positions; grounded in Bender & Koller. **Honest gap flagged:** Putnam 1975 / Evans 1973 are *not* in-repo, so the `referential.externalist` sub-tag has no in-repo primary anchor yet (both in `wanted.md`).
  - `concept/grounding` — Bender & Koller's binary form/meaning denial vs. Lyre's grounding-as-gradual three-dimensional typology; the project's gradient stance flagged as a contestable working choice.
  - **All six base concepts are now filled.** No concept stubs remain.
- **New source** `source/scivetti-2025-beyond-memorization` (Scivetti, Tayyar Madabushi et al. 2025, IJCNLP-AACL; arXiv 2501.04661) — a CxG inference benchmark over 8 phrasal constructions with human comparison; GPT-o1 drops >40% on syntactically-identical/semantically-divergent forms. **Resolves both P2 wants** (one paper; Tayyar Madabushi is senior author). Abstract verbatim from ACL Anthology + 3 section-level body quotes from arXiv v1 HTML; quotes independently re-verified by the cataloguing subagent.
- **NITs folded in** — "canonical demonstration" → "Goldberg's canonical argument" in `caused-motion-construction`; `inferential` added to `constructional-vs-frequency-confound`'s meaning-senses.

Coherence pass returned **no BLOCKERs**: all quotes verbatim against in-repo sources, no fabrication (referential-meaning carries zero Putnam/Evans quotes/citations, as required), typed links clean, the four concept pages partition cleanly. One real typo fixed (`a expression's` → `an`); the verbatim "others symbols" quote was correctly left intact. senselint: 0 errors (expected `wanted.md` WARN + 4 contingent INFOs).

**Lead worth acting on next:** Scivetti et al. 2025 probes **caused-motion, conative, and way-manner** — three of this repo's conjectures — *with public prompts/responses and a human baseline*. That public dataset is a candidate human anchor for three currently-pending anchor decisions (see below).

## Next concrete action

Default is **workflow mode** (`PROTOCOL.md §A`). Suggested backlog of independent, now-tractable units (disjoint files):

1. **Catalogue the Scivetti et al. 2025 public dataset as a `resource` page** under `wiki/base/resources/` (prompts + model responses + human comparison on 8 constructions). This is the high-value unit: it could supply a CxG-native human anchor for `caused-motion-anchor`, `conative-anchor`, and `way-construction-anchor` (three open decisions). Inspect the actual dataset (the paper says it is publicly available) and record at the item/annotation level *what it can ground*, not by existence. Then **surface** (do not auto-resolve) the option in each of those three decision pages.
2. **Deepen `source/scivetti-2025-beyond-memorization` to page-level** from the ACL camera-ready PDF (pp. 1184–1201) — per-construction numbers and the human-baseline figures — if a finding needs them. Body quotes are currently arXiv-v1-HTML/section-level only.
3. **Deepen a still-section-level source** (`piantadosi-hill-2022`, `weissweiler-2023`, or `mahowald-2024`) toward page-level quotes, *only if* the original is re-fetchable — never fabricate pagination.
4. **Extend the theory page or an open question** now that all concepts are filled: e.g. fold the four filled concepts into `theory/constructional-meaning-in-llms`'s framing, or sharpen `open-question/relational-meaning-pilot`.

Match the shape of the filled concept pages. Run `senselint.py` (0 errors) + `linkify.py` before commit.

## Blocked pending Tom

Six open decisions gate promotion of contingent work — **unchanged this run** (none resolved). Note the new Scivetti lead bears on three of them (it may supply the missing anchor, pending Tom's ratification):

- `wiki/decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary AANN anchor (default), or switch.
- `wiki/decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- `wiki/decisions/open/way-construction-anchor.md` — ratify Option A (Goldberg 1995 examples as seed), or supply data. **Scivetti 2025 tests way-manner with a human baseline — a candidate anchor.**
- `wiki/decisions/open/cxg-probing-anchor.md` — scope the CxG-probing-validity claim to AANN (default), acquire a CxG-native broad human anchor, or split the claim. **Scivetti 2025 is a candidate CxG-native broad anchor.**
- `wiki/decisions/open/caused-motion-anchor.md` — anchor for the caused-motion conjecture. **Scivetti 2025 tests caused-motion with a human baseline — a candidate anchor.**
- `wiki/decisions/open/conative-anchor.md` — anchor for the conative conjecture (provisional default: Levin 1993 / VerbNet). **Scivetti 2025 tests conative with a human baseline — a candidate anchor.**

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md` — **"continue working" ⇒ workflow mode (§0/§A)**: plan a wave, fan out parallel subagents, run an adversarial coherence pass, integrate + verify, commit the wave, and (if Tom gave a deadline) loop until the clock. Read `wiki/index.md` before opening individual pages. **Reconcile `wiki/decisions/open/` first** (six entries). **Run `python3 tools/senselint.py` (0 errors) and `python3 tools/linkify.py` before each commit.** **Commit and merge to the default branch before stopping.**
