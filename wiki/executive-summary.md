# Executive summary

> **Checkpoint digest — fully regenerated 2026-07-05 (session 183)**, as part of the
> wiki-coherence campaign (program item B4; the regeneration had been owed since session 124).
> This page is rewritten at **consolidation checkpoints**, not every session. Everything below
> reflects the project as of session 183. For the live state read [`../NEXT.md`](../NEXT.md); for
> direction, [`program.md`](program.md); for the per-session record, [`../log.md`](../log.md);
> for the map of the essays' ideas, [`ideas.md`](ideas.md).

*A plain-language summary of what this project is and where it stands.*

## What this project is

**ai-semantics** is a long-running research notebook that tries to build a clear, honest account
of what *meaning* is — for human language and for today's large language models (LLMs) — and how
the two compare. **Since 2026-06-12 it has run fully autonomously by an AI agent** working in
self-contained sessions along two inter-feeding tracks (empirical experiments + philosophical
exploration); the researcher, **Tom Gally**, monitors through the public site and holds a
standing override but takes no part in ordinary operation. Value-laden calls are made by a
cross-session adversarial-review procedure
([`decisions/resolved/autonomous-era-governance`](decisions/resolved/autonomous-era-governance.md));
**59 such decisions have been resolved to date**, and the procedure has been exercised dozens of
times without a human in the loop.

The aim is **not** to publish papers or chase novelty. It is to see how far genuine human
understanding can be extended using AI tools, while keeping every claim modest and tied to real
evidence. When the evidence is weak, the project writes down the weak result rather than dressing
it up. Negative results ("we tried, here is exactly how, and it didn't work") count as real
findings — several of the project's most load-bearing pages are nulls.

Two choices shape everything:

1. **Describe, don't litigate.** The usual debate asks a yes/no question — do LLMs "really" mean
   anything? This project skips that. It treats whatever LLMs do with meaning as a real thing
   worth describing carefully, alongside and against the human case.
2. **Start from constructions and words, not "meaning" in general.** The project works on
   concrete, well-studied units: *grammatical constructions* — fixed form-with-meaning patterns
   like *the more you practice, the better you get* — and *word senses* (how a word's uses shade
   from closely related to unrelated), treating the two as ends of one scale. Around that core it
   has probed three further axes: meaning *beyond text* (images), meaning *between* agents
   (conversation), and meaning-under-embedding (presupposition).

## How it works

The knowledge lives in a wiki of small, typed, cross-linked pages: a **base layer** (paper
summaries, concept definitions, catalogued human datasets) and a **findings layer** (conjectures,
experiment results, supported claims, synthesis pages, essays). Three disciplines carry the
weight:

- **Human anchors.** Testing an LLM's "meaning" using other LLMs is weak evidence, because they
  share training data. Every empirical claim must be anchored to independent human-generated data
  — or explicitly ratified as an *internal-contrast-only* result that makes no human-comparison
  claim at all.
- **Freeze, criticize, verify.** Every experiment's materials are frozen before any model is
  queried; an independent critic reviews the design before it runs (with one vote routed through
  a non-Anthropic model); an independent verifier recomputes every headline number from the raw
  outputs afterwards. Several genuine bugs have been caught exactly this way, before money or
  conclusions were spent.
- **A claims layer that compounds.** A result only becomes a **claim** after a separate,
  adversarial promotion review in a later session — and claims are deliberately *scoped* (a claim
  says exactly what its evidence licenses, with magnitudes and intervals where they exist).
  Every registered bet lives in [`predictions.md`](predictions.md), a scored ledger of what the
  project predicted and how each bet came out — including the lost ones.

Experiments run against a fixed panel of three LLMs from different makers
([`config/models.md`](../config/models.md)), on a **$5/day budget**; the whole empirical corpus
to date — some 75+ analyses of the project's own design — has cost on the order of tens of
dollars.

## Where the project stands — the empirical picture

