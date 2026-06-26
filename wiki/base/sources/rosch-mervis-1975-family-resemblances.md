---
type: source
id: rosch-mervis-1975-family-resemblances
title: "Family resemblances: Studies in the internal structure of categories"
authors:
  - Rosch, Eleanor
  - Mervis, Carolyn B.
year: 1975
venue: "Cognitive Psychology 7(4) (1975): 573–605"
url: http://matt.colorado.edu/teaching/categories/rm75.pdf
access: in-copyright-fair-use
meaning-senses:
  - referential
  - distributional
status: received
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: refines
    target: concept/frame-and-prototype-semantics
  - rel: refines
    target: source/wittgenstein-1953-philosophical-investigations
---

# Rosch & Mervis 1975 — Family resemblances: Studies in the internal structure of categories

## What it is

Eleanor Rosch and Carolyn B. Mervis's 1975 paper "Family resemblances: Studies in the internal structure of categories," *Cognitive Psychology* 7(4): 573–605. It is the **prototype primary** that turned Wittgenstein's family-resemblance idea into an experimental, quantitative result. Across six experiments — four on natural semantic categories (*furniture*, *vehicle*, *fruit*, *weapon*, *vegetable*, *clothing*), two on artificial categories — the authors test the hypothesis that **the more attributes a category member shares with other members (a high "family resemblance" score), the more typical (prototypical) it is rated**, and conversely that the most typical members share *least* with contrasting categories. The category members are not held together by a set of necessary-and-sufficient criterial attributes but by a network of overlapping-but-not-shared features; typicality is graded and predicted by attribute overlap.

It is a **primary cognitive-psychology / theory text** — not a human-labeled empirical *resource* for this project, and so **not a human anchor** for any LLM result. It predates LLMs entirely; it grounds the *theory* (the graded / prototype / family-resemblance picture of category structure) that the project's concept pages characterize, never a result about any model. (See "What it cannot ground.")

This page closes a gap flagged in [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md), whose "Honest gaps" section listed "Rosch & Mervis, 'Family resemblances' … (1975) — **not in-repo; characterization**" among the prototype primaries the page rested on without a quote or locator. It is also the experimental descendant of [`source/wittgenstein-1953-philosophical-investigations`](wittgenstein-1953-philosophical-investigations.md) §§66–67 (the `Familienähnlichkeit` / "network of similarities overlapping and criss-crossing" passages): Rosch & Mervis cite Wittgenstein 1953 **by name** as the source of the idea and frame their study as "an empirical confirmation of Wittgenstein's (1953) argument" (p. 605, quoted below). The `refines` links to both the concept and the Wittgenstein source record that descent.

## Provenance — what was fetched, from where, and at what strength

