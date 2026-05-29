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

## Next concrete action

**Fill the three remaining `base/concepts/` stubs**, starting with `concept/inferential-meaning` — this is now load-bearing: both new conjectures (`caused-motion-construction`, `conative-construction`) and one open-question `depends-on` it, yet it is still a stub (a latent defect). Then `concept/referential-meaning` and `concept/grounding`.

- Ground `inferential-meaning` in `source/piantadosi-hill-2022-meaning-without-reference` (now carries verbatim conceptual-role quotes) and the `inferential` entry in `wiki/meaning-senses.md`.
- Match the shape of the three concept pages filled this run (front-matter, ≥1 meaning-sense, typed `depends-on`/`refines` links, one verified quote, a "live tension" note).
- Files the next run needs: `wiki/base/concepts/inferential-meaning.md`, `wiki/meaning-senses.md`, `wiki/base/sources/piantadosi-hill-2022-meaning-without-reference.md`, and `tools/senselint.py` (run it before commit).

Smaller queued NITs from the coherence sweep (do alongside if cheap, else leave): hedge "canonical demonstration" → "Goldberg's canonical argument" in `caused-motion-construction.md`; consider adding `inferential` to `constructional-vs-frequency-confound`'s meaning-senses.

## Blocked pending Tom

Six open decisions now gate promotion of contingent work. The three new ones came from this session:

- `decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary AANN anchor (default), or switch.
- `decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- `decisions/open/way-construction-anchor.md` — ratify Option A (Goldberg 1995 examples as seed), or supply data.
- `decisions/open/cxg-probing-anchor.md` — **new.** Scope the CxG-probing-validity claim to AANN (default), acquire a CxG-native broad human anchor, or split the claim.
- `decisions/open/caused-motion-anchor.md` — **new.** Anchor for the caused-motion conjecture.
- `decisions/open/conative-anchor.md` — **new.** Anchor for the conative conjecture (provisional default: Levin 1993 / VerbNet conative-class membership as partial anchor).

Charter-level note for Tom: this run is a deliberate stress test of the dynamic-workflow mode. If the burst pattern is to be repeated, decide whether `PROTOCOL.md` should grow an explicit "workflow run" variant or whether the project stays on one-unit-per-run.

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Reconcile `decisions/open/` first** (six entries now). **Run `python3 tools/senselint.py` before commit** — it now exists. **Commit and merge to the default branch before stopping.**