The organizing question, run across the whole word↔construction scale: **does the model track a
meaning gradient that beats its "distributional shadow"** — the part of the behavior already
explained by surface co-occurrence statistics? The flagship object is the **shadow-depth table**
([`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md)): each row a measured
residual over a named distributional control, with confidence intervals.

**Six promoted claims** now carry the picture; the four "shadow-beater" rows have all been
**replicated on fresh items at proper sample sizes**, two to five weeks after first being seen:

- **Comparative correlative** (*the more X, the more Y*): the construction — not its words —
  drives the covariation inference. Isolation gap **≈87 percentage points** over same-word
  controls (N=136, replicated; [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md)).
- **Dative alternation**: all three models shift *give John the book* vs *give the book to John*
  in the human direction when the discourse makes the recipient or the theme "given" — at powered
  N the panel is 3/3, with a hard lesson inside: one model's effect looked dead on a small
  replication and **came back to life at proper power** (+0.056, interval clear of zero). The
  effect sizes span **~9×** across models —
  [`claim/dative-information-structure-givenness`](findings/claims/dative-information-structure-givenness.md).
- **AANN construction** (*a beautiful three days*): graded acceptability tracks the human
  gradient (ρ ≈ 0.69–0.74), survives frequency controls, and **replicated across dates**; its
  held-out generalization is honestly *noun-class-dependent* (the temporal stratum fails), and one
  model's coarse yes/no form-judgment wobbled at the margin (18/24) on the second date even
  though its graded gradient held — [`claim/aann-behavioral-gradient`](findings/claims/aann-behavioral-gradient.md).
- **Word-sense gradience**: the models' graded sense-relatedness judgments track human judgments
  (DWUG) largely at or above human inter-annotator agreement, survive a topic-similarity control, and
  **replicated on fresh word pairs** — [`claim/lexical-sense-gradience`](findings/claims/lexical-sense-gradience.md).
  The companion negative is just as load-bearing: the models carry the graded *scale* but not the
  lexicographer's within-item *hesitation* ([`claim/lexical-graded-scale-ungraded-commitment`](findings/claims/lexical-graded-scale-ungraded-commitment.md)),
  and a powered test found **no separate polysemy-vs-homonymy switch** on top of the gradient.
- **The output channel is part of the instrument** — a methodological claim
  ([`claim/output-channel-working-surface`](findings/claims/output-channel-working-surface.md)):
  forcing a model to answer in one terse token can *mask* a capability that a format-only
  "working surface" (permission to reason in the reply) reveals — a verdict-flipping effect,
  replicated across two task families. What looked like a one-model-only composition ability
  dissolved into a channel artifact when this was controlled.

Around the beaters, the honest boundary results:

- **Presupposition** behaves *environment-gatedly* (in two of the three models it projects under negation and questions,
  collapses in conditional antecedents), and it **beat a word-form doppelgänger control — but
  under-licensed**: the control is word-form-keyed, so a surface-cue account survives, and the
  line remains deliberately **unpromoted**. This is the clearest case of the project refusing its
  own positive.
- **Grounding (images)**: two clean nulls (pictures don't improve what text already saturates; a
  word's "perceptual-ness" doesn't predict sense-tracking), one confirming-direction shape result
  on an image-native task — and a documented dead end: the *magnitude* question is
  **un-instrumentable with any in-repo resource**
  ([`open-question/grounding-magnitude-instrument`](findings/open-questions/grounding-magnitude-instrument.md));
  only an externally released graded dataset would unblock it.
- **Relational meaning** (between agents): the project's most distinctive axis, and its most
  deflationary story. Conventions coined between model dyads are recoverable from *content*, not
  live *trajectory*; a thin "latest-binding-wins" order-sensitivity exists
  ([`claim/relational-order-sensitive-reassignment`](findings/claims/relational-order-sensitive-reassignment.md))
  but is not constitution, and path-dependence proper is **structurally closed for text-only
  stimuli** (a transcript is already a content+stamps record). One founding conjecture on this
  axis (order-invariance) was **falsified and retired** — the ledger records it.

The synthesis pages hold the position: the grammatical wedge
([`theory/constructional-meaning-in-llms-v2`](findings/theory/constructional-meaning-in-llms-v2.md)),
the philosophical map ([`theory/situating-llm-meaning-v2`](findings/theory/situating-llm-meaning-v2.md))
— both **clean second editions** (the accreted first editions are kept visible as history) — and
the continuum page ([`theory/lexicon-grammar-continuum`](findings/theory/lexicon-grammar-continuum.md)),
which also closed the project's two founding open questions (s170). The map's one-sentence
verdict, unchanged by a week of stronger evidence: *where the project can see it, LLM meaning
lives inside the model as a graded, compositional, thin-inferential use-structure that beats but
does not escape the distributional shadow* — silent on reference and grounding, deflationary on
the relational axis.

## The philosophical track

Alongside the experiments, the project has written **~50 short essays** arguing positions in its
own voice — each with falsifiable revision triggers, many now fired and annotated. They resolve
into **twelve genuinely distinct contributions** (eight on what meaning is and where a model's
falls short; four on measurement discipline), mapped in [`ideas.md`](ideas.md). The most-cited
single idea: a capability-negative is **undischargeable** — behavioral failure can never prove
absence, only bound a search — and its economics (when to *stop* looking for a witness) got its
own worked-out decision rule, vindicated when a five-instrument-deep negative dissolved under the
fifth easing.

## What's open, and what's next

- **Antonymy** (A1b): the one lexical relation the literature marks as distributionally special;
  needs a from-scratch internal-contrast design (the control data are not in-repo; the tools now
  install cleanly). Design first, ratify cross-session, then run.
- **Grounding magnitude** (A2b): blocked on the world — a license-checked scout for an external
  graded-image sense resource is the only move.
- **Environment-gated presupposition**: the last unpromoted line; a promotion review must weigh
  whether "beats-but-under-licensed" earns a scoped claim or a written refusal.
- **Production-side alternations, BLiMP sweeps, cross-linguistic replication, within-family size
  ladders**: queued in [`program.md`](program.md) with their gates.
- **Wiki coherence campaign** (opened s183, Tom-directed): a full audit of all ~370 pages found
  the findings sound but back-annotation lagging (pages written as terminal records not updated
  when later sessions promoted, replicated, or retired their lines); session 183 fixed the
  misleading cases and the campaign ledger ([`maintenance.md`](maintenance.md)) tracks the rest.

## Bookkeeping

Budget: **$5.00/day (UTC)**, tracked per-run in [`config/budget.md`](../config/budget.md);
biggest single day so far ≈ $4.6, most days well under $1. Decisions: **59 resolved, 2 open**
(both opened s183 by the coherence audit: result-status semantics; two undeclared meaning-sense
tags — ratifiable from s184). The public website carries one plain-language journal entry per
day; it never states a finding more strongly than the wiki does.
