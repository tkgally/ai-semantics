---
type: source
id: rosch-1975-cognitive-representations
title: "Cognitive Representations of Semantic Categories"
authors:
  - Rosch, Eleanor
year: 1975
venue: "Journal of Experimental Psychology: General 104(3) (1975): 192–233. DOI 10.1037/0096-3445.104.3.192"
url: https://doi.org/10.1037/0096-3445.104.3.192
access: not-open-access
meaning-senses:
  - referential
  - distributional
status: secondary-only
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: refines
    target: concept/frame-and-prototype-semantics
  - rel: supports
    target: result/lexical-sense-gradience-v1
---

# Rosch 1975 — Cognitive Representations of Semantic Categories

## What it is

Eleanor Rosch's "Cognitive Representations of Semantic Categories," published in *Journal of Experimental Psychology: General* 104(3) (1975): 192–233 (DOI 10.1037/0096-3445.104.3.192). It is the **prototype / graded-category primary** behind this project's prototype mapping: a set of priming and verification experiments establishing that natural semantic categories (*bird*, *furniture*, *fruit*, etc.) have **graded internal structure** — subjects reliably rate some members as more central / typical than others, that typicality predicts processing (reaction time, the effect of an advance category-name prime on a matching task), and that category boundaries are fuzzy rather than sharp. The classical theory — a category fixed by necessary-and-sufficient conditions, with all-or-none membership — predicts none of this. The 1975 paper is one half of the empirical backbone (the other being the in-repo companion [`source/rosch-mervis-1975-family-resemblances`](rosch-mervis-1975-family-resemblances.md)) of the prototype account that [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md) maps onto the project's lexical-sense-gradience result.

It is a 1975 empirical-psychology primary — **not** a human-labeled empirical resource in this project's sense, and so **not a human anchor** for any LLM result (see "What it cannot ground"). It predates LLMs; it grounds the *theory* a model may or may not instantiate, never a result about a model.

Before this page, [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md) cited Rosch 1975 only as "(not in-repo; characterization)" in its "Honest gaps" section, with no quote or locator. This page closes that gap **only partially**: the open-access *primary* could not be reached (see provenance), so the findings below are carried **via a named secondary** — Rosch's own 1978 retrospective — at lower strength than primary-direct.

## Provenance — what was fetched, from where, at what strength

The **open-access primary full text could not be reached** this session, and the findings are therefore carried **carried-via-secondary** through a single named, open-access source. Every quote below is flagged. **No primary-direct quotation, page number, experiment count, or figure from the 1975 paper itself is asserted on this page.**

**Routes tried for the primary (all failed or disallowed), 2026-06-26:**

- **Unpaywall** (`api.unpaywall.org`, DOI 10.1037/0096-3445.104.3.192) returned `is_oa: false`, `oa_status: "closed"`, `best_oa_location: null`, `oa_locations: []` — **authoritative: no open-access copy is indexed anywhere.**
- **Semantic Scholar API** (`api.semanticscholar.org`, same DOI) returned `isOpenAccess: false`, `openAccessPdf: {status: "CLOSED"}`.
- **ontology4.us** "direct PDF" (`/download/dot/ontopage/sub_Rosc1975.pdf`) — fetched (HTTP 200) but is a **1-page citation stub**, not the article; it merely points back to academia.edu.
- **academia.edu** (`/24474401/...`) — HTTP 403 (login wall); not open access.
- **PhilPapers** (`/rec/ROSCRO`), **CORE** (`core.ac.uk/search`), **scispace** (`/papers/...`) — 403 / Cloudflare bot-challenge. The scispace `/pdf/...` endpoint returned a 3.5 MB body that `file(1)` misreported as "PDF, 42 page(s)" but is in fact a Cloudflare "Just a moment…" JavaScript challenge page (raw bytes begin `<!DOCTYPE html>`), **not** the article.
- **pdfcoffee.com** — a scraper/file-locker host of the kind excluded by charter §12.4 (no pirated/paywalled full text); **not used.**
- **APA / EBSCO version of record** — paywalled; **not used.**

So the **citation target is the 1975 JEP:General original (104(3): 192–233)**, which was **not read**.

**The single secondary actually read (carried-via-secondary).** Rosch, E. (1978), "Principles of Categorization," in E. Rosch & B. B. Lloyd (eds.), *Cognition and Categorization* (Hillsdale, NJ: Lawrence Erlbaum, 1978), pp. 27–48 — i.e. **Rosch's own retrospective summary of her early-1970s program, written three years after the 1975 paper.** Fetched 2026-06-26 as an open-access scan from a university course page (`cs.rice.edu/~vo9/recognition/2016/slides/lecture07/CognitionAndCategorization.pdf`, HTTP 200, 24-page PDF), extracted with `pdftotext -layout`, and every quoted string below matched character-for-character against that extracted text. Locators are the chapter's own in-text author-date citations; **OCR-artifact note**: the scan carries occasional OCR errors (e.g. "morining" for "morning", "virutally" for "virtually", "New Sork" for "New York" in the references), reproduced verbatim where they fall inside a quoted span and flagged inline.

