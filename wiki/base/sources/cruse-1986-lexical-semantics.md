---
type: source
id: cruse-1986-lexical-semantics
title: "Lexical Semantics (1986)"
authors:
  - Cruse, D. Alan
year: 1986
venue: "Cambridge: Cambridge University Press (Cambridge Textbooks in Linguistics). pp. xiv + 310."
url: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/523D4BB8D838D5341CDA72E2EE7385EA/S0272263100007543a.pdf/lexical_semantics_d_a_cruse_new_york_cambridge_university_press_1986_pp_xiv_310.pdf
access: in-copyright-secondary-only
meaning-senses:
  - referential
  - distributional
status: received
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: refines
    target: concept/polysemy
  - rel: depends-on
    target: source/armendariz-2020-cosimlex
---

# Cruse 1986 — Lexical Semantics

## What it is

D. Alan Cruse's *Lexical Semantics* (Cambridge University Press, 1986) is the standard textbook statement of the **descriptive, sense-relation tradition** in word meaning: it takes the **lexical unit** (a form together with a single sense) as its object, and builds up word meaning from the **relations** a unit contracts — paradigmatic relations (synonymy, hyponymy, meronymy, the varieties of oppositeness) and the way **context** modifies meaning. It is the founding-reading-list item the project listed for "baseline sense-relation vocabulary; benchmark for the gradiness wedge" ([`base/wanted.md`](../wanted.md)), and the work [`concept/polysemy`](../concepts/polysemy.md) explicitly named as a pending ingestion in its "Honest gaps" section.

Its two load-bearing contributions **for this project** are:

1. **The selection / modulation distinction** — Cruse separates two ways context modifies a word's meaning: *contextual selection of senses* (the context picks out one of several **discrete** senses → the word is **ambiguous**) versus *contextual modulation* (the context modifies meaning **within a single sense**, highlighting some semantic traits and backgrounding others → the word is **general** with respect to those traits). The first is discrete; the second is "by nature not discrete but continuous and fluid."
2. **Lexical meaning as a structure of sense relations** — a lexical semantic relation is a relation between lexical units, and certain relations (hyponymy, meronymy, antonymy, troponymy) are systematic enough to give the lexicon descriptive structure.

It is a **theory/descriptive-linguistics source, NOT a human anchor.** It is a 1986 textbook, not an in-repo human-labeled empirical *resource* (no treebank, sense inventory, acceptability norm, or per-item annotation). Citing this page **discharges no empirical claim's human-anchor obligation**; it grounds the *vocabulary and the theoretical carving* (selection vs. modulation; sense relations) that a model's behavior may or may not line up with, never a result about a model. This is restated in "What it cannot ground."

## Provenance — what was fetched, from where, at what strength

**SECONDARY-ONLY. The primary was NOT consulted.** *Lexical Semantics* is an in-copyright Cambridge monograph. No legitimate open-access full text was found: the search-surfaced full-text copies (pdfcoffee, pdfroom, scribd, academia.edu, pdfdrive) are unauthorized mirrors of an in-print copyrighted book, which the project's ingest policy excludes exactly as it did for the Goldberg 1995, Croft 2001, and Firth 1957 primaries (no Sci-Hub, no pirate mirrors). The publisher page and Google-Books listing are preview/metadata only. Accordingly **every Cruse claim below is carried via named scholarly secondaries that quote or gloss Cruse 1986**, each flagged, and **no page number is asserted as verified against the book** except the single locator a secondary itself reports (and that too is flagged unverified).

**Secondary sources read (fetched 2026-06-26, text extracted with `pypdf`):**

