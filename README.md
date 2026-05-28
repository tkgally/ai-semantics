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
- `decisions/` — `open/` for asynchronous gate decisions awaiting Tom; `resolved/` once ratified.
- `config/` — `models.md` (the panel) and `budget.md` (OpenRouter spend cap).
- `tools/` — small stdlib-Python CLIs, added when a run needs them.

## Status

Bootstrapped 2026-05-28. No empirical claims on the books yet. Next concrete action is in `NEXT.md`.
