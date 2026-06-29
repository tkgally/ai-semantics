---
type: source
id: cao-2025-distinctive-cooccurrence-antonymy
title: On the Distinctive Co-occurrence Characteristics of Antonymy
authors:
  - Cao, Zhihan
  - Yamada, Hiroaki
  - Tokunaga, Takenobu
year: 2025
venue: "*SEM 2025 (accepted). Preprint arXiv:2509.11534 (cs.CL), submitted 2025-09-15 [v1]; HTML v1 used for body quotes."
arxiv: "2509.11534"
doi: 10.48550/arXiv.2509.11534
url: https://arxiv.org/abs/2509.11534
access: open-access
meaning-senses:
  - distributional
status: received
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: supports
    target: essay/antonymy-outlier-distributional-shadow
  - rel: supports
    target: conjecture/lexical-relation-shadow-saturation
  - rel: refines
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/distributional-meaning
---

# Cao, Yamada & Tokunaga 2025 — On the Distinctive Co-occurrence Characteristics of Antonymy

## What it is

A short corpus-linguistic study (accepted at **\*SEM 2025**; arXiv:2509.11534, cs.CL, submitted
2025-09-15) by **Zhihan Cao, Hiroaki Yamada, and Takenobu Tokunaga** (Institute of Science Tokyo) —
the **same group** whose earlier paper, [`source/cao-2025-semantic-relation-knowledge`](cao-2025-semantic-relation-knowledge.md)
(cited here as "Cao et al. 2025a"), reported the antonymy outlier in *model* performance. This paper
turns to the *corpus* side: it measures, on a large modern corpus, **whether the well-known
co-occurrence of antonym pairs is *distinctive* of antonymy relative to other semantic relations** —
something prior antonymy-co-occurrence work (Charles & Miller 1989; Justeson & Katz 1991; Fellbaum
1995; Jones) never tested, because it studied antonymy in isolation without a cross-relation
comparison. The headline, verbatim:

> "We find that antonymy is distinctive in three respects: antonym pairs co-occur with high strength,
> in a preferred linear order, and within short spans." (Abstract)

This is the **first in-repo source that directly compares antonymy's intra-sentential co-occurrence
against other lexical relations across parts of speech**, and the first that extends the antonym
co-occurrence measurement *beyond predicative adjectives* (the scope of the in-repo primary,
[`source/justeson-katz-1991-antonym-cooccurrence`](justeson-katz-1991-antonym-cooccurrence.md)) to
**nouns, verbs, adjectives, and adverbs** on COCA. It is **prior-art corpus measurement + the
authors' own connection to the PLM "antonymy bias"**, *not* a result about the project's panel and
*not* a human-annotated resource. See "What it cannot ground" for the precise fences.

## Provenance