**Resolving the 1975 citation key.** The 1978 chapter cites the early-1970s work with suffixed keys (Rosch 1975a–d). Its reference list (read verbatim from the same scan) pins the target paper to key **(b)**:

> "Rosch, E. Cognitive representations of semantic categories. Journal of Experimental Psychology: General., 1975, 104, 192-233. (b)"

*(Carried-via-secondary: Rosch 1978 reference list, cs.rice.edu scan. Confirms key "1975b" = this page's target. The "1975c" key is the color paper, JEP:HPP 1(303–322); "1975a" is Cognitive Psychology 7(532–547), "Cognitive reference points"; "1975d" is a cross-cultural chapter — none of those three is this page's target.)* Only findings the chapter pins specifically to **1975b** are credited to the target below; where the chapter cites 1975b jointly with other works, that is stated.

## Key passages (all carried-via-secondary, primary NOT consulted)

All quotes are from Rosch 1978, "Principles of Categorization" (cs.rice.edu scan), reporting the 1975b findings. **None is a quotation of the 1975 paper itself.**

### 1. Typicality judgments are reliable and graded (cited to 1975b among others)

> "It is by now a well-documented finding that subjects overwhelmingly agree in their judgments of how good an example or clear a case members are of a category, even for categories about whose boundaries they disagree (Rosch, 1974, 1975b). Such judgments are reliable even under changes of instructions and items (Rips, Shoben, & Smith, 1973; Rosch, 1975b, 1975c; Rosch & Mervis, 1975)."

*(Carried-via-secondary: Rosch 1978, p. ~33 of the chapter; primary NOT consulted. Note this finding is attributed jointly — the target 1975b is one of several cited sources, not the sole source.)*

This is the graded-internal-structure core: stable, reproducible goodness-of-example ratings *even where category boundaries are disputed* — the fuzzy-boundary + graded-membership picture the classical necessary-and-sufficient account forbids.

### 2. Prototypicality is correlated with production frequency / output order (1975b)

> "Battig and Montague (1969) provided a normative study of the probability with which college students listed instances of superordinate semantic categories. The order is correlated with prototypicality ratings (Rosch, 1975b)."

*(Carried-via-secondary: Rosch 1978, p. ~34; the correlation between Battig–Montague output order and prototypicality ratings is pinned specifically to 1975b. Primary NOT consulted.)*

### 3. Advance information (priming / set) effect for natural superordinate categories (1975b)

> "Effects of Advance Information on Performance: Set, Priming. For colors (Rosch, 1975c), for natural superordinate semantic categories (Rosch, 1975b), and for artificial categories (Rosch et al., 1976b), it has been shown that degree of prototypicality determines whether advance information about the category name facilitates or inhibits responses in a matching task."

