---
type: resource
id: cooccurrence-corpus-scouting
title: "Co-occurrence corpus scouting — license survey for a fetched running-text corpus to compute the A1b contrastive-frame G² control (no co-occurrence data in-repo)"
meaning-senses:
  - distributional
status: scouting
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: depends-on
    target: conjecture/lexical-relation-shadow-saturation
---

# Co-occurrence corpus scouting — a license survey for the A1b contrastive-frame G² baseline

> **This is a scouting page (a license survey). Nothing was fetched, downloaded, built, or
> adopted.** It records, per candidate corpus, whether an **open license permitting compute-derived
> co-occurrence statistics over the running text** could be *verified* this session — with the exact
> license string and the URL it was read at, or an explicit **UNVERIFIED**. The project's cardinal
> scouting rule binds (s168): **never adopt an unverified-license corpus, and never fabricate a
> plausible-sounding license.** A "probably CC BY" is a fabrication; where a license could not be
> read, it is marked UNVERIFIED and what could not be confirmed is stated.

**Scouted:** 2026-07-06 (session 185, program item A1b). **Why owed:** the ratified decision
[`decisions/resolved/antonymy-internal-contrast-scoring`](../../decisions/resolved/antonymy-internal-contrast-scoring.md)
adopted **Q1-C** — the A1b probe's *primary* distributional control is a **faithful
contrastive-frame co-occurrence (G²) baseline**, and the *run* is **gated on this license scout**
because **there is NO co-occurrence data in-repo**: [`resource/subtlex-us-frequency`](subtlex-us-frequency.md)
is a pure **unigram** norm (columns `freqcount`, `lg10wf` — no bigram/co-occurrence field) and its
underlying 51M-word subtitle corpus is not in-repo. So the contrastive-frame G² baseline the
conjecture names **cannot be computed from any in-repo artifact** — it must be built from a *fetched,
license-verified* corpus, or the run stays honestly blocked. This scout checks whether such a corpus
exists. Design: [`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md);
conjecture: [`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md).

This is a **scouting** note in the mould of
[`base/resources/scalar-implicature-anchor-scouting.md`](scalar-implicature-anchor-scouting.md)
and [`base/resources/presupposition-projection-human-anchor-scouting.md`](presupposition-projection-human-anchor-scouting.md);
it **adopts nothing**. No `anchors:` link is asserted (this is a distributional *statistic* corpus,
not a human-comparison anchor — the A1b result is ratified `internal-contrast-only`).

**Headline (calibrated):** unlike the projection-anchor scout, **a candidate DOES clear the bar.**
**English Wikipedia, via the official Wikimedia dumps, is released under CC BY-SA 4.0 + GFDL**
(license read directly this session) — massive intact running text, cleanly licensed for
compute-derived statistics. So the A1b run is **not** license-blocked; the "honest design-only
block" fallback in Q1-C is *not* triggered. C4 (ODC-BY) is a verified second option; Leipzig (CC
BY-NC, license read only via a search summary — flagged) a viable third. Two candidates named in the
assignment — **OPUS OpenSubtitles** and **COCA** — do **not** clear the bar (no license grant / a
restricted paid license respectively), which is exactly the point of the "Cao used it ≠ it is open"
discipline.

---

## What the corpus must satisfy (requirement recap)

From Q1-C and the design's Gate Q1:

