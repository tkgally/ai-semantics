---
type: source
id: du-2023-shortcut-learning
title: "Shortcut Learning of Large Language Models in Natural Language Understanding"
authors:
  - Du, Mengnan
  - He, Fengxiang
  - Zou, Na
  - Tao, Dacheng
  - Hu, Xia
year: 2023
venue: "*Communications of the ACM* 67(1):110–120 (2023, Review Article). Preprint arXiv:2208.11857 (cs.CL, cs.LG), submitted 2022-08-25; ar5iv HTML used for body quotes."
arxiv: "2208.11857"
doi: 10.1145/3596490
url: https://arxiv.org/abs/2208.11857
access: open-access
meaning-senses:
  - distributional
  - functional-vs-formal
status: received
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: depends-on
    target: concept/distributional-meaning
---

# Du, He, Zou, Tao & Hu 2023 — Shortcut Learning of Large Language Models in Natural Language Understanding

## Why this is in-repo (the specific obligation it discharges)

This survey is the **primary "shortcut" source** that [`source/cao-2025-distinctive-cooccurrence-antonymy`](cao-2025-distinctive-cooccurrence-antonymy.md)
cites (§5: "models might take advantage of those intra-sentential co-occurrence characteristics,
**using them as a shortcut Du et al. (2023)** rather than relying on knowledge of antonymy"). It is
ingested to discharge **revision trigger (d)** of
[`essay/shortcut-vs-competence-mis-cut`](../../findings/essays/shortcut-vs-competence-mis-cut.md),
which was left live precisely for this reading: *"if the primary turns out to mean by 'shortcut'
something closer to 'local cue-use' already, the essay's correction is partly pre-empted and should
credit it."* The verdict (see "What this bears on in-repo" below, and the essay's revised §"Prior art"):
**trigger (d) fires partially** — Du et al.'s shortcut/robust contrast *is* a generalization-scope
(in-distribution-vs-OOD) axis, so the essay's reframing of the contrast as generalization-scope is
**anticipated and now credited**; but Du et al. ties the transferable/robust pole to "high-level
semantic understanding" that "pure data-driven training" is "insufficient" for, which is exactly the
non-distributional baseline the essay corrects — so on its **load-bearing** point the essay is **not**
pre-empted, and Du et al. is a **foil**, not a forerunner.

## What it is

A peer-reviewed **review article** (Communications of the ACM 67(1):110–120, 2023; preprint
arXiv:2208.11857, submitted 2022-08-25) by **Mengnan Du, Fengxiang He, Na Zou, Dacheng Tao, and Xia
Hu**. It surveys the **shortcut-learning and robustness problem** for language models in natural
language understanding (NLU): the concepts, detection methods, origins, and mitigation, plus future
directions and a prompt-based-paradigm coda. It is a **methodology/critique source about model
behavior**, **not** a human-annotated resource and **not** a result about the project's panel
(BERT/RoBERTa-generation models are the running examples). It bears on the project as the conceptual
origin of the "shortcut" framing the lexical wedge inherited second-hand through Cao et al.

## Provenance

Title, full author list, submission date (2022-08-25), subject categories (cs.CL, cs.LG), CACM
acceptance note, and **license (Creative Commons Attribution 4.0, CC BY 4.0)** were read from the
arXiv abs page (https://arxiv.org/abs/2208.11857) on 2026-06-30. Because the paper is **CC BY 4.0**,
verbatim quotation (and even verbatim mirroring) is permitted with attribution. **All body quotes
below are taken from the ar5iv HTML full text (https://ar5iv.labs.arxiv.org/html/2208.11857)**,
fetched and stripped to text on 2026-06-30 and verified character-for-character; quote locators are
the **section numbers/headings from that HTML** (no CACM print page numbers were taken from the open
HTML). One typographic apostrophe in the §8 quote ("survey's") is the source's curly `’`, reproduced
as-is.

## Abstract (verbatim, from the ar5iv HTML)

> "Large language models (LLMs) have achieved state-of-the-art performance on a series of natural
> language understanding tasks. However, these LLMs might rely on dataset bias and artifacts as
> shortcuts for prediction. This has significantly affected their generalizability and adversarial
> robustness. In this paper, we provide a review of recent developments that address the shortcut
> learning and robustness challenge of LLMs. We first introduce the concepts of shortcut learning of
> language models. We then introduce methods to identify shortcut learning behavior in language
> models, characterize the reasons for shortcut learning, as well as introduce mitigation solutions.
> Finally, we discuss key research challenges and potential research directions in order to advance
> the field of LLMs."

## How it defines "shortcut" (verbatim; §2.1 "What is Shortcut Learning?")

The definition is built on a **non-robust-vs-robust feature** contrast:

> "Shortcut learning refers to the phenomenon that LLMs (especially those trained with standard
> ERM-based method) highly rely on non-robust features as shortcuts, failing to learn robust features
> and capture high-level semantic understanding and reasoning." (§2.1)

Crucially, the survey is explicit that a shortcut (non-robust) feature is **a genuine, locally-working
statistical feature**, not "no feature at all" — it works **in-distribution** and fails **out of
distribution**:

> "Non-robust features do help generalization for development and test sets that share the same
> distribution with training data. However, they cannot generalize to OOD test sets and are vulnerable
> to adversarial attacks. Non-robust features are oriented from biases in the training data and come in
> different formats." (§2.1)

And the **robust pole** is defined as **high-level semantic understanding**:

> "In contrast, robust features denote features of high-level semantic understanding that are robust to
> changes in the input." (§2.1)

The Introduction states the same idea as reliance on spurious correlations / dataset artifacts:

> "LLMs have learned to rely on dataset artifacts and biases and capture their spurious correlations
> with certain class labels as shortcuts for prediction." (§1)

## The contrast is a generalization-scope (IID vs OOD) axis (verbatim; §2.2)

The "challenge" the shortcut concept names is a **generalization gap between in-distribution and
out-of-distribution** test data:

> "A common assumption is that training and test data are independently and identically distributed
> (IID)." (§2.2)

> "When LLMs are deployed in real-world applications with distribution shifts, this IID assumption will
> not hold any longer." (§2.2)

> "Using BERT-base as an example, there is a more than 20% reduction in accuracy on the OOD test set
> compared to the accuracy on the in-distribution test sets for NLU tasks" (§2.2)

So a "shortcut" is operationally **a feature that works on the in-distribution split but does not
transfer to OOD** — i.e., the contrast Du et al. draws is, structurally, a **local (IID) vs
transferable (OOD) generalization-scope** distinction.

## The survey's bottom line: pure data-driven training is "insufficient" for the robust pole (verbatim)

The survey concludes that **distributional / data-driven training alone cannot reach** the robust
(high-level-understanding) pole, and recommends **adding non-data-driven domain knowledge**:

> "As a result, it is preferable to combine the data-driven scheme with domain knowledge by
> incorporating knowledge at various stages of training." (§6.1 "Introducing More Domain Knowledge")

> "In the future, the data-driven paradigm should be combined with domain knowledge at every stage of
> model design and evaluation to advance the field of LLMs." (§6.1)

> "The key takeaways from this survey’s analysis are that the current pure data-driven training
> paradigm for LLMs is insufficient for high-level natural language understanding." (§8 Conclusions)

This is the load-bearing point for the in-repo bearing below: Du et al. places the
transferable/robust pole **outside** what pure distributional training reaches, treating it as a
different *kind* of thing ("understanding and reasoning") rather than a more-general distributional
feature.

## What this bears on in-repo

- **[`essay/shortcut-vs-competence-mis-cut`](../../findings/essays/shortcut-vs-competence-mis-cut.md)
  — discharges revision trigger (d); the essay now `depends-on` this page.** Two findings, opposite
  signs, neither of which retracts the essay:
  1. **Partial pre-emption → credit owed.** Du et al.'s shortcut/robust contrast is a
     **generalization-scope (IID-vs-OOD)** axis: a shortcut is reliance on non-robust features that "do
     help generalization for … the same distribution" (they work **locally**) but "cannot generalize to
     OOD" (they do not **transfer**) (§2.1). That is, structurally, the essay's **local-vs-transferable** cut,
     and the shortcut-learning literature already locates the contrast there — and already knows a
     shortcut is a *locally-working feature*, not "no knowledge." So the essay's **reframing of the
     contrast as generalization-scope (rather than knowledge-presence)** is **anticipated** by the
     primary and should be credited, not presented as wholly novel. This is the pre-emption trigger (d)
     anticipated.
  2. **The essay's load-bearing correction is NOT pre-empted; Du et al. is a foil for it.** The
     essay's distinctive claim is that **both** poles are **distributional** — the transferable pole is
     an abstracted contrast direction that *travels*, still a creature of the corpus — so a
     co-occurrence control grades *locality*, not *distribution-vs-not*. Du et al. holds the **opposite**
     on exactly this axis: it defines robust features as "**high-level semantic understanding**" (§2.1)
     and concludes "**pure data-driven training … is insufficient for high-level natural language
     understanding**" (§8), recommending non-data-driven "**domain knowledge**" (§6.1). It thus locates
     the transferable/robust pole *outside* distribution — a concrete instance of the very mis-cut the
     essay names (treating "shortcut vs robust" as "distributional vs understanding-beyond-distribution").
     So on its load-bearing point the essay stands, and Du et al. sharpens it as a worked example.
  - **Scope caveat to keep:** Du et al. is about **supervised NLU classification** (NLI/QA/reading
    comprehension) under **fine-tuning/ERM**, with a *task-defined* "intended solution," and its
    examples are **BERT/RoBERTa-generation** models. The project's wedge is **lexical-relation
    recovery** on a **frontier panel** against a **co-occurrence control**, with no task-supervised
    "correct" label in the same sense. The generalization-scope analogy (local/IID vs transferable/OOD)
    transfers cleanly; the supervised "spurious-vs-causal-feature" machinery transfers only loosely.
    Do **not** read Du et al. as a result about the panel or as a human anchor.
- **[`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md)
  — context only.** The conjecture's blocked control is "the shadow" operationalized as a co-occurrence
  baseline; Du et al. supplies the prior-art language for *why* a model might lean on such co-occurrence
  ("shortcut"), but it does **not** unblock the conjecture, supply a human anchor, or transfer a panel
  result. (No typed link added; the bearing is the essay's, which the conjecture's falsifier already
  reflects post-s151.)

## What it can ground

- A citation that the **"shortcut" framing the project inherited (via Cao et al.) is, in its primary,
  a generalization-scope notion**: a shortcut is a **non-robust feature that works in-distribution but
  fails to generalize to OOD** (§2.1–§2.2, verbatim), explicitly *not* "no feature."
- A citation that the shortcut-learning literature's **robust pole is defined as "high-level semantic
  understanding"** and that the survey judges **"pure data-driven training … insufficient"** for it,
  recommending **domain knowledge** beyond the data-driven scheme (§2.1, §6.1, §8, verbatim) — i.e.
  prior art that locates the transferable pole *outside* distribution.
- The verbatim Du et al. definition of shortcut learning (§2.1), for any future page that needs the
  primary rather than Cao et al.'s one-clause secondary deployment of it.

## What it cannot ground

- **Any claim about the project's panel.** Running examples are BERT-base and similar; no
  claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash result is present.
- **A human anchor.** It is a survey of model behavior and methods; there is no human-annotated
  comparison dataset here. It cannot serve as an `anchors:` resource.
- **A lexical-relation or antonymy result.** Its tasks are sentence-level NLU classification (NLI/QA/
  reading comprehension), not lexical-relation recovery; the antonymy application is the project's
  interpretive bridge (via Cao et al.), not a Du et al. finding.
- **A settled verdict on whether the "robust" pole is non-distributional.** The survey *asserts* a
  data-driven-insufficiency takeaway; it does not *demonstrate* that robust features are
  non-distributional. The project reads its "understanding"/"domain knowledge" framing as a **stance**
  the essay contests, not as established fact.

## Known limits

- **Survey, not a primary experiment of its own.** Numbers (e.g. the BERT-base >20% IID→OOD drop, §2.2)
  are reported from cited works, not produced here.
- **Pre-frontier model generation.** The 2022 vintage means its examples predate the project's panel.
- **CACM print pagination not cross-checked.** Body quotes are from the ar5iv HTML; section locators
  are HTML section numbers, not CACM page numbers. The abstract and definitional quotes were verified
  character-for-character against the ar5iv text.

## Status in wanted.md

Not previously listed by id in `wanted.md`; surfaced in [`NEXT.md`](../../../NEXT.md) and in
[`essay/shortcut-vs-competence-mis-cut`](../../findings/essays/shortcut-vs-competence-mis-cut.md)'s
**revision trigger (d)** as the **Du et al. (2023) "shortcut" source Cao et al. cite**. **RECEIVED
2026-06-30 (session 152)** — a `[methodology]` entry was added to `wanted.md` recording the ingest;
trigger (d) discharged (partial pre-emption — credited; the essay's load-bearing claim not pre-empted).
