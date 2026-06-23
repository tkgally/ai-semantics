# wanted.md — the project's own source backlog, prioritized

> **Repurposed 2026-06-12 (autonomous era, charter §12.4 — pure autonomy).** This is no longer a
> fetch-request channel to Tom; no human fetches anything. It is the project's **own** backlog of
> sources to ingest. A session picks an item, tries to fetch it from open-access channels (arXiv,
> ACL Anthology, publisher OA, author self-archives), and either catalogues it into
> `base/sources/` or marks it `unreachable`. Unreachable items stay listed for the record; they
> may be *characterized* from reliable secondary literature (clearly flagged, never quoted as if
> read) or satisfied by an open-access alternative — never fabricated around.

Keep current — stale wants accumulate and become noise.

Format per entry:

```
- [priority] Author, Year. Title.
  why: one sentence — what this would let the project ground.
  status: wanted | received | unreachable | declined
  pages: (when received) page range needed, if not whole work.
```

`priority` is `P1` (next), `P2` (soon), `P3` (eventually). Entries below predating 2026-06-12 may
still say `requested` (the old to-Tom status); treat those as `wanted`.

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
- [P1] Grindrod, J. (2024–25 work on LLMs and language).
  why: cited as a current systematic treatment; check actual title and pull intro + relevant chapters.
  status: **RECEIVED** (2026-06-14 — the on-point item is Grindrod, J. 2024. "Large language models and linguistic intentionality." *Synthese* 204:71 (arXiv 2404.09576); catalogued as [`wiki/base/sources/grindrod-2024-linguistic-intentionality.md`](sources/grindrod-2024-linguistic-intentionality.md) — abstract + 6 §-located body quotes verified character-for-character against the accepted-version PDF). The backlog entry's tentative titles were not this paper. **Still uncatalogued** (fetch only if a finding needs them): Grindrod's *Philosophical Studies* 2026 "Modelling Language using Large Language Models," and his chapter (with J.D. Porter & Nat Hansen) in the Sterken & Cappelen *Communicating with AI* volume listed above.
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
- [P1] Baggio, G. & Murphy, E. 2024. "On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen." arXiv 2406.00159.
  why: the published **internalist** rebuttal to Mandelkern & Linzen 2024 — contests both the "natural-histories-suffice" grounding move and the corpus-membership reading; the in-repo counter-pole to the strongest pro-reference argument, and the source revision-trigger (d) of the sixth essay wanted.
  status: **RECEIVED** (2026-06-15; catalogued as [`wiki/base/sources/baggio-murphy-2024-internalist-rejoinder.md`](sources/baggio-murphy-2024-internalist-rejoinder.md) — 8 §-located quotes incl. the "neither LMs nor 'their words' refer" bottom line, verified character-for-character against the arXiv PDF via pdfminer; arXiv preprint, peer-review status unconfirmed at fetch time).
- [P2] Ostertag, G. 2025. "Language Models and Externalism: A Reply to Mandelkern and Linzen." *Computational Linguistics* 51(2):651–659 (ACL Anthology 2025.cl-2.8; DOI 10.1162/coli_a_00551).
  why: the **externalist-side** reply to Mandelkern & Linzen — argues a term's "natural history" does not generally ground its referential properties; the complement to the internalist rejoinder catalogued above.
  status: **RECEIVED** (2026-06-15; catalogued as [`wiki/base/sources/ostertag-2025-externalist-reply.md`](sources/ostertag-2025-externalist-reply.md) — 10 page-located quotes incl. the §3 "externalism, as understood by Mandelkern and Linzen, cannot ground reference" verdict and the §4 conditional-accepted/antecedent-doubted statement, verified character-for-character against the publisher PDF via pdfminer; peer-reviewed CL version of record). **Correction to the framing it was queued under:** Ostertag is **not** a *defense* of M&L and **not** an internalist — he is an *intramural externalist* who argues M&L's particular "naïve externalist" route fails on its own terms (contrastive-explanation test, the H2O-vs-oxygen difference-maker); the M&L link is `contradicts`, not `supports`. He does **not** cite or engage Baggio & Murphy.

**2025–2026 OA finds on whether/which "meaning"-sense LLMs have (literature refresh, 2026-06-12 — found, abstracts checked, not catalogued):**

