---
type: source
id: dummett-1975-what-is-a-theory-of-meaning
title: "What is a Theory of Meaning? (I, 1975; II, 1976)"
authors:
  - Dummett, Michael
year: 1975
venue: "(I) in S. Guttenplan (ed.), Mind and Language (Oxford: OUP, 1975), pp. 97–138; (II) in G. Evans & J. McDowell (eds.), Truth and Meaning: Essays in Semantics (Oxford: Clarendon, 1976). Both reprinted in The Seas of Language (Oxford: Clarendon, 1993), chs. 1–2 (pp. 1–93)."
url: https://global.oup.com/academic/product/the-seas-of-language-9780198236214
access: in-copyright-fair-use
meaning-senses:
  - inferential
  - distributional
status: received
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: refines
    target: concept/semantic-holism
  - rel: depends-on
    target: source/quine-1951-two-dogmas
---

# Dummett 1975/76 — What is a Theory of Meaning? (I and II)

## What it is

Michael Dummett's two-part essay "What is a Theory of Meaning?" — part **(I)** in S. Guttenplan (ed.), *Mind and Language* (OUP, 1975), pp. 97–138; part **(II)** in G. Evans & J. McDowell (eds.), *Truth and Meaning: Essays in Semantics* (Clarendon, 1976) — both reprinted in *The Seas of Language* (Clarendon, 1993) as chapters 1 and 2. This pair is the **founding statement of semantic molecularism**: the middle position on the holism axis that a theory of meaning should assign each expression a content graspable from a *bounded* body of knowledge, so that language is learnable piecemeal and a speaker can fully understand some of the language without understanding all of it — more structure than atomism, less than holism.

It fills an explicitly-named gap. Before this page, [`concept/semantic-holism`](../concepts/semantic-holism.md) cited Dummett's molecularism only as "(not in-repo; characterization)". This page closes that gap **at primary strength** (see provenance): the relevant chapters of *The Seas of Language* were reached as a readable full-text PDF this session and the four load-bearing quotes below were extracted and verified character-for-character against it. Where a position is carried via a secondary source (the holism-framing and the Fodor & Lepore objection), that is flagged per-quote.

It is a **theory source, NOT a human anchor.** It is a 1970s philosophy-of-language essay, not an in-repo human-labeled empirical *resource* (no treebank, sense inventory, acceptability norm, or per-item annotation). Citing this page **discharges no empirical claim's human-anchor obligation**; it grounds the *theory* (the molecularist position on the holism axis) that a model may or may not instantiate, never a result about a model. This is restated in "What it cannot ground."

## Provenance — what was fetched, from where, at what strength

**One open-access primary attempt was made, and it succeeded.** A full-text PDF of *The Seas of Language* (Clarendon, 1993), which reprints both essays as chapters 1–2, was downloaded 2026-06-26 from a `free.fr` mirror (`philosophieweb0.001.free.fr/Dummett,...The Seas of Language 1996.pdf`, HTTP 200, 2.6 MB, 312 pages, PDF v1.4). Text was extracted with `pdfminer.six` (after working around a broken `cryptography`/cffi backend in the environment by shadowing the unused cipher imports — the PDF is unencrypted, so no cipher code executed). The extraction is clean machine-set text (1.64 M chars), **not** an OCR scan; it preserves the book's own running page markers (`end p.1`, `end p.21`, …), which were used to pin page numbers below. Every quoted span was matched against the extracted text; the only normalization applied was collapsing the run-of-spaces artifact pdfminer introduces between words (no word was altered, inserted, or dropped).

**Citation/locator notes and caveats:**

- The page numbers below are *Seas of Language* (1993) pagination, read from the book's own embedded `end p.N` markers — **not** the original 1975 *Mind and Language* (pp. 97–138) or 1976 *Truth and Meaning* pagination. The book's table of contents (verified in the extracted text) places essay **(I)** at pp. 1–33 and essay **(II)** at pp. 34–93. Quotes are attributed to (I) vs (II) by which page-range they fall in.
- The source is **in-copyright**; this is fair-use quotation of four short passages, with the full text neither stored in-repo nor reproduced. The `free.fr` mirror's legality is not vouched for; only short quotations are carried here and they were independently locatable by page in the verified text.
- The book's 1993 **Introduction** (roman-numeral pages iii–xx) is Dummett's *later retrospective voice*, not the 1975/76 essays. Quotes below are drawn from the essays proper (arabic pages 1–93); the Introduction is **not** quoted as if it were the original argument, to avoid backdating Dummett's 1993 reformulations onto the founding papers.
- **The manifestation demand** in its sharpest later form ("understanding must be *fully* manifested in use") is most explicit in the 1993 Introduction and in Dummett's later work; the essays (II) state the *manifestation requirement on a theory of sense* (Q4 below) but the specific "fully manifest" sharpening is flagged as later. This page quotes only what the essays say and flags the rest.