*(Carried-via-secondary: Rosch 1978, p. ~34; the "natural superordinate semantic categories" clause is pinned specifically to 1975b — this is the target paper's signature priming method. Primary NOT consulted.)*

This is the load-bearing mechanism for the project's purposes: an advance category-name prime *helps* matching for typical members and *hurts* it for atypical ones, so processing tracks graded typicality — exactly the behavioral signature a prototype account predicts and a discrete-definition account does not.

### 4. The graded-membership / fuzzy-boundary framing the program established

> "Although logic may treat categories as though membership is all or none, natural languages themselves possess linguistic mechanisms for coding and coping with gradients of category membership."

> "Even those who insist that statements such as 'A robin is a bird' and 'A penguin is a bird' are equally true, have to admit different hedges applicable to statements of category membership. Thus it is correct to say that a penguin is technically a bird but not that a robin is technically a bird, because a robin is more than just technically a bird; it is a real bird, a bird par excellence."

*(Both carried-via-secondary: Rosch 1978, p. ~35–36. These two passages are the chapter's *general* statement of graded category structure — Rosch's synthesis of her program, **not** pinned to 1975b alone; the robin/penguin "hedges" point continues into a sentence the chapter attributes to Rosch 1975a, the separate "Cognitive reference points" paper. They are quoted here for the conceptual framing the 1975b experiments serve, not as findings of the target paper. Primary NOT consulted.)*

## Bearing on this project

This page is the in-repo theory primary (at secondary strength) behind the prototype mapping in [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md), which is the concept page standing over [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md).

- **The graded-category prediction the project tests.** The concept page frames the sharp behavioral prediction: *if* a model's sense structure is graded (prototype-like) rather than a classical discrete inventory, its same/different-sense behavior should be **monotone in human-rated relatedness**, not a step function. Rosch 1975b is the experimental origin of the "graded, prototype-organized category" half of that contrast (typicality ratings are reliable and graded; priming and verification track typicality; boundaries are fuzzy). The classical necessary-and-sufficient theory it argues against is the "discrete inventory" half.
- **What [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md) showed against that frame.** That result found every panel model's graded sense-relatedness rating strongly rank-correlated with the human DURel median (Spearman 0.68/0.60/0.80 on the 4-point framing), in or above the human inter-annotator range, with monotone per-level means and the signal surviving partialling-out of the model's own topic-similarity rating. Read through Rosch, the models order usages by relatedness much as a prototype account predicts and a classical discrete-sense account does not — hence the `supports` link. **But note the standing distributional caveat the concept page carries**: that is prototype-*consistent behavior*, not evidence of a prototype *representation* distinct from graded distributional similarity. Rosch 1975b grounds the theory; it does not license reading the model result as more than behavioral.
- **`meaning-senses` justification.** Tagged `referential` because graded category structure is about `referential.sense` at fine grain — modes of presentation / degrees of category centrality for a referent, the same wedge [`concept/polysemy`](../concepts/polysemy.md) and the concept page occupy (not `referential.reference`: the paper is about internal category structure, not extension-fixing). Co-tagged `distributional` deliberately, per the concept page's discipline: for the project's models, "graded prototype structure" and "graded distributional similarity" may be the same thing, so the distributional null rides on every finding this source is cited for. The 1975 paper itself is pre-distributional-semantics; the tag marks the *project-side* live alternative, not a claim about Rosch's own framework.

## What it can ground

- The **theory** that natural semantic categories have graded internal structure (reliable typicality ratings; processing — priming/verification — tracking typicality; fuzzy boundaries), as the cognitive-psychology origin of the prototype half of the project's prototype-vs-classical contrast — at **secondary strength**, via Rosch's own 1978 retrospective, until the primary is read.
- The historical-conceptual placement of Rosch 1975 as the prototype/graded-category primary that [`concept/frame-and-prototype-semantics`](../concepts/frame-and-prototype-semantics.md)'s prototype mapping rests on, alongside Wittgenstein's family-resemblance ancestor ([`source/wittgenstein-1953-philosophical-investigations`](wittgenstein-1953-philosophical-investigations.md), §§66–67).

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models, and no human-anchor obligation.** The paper predates all of it. It is a **theory/empirical-psychology primary, NOT a human anchor** in this project's sense: it is not an in-repo human-labeled empirical *resource* (no treebank, sense inventory, acceptability norm, or per-item annotation usable as a yardstick — the human typicality norms *inside* the 1975 paper are not ingested here, and even if they were, a `source` page is not an `anchors:` resource). Citing this page **discharges no empirical claim's human-anchor obligation**; the `supports` link to [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md) is theory-grounding, and that result's actual human anchor remains its DURel/Usim resource ([`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md)), not this source.
- **Any verbatim sentence, page number within 192–233, experiment count, subject count, stimulus set, or numerical result *of the 1975 paper itself*.** None was read: the OA primary was unreachable. Everything above is Rosch's later (1978) characterization of the work, at secondary strength. A session needing the 1975 paper's own wording, its specific experiments, or its data tables **must reach the primary** (a legitimate APA/EBSCO copy or a genuine OA scan) and re-verify before citing at primary strength.
- **The distinction between the four 1975 Rosch papers.** Only findings the 1978 chapter pins specifically to key **1975b** are credited here to the target; 1975a (Cognitive reference points), 1975c (color codes), and 1975d (cross-cultural) are *different papers* and their findings are **not** this source's.

## Known limits

- **Secondary-only; primary not consulted.** `status: secondary-only`, `access: not-open-access`. Unpaywall confirms there is no indexed open-access copy (`oa_status: closed`); the readable hits are paywalled, login-walled, or pirate scrapers. All substantive content is carried through Rosch's 1978 "Principles of Categorization" retrospective. This is weaker than the project's primary-direct source pages; treat it as a **placeholder grounding the theory** until the primary is ingested.
- **Joint attribution.** Two of the four quoted passages (1 and 4) cite 1975b *jointly* with other Rosch works or are the chapter's general synthesis, not findings pinned to 1975b alone; this is flagged per-quote. Only passages 2 and 3 are pinned specifically to 1975b.
- **OCR artifacts.** The cs.rice.edu scan carries OCR errors (e.g. "New Sork", "morining", "virutally"); quoted spans reproduce them verbatim where they occur. Locators given as "p. ~NN of the chapter" are approximate (the scan's page breaks, not the 1978 volume's pp. 27–48 pagination at fine grain).
- **Open backlog item.** The companion paper [`source/rosch-mervis-1975-family-resemblances`](rosch-mervis-1975-family-resemblances.md) (*Cognitive Psychology* 7, 573–605) is already in-repo (`status: received`); the **primary of *this* paper** is the piece that remains wanted. The concept page's "Honest gaps" list still stands for the Rosch 1975b primary. This page narrows that gap for Rosch 1975b to **secondary strength**, not primary.
