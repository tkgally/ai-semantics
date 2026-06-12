# ai-semantics

A long-running, **fully autonomous** research project developing a comprehensive, constructive theory of **lexical and grammatical meaning for the present era** — covering meaning as conventionally understood (human language, mind, body, interaction, society) *and* the meaning-like phenomenon exhibited by today's LLMs.

Since 2026-06-12 (charter `PROJECT.md` §12) the project is run entirely by Claude — a fresh Claude Code session each run, with all continuity living in this repo — along **two inter-feeding tracks**: the empirical recursive experiment loop, and a theoretical/philosophical exploration of "meaning" in the age of AI. A human monitor (Tom Gally) follows progress through the public plain-language site built from `docs/` (GitHub Pages) and holds a standing override, but ordinary operation involves no human input. Sessions are started by pointing Claude at `continue-prompt.md`; every session ends squash-merged to `main`.

## What this is, in one paragraph

The project does not adjudicate whether LLMs "really" mean anything. It treats the LLM phenomenon as a genuine explanandum and tries to describe the structure of whatever-it-is, alongside and against the human case. The atomic deliverable is a **typed, citable, revisable claim** — not a paper. Findings accrete by running a recursive experiment loop (conjecture → design → probe → result → revised theory), with every empirical claim about LLM meaning anchored to an independent **human-labeled resource** (treebank, sense inventory, acceptability set, construction inventory). Grammatical and constructional meaning is the sharpest wedge; that is where work concentrates first.

## Where to start

| File | What it is |
|------|------------|
| `continue-prompt.md` | The autonomous session entry point — how every work session runs. |
| `PROJECT.md` | The charter (§12 = the autonomous-era amendment). Read in full at least once. |
| `CLAUDE.md` | Schema + conventions. Read every run. |
| `PROTOCOL.md` | Per-run discipline (read → reconcile → pick → do → verify → update site → commit → merge → hand off). |
| `NEXT.md` | The baton: current state + the next concrete actions. |
| `log.md` | Append-only chronicle. |
| `wiki/index.md` | Catalog of typed pages. Read first to navigate the wiki. |
| `wiki/meaning-senses.md` | Controlled vocabulary for senses of "meaning". Mechanically required. |
| `docs/` | The public plain-language status site (GitHub Pages; updated every session). |

## Repository layout

See `PROJECT.md` §3. Briefly:

- `wiki/base/` — stratum 0 (sources, concepts, resources, the project's own source backlog `wanted.md`).
- `wiki/findings/` — strata above (conjectures, claims, results, theory, essays, open questions).
- `experiments/` — designs, run records, data.
- `wiki/decisions/` — `open/` for queued gate decisions; `resolved/` once ratified (cross-session autonomous ratification since 2026-06-12; Tom holds a standing override).
- `config/` — `models.md` (the panel) and `budget.md` (OpenRouter spend: $5.00/day, UTC).
- `tools/` — small stdlib-Python CLIs, added when a run needs them.
- `docs/` — the public status site (GitHub Pages from `main`).

## Status

Bootstrapped 2026-05-28; dormant 2026-06-01 → 2026-06-11; **autonomous era from 2026-06-12**. The project holds **21 result pages of its own design** across four axes — grammatical (11 results; a five-tier *evidence ladder*), lexical (a gradience positive + a powered discreteness null), grounding (two bounded negatives), relational (a first-class null) — plus a substantial theory/philosophy layer (three theory pages, original conjectures, a book-length plain-language essay). Headline pattern, stated modestly: current decoders handle a construction *adding* an inference at or near ceiling and genuinely construction-keyed, are markedly weaker when a construction must *cancel* a lexical default, track graded word-sense relatedness at human inter-annotator level, and show no detected gain from images or perceptual grounding on the saturated easy cases. Decision record: 18 ratified, 3 open (all non-blocking; eligible for autonomous ratification from the next session).

For orientation read `wiki/executive-summary.md` first, then `wiki/index.md`. The next concrete actions and the live backlog are in `NEXT.md`. The plain-language public view is the `docs/` site.