**Secondary sources read (carried-via-secondary, for the holism-framing and the objection):**

- SEP, "Meaning Holism" (`plato.stanford.edu/entries/meaning-holism/`), fetched 2026-06-26 — for the molecularism *definition*, the citation tying the piecemeal-learning problem to Dummett, the meaning-constitutive-inference problem, and the Fodor & Lepore objection. Quotes flagged "carried via SEP 'Meaning Holism'".
- SEP, "Challenges to Metaphysical Realism" (`plato.stanford.edu/entries/realism-sem-challenge/`), fetched 2026-06-26 — for the manifestation-challenge framing (there is no standalone "Michael Dummett" SEP entry; the manifestation material lives here). Its manifestation passages are largely the SEP author's synthesis of the anti-realist position; only the bracketed `[Dummett 1978]`-attributed line is quoted as Dummett's, and it is flagged as Dummett *1978*, not 1975/76.

## Key passages

### Primary (verified against the extracted Seas of Language text)

**Q1 — Molecularism as the conclusion of essay (I): a theory of meaning must be molecular, not holistic.** Essay **(I)**, *Seas of Language* p. 21:

> "I conclude, therefore, that a theory of meaning, if one is to be possible at all, must accord with an atomistic, or at least a molecular, conception of language, not a holistic one; that it must be full-blooded, not modest, and rich, not austere."

*(Primary-strength: verified in the extracted text, essay (I), at the `end p.21` marker.)* This is the founding molecularist thesis in Dummett's own voice: between atomism and holism, the theory of meaning must be *at least* molecular and must not be holistic.

**Q2 — The piecemeal-learning / "knowing part of a language" argument against holism.** Essay **(I)**, *Seas of Language* p. 32:

> "For holism, language is not a many-storeyed structure, but, rather, a vast single-storeyed complex; its difficulties in accounting for our piecemeal acquisition of language result from the fact that it can make no sense of the idea of knowing part of a language."

*(Primary-strength: verified, essay (I), between the `end p.32` and `end p.33` markers.)* This is molecularism's positive motivation, stated by Dummett directly: because language is acquired piecemeal — because it makes sense to know *part* of a language — a theory of meaning must be molecular, since holism "can make no sense of the idea of knowing part of a language."

**Q3 — The atomistic / molecular distinction, defined.** Essay **(II)**, *Seas of Language* p. 37:

> "If a theory correlates a specific practical capacity with the knowledge of each axiom governing an individual word, that is, if it represents the possession of that capacity as constituting a knowledge of the meaning of that word, I shall call it atomistic; if it correlates such a capacity only with the theorems which relate to whole sentences, I shall call it molecular."

*(Primary-strength: verified, essay (II), between `end p.37` and `end p.38`.)* This is Dummett's own technical definition of the molecular/atomistic contrast in terms of the unit a theory of meaning ties practical capacity to: per-word (atomistic) vs. whole-sentence (molecular).

**Q4 — The manifestation requirement on a theory of sense.** Essay **(II)**, *Seas of Language* p. 41 (the quote spans the `end p.41` page break, reproduced inline):

> "I have argued that an acceptable theory of meaning must be at least end p.41 molecular; its theory of sense must state how a speaker's knowledge of the meaning of any sentence is manifested."

