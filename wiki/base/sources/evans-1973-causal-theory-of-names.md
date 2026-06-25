---
type: source
id: evans-1973-causal-theory-of-names
title: The Causal Theory of Names
authors:
  - Evans, Gareth
year: 1973
venue: "I-Gareth Evans, in the symposium 'The Causal Theory of Names' (with II-J. E. J. Altham), Proceedings of the Aristotelian Society, Supplementary Volume 47 (1973), pp. 187-225. Evans's part (Part I) is pp. 187-208; Altham's reply (Part II) is pp. 209-225. Published by Blackwell Publishing on behalf of The Aristotelian Society. (Reprinted in Evans, Collected Papers, Oxford UP 1985, and in several anthologies — those reprints were NOT the version read here.)"
url: http://www.gbppr.net/2600/TheCausalTheoryofNames.pdf
access: open-access (self-archived JSTOR scan; official version paywalled at academic.oup.com / JSTOR stable/4106912)
meaning-senses:
  - referential
status: received
created: 2026-06-25
updated: 2026-06-25
links:
  - rel: supports
    target: concept/referential-meaning
  - rel: refines
    target: source/putnam-1975-meaning-of-meaning
---

# Evans 1973 — The Causal Theory of Names

## What it is

The classic **critique-from-within** of the causal theory of reference. Gareth Evans, "The Causal Theory of Names" (Part I of a 1973 Aristotelian Society symposium with J. E. J. Altham), *Proceedings of the Aristotelian Society*, Supplementary Volume 47, pp. 187-208. Evans takes Kripke's causal/historical picture of how a name reaches its bearer, **agrees that there must be a causal element** in name-reference, but argues that the **pure causal "chain of communication" picture is not adequate**: the causal *origin* of a name (its baptism) does not by itself fix what the name now denotes, because the referent can **shift** through the causal chain (the "Madagascar" case). Evans's positive proposal relocates the causal relation: a name's denotation in a community depends on the **dominant causal source of the body of information** the community associates with the name, together with a **common-knowledge-in-a-community** condition for an expression's being a name at all. This is the externalist primary the project's [`concept/referential-meaning`](../concepts/referential-meaning.md) had listed as "**not in-repo; characterization**" (the "Evans's causal theory of names" half of the `referential.externalist` sub-tag), and the companion the [`source/putnam-1975-meaning-of-meaning`](putnam-1975-meaning-of-meaning.md) page flagged as still-queued in [`wanted.md`](../wanted.md). This page supplies the verbatim primary.

**A `source` page is NOT a human anchor.** This is a 1973 philosophy essay; it grounds the *concept* the `referential.externalist` sub-tag names (specifically the causal/information-source theory of name-reference), not any empirical result about any model, and it licenses no human-comparison claim. It predates LLMs by decades and is silent on machines; where the text bears on a machine-relevant question at all, it does so only as theory whose antecedents a later argument would have to settle.

## Provenance — exactly what was fetched and verified

