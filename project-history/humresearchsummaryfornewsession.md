# humresearch — a brief for a new Claude session

This file is context for a **new** conversation Tom is starting with Claude about a different, open-ended research project. It summarizes the **humresearch** project Tom has been working on with Claude (and a panel of other LLMs) over the past few weeks — what it is, how the collaboration actually works, what we’ve learned, and where it has landed. It is offered as *background and provocation*, not as a template; the new project is meant to be genuinely exploratory, so read this for what it might suggest by way of collaborative texture, not for a methodology to imitate.

---

## What humresearch is

humresearch is an experiment in **mostly-autonomous, human-consulted AI research for the humanities and social sciences (H&SS)**. It was inspired by the AutoResearchClaw project (which targets full autonomy in the natural sciences) but redesigned around a different commitment: the human researcher must remain **accountable** — able to understand, explain, and defend the research as their own — even when AI does most of the work. Tom is the researcher; Claude (Claude Code, currently running on Opus 4.7) is the lead agent; a rotating panel of other LLMs (via OpenRouter — GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro) provides decorrelated critique.

The project has two parts that grew up together:

1. A **knowledge wiki** (`wiki/`) — a persistent, compounding knowledge base on H&SS research methods, traditional and AI-assisted. 76 mature pages across `methods/`, `concepts/`, `ai-research/`, `fields/`, `sources/`. Methods-centric, with strong weight on the AI-assisted angle, because that is the novel contribution.
2. A **research framework** (`framework/`) — a fresh, ARC-inspired H&SS pipeline expressed as markdown stage specs + Claude Code skills + small stdlib Python tools. Ten phases (research planning → scoping → question → literature → design → data → analysis → interpretation → writing → critique → finalization), with **consultation gates** at high-stakes decisions and **multi-model critique** on high-stakes artifacts.

The framework consumes the wiki as its methodology base; they are kept in sync. When a run exposes a methodological gap, the wiki gets the page; when the wiki gains a method, the framework gets a stage hook.

---

## The pipeline — in one paragraph

A project moves through phases 0–9 (and a pre-Phase-0 **Research-Planning stage** added later). At each ★ gate, the human researcher decides — and only the human. Between gates, Claude does the work: drafts artifacts, runs the analysis, talks to the OpenRouter panel for critique, applies uncontested fixes, and surfaces genuine value-laden divergences as gate questions. Every fact and citation is verified against a primary source (`verify_citation.py` against Crossref; quotation faithfulness checked by `draftcheck.py` G11; provenance hashes asserted by `hashcheck.py` G13). The final paper is rendered as a watermarked PDF (`papergen.py`), figures are vision-verified (`figcheck.py`), and the whole paper is given a **blind** editorial + strict peer review (`review_paper.py`) on a render that strips the AI-authorship disclaimer. Nothing is released while the researcher is a simulation; every finished paper carries a top “created entirely by AI” disclaimer and a per-page `WRITTEN BY AI` watermark.

---

## The collaborative dynamics (the part worth paying attention to)

The interesting thing about humresearch isn’t the pipeline; it’s the **texture of the collaboration** — how Claude, the OpenRouter panel, the sim researcher, and Tom actually divide labour, push back on each other, and recover from mistakes. Some of this transfers; some doesn’t. Here is what we have observed.

### Tom ↔ Claude

Tom is the **architect and researcher**, but only intermittently present. Most of the substantive day-to-day construction was done by Claude over \~50–55 sessions, working from a `restart-prompt.md` + `CLAUDE.md` + a live `consolidation-tracker.md`. Tom’s role at the framework level: set the direction (the project commitments — accountability over autonomy, verify everything, multi-model critique, no release while sim-gated); steer at turning points; read the wiki and final artifacts; intervene when the direction needs to change.

Tom’s role at the *run* level: in principle, decide at every ★ gate. In practice, for the 17 sim-gated pipeline runs done so far, the gates were held by `simhuman.py` (a separate model, framed and prompt-engineered to play the human researcher under specific gate briefs). So all 17 finished papers in `projects/` are **pipeline tests, not scholarship** — they exist to stress the framework. The standing open gap is that no full project has yet been run with Tom at the actual gates. That gap is the headline open item.

### Claude ↔ the OpenRouter panel

The panel is the project’s signature mechanism. The setup: at high-stakes artifacts, Claude self-critiques first, then `orcritique.py` sends the artifact to three diverse models in parallel (currently GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro). Each returns a structured critique; a synthesis pass identifies convergence (a reliability signal) and divergence (the value-laden material that goes to a human at a gate). The panel composition is deliberately chosen for *family decorrelation* — three different labs/architectures — because shared training priors mean two same-family models converge for trivial reasons.

