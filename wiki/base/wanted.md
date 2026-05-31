# wanted.md — sources to fetch, prioritized

Tom has University of Tokyo library access. Anything here is something a run wanted but could not pull itself. Keep current — stale wants accumulate and become noise.

Format per entry:

```
- [priority] Author, Year. Title.
  why: one sentence — what this would let the project ground.
  status: wanted | requested | received | declined
  pages: (when received) page range needed, if not whole work.
```

`priority` is `P1` (next), `P2` (soon), `P3` (eventually).

## Founding reading list (charter §11.4)

These are seeds, not commitments — drop any that turn out not to bear on grammatical/constructional meaning.

### Lexical semantics — likely in-library, possibly OA

- [P2] Cruse, D.A. 1986. *Lexical Semantics.* Cambridge.
  why: baseline sense-relation vocabulary; benchmark for the gradiness wedge.
  status: wanted
- [P2] Murphy, M.L. 2003. *Semantic Relations and the Lexicon.* Cambridge.
  why: a more recent and finer-grained treatment of antonymy, hyponymy, meronymy as testable structures.
  status: wanted
- [P3] Lyons, J. 1977. *Semantics* (vols. 1–2). Cambridge.
  why: classical reference; only fetch chapters as a finding demands.
  status: wanted

### Constructional / cognitive

- [P1] Goldberg, A.E. 1995. *Constructions: A Construction Grammar Approach to Argument Structure.* Chicago.
  why: the canonical statement of constructions as form–meaning pairings; needed for `constructional` tag grounding.
  status: wanted
- [P1] Goldberg, A.E. 2006. *Constructions at Work.* OUP.
  why: usage-based extension; bridges to distributional anchors.
  status: wanted
- [P2] Croft, W. 2001. *Radical Construction Grammar.* OUP.
  why: cross-linguistic / typological framing of constructions.
  status: wanted

### Classics the LLM-meaning debate keeps invoking

- [P2] Putnam, H. 1975. "The Meaning of 'Meaning'." In *Mind, Language and Reality*, vol. 2. Cambridge.
  why: externalism; Twin Earth; the case the `referential.externalist` tag rests on.
  status: wanted
- [P3] Lewis, D. 1970. "General Semantics." *Synthese* 22.
  why: the Markerese argument — relevant to how we treat the form-vs-meaning line.
  status: wanted
- [P2] Evans, G. 1973. "The Causal Theory of Names." *Aristotelian Society Suppl.* 47.
  why: cited routinely in LLM-reference debates; check what survives.
  status: wanted
- [P3] Millikan, R.G. 1984. *Language, Thought, and Other Biological Categories.* MIT.
  why: teleosemantics; only fetch if a finding needs it.
  status: wanted
- [P3] Brandom, R.B. 1994. *Making It Explicit.* Harvard. (or *Articulating Reasons*, 2000.)
  why: the systematic statement of inferentialism — content fixed by an expression's position in a web of material inferences, not by prior relation to objects; grounds the philosophical framing cited as "not in-repo" in [`concept/inferential-meaning`](concepts/inferential-meaning.md). Fetch only if a finding leans on the normative-inferentialism distinction.
  status: wanted

### Firth / Harris originals

- [P2] Firth, J.R. 1957. "A synopsis of linguistic theory, 1930–55." In *Studies in Linguistic Analysis.* Blackwell.
  why: the "you shall know a word by the company it keeps" source — for the `distributional` tag.
  status: wanted
- [P2] Harris, Z.S. 1954. "Distributional Structure." *Word* 10(2–3): 146–162.
  why: the distributional hypothesis stated formally.
  status: wanted

### Current wave on LLMs and meaning

- [P1] Sterken, R.K. & Cappelen, H. (eds.). *Communicating with AI: Philosophical Perspectives.* OUP (forthcoming/recent).
  why: the most current edited volume on LLM-meaning specifically; central to where the debate is now.
  status: wanted
- [P1] Grindrod, J. *The Persuasive Machines? / Talking to Robots / [check current title].* (2024–25 monograph on LLMs and language).
  why: cited as a current systematic treatment; check actual title and pull intro + relevant chapters.
  status: wanted