- **Kilgarriff, A. 1997. "I don't believe in word senses." *Computers and the Humanities* 31(2): 91–113** (arXiv `cmp-lg/9712006`; the journal volume/pages are from the public record — the fetched arXiv preprint carries no journal pagination). A widely-cited lexical-semantics / WSD paper that opens its analysis from Cruse's textbook; it reproduces one short **direct quotation** of Cruse 1986 and reports one page locator. Quotes flagged "via Kilgarriff 1997."
- **Mohammad, S. & Hirst, G. 2012. "Distributional Measures of Semantic Distance: A Survey."** arXiv `1203.1858`. Glosses Cruse 1986 on what a lexical semantic relation is and which relations are systematic. Glosses flagged "via Mohammad & Hirst 2012."
- **Armendáriz, C.S., Purver, M., Ulčar, M., Pollak, S., Ljubešić, N. & Granroth-Wilding, M. 2020. CoSimLex (LREC 2020),** arXiv `1912.05320` — **already in-repo** as [`source/armendariz-2020-cosimlex`](armendariz-2020-cosimlex.md). Its "Contextual Modulation" section gives the fullest secondary exposition of Cruse's selection/modulation distinction. Glosses flagged "via Armendáriz et al. 2020 (CoSimLex)."

## Key passages

### Direct quotation of Cruse 1986 (one, via Kilgarriff 1997 — page not given by Kilgarriff)

**Q1 — the basic problem of lexical semantics.** Cruse 1986, block-quoted by Kilgarriff (1997, §3.1 "Selection and modulation"):

> "One of the basic problems of lexical semantics is the apparent multiplicity of semantic uses of a single word form (without grammatical difference)."

