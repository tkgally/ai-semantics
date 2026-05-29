---
type: source
id: mahowald-2023-aann-judgments
title: "A Discerning Several Thousand Judgments: GPT-3 Rates the Article + Adjective + Numeral + Noun Construction"
authors:
  - Mahowald, Kyle
year: 2023
venue: "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2023), Dubrovnik, Croatia, pp. 265–273"
arxiv: "2301.12564"
doi: "10.18653/v1/2023.eacl-main.20"
url: https://aclanthology.org/2023.eacl-main.20/
access: open-access
meaning-senses:
  - constructional
  - functional-vs-formal
  - human-comparison
status: received
created: 2026-05-29
updated: 2026-05-29
pdf-pages: "ACL Anthology 2023.eacl-main.20 (PDF, pp. 265–273) for title/venue/abstract; abstract verbatim from the ACL Anthology page and arXiv 2301.12564; body section quotes read from the ar5iv HTML rendering (ar5iv.labs.arxiv.org/html/2301.12564), cited by section name, no page numbers in HTML"
links:
  - rel: supports
    target: concept/constructional-meaning
  - rel: supports
    target: claim/formal-competence-aann-ceiling
  - rel: supports
    target: conjecture/aann-construction
---

# Mahowald 2023 — A Discerning Several Thousand Judgments: GPT-3 Rates the AANN Construction

## What it is

Single-author empirical paper by Kyle Mahowald (University of Texas at Austin), published at EACL 2023 (pp. 265–273), arXiv 2301.12564, DOI 10.18653/v1/2023.eacl-main.20. It prompts GPT-3 (`text-davinci-002`) to give acceptability judgments on the English **Article + Adjective + Numeral + Noun (AANN)** construction (e.g. *a lovely five days*), validates the prompting measure on the CoLA acceptability corpus, and compares GPT-3's judgments both to crowdsourced human judgments and to the constraints on AANN proposed in the linguistics literature.

This page is the **argument-and-findings** record for the paper. The paper's **dataset** — the templatic stimulus generator, the slot-filler tables, the MTurk acceptability ratings, and the GPT-3 rating data — is catalogued separately as the resource page [`resource/mahowald-2023-aann-stimuli`](../resources/mahowald-2023-aann-stimuli.md). Division of labor: **this page** summarizes what the paper claims and finds and supplies its verbatim provenance; **that page** holds the dataset/stimulus structure and is the human-anchor (`anchors`) resource. Stimulus templates and slot-filler inventories are not duplicated here — see the resource page for those.

## Summary

The paper frames the AANN construction as a test case for whether an LLM has learned a "rare, idiosyncratic construction" against the grain of frequency bias. The method is behavioral: GPT-3 is prompted for a "good"/"bad" acceptability judgment, the prompt is first validated on the CoLA dev set, and then GPT-3 is run over a templatically generated AANN stimulus suite spanning several proposed constraints (adjective type, noun type, numeral, article, modifier-presence, and ordering). GPT-3's gradient is compared against crowdsourced human acceptability ratings on a subset and against the constraints named in the AANN literature.

Headline finding: GPT-3's judgments are "broadly similar to human judgments and generally align with proposed constraints in the literature," but in some cases GPT-3 and the human raters diverge both from the literature and from each other. The paper's framing in the conclusion is explicitly cautious about what this licenses: recognizing and using the *form* of the construction in a human-like way "is not the same thing as showing that it understands the meaning or function of the construction." This formal-vs-meaning hedge is exactly the wedge that [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md) builds on, and the paper is the empirical instance behind [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md).

## Key passages