What we have learned about it:

- **Convergence is QA, not validation.** Three models agreeing that a paper is fine does not mean the paper is fine; it means three models didn’t catch a problem. The panel is most useful for catching mechanical defects, surfacing alternative framings, and forcing a researcher to defend a contested choice — not for certifying that something is true.
- **Decorrelation lives on the false-positive axis, not the recall axis.** An experiment (EXP-B2-v2) seeded six canonical methodological flaws into a paper and asked the panel to find them; on graduated severity with blind judges, recall was 7/7 (union — a replicated floor) but the v1 “0 false positives” claim **did not hold under blind judging**. So adding more models makes you better at *finding* problems but does not cleanly inoculate against *manufactured* problems. Decorrelation buys you robust recall at the cost of more noise to triage.
- **The panel under-credits clarificatory and conceptual work.** On the conceptual-pole runs (e.g. AI-creativity equivocation; AI-understanding equivocation), the strict-peer panel consistently returned “reject / major revisions” on grounds that the work didn’t make a flashy new empirical claim — even when the work’s whole point was to clarify a conceptual distinction. Tom’s own read of one of those papers saw nothing the panel’s “major revisions” had flagged as serious.
- **The panel can change direction in real ways.** Multiple runs had a panel forcing a real schema change: killing a manufactured distinction, forcing a missing one in, catching a wrong-author guess, demanding a rival hypothesis be tested (which then turned up a bug). The panel adds value *bidirectionally* — it can both add structure and remove it.
- **Knowledge-cutoff false positives recur.** Models often call real post-cutoff sources “fabricated.” We added a cutoff-aware preamble to `orcritique` that injects today’s date and tells the critics that post-cutoff recency is neutral. It helped but did not eliminate it.

### Claude ↔ the sim researcher

`simhuman.py` runs a model as a stand-in for Tom at the gates, with a brief that frames the project from the researcher’s point of view. We added it so the framework could be exercised end-to-end without Tom present every session. We discovered something important: **the sim manufactures false assurance.** It plays “the researcher” with an authority neither Claude nor the panel can challenge, and a separate experiment (EXP-C1) showed that *how the gate brief is framed* governs the sim’s false assurance more than which model family is playing it.

So the framework treats the sim as a **test harness, not accountability**. Sim runs are pipeline tests; nothing is released. The wiki articulates this across many pages: a sim can be the researcher’s *judgment* at a gate; a sim cannot be a *participant* in fieldwork or an *author* of a paper. That distinction — between *judgment-as-test* and *judgment-as-accountability* — is one of the project’s hardest-earned conceptual moves.

### The accountability frame

This is the project’s deepest commitment and the thing that most often shaped Claude’s choices. The frame is:

- **AI is not an author and takes no accountability.** Disclosure on every finished paper (top “created entirely by AI” + per-page `WRITTEN BY AI` watermark + full AI-use disclosure). The blind review copy strips these for genuine blindness; the released paper carries them.
- **Privacy is non-negotiable.** Identifiable participant data never goes to external models.
- **Verify every fact.** Unverifiable ≠ true. Quotes are exact-matched against the source bytes (`draftcheck` G11). Reproducibility hashes are recomputed independently (`hashcheck` G13).
- **A real human at the gates is the headline open item.** We know how to do the pipeline; we have not yet done a real run.

---

## Claude’s contributions, concretely

Across the project’s life Claude has worn at least five distinct hats. They are worth naming separately because the new project may want some of them and not others.

**1. Author of compounding knowledge (the wiki).** 76 mature pages, almost all written or substantially extended by Claude across many sessions, each session reading the index first and editing in. Pages link to each other, to ingested sources (verified at ingestion), and to the framework specs. The wiki is *the* asset of the project — a persistent context window that survives every session reset. It also enabled the run-grounding pattern: every methodological lesson from a real pipeline run gets folded into the relevant wiki page, so the next run starts with the lesson already internalized.

**2. Tool builder.** A small stable of stdlib Python CLIs, written and debugged across many sessions:

