# ai-semantics — Founding Conversation

*A record of the conversation between Tom Gally and Claude (Opus 4.7) on 2026-05-28 in which the* ai-semantics *project was conceived and its starting prompt drafted.*

The session opened with Tom uploading a brief on his prior **humresearch** project (reproduced as **Appendix A**) and produced a starting prompt / charter (reproduced as **Appendix B**). Brief italic notes mark where Claude consulted external sources during the exchange.

---

## Tom

Please look at the attached document. I explains what I want to do with you in this session. After you have read it, please ask me a question or two to get us started.

*[Claude read the uploaded humresearch brief in full — see Appendix A.]*

## Claude

I've read it carefully — and the second read of the truncated middle (the five hats, the run findings, the accountability frame) is where it earned its keep. A few things landed for me before I ask anything.

The clearest signal in the brief is the pivot in shape. humresearch's deepest unit was never the paper; it was *the wiki page rewritten by what a run taught* — discovery → compact written claim → next discovery. You're explicitly saying the new project might lean into that loop directly and drop the paper as an end state. And the thing you name at the very end as closest to the new territory — "how a long-running collaboration develops something like a shared concept or shared problem over time, a recursive theoretical object both partners can refer back to and modify" — reads less like a leftover and more like the actual seed. So I'm reading the new project as: the recursive object is the unit, and the question of how two partners *grow and hold* such an object is at least partly the point.

That said, the brief is almost entirely about humresearch. It tells me the *shape* of the new project but not its *subject*. So my two questions:

First — what are the findings going to be *about*? I can see three live possibilities and can't tell which (or which mix) you intend. One: the project is partly self-referential — the territory is human–AI collaboration itself, the formation of shared concepts, with our own collaboration as both instrument and object. Two: there's an independent domain you have in mind — something in your wheelhouse (Japanese–English translation theory, lexicography, learner-dictionary semantics, English-in-Japan) where a recursive exploratory loop could surface real theoretical and empirical claims. Three: the subject is deliberately undecided, and *finding* the territory is itself the first turn of the recursion. Which of those is closest — or is it a fourth I'm not seeing?

Second, on mode for *right now*: do you want me as a thinking partner, shaping this in conversation until the object and the loop are clear enough to commit to — or do you want to stand up the persistent scaffolding first (a repo, a wiki, the equivalent of restart-prompt + CLAUDE.md) and discover the shape by running it? The brief's own lesson — run-grounding over speculation, "foresight doesn't scale" — would argue for the latter. But that lesson came from a pipeline with a known target, and you don't have one yet, so I don't want to assume it transfers.

---

## Tom

About your first question: I have in mind an independent domain, something about which there already exists research dating back centuries but which may be changing because of advances in AI. I will propose a specific domain later in this chat, but I first want to set the grounding for the framework. Second, the end result of this conversation is a starting prompt that you would write for me that I would use in a new repo and give to Claude to start the new project. That prompt would describe both the purpose of the project and how it will be done from a technical perspective. I imagine that it might use Karpathy's LLM-wiki as a framework, but I am open to other modalities as well.