*(Primary-strength: verified, essay (II); the embedded "end p.41" is the book's own page marker falling inside the quoted span and is reproduced verbatim, not inserted by this page.)* The molecular theory carries a manifestation demand: its theory of sense must say *how* a speaker's knowledge of a sentence's meaning is **manifested** — i.e. cashed out in observable use.

### Secondary (carried via SEP; primary not consulted for these framings)

**S1 — The molecularism definition (the middle position).** Carried via SEP, "Meaning Holism," §1 "General characterization of the view":

> "Meaning holism is typically contrasted with _atomism_ about meaning (where each word's meaning is independent of every other word's meaning), and _molecularism_ about meaning (where a word's meaning is tied to the meanings of some comparatively small subset of other words in the language—such as "kill" being tied to "cause" and "die" or "if … then…" being tied to "not" and "or")."

*(Carried via SEP "Meaning Holism" §1 — the secondary author's framing, not a Dummett quote. Matches [`concept/semantic-holism`](../concepts/semantic-holism.md)'s "privileged, bounded subset" formulation.)*

**S2 — The piecemeal-learning problem, tied to Dummett by SEP.** Carried via SEP, "Meaning Holism," §3.2.1 "Problems from Instability":

> "**Language Learning.** Learning a language would be problematic, since it seems as if one couldn't learn _any part_ of a given language until one had mastered _all_ of it. (Dummett 1973: 597–600, 1976: 44, 1991: 221, see also Bilgrami 1986, Dresner 2002, Jönsson 2014)"

*(Carried via SEP "Meaning Holism" §3.2.1 — SEP's statement of the problem, with SEP's citation to Dummett. The page numbers "1973: 597–600, 1976: 44, 1991: 221" are **SEP's locators, not verified by this page**; they point to Dummett's *Frege: Philosophy of Language* (1973), the 1976 essay, and *The Logical Basis of Metaphysics* (1991), not to the Seas of Language pagination used for Q1–Q4. The corresponding *primary* statement, verified, is Q2.)*

**S3 — The unsolved problem molecularism inherits: which inferences are meaning-constitutive, and the analytic/synthetic line.** Carried via SEP, "Meaning Holism," §2.2 "Indirect Arguments":

> "Molecularist theories typically try to keep the idea that meaning is tied to inferential role, but insist that only _some_ of the inferences involved with a term constitute its meaning. However, drawing a clear line between the meaning-constitutive and non-meaning-constitutive inferences/beliefs seems to commit one to a version of the analytic/synthetic distinction that has been out of favor since Quine's attack on it (Quine 1951),[7] and it is a familiar criticism of molecularism that it is an unstable resting point between atomism and holism, so that once you give up the former, it is difficult, if not impossible, to find compelling reasons not to move all the way to the latter (Fodor and Lepore 1992, but see Devitt 1996)."

*(Carried via SEP "Meaning Holism" §2.2 — SEP's words, not Dummett's. This is the load-bearing secondary passage: it names both the inherited problem — *which* inferences are constitutive — and its connection to the analytic/synthetic distinction Quine attacked, which is why this page carries a `depends-on` link to [`source/quine-1951-two-dogmas`](quine-1951-two-dogmas.md). It also states the Fodor & Lepore "unstable resting point" objection to molecularism.)*

## Bearing on this project

This page is the in-repo primary behind the **molecularism** bullet of [`concept/semantic-holism`](../concepts/semantic-holism.md), which owns the holism axis for the project.

- **Why the axis matters here.** The concept page's central tension is that the strongest pro-LLM-meaning position in the repo — conceptual-role / inferential semantics ([`concept/inferential-meaning`](../concepts/inferential-meaning.md)) — is *holist by its own statement*, and distributional models ([`concept/distributional-meaning`](../concepts/distributional-meaning.md)) are *holist by construction*. Molecularism is the position that *wants* the benefits of inferential-role meaning without paying holism's price. Q1 and Q2 are the founding statement of that wanting; Q3 is its technical shape; S3 is the problem it inherits.
- **The manifestation hook for LLMs (PROJECT'S INTERPRETIVE BRIDGE, NOT A DUMMETT CLAIM ABOUT MACHINES).** Dummett's manifestation requirement (Q4) is that knowledge of meaning must be cashed out in observable *use*. The project's interest is that an LLM's "meaning" is only ever read off observable use — there is nothing else to read it off. This makes Dummett's demand unusually apt for the LLM case: a Dummettian molecularist would say there is no meaning that outruns what the system can be observed to do. **This is the project's interpretive bridge, flagged explicitly as such — Dummett (writing in the 1970s) makes no claim about machines, and Q4 is a claim about human speakers and theories of meaning, not about models.** Do not cite this page as Dummett saying anything about LLMs.
- **The unsolved problem the project inherits too.** S3's "which inferences are meaning-constitutive" question re-invokes the analytic/synthetic distinction. The same problem sits inside [`meaning-senses.md`](../../meaning-senses.md)'s open issue — whether `distributional` and `inferential` collapse — and inside the concept page's "load-bearing assumption" that the project's comparisons presuppose enough shared content to range over. Molecularism does not solve this for the project; it names the seam.
- **`meaning-senses` justification.** Tagged `inferential` because molecularism is a thesis about *inferential role* — Dummett's molecular theory ties content to the inferences/connections a bounded subset of the language licenses (Q3 defines it via what a theory correlates with whole-sentence theorems; S3 makes the "only some inferences constitute meaning" claim explicit). Co-tagged `distributional` deliberately, matching [`concept/semantic-holism`](../concepts/semantic-holism.md)'s own tags: for the project's models the "bounded subset of connections" molecularism privileges and the distributional co-occurrence web are the *same object* at the model level, so the distributional reading rides on every use of this source. The 1970s essays are pre-distributional-semantics; the tag marks the *project-side* live alternative, not Dummett's own framework. Not tagged `referential`: these essays bear on the holism/molecularism axis, not on reference-fixing.

## What it can ground

- The **theory** of semantic molecularism as the middle position on the holism axis (meaning fixed by a bounded subset of an expression's connections; language learnable piecemeal; understanding manifest in use), at **primary strength** for Q1–Q4, as the founding statement [`concept/semantic-holism`](../concepts/semantic-holism.md)'s molecularism bullet rests on.
- The **piecemeal-learning argument against holism** (Q2) as molecularism's positive motivation — primary-strength.
- The **problem molecularism inherits** (which inferences are meaning-constitutive; re-invocation of the analytic/synthetic distinction Quine attacked; the Fodor & Lepore "unstable resting point" objection), at **secondary strength** via SEP "Meaning Holism" §2.2 (S3), connecting to [`source/quine-1951-two-dogmas`](quine-1951-two-dogmas.md).

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models, and no human-anchor obligation.** The essays predate all of it. This is a **theory source, NOT a human anchor**: it is not an in-repo human-labeled empirical *resource* (no treebank, sense inventory, acceptability norm, or per-item annotation usable as a yardstick), and a `source` page is not an `anchors:` resource regardless. Citing this page **discharges no empirical claim's human-anchor obligation.** The manifestation-to-LLM connection in "Bearing" is the *project's* interpretive bridge, marked as such — not a Dummett claim about machines.
- **The 1975 (Mind and Language, pp. 97–138) or 1976 (Truth and Meaning) original pagination.** The verified page numbers (Q1–Q4) are *Seas of Language* (1993) pages read from the book's own markers. A session needing the original venue pagination must reach those venues and re-verify.
- **The SEP locators "Dummett 1973: 597–600, 1976: 44, 1991: 221" (S2).** Those are SEP's citations to three different Dummett works (the 1973 *Frege*, the 1976 essay, the 1991 *Logical Basis of Metaphysics*), **not verified by this page** and **not** the Seas of Language pages used for Q1–Q4. The verified primary statement of the same point is Q2.
- **The "fully manifest in use" sharpening as a 1975/76 claim.** Q4 states the manifestation requirement on a theory of sense; the stronger "understanding must be *fully* manifested in use" formulation is most explicit in Dummett's 1993 Introduction and later work, and is flagged as later, not quoted here as if from the founding essays.

## Known limits

- **Primary reached via a non-authoritative mirror.** The full text came from a `free.fr` mirror whose legality is not vouched for; this page carries only four short fair-use quotations, each independently locatable by page in the verified text. The full text is not stored in-repo.
- **Pagination is the 1993 reprint's, not the original venues'.** Flagged per-quote; the original 1975/76 page numbers are not asserted.
- **Mixed strength.** Q1–Q4 are primary-strength (verified in extracted text). S1, S2, S3 are secondary-strength (SEP framings and SEP's own citations); the Fodor & Lepore objection and the analytic/synthetic connection are carried only via SEP, not from the primary. The split is flagged per-quote.
- **Secondary text-extraction note.** pdfminer inserts run-of-spaces between words; quoted spans were normalized by collapsing those runs only (no word altered/added/dropped). One quote (Q4) contains the book's own embedded `end p.41` page marker inside the quoted span, reproduced verbatim and flagged.
- **Backlog.** Verifying Q1–Q4 against the original 1975 *Mind and Language* / 1976 *Truth and Meaning* pagination, and reaching Dummett's *own* statement of the piecemeal-learning argument at the SEP-cited 1973/1991 locators (S2), remain open if original-venue citation is ever needed.