Title, full author list, submission date (2025-09-15 [v1]), subject category (cs.CL), venue
("Accepted by \*SEM 2025"), and license were read from the arXiv abs page
(https://arxiv.org/abs/2509.11534) on 2026-06-30. The license shown is the **arXiv.org perpetual
non-exclusive distribution license** (http://arxiv.org/licenses/nonexclusive-distrib/1.0/) — i.e.
the paper is publicly readable on arXiv; it is *not* a CC-BY grant, so quote-and-cite (fair use of
short verbatim excerpts) is the appropriate use, exactly as for the project's other arXiv sources.
**All body quotes below are taken from the v1 HTML full text (https://arxiv.org/html/2509.11534v1)**,
fetched and stripped to text on 2026-06-30 and verified character-for-character. Quote locators are
**section names/numbers from the HTML** (no journal/proceedings page numbers were available from the
open HTML; the camera-ready \*SEM 2025 version was not consulted). Acknowledgments name JSPS KAKENHI
JP25KJ1271 and thank Prof. Simone Teufel (a co-author of Cao et al. 2025a).

## Abstract (verbatim, from the arXiv abs page / v1 HTML)

> "Antonymy has long received particular attention in lexical semantics. Previous studies have shown
> that antonym pairs frequently co-occur in text, across genres and parts of speech, more often than
> would be expected by chance. However, whether this co-occurrence pattern is distinctive of antonymy
> remains unclear, due to a lack of comparison with other semantic relations. This work fills the gap
> by comparing antonymy with three other relations across parts of speech using robust co-occurrence
> metrics. We find that antonymy is distinctive in three respects: antonym pairs co-occur with high
> strength, in a preferred linear order, and within short spans."

## The data and design (corpus-only, lemma+PoS level)

The study measures co-occurrence on the **Corpus of Contemporary American English (COCA)** — after
dropping sentences shorter than five words, "**This leaves 17,718,403 sentences for analysis**" (§3).
It compares **four WordNet relations plus an unrelated control** (§3, verbatim):

> "We evaluate four semantic relations: antonymy (ANT), synonymy (SYN), hyper-hyponymy (HYP), and
> holo-meronymy (HOL)."

> "As a control, we additionally randomly sample 10,000 lemma pairs from all lemma pairs that
> co-occur intra-sententially but are unrelated (UNR) in any relation defined in WordNet." (§3)

Pairs are retrieved from WordNet (25,115 lemma pairs after filtering; "**22,399 lemma pairs are
observed in COCA**", §3), sorted by descending frequency, over **nouns, verbs, adjectives, and
adverbs**. The unit of analysis is the **lemma + PoS**, with **no word-sense disambiguation** (a
limit the paper flags — see below). Three metrics are computed and compared across relations with a
Brunner-Munzel test (significance level 0.01):

- **Strength** — the **G² (log-likelihood-ratio) score** of Dunning (1993), chosen because raw counts
  and PMI are "**biased toward extremely low or high frequencies**" and make χ²-style tests
  "**unreliable**" under word-frequency sparsity (both §1). G² is "**theoretically and empirically
  robust to data sparsity … and supports a reliable statistical test**" (§2.1).
- **Order** — a binomial test on whether each pair has a preferred linear order (the more frequent
  lemma first vs. second) (§2.2).
- **Distance** — the average number of words separating the two co-occurring lemmas (§2.3).

So the measurement is **purely distributional/corpus-internal** — a sharpened, cross-relation
re-measurement of the Charles & Miller / Justeson & Katz co-occurrence tradition, with a modern
corpus, a sparsity-robust statistic, and (its key novelty) a **control set of other relations**.

## Key findings (verbatim; v1 HTML section locators)

**Antonymy co-occurs with the greatest *strength*, across every PoS:**

> "Antonymy pairs consistently yield both the highest G² scores (ranging from 915 to 11,144) and the
> largest percentage (at least 91%) of significant co-occurring pairs across all PoS." (§4)

> "These results confirm that antonyms not only co-occur more frequently than expected by chance, but
> also with greater strength than other relations." (§4)

The nominal case is the strongest — and the paper flags an outlier caveat honestly:

> "For nominal antonymy, there are even two pairs, ('child','parent') and ('man','woman'), whose G²
> scores are greater than 100,000. Such extremely high outliers might have inflated the average G²
> scores to 11,144 for nominal antonymy, making it the highest among all PoS and relations." (§4)

**Antonymy alone shows a consistent preferred *order*:**

> "Across all PoS, more than 90% of the co-occurring antonymy pairs have a preferred order, typically
> with an average order score above 0.10." (§4, Table 3)

> "This indicates that the more frequent antonym slightly tends to precede the less frequent
> counterpart." (§4)

> "For other relations, a preferred order exists at the pair level but is not consistent across pairs,
> resulting in no clear pattern at the relation level." (§4)

**Antonyms co-occur at the shortest *distance*:**

> "Antonyms co-occur more closely than other relations. On average, antonyms co-occur within 18 words,
> which is shorter than the span of pairs in other relations across PoS." (§4, Table 4)

**The summary claim — distinctive, and extended to nouns/verbs/adverbs:**

> "Our findings align with previous observations on antonyms, and extend them to other relations and
> PoS, revealing the distinctive co-occurrence characteristics of antonymy." (§4)

> "We find that antonymy is consistently distinctive from all other relations across all metrics
> used." (§6 Conclusion)

> "Our findings establish a robust empirical foundation for the distributional nature of antonymy,
> offering a solid empirical basis for its future analysis." (§6 Conclusion)

## The lexical-pairing / contrast discussion (note: speculation, *not* a construction measurement)

The Discussion connects the strength to **semantic contrast and lexical constraint**, citing the
in-repo J&K source for the framing:

> "Antonymy is considered to differ from hypernymy, holonymy, and synonymy in nature because it is not
> just semantic but also lexically constrained Justeson and Katz (1991)." (§5)

The paper measures lexical constraint by how many distinct relata each frequent lemma has: "**For
antonymy, the frequent lemma is associated with only one lemma on average, whereas for other
relations, it ranges from 1.7 to 6.7**" (§5), so "**antonymy is the most lexically constrained among
the other relations studied here**" (Appendix C). It then offers a **speculation** about *why* this
drives co-occurrence:

> "This result suggests that antonymy involves the strongest lexical pairing, which might enhance their
> suitability for parallel constructions and, in turn, contribute to their frequent co-occurrence in
> texts." (§5)

**This is the one place the paper touches "parallel constructions," and it is explicitly a "might"
speculation, not a measurement.** The Limitations section is unambiguous that construction *type* was
not measured (load-bearing for how this source may be cited):

> "We only characterise the co-occurrence of semantically related words in a quantitative manner and
> do not address the qualitative evaluation. We hence can not answer in which lexical and dependency
> constructions two words are likely to occur." (Limitations)

So this source **measures** that antonym co-occurrence is strong/ordered/short-span for nouns (and
verbs/adverbs); it does **not** measure whether nominal antonyms concentrate in the *syntactically
parallel, lexically-identical contrastive frames* that J&K measured for adjectives — it only
*conjectures* the parallel-frame link. The cross-PoS robustness it does show is a **derivation test**:
co-occurrence significance is "**robust under derivational change**" (e.g. *strong/weak* → *strongly/
weakly*), "**aligning with the idea that co-occurrence might stem from the semantic contrast**" (§5).

## The authors' own link to the PLM "antonymy bias" (convergent with the project's shadow reading)

The motivation and the "Relating Language Models" discussion state, in the authors' own voice, the
deflationary/distributional reading the project's [`essay/antonymy-outlier-distributional-shadow`](../../findings/essays/antonymy-outlier-distributional-shadow.md)
argues:

> "Recently, pretrained language models (PLMs) have exhibited a puzzling phenomenon, antonymy bias.
> Regardless of architecture and size, PLMs perform substantially better on predicting the antonym of
> a given word over other relations (Pitarch et al., 2023; Cao et al., 2025a)." (§1)

> "The distinctive co-occurrence characteristics of antonymy may provide signals that facilitate
> learning antonym pairs during pretraining. However, as prior studies commonly use sentence
> completion tasks in evaluation, models might take advantage of those intra-sentential co-occurrence
> characteristics, using them as a shortcut Du et al. (2023) rather than relying on knowledge of
> antonymy." (§5)

> "Given this, our findings highlight the need to disentangle the extent to which PLMs rely on such
> distributional clues from the extent to which they generalise beyond them." (§5)

That last sentence is, almost exactly, the project's [`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md)
stated as a research need by the source authors themselves — the conjecture proposes the
contrastive-frame *control* that would do this disentangling on the project's panel. The "antonymy
bias" they cite is, however, in **non-frontier PLMs** (Pitarch et al. 2023; Cao et al. 2025a =
BERT/RoBERTa/Llama-3), so it does not transfer to the panel (see below).

## What this bears on in-repo

- **[`essay/antonymy-outlier-distributional-shadow`](../../findings/essays/antonymy-outlier-distributional-shadow.md) — `supports`.**
  The essay's distributional-shadow reading rests on antonym pairs being densely written into the
  corpus in contrastive frames. This source **extends** that corpus premise from J&K's predicative
  adjectives to **nouns, verbs, adjectives, and adverbs** (confirming the essay's flagged adjectival→
  nominal extrapolation on the *co-occurrence-strength* leg), and **adds the cross-relation comparison
  J&K lacked** — antonymy is the relation with the *highest* co-occurrence strength, the only
  consistent order preference, and the shortest span, distinctively above SYN/HYP/HOL. And the authors
  independently state the "shortcut" / "distributional clues" reading. *Residual the essay must keep:*
  this source does **not** measure construction type, so the specific *parallel-contrastive-frame*
  mechanism for nouns stays inferential (the authors only speculate it), and the antonymy bias is in
  non-frontier PLMs.
- **[`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md) — `supports`.**
  The conjecture's clause 2 is "raw recovery tracks distributional cue strength," premised on antonymy
  being the most distributionally/contrastively cued of the relations. That premise previously rested
  on reasoning plus J&K (antonymy-only, no cross-relation comparison). This source supplies a **direct
  corpus measurement of the cross-relation cue-strength ranking** — antonymy highest, distinctively so
  — which is exactly the independent distributional ranking the conjecture's clause 2 calls for. It
  does **not** unblock the conjecture (see below): it grounds the *corpus-side* cue-strength premise,
  not the *model-side* recovery, and supplies no human anchor and no panel result.
- **[`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md) — `refines`.**
  The continuum's lexical pole is "beat the distributional shadow," and its relation-type gradient
  places antonymy at the shadow-saturated end. This source measures, corpus-side, that antonymy *is*
  the most distributionally distinctive of the four relations — sharpening the gradient's lexical-pole
  ordering with a direct cross-relation corpus statistic rather than an inference.

## What it can ground

- A citation that, on COCA (17.7M sentences) with a sparsity-robust G² statistic and an unrelated
  control, **antonym pairs co-occur intra-sententially with the highest strength, the only consistent
  order preference, and the shortest span of four lexical relations (ANT/SYN/HYP/HOL), across nouns,
  verbs, adjectives, and adverbs** (verbatim Abstract + §4 + §6).
- A citation that antonym co-occurrence's distinctiveness **extends beyond adjectives to other parts
  of speech** (verbatim §4), and is **robust under derivation** that changes PoS (§5) — the
  cross-PoS evidence the in-repo J&K adjective-only study could not supply.
- A citation that antonymy is **the most lexically constrained** of these relations (~1 relatum per
  cue vs 1.7–6.7), which the authors *conjecture* enhances suitability for **parallel constructions**
  (§5, App C) — cite as the authors' speculation, not a measured construction result.
- The authors' own statement that the distinctive co-occurrence may be a **pretraining shortcut** that
  needs disentangling from genuine antonymy knowledge (§1, §5) — independent, same-direction support
  for the project's distributional-shadow reading, from the authors of the antonymy-outlier paper.

## What it cannot ground

- **Any claim about the project's panel — or any model's own behavior.** This is a corpus measurement;
  it contains **no model experiment of its own**. The "antonymy bias" it cites is in BERT/RoBERTa/
  Llama-3-generation PLMs (Pitarch et al. 2023; Cao et al. 2025a), **not** claude-sonnet-4.6 /
  gpt-5.4-mini / gemini-3.5-flash; no transfer to the panel is asserted or implied.
- **A human anchor.** There is no human experiment here; it is a corpus statistic. It cannot serve as
  an `anchors:` resource for any human-comparison claim.
- **The parallel-contrastive-frame mechanism for nouns.** The paper explicitly "**can not answer in
  which lexical and dependency constructions two words are likely to occur**" (Limitations). It grounds
  *co-occurrence strength/order/distance* across PoS, **not** the J&K-style finding that co-occurrences
  are concentrated in syntactically parallel, lexically-identical frames — that frame-concentration
  result remains adjective-only (J&K). Read the cross-relation distinctiveness as the measured claim;
  read the parallel-construction link as the authors' flagged conjecture.
- **A word-sense or referential claim.** Analysis is at the lemma+PoS level with "**no word sense
  disambiguation**" (Limitations); it is sense-agnostic and says nothing about reference.

## Known limits

- **Corpus-only, one corpus.** "**We only studied COCA**" (Limitations); American English, balanced
  genres — a fact about *that* corpus's co-occurrence structure, read forward to a model's training
  distribution only as an interpretive move (the project's, not the paper's).
- **No construction-type / qualitative analysis** (Limitations) — strength/order/distance only.
- **No word-sense disambiguation; lemma+PoS shallow filtering** (Limitations).
- **Imbalanced relation counts** (e.g. 97 nominal antonymy pairs vs 11,664 nominal HYP pairs, Table 1)
  and **extreme G² outliers** for a few nominal antonym pairs (§4) — the averages are read with those
  caveats, which the authors state.
- **arXiv v1 / camera-ready not cross-checked.** Body quotes are from the v1 HTML; the \*SEM 2025
  camera-ready was not consulted, and locators are section-level (no proceedings page numbers).

## Status in wanted.md

Not previously listed by id. Ingested 2026-06-30 (session 149) as the **further primary
antonymy-distribution source bearing on nominal antonymy** that
[`essay/antonymy-outlier-distributional-shadow`](../../findings/essays/antonymy-outlier-distributional-shadow.md)'s
revision trigger (d) was left live for — the cross-PoS, cross-relation companion to the in-repo
adjective-only primary [`source/justeson-katz-1991-antonym-cooccurrence`](justeson-katz-1991-antonym-cooccurrence.md)
and to the same group's model-side paper [`source/cao-2025-semantic-relation-knowledge`](cao-2025-semantic-relation-knowledge.md).