*(Secondary-strength: this is the one passage carried as **Cruse's own words**, reproduced by Kilgarriff as a block quotation. **Kilgarriff supplies no page number** for it, and the primary was not consulted, so no page is asserted. It states the explanandum the selection/modulation distinction is built to address.)*

**Q1-locator — autohyponymy.** Kilgarriff cites, with a page range, Cruse's discussion of *autohyponymy* (a general term that also has a more specific reading — e.g. *dog* covering "(male) dog" within "dog"):

> "The situation is a variant on autohyponymy (Cruse, 1986, pp 63–65) …"

*(Secondary-strength: the page range **pp. 63–65 is Kilgarriff's locator, reported here unverified against the book.** It is the only Cruse 1986 page number this page carries, and it is flagged as such.)*

### Glosses of Cruse's position (secondary authors' words, not Cruse quotations)

**Q2 — selection vs. modulation, stated in full.** Via Armendáriz et al. 2020 (CoSimLex), §"Contextual Modulation":

> "Within the field of lexical semantics, Cruse (1986) proposed an interesting compromise between those linguists that saw words as associated with a number of discrete senses and those that thought that the perceived discreteness of lexical senses is just an illusion. He distinguishes two different manners in which sentential context modifies the meaning of a word. First, the context can select for different discrete senses; if that is the case, the word is described as ambiguous, and the process is referred [to] as contextual selection of senses. … The second way in which context can modify the meaning of a word works within the scope of a single sense, modifying it in an unlimited number of ways by highlighting certain semantic traits and backgrounding others. This process is called contextual modulation of meaning, and the word is said to be general with respect to the traits that are being modulated. This effect is by nature not discrete but continuous and fluid …"

*(Secondary-strength: these are the **CoSimLex authors' words** characterizing Cruse, not a Cruse quotation. The ellipses elide the authors' worked examples — *bank* for selection; *cousin*, *butter* for modulation. "[to]" marks a typo-correction of the source's "referred as".)*

**Q3 — contextual normality as the selection mechanism.** Via Armendáriz et al. 2020 (CoSimLex):

> "Cruse (1986) sees the evaluation of contextual normality as the main mechanism for sense selection."

*(Secondary-strength: CoSimLex authors' gloss. Bears directly on the project's distributional null — see "Bearing.")*

**Q4 — a lexical semantic relation, and the systematic relations.** Via Mohammad & Hirst 2012:

> "According to Cruse (1986), a lexical semantic relation is a relation between lexical units—a surface form along with a sense. As he points out, the number of semantic relations that bind concepts is innumerable; but certain relations, such as hyponymy, meronymy, antonymy, and troponymy, are more systematic and have enjoyed more attention in the linguistics community."

*(Secondary-strength: Mohammad & Hirst's gloss of Cruse, not a Cruse quotation. Gives the **lexical unit = form + sense** definition and the systematic-relations inventory.)*

**Q5 — Cruse prefers "discrete vs. continuous variability" over the polysemy/homonymy terms.** Via Armendáriz et al. 2020 (CoSimLex):

> "A final interesting point about Cruse's view is that he doesn't find the contrast between polysemy and homonymy particularly helpful, and dislikes the use of these terms because they promote the idea that the primary semantic unit is some common lexeme and each of the different senses are just variants of it. He instead believes the primary semantic unit should be the lexical units, a union of a single sense and a lexical form, and finds it more useful to look at the contrast between discrete and continuous semantic variability."

*(Secondary-strength: CoSimLex authors' gloss, not a Cruse quotation. Load-bearing for "Bearing" below: Cruse's own preferred axis is **discrete vs. continuous semantic variability** — which is the selection/modulation axis, **not** the relatedness-between-senses axis the project's gradient runs on; and Cruse is reported to actively dislike the polysemy/homonymy labels the project uses as its internal control.)*

**Book coverage (catalogue-level, not page-located).** The Cambridge University Press description and standard reviews list the book's topics as idiomaticity, lexical ambiguity, synonymy, the hierarchical relations hyponymy and meronymy, and the varieties of oppositeness/antonymy. This is recorded at **catalogue level only** — no chapter or page is asserted, and no quotation of those chapters is carried.

## Bearing on this project

This source supplies the **lexicographic backbone** that [`concept/polysemy`](../concepts/polysemy.md) said was "pending the Cruse and Murphy ingestions." Its bearing is unusually direct, because Cruse's two-way carving lines up with the project's own lexical wedge:

- **Selection vs. modulation is a *different* cut from the project's relatedness gradient — keep them apart.** Cruse's *contextual selection of senses* (discrete, "ambiguous") vs. *contextual modulation* (within a single sense, "continuous and fluid," trait highlighting/backgrounding) is the **within-sense-vs-between-senses** axis — *generality* vs. *ambiguity*. This is **not** the **relatedness-between-senses** axis (unrelated homonyms vs. related polysemes) the project's graded usage-similarity instruments measure (**Usim/DWUG**; [`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md), [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md)). The two cuts cross: discrete-but-*related* senses — the *paper* = material/newspaper/article case, and Kilgarriff's autohyponymy *dog* example (Q1-locator), which he flags as a case where "there clearly are distinct senses" — are *selection* in Cruse's terms, **not** modulation. So Cruse's modulation does **not** equal the project's polysemy/gradience pole, and the two must not be identified. What Cruse contributes is **convergent, not identical**: a lexical semanticist's own refusal of clean sense boundaries — he is reported (Q5) to find the polysemy/homonymy contrast "particularly [un]helpful" and to prefer "the contrast between discrete and continuous semantic variability," treating discreteness as itself a matter of degree — which independently motivates "the gradiness is the point" from a different starting axis. (Cruse's WiC-measured discrete pole and the project's binary same/different test still line up at the *discrete* end; it is the *graded* end where the axes diverge.)
- **Cruse's own statement of the distributional null.** Q3 (selection by "contextual normality") together with the CoSimLex exposition's corollary that, since every word is general to some degree, "a word has a different meaning in every context in which it appears," is the **lexical-semantics-side statement of the project's distributional null** ([`concept/polysemy`](../concepts/polysemy.md) §"The distributional null"; [`concept/distributional-meaning`](../concepts/distributional-meaning.md)): apparent sense behavior may be context-normality / context-similarity all the way down. Cruse motivates *why* the project's context-similarity control is the design spine, not an afterthought — modulation is by Cruse's own account continuous with mere contextual variation.
- **Modulation as the lexical ancestor of constructional coercion.** Cruse's modulation (the context highlighting/backgrounding *traits within a single sense*) is the lexical-level cousin of [`concept/coercion`](../concepts/coercion.md)'s "the construction modifies the verb's reading" — the project's own "coercion-as-sense-modulation" bridge probe borrowed the term. The connection is an **analogy across levels** (lexical modulation vs. constructional coercion), flagged as such, not an identity.
- **`meaning-senses` justification.** Tagged `referential` because Cruse's object is **sense** — the lexical unit is "a surface form along with a sense" (Q4), and the sense-relation inventory (hyponymy, meronymy, antonymy) structures `referential.sense`, modes of presentation at fine grain. Co-tagged `distributional` because Cruse's method is **contextual/relational** — meaning read off the relations a unit contracts with its contexts (Q2, Q3), which is the lexical-semantics neighbour of the Firth/Harris distributional tradition ([`source/firth-1957-synopsis`](firth-1957-synopsis.md), [`source/harris-1954-distributional-structure`](harris-1954-distributional-structure.md)). Not tagged `referential.reference`/`referential.externalist`: Cruse's carving is within-sense and relational, not a reference-fixing or world-relation story.

## What it can ground

- The **selection vs. modulation** distinction (discrete sense-selection / ambiguity vs. within-sense modulation / generality) as the lexical-semantics vocabulary behind the project's polysemy-gradience wedge — at **secondary strength** (Q1, Q2).
- **Contextual normality as the selection mechanism** (Q3) as the lexical-semantics statement of the project's distributional null — **secondary strength**.
- The **lexical unit** (form + single sense) and the **systematic sense relations** (hyponymy, meronymy, antonymy, troponymy) as the descriptive backbone the polysemy concept page rests on — **secondary strength** (Q4), replacing that page's prior reliance on "common knowledge in the field."

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models, and no human-anchor obligation.** A 1986 textbook predates all of it. This is a **descriptive-theory source, NOT a human anchor**: it is not an in-repo human-labeled empirical *resource* (no graded usage-similarity ratings, sense annotations, or norms usable as a yardstick), and a `source` page is not an `anchors:` resource regardless. The project's graded human anchor remains **Usim/DWUG/CoSimLex-class data**, not Cruse. Citing this page discharges no empirical claim's human-anchor obligation.
- **Any page number except the flagged Kilgarriff locator (Q1-locator, pp. 63–65, autohyponymy), itself unverified against the book.** No chapter/page of the selection–modulation or sense-relations material is asserted, because the primary was not consulted.
- **Anything beyond what the three named secondaries carry.** The book's fuller treatments (e.g. the taxonomy of oppositeness, congruence relations, the syntagmatic delimitation of lexical units) are recorded only at catalogue level and are not quoted or grounded here.

## Known limits

- **Secondary-only; primary not consulted.** Mirrors the Firth 1957 / Goldberg 1995 / Croft 2001 precedent. Every Cruse claim is carried via Kilgarriff 1997, Mohammad & Hirst 2012, or Armendáriz et al. 2020; only Q1 is reproduced as Cruse's own words, and even it has no page.
- **Mixed status within "secondary."** Q1 is a direct Cruse quotation (via Kilgarriff); Q2–Q4 are the secondary authors' *glosses* of Cruse, not his words — flagged per-passage.
- **The famous contextualist thesis is deliberately NOT quoted.** Cruse 1986 is often summarized as holding that a word's meaning is fully reflected in / constituted by its contextual relations; this page does **not** quote that thesis, because no legitimate secondary reproduced it with a verifiable page in this session and the primary was not consulted. It is left as an un-quoted characterization, not asserted as a Cruse quotation.
- **Backlog.** Reaching a legitimate full text of *Lexical Semantics* should: re-verify Q1 against Cruse's own page; verify the pp. 63–65 autohyponymy locator; and pin the selection–modulation and sense-relation chapters to real page numbers (Firth/Fillmore precedent — promote provenance, do not re-ingest). **Murphy 2003** (*Semantic Relations and the Lexicon*) and **Lyons 1977** (*Semantics*) remain wanted as the finer-grained / classical companions ([`base/wanted.md`](../wanted.md)).
</content>
</invoke>