- [P1] Piantadosi, S.T. & Hill, F. 2022. "Meaning without reference in large language models." NeurIPS workshop / arXiv 2208.02957.
  why: foundational for the `inferential` tag's application to LLMs. Likely OA — try to fetch directly first.
  status: received (2026-05-28, section-level quotes from arXiv abs + ar5iv HTML; 5 additional quotes added 2026-05-28 from "Communicative intentions" and "Discovering conceptual role" sections; see wiki/base/sources/piantadosi-hill-2022-meaning-without-reference.md)
- [P1] Bender, E. & Koller, A. 2020. "Climbing towards NLU: On meaning, form, and understanding in the age of data." ACL.
  why: the form-vs-meaning argument; sets up `grounded` and the octopus thought experiment. OA via ACL Anthology.
  status: received (2026-05-28, abstract verbatim from ACL Anthology + body quotes pp. 5187–5190 from prior PDF ingestion; full abstract added verbatim 2026-05-28; ACL Anthology offers PDF only, no HTML rendering; see wiki/base/sources/bender-koller-2020-climbing.md)
- [P1] Mahowald, K., Ivanova, A.A., Blank, I.A., Kanwisher, N., Tenenbaum, J.B., Fedorenko, E. 2024. "Dissociating language and thought in large language models." *Trends in Cognitive Sciences* 28(6).
  why: the formal-vs-functional competence frame.
  status: received (2026-05-28, section-level quotes from arXiv HTML 2301.06627v3; 7 additional quotes added 2026-05-28 covering functional competence definition, BLiMP benchmark, hierarchical structure, commonsense failure, theory of mind, and modularity agenda; see wiki/base/sources/mahowald-2024-dissociating.md)
- [P1] Lyre, H. 2024. "Understanding AI: Semantic grounding in large language models." arXiv 2402.10992.
  why: grounding-as-gradual, the basis for the `grounded.*` sub-tag structure.
  status: received (2026-05-28, page-level quotes from arXiv PDF pp. 1–14; no HTML version available; ar5iv redirect to abs page; PDF is binary-only via WebFetch; body quotes were extracted at prior ingestion step; no new quotes added 2026-05-28 due to HTML unavailability; see wiki/base/sources/lyre-2024-semantic-grounding.md)
- [P1] Weissweiler, L., et al. 2022–24 (multiple papers on CxG probing of LLMs).
  why: nearest existing line to this project's wedge.
  status: catalogued (2026-05-28, 2023 survey paper as primary entry; see wiki/base/sources/weissweiler-2023-cxg-insight.md). 2022 comparative-correlative paper now RECEIVED as its own page (2026-05-29; EMNLP 2022, arXiv 2210.13181; see wiki/base/sources/weissweiler-2022-comparative-correlative.md). A 2024 empirical paper remains uncatalogued — give it a page only if a finding cites it (avoid guessing which 2024 paper without verifying).
- [P2] Tayyar Madabushi, H., et al. on AANN and constructional probing.
  why: same line.
  status: received (2026-05-29, via Scivetti et al. 2025 — Tayyar Madabushi is senior author; see wiki/base/sources/scivetti-2025-beyond-memorization.md). NOTE: that paper covers 8 phrasal constructions but NOT AANN; the AANN-specific portion of this want is split out below.
