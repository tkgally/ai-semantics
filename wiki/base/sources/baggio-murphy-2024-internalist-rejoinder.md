---
type: source
id: baggio-murphy-2024-internalist-rejoinder
title: "On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen"
authors:
  - Baggio, Giosuè
  - Murphy, Elliot
year: 2024
venue: "Preprint, arXiv:2406.00159 (cs.CL), submitted 2024-05-31. Framed as a commentary/rejoinder to Mandelkern & Linzen 2024; no journal reference listed on the arXiv abs page at fetch time — see provenance."
arxiv: "2406.00159"
url: https://arxiv.org/abs/2406.00159
access: open-access
meaning-senses:
  - referential
  - inferential
status: received
created: 2026-06-15
updated: 2026-07-05
links:
  - rel: contradicts
    target: source/mandelkern-linzen-2024-do-words-refer
  - rel: depends-on
    target: concept/referential-meaning
  - rel: refines
    target: concept/referential-meaning
---

# Baggio & Murphy 2024 — On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen

## What it is

A short commentary / rejoinder by Giosuè Baggio (Norwegian University of Science and Technology) and Elliot Murphy (UTHealth Houston), posted to arXiv as 2406.00159 (cs.CL; submitted 2024-05-31), replying directly to [`source/mandelkern-linzen-2024-do-words-refer`](mandelkern-linzen-2024-do-words-refer.md) (M&L). It is the **published rebuttal from the internalist side** that the project's referential-meaning concept and the sixth essay had been missing: where M&L run an externalist, causal-historical metasemantics to a *positive* verdict (LMs' words may refer because training-text forms carry natural histories), Baggio & Murphy argue from the internalist tradition of theoretical linguistics and philosophy of language (Chomsky, Jackendoff, Pietroski) that the verdict is at best valid for a **narrow class** of expressions and that, more deeply, **neither LMs nor "their words" refer** — because reference, where it occurs at all, is a function of speakers' mental/cognitive states, not of word-histories in a corpus.

This is a **philosophical interlocutor, not a human-annotated resource.** Its evidence base is conceptual argument; it makes no measurements and cannot anchor any claim or result. Its in-repo role is to contest, from the internalist pole, the strongest in-repo pro-reference argument (M&L) — directly servicing revision-trigger **(d)** of the sixth essay [`essay/reference-as-premise-bound`](../../findings/essays/reference-as-premise-bound.md), which asked for "a published rebuttal to Mandelkern & Linzen … contesting the natural-histories-suffice move or the corpus-membership reading specifically." Baggio & Murphy contest **both**.

## Section structure (verbatim numbered headings, from the arXiv PDF)

1. Summary of Mandelkern & Linzen (2024)
2. Machines under public scrutiny: Why reference matters
3. "Words"? What words?
4. Deeper problems with externalism
5. Crawl out through the fallout: Machines in linguistic communities

## Key passages (verbatim, section locators from the arXiv PDF)

**§1 Summary — the dual move (qualify, then dispute scope): the central structuring thesis:**

> "In this commentary, we first qualify M&L's claim as applying to a narrow class of natural language expressions. Thus qualified, their claim is valid, and we emphasise an additional motivation for that in Section 2. Next, we discuss the actual scope of their claim, and we suggest that the way they formulate it may lead to unwarranted generalisations about reference in LMs."

**§3 "Words"? What words? — the narrow-vs-wide-class objection (the externalist analysis only fits a narrow class of words):**

> "There are causal histories of usage for all words in a language, and there is a variety of ultimate anchors for those histories. Not all such anchors are of the ontological types that externalism favours."

**§3 — the bound on externalist logic, stated as a thesis:**

> "Externalist logic then applies to an important but narrow class of expressions."

**§4 Deeper problems with externalism — the head-on attack on M&L's "natural history" grounding move:**

> "This concept of 'natural histories' cannot be subject to much interrogation given its artificial nature, particularly in the context of machine language, as there appears to be nothing natural, nor historical, about linear strings of tokens, as considered by current tokenisation algorithms."

**§4 — the meta-internalist counter-thesis (mind-brain facts, not word-histories, determine what fixes reference):**

> "Facts about the mind-brain must be invoked to explain how words refer: not what they refer to, but what determines what they refer to (Block 1987; Carey 2009; Baggio 2018)."

**§4 — the bottom-line verdict on whether LM words refer:**

> "Neither language models themselves can refer, and nor can 'their words' refer."

**§5 Crawl out through the fallout — the community-membership rebuttal (extending "linguistic community" to LMs does not settle the issue):**

