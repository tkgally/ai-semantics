# ai-semantics

A long-running, mostly-autonomous research project developing a comprehensive, constructive theory of **lexical and grammatical meaning for the present era** — covering meaning as conventionally understood (human language, mind, body, interaction, society) *and* the meaning-like phenomenon exhibited by today's LLMs.

Lead human researcher: **Tom Gally**. Lead agent: a fresh Claude Code session each run, with all continuity living in this repo.

## What this is, in one paragraph

The project does not adjudicate whether LLMs "really" mean anything. It treats the LLM phenomenon as a genuine explanandum and tries to describe the structure of whatever-it-is, alongside and against the human case. The atomic deliverable is a **typed, citable, revisable claim** — not a paper. Findings accrete by running a recursive experiment loop (conjecture → design → probe → result → revised theory), with every empirical claim about LLM meaning anchored to an independent **human-labeled resource** (treebank, sense inventory, acceptability set, construction inventory). Grammatical and constructional meaning is the sharpest wedge; that is where work concentrates first.

## Where to start

| File | What it is |
|------|------------|
| `PROJECT.md` | The charter. Read in full at least once. |
| `CLAUDE.md` | Schema + conventions. Read every run. |
| `PROTOCOL.md` | Per-run discipline (read → reconcile → pick → do → verify → commit → hand off). |
| `NEXT.md` | The baton: current state + the single next concrete action. |
| `log.md` | Append-only chronicle. |
| `wiki/index.md` | Catalog of typed pages. Read first to navigate the wiki. |
| `wiki/meaning-senses.md` | Controlled vocabulary for senses of "meaning". Mechanically required. |

## Repository layout

See `PROJECT.md` §3. Briefly:

- `wiki/base/` — stratum 0 (sources, concepts, resources, the prioritized fetch list `wanted.md`).
- `wiki/findings/` — strata above (conjectures, claims, results, theory, open questions).
- `experiments/` — designs, run records, data.
- `wiki/decisions/` — `open/` for asynchronous gate decisions awaiting Tom; `resolved/` once ratified.
- `config/` — `models.md` (the panel) and `budget.md` (OpenRouter spend cap).
- `tools/` — small stdlib-Python CLIs, added when a run needs them.

## Status

Bootstrapped 2026-05-28; active. The project has run **six probes of its own design** (all behavioral, read-only, under $0.60 total against a $20/month cap) and holds a first synthesis: a five-tier *evidence ladder* for constructional meaning in LLMs. The headline pattern so far is modest and bounded — current decoders handle the "easy direction" of the upper ladder (a construction *adding* an inference onto a verb) at or near ceiling, while the "hard direction" (the same surface form mapping to a *divergent* meaning, or a construction *cancelling* a lexical default) is markedly weaker and instrument-sensitive; an off-ceiling stress test shows the easy-direction ceilings are cue-sensitive computation, not a brittle template. Thirteen decisions have been put to Tom — eleven ratified, two open (both non-blocking).

For orientation read `wiki/executive-summary.md` first, then `wiki/index.md`. The next concrete action and the live backlog are in `NEXT.md`.