- **Venue actually read:** a self-archived **JSTOR scan of the original Aristotelian Society Supplementary Volume 47 (1973)** — the PDF carries JSTOR's own cover page (`Stable URL: http://www.jstor.org/stable/4106912`, "Accessed: 23/06/2012", "Source: Proceedings of the Aristotelian Society, Supplementary Volumes, Vol. 47 (1973), pp. 187-225"). Downloaded 2026-06-25 from `http://www.gbppr.net/2600/TheCausalTheoryofNames.pdf` (HTTP 200, 3,795,147 bytes, MD5 `7edec39d8b5212d424ee8c9f8963a4e2`). The official channels are paywalled: `academic.oup.com/aristoteliansupp/article-pdf/47/1/187/...` and JSTOR `stable/4106912` both require subscription. This scan is the **original pagination** (pp. 187-225), so locators are the printed Aristotelian Society page numbers, suitable for citation.
- **Scope read and quoted:** the symposium is two parts; **only Part I (Evans, printed pp. 187-208) was read and is quoted here.** Part II (Altham's reply, pp. 209-225) was not ingested. The 40-page scan maps cleanly: scan page `i` (1≤i≤22) is printed page `186+i`; even printed pages carry the number as the first line, odd pages carry it in the running head ("THE CAUSAL THEORY OF NAMES … 189"). Part II begins at scan page 23 (printed p. 209).
- **Text extraction:** the PDF has a genuine embedded text layer (a clean JSTOR OCR, ~93k extractable chars over 40 pages). Text was extracted locally with **PyMuPDF (fitz) 1.27.2** (`pip install pymupdf`; `pdftotext`/poppler was not available in this environment). Every quote below was verified **character-for-character against that extracted text** by whitespace-normalized exact substring match (PDF hard line-breaks normalized to single spaces before matching).
- **OCR-quality flag:** this is OCR of a 1973 scan, so the extracted text carries scanner artifacts — "Gödel" reads "G6del", "rôle" reads "r61e", "1814" reads "18x14"/"x814", the diagram labels α and β read "a"/"cx" and "Pf"/"fI", "sufficient" occasionally "suficient", "themselves" once "themself". **None of these corruptions fall inside the quotes used below** (the quoted strings were chosen to avoid them, or are flagged inline `[OCR: …]` where unavoidable); the **wording** of every quote was checked against the extracted text, but a session quoting at length should re-verify against the scan image.

## The two questions, and the target: the pure Causal Theory

Evans separates two questions a theory of names must answer (printed p. 187):

> "The first is about what the name denotes upon a particular occasion of its use … I shall use the faintly barbarous coinage: what the speaker denotes (upon an occasion) for this notion. The second is about what the name denotes; we want to know what conditions have to be satisfied by an expression and an item for the first to be the, or a, name of the second." (p. 187)

The Causal Theory he targets is Kripke's, tightened into a theory (Evans flags that Kripke "deliberately held back from presenting his ideas as a theory," p. 187). Its core, as Evans states it, is that **the denotation of a name in a community is found by tracing a causal chain back to the item** (printed p. 195):

> "These points might be conceded by Kripke while maintaining the general position that the denotation of a name in a community is still to be found by tracing a causal chain of reference preserving links back to some item. It is to this theory that I now turn." (p. 195)

What a causal theory must explain — Evans's argument by parallel with general terms — is that a single mechanism gives a word its denotation and preserves it; a theory with a *separate* preservation mechanism cannot account for **change** (printed p. 195):

> "There aren't two fundamentally different mechanisms involved in a word's having a meaning: one bringing it about that a word acquires a meaning, and the other—a causal mechanism—which operates to ensure that its meaning is preserved. … Indeed such a theory could not account for the phenomenon of a word's changing its meaning." (p. 195)

> "Change of meaning would be decisive against such a theory of the meaning of general terms. Change of denotation is similarly decisive against the Causal Theory of Names." (pp. 195-196)

## The Madagascar case — the causal origin does NOT fix current reference

The famous counterexample: the name's referent **shifted through a mistake in the causal chain**, so the baptismal/causal origin is not what the name now denotes (printed p. 196):

> "In the case of 'Madagascar' a hearsay report of Malay or Arab sailors misunderstood by Marco Polo … has had the effect of transferring a corrupt form of the name of a portion of the African mainland to the great African Island." (p. 196, Evans quoting Isaac Taylor, *Names and their History*, 1898)

Evans adds an imaginary twin-case (a nurse switches two babies; "the man universally known as 'Jack' is so called because a woman dubbed some *other* baby with the name," p. 196) and draws the verdict (printed p. 196):

> "It is clear that the Causal Theory unamended is not adequate. It looks as though, once again, the intentions of the speakers to use the name to refer to something must be allowed to count in determination of what it denotes." (p. 196)

The constraint on any fix (printed p. 196): a theory must let "'Madagascar' … be the name of the island" while NOT making "'Gödel' [OCR: 'G6del'] … become a name of Schmidt in the situation envisaged by Kripke nor 'Goliath' a name of the Philistine killed by David." (p. 196). Evans had earlier given a parallel everyday case against the chain being *necessary or determinative*: on a TV quiz he says "'Kingston is the capital of Jamaica'" and says something true even though the man he picked the scrap from "was actually referring to Kingston-upon-Thames" (p. 194); and the chain is not even *necessary* — Wagera Indian and US-street naming-by-rule let "a knowledgeable speaker … excogitate a name … without any causal connexion whatever with the use by others of that name" (pp. 194-195).

## The positive proposal — reference tracks the dominant causal SOURCE of the information

Evans agrees with Kripke that the absurdity in the pure Description Theory "resides in the absence of any causal relation between the item concerned and the speaker," but argues Kripke **mislocated** the causal relation (printed p. 197):

> "But it seems to me that he has mislocated the causal relation; the important causal relation lies between that item's states and doings and the speaker's body of information—not between the item's being dubbed with a name and the speaker's contemporary use of it." (p. 197)

The reference-fixing relation is therefore to the **source of the information**, not the baptism (printed p. 198):

> "… typically a necessary (but not sufficient) condition for x's being the intended referent of S's use of a name is that x should be the source of causal origin of the body of information that S has associated with the name." (p. 198)

> "… it is rather that item which is causally responsible for the speaker's possession of that body of information, or dominantly responsible if there is more than one." (p. 199)

Two ideas do the work, **source** and **dominance**. Source (printed pp. 199-200): "X is the source of the belief S expresses by uttering 'Fa' if there was an episode which caused S's belief in which X and S were causally related in a type of situation apt for producing knowledge that something F-s" (pp. 199-200) — a man "can be the source of things we discover by rifling through his suitcase or by reading his works" (p. 199). Dominance handles a *dossier* whose elements have mixed sources, and lets persistent misidentification shift which item a cluster is "dominantly of" (the identical-twin-takeover and Napoleon-impostor cases, pp. 200-202). The summary verdict (printed p. 202):

> "I think we can say that in general a speaker intends to refer to the item that is the dominant source of his associated body of information." (p. 202)

## The community / common-knowledge condition for being a name

Evans's tentative definition makes name-hood a fact about a **community** and its **common knowledge**, not about an originating baptism (printed p. 202):

> "'NN' is a name of x if there is a community C / 1. in which it is common knowledge that members of C have in their repertoire the procedure of using 'NN' to refer to x (with the intention of referring to x) / 2. the success in reference in any particular case being intended to rely on common knowledge between speaker and hearer that 'NN' has been used to refer to x by members of C and not upon common knowledge of the satisfaction by x of some predicate embedded in 'NN'." (p. 202)

He explicitly contrasts this with Kripke's baptism-suffices picture (printed p. 203):

> "Our conditions are more stringent than Kripke's since for him an expression becomes a name just so long as someone has dubbed something with it and thereby caused it to be in common usage. This seems little short of magical." (p. 203)

A further complication is **deference**: standardly we intend to conform to the community's general use, but "sometimes we use them with the over-riding intention to conform to the use made of them by some other person or persons. In that case I shall say that we use the expression deferentially" (p. 205) — and a deferentially-used name denotes whatever the deferred-to authority denotes, regardless of the deferring speaker's own dominant information-source (the biblical-archaeologists and "Turnip" cases, pp. 205-207).

Evans's own conclusion grants both camps something — the Description Theorist gets denotation fixed "in a more or less complicated way by the associated bodies of information," but "the fix is by causal origin and not by fit"; the Causal Theorist keeps "the importance of causality … in a central position" and the non-contingency of identity statements, because "Information is individuated by source; if a is the source of a body of information nothing else could have been." (p. 207).

## Bearing on this project

- **[`concept/referential-meaning`](../concepts/referential-meaning.md) — the second externalist primary the `referential.externalist` sub-tag rested on.** That page names "Evans's causal theory of names (that a name refers via a causal chain back to a baptismal event, not via a cluster of descriptions)" as a canonical externalist statement but flagged it "**not in-repo; characterization**." Two things to note for whoever updates the concept page. First, the in-repo characterization is **too crude in exactly the way Evans's paper is about**: Evans does *not* hold that a name "refers via a causal chain back to a baptismal event" — that is the pure Kripkean picture he **rejects** (the Madagascar case is precisely a counterexample to it). His view is that reference tracks the **dominant causal source of the body of information** a community associates with the name (pp. 198-199, 202), which can come apart from the baptism. Second, the link to the concept page is `supports` (this source secures and corrects the externalist characterization the page presupposes); a separate `refines` link to [`source/putnam-1975-meaning-of-meaning`](putnam-1975-meaning-of-meaning.md) records that Evans's information-source account and Putnam's division-of-labour account are two different externalist reference-fixers, not the same one (see next bullet).
- **Evans's information-source account vs. Putnam's division-of-labour account (refines, no claim).** Putnam fixes natural-kind reference by the *environment* + an *expert sub-community* the layperson defers to + an indexical `sameL` relation to locally-sampled stuff ([`source/putnam-1975-meaning-of-meaning`](putnam-1975-meaning-of-meaning.md), pp. 144-152). Evans fixes *name*-reference by the *dominant causal source of the associated information* + a *common-knowledge-in-a-community* naming practice (pp. 198-202). These overlap (both are externalist; both make a community load-bearing; Evans's "deference," p. 205, is structurally close to Putnam's expert-deference) but they are not the same mechanism — Evans's reference-fixer is an *information-flow* relation from item to dossier, not Putnam's environment+expert+indexical triad. This difference is the load-bearing one for the project's open question below.
- **The corpus-inheritance / community-membership question (CRUCIAL framing — evidence both ways, undecided here).** The in-repo essays [`essay/reference-as-premise-bound`](../../findings/essays/reference-as-premise-bound.md) and [`essay/reference-denials-disunified`](../../findings/essays/reference-denials-disunified.md) carry a **revision trigger (c)** armed for Evans 1973: the question is whether Evans's account "fix[es] the community-membership / corpus-inheritance question on independent grounds" (does a system trained on a community's pooled corpus inherit the causal-historical chain that fixes reference?) or, like Putnam, leaves it open. The text cuts **both ways**, and this page does **not** decide it (the decision is the orchestrator's adversarial-integration job, per `PROJECT.md` §12.3 — a source page surfaces evidence, it does not ratify):
  - **Reading that pushes toward "open / membership still off-board" (parallels Putnam):** Evans's name-hood condition is *common knowledge within a community C* that members "have in their repertoire the procedure of using 'NN' to refer to x" (p. 202). Like Putnam's "sociolinguistic state of the collective linguistic body," this presupposes a *community* whose membership Evans never defines machine-relevantly; nothing in the text says whether a corpus-trained system that emits the procedure counts as a member of C, or merely as a record of C's procedure. On this reading Evans, like Putnam, *sharpens the antecedent without deciding it*, and trigger (c) comes out the same way it did for Putnam (premise stays a free classificatory choice).
  - **Reading that could bear DIFFERENTLY from Putnam (why the trigger was armed specifically for Evans):** Evans's reference-fixer is the **dominant causal source of a *body of information*** (pp. 198-199), and his "source" relation is explicitly satisfied by *reading a person's works* ("a man can be the source of things we discover by … reading his works," p. 199) — i.e. by *textual* information transmission, not only perception or baptism. A corpus is, on its face, exactly "a body of information" with item-sources, and "reading works" is exactly how a text-trained system acquires it. So Evans's apparatus, unlike Putnam's environment+indexical triad, contains a hook (information-source-by-text) that *might* be argued to transfer to the corpus case — making the antecedent arguable rather than free. **But equally**, Evans pairs source with two conditions that resist the transfer: (i) the source relation must be "a type of situation apt for producing *knowledge*" (p. 200), and (ii) name-hood requires *intentions* and *common knowledge* in a community (pp. 202: "without the intentions being manifest there cannot be the common knowledge required for the practice") — both of which a deflationist would say a corpus-trained next-token predictor lacks. The textual evidence therefore genuinely supports both verdicts; which one wins turns on a further premise (whether corpus-ingestion is a knowledge-apt information-source and whether the system is a community member) that **Evans's text does not settle**. Flagged honestly: the paper is silent on machines, so any transfer is an *application* of Evans, not a reading of him.
- **What it does NOT license.** No claim about any model follows from this page. It grounds the *theory* (the causal/information-source account of name-reference) a model's reference-relation would be judged against; it is not a human anchor and supports no human-comparison.

## What it can ground

- The verbatim primary for **the causal/information-source theory of name-reference**: the two questions (p. 187); the statement of the pure Causal Theory as chain-tracing (p. 195); the change-of-denotation argument (pp. 195-196); the **Madagascar** referent-shift case and the "unamended … not adequate" verdict (p. 196); the **mislocated causal relation** correction (p. 197); the **source / dominant-source** reference-fixing condition (pp. 198-199, 202); the **common-knowledge-in-a-community** name-hood definition (p. 202) and its contrast with Kripke's baptism-suffices view (p. 203); **deference** (p. 205); and "Information is individuated by source" (p. 207) — for any page needing the externalist *name*-reference primary rather than a paraphrase.
- The textual basis for treating Evans as an externalist who **rejects the pure causal-chain/baptism picture** and substitutes an information-source + community account — correcting the cruder "causal chain back to a baptismal event" characterization currently on the concept page.
- The evidence (both directions) for the essays' **trigger (c)** on corpus-inheritance/community-membership — laid out, not adjudicated.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models:** the essay predates all of it by decades and is silent on machines. It grounds the *theory*, never a result about a model. It is **not a human anchor** and licenses no human-comparison claim.
- **A settled verdict on the corpus-inheritance / community-membership question.** The text supports both the "membership still off-board" reading and the "information-source might transfer" reading; the page records both and decides neither. Ratifying which way trigger (c) fires is a later, independent adversarial pass ([`PROJECT.md`](../../../PROJECT.md) §12.3), not this ingestion.
- **A settled verdict that the causal/externalist theory of reference is correct.** It is one strongly-argued position (and itself a *critique* of the cruder causal theory); the internalist pole and the deflationary line contest the whole frame. Cite it as the externalist name-reference primary, not as established fact.
- **Altham's reply (Part II, pp. 209-225)** was not read; nothing here represents Altham's position.

## Known limits

- **OCR of a 1973 scan.** Locators are the original Aristotelian Society Supplementary Volume 47 page numbers read from the scan; reliable for citation, but the source is an OCR text layer over a scanned image, so a citing session quoting at length should re-verify against the scan image. Quoted strings were chosen to avoid the known OCR corruptions ("G6del", "18x14", "r61e", α/β as "cx"/"Pf"); the one unavoidable corruption inside a quote is flagged `[OCR: …]`.
- **Self-archived copy, not the publisher's.** The official version (OUP / JSTOR `stable/4106912`) is paywalled; the read copy is a self-archived JSTOR scan. Pagination matches the original (pp. 187-225), so citation is unaffected, but the provenance is a third-party host (gbppr.net), recorded with byte size and MD5 above.
- **Reprint pagination differs.** A reader using the *Collected Papers* (Oxford UP 1985) reprint or an anthology must re-map page numbers; the locators here are the 1973 Aristotelian Society originals only.
- **Evans ≠ "the causal theory."** The most citable risk: this paper is widely shelved *as* "the causal theory of names," but Evans's own position is a **critique** of the pure causal/baptism theory and a substitute (information-source + community). A citing page must not use this source to support the claim that Evans held names refer "via a causal chain back to a baptismal event" — he argues the opposite.
