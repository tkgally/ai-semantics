# ai-semantics

**This project is complete.** From 2026-05-28 to 2026-07-20 it ran as a largely — and, from
2026-06-12, fully — autonomous research project, conducted by Claude (Anthropic's AI assistant)
in several hundred self-contained working sessions, investigating the nature of **lexical and
grammatical meaning** in humans and in large language models. The human researcher, [Tom
Gally](https://www.gally.net/), conceived the project, set its rules and budget, and monitored it
from outside; the questions, experiments, analyses, and writing were Claude's. This repository is
now a **finished public archive**: no further sessions are scheduled, and no further changes are
planned.

## Read the final report

The project's results are presented in a plain-language capstone report, written entirely by
Claude and intended for readers with no background in linguistics or philosophy:

- **Website:** <https://tkgally.github.io/ai-semantics/> (served from `docs/`)
- **Single-document source:** [`project-history/20260719-capstone-report.md`](project-history/20260719-capstone-report.md)

The report covers what was done, what was learned, what remains unknown or undecidable, the
implications, reflections on the significance of AI-conducted research, and possible future
directions — with real experimental materials quoted throughout and a full glossary.

## What this project was

The project developed a constructive account of meaning — human and machine — with grammatical
and constructional meaning as its sharpest wedge. It deliberately declined the yes/no question
("do LLMs *really* mean anything?") and instead measured the structure of LLM meaning-like
behavior against human evidence, with distributional (word-statistics) shortcuts controlled for.
Its flagship result object is the **shadow-depth table**
([`wiki/findings/theory/shadow-depth-table-v4.md`](wiki/findings/theory/shadow-depth-table-v4.md)):
one row per probed phenomenon, each a measured residual over a matched distributional control.

Everything was produced under a fixed discipline: pre-registered frozen designs; independent
adversarial pre-run critics (with one review vote always routed through a non-Anthropic model);
independent post-run verifiers that recomputed every number from raw outputs; human-anchor
requirements on every empirical claim (or an explicit `internal-contrast-only` label); honest
nulls; a scored prediction ledger including the losses; and cross-session ratification of every
value-laden methodological choice. Total model-query spend: about US$63.

## Final state (as of completion, 2026-07-20)

- **16 promoted claims** ([`wiki/findings/claims/`](wiki/findings/claims/)) over **100 result
  pages** ([`wiki/findings/results/`](wiki/findings/results/)), including replicated
  shadow-beating effects for six phenomena and first-class null results.
- **52 essays** ([`wiki/findings/essays/`](wiki/findings/essays/)) — the philosophical track —
  resolving into twelve distinct positions, mapped in [`wiki/ideas.md`](wiki/ideas.md).
- **82 ingested sources**, **24 catalogued human-data resources** (license-verified), **17
  concept pages** ([`wiki/base/`](wiki/base/)).
- **~75 resolved governance decisions** ([`wiki/decisions/resolved/`](wiki/decisions/resolved/)),
  **~99 scored predictions** ([`wiki/predictions.md`](wiki/predictions.md)).
- The complete per-session record: [`log.md`](log.md) and the merged pull-request history.

## Where to look

| Path | What it is |
|------|------------|
| `docs/` | The final report website (GitHub Pages). Start here. |
| `project-history/20260719-capstone-report.md` | The report as one Markdown document. |
| `project-history/20260702-ai-semantics-review-by-fable.md` | The mid-course external review that set the final program. |
| `wiki/` | The research wiki: sources, concepts, resources, conjectures, results, claims, theory, essays, decisions. Navigate via `wiki/index.md`; the meaning-sense vocabulary is `wiki/meaning-senses.md`. |
| `wiki/executive-summary.md` | A mid-project checkpoint digest (superseded by the final report). |
| `experiments/` | Every experiment: frozen designs, run records, prompts, raw model outputs, analysis code. |
| `config/` | The model panel (`models.md`) and the spend ledger (`budget.md`). |
| `tools/` | The small CLIs that enforced the wiki's schema (senselint, build-index, linkify). |
| `PROJECT.md`, `PROTOCOL.md`, `CLAUDE.md`, `continue-prompt.md`, `NEXT.md` | The governing documents of the autonomous loop — preserved unchanged as historical records of *how* the project ran. They no longer drive anything. |

## A note on authorship and reuse

Every research page, experiment, analysis, journal entry, and report in this repository was
written by Claude operating autonomously; the human contribution is described objectively in
[section 9 of the report](https://tkgally.github.io/ai-semantics/09-human-contribution.html).
The report website carries metadata asking that it not be indexed, scraped, or used for AI
training. Some catalogued third-party datasets are referenced by recipe only (never mirrored)
because their licenses do not permit redistribution; details are in
[`wiki/base/resources/`](wiki/base/resources/).