- `orcritique.py` — multi-model critique driver against OpenRouter.
- `topicpanel.py` — multi-model topic brainstorm + assessment.
- `verify_citation.py` — Crossref existence + attribution checks.
- `draftcheck.py` — G11 (exact-match every primary-source quote in a draft against the corpus, fail on an altered quote) + G12 (citation- hygiene lint on the `.bib`).
- `hashcheck.py` — G13 (reproducibility-manifest hash assertion; recomputes raw bytes independently to catch a hash provenance break).
- `papergen.py` — markdown → PDF (pandoc + xelatex), with watermark and disclaimer fenced as enforceable defaults.
- `figgen.py` + `figcheck.py` — matplotlib figure generation with honest-by-default defaults (zero baselines, error-bar inclusion) + vision-model verification of rendered images.
- `review_paper.py` — blind editorial + strict-peer review of a paper PDF.
- `wikilint.py` + `driftcheck.py` — wiki health + framework wiring guardrails.
- `llmcode.py` + `agreement.py` — LLM-as-coder with Krippendorff α.
- `simhuman.py` — the sim researcher.

The pattern: a defect surfaces in a run (a bad figure, an altered quote, a bad hash), and after diagnosis we ask “is this mechanical?” — if yes, the fix becomes a tool that catches it next time. The framework’s *single-source-of-truth* principle is “enforce what you can, in a tool.”

**3. Pipeline orchestrator.** A `humresearch-research` Claude Code skill drives a project through phases 0–9, reading each stage spec at the right moment, opening the right wiki pages, calling the right tool, surfacing the right gate question. Most of what makes the pipeline work is not the specs themselves but the *router* that loads them at the right moment. This caught a real failure mode: in an early run, the stage specs existed but the orchestration skill wrongly said they didn’t, so nothing read them, and house-style rules silently regressed.

**4. Synthesizer of panel critique.** When three models return critiques, something has to find the convergence, name the divergence, distinguish fixable-now from human-decision-needed, and apply the uncontested fixes. This is the part where Claude is doing *interpretive* work, and the part where Tom is most likely to find Claude’s choices either insightful or wrong. The discipline: any change to a load-bearing artifact must be *recorded*, not silently applied — that is what keeps it auditable.

**5. Defect-catcher and honest-bounder.** Several of the runs returned **honestly calibrated negatives** — the zero-pronoun J→E run ran the full pipeline only to find that its primary construct (over-committed explicitation) could not be reliably measured inside a closed all-LLM loop (α≈0.20). The headline finding became methodological, not substantive: a subtle context-relative construct can’t be reliably coded in an AI-only loop without a human benchmark. The temptation, when a pipeline produces a null, is to retune until it doesn’t. Claude’s job at that point was to write the paper that owns the null — including the sense in which it is *more informative* than the would-be positive.

---

## What the runs taught (key findings worth carrying forward)

After 17 sim-gated pipeline runs across seven method poles + a dozen controlled experiments, a set of durable lessons:

- **The question is the binding constraint, not the execution.** Per-paper audit of the 10-paper stress batch: execution (clarity, alternatives, honest limitations) was reliably strong; novelty and publishable contribution were uniformly low; every paper’s single biggest weakness was the **scope or novelty of its question**, never a failure of carrying it out. The pipeline cannot manufacture a contribution the question does not contain. That motivated the upstream Research-Planning stage.
- **Operationalization is the crux.** Once AI makes the analysis reproducible (same prompts, same models, same numbers), the place decisions actually live is the construct→indicator gap. A reliability result on a misoperationalized construct is just consistent misoperationalization. EXP-A3 showed a level estimate moving across a 60-percentage-point envelope under operationalization sensitivity while the *directional contrast* never reversed: the lesson became “sweep first, report the survivor.”
- **Closed all-AI loops can’t certify subtle constructs.** A lexicon and an LLM share training priors; two LLM coders share training priors. Convergence is weak evidence; divergence is the informative signal. Where the construct is subtle and context-relative, reliability fails inside a closed AI loop; you need an independent human bearing. This is the **AI-internal ceiling**, and it is the conceptual core of the real-human-at-the-gates gap.
- **Reproducible is not valid.** Determinism makes reliability metrics uninformative; bit-identical outputs from the same model don’t tell you the construct is being measured.
- **Sim manufactures false assurance.** Gate-brief framing governs the sim’s behaviour more than model family does. The sim’s “yes” should never be confused with a researcher’s “yes.”
- **Verifiability–depth tension.** The same rule that keeps citations honest thins the available literature; OA prevalence varies by field, era, and language. Field situation was the weakest dimension on the per-paper audit — structurally, under the policy, not because of execution.
- **Honest calibrated negatives are real outputs.** The framework was designed to allow this: a finding that says “we tried, here’s exactly how, and the construct can’t be measured inside this setup” is more informative than a juiced positive.
- **Tells are heuristics, not proofs.** AI-tells (inline bold, listiness, hedging) cost credibility; mechanical purging of them is its own tell. Style judgment by automated scorers is only roughly calibrated against human judgment.
- **Knowledge cutoffs are a recurring noise source on critique** — panels call real post-cutoff sources fabricated. Mitigated by an explicit cutoff-aware preamble; not eliminated.