**Route that worked (primary-direct).** The full paper was fetched on **2026-06-26** as a PDF from an open-access University-of-Colorado teaching page, **`http://matt.colorado.edu/teaching/categories/rm75.pdf`** (a self-archived course copy; the project's standard self-archive route, not the paywalled Elsevier version of record). It is a 33-page scan of the *Cognitive Psychology* article, carrying the original journal pagination in its running heads ("COGNITIVE PSYCHOLOGY 7, 573-605 (1975)" on p. 573; page numbers 574–605 print in the scan). The PDF was downloaded with `curl --compressed`, and the text was extracted with `pdftotext`. Every quote below was matched **character-for-character** against that extracted text, and the page locators are read from the article's own printed page numbers in the scan. This is **primary-direct** provenance against the version of record's text and pagination.

**Routes not used.** The Elsevier *Cognitive Psychology* version of record (`sciencedirect.com/science/article/abs/pii/0010028575900249`) is paywalled and was **not** used (charter §12.4). Academia.edu / ResearchGate / Semantic Scholar mirrors were located but not needed once the Colorado scan read cleanly.

**OCR-artifact flags.** The `pdftotext` extraction of this scan carries two systematic OCR substitutions inside otherwise-faithful text, flagged here so the quotes below stay faithful to *what the tool returned* while the reader can see the intended word:
- The scan's serif "l" in **"criterial"** is repeatedly mis-read as a digit **1** → "criteria1". The author's word is *criterial*; "criteria1" in the quotes below is an OCR artifact, marked inline.
- In the significance report the scan renders **"p < .001"** as **"p < .OOl"** (zeros read as capital O, the final 1 read as lowercase l). Flagged inline.
These are extraction artifacts, not the authors' text; no page number, sentence, or figure here is reconstructed from memory — each is the `pdftotext` output of the fetched scan.

**Access / license.** The *work* (© 1975 Academic Press; the scan's p. 573 footer reads "Copyright 8 1975 by Academic Press, Inc. All rights of reproduction in any form reserved." — the "8" is the OCR of the © glyph) is **still in copyright**. Access is recorded `in-copyright-fair-use`: this page quotes only short fair-use passages from an open-access self-archive, copyright flagged here and under Known limits.

## Key passages (verbatim, with page locators)

### 1. The classical (criterial-features) target it argues against (pp. 573–574)

The paper opens by naming the view it overturns — category membership as all-or-none possession of criterial features:

> "However, when describing categories analytically, most traditions of thought have treated category membership as a digital, all-or-none phenomenon. That is, much work in philosophy, psychology, linguistics, and anthropology assumes that categories are logical bounded entities, membership in which is defined by an item's posses[s]ion of a simple set of criterial features, in which all instances possessing the criteria[l] attributes have a full and equal degree of membership." (pp. 573–574)

*(Primary-direct. "criteria[l]" = OCR "criteria1"; the line breaks across the 573/574 page boundary, where the scan splits "posses-/sion".)*

### 2. The Wittgenstein lineage and the family-resemblance definition (pp. 574–575)

The load-bearing methodological move: Rosch & Mervis take the family-resemblance idea **explicitly from Wittgenstein (1953)** and give it an operational, set-theoretic form:

> "This principle was first suggested in philosophy; Wittgenstein (1953) argued that the referents of a word need not have common elements in order for the word to be understood and used in the normal functioning of language. He suggested that, rather, a family resemblance might be what linked the various referents of a word. A family resemblance relationship consists of a set of items of the form AB, BC, CD, DE. That is, each item has at least one, and probably several, elements in common with one or more other items, but no, or few, elements are common to all items. The existence of such relationships in actual natural language categories has not previously been investigated empirically." (pp. 574–575)

*(Primary-direct; the passage spans the 574/575 page break.)*

The basic hypothesis, stated as attribute overlap:

> "In the present research, we viewed natural semantic categories as networks of overlapping attributes; the basic hypothesis was that members of a category come to be viewed as prototypical of the category as a whole in proportion to the extent to which they bear a family resemblance to (have attributes which overlap those of) other members of the category. Conversely, items viewed as most prototypical of one category will be those with least family resemblance to or membership in other categories." (p. 575)

*(Primary-direct.)*

### 3. The family-resemblance method — attribute-overlap scoring (pp. 581–582)

How "family resemblance" is operationalized as a per-item score and correlated against typicality — the method that makes the finding quantitative:

> "The measure of prototypicality was the mean rating on a 7-point scale of the extent to which items fit subjects' idea or image of the meaning of the category names (Rosch, 1975a). The basic measure of degree of family resemblance for an item was the sum of the weighted raw scores of each of the attributes listed for the item. … Items in each category were ranked 1-20 on the basis of prototypicality and were ranked 1-20 on the basis of each of the measures of family resemblance. Spearman rank-order correlations between the ranks of items on family resemblance and their ranks on prototypicality were performed separately for each of the measures of family resemblance and for each of the categories." (pp. 581–582)

*(Primary-direct; ellipsis omits the parallel definition of the logarithmic measure of family resemblance.)*

### 4. The typicality finding — the load-bearing result (p. 582)

The Experiment 1 result: family-resemblance score and rated typicality are strongly rank-correlated across all six categories.

> "These correlations, for the basic measure of family resem[b]lance, were: furniture, 0.88; vehicle, 0.92; weapon, 0.94; fruit, 0.85; vegetable, 0.84; clothing, 0.91. … All were significant (p < .001)." (p. 582)

*(Primary-direct; "resem[b]lance" splits across the 581/582 page break; "p < .001" is rendered "p < .OOl" by OCR.)*

And the authors' own reading of it:

> "Such results strongly confirm our hypothesis that the more an item has attributes in common with other members of the category, the more it will be considered a good and representative member of the category." (p. 582)

*(Primary-direct.)*

The complementary "no feature common to all" demonstration (Table 2): comparing the five most- vs. five least-typical members, the most-typical members share many attributes with each other while the least-typical share almost none — e.g., *fruit* 16 vs. 0, *weapon* 9 vs. 0, *clothing* 21 vs. 0, *vehicle* 36 vs. 2 (Table 2, p. 582, "NUMBER OF ATTRIBUTES IN COMMON TO FIVE MOST AND FIVE LEAST PROTOTYPICAL MEMBERS OF SIX CATEGORIES").

*(Table values primary-direct from the Table 2 cells in the scan.)*

### 5. The conclusion — family resemblance as the alternative to criterial features (p. 605)

The paper's closing claim ties the result back to Wittgenstein and to the rejection of necessary-and-sufficient definitions:

> "Family resemblance as a logical alternative to criteria[l] attributes. There is a tenacious tradition of thought in philosophy and psychology which assumes that items can bear a categorical relationship to each other only by means of the possession of common criteria[l] attributes. The present study is an empirical confirmation of Wittgenstein's (1953) argument that formal criteria are neither a logical nor psychological necessity; the categorical relationship in categories which do not appear to possess criteria[l] attributes, such as those used in the present study, can be understood in terms of the principle of family resemblance." (p. 605)

*(Primary-direct; "criteria[l]" = OCR "criteria1" in all three occurrences.)*

The abstract states the same verdict compactly (p. 573): "It is argued that family resemblance offers an alternative to criterial features in defining categories." *(Primary-direct, abstract.)*

## Bearing on this project

- **[`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md) — the prototype/graded-category mapping.** That page's "Prototype and graded-category semantics" section attributes to "Rosch & Mervis, 'Family resemblances' 1975 (**not in-repo; characterization**)" the founding result that "semantic categories have **graded internal structure**" organized around prototypes, with the classical necessary-and-sufficient view failing to predict the gradience. This page is the in-repo primary for exactly that: the attribute-overlap method (§3 above), the strong Spearman correlations between family resemblance and typicality (§4), and the explicit "alternative to criterial features" conclusion (§5). It is the empirical backbone — alongside Rosch 1975 (*JEP:General*), still not-in-repo — behind the project's prototype mapping onto [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md), where panel models' graded sense-relatedness ratings track the human DURel median monotonically, the behavioral shape a prototype/graded account predicts and a classical-discrete-sense account forbids.
- **The Wittgenstein lineage the concept page draws.** [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md) notes that "the graded view connects to Wittgenstein's *family resemblance* … — Rosch herself drew the connection." This page substantiates that with the primary's own words: Rosch & Mervis cite Wittgenstein (1953) by name (pp. 574, 605) and call their result "an empirical confirmation of Wittgenstein's (1953) argument." It is therefore the experimental hinge between [`source/wittgenstein-1953-philosophical-investigations`](wittgenstein-1953-philosophical-investigations.md) (§§66–67, the `Familienähnlichkeit` passages) and the project's graded-sense findings — the `refines` link to the Wittgenstein source records that the experiment sharpens (operationalizes-and-tests) the philosophical idea.
- **The `referential` and `distributional` meaning-senses.** `referential` (specifically the graded `referential.sense` reading [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md) uses): the paper is about categories of *referents* and how they are internally structured — typicality is a property of the word's extension, graded rather than all-or-none, the "modes of presentation at fine grain" the concept page tags `referential`. `distributional`: the family-resemblance score is built from **co-occurrence of attributes across category members** — an item's typicality is its position in a network of overlapping features, which is the cognitive-psychology ancestor of the project's standing "graded behavior may be nothing more than graded distributional similarity" worry. Tagging both reflects that this prototype result sits precisely on the referential-sense / distributional-similarity boundary the concept page flags as live.

## What it can ground

- The verbatim founding statement of the **prototype / graded-category** result: that natural categories have graded internal structure, that typicality is predicted by family-resemblance (attribute-overlap) score (strong Spearman correlations, §4), and that this is offered as "an alternative to criterial features" (§5) — for any page needing Rosch & Mervis's own words and figures rather than a paraphrase.
- The **operational definition** of a "family resemblance relationship" (set of items AB, BC, CD, DE; few or no elements common to all) and of the per-item family-resemblance score (§§2–3) — the method, not just the slogan.
- The **explicit historical-conceptual lineage** from Wittgenstein 1953 to the experimental prototype tradition (the paper cites Wittgenstein by name and frames itself as confirming his argument), grounding the bridge the project draws between [`source/wittgenstein-1953-philosophical-investigations`](wittgenstein-1953-philosophical-investigations.md) and its graded-sense findings.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models, AND it is not a human anchor.** This is the critical limit. The paper predates all neural language modeling; it grounds the *theory* (the prototype / family-resemblance picture of category structure) that a model may or may not behave as if it instantiates, never a result about a model. **It is not an `anchors:` resource** — it is a primary cognitive-psychology / theory text, not a human-labeled empirical asset the project scores model behavior against (no treebank, sense inventory, acceptability norm, or annotation released for project use). Citing it discharges **no** empirical claim's human-anchor obligation. The graded *human* yardstick the project's lexical results are actually scored against is the DURel/Usim graded-similarity tradition ([`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md)), not this 1975 paper; Rosch & Mervis grounds the *theory those resources operationalize*, a different role.
- **The Rosch 1975 *JEP:General* companion** ("Cognitive representations of semantic categories," *J. Exp. Psychol. General* 104: 192–233) — the other half of the prototype backbone — is **not** this paper and remains not-in-repo. Do not attribute that paper's typicality-rating norms or the standalone gradedness demonstrations to this source.
- **A processing / learning model of how prototypes form.** The authors state explicitly that "the present research was not intended to provide a processing model of the learning of categories or formation of prototypes" (p. 574); this page grounds the *structural* family-resemblance ↔ typicality result, not a mechanistic account.
- **Fine-grained quotation beyond the passages above.** Only the criterial-features framing (pp. 573–574), the Wittgenstein lineage and family-resemblance definitions (pp. 574–575), the Experiment 1 method and result with Table 2 (pp. 581–582), and the closing "alternative to criterial features" passage (p. 605) were read closely and verified. Experiments 2–6 (superordinate listing, contrasting-category overlap, the two artificial-category studies on learning and reaction time) are present in the scan but quoted only via the abstract here; do not cite their specific figures on the strength of this page.

## Known limits

- **In-copyright; short fair-use quotation only.** © 1975 Academic Press. This page reproduces only short passages from an open-access self-archive; do not reproduce the article wholesale.
- **Self-archived scan, with OCR artifacts.** The text was read from a course-page PDF scan via `pdftotext`, not from the Elsevier version of record. The pagination matches the journal (the scan prints 573–605), but two systematic OCR substitutions are present and flagged in every affected quote: "criterial" → "criteria1" and "p < .001" → "p < .OOl". A session quoting at length or at finer grain should re-verify against a clean version of record, especially any quotation from Experiments 2–6 not read here.
- **Companion paper conflation risk.** Rosch published two foundational 1975 prototype papers; this is the *Cognitive Psychology* "Family resemblances" one (Rosch & Mervis), **not** the single-author *JEP:General* "Cognitive representations of semantic categories." Keep the two distinct when citing typicality norms vs. the family-resemblance/attribute-overlap result.