> "Extending the notion of 'linguistic community member' to include LMs can be a valuable conceptual engineering exercise, but it does not address the issue whether LMs have the required status in our communities, such that some of their 'words' can refer in the ways envisaged by externalist theories."

**§5 — the positive residue they will grant (aboutness, not reference):**

> "Aboutness is more directly applicable to LMs than reference: LMs' performance in topic modelling tasks is easily explained by positing internal states that are less problematic philosophically, and that do not invite unwarranted comparisons to human cognition."

(Single quotes around 'Peano', 'natural histories', 'words', 'linguistic community member', curly apostrophes, and the British spelling "generalisations" are reproduced as printed in the PDF. The §4 verdict and §5 aboutness lines are full sentences; all quotes above are full sentences.)

## What this grounds / bears on

- **[`source/mandelkern-linzen-2024-do-words-refer`](mandelkern-linzen-2024-do-words-refer.md) — the principal connection: a direct, published `contradicts`.** Baggio & Murphy accept M&L's argument *only* for "a narrow class of natural language expressions" (proper names, natural-kind terms) and dispute that it generalises; they then reject even the narrow grounding move, arguing the "natural histories" of tokenised training text are neither natural nor historical (§4), and that reference is fixed by mind-brain states, not corpus word-histories. Their explicit bottom line — "Neither language models themselves can refer, and nor can 'their words' refer" (§4) — directly opposes M&L's modal "yes." This is the published pole-against-pole the project needed: M&L and Baggio & Murphy run *opposite* metasemantics (externalist vs. internalist) to opposite verdicts on the same case. Link is `contradicts` (it makes M&L's positive conclusion less likely).
- **[`concept/referential-meaning`](../concepts/referential-meaning.md) — it instantiates the page's own internalism/externalism axis with a live published voice on the internalist side.** That concept page already frames the LLM as "an unusually clean instance of the *narrow* case" and notes the internalist verdict is "gentler but thinner" ("yes, but narrow"). Baggio & Murphy are a published, citable statement of exactly that internalist position applied to LMs — but pushed harder than the concept page's neutral framing: they conclude *not even narrow reference* for LMs, granting only "aboutness" (§5). They also flag that even *first-order* externalism would leave "meta-internalism" applicable (§4), a distinction the concept page can now cite. Links are `depends-on` (the rebuttal presupposes the internalism/externalism machinery the concept page lays out) and `refines` (it sharpens the internalist application to the LM case). The concept page's standing observation — that the externalist primaries (Putnam 1975, Evans 1973) remain not-in-repo — is unchanged by this source; Baggio & Murphy cite Kripke 1980, Chomsky 2000, Pietroski, Jackendoff, etc., none of which are in-repo either, so their internalist citations are likewise characterizations here, not in-repo primaries. *(Correction, 2026-07-05, s183: Putnam 1975 and Evans 1973 have since been ingested at primary strength — [`source/putnam-1975-meaning-of-meaning`](putnam-1975-meaning-of-meaning.md), session 110, and [`source/evans-1973-causal-theory-of-names`](evans-1973-causal-theory-of-names.md), session 111 — and the concept page updated; Kripke 1980 and Chomsky 2000 remain wanted, so Baggio & Murphy's own internalist citations stay characterization-strength here.)*
- **[`essay/reference-as-premise-bound`](../../findings/essays/reference-as-premise-bound.md) — it feeds revision-trigger (d) directly.** That essay frames M&L as "the strongest in-repo pro-reference statement" whose force depended on being *uncontested in-repo*. With this rebuttal catalogued, that pole is now contested in-repo: the essay's trigger (d) condition ("If a published rebuttal to Mandelkern & Linzen is catalogued") is met, and the essay can be revised to re-state the pro-reference pole at its new, contested strength. (This source page does not edit the essay; it records that the trigger now fires.)
- **[`concept/inferential-meaning`](../concepts/inferential-meaning.md) (lighter touch).** Baggio & Murphy's positive proposal — that lexical items are "algorithms that can instruct cognitive brain systems" and that language provides "truth-indications, rather than truth-evaluations" (§4) — is an internalist, broadly conceptual-role picture of meaning that sits near the inferential/internalist family, though they do not use inferentialist vocabulary. Co-tagged `inferential` for that reason; no typed link, as the connection is thematic, not a sharpening of the inferential concept.

## What it does (and does not) establish — for this project

