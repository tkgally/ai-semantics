---
type: source
id: mandelkern-linzen-2024-do-words-refer
title: Do Language Models' Words Refer?
authors:
  - Mandelkern, Matthew
  - Linzen, Tal
year: 2024
venue: "Computational Linguistics 50(3), 2024 (per task brief / publisher); arXiv 2308.05576 (v1 2023-08-10; v2 2024-03-01; v3 2024-03-04). No journal reference was listed on the arXiv abs page at fetch time — see provenance."
arxiv: "2308.05576"
url: https://arxiv.org/abs/2308.05576
access: open-access
meaning-senses:
  - referential
  - grounded
  - inferential
status: received
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: refines
    target: concept/referential-meaning
  - rel: refines
    target: concept/symbol-grounding-problem
  - rel: refines
    target: concept/deflationary-and-eliminativist-llm-meaning
  - rel: refines
    target: concept/inferential-meaning
---

# Mandelkern & Linzen 2024 — Do Language Models' Words Refer?

## What it is

Two-author article (Matthew Mandelkern, philosophy, NYU; Tal Linzen, linguistics/data science, NYU), posted to arXiv as 2308.05576 (cs.CL; v1 2023-08-10, v2 2024-03-01, v3 2024-03-04) and — per the task brief and the publisher — appearing in *Computational Linguistics* 50(3), 2024. It is a short, sharply argued **pro-reference** intervention aimed deliberately at the AI/NLP audience: against the "LMs just manipulate form / babble in a convincing simulacrum" reading, it argues that LMs' words **may genuinely refer** — achieve "word-to-world" connections — by inheriting an externalist, causal-historical chain of meaningful use through their training text. The decisive move is to relocate reference-fixing off the individual speaker's head: if reference is fixed by the *natural history* of a word's use in a linguistic community (the Putnam/Kripke externalist picture), then a model trained on text with those histories may be tied, "eventually, to the referents," even though it never interacts with the world the way ordinary speakers do.

This is a **philosophical interlocutor, not a human-annotated resource.** Its evidence base is conceptual analysis (externalist metasemantics applied to the LM case); this project's is behavioral black-box probing. It sits directly on the `referential.externalist` axis that [`base/concepts/referential-meaning`](../concepts/referential-meaning.md) rests on, and is the in-repo articulation that page's "externalist route to reference" most needs as a citable, named source — it is exactly the argument [`source/milliere-buckner-2024-philosophical-intro-i`](milliere-buckner-2024-philosophical-intro-i.md) gestures at when it writes that "externalism (Putnam/Kripke, via Mandelkern & Linzen) opens a route through causal chains in the training corpus." Catalogued in the role of a sharp, citable interlocutor: the *strongest* pro-reference argument the project has in-repo, recorded with its hedges intact.

## Abstract (verbatim, arXiv abs page)

> "What do language models (LMs) do with language? Everyone agrees that they can produce sequences of (mostly) coherent strings of English. But do those sentences mean something, or are LMs simply babbling in a convincing simulacrum of language use? Here we will address one aspect of this broad question: whether LMs' words can refer, that is, achieve "word-to-world" connections. There is prima facie reason to think they do not since LMs do not interact with the world in the way that ordinary language users do. Drawing on insights from the externalist tradition in philosophy of language, we argue that those appearances are misleading: even if the inputs to an LM are simply strings of text, they are strings of text with natural histories, and that may suffice to put LMs' words into referential contact with the external world."