- [P2] Scivetti, W., Tayyar Madabushi, H., et al. 2025. "Beyond Memorization: Assessing Semantic Generalization in LLMs Using Phrasal Constructions." IJCNLP-AACL 2025; arXiv 2501.04661.
  why: nearest recent empirical CxG-probing instance; tests caused-motion, conative, way-manner (3 of this repo's conjectures) with human comparison.
  status: received (2026-05-29, abstract from ACL Anthology + section-level body quotes from arXiv v1 HTML; see wiki/base/sources/scivetti-2025-beyond-memorization.md). Full PDF (pp. 1184–1201) holds per-construction + human-baseline numbers if a finding needs them.
- [P2] AANN-specific human probing: Mahowald 2023 "A discerning several thousand judgments…" (EACL) / Chronis et al. 2023.
  why: the AANN portion of the constructional-probing line that Scivetti et al. 2025 does NOT cover; needed if the AANN conjecture wants a CxG-native human anchor beyond the existing Mahowald 2023 stimulus suite.
  status: Mahowald 2023 RECEIVED as its own source page (2026-05-29; EACL, arXiv 2301.12564; see wiki/base/sources/mahowald-2023-aann-judgments.md — argument/findings; dataset on resource/mahowald-2023-aann-stimuli). Chronis et al. 2023 still wanted (fetch only if a finding cites it).

### Relational / dyadic-interaction anchors (for the relational-meaning pilot)

These would supply the human dyadic-interaction anchor the [`open-question/relational-meaning-pilot`](../findings/open-questions/relational-meaning-pilot.md) needs before any relational result can be promoted. **Anchor decision RESOLVED 2026-05-29** (`decisions/resolved/relational-anchor-shortlist`, Option A): Clark & Wilkes-Gibbs 1986 is the ratified empirical anchor + Pickering & Garrod 2004 the theoretical backdrop — so the first two below are now the **priority fetches** (the other two are no longer needed unless the pilot's emphasis shifts).

- [P1] Clark, H.H. & Wilkes-Gibbs, D. 1986. "Referring as a collaborative process." *Cognition* 22(1): 1–39. **← RATIFIED ANCHOR (fetch first).**
  why: the canonical tangram-naming convergence paradigm; dyads collaboratively coin and compress shared labels over rounds — the closest human analogue to the iterated-reference-game pilot. Ratified as the empirical anchor; the pilot cannot promote a result until this is in-repo.
  status: wanted (priority)
- [P2] Brennan, S.E. & Clark, H.H. 1996. "Conceptual pacts and lexical choice in conversation." *Journal of Experimental Psychology: LMC* 22(6): 1482–1493. **← added 2026-05-31 (Tom, decision `relational-fetchable-anchor`).**
  why: the human result that most directly *motivates* the pilot's live-vs-shuffled discriminator — lexical entrainment is shown to be **historical** (not merely salience-driven) and **partner-specific**, the human-side analogue of "live ≠ shuffled." Complements C&W-G 1986. A fetchable derived/aggregate baseline is now available via the Hawkins tangrams corpus ([`decisions/resolved/relational-fetchable-anchor`](../decisions/resolved/relational-fetchable-anchor.md), Option A).
  status: wanted
- [P3] Krauss, R.M. & Weinheimer, S. 1964/1966. Reference-phrase-shortening studies.
  why: the earlier convergence-curve studies the entrainment measure would be calibrated against.
  status: wanted
- [P3] HCRC Map Task corpus (Anderson et al. 1991).
  why: corpus-grade anchor for referential alignment / entrainment in goal-directed dyads.
  status: wanted
- [P2] Pickering, M.J. & Garrod, S. 2004. "Toward a mechanistic psychology of dialogue." *Behavioral and Brain Sciences* 27(2). **← RATIFIED theoretical backdrop.**
  why: the "interactive alignment" framework — theoretical anchor for what alignment-across-levels predicts (and what it does not claim about meaning-constitution).
  status: wanted

### Graded usage/sense-similarity anchor (for the lexical-sense-gradience conjecture)

The lexical conjecture's anchor decision RESOLVED 2026-05-29 ([`decisions/resolved/lexical-sense-gradience-anchor`](../decisions/resolved/lexical-sense-gradience-anchor.md), **Option B**: a different graded set, NOT Usim — Usim is unfetchable/unlicensed). Need a graded, released, licensed usage/sense-similarity set to ground the monotonicity clause:

- [P1] DWUG — Diachronic Word Usage Graphs (Schlechtweg et al.). Graded human usage-similarity judgments (4-point DURel/Usim tradition), **CC BY-ND 4.0** (corrected 2026-05-30 from 'CC BY' after verification — analysis + verbatim mirroring OK, distributing a modified/augmented version is not; see wiki/base/resources/dwug-usage-graphs.md), on Zenodo. **← leading Option-B candidate (verify license + scale + counts + fetchability, then mirror to experiments/data/ + write a resource page).**
  why: the load-bearing graded anchor the monotonicity clause needs; well-licensed and available (unlike Usim).
  status: catalogued (2026-05-30 — resource page created: wiki/base/resources/dwug-usage-graphs.md; see page for the license / scale / counts / fetchability / fit verification breakdown)
- [P2] CoSimLex (SemEval-2020 Task 3). Graded human ratings of word similarity in context; released.
  why: alternative graded in-context similarity anchor if DWUG does not fit.
  status: wanted

### Multimodal / grounded anchors (for the new multimodal / physical-AI axis)

Scouted 2026-05-30 ([`base/resources/multimodal-anchor-scouting.md`](resources/multimodal-anchor-scouting.md)); license + URL verified, data not yet fetched. The axis's anchor-class choice is surfaced in [`decisions/resolved/multimodal-panel-and-grounding-theory`](../decisions/resolved/multimodal-panel-and-grounding-theory.md) (Q3).

- [P1] Lancaster Sensorimotor Norms (Lynott, Connell, Brysbaert, Brand & Carney 2020). OSF https://osf.io/7emr6/. CC BY 4.0 (verified). 39,707 words × 11 perceptual/action dimensions, ~3,500 raters.
  why: the cheapest first multimodal unit — a **text-side perceptual-grounding moderator on the existing DWUG lexical result** (does monotonicity strengthen for perceptually grounded words?). Joins the lexical program to the grounded axis; $0, no new probe; a plain data download.
  status: catalogued (2026-05-30 — fetched + checksummed and resource page created: wiki/base/resources/lancaster-sensorimotor-norms.md; see page for the license / dimensions / counts / fetchability / fit verification breakdown)
- [P2] THINGS-data behavioral triplet judgments (Hebart et al., eLife 2023). OSF https://osf.io/f5rn6/. CC0 (via the eLife publication; OSF README not directly inspected).
  why: 4.7M graded human object-similarity judgments — the strongest multimodal *behavioral* anchor if a VLM image-input comparison axis opens (Q3 Option B). Needs a probe design + budget.
  status: wanted (scouted 2026-05-30; CC0 via secondary source; verify OSF README before cataloguing as a typed resource).
- [P3] NLVR2 annotations (Suhr et al. 2019). https://github.com/lil-lab/nlvr. CC BY 4.0 (annotations; images via Google Form).
  why: 107k fully human-written sentences + binary labels over image pairs; cleanest human provenance in image-text entailment; relevant if a VLM constructional-inference axis opens.
  status: wanted (scouted 2026-05-30; annotation license verified).

### Theory / philosophy-of-meaning primary texts (added 2026-05-31, theory session)

The 2026-05-31 theory wave wrote five established-position concept pages that **characterize** these works (no quotes, no page numbers — flagged "(not in-repo; characterization)"). Fetch the load-bearing ones if a later finding needs to quote or pin a position. (Putnam 1975, Evans 1973, Brandom 1994, Lewis 1970, Firth 1957, Harris 1954 are already listed above and are not repeated here.)

- [P2] Wittgenstein, L. 1953. *Philosophical Investigations.*
  why: the meaning-as-use pole (language-games, "look for the use," family resemblance) — the Wittgensteinian half of [`base/concepts/truth-conditional-and-use-meaning.md`](concepts/truth-conditional-and-use-meaning.md); also the ancestor of prototype theory's family-resemblance categories.
  status: wanted
- [P3] Frege, G. 1892. "Über Sinn und Bedeutung" ("On Sense and Reference").
  why: the sense/reference distinction + the root of the truth-conditional pole and the principle of compositionality; underpins `truth-conditional-and-use-meaning` and [`base/concepts/compositionality.md`](concepts/compositionality.md).
  status: wanted
- [P3] Tarski, A. 1933/1944. "The Concept of Truth in Formalized Languages" / "The Semantic Conception of Truth."
  why: the recursive truth-via-satisfaction definition the model-theoretic lineage is built on.
  status: wanted
- [P3] Davidson, D. 1967. "Truth and Meaning." *Synthese* 17. (Reprinted with his holism essays in *Inquiries into Truth and Interpretation*, 1984.)
  why: "meaning = truth-conditions" as a theory of meaning (truth-conditional pole); *Inquiries* also carries the holism-of-the-mental that grounds [`base/concepts/semantic-holism.md`](concepts/semantic-holism.md).
  status: wanted
- [P3] Montague, R. 1973. "The Proper Treatment of Quantification in Ordinary English" (PTQ); and Partee, B.H. on compositionality (e.g. *Mathematical Methods in Linguistics*, 1990).
  why: natural language as a formal language with homomorphic syntax→semantics — compositional truth-conditional semantics in its strongest form; for `compositionality`.
  status: wanted
- [P2] Fillmore, C.J. 1982. "Frame Semantics" (in *Linguistics in the Morning Calm*); and 1985. "Frames and the semantics of understanding." *Quaderni di Semantica* 6.
  why: frame semantics as the semantic backbone of Construction Grammar (Fillmore founds both) — the tie between the lexical and grammatical wedges at the level of semantic theory; for [`base/concepts/frame-and-prototype-semantics.md`](concepts/frame-and-prototype-semantics.md).
  status: wanted
- [P3] Rosch, E. 1975. "Cognitive representations of semantic categories." *J. Exp. Psychol. General* 104; and Rosch, E. & Mervis, C.B. 1975. "Family resemblances." *Cognitive Psychology* 7.
  why: the prototype / graded-category experiments the lexical-gradience mapping leans on; for `frame-and-prototype-semantics`.
  status: wanted
- [P3] Lakoff, G. 1987. *Women, Fire, and Dangerous Things.* Chicago.
  why: radial categories / radial-network treatment of polysemy; for `frame-and-prototype-semantics` and [`base/concepts/polysemy.md`](concepts/polysemy.md).
  status: wanted
- [P2] Quine, W.V.O. 1951. "Two Dogmas of Empiricism"; and 1960. *Word and Object.*
  why: confirmation/meaning holism — the source of the holist pole; for `semantic-holism`.
  status: wanted
- [P3] Dummett, M. 1975/76. "What is a Theory of Meaning?" (I & II).
  why: molecularism — the middle position between atomism and holism; for `semantic-holism`.
  status: wanted
- [P2] Fodor, J.A. & Lepore, E. 1992. *Holism: A Shopper's Guide.* Blackwell.
  why: the anti-holism argument + the claim that holism threatens compositionality, communication, and stability of meaning; bears on both `semantic-holism` and `compositionality`.
  status: wanted
- [P2] Bender, E.M., Gebru, T., McMillan-Major, A. & Shmitchell, S. 2021. "On the Dangers of Stochastic Parrots." FAccT.
  why: the eliminativist-leaning origin of the "stochastic parrot" framing — the foil for [`base/concepts/deflationary-and-eliminativist-llm-meaning.md`](concepts/deflationary-and-eliminativist-llm-meaning.md). (The phrase currently appears in-repo only inside the verbatim Lyre quote.)
  status: wanted
- [P3] Cappelen, H. & Dever, J. 2021. *Making AI Intelligible: Philosophical Foundations.* OUP.
  why: a worked deflationary/anti-anthropomorphic treatment of AI content/reference; for `deflationary-and-eliminativist-llm-meaning`. (Complements the already-listed Sterken & Cappelen ed. volume.)
  status: wanted

## Notes on fetching

- **Try open-access first.** ACL Anthology, arXiv, preprint pages, lab pages — many of the LLM-meaning items above are OA and a run can fetch them via `WebFetch`. Only escalate to Tom when paywalled.
- **Page-level provenance, not wholesale text.** When a source is ingested into `wiki/base/sources/`, the page records summary + exact short quotes with page numbers, not the source itself.