Honestly bounded: this is a **conceptual rebuttal**, not evidence about any model. It establishes that the externalist route M&L take is contested in the published literature from a well-developed internalist tradition, and it supplies a citable counter-thesis: that (a) M&L's argument, even if granted, covers only a narrow class of expressions (names, natural-kind terms), not indexicals, abstract nouns, most adjectives, etc. (§3); (b) the "natural histories" of tokenised text are a poor fit for the causal-historical machinery, since tokenisers cut across the units (morphemes, words) that could bear histories (§4); and (c) reference, where it occurs, is determined by speakers' cognitive states, which LMs lack — so neither LMs nor their words refer, though their outputs can be *about* subject matters (§5). It does **not** establish any empirical fact about any model, and the project's own descriptivist stance ("describe, don't litigate") means this should be cited as one strongly-argued position, not as a verdict the project endorses. It does not touch the project's grounding *nulls* (perceptual-channel results), which are orthogonal to this metasemantic dispute.

## What it cannot ground

- **Any empirical claim about any model.** No experiments, probes, or measurements; not a human-labeled resource — cannot serve as an `anchors:` resource.
- **A settled verdict that LMs do not refer.** It is an argued position resting on internalist premises (Chomsky/Pietroski/Jackendoff lineage) that are themselves contested; cite it as the internalist pole, not as established fact. Note also that M&L thanked the authors for comments (§Acknowledgements), so the exchange is collegial, not adjudicated.
- **Anything about lexical gradience or Construction Grammar.** Like M&L, it works at the level of names, natural-kind terms, indexicals, and a few adjective types; it does not bear on graded word sense, constructional form–meaning pairing, or acceptability methodology.
- **The relational/between-agents axis.** Its picture is a single model's (lack of) relation to mind-external referents and to a linguistic community; not meaning constituted between agents.

## Known limits

- **arXiv preprint, peer-review status unconfirmed.** The arXiv abs page listed no journal reference at fetch time; standing is "published preprint / commentary," not a journal version of record. The Acknowledgements note thanks to Mandelkern and Linzen for comments, indicating a circulated reply rather than an independent adversarial review.
- **Internalist premises are themselves contested.** The rebuttal's force depends on accepting a Chomskyan/internalist metasemantics; report the verdict with that conditionality, exactly as M&L's positive verdict is reported as conditional on externalism.
- **No page numbers.** The arXiv PDF carries printed page numbers (1–12) but the body quotes above are located by **section number/heading**, which is the more stable locator; treat locators as section-level.
- **Internalist primaries not in-repo.** Kripke 1980, Chomsky 2000, Pietroski 2017/2018, Jackendoff 2002, Baggio 2018 etc. are cited by the authors but are not in-repo; this source is a worked *application*, not a substitute for those primaries (Chomsky 2000 and the externalist primaries are already queued in [`wanted.md`](../wanted.md)).

## Provenance — exactly what was fetched and verified

- **arXiv abstract page** — https://arxiv.org/abs/2406.00159, fetched 2026-06-15. Verified: title, both authors, the central-thesis framing (qualify-then-dispute-scope), and the closing comment on linguistic-community membership.
- **Full-text PDF** — https://arxiv.org/pdf/2406.00159, fetched 2026-06-15. The PDF is binary; it was saved locally by the fetch tool and the full text was extracted with **pdfminer (v20260107)**. Verified against that extraction: the **numbered section structure** (§§1–5) and **all body quotes above**, character-for-character against the extracted text. Full text was reached (not abstract-only).
- **Provenance notes, recorded honestly:** (1) The arXiv abs page listed **no journal reference** at fetch time — treat standing as a preprint/commentary; cite the arXiv version as the verified text. (2) Quote locators are **section numbers/headings only**, not page numbers, because section locators are more robust than the pdfminer page mapping. (3) Typographic rendering (curly vs. straight quotes/apostrophes, British spelling) follows the PDF text as extracted and is flagged at the quote block. (4) The first WebFetch of the PDF could not parse the binary stream and returned a paraphrase only; that paraphrase was **discarded** — every quote above comes from the pdfminer extraction of the actual PDF bytes, not from any fetch-tool paraphrase.

## Status in wanted.md

This paper was **not** an existing `wanted.md` entry (neither Baggio & Murphy 2024 nor any M&L rebuttal was listed). Proposed orchestrator edit: under "Current wave on LLMs and meaning," add a **RECEIVED** entry recording this source, and add the *other* candidate rebuttal — **Ostertag, G. 2025, "Language Models and Externalism: A Reply to Mandelkern and Linzen," *Computational Linguistics* (ACL Anthology 2025.cl-2.8)** — as a new `wanted` (P2) item for a later session (the externalist-side reply, complementing this internalist one; not fetched this session). See the integration note in the return message.