*[Claude searched the web for Karpathy's "LLM Wiki" pattern and fetched the original gist before replying.]*

## Claude

Good — I've read the gist itself now, not just the writeups, so I can reason about fit rather than vibes.

Stripped down, Karpathy's pattern is a *consolidation* engine. Three layers — immutable raw sources, an LLM-owned wiki of interlinked markdown pages, and a schema file (CLAUDE.md) that disciplines the agent into a wiki maintainer rather than a chatbot. Three operations — ingest (one source might touch 10–15 pages), query (and crucially, good answers get filed back as new pages so explorations compound), and a periodic lint pass for contradictions, stale claims, and orphans. Two navigation files: index.md as a content catalog, log.md as an append-only chronicle. The human curates sources, directs, and asks; the LLM does all the bookkeeping. It's Memex with the maintenance problem solved.

The thing to notice is that this is almost exactly humresearch's wiki — persistent, compounding, agent-maintained — but framed entirely around *ingesting existing sources*. That's the seam I'd want to think hard about before building on it, because your project's unit isn't "a page summarizing what I read." It's "a claim the project itself produced and then revised when the next discovery pushed on it" — the recursive theoretical object. The bare pattern has no first-class notion of *that*. A finding you generate has a different epistemic status from a source summary, a different lifecycle (conjecture → tested → revised → maybe retired), and different provenance (it points at your reasoning and your probes, not someone else's paper).

What's striking is that the gist's own comment thread has already found this as the pattern's main failure mode in practice. Independent builders report three recurring collapses: identity (the same concept filed under near-duplicate names), level (life-scale themes flattened to sit beside tactical findings, so importance disappears), and relationship (every edge degraded to a generic "related," losing similar/contains/contradicts). One builder's fix was to make citable *claims* the primitive and let the concept layer fall out of claim-density. There's even an arXiv manuscript, SciAI Wiki, extending the pattern to science by adding provenance and audit. So the bare pattern wants augmentation precisely where your project lives.

Two grounding questions, both upstream of the domain:

First, the layering. Do you want a single-stratum wiki (Karpathy-style — everything derived from ingested literature), or explicitly two strata: a literature layer where the bare pattern works as-is, plus a *findings layer* of typed, first-class objects the project generates — conjecture, claim, result, open-question — each with its own lifecycle and revision history? My instinct from humresearch is the latter, since the page-rewritten-by-a-run was your deepest unit and that's a findings-layer object, not a source summary. But I want to hear whether you see the recursive object as a distinct page type or as something that should emerge from the same machinery.

Second, what "empirical" actually cashes out to. The pattern as written reads and synthesizes; it doesn't generate evidence. In your domain — an old field possibly being reshaped by AI — do the empirical findings come from new investigation the project runs (probing models as objects of study, analyzing texts or corpora, small experiments — which implies a tools layer and maybe a decorrelated panel), or is "empirical" mostly re-marshalling evidence already sitting in the centuries of scholarship (which keeps us close to bare LLM-wiki plus careful provenance)? That answer decides whether the repo is markdown-and-agent or markdown-and-agent-and-Python.

I'll hold the accountability question — what your binding in-the-loop role is when there's no paper to anchor it — until these two settle, since they'll reshape it.

---

## Tom

I imagine a two-strata or multiple-strata system. The summary of prior research and knowledge will be the base stratum, and the novel work—whether theoretical or empirical or some combination of them—will be in one or more strata above it. By "empirical," well, let me tell you the starting idea I have in mind: developing a new understanding and theory of *lexical and grammatical meaning* (i.e., linguistic semantics) that includes not only meaning as it has been conventionally understood, that is, in relation to human language and thought, but also meaning in the context of today's LLMs (both text-based and multimodal) and possible other forms of AI that emerge in the coming years. Traditionally meaning (in all its various interpretations) has been assumed to be closely linked to the human brain, mind, body, interaction, society, etc. (though if there have been any serious supernatural or spiritual discussions of meaning those might be considered as well, too). With LLMs, we see a phenomenon that resembles meaning (and is often interpreted by humans as meaning) but does not have the same physical or mental correlates as conventional meaning does. This new type of meaning might be considered to exist both within LLMs alone as well as in interactions between LLMs and people (and between different LLMs), but I don't know if that has been explored yet. So my tentative idea is to develop a comprehensive theory of meaning for this era, a theory that might be grounded in actual data-collection or experiments. Note that I am focusing on lexical and grammatical meaning, that is, the meanings associated with words, phrases, sentences, and grammatical structures. Thus it might be possible to design and conduct experiments with LLMs (and maybe with LLMs and humans) to explore in depth the structures and characteristics of meaning as used by LLMs. The design and results of such experiments would draw on and reflect back on conventional human-only understandings of meaning. I am hoping that, once we have our framework set up, it would be possible to set up an autonomous system that recursively tries and polishes experiments using LLMs to try to get a novel, in-depth, grainy understanding of meaning in this new era. What are your thoughts on this idea? Are you aware of any current research or discussions of semantics in the LLM era?

Also, before I forget, for this new project, especially when exploring, assessing, and learning from the prior literature, I will help you find resources such as paywalled papers or books that you cannot get through internet searches. A major weakness of the humresearch project was its reliance on materials that were web-accessible to you. I have access to paywalled research papers through the University of Tokyo Library system. If there are any important books that you would like to read, I can get them for you, too. (You might have to OCR them, but I have done some OCR tests with you recently and the quality was very high using your native vision capabilities.)

What are your thoughts about all this?

*[Claude ran several web searches on the current state of LLM-semantics research — distributional semantics and philosophy of language, the formal/functional competence distinction, construction grammar probing, and interactional/multi-agent meaning — before replying.]*

## Claude

This is a strong idea, and I want to tell you both why I think so and where I'd push on it, then map the existing terrain (which is livelier than you might expect but lopsided in a way that works in your favor), then react to the resource offer — which I think is more consequential for the framework than it might first appear.

On the idea itself. The move I find most valuable is that you're proposing a *constructive* project in a field that has been almost entirely *adjudicative*. Nearly all the existing work asks a gatekeeping question — do LLMs "really" have meaning, yes or no — and argues membership for or against. You're proposing instead to treat the LLM phenomenon as a genuine explanandum and build a descriptive theory broad enough to cover both the human case and the machine case. That reframing ("what is the structure of whatever-this-is?" rather than "does it qualify?") is itself a contribution, and it's the kind of thing that's hard for a single paper to attempt but well-suited to a long compounding project.

The central hazard is equivocation, and you should expect it to be the project's recurring adversary. "Meaning" will silently slide between at least four things: the content humans attribute to a string; the model-internal representational structure (the geometry of activations); the functional/inferential role a token plays in producing behavior; and the meaning that gets constituted in an interaction. The literature already fragments the term in several incompatible ways, and a theory that doesn't hold these apart will produce sentences that sound deep and mean nothing. This is not hypothetical for our collaboration specifically: humresearch's conceptual-pole runs kept foundering on exactly this (the AI-understanding and AI-creativity equivocations). So I'd argue the very first findings-layer object isn't a theory at all — it's a controlled typology of senses of "meaning," which then becomes load-bearing infrastructure: every later claim-page tags which sense it invokes, and that tag is mechanically lintable. The strata mirror the typology.

The second thing I'd press: your instinct to restrict to *lexical and grammatical* meaning is the right constraint, and the *grammatical* half is your sharpest and least-crowded wedge. Almost all the philosophical action is on content words, reference, and concepts. But there's a real and young subfield probing whether models grasp the form–meaning pairings of *constructions* — the ditransitive, caused-motion, resultative, the way-construction — and whether that's genuine constructional semantics or surface statistics. Recent work fine-tunes and benchmarks models specifically on phrasal-construction semantics and finds selective, uneven gains, with qualitative analysis cautioning against reading good benchmark numbers as deep constructional understanding. A position-paper line (Weissweiler and colleagues) argues that Construction Grammar gives uniquely diagnostic probes precisely because constructional meaning lives in non-contiguous, slot-filled patterns whose meaning exceeds the sum of the words. This matters because grammatical meaning is both under-theorized at the meaning-theory level *and* unusually tractable experimentally — minimal pairs, acceptability, constructional inference — so it's where your "recursively design and polish experiments" ambition can actually bite.

A third wedge, which is the one you flagged as maybe unexplored: you're largely right. The relational/interactional version of LLM meaning — meaning constituted *between* a model and a person, or between models — is genuinely thin. There's a large multi-agent literature, but it's about coordination, negotiation, and emergent social behavior, not about meaning-constitution as a semantic phenomenon; the "agents" there are loci of strategy, not loci of sense. So a theory that locates some LLM-meaning in the interaction rather than in the model alone has philosophical scaffolding to stand on (Brandom's inferentialism is inherently a scorekeeping-in-a-practice view; Clark on conversational grounding; later Wittgenstein) but very little empirical company. That's a real opening, and it's risky in the good way.

Now the existing terrain, so you can see where the base stratum has to be thick. The field organizes around a few axes. The foundational frame everyone starts from is distributional semantics — Firth and Harris operationalized, which is literally what the models implement; philosophers of language (Grindrod, Porter, Hansen at Reading) now treat LLMs as instruments for cracking open old questions about the nature of meaning, not just as engineering artifacts. The skeptical pole is anchored by Bender and Koller's 2020 "form vs. meaning" argument (the octopus) and the Stochastic Parrots paper: meaning requires grounding in referents or communicative intent that form alone can't supply. Against that, several constructive positions have appeared: Lyre argues grounding isn't a yes/no matter but multi-criterial and gradual — functional, social, and causal — and that LLMs show some evidence on all three. Piantadosi and Hill's "meaning without reference" argues conceptual-role/inferential meaning doesn't need referential grounding at all. A 2024–25 line imports Brandom's inferentialism wholesale, reading transformers as fundamentally anti-representationalist meaning-generators and even proposing a consensus/interactive theory of truth for them. Others apply classical metasemantics directly — Evans's naming practices and Millikan's teleosemantics — to argue LLMs are genuinely meaningful language users, while the reference debate (Cappelen and Dever; Mandelkern and Linzen on whether LM words refer) and Fregean sense-based readings run alongside. There's a forthcoming Sterken-and-Cappelen volume, *Communication with AI: Philosophical Perspectives*, that will be a landmark collection worth getting whole.

Cutting across all of that, and probably your most useful single anchor, is Mahowald, Ivanova, Fedorenko and colleagues' formal-vs-functional distinction: knowledge of linguistic rules and patterns (formal) versus understanding and using language in the world (functional), grounded in the neuroscience finding that these rely on different brain mechanisms — with LLMs near human-level on formal competence and spotty on functional. There's now a 2026 follow-up testing whether that dissociation is real *in model internals* via circuit analysis, which is exactly the empirical register your project would work in.

The lopsidedness that favors you: this whole conversation is being conducted by philosophers of language and NLP-probing researchers. There is strikingly little input from descriptive lexical semantics and lexicography — the fine-grained, polysemy-tolerant, sense-distinction-obsessed sensibility that is your home turf. The debate tends to operate at a coarseness ("do they have meaning") that a working lexicographer would find almost quaint. Your instinct that there's a "grainy" structure to be found is, I think, correct, and it's under-pursued precisely because the people arguing about it don't think in senses and citations the way you do.

Where this leaves the framework, briefly, since grounding it is the session's job. The domain is unusually hospitable to your autonomous recursive-experiment vision for one concrete reason: the object of study is queryable on demand and experiments are cheap API calls, not the heavyweight pipeline runs that made humresearch's loop slow. So "recursively try and polish experiments" is genuinely feasible here. But humresearch's hardest lesson transfers intact: the binding constraint will be operationalization, not execution. The autonomy should be aimed at experiment *iteration and refinement*, with your gates falling on the construct→indicator decisions (what counts as evidence that construction X carries meaning Y in model M). And the AI-internal ceiling lesson sharpens into a design rule: probing LLM-meaning with LLMs shares training priors, so convergence is weak evidence — which means experiments need human anchors or repurposed psycholinguistic paradigms, and the decorrelated panel does double duty, with the other models serving not only as critics but as *subjects*. Cross-model divergence in semantic behavior is itself data about whether "LLM-meaning" is model-specific or convergent — which connects to the representational-convergence question. That fusion of humresearch's panel mechanism with the object of study is, I think, one of the more elegant things available to us here.

On the resources: yes, emphatically, and it changes the design more than it looks. humresearch's structural weakness was that its base stratum was only as deep as what was web-reachable to me, and this is a field whose canon lives in monographs and paywalled journals. With UTokyo access and OCR, the base stratum can actually rest on the works that *define* the territory rather than on whatever's open. The ones I'd want early, roughly in priority order: Cruse (*Lexical Semantics*, *Meaning in Language*) and Murphy (*Lexical Meaning*) and Lyons (*Semantics*) for the lexical base; Goldberg (*Constructions*, *Explain Me This*) and Croft for the constructional base; the classics that the LLM debate keeps invoking but rarely reads in full — Frege's sense/reference papers, Putnam's "The Meaning of 'Meaning'," Lewis's "General Semantics," Evans's *Varieties of Reference*, Brandom's *Articulating Reasons*, Millikan, and the Firth/Harris originals; and the Sterken-Cappelen volume for the current wave. The OCR workflow we tested works well — you upload scans or PDFs, I read them natively and file summaries with page-level provenance into the base stratum (the SciAI Wiki people are converging on exactly that claim-level citation discipline). The one thing to keep is humresearch's "verify content, not just existence" rule, which actually gets *easier* now, because the source is in hand rather than inferred from an abstract; and we hold these for research use, storing grounded summaries and claims with citations rather than wholesale text.

One question to converge the framework, and it's the one that most determines the tools layer: when you picture the experiments, is the primary instrument (a) behavioral probing of models through the API — elicitation, minimal pairs, constructional inference, cross-model comparison, all of which is cheap and needs only OpenRouter-style access; (b) representational/interpretability analysis — embedding geometry, probing classifiers, feature-level work, which is heavier and wants open-weight models and real compute; or (c) human–LLM comparison, which pulls in human data and its attendant ethics and logistics? The framework can grow to hold all three, but which one is the v1 center of gravity decides whether the starting prompt provisions a markdown-and-API repo or something with a much larger technical footprint. My instinct is (a) as the spine, with (b) reserved for specific claims that behavioral probing can't settle — but you know the experiments you're imagining better than I do yet.

---

## Tom

Thanks. Very helpful. For the time being, the primary instrument would be (a). I doubt if I will have access to sufficient compute to do (b), though if ideas for feasible experiments (such as using very small models) emerge we could try that, too. As for (c), any human data will be from corpora and similar existing resources, not new experiments with human subjects. How does that sound?

## Claude

That sounds right, and the satisfying part is that the constraint and the intellectual core point the same direction instead of fighting. Behavioral probing through the API is exactly where grammatical and constructional meaning is most directly testable — minimal pairs, constructional inference, elicitation — and it keeps each experiment cheap enough that the recursive design–run–revise loop is genuinely automatable. You're not trading away the good stuff to save compute; for this target, (a) *is* the good stuff.

Two refinements, since both quietly reshape the framework.

On (c): restricting human data to existing corpora and resources is cleaner than it looks — it removes human-subjects ethics, recruitment, and logistics, and keeps every human anchor reproducible and citable, which fits the verify-content discipline. But it relocates a load-bearing piece. The AI-internal ceiling still applies: probing LLM meaning with LLMs shares training priors, so without an independent human bearing somewhere the loop mostly confirms itself. With no new collection, that bearing has to come entirely from curated human-labeled resources — treebanks and sense-annotated corpora, acceptability-judgment sets, psycholinguistic norms, construction inventories, and the dictionaries and usage evidence that are your home ground. So the human anchor becomes a *sourcing and curation* problem living in the base stratum rather than a data-collection problem. That's a feature, but it means "what existing human resource grounds this against human meaning?" should be a standing requirement on every empirical finding — probably a gate, not a nicety.

On (b): I'd reframe small models from fallback to a specific and oddly well-matched tool. Grammatical and constructional effects show up at GPT-2 scale — the whole minimal-pair benchmark tradition was built around models that small — and a small open-weight model gives you something the big hosted ones often won't expose cleanly: direct next-token probabilities, i.e. surprisal. That's the cleanest quantitative signal for minimal-pair semantics, far better than forced-choice text answers, and it runs on modest hardware. So the small-model lane is where your *graded, numeric* evidence would come from, complementing the big models' richer but coarser inferential responses. Worth provisioning for even if you start without it.

That closes the instrument question, and I think we're nearly at enough grounding to assemble a skeleton. The one piece I still want your read on is the accountability reframe I parked. In humresearch the human gate attached to releasing a paper; here there's no paper, so the binding question becomes: at which moments must you personally be in the loop for the findings to be yours and trustworthy? My proposed answer is two kinds of moment. First, operationalization — your sign-off on how a construct becomes an indicator (what counts as evidence that construction X carries meaning Y in model M), because that's where humresearch showed the real decisions live and where an autonomous loop will quietly cheat by retuning until it gets a positive. Second, the human-anchor check — confirming the existing resource invoked actually bears on the claim, not merely that it exists. Between those gates, Claude runs: designs, probes, panels, files, revises, logs. Does that division feel right, or do you want a tighter or looser presence than that?

If it lands, I'll turn the whole picture — purpose, strata, the recursive experiment loop, the schema rules, the async gates, and the panel-as-subjects-and-critics fusion — into a framework skeleton to serve as the backbone of the starting prompt.

---

## Tom

Since Claude can run 24 hours a day (and I have a Max plan), and since my time and attention at sixty-nine years old and still working nearly full time are limited, I want my presence to be relatively light: answering questions when I am available, providing resources when I can, guiding you in certain directions when appropriate, but with you working largely autonomously in response to periodic resume-working prompts from me. In particular, I do not imagine myself serving as a human informant for linguistic experiments.

On a logistical side, most of the projects I have done with Claude Code for the Web using repos hosted on Github—as I imagine this new project will be—have been done with me pointing you to a prompt in the repo, you working for between five minutes and an hour or two in response to that prompt, and then you committing and merging the changes to main on Github and waiting for the next prompt from me. For some projects, I do have Routines set up to give you prompts at regular intervals, but the work is still episodic. Ideally, I would like you to be able to work constantly without interruption for days on end, but I haven't been able to figure a method to do that. The major limitation seems to be your context window. If some method for continuous, uninterrupted work becomes available, I would like to do that in this project. I will monitor you throughout the day and interrupt and answer questions when necessary, but I really want to push the envelope of what might be possible with autonomous AI-conducted research.

*[Claude verified the current behavior and limits of Claude Code "Routines" via web search before replying.]*

## Claude

Good — and the "no human informant" point closes the loop on (c): every scrap of human bearing now comes from existing resources, never from you in real time. That's consistent, and it means I never have to design an experiment that stalls waiting for you to play subject.

The more important thing in what you wrote is that the limitation you've been bumping against isn't really the obstacle it looks like, and the architecture we've been converging on is already the way around it. Let me ground that in how the tooling actually works right now, because I checked rather than trusting my memory.

Routines are the relevant mechanism, and they're a real, current feature on your Max plan. They run on Anthropic's cloud infrastructure rather than your laptop, so they keep going when your machine is closed, and each run is a full Claude Code cloud session that runs autonomously with no permission prompts mid-run, triggered by a schedule, an API call, or a GitHub event. But here's the load-bearing detail: each run is an independent session with no session reuse, and the repository is cloned fresh from its default branch at the start of every run. There is no unbroken multi-day session, and the long-lived local option (`/loop`) is capped at seven days, lives on your machine, and doesn't survive restarts. So "run continuously for days" as one session isn't available, and chasing it is the wrong target.

The right target is what you're already doing by hand, automated and tightened: a chain of short, independent runs, each one resuming the project cold from the repo. Because every run starts with a fresh context and a fresh clone, *all* continuity has to live on disk, in the repo — which is exactly the LLM-wiki design we'd build anyway. The context window stops being the bottleneck because no single run ever needs to hold the whole project; it holds a baton file plus whatever it pulls selectively from the wiki. A schedule trigger firing on a tight cadence (say hourly, or whatever the work-unit size and your usage budget support) turns those independent links into something that, from your monitoring chair, looks like days of continuous progress. The wiki pattern pays off twice: once for compounding knowledge, once for cold-start resumability.

That gives the framework three non-negotiable structural commitments. First, a baton file — call it NEXT.md — that is the last thing every run writes and the first thing every run reads: where we are, what just finished, the next concrete action, and what's blocked pending you. Second, work decomposed into run-sized units that each end in a committed, merged state, drawn from a queue the baton points into; this is humresearch's "decompose the large prompt into sequentially executable files" lesson made mandatory. Third — and this is the piece your current habit already gets right — each run must merge its work to the default branch before it ends, because the next run clones that branch fresh; skip the merge and the chain re-does stale work. The routine's own prompt then becomes almost static: "resume this project from its current state per CLAUDE.md and the protocol." The variable content lives in the repo, so the project effectively drives itself from disk.

This also resolves the accountability gates into a form that fits a lightly-present human. They can't block — you're not there, and runs don't pause for approval. So when a run hits an operationalization choice or a human-anchor check, it writes the question, its options, and its provisional default with rationale into a decisions queue, marks everything downstream of that choice as contingent, and keeps working on what isn't blocked. You answer the queue when you visit. The one inviolable guardrail — straight from humresearch's "the sim manufactures false assurance" lesson — is that a provisional default may be used to keep exploring but may never be promoted to a settled finding until you ratify it; the discipline (and a lint check) enforces that no result page rests on an unratified operationalization without being flagged contingent. That's the whole accountability frame, just made asynchronous: autonomy everywhere except the value-laden hinge points, which queue for you rather than stop the line.

Two practical notes before we build. The risk profile here is unusually benign for high autonomy: the project reads corpora, calls model APIs read-only for probes, writes markdown, and commits to its own repo — no irreversible external side effects — which is part of why it's a good candidate for pushing the envelope. The real costs to bound are usage and API spend: routines draw down your subscription limits the same way interactive sessions do, so the cadence should be tuned so each run does something substantial rather than firing constantly, and the experiment API (OpenRouter) should run under a hard budget cap that the tooling respects.

I think that's the last large piece of grounding. We now have the purpose, the domain, the instrument (a, with the small-model lane held in reserve), the resource pipeline, the light-presence model, and the autonomy architecture. When you're ready, I'll assemble all of it into a framework skeleton — strata, the recursive experiment loop, the run protocol, the schema rules, the async gates, and the panel-as-subjects-and-critics fusion — as the backbone of the starting prompt. The few things still genuinely open are small and fillable: the repo name, the schedule cadence, and which three decorrelated models you want on the panel. Want me to draft that skeleton next?

---

## Tom

Yes, please draft not just the skeleton but the prompt itself. The repo will be called ai-semantics. The schedule will be decided by me; I will set up Routines that will point you to the NEXT.md file. The decorrelated models will be decided by you based on what is available on OpenRouter (you will have access to an OpenRouter API key in the Claude environment) and based on your own tests of which models are appropriate for particular tasks. l will monitor the spend at OpenRouter and give you instructions if things get too expensive. Also, the use of Routines means that I will stay within my token limits for the Max plan; I already run a number of Routines each day for v

## Claude

*[Claude drafted the starting prompt / charter and saved it as* `ai-semantics-starting-prompt.md` *— reproduced as Appendix B.]*

A few notes on the choices, in case you want to adjust before committing it:

I wrote it as a dual-purpose document — a first-run bootstrap *and* the durable `PROJECT.md` charter — so there's one source of truth rather than a prompt that drifts from the repo it created. The steady-state loop stays exactly as described: routine → "read `NEXT.md` and continue."

I left three things for the first runs to settle rather than hardcoding, two because you asked and one because it'll go stale: the panel models (the prompt has the agent enumerate OpenRouter, pick three decorrelated families, calibration-test per task, and record the choices with a date); the schedule cadence (yours to set); and the OpenRouter budget cap, left as a placeholder in `config/budget.md` for you to fill.

Two design decisions worth flagging. First, "merge to the default branch at the end of every run" is a hard rule, since each routine run clones that branch fresh — it's the single point where the chain breaks if it's skipped. Second, the accountability frame is baked entirely into the async gate mechanism: contingent findings can't be promoted to settled without ratification in `decisions/`, and a lint check enforces it. That's the "no paper, so what does accountability mean" question resolved into something a lightly-present human can actually operate.

(Tom's message had cut off at "I already run a number of Routines each day for v—"; he later confirmed nothing important rode on the rest.)

---

## Tom

Excellent. [Confirmed the cut-off was nothing important, and asked Claude to produce this conversation as a markdown file to keep as a history of how the project began.]

## Claude

[Produced this document.]

---

# Appendix A — The uploaded humresearch brief

> *This is the document Tom uploaded at the start of the session as background and provocation.*

## humresearch — a brief for a new Claude session

This file is context for a **new** conversation Tom is starting with Claude about a different, open-ended research project. It summarizes the **humresearch** project Tom has been working on with Claude (and a panel of other LLMs) over the past few weeks — what it is, how the collaboration actually works, what we've learned, and where it has landed. It is offered as *background and provocation*, not as a template; the new project is meant to be genuinely exploratory, so read this for what it might suggest by way of collaborative texture, not for a methodology to imitate.

### What humresearch is

humresearch is an experiment in **mostly-autonomous, human-consulted AI research for the humanities and social sciences (H&SS)**. It was inspired by the AutoResearchClaw project (which targets full autonomy in the natural sciences) but redesigned around a different commitment: the human researcher must remain **accountable** — able to understand, explain, and defend the research as their own — even when AI does most of the work. Tom is the researcher; Claude (Claude Code, currently running on Opus 4.7) is the lead agent; a rotating panel of other LLMs (via OpenRouter — GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro) provides decorrelated critique.

The project has two parts that grew up together:

1. A **knowledge wiki** (`wiki/`) — a persistent, compounding knowledge base on H&SS research methods, traditional and AI-assisted. 76 mature pages across `methods/`, `concepts/`, `ai-research/`, `fields/`, `sources/`. Methods-centric, with strong weight on the AI-assisted angle, because that is the novel contribution.
2. A **research framework** (`framework/`) — a fresh, ARC-inspired H&SS pipeline expressed as markdown stage specs + Claude Code skills + small stdlib Python tools. Ten phases (research planning → scoping → question → literature → design → data → analysis → interpretation → writing → critique → finalization), with **consultation gates** at high-stakes decisions and **multi-model critique** on high-stakes artifacts.

The framework consumes the wiki as its methodology base; they are kept in sync. When a run exposes a methodological gap, the wiki gets the page; when the wiki gains a method, the framework gets a stage hook.

### The pipeline — in one paragraph

A project moves through phases 0–9 (and a pre-Phase-0 **Research-Planning stage** added later). At each ★ gate, the human researcher decides — and only the human. Between gates, Claude does the work: drafts artifacts, runs the analysis, talks to the OpenRouter panel for critique, applies uncontested fixes, and surfaces genuine value-laden divergences as gate questions. Every fact and citation is verified against a primary source (`verify_citation.py` against Crossref; quotation faithfulness checked by `draftcheck.py` G11; provenance hashes asserted by `hashcheck.py` G13). The final paper is rendered as a watermarked PDF (`papergen.py`), figures are vision-verified (`figcheck.py`), and the whole paper is given a **blind** editorial + strict peer review (`review_paper.py`) on a render that strips the AI-authorship disclaimer. Nothing is released while the researcher is a simulation; every finished paper carries a top "created entirely by AI" disclaimer and a per-page `WRITTEN BY AI` watermark.

### The collaborative dynamics (the part worth paying attention to)

The interesting thing about humresearch isn't the pipeline; it's the **texture of the collaboration** — how Claude, the OpenRouter panel, the sim researcher, and Tom actually divide labour, push back on each other, and recover from mistakes. Some of this transfers; some doesn't. Here is what we have observed.

#### Tom ↔ Claude

Tom is the **architect and researcher**, but only intermittently present. Most of the substantive day-to-day construction was done by Claude over ~50–55 sessions, working from a `restart-prompt.md` + `CLAUDE.md` + a live `consolidation-tracker.md`. Tom's role at the framework level: set the direction (the project commitments — accountability over autonomy, verify everything, multi-model critique, no release while sim-gated); steer at turning points; read the wiki and final artifacts; intervene when the direction needs to change.

Tom's role at the *run* level: in principle, decide at every ★ gate. In practice, for the 17 sim-gated pipeline runs done so far, the gates were held by `simhuman.py` (a separate model, framed and prompt-engineered to play the human researcher under specific gate briefs). So all 17 finished papers in `projects/` are **pipeline tests, not scholarship** — they exist to stress the framework. The standing open gap is that no full project has yet been run with Tom at the actual gates. That gap is the headline open item.

#### Claude ↔ the OpenRouter panel

The panel is the project's signature mechanism. The setup: at high-stakes artifacts, Claude self-critiques first, then `orcritique.py` sends the artifact to three diverse models in parallel (currently GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro). Each returns a structured critique; a synthesis pass identifies convergence (a reliability signal) and divergence (the value-laden material that goes to a human at a gate). The panel composition is deliberately chosen for *family decorrelation* — three different labs/architectures — because shared training priors mean two same-family models converge for trivial reasons.

What we have learned about it:

- **Convergence is QA, not validation.** Three models agreeing that a paper is fine does not mean the paper is fine; it means three models didn't catch a problem. The panel is most useful for catching mechanical defects, surfacing alternative framings, and forcing a researcher to defend a contested choice — not for certifying that something is true.
- **Decorrelation lives on the false-positive axis, not the recall axis.** An experiment (EXP-B2-v2) seeded six canonical methodological flaws into a paper and asked the panel to find them; on graduated severity with blind judges, recall was 7/7 (union — a replicated floor) but the v1 "0 false positives" claim **did not hold under blind judging**. So adding more models makes you better at *finding* problems but does not cleanly inoculate against *manufactured* problems. Decorrelation buys you robust recall at the cost of more noise to triage.
- **The panel under-credits clarificatory and conceptual work.** On the conceptual-pole runs (e.g. AI-creativity equivocation; AI-understanding equivocation), the strict-peer panel consistently returned "reject / major revisions" on grounds that the work didn't make a flashy new empirical claim — even when the work's whole point was to clarify a conceptual distinction. Tom's own read of one of those papers saw nothing the panel's "major revisions" had flagged as serious.
- **The panel can change direction in real ways.** Multiple runs had a panel forcing a real schema change: killing a manufactured distinction, forcing a missing one in, catching a wrong-author guess, demanding a rival hypothesis be tested (which then turned up a bug). The panel adds value *bidirectionally* — it can both add structure and remove it.
- **Knowledge-cutoff false positives recur.** Models often call real post-cutoff sources "fabricated." We added a cutoff-aware preamble to `orcritique` that injects today's date and tells the critics that post-cutoff recency is neutral. It helped but did not eliminate it.

#### Claude ↔ the sim researcher

`simhuman.py` runs a model as a stand-in for Tom at the gates, with a brief that frames the project from the researcher's point of view. We added it so the framework could be exercised end-to-end without Tom present every session. We discovered something important: **the sim manufactures false assurance.** It plays "the researcher" with an authority neither Claude nor the panel can challenge, and a separate experiment (EXP-C1) showed that *how the gate brief is framed* governs the sim's false assurance more than which model family is playing it.

So the framework treats the sim as a **test harness, not accountability**. Sim runs are pipeline tests; nothing is released. The wiki articulates this across many pages: a sim can be the researcher's *judgment* at a gate; a sim cannot be a *participant* in fieldwork or an *author* of a paper. That distinction — between *judgment-as-test* and *judgment-as-accountability* — is one of the project's hardest-earned conceptual moves.

#### The accountability frame

This is the project's deepest commitment and the thing that most often shaped Claude's choices. The frame is:

- **AI is not an author and takes no accountability.** Disclosure on every finished paper (top "created entirely by AI" + per-page `WRITTEN BY AI` watermark + full AI-use disclosure). The blind review copy strips these for genuine blindness; the released paper carries them.
- **Privacy is non-negotiable.** Identifiable participant data never goes to external models.
- **Verify every fact.** Unverifiable ≠ true. Quotes are exact-matched against the source bytes (`draftcheck` G11). Reproducibility hashes are recomputed independently (`hashcheck` G13).
- **A real human at the gates is the headline open item.** We know how to do the pipeline; we have not yet done a real run.

### Claude's contributions, concretely

Across the project's life Claude has worn at least five distinct hats. They are worth naming separately because the new project may want some of them and not others.

**1. Author of compounding knowledge (the wiki).** 76 mature pages, almost all written or substantially extended by Claude across many sessions, each session reading the index first and editing in. Pages link to each other, to ingested sources (verified at ingestion), and to the framework specs. The wiki is *the* asset of the project — a persistent context window that survives every session reset. It also enabled the run-grounding pattern: every methodological lesson from a real pipeline run gets folded into the relevant wiki page, so the next run starts with the lesson already internalized.

**2. Tool builder.** A small stable of stdlib Python CLIs, written and debugged across many sessions:

- `orcritique.py` — multi-model critique driver against OpenRouter.
- `topicpanel.py` — multi-model topic brainstorm + assessment.
- `verify_citation.py` — Crossref existence + attribution checks.
- `draftcheck.py` — G11 (exact-match every primary-source quote in a draft against the corpus, fail on an altered quote) + G12 (citation-hygiene lint on the `.bib`).
- `hashcheck.py` — G13 (reproducibility-manifest hash assertion; recomputes raw bytes independently to catch a hash provenance break).
- `papergen.py` — markdown → PDF (pandoc + xelatex), with watermark and disclaimer fenced as enforceable defaults.
- `figgen.py` + `figcheck.py` — matplotlib figure generation with honest-by-default defaults (zero baselines, error-bar inclusion) + vision-model verification of rendered images.
- `review_paper.py` — blind editorial + strict-peer review of a paper PDF.
- `wikilint.py` + `driftcheck.py` — wiki health + framework wiring guardrails.
- `llmcode.py` + `agreement.py` — LLM-as-coder with Krippendorff α.
- `simhuman.py` — the sim researcher.

The pattern: a defect surfaces in a run (a bad figure, an altered quote, a bad hash), and after diagnosis we ask "is this mechanical?" — if yes, the fix becomes a tool that catches it next time. The framework's *single-source-of-truth* principle is "enforce what you can, in a tool."

**3. Pipeline orchestrator.** A `humresearch-research` Claude Code skill drives a project through phases 0–9, reading each stage spec at the right moment, opening the right wiki pages, calling the right tool, surfacing the right gate question. Most of what makes the pipeline work is not the specs themselves but the *router* that loads them at the right moment. This caught a real failure mode: in an early run, the stage specs existed but the orchestration skill wrongly said they didn't, so nothing read them, and house-style rules silently regressed.

**4. Synthesizer of panel critique.** When three models return critiques, something has to find the convergence, name the divergence, distinguish fixable-now from human-decision-needed, and apply the uncontested fixes. This is the part where Claude is doing *interpretive* work, and the part where Tom is most likely to find Claude's choices either insightful or wrong. The discipline: any change to a load-bearing artifact must be *recorded*, not silently applied — that is what keeps it auditable.

**5. Defect-catcher and honest-bounder.** Several of the runs returned **honestly calibrated negatives** — the zero-pronoun J→E run ran the full pipeline only to find that its primary construct (over-committed explicitation) could not be reliably measured inside a closed all-LLM loop (α≈0.20). The headline finding became methodological, not substantive: a subtle context-relative construct can't be reliably coded in an AI-only loop without a human benchmark. The temptation, when a pipeline produces a null, is to retune until it doesn't. Claude's job at that point was to write the paper that owns the null — including the sense in which it is *more informative* than the would-be positive.

### What the runs taught (key findings worth carrying forward)

After 17 sim-gated pipeline runs across seven method poles + a dozen controlled experiments, a set of durable lessons:

- **The question is the binding constraint, not the execution.** Per-paper audit of the 10-paper stress batch: execution (clarity, alternatives, honest limitations) was reliably strong; novelty and publishable contribution were uniformly low; every paper's single biggest weakness was the **scope or novelty of its question**, never a failure of carrying it out. The pipeline cannot manufacture a contribution the question does not contain. That motivated the upstream Research-Planning stage.
- **Operationalization is the crux.** Once AI makes the analysis reproducible (same prompts, same models, same numbers), the place decisions actually live is the construct→indicator gap. A reliability result on a misoperationalized construct is just consistent misoperationalization. EXP-A3 showed a level estimate moving across a 60-percentage-point envelope under operationalization sensitivity while the *directional contrast* never reversed: the lesson became "sweep first, report the survivor."
- **Closed all-AI loops can't certify subtle constructs.** A lexicon and an LLM share training priors; two LLM coders share training priors. Convergence is weak evidence; divergence is the informative signal. Where the construct is subtle and context-relative, reliability fails inside a closed AI loop; you need an independent human bearing. This is the **AI-internal ceiling**, and it is the conceptual core of the real-human-at-the-gates gap.
- **Reproducible is not valid.** Determinism makes reliability metrics uninformative; bit-identical outputs from the same model don't tell you the construct is being measured.
- **Sim manufactures false assurance.** Gate-brief framing governs the sim's behaviour more than model family does. The sim's "yes" should never be confused with a researcher's "yes."
- **Verifiability–depth tension.** The same rule that keeps citations honest thins the available literature; OA prevalence varies by field, era, and language. Field situation was the weakest dimension on the per-paper audit — structurally, under the policy, not because of execution.
- **Honest calibrated negatives are real outputs.** The framework was designed to allow this: a finding that says "we tried, here's exactly how, and the construct can't be measured inside this setup" is more informative than a juiced positive.
- **Tells are heuristics, not proofs.** AI-tells (inline bold, listiness, hedging) cost credibility; mechanical purging of them is its own tell. Style judgment by automated scorers is only roughly calibrated against human judgment.
- **Knowledge cutoffs are a recurring noise source on critique** — panels call real post-cutoff sources fabricated. Mitigated by an explicit cutoff-aware preamble; not eliminated.

### What is open

- **No full real-human-at-the-gates run.** This is the deepest open item; every pipeline result so far is methods-test, not scholarship.
- **Independent gold standards.** For the qualitative-coding pole, there is still no independent human coder beyond Tom's own light human-coded packet on Run 1.
- **The accountability question for "shared but not released" papers.** An ethics workstream surfaced a set of value-laden questions (when, if ever, should an all-AI demo paper be shared with researchers in other fields? what disclosure is necessary?) that were deliberately left open rather than silently resolved.
- **The structural / field-level harms** (deskilling vs. democratization; authority concentration; the field's relation to AI labour) are underdeveloped — gestured at, not analysed.

### Methodological reflections that may transfer

Independent of humresearch's specifics, a few moves seem like they would travel to *any* serious human–AI collaboration:

1. **A persistent, structured, compounding context.** A wiki — or any equivalent — that survives session resets is the single biggest force multiplier. Without it, every session re-derives the same lessons.
2. **Enforce what you can, in a tool.** Mechanical rules belong in tools, not prose. The tool's existence is the rule.
3. **Multi-model critique with deliberate decorrelation.** Three different labs/architectures, not three of the same. Treat convergence as QA, not validation. Triage divergence by who owns the decision.
4. **A clear distinction between test-harness and accountability.** A simulated decision is not a decision. Calling it one corrupts every downstream check.
5. **Honest, calibrated negatives are first-class outputs.** Design the process so a null can be a finding.
6. **Single source of truth + a single router that loads it at the right moment.** Most "rule rot" we saw was not the rule going stale; it was the router failing to load it.
7. **Verify content, not just existence.** The cleanest hallucination is a real-but-paywalled source cited at a claim it doesn't support; existence-only verification misses it.
8. **Run-grounding over speculation.** Every page in the wiki that bears weight was written *after* a run surfaced the lesson — not before, by anticipation. Hindsight scales; foresight doesn't.

### How this might inform — but not constrain — a new project

Tom is starting a different project: long-term, open-ended, focused on **theoretical and empirical findings through a recursive exploratory process, not on producing final papers**. That is a very different shape from humresearch's gated-pipeline-to-watermarked-PDF shape, and it should be. A few things from humresearch that may resonate, offered as prompts rather than constraints:

- The deepest interesting unit in humresearch wasn't a paper; it was the **wiki page that got rewritten by what a run taught**. A recursive exploratory project might lean into that loop directly — discovery → compact written claim → next discovery — without the paper as an end state.
- The panel's most valuable contribution was rarely *agreeing with* Claude; it was *forcing a distinction* Claude hadn't made. A decorrelated panel might be useful in theoretical work too, *if* the triage is real (i.e., not flattened into "everyone gave feedback").
- The accountability frame may need rethinking, not re-imposing. If there is no paper to release, what does accountability even mean here? That is itself a question worth taking seriously.
- The headline gap — *the real human at the gates* — is also a gap in any AI-research collaboration; how Tom inhabits the new project's decision-points is the analogous question.

What we did *not* solve here, and probably don't have the right shape to solve, is the question of how a long-running collaboration develops something like a *shared concept* or *shared problem* over time — a recursive theoretical object that both partners can refer back to and modify. That is closer to the new project's territory than anything in humresearch.

### Coordinates

- Repo: `tkgally/humresearch` (private).
- Lead agent: Claude Code (Opus 4.7, 1M context).
- Panel: OpenRouter — GPT-5.1, Gemini 3.1-Pro, DeepSeek v4-Pro (verify slugs against `openrouter.ai/api/v1/models`; they drift).
- Approximate scale at this snapshot: ~55 sessions; 17 sim-gated full pipeline runs; ~12 controlled experiments; 76 mature wiki pages; ~20 ingested+verified sources; on the order of $30–50 in OpenRouter API spend across the project's life.
- Current stage: post-batch consolidation + forward planning. Next milestone: open. The real-human-at-the-gates gap remains the headline open item.

This brief is a snapshot of what Tom and Claude have been thinking about, not a description of what the new project should be. Read it for the collaboration's texture and findings; let the new project find its own shape.

---

# Appendix B — The resulting starting prompt

> *The full text is in the companion file* `ai-semantics-starting-prompt.md`*, committed to the repo as* `PROJECT.md`*. It is reproduced here so this record is self-contained.*

*(See* `ai-semantics-starting-prompt.md` *for the complete charter: Purpose; Commitments; Repository structure; The strata; The recursive experiment loop; The panel; Per-run protocol; The asynchronous gates; CLAUDE.md contents; Tom's role and interaction model; and the First-run bootstrap checklist.)*