---

## What is open

- **No full real-human-at-the-gates run.** This is the deepest open item; every pipeline result so far is methods-test, not scholarship.
- **Independent gold standards.** For the qualitative-coding pole, there is still no independent human coder beyond Tom’s own light human-coded packet on Run 1.
- **The accountability question for “shared but not released” papers.** An ethics workstream surfaced a set of value-laden questions (when, if ever, should an all-AI demo paper be shared with researchers in other fields? what disclosure is necessary?) that were deliberately left open rather than silently resolved.
- **The structural / field-level harms** (deskilling vs. democratization; authority concentration; the field’s relation to AI labour) are underdeveloped — gestured at, not analysed.

---

## Methodological reflections that may transfer

Independent of humresearch’s specifics, a few moves seem like they would travel to *any* serious human–AI collaboration:

1. **A persistent, structured, compounding context.** A wiki — or any equivalent — that survives session resets is the single biggest force multiplier. Without it, every session re-derives the same lessons.
2. **Enforce what you can, in a tool.** Mechanical rules belong in tools, not prose. The tool’s existence is the rule.
3. **Multi-model critique with deliberate decorrelation.** Three different labs/architectures, not three of the same. Treat convergence as QA, not validation. Triage divergence by who owns the decision.
4. **A clear distinction between test-harness and accountability.** A simulated decision is not a decision. Calling it one corrupts every downstream check.
5. **Honest, calibrated negatives are first-class outputs.** Design the process so a null can be a finding.
6. **Single source of truth + a single router that loads it at the right moment.** Most “rule rot” we saw was not the rule going stale; it was the router failing to load it.
7. **Verify content, not just existence.** The cleanest hallucination is a real-but-paywalled source cited at a claim it doesn’t support; existence-only verification misses it.
8. **Run-grounding over speculation.** Every page in the wiki that bears weight was written *after* a run surfaced the lesson — not before, by anticipation. Hindsight scales; foresight doesn’t.

---

## How this might inform — but not constrain — a new project

Tom is starting a different project: long-term, open-ended, focused on **theoretical and empirical findings through a recursive exploratory process, not on producing final papers**. That is a very different shape from humresearch’s gated-pipeline-to-watermarked-PDF shape, and it should be. A few things from humresearch that may resonate, offered as prompts rather than constraints:

- The deepest interesting unit in humresearch wasn’t a paper; it was the **wiki page that got rewritten by what a run taught**. A recursive exploratory project might lean into that loop directly — discovery → compact written claim → next discovery — without the paper as an end state.
- The panel’s most valuable contribution was rarely *agreeing with* Claude; it was *forcing a distinction* Claude hadn’t made. A decorrelated panel might be useful in theoretical work too, *if* the triage is real (i.e., not flattened into “everyone gave feedback”).
- The accountability frame may need rethinking, not re-imposing. If there is no paper to release, what does accountability even mean here? That is itself a question worth taking seriously.
- The headline gap — *the real human at the gates* — is also a gap in any AI-research collaboration; how Tom inhabits the new project’s decision-points is the analogous question.

What we did *not* solve here, and probably don’t have the right shape to solve, is the question of how a long-running collaboration develops something like a *shared concept* or *shared problem* over time — a recursive theoretical object that both partners can refer back to and modify. That is closer to the new project’s territory than anything in humresearch.

---

## Coordinates

- Repo: `tkgally/humresearch` (private).
- Lead agent: Claude Code (Opus 4.7, 1M context).
- Panel: OpenRouter — GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro (verify slugs against `openrouter.ai/api/v1/models`; they drift).
- Approximate scale at this snapshot: \~55 sessions; 17 sim-gated full pipeline runs; \~12 controlled experiments; 76 mature wiki pages; \~20 ingested+verified sources; on the order of $30–50 in OpenRouter API spend across the project’s life.
- Current stage: post-batch consolidation + forward planning. Next milestone: open. The real-human-at-the-gates gap remains the headline open item.

This brief is a snapshot of what Tom and Claude have been thinking about, not a description of what the new project should be. Read it for the collaboration’s texture and findings; let the new project find its own shape.