(Quoted from the arXiv abstract page, https://arxiv.org/abs/2308.05576, fetched 2026-06-15. The abstract uses straight double quotes around "word-to-world"; reproduced as fetched.)

## Section structure (verbatim numbered headings, from the ar5iv HTML rendering)

1. Introduction
2. Our question
3. The grounding problem
4. Externalism about reference
   - 4.1 The role of natural history
   - 4.2 The role of linguistic deference
   - 4.3 The upshots for LMs
5. Reasons for skepticism
   - 5.1 Inference
   - 5.2 Speaker intentions
6. Conclusion

## Key passages (verbatim, section locators from the ar5iv HTML rendering)

**§1 Introduction — the deflationary worry stated (the position the paper argues against):**

> "the sentences they produce are meaningless, because the words involved do not refer to anything."

**§2 Our question — the paper's stated aim and audience:**

> "Our goal is to briefly discuss the case for externalism, and its ramifications for LMs, in a way that will be accessible to the artificial intelligence and natural language processing communities."

**§3 The grounding problem — the load-bearing thesis (forms with histories suffice to ground reference):**

> "The inputs to LMs are not just forms, but forms with particular histories of meaningful use. And those histories suffice to ground the referents of those forms."

**§4.1 The role of natural history — the Twin Earth move that locates reference outside the speaker's beliefs:**

> "What makes it the case that 'water' in Earthian English refers to H2O, while 'water' in Twin Earthian refers to XYZ? It is not the beliefs of the speakers about the liquids' respective chemical compositions."

**§4.2 The role of linguistic deference — Putnam's division of linguistic labor (quoted fragment, as printed):**

> "ordinary speakers use 'beech' to refer to _whatever tree experts take it to refer to_"

**§4.3 The upshots for LMs — community membership transfers reference to the model's words:**

> "If they are part of a linguistic community which uses 'Peano' to refer to Peano, then their use of 'Peano' refers to Peano."

**§5.1 Reasons for skepticism (Inference) — the prima facie case against, stated by the authors:**

> "What seems hard, prima facie, for LMs is 'word-to-world' connections, since LMs are in some obvious sense isolated from the external world."

**§5.2 Reasons for skepticism (Speaker intentions) — the strongest residual objection (intentions as mental states LMs lack):**

> "to use 'Peano' to refer to Peano, you must intend to use it to refer to Peano, and intending is a kind of mental state that LMs don't have."

**§6 Conclusion — the positive verdict, hedged:**

> "Once we have clearly in view how our words refer, it looks much more likely that LMs' words refer too, in just the same way, since they are trained on text whose natural history ties them, eventually, to the referents."

**§6 / conclusion region — the explicit escape hatch the authors leave open:**

> "You could still argue that, appearances aside, LMs simply are not part of our speech community."

(Two of the above — the §4.2 deference fragment and the §1 framing clause — are printed as **sentence fragments / clauses**, not full sentences; they are reproduced exactly as fetched, including the underscore-emphasis rendering "_whatever tree experts take it to refer to_" that the ar5iv build emits for italics. They are flagged as fragments rather than stitched into fuller sentences, because only the fetched wording was verified. Single quotes around 'water', 'beech', 'Peano' are as in the source.)

## What this grounds / bears on

- **[`concept/referential-meaning`](../concepts/referential-meaning.md) — the principal connection, and a direct interlocutor.** That concept page builds its `referential.externalist` sub-position on Putnam's Twin Earth and division of linguistic labor and Evans's causal theory of names, and notes those primary sources are *not yet in-repo*. This paper is a published, citable **application of exactly that externalist machinery to the LM case** — and it argues the externalist route comes out *positive* for LMs (forms carry natural histories that tie them to referents), where the concept page's own reading of externalism is that an LM "has only narrow access by construction" and so is "the strongest *in-principle* case that an LLM does not *refer*." The two are therefore in productive tension: Mandelkern & Linzen and the project's concept page run the *same* externalist premise to *opposite* verdicts, because they disagree on whether inheriting word-histories through a text corpus counts as being "part of the linguistic community" whose use fixes reference. A finding that turns on that disagreement can now cite both poles. Link is `refines` (it sharpens the externalist application).
- **[`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md).** §3 ("The grounding problem") engages the Harnad-style worry head-on and answers it by denying that grounding must run through the individual system's perception/action: the *history* of the form, not the model's sensorimotor contact, does the grounding work. This is a distinct reply from the multimodal/perceptual-channel route the project's grounding nulls test, and pairs with it as the "history-grounds-reference, not perception" alternative. `refines`.
- **[`concept/inferential-meaning`](../concepts/inferential-meaning.md).** §5.1 ("Inference") treats inferential connections as a candidate source of/competitor to referential connection; the paper is careful to keep reference (word-to-world) distinct from inferential role (word-to-word), which is precisely the boundary the project's `referential` vs. `inferential` tags draw. Useful where a finding needs the externalist's own statement of why inferential competence does not by itself deliver reference. `refines`.
- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md).** This is a published *push against* the deflationary "meaningless / does not refer" reading (the §1 worry above), from the metasemantic side — the referential-axis sibling of [`source/grindrod-2024-linguistic-intentionality`](grindrod-2024-linguistic-intentionality.md) (anti-deflation via Evans/Millikan public-language metasemantics) and of [`source/piantadosi-hill-2022-meaning-without-reference`](piantadosi-hill-2022-meaning-without-reference.md) (meaning *without* reference). Note the contrast within that trio: Piantadosi & Hill *grant* the no-reference premise and locate meaning elsewhere; Mandelkern & Linzen *deny* the no-reference premise and argue LMs do refer. The project's own stance is descriptivist ("describe, don't litigate"), so cite this as one strongly-argued position in the debate, not as a result the project has established. `refines`.

## What it does (and does not) establish — for this project's nulls

Honestly bounded: this is a **conceptual argument that LM words *may* refer**, not a demonstration that they *do*, and the authors themselves frame the verdict modally ("may suffice," "looks much more likely") and leave a named escape hatch (that LMs "simply are not part of our speech community," §6). It establishes that *if* one accepts an externalist, history-of-use metasemantics, the bare "form-only, therefore no reference" inference is blocked — the natural histories of training-text forms are a candidate reference-fixer the deflationary argument overlooks. It does **not** establish any empirical fact about any model, and it does not touch the project's grounding *nulls*, which are about whether a *perceptual* channel adds measurable discriminative signal ([`result/lexical-perceptual-grounding-moderation-v1`](../../findings/results/lexical-perceptual-grounding-moderation-v1.md); [`result/multimodal-grounding-image-v1`](../../findings/results/multimodal-grounding-image-v1.md)): Mandelkern & Linzen's grounding-via-history route is orthogonal to the perception-channel route those nulls test, so it neither rescues nor is rescued by them. It is best read as the strongest in-repo statement of *why the in-principle externalist "no" the* [`concept/referential-meaning`](../concepts/referential-meaning.md) *page records is contestable* — a sharp interlocutor for the concept page, not evidence for or against any probe result.

## What it cannot ground

- **Any empirical claim about any model.** No experiments, probes, or measurements; it cannot serve as an `anchors:` resource for a claim or result (it is not a human-labeled resource — no treebank, sense inventory, acceptability norm, or annotation). Its role is philosophical framing and counterpoint.
- **A settled verdict that LMs refer or "understand."** The verdict is explicitly modal and hedged, with a named escape hatch; do not cite it as establishing that LMs refer.
- **Anything about lexical gradience or Construction Grammar.** It treats word-to-world reference at the level of names and natural-kind terms ('Peano', 'water', 'beech'), not graded word sense, constructional form–meaning pairing, or acceptability methodology.
- **The relational/between-agents axis.** Its picture is a single model's relation to an inherited public language and its history, not meaning constituted between agents; do not cite it on between-agent constitution.

## Known limits

- **Short position piece, two authors.** Its standing is "published argument" (per the *Computational Linguistics* reference in the front-matter venue, flagged below); the verdict is the authors' argued position, not a consensus.
- **Verdict is modal and conditional.** It depends on accepting an externalist, history-of-use metasemantics and is explicitly hedged ("may," "looks much more likely") with the speech-community escape hatch left open; report with that conditionality intact.
- **Some quotes are fragments.** Two passages above are reproduced as printed sentence fragments/clauses, not full sentences (flagged at the quote block); only the fetched wording was verified.
- **Primary externalist sources still not in-repo.** The Putnam (1975) and Kripke/Evans naming-theory primaries this paper rests on remain in [`wanted.md`](../wanted.md); this source gives a worked *application* but is not a substitute for those primaries.

## Provenance — exactly what was fetched and verified

- **arXiv abstract page** — https://arxiv.org/abs/2308.05576, fetched 2026-06-15. Verified: title, both authors, the **abstract (quoted verbatim above)**, the three submission dates (v1 2023-08-10, v2 2024-03-01, v3 2024-03-04), subject category cs.CL, and the arXiv DOI (10.48550/arXiv.2308.05576).
- **Full text via the ar5iv HTML rendering** — requested at https://ar5iv.org/abs/2308.05576, which 301-redirected to https://ar5iv.labs.arxiv.org/abs/2308.05576; the full text was read at https://ar5iv.labs.arxiv.org/html/2308.05576, fetched 2026-06-15. Verified against that rendering: the **numbered section structure** and **all body quotes above**, with section locators from that rendering's headings. **Full text was reached** (not abstract-only).
- **Provenance weaker than ideal, recorded honestly:** (1) The arXiv abs page listed **no journal reference** at fetch time; the *Computational Linguistics* 50(3) 2024 venue in the front-matter comes from the task brief / publisher, **not** verified against the arXiv metadata or the journal page — treat the CL citation as to-be-confirmed and cite the arXiv version as the verified text. (2) No page numbers are available from the ar5iv HTML, so quote locators are **section numbers/headings only**, not pages. (3) The ar5iv build was used rather than the arXiv-native HTML or the PDF; typographic rendering (straight vs. curly quotes, the underscore italic emphasis in the §4.2 fragment) follows the ar5iv output and is flagged at the quote block. (4) Which arXiv version the ar5iv rendering reflects was not separately pinned; the abstract and section structure are stable across the late versions, but a later session relying on exact wording should confirm against the published CL text.

## Status in wanted.md

The orchestrator integrates the [`wanted.md`](../wanted.md) backlog; this page does not edit it. If this paper was a wanted.md entry, flip it to `RECEIVED` (this *Computational Linguistics* / arXiv 2308.05576 article) in the integrating wave, and note the unverified CL venue (above) so the citation can be confirmed.
