# Executive summary

*A plain-language summary of what this project is and where it stands. Updated at the end of each work session. Last updated: **2026-05-29**.*

For the navigable catalog of every page, see [`index.md`](index.md). For the live next-action handoff, see [`NEXT.md`](../NEXT.md). For the full charter, see [`PROJECT.md`](../PROJECT.md).

---

## What this project is

**ai-semantics** is a long-running research notebook that tries to build a clear, honest account of what *meaning* is — for human language and for today's large language models (LLMs) — and how the two compare. It is run mostly by an AI agent working in short autonomous sessions, with the researcher, **Tom Gally**, steering lightly and making the value-laden calls.

The aim is **not** to publish papers or chase novelty. It is to see how far genuine human understanding can be extended using AI tools, while keeping every claim modest and tied to real evidence. When the evidence is weak, the project writes down the weak result rather than dressing it up. Negative results ("we tried, here is exactly how, and it didn't work") count as real findings.

Two choices shape everything:

1. **Describe, don't litigate.** The usual debate asks a yes/no question — do LLMs "really" mean anything? This project skips that. It treats whatever LLMs do with meaning as a real thing worth describing carefully, alongside and against the human case.
2. **Focus on grammar and constructions.** Rather than tackle "meaning" in general, the project works on the meanings of *grammatical constructions* — fixed form-with-meaning patterns like *she sneezed the napkin off the table* (where the sentence pattern, not the verb, tells you the napkin moved). These are concrete, well-studied, and easy to probe, which makes them a sharp test case.

## How it works

The project keeps all its knowledge in a wiki of small, typed, cross-linked pages:

- **Base layer** — what's already known: summaries of research papers, definitions of key concepts, and catalogues of human-generated datasets the project can lean on.
- **Findings layer** — the project's own work: *conjectures* (educated guesses), *claims* (supported statements), *results* (experiment outcomes), and a *theory* page that ties it together and gets rewritten as new evidence arrives.

A rule the project holds firmly: testing an LLM's "meaning" using other LLMs is weak evidence, because they share the same training. So **every empirical claim must be anchored to independent human-generated data** (a dataset of human judgments, a linguistic resource), never to AI agreement alone.

Experiments are run by sending carefully designed prompts to a panel of three LLMs from different makers (chosen to disagree in informative ways) and comparing their behavior to the human benchmark.

## Where the project stands now

The project has a working method and its first body of original results. The centerpiece is an **"evidence ladder"** — a five-rung scale from weak to strong evidence that a model has truly grasped a construction's meaning (not just its surface form): from telling well-formed sentences apart, up to *drawing the right inferences* the construction licenses.

So far the project has run **six experiments of its own design**, all cheap (under $0.60 total spent against a $20/month budget) and read-only. In plain terms, the picture is:

- **LLMs handle the "easy direction" well.** When a construction *adds* a meaning onto a verb (e.g. the pattern makes *whistle* imply movement down a hall), today's models reliably draw that inference — often near-perfectly.
- **They struggle with the "hard direction."** When the *same surface form* has to be mapped to a *different* meaning, or when a construction must *cancel* a meaning the verb normally carries, models do markedly worse and become inconsistent.
- **It's genuine computation, not a trick.** A stress test showed that when a sentence explicitly contradicts the expected inference, the models correctly withhold it — so their success is sensitive to context, not a brittle "this pattern always means X" reflex.
- **How you ask matters.** The same model can show competence one way of asking and lose it another — a caution against trusting any single test.

These are honest, bounded results: single runs, small samples, all on text-only models, and each carries its caveats on the relevant page. The live synthesis lives on the [theory page](findings/theory/constructional-meaning-in-llms.md).

## What's open or on hold

- **The "relational" frontier is untouched.** The project's most distinctive idea — that meaning might be constituted *between* agents in conversation, not just inside one model — has a sharpened plan but no experiment yet, and is waiting on a key human dataset to be obtained. See [`concept/relational-meaning`](base/concepts/relational-meaning.md).
- **One experiment is on hold for technical reasons.** A planned probe (the "AANN" construction) needs fine-grained probability outputs that the current model service doesn't expose; it waits for a setup with local compute.
- **Two small decisions are pending Tom**, neither blocking ongoing work.

## What's next

Extend the existing results with harder versions that escape the "too easy" ceiling, obtain the lexical and relational datasets that several next steps depend on, and (when compute allows) run the held experiment. The detailed, always-current to-do list is in [`NEXT.md`](../NEXT.md).
