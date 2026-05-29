# NEXT.md

## State

This session was an **experimental dynamic-workflow burst** (orchestrator + six parallel subagents + one adversarial coherence pass), run with Tom's explicit authorization to depart from the one-bounded-unit-per-run discipline of `PROTOCOL.md` and to observe coherence/token behavior. It landed, in one PR (#9):

- **Claim** `cxg-probing-surprisal-validity` (proposed) — surprisal contrast on form–meaning minimal pairs as a valid-but-bounded operationalization of constructional-meaning *sensitivity*; `anchor: pending`, contingent on `cxg-probing-anchor`.
- **Theory** `constructional-meaning-in-llms` (draft) — the project's first `theory` page: a five-tier evidence ladder placing every existing claim/conjecture.
- **Conjectures** `caused-motion-construction`, `conative-construction` (both proposed; anchors pending).
- **Open-questions** `constructional-vs-frequency-confound` (form-level), `distributional-vs-inferential-constructional` (meaning-level, downstream).
- **Concepts filled** `distributional-meaning`, `constructional-meaning`, `formal-vs-functional-competence`.
- **Sources deepened** Mahowald 2024 (+7 quotes), Piantadosi & Hill 2022 (+5), Bender & Koller 2020 (abstract); all five P1 sources `received`.
- **Tooling** `tools/senselint.py` + README — mechanizes the PROTOCOL §5 gates. **Current run: 0 errors, 1 benign warn (`wanted.md` has no front-matter), 4 expected contingent-page info notes.**

A coherence sweep confirmed no duplication (the four argument-structure conjectures partition cleanly) and no contradictions; all link-relation/quote-integrity defects it found were fixed in-session.

A follow-up maintenance pass (same PR) made the wiki **clickable** (`tools/linkify.py`; 120 relative links; senselint check 7 guards them) and rewrote `PROTOCOL.md` / `CLAUDE.md` so that **"continue working on the project" now defaults to workflow mode** (see `PROTOCOL.md §0`/`§A`).

## Next concrete action

Default mode for the next run is **workflow mode** (`PROTOCOL.md §A`). Fan out this backlog of independent, anchor-tractable units (disjoint files; orchestrator integrates the shared files):

1. **Fill `concept/inferential-meaning`** — now load-bearing: both new conjectures and one open-question `depends-on` it, yet it is still a stub. Ground in `source/piantadosi-hill-2022-meaning-without-reference` (carries verbatim conceptual-role quotes) and the `inferential` entry in `wiki/meaning-senses.md`.
2. **Fill `concept/referential-meaning`** — ground in the `referential` sense (Frege/Putnam) and Bender & Koller's reference discussion; note the externalist sub-tags.
3. **Fill `concept/grounding`** — ground in `source/lyre-2024-semantic-grounding` (gradual, three-dimensional) and `source/bender-koller-2020-climbing` (the strong form/meaning denial).
4. **Deepen a source** still at abstract/section level toward page-level quotes, or catalogue a new P2 source (Tayyar Madabushi / Scivetti constructional probing) if OA-fetchable.

Match the shape of the three concept pages filled this run (front-matter, ≥1 meaning-sense, typed links, ≥1 verified quote, a "live tension" note). Run `senselint.py` + `linkify.py` before commit.

Smaller queued NITs from the coherence sweep (fold into any wave): hedge "canonical demonstration" → "Goldberg's canonical argument" in `caused-motion-construction.md`; consider adding `inferential` to `constructional-vs-frequency-confound`'s meaning-senses.

## Blocked pending Tom

Six open decisions now gate promotion of contingent work. The three new ones came from this session:

- `wiki/decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary AANN anchor (default), or switch.
- `wiki/decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- `wiki/decisions/open/way-construction-anchor.md` — ratify Option A (Goldberg 1995 examples as seed), or supply data.
- `wiki/decisions/open/cxg-probing-anchor.md` — **new.** Scope the CxG-probing-validity claim to AANN (default), acquire a CxG-native broad human anchor, or split the claim.
- `wiki/decisions/open/caused-motion-anchor.md` — **new.** Anchor for the caused-motion conjecture.
- `wiki/decisions/open/conative-anchor.md` — **new.** Anchor for the conative conjecture (provisional default: Levin 1993 / VerbNet conative-class membership as partial anchor).

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md` — **"continue working" ⇒ workflow mode (§0/§A)**: plan a wave, fan out parallel subagents, run an adversarial coherence pass, integrate + verify, commit the wave, and (if Tom gave a deadline) loop until the clock. Read `wiki/index.md` before opening individual pages. **Reconcile `wiki/decisions/open/` first** (six entries now). **Run `python3 tools/senselint.py` (0 errors) and `python3 tools/linkify.py` before each commit.** **Commit and merge to the default branch before stopping.**