1. **Raw running text** (intact sentences / tokens), **not** precomputed unigram frequencies — so
   that co-occurrence within short spans and in **contrastive frames** ("neither X nor Y", "from X to
   Y", "X versus Y", conjoined/parallel structures) can be counted and a **log-likelihood G²**
   (Dunning 1993, Cao 2025b's measure) computed. Intra-sentential co-occurrence is the operative
   grain (Cao measured G² over intra-sentential co-occurrence; Justeson & Katz over within-sentence
   predicative adjectives).
2. A **verifiable open license** permitting this research use (computing statistics over the text).
   Permissive / CC / open-data licenses qualify. A **non-commercial** CC license also qualifies for
   *this* project (it is non-commercial scientific research) — flagged as NC where it applies. A
   corpus with **no discoverable license** does **not** qualify (→ UNVERIFIED → not adoptable).
3. **Reasonably fetchable** in a later freeze session (a public dump / package), **English**.

Two non-license considerations are recorded but are **not** this scout's job to settle (they belong
to the `prep.py` freeze): the **proxy-corpus fence** (freeze-condition 2 — any control corpus is a
proxy for the panel's unknown pretraining distribution, not the training data itself) and the
**construction of "contrastive-frame G²"** itself (freeze-condition 3 — which frames, window,
weighting; the project's own synthesis, frozen in `prep.py`).

---

## Candidates

### A. Clears the license bar

#### 1. English Wikipedia — Wikimedia text dumps · **CC BY-SA 4.0 + GFDL** (verified, read directly)

**What it is.** The full text of English Wikipedia, published as periodic database dumps by the
Wikimedia Foundation (`enwiki` `pages-articles`). Millions of articles; **billions of words** of
intact encyclopedic running text. Officially published at **dumps.wikimedia.org**. Pre-extracted,
same-content packages also exist (e.g. the `wikimedia/wikipedia` dataset on Hugging Face), but the
**license is anchored on the official dump's legal page**, read below.

**License (verbatim, read directly).** From <https://dumps.wikimedia.org/legal.html>:
> "all original textual content is licensed under the GNU Free Documentation License (GFDL) and the
> Creative Commons Attribution-Share-Alike 4.0 License."

i.e. **dual GFDL + CC BY-SA 4.0**. Both permit computing and publishing derived statistics with
attribution (CC BY-SA's ShareAlike binds redistribution of *adapted text*, not the reporting of
co-occurrence counts/G²). **Not** non-commercial-restricted. This is the cleanest license in the
survey.

**Raw text for G²? YES.** Intact articles and sentences — supports both intra-sentential and
wider-window contrastive-frame counting.

**Adoptability: ADOPTABLE — first choice.** Cleanest license (read firsthand), largest running-text
volume (ample for powered per-relation G² over ~120–150 cues × 6 relations), official stable dump
location. Bonus for freeze-condition 2: Wikipedia is heavily represented in LLM pretraining, so it is
a *defensible* proxy for the panel's distribution — arguably a better proxy than Cao's COCA.
Register caveat (a `prep.py` matter, not a license matter): encyclopedic prose is more formal than
COCA's balanced spoken+written mix, so contrastive-dialogue frames may be rarer — recorded, not
disqualifying.

#### 2. C4 (Colossal Clean Crawled Corpus, `allenai/c4`, `en`) · **ODC-BY** (verified, read directly)

**What it is.** A cleaned Common-Crawl web-text corpus (Raffel et al. 2020, T5). The `en` subset is
~156 billion tokens of intact English documents. Distributed on Hugging Face (`allenai/c4`).

**License (verbatim, read directly).** From the dataset card at
<https://huggingface.co/datasets/allenai/c4>:
> "We are releasing this dataset under the terms of [ODC-BY]."

and, layered on top:
> "By using this, you are also bound by the [Common Crawl terms of use] in respect of the content
> contained in the dataset."

**ODC-BY** (Open Data Commons Attribution 1.0) is a permissive open-data license and qualifies. The
**Common Crawl terms-of-use layer** is a caveat to record — the *dataset packaging* is ODC-BY, the
*underlying web content* remains under Common Crawl's terms.

**Raw text for G²? YES.** Intact documents.

**Adoptability: ADOPTABLE — verified second choice**, with the Common-Crawl-terms caveat. Larger and
noisier than Wikipedia; heavier to fetch (~305 GB for `en`, though streamable and only a fixed cue
set need be counted). Prefer Wikipedia unless a larger/web-register baseline is specifically wanted.

#### 3. Leipzig Corpora Collection (English sentence packages) · **CC BY-NC** (license read via SEARCH SUMMARY only — flagged)

**What it is.** Monolingual sentence corpora (Goldhahn, Eckart & Quasthoff 2012) — randomly selected
sentences from news / web / Wikipedia sources, in packages from **10,000 up to 1,000,000 sentences**
(some English packages larger, e.g. multi-million-sentence news sets across years); tens of millions
of words available across the English packages. Downloadable per-package files at
wortschatz.uni-leipzig.de.

**License (⚠ read via search summary, NOT the actual terms page).** A web-search summary of the
Terms of Usage page (<https://wortschatz.uni-leipzig.de/en/usage>) returned:
> "Permission for use is granted free of charge solely for non-commercial personal and scientific
> purposes licensed under the Creative Commons License CC BY-NC."

**CC BY-NC** would qualify for this non-commercial project. **CONFIDENCE FLAG:** the actual
`/en/usage` page could **not** be fetched directly — both `wortschatz.uni-leipzig.de` and
`wortschatz-leipzig.de` sit behind an **Anubis proof-of-work bot wall** that WebFetch could not pass,
so this string is **search-summarized, below the "I read the actual license text" bar.** A freeze
session must read the terms page directly before adopting. (Some *non-English* Leipzig corpora and
the frequency word-lists are separately reported as CC BY / CC BY 3.0; do not conflate those with the
English-sentence-package terms.)

**Raw text for G²? YES — and a positive worth noting.** Leipzig ships **intact sentences** but
**randomly shuffles sentence order and deletes the source documents** ("every text is split into its
sentences and those sentences are randomly ordered to destroy the original document structure").
Because the A1b control needs **intra-sentential** co-occurrence, this shuffling does **not** harm the
measurement — each sentence, and every within-sentence contrastive frame, is preserved; only
cross-sentence/document context is lost (which G² over intra-sentential co-occurrence does not use).

**Adoptability: ADOPTABLE pending a direct terms-page read** (CC BY-NC, confidence-flagged). A good
medium-size English option whose sentence-level packaging is well-matched to intra-sentential G²; the
license just needs to be *read*, not search-summarized, at freeze.

#### 4. UD English-EWT treebank · **CC BY-SA 4.0** (verified, read directly) — but TINY

**What it is.** The English Web Treebank in Universal Dependencies (program A6 notes UD is in-scope).
Web-media text (weblogs, newsgroups, emails, reviews, Yahoo! answers), from the English Web Treebank
LDC2012T13.

**License (verbatim, read directly).** README at
<https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/README.md>:
> "Creative Commons Attribution-ShareAlike 4.0 International License"

and the repo's `LICENSE.txt`
(<https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/LICENSE.txt>) is the
verbatim **CC BY-SA 4.0 International** legal code — both confirm the license firsthand.

**Size (verified, from the README).** **254,820 words / 16,622 sentences.**

**Raw text for G²? YES (intact sentences) — but far too small.** ~255K words cannot support powered
per-relation G² over ~120–150 cues × 6 relations; antonym-pair counts would be near-zero and G²
unstable. (Other English UD treebanks, e.g. GUM, are similar-order-small and each carries its **own**
license — UD is a collection of individually-licensed treebanks, not one license.)

**Adoptability: license-clean, size-disqualifying as the primary G² corpus.** Usable only as a
license-clean *supplementary* sanity check, not the baseline.

#### 5. Brown Corpus (via NLTK) · **"non-commercial purposes"** (verified, read directly) — but TINY

**What it is.** The Brown University Standard Corpus of Present-Day American English (~1 million
words, ~500 samples of ~2,000 words across genres). The corpus Justeson & Katz 1991 used for their
antonym co-occurrence study. License-clean and trivially fetchable via `nltk.download('brown')`.

**License (verbatim, read directly).** From the authoritative NLTK package metadata
`brown.xml` (<https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/brown.xml>):
> "May be used for non-commercial purposes."

**Non-commercial**, which qualifies for this project — and NLTK redistributes it with the copyright
holder's permission.

**Raw text for G²? YES (intact sentences) — but ~1M words is too small** for powered per-relation G²
across 6 relations (it is the right order of magnitude for J&K's *adjective-only* study, not for a
six-relation ~120–150-cue design).

**Adoptability: license-clean, size-disqualifying as primary.** Best use: a license-clean,
zero-friction *replication check* of the J&K adjective frames, or a supplement — not the baseline.

### B. Does NOT clear the license bar

#### 6. OPUS OpenSubtitles · **NO LICENSE GRANT** (attribution request only) — read directly

**What it is.** Movie/TV subtitle text aggregated by the OPUS project (Lison & Tiedemann 2016);
very large (billions of tokens, English). The register (dialogue) is attractive for contrastive
frames.

**License (what was actually found, read directly).** OPUS provides **no explicit open-license
grant** for OpenSubtitles. The legacy corpus page
(<https://opus.nlpl.eu/legacy/OpenSubtitles-v2018.php>) carries only an **attribution request**:
> "IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/
> to your website and to your reports and publications produced with the data! I promised this when I
> got the data from the providers of that website!"

and the OPUS site (<https://opus.nlpl.eu/legacy/>) states only:
> "OPUS is based on open source products and the corpus is also delivered as an open content package."

Neither is a license: OPUS does **not** own the subtitle copyright (the general OPUS disclaimer is
that it redistributes only files it *believes* it may, and removes them on complaint). "Open content
package" + a link-back request is **not** a verifiable open-license grant.

**Adoptability: NOT ADOPTABLE — UNVERIFIED (no license grant).** Fails requirement 2. Do not adopt on
the strength of an attribution request. (What could not be confirmed: any actual copyright/redistribution
license for the underlying subtitles.)

#### 7. COCA (Corpus of Contemporary American English) · **RESTRICTED / PAID LICENSE** — verified (not open)

**What it is.** Mark Davies' ~1-billion-word balanced corpus of American English — **the corpus Cao
2025b used** for its antonymy G² measurements. Free *online KWIC interface*; the **full running text**
is a separate paid product (corpusdata.org).

**License (verbatim, read directly from a neutral source).** The University of Virginia Library's
*licensed*-data-source page
(<https://library.virginia.edu/data/datasources/licensed/corpus-of-contemporary-american-english-coca>)
records it as a **restricted licensed-access agreement, not openly licensed**, and quotes the
redistribution cap:
> distributing "substantial amounts of the full-text data (typically, a total of 50,000 words or
> more)" [outside the licensed organization is prohibited]

with access limited to "Faculty and graduate students" for research, unique identifiers embedded in
each download, and "Automated Google searches ... daily to find copies of the data on the Web." The
full-text data is sold (corpusdata.org, ~$395 tier).

**Adoptability: NOT ADOPTABLE — restricted/paid, redistribution-capped.** This is the canonical "Cao
using it does not make it open" case: Cao 2025b's use of COCA does **not** confer an open license.
Fails requirement 2.

#### 8. OSCAR (`oscar-corpus/OSCAR-2301`) · packaging **CC0**, **text NOT licensed by distributor** — read directly

**What it is.** A large multilingual Common-Crawl-derived corpus. Included as a documented alternative
to C4.

**License (verbatim, read directly).** Dataset card
(<https://huggingface.co/datasets/oscar-corpus/OSCAR-2301>):
> "We license the actual packaging, the metadata and the annotations of these data under the Creative
> Commons CC0 license ('no rights reserved')."

but, for the text itself:
> "We do not own any of the text from which these data has been extracted."

So **only the packaging/metadata is CC0**; the **running text carries no distributor license grant**
(same structure as OPUS), plus a jurisdiction caveat that non-research/TDM uses may be prohibited in
some countries.

**Adoptability: NOT ADOPTABLE on the strength of the card.** The CC0 covers packaging, not content;
the text relies on Common-Crawl terms / national TDM-research exceptions rather than a content
license. Weaker than C4, whose `allenai` release *does* place the dataset itself under ODC-BY. If a
Common-Crawl-register corpus is wanted, prefer C4.

---

## Verification ledger

| Candidate | What / running-text unit | Size | License (verbatim or UNVERIFIED) + URL | Raw text for G²? | Adoptable? | Confidence |
|-----------|--------------------------|------|-----------------------------------------|------------------|------------|------------|
| **English Wikipedia** (Wikimedia dumps) | intact articles/sentences | billions of words | **CC BY-SA 4.0 + GFDL** — "licensed under the GNU Free Documentation License (GFDL) and the Creative Commons Attribution-Share-Alike 4.0 License" · dumps.wikimedia.org/legal.html | YES | **YES — first choice** | **read license page directly** |
| **C4** (`allenai/c4`, en) | intact web documents | ~156B tokens (en) | **ODC-BY** — "We are releasing this dataset under the terms of [ODC-BY]" (+ Common Crawl terms) · huggingface.co/datasets/allenai/c4 | YES | **YES — 2nd choice** (CC-terms caveat) | **read card directly** |
| **Leipzig** (English sentence packages) | intact sentences, shuffled order | 10K–1M+ sent/package | **CC BY-NC** — "granted free of charge solely for non-commercial personal and scientific purposes licensed under the Creative Commons License CC BY-NC" · wortschatz.uni-leipzig.de/en/usage | YES (intra-sentential preserved) | **YES pending direct read** | ⚠ **search summary only** (Anubis wall; not read directly) |
| **UD English-EWT** | intact sentences | 254,820 words / 16,622 sent | **CC BY-SA 4.0** — README "Creative Commons Attribution-ShareAlike 4.0 International License"; LICENSE.txt = CC BY-SA 4.0 legal code · github UniversalDependencies/UD_English-EWT | YES but tiny | license-clean, **too small for primary** | **read README+LICENSE directly** |
| **Brown** (NLTK) | intact sentences | ~1M words | **non-commercial** — "May be used for non-commercial purposes" · nltk_data …/corpora/brown.xml | YES but tiny | license-clean, **too small for primary** | **read NLTK metadata directly** |
| **OPUS OpenSubtitles** | subtitle text | billions of tokens | **NO LICENSE GRANT** — only "add a link to opensubtitles.org …" + "open content package" · opus.nlpl.eu/legacy | (text yes) | **NO — UNVERIFIED** | **read directly** (no grant found) |
| **COCA** | balanced am-English text | ~1B words | **RESTRICTED/PAID** — redistribution of "50,000 words or more" prohibited; licensed-access · library.virginia.edu …/coca | (paid full-text) | **NO — restricted** | **read neutral library page directly** |
| **OSCAR** (2301) | CC-derived web text | very large | packaging **CC0**; text "We do not own any of the text …" · huggingface.co/datasets/oscar-corpus/OSCAR-2301 | (text yes) | **NO** (text unlicensed by distributor) | **read card directly** |

---

## Bottom-line recommendation

**A candidate clears the license bar, so A1b's run is not license-blocked.**

1. **Primary G² corpus for the A1b freeze: English Wikipedia (official Wikimedia dumps, CC BY-SA 4.0 +
   GFDL).** It is the only candidate combining (a) an **open, non-NC license read firsthand**, (b)
   **billions of words** of intact running text — ample for powered per-relation G² over the six
   relations, including the antonym-sparse strata — and (c) an **official, stable public dump**. It is
   also a defensible **proxy** for the panel's pretraining distribution (freeze-condition 2), being
   heavily represented in LLM training data.
2. **Verified fallback: C4 (ODC-BY)** if a larger or web-register baseline is wanted — with the
   Common-Crawl-terms caveat, and heavier to fetch.
3. **Viable pending a direct terms read: Leipzig English (CC BY-NC).** Its intra-sentential packaging
   is well-suited to the measurement; adopt **only after reading `/en/usage` directly** (this scout
   could reach it only via a search summary).
4. **License-clean but too small to be primary: UD English-EWT (CC BY-SA 4.0) and Brown (NC).** Use as
   supplements / replication checks, not the baseline.
5. **Do NOT adopt: OPUS OpenSubtitles** (no license grant), **COCA** (restricted/paid), **OSCAR**
   (text unlicensed by distributor).

Because a corpus clears the bar, the Q1-C "honest design-only block if none clears" is **not**
triggered. The **frame-ablation arm** (a within-model manipulation needing no external corpus) remains
the corpus-free complement regardless, and runs under either outcome.

**Scope of this verdict (calibrated).** This is a **license** verdict only. The freeze session
(`prep.py`) still owes, independently of licensing: the actual corpus fetch/build; the frozen
construction of "contrastive-frame G²" (which frames, window, weighting — the project's own synthesis,
freeze-condition 3); the register/proxy fence (freeze-condition 2); and the option of computing a
**6-relation** cue-strength ranking from the same corpus (freeze-condition 1). None of those is a
license question, and none is settled here.

---

## Fetches that failed or were proxy-/bot-blocked (stated honestly, for spot-checking)

- **Leipzig Corpora Collection terms page** — `wortschatz.uni-leipzig.de/en/download`,
  `wortschatz.uni-leipzig.de/en/usage`, and the `wortschatz-leipzig.de` mirror all sit behind an
  **Anubis proof-of-work bot wall**; WebFetch returned the Anubis challenge page, not the terms. The
  **CC BY-NC** string is therefore **search-summarized, not read directly** — the single candidate in
  the "clears" group below the "read the actual license text" bar. Flagged above and in the ledger.
- **COCA** — `english-corpora.org/coca/` returned **HTTP 403** and `corpusdata.org` returned **HTTP
  403** to WebFetch; the restricted-license verdict rests on the **UVA Library licensed-resource page**
  (fetched directly, a neutral third party) plus corroborating search results ($395 purchase tier).
  The "50,000 words" redistribution-cap quote is from the UVA page as fetched.
- **OPUS** — the modern `opus.nlpl.eu/OpenSubtitles-v2018.php` path returned **HTTP 404**; the
  verdict rests on the **legacy** pages (`opus.nlpl.eu/legacy/` and
  `opus.nlpl.eu/legacy/OpenSubtitles-v2018.php`), fetched directly, which carry only the
  attribution request and "open content package" phrasing — **no license grant**.

**Confidence summary.** Read the *actual* license text firsthand for: **Wikipedia, C4, UD-EWT, Brown,
OSCAR, OPUS-OpenSubtitles**, and (via a neutral library page) **COCA**. **Below** that bar — search
summary only, flagged: **Leipzig (CC BY-NC)**. No license was fabricated or inferred; every "clears"
verdict except Leipzig rests on a license string read at its cited URL.