The abstract is quoted verbatim from the ACL Anthology page (https://aclanthology.org/2023.eacl-main.20/, fetched 2026-05-29), cross-checked against the arXiv abstract (arxiv.org/abs/2301.12564). Body passages were read from the ar5iv HTML rendering (https://ar5iv.labs.arxiv.org/html/2301.12564, fetched 2026-05-29) and verified character-for-character; the HTML carries no page numbers, so body quotes are cited by section.

**Abstract (verbatim, ACL Anthology / arXiv) — design and headline result:**

> "Knowledge of syntax includes knowledge of rare, idiosyncratic constructions. LLMs must overcome frequency biases in order to master such constructions. In this study, I prompt GPT-3 to give acceptability judgments on the English-language Article + Adjective + Numeral + Noun construction (e.g., "a lovely five days"). I validate the prompt using the CoLA corpus of acceptability judgments and then zero in on the AANN construction. I compare GPT-3's judgments to crowdsourced human judgments on a subset of sentences. GPT-3's judgments are broadly similar to human judgments and generally align with proposed constraints in the literature but, in some cases, GPT-3's judgments and human judgments diverge from the literature and from each other."

**§Introduction (verbatim, ar5iv HTML) — the central question:**

> "Here, I ask what GPT-3 text-davinci-002 (now often classed as an instance of GPT-3.5) learns about the AANN construction by testing its sensitivity to several constraints proposed in the literature."

**§Methods (verbatim, ar5iv HTML) — prompt validation on CoLA:**

> "To validate the measure, I tested the final prompt on the CoLA dev set. It attained accuracy of 84%, with a Matthew's correlation coefficient of 0.63."

**§Conclusion (verbatim, ar5iv HTML) — the form-vs-meaning takeaway:**

> "This work shows that GPT-3 can recognize and use the form of the AANN construction in a relatively (but not perfectly) human-like way, matching judgments across a variety of conditions, which is not the same thing as showing that it understands the meaning or function of the construction (Mahowald et al., 2023)."

(The trailing parenthetical "(Mahowald et al., 2023)" is an in-text citation marker in the original; the cited reference is a separate Mahowald et al. work, not this single-author paper.)

## What it can ground

- The AANN-specific behavioral findings: that GPT-3 (`text-davinci-002`) gives acceptability judgments on AANN that are broadly similar to crowdsourced human judgments and broadly align with the constraints proposed in the AANN literature, with documented divergences. This is the **argument** behind the dataset on [`resource/mahowald-2023-aann-stimuli`](../resources/mahowald-2023-aann-stimuli.md).
- The `functional-vs-formal` reading drawn by [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md): the paper's own conclusion distinguishes recognizing/using the *form* of the construction "in a relatively (but not perfectly) human-like way" from "showing that it understands the meaning or function of the construction." The acceptability-as-formal-competence line has the author's own framing behind it.
- The prompt-on-CoLA validation method (84% accuracy, MCC 0.63 on the CoLA dev set) as a method precedent for prompted acceptability judgments — relevant to the operationalization decision recorded in [`decisions/open/aann-operationalization`](../../decisions/open/aann-operationalization.md).
- The model-vs-human comparison pattern on a single construction, as a `human-comparison` exemplar.

## What it cannot ground

- Claims about any model other than GPT-3 `text-davinci-002`: this is a single-model study (with CoLA validation). Newer-model AANN behavior is out of scope.
- Claims about constructions other than AANN, or AANN in languages other than English.
- Representational or mechanistic claims: the evidence is prompted behavioral acceptability rating, not probing of internal representations — it does not ground `model-internal` claims.
- Claims that GPT-3 tracks the *meaning* or *function* of AANN: the paper explicitly disclaims this inference. A ceiling on form-acceptability is, by the author's own statement, "not the same thing" as meaning-understanding.
- Exact per-condition magnitudes, the full slot-filler inventory, the MTurk rater counts, and the gradient figures: those are dataset-level facts held on [`resource/mahowald-2023-aann-stimuli`](../resources/mahowald-2023-aann-stimuli.md), not transcribed here.

## Meaning-sense justification

- `constructional` — the paper's object is a form–meaning pairing (the AANN construction) in the CxG sense; supports [`concept/constructional-meaning`](../concepts/constructional-meaning.md).
- `functional-vs-formal` — the paper's own conclusion turns precisely on the form-vs-meaning/function line, making it the empirical hook for [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md).
- `human-comparison` — the finding's force comes from setting GPT-3 judgments against crowdsourced human acceptability ratings and the linguistics literature's proposed constraints.
- (`distributional` not tagged: the paper's measure is prompted acceptability, not surprisal/co-occurrence structure, so a distributional tag would overclaim.)

## Status in wanted.md

`received`: abstract verbatim from the ACL Anthology page (cross-checked against arXiv 2301.12564), plus three section-level body quotes (Introduction, Methods, Conclusion) verbatim from the ar5iv HTML, all fetched and verified character-for-character on 2026-05-29. Venue, page range (265–273), and DOI confirmed from the ACL Anthology. The dataset/stimuli are catalogued separately at [`resource/mahowald-2023-aann-stimuli`](../resources/mahowald-2023-aann-stimuli.md). The camera-ready PDF (pp. 265–273) remains available for page-level provenance on body passages if a finding needs it.