- [P2] Schuele, M. 2024/2025. "On the Semantics of Large Language Models." *Intellectica* 81: 15–36 (2024); arXiv 2507.05448 (July 2025).
  why: applies classical Frege/Russell semantic theory to LLM word- and sentence-level representations — directly on the `referential` vs. `distributional` boundary; abstract fetched verbatim 2026-06-12, full text not read.
  status: **RECEIVED** (2026-06-12; catalogued as [`wiki/base/sources/schuele-2025-semantics-of-llms.md`](sources/schuele-2025-semantics-of-llms.md) — abstract + 7 section-level quotes verbatim-verified against arXiv HTML v1; the Intellectica original was not consulted).
- [P2] Millière, R. & Buckner, C. 2024. "A Philosophical Introduction to Language Models — Part I: Continuity with Classic Debates." arXiv 2401.03910.
  why: the standard survey connecting LLM-meaning disputes to the classic debates the project's concept pages characterize; useful as a map, not an anchor.
  status: **RECEIVED** (2026-06-13; catalogued as [`wiki/base/sources/milliere-buckner-2024-philosophical-intro-i.md`](sources/milliere-buckner-2024-philosophical-intro-i.md) — abstract + 7 section-level quotes verbatim-verified against the ar5iv HTML rendering of arXiv v1; arxiv.org/html returns 404 for this paper. **Part II, arXiv 2405.03207, is ALSO received** — catalogued same session as [`wiki/base/sources/milliere-buckner-2024-philosophical-intro-ii.md`](sources/milliere-buckner-2024-philosophical-intro-ii.md) (the earlier "uncatalogued backlog" note here was stale; corrected 2026-06-14). **Open verification item — RESOLVED 2026-06-14.** The two later-section quotes (§3.2 "fluent mimicry of experience reports" and §4 "supports a broadly negative answer") that the 2026-06-13 ar5iv pass could not reach — every HTML route (ar5iv, arxiv.org/html) truncates this long paper, ar5iv cutting off mid-§3.1.2 — were independently re-verified verbatim against the arXiv PDF (`https://arxiv.org/pdf/2405.03207`, extracted locally with pdfminer). Both strings found character-for-character with their stated locators (§3.2 "Consciousness"; §4 "The status of LLMs as cognitive models"); no correction needed.
- [P3] Beckmann, P. & Queloz, M. 2025. "Mechanistic Indicators of Understanding in Large Language Models." arXiv 2507.08017 (v5).
  why: candidate bridge between interpretability evidence and the understanding/meaning question; the published interpretability-side statement of the anti-binary stance allied to the project's "describe, don't litigate" — map and counterpoint, not a human anchor.
  status: RECEIVED (catalogued 2026-06-14 → base/sources/beckmann-queloz-2025-mechanistic-indicators.md; abstract verbatim-verified, §5/§6 bodies unreachable via the truncated HTML renderings).
- [methodology] Li, Z., Liu, H., Zhou, D. & Ma, T. 2024. "Chain of Thought Empowers Transformers to Solve Inherently Serial Problems." ICLR 2024; arXiv 2402.12875.
  why: theoretical grounding for the [`essay/output-channel-confound`](../findings/essays/output-channel-confound.md) serial-computation mechanism — a constant-depth transformer is expressively bounded (AC^0/TC^0) without CoT but with T intermediate steps computes any size-T circuit, so a working surface supplies inherently serial computation a forced single token cannot; lead hard example is permutation-group composition, the project's own composition-probe object. Not previously on this list; surfaced and catalogued 2026-06-19 because it bears directly on the in-repo composition line.
  status: **RECEIVED** (2026-06-19; catalogued as [`wiki/base/sources/li-2024-cot-serial.md`](sources/li-2024-cot-serial.md) — abstract verbatim from the arXiv abs page; body section-located via arXiv HTML / ar5iv with a §3.4 locator correction logged in-page. Theory/mechanism source, not a human anchor; licenses no human comparison.)

### Relational / dyadic-interaction anchors (for the relational-meaning pilot)

These would supply the human dyadic-interaction anchor the [`open-question/relational-meaning-pilot`](../findings/open-questions/relational-meaning-pilot.md) needs before any relational result can be promoted. **Anchor decision RESOLVED 2026-05-29** (`decisions/resolved/relational-anchor-shortlist`, Option A): Clark & Wilkes-Gibbs 1986 is the ratified empirical anchor + Pickering & Garrod 2004 the theoretical backdrop — so the first two below are now the **priority fetches** (the other two are no longer needed unless the pilot's emphasis shifts).

- [P1] Clark, H.H. & Wilkes-Gibbs, D. 1986. "Referring as a collaborative process." *Cognition* 22(1): 1–39. **← RATIFIED ANCHOR (fetch first).**
  why: the canonical tangram-naming convergence paradigm; dyads collaboratively coin and compress shared labels over rounds — the closest human analogue to the iterated-reference-game pilot. Ratified as the empirical anchor; the pilot cannot promote a result until this is in-repo.
  status: wanted (priority). Publisher route checked 2026-06-12: ScienceDirect article page returns HTTP 403 to anonymous fetch — plainly paywalled via the publisher. Not yet marked `unreachable` outright: Clark's Stanford publications page (web.stanford.edu/~clark/pubs.html) is a plausible author self-archive route, not tried this session.
- [P2] Brennan, S.E. & Clark, H.H. 1996. "Conceptual pacts and lexical choice in conversation." *Journal of Experimental Psychology: LMC* 22(6): 1482–1493. **← added 2026-05-31 (Tom, decision `relational-fetchable-anchor`).**
  why: the human result that most directly *motivates* the pilot's live-vs-shuffled discriminator — lexical entrainment is shown to be **historical** (not merely salience-driven) and **partner-specific**, the human-side analogue of "live ≠ shuffled." Complements C&W-G 1986. A fetchable derived/aggregate baseline is now available via the Hawkins tangrams corpus ([`decisions/resolved/relational-fetchable-anchor`](../decisions/resolved/relational-fetchable-anchor.md), Option A).
  status: **RECEIVED** (2026-06-12; the profgerhard.de mirror PDF was fetched and verified to be the JEP:LMC paper — masthead, both authors, vol/issue/pagination 22(6):1482–1493 all confirmed; catalogued as [`wiki/base/sources/brennan-clark-1996-conceptual-pacts.md`](sources/brennan-clark-1996-conceptual-pacts.md)). Honest limit recorded in-page: it grounds historicity + partner-specificity, **not** order-sensitivity ("Frequency of use better explains our data than does simple recency"), so it only partly grounds the commutative-convention conjecture's human clause.
- [P3] Krauss, R.M. & Weinheimer, S. 1964/1966. Reference-phrase-shortening studies.
  why: the earlier convergence-curve studies the entrainment measure would be calibrated against.
  status: wanted
- [P3] HCRC Map Task corpus (Anderson et al. 1991).
  why: corpus-grade anchor for referential alignment / entrainment in goal-directed dyads.
  status: wanted
- [P2] Pickering, M.J. & Garrod, S. 2004. "Toward a mechanistic psychology of dialogue." *Behavioral and Brain Sciences* 27(2). **← RATIFIED theoretical backdrop.**
  why: the "interactive alignment" framework — theoretical anchor for what alignment-across-levels predicts (and what it does not claim about meaning-constitution).
  status: wanted

**LLM-side relational sources (the model side of the axis — first catalogued 2026-06-12):**

- [P1] Ashery, A.F., Aiello, L.M. & Baronchelli, A. 2025. "Emergent social conventions and collective bias in LLM populations." *Science Advances* 11(20), eadu9368; arXiv 2410.08948.
  why: the first major demonstration of spontaneous convention emergence in LLM-agent populations — the relational axis's load-bearing LLM-side prior art (coordination shown, constitution untested; the foil the pilot positions against).
  status: received (2026-06-12, abstract verbatim from arXiv HTML v2 + section-level body quotes verified character-for-character against the v2 HTML; see wiki/base/sources/ashery-2025-llm-conventions.md)
- [P1] Imai, S., İnan, M., Sicilia, A. & Alikhani, M. 2025. "Measuring How (Not Just Whether) VLMs Build Common Ground." arXiv 2509.03805.
  why: VLM self-play dyads in the PhotoBook reference game scored against 2,506 human dialogues on grounding efficiency / content alignment / lexical adaptation / human-likeness — the conceptual-pacts question asked of model dyads directly; independently corroborates the pilot's convergence-without-human-like-compression pattern.
  status: received (2026-06-12, abstract verbatim from arXiv abs page + section-level body quotes verified character-for-character against the v1 HTML; see wiki/base/sources/imai-2025-vlm-common-ground.md)
- [P2] Barrie, C. & Törnberg, P. 2025. "Emergent LLM behaviors are observationally equivalent to data leakage." arXiv 2505.23796; and the authors' reply: Ashery, Aiello & Baronchelli 2025, arXiv 2506.18600.
  why: the live critique exchange over the Ashery et al. result (data-contamination deflation vs. genuinely emergent dynamics); fetch both before any in-repo finding leans on the *emergence* (rather than the mere occurrence) of LLM conventions.
  status: **received** (2026-06-13; both abstracts verbatim from the arXiv abs pages + section-level body quotes verified character-for-character against the v1 HTML of each; catalogued as [`wiki/base/sources/barrie-tornberg-2025-data-leakage.md`](sources/barrie-tornberg-2025-data-leakage.md). Both are arXiv v1 preprints — peer-review status not confirmed; the exchange is recorded as unadjudicated.)
- [P3] [authors not yet verified] 2026. "LVLMs and Humans Ground Differently in Referential Communication." arXiv 2601.19792.
  why: dyadic-grounding comparison (surfaced in the 2026-06-12 search; only the arXiv id and title were seen — the page was not opened, so the author list is unknown); fetch only if the relational program needs a second dyadic datapoint beyond 2509.03805.
  status: wanted (found 2026-06-12, not catalogued)

### Graded usage/sense-similarity anchor (for the lexical-sense-gradience conjecture)

The lexical conjecture's anchor decision RESOLVED 2026-05-29 ([`decisions/resolved/lexical-sense-gradience-anchor`](../decisions/resolved/lexical-sense-gradience-anchor.md), **Option B**: a different graded set, NOT Usim — Usim is unfetchable/unlicensed). Need a graded, released, licensed usage/sense-similarity set to ground the monotonicity clause:

- [P1] DWUG — Diachronic Word Usage Graphs (Schlechtweg et al.). Graded human usage-similarity judgments (4-point DURel/Usim tradition), **CC BY-ND 4.0** (corrected 2026-05-30 from 'CC BY' after verification — analysis + verbatim mirroring OK, distributing a modified/augmented version is not; see wiki/base/resources/dwug-usage-graphs.md), on Zenodo. **← leading Option-B candidate (verify license + scale + counts + fetchability, then mirror to experiments/data/ + write a resource page).**
  why: the load-bearing graded anchor the monotonicity clause needs; well-licensed and available (unlike Usim).
  status: catalogued (2026-05-30 — resource page created: wiki/base/resources/dwug-usage-graphs.md; see page for the license / scale / counts / fetchability / fit verification breakdown)
- [P2] CoSimLex (SemEval-2020 Task 3). Graded human ratings of word similarity in context; released.
  why: alternative graded in-context similarity anchor if DWUG does not fit.
  status: wanted

### Sense co-activation / in-item-balance anchor (for the parked forced-both lexical line)

The forced-both build attempt ([`findings/results/forced-both-lexical-build-attempt-v1.md`](../findings/results/forced-both-lexical-build-attempt-v1.md), session 91) hit trigger (c): its Q1-ii — an independent, *not-model-based* check that neither sense **dominates** in a constructed forced-both item — had no honest route, and that page named "a released corpus of human-annotated puns/zeugmas with per-item balance or co-activation labels (none in-repo or on `wanted.md` today)" as the only unblocker.

- [P1] Miller, T., Hempelmann, C.F. & Gurevych, I. 2017. "SemEval-2017 Task 7: Detection and Interpretation of English Puns." SemEval-2017, ACL; pp. 59–69.
  why: human-annotated puns (~1298 homographic + ~1098 heterographic) with **per-item dual WordNet-sense gold on the actual sentence** — i.e. human sense **co-activation** labels for genuine forced-both items, the in-item evidence SemCor's general-usage proxy could not give. Candidate anchor for the forced-both gate's Q4 (sense co-activation) and the matched-ambiguity Option-A homonym sense-anchor.
  status: **RECEIVED** (2026-06-23, session 92; fetched + sha256-hashed + inspected firsthand; catalogued as [`wiki/base/resources/semeval2017-pun-corpus.md`](resources/semeval2017-pun-corpus.md)). Licence MIXED (scorer Apache-2.0; data CC BY 4.0 with a CC BY-NC 4.0 PunoftheDay.com subset). **Anchor RATIFIED for Q4 co-activation only (session 93, 2026-06-23)** — the cross-session decision [`wiki/decisions/resolved/sense-coactivation-anchor-semeval-puns.md`](../decisions/resolved/sense-coactivation-anchor-semeval-puns.md) adopted Q-A (Q4 co-activation anchor) + Q-B-1 (a separate dominance step still owed) + Q-C-1 (puns as forced-both stimuli, homonym subset, frozen). Honest limit recorded in-page: it certifies sense **co-presence**, not a graded **balance/dominance** score, so it discharges **only Q4**, not Q1-ii.
- [P2] British eDom (Maciejewski & Klepousniotou 2016, J. Open Psychology Data 10.5334/jopd.28) + spoken-ambiguity dominance norms (J. Cognition 10.5334/joc.194).
  why: per-**word** human meaning-dominance for *selecting* balanced homonyms (D≈0 = balanced) — the human-anchored balance/dominance step the forced-both Q1-ii / the sense-coactivation decision's Q-B calls for; a CC-BY upgrade over SemCor's general-balance proxy. **General usage, not the specific sentence** — softens-not-eliminates the in-item gap.
  status: **RECEIVED/USED** (data fetched firsthand session 94, 2026-06-23 — eDom Norms File + Rodd & Gilbert WA Dominance Norms, both CC BY 4.0; used to build the v2 frozen subset). eDom-original (Armstrong et al. 2012, 544 US homonyms) unreachable-as-OA (Springer paywalled / KiltHub 403). RAW-C (Trott & Bergen 2021) scouted, not catalogued (relatedness-between-uses, not co-activation; dataset license unconfirmed).

- [P3] **STILL WANTED — a per-item, in-context, *graded* in-item-balance signal on actual forced-both / pun sentences** (sentence-grain, not word-grain; graded, not a presence/co-activation label).
  why: the v2 build ([`findings/results/forced-both-lexical-build-attempt-v2.md`](../findings/results/forced-both-lexical-build-attempt-v2.md), session 94) **solved the power problem** (43 attested balanced-homonym pun items) but a fresh critic ruled the **Q-B-1 transfer-to-item** step NOT satisfiable: word-grain dominance (P2) is the wrong grain for a pun sentence's in-item balance, and the pun genre directionally installs the lean. The only honest discharge is a human-annotated resource that rates *relative salience of the two senses in the specific sentence* — distinct from SemEval's co-presence gold (P1) and from word-grain dominance (P2). **Or** an attested forced-both genre demonstrated *balance-unbiased by construction* (puns are not). Scout reachability before committing time.
  status: wanted (no in-repo or scouted candidate; the forced-both line stays at R1 until one is found + cross-session ratified).

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
- [P3] Visual Word Sense Disambiguation (VWSD) — SemEval-2023 Task 1 (Raganato et al. 2023).
  why: the **image-native** sense-selection task [`findings/conjectures/distributional-saturation-grounding-headroom.md`](../findings/conjectures/distributional-saturation-grounding-headroom.md) names as the next grounding step — sense selection *requires* the image, so it directly instantiates the text-under-determined regime (unlike the image-as-add-on probe that saturated). Needs scouting/license/fetch verification before it can anchor a result.
  status: wanted (named 2026-05-31; not yet scouted).

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
  why: the eliminativist-leaning origin of the "stochastic parrot" framing — the foil for [`base/concepts/deflationary-and-eliminativist-llm-meaning.md`](concepts/deflationary-and-eliminativist-llm-meaning.md).
  status: **RECEIVED** (2026-06-15; catalogued as [`wiki/base/sources/bender-2021-stochastic-parrots.md`](sources/bender-2021-stochastic-parrots.md) — 6 §6.1/§2 quotes incl. the canonical "stochastic parrot" definition verified character-for-character from the CC BY 4.0 PDF via pdfminer; section-level locators. The ACM version of record returned HTTP 403; quotes from the open-access mirror, whose text matches the canonical citation. The deflationary concept page's prior "(not in-repo; characterization)" flag is upgraded to a sourced verbatim quote.)
- [P3] Cappelen, H. & Dever, J. 2021. *Making AI Intelligible: Philosophical Foundations.* OUP.
  why: a worked deflationary/anti-anthropomorphic treatment of AI content/reference; for `deflationary-and-eliminativist-llm-meaning`. (Complements the already-listed Sterken & Cappelen ed. volume.)
  status: wanted

The wave-2 deepenings and original conjectures (2026-05-31) added these (the pages characterize them, no quotes; none was already listed):

- [P3] Sellars, W. 1956. "Empiricism and the Philosophy of Mind."
  why: the "space of reasons" lineage behind Brandom's normative inferentialism, characterized in [`base/concepts/inferential-meaning.md`](concepts/inferential-meaning.md). Fetch only if a finding leans on the Sellarsian lineage.
  status: wanted
- [P2] Burge, T. 1979. "Individualism and the Mental." *Midwest Studies in Philosophy* 4.
  why: social externalism (the *arthritis* case) extending Twin-Earth content-fixing to ordinary concepts; the externalist pole of [`base/concepts/referential-meaning.md`](concepts/referential-meaning.md)'s internalism/externalism section.
  status: wanted
- [P3] Chomsky, N. 2000. *New Horizons in the Study of Language and Mind.* Cambridge.
  why: the i-language internalist position + the argument that word-world reference is not a natural-scientific relation; the internalist pole of `referential-meaning`.
  status: wanted
- [P3] Fodor, J.A. 1987. *Psychosemantics.* MIT.
  why: **narrow content** — the individualistic content meant to survive Twin Earth; the internalist content notion in `referential-meaning`. Distinct from the already-listed Fodor & Lepore 1992 (anti-holism).
  status: wanted
- [P2] Lewis, D. 1969. *Convention: A Philosophical Study.* Harvard.
  why: the philosophical theory of convention behind the "commutative convention" framing in [`findings/conjectures/commutative-convention.md`](../findings/conjectures/commutative-convention.md). Distinct from the already-listed Lewis 1970 "General Semantics".
  status: wanted
- [P3] A defeasible-reasoning / non-monotonic-logic reference (e.g. Reiter, R. 1980. "A Logic for Default Reasoning." *Artificial Intelligence* 13; or a current survey).
  why: [`findings/conjectures/constructional-monotonicity-asymmetry.md`](../findings/conjectures/constructional-monotonicity-asymmetry.md) characterizes the add/cancel asymmetry as monotone-accumulation-vs-defeasance *by analogy only*; fetch first if the project ever leans on the formal mapping.
  status: wanted

The session-63 measurement-epistemics essay (2026-06-21) added this (methodology source; the essay rests on a single in-repo behavioral observation and explicitly does not fabricate the mechanism):

- [P2] A source on **temperature-0 nondeterminism in LLM inference** (e.g. an open-access systems/ML write-up on why greedy decoding is not bit-reproducible — floating-point non-associativity under varying batch/hardware execution order, server-side routing/batching effects; a current arXiv or engineering-blog treatment).
  why: [`findings/essays/point-estimate-is-a-draw.md`](../findings/essays/point-estimate-is-a-draw.md) observes *behaviorally* (the session-62 let-alone re-run) that temp-0 labels are not reproducible run-to-run, but the *mechanism* is uncited in-repo and is **not** fabricated. An OA source would let the essay speak to *why* the jitter occurs (trigger (c)), not only *that* it does. Fetch first if a finding ever leans on the mechanism.
  status: **received** (session 65, 2026-06-21) → [`base/sources/he-2025-defeating-nondeterminism.md`](sources/he-2025-defeating-nondeterminism.md). He, Horace & Thinking Machines Lab 2025, "Defeating Nondeterminism in LLM Inference" (OA engineering blog). Identifies the mechanism as **load-dependent batch-size variation × non-batch-invariant kernels** (floating-point non-associativity the ultimate numeric cause; the common "concurrency" half is largely a red herring). Discharges `essay/point-estimate-is-a-draw` trigger (c).

## Notes on fetching

- **Try open-access first.** ACL Anthology, arXiv, preprint pages, lab pages — many of the LLM-meaning items above are OA and a run can fetch them via `WebFetch`. Only escalate to Tom when paywalled.
- **Page-level provenance, not wholesale text.** When a source is ingested into `wiki/base/sources/`, the page records summary + exact short quotes with page numbers, not the source itself.
