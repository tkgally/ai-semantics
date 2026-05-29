---
type: resource
id: wic-graded-usage-similarity
title: Usim graded usage-similarity ratings (Erk, McCarthy & Gaylord) — with WiC as the binary cross-check
status: external-only
url: https://www.katrinerk.com/graded-sense-and-usage-annotation
url-note: "Erk's graded-sense/usage-annotation landing page (https://www.katrinerk.com/graded-sense-and-usage-annotation) WAS reachable on 2026-05-29 and links a single combined download of both the usage-similarity (Usim) and graded-sense (WSsim) datasets at https://utexas.box.com/shared/static/eim0x9d6wteiisejndzukveh4elywbnl.tgz — but that Box link returned HTTP 404 (Box generic error HTML, ~2.2 KB; following its 301 to utexas.app.box.com also 404) on 2026-05-29, so the data file is NOT currently fetchable. The second-round mirror http://www.dianamccarthy.co.uk/downloads/WordMeaningAnno2012/ returned HTTP 503 on 2026-05-29. The annotation-guidelines subpages and the ACL 2009 PDF WERE retrieved (see Known limits / scope below)."
paper: "ACL 2009 https://aclanthology.org/P09-1002/ ; journal version Computational Linguistics 39(3):511-554, 2013 https://aclanthology.org/J13-3001/ (MIT Press https://direct.mit.edu/coli/article/39/3/511/1437/ — paywalled, returned HTTP 403 on 2026-05-29)"
venue: "Usim: Erk, McCarthy & Gaylord, ACL 2009 / Computational Linguistics 2013. WiC cross-check: Pilehvar & Camacho-Collados, NAACL 2019, https://aclanthology.org/N19-1128/"
meaning-senses:
  - distributional
  - referential
  - human-comparison
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: anchors
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Usim graded usage-similarity ratings (with WiC as the binary cross-check)

This page catalogs a candidate human anchor for the project's first **lexical** finding: the **Usim usage-similarity** ratings of Erk, McCarthy & Gaylord. The load-bearing property — the whole reason this resource is catalogued rather than the more famous WiC — is that Usim carries **graded** (not binary) human judgments of how similar two usages of the same word are. That graded signal is exactly what the gradience hypothesis in [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) needs and what a binary set like WiC cannot supply (see the seed [`open-question/lexical-polysemy-gradience`](../../findings/open-questions/lexical-polysemy-gradience.md), which flags that "WiC alone (binary) underdetermines" the gradience question).

The data **file is not yet mirrored or inspected in-repo, and is not currently fetchable** (`status: external-only`): the advertised Box download returned HTTP 404 and the McCarthy mirror HTTP 503 on 2026-05-29 (see *Known limits*). However, the **scale wording, item/lemma/annotator counts, and the abstract finding WERE verified this run** from primary sources that did load — the ACL 2009 PDF (retrieved via https://aclanthology.org/P09-1002.pdf) and Erk's usage-similarity annotation-guidelines page. Facts below carry their source URL; anything still unverified is flagged inline.

## What it is

**Usim (usage similarity).** A human-rated dataset in which annotators judge, on a **graded 5-point scale**, how similar two usages (two sentence contexts) of the *same* target lemma are — without first committing to a discrete sense label. The full scale wording, **verified verbatim** from the ACL 2009 paper (https://aclanthology.org/P09-1002.pdf, §3 Annotation):

> "The scale was 1 – completely different, 2 – mostly different, 3 – similar, 4 – very similar and 5 – identical."

and the Usim annotator instruction (same source, §3; corroborated on Erk's usage-similarity guidelines page, https://www.katrinerk.com/graded-sense-and-usage-annotation/annotation-guidelines-for-usage-similarity-annotation):

> "Your task is to rate, for each pair of sentences, how similar in meaning the two boldfaced words are on a five-point scale."

Annotators could additionally respond **"Cannot Decide"** (ACL 2009 §3; this occurred in 9 paired occurrences, which were excluded). The dataset was introduced in:

- Katrin Erk, Diana McCarthy & Nicholas Gaylord, *Investigations on Word Senses and Word Usages*, ACL-IJCNLP 2009 (https://aclanthology.org/P09-1002/), and developed in the journal version,
- Katrin Erk, Diana McCarthy & Nicholas Gaylord, *Measuring Word Meaning in Context*, Computational Linguistics 39(3):511–554, 2013 (https://aclanthology.org/J13-3001/).

Scope figures, **verified verbatim from the ACL 2009 PDF (§3 Annotation)** — and these correct an earlier provisional summary that mis-attributed the WSsim figures to Usim:

- **Usim** "used data from LEXSUB" (the English lexical-substitution task). "34 lemmas (nouns, verbs, adjectives and adverbs) were manually selected, including the 3 lemmas also used in WSsim." "Each lemma is the target in 10 LEXSUB sentences. For our experiment, we took every possible pairwise comparison of these 10 sentences for a lemma. We refer to each such pair of sentences as an SPAIR. The resulting dataset comprised 45 SPAIRs per lemma, adding up to **1530 comparisons per annotator** overall." So Usim = **34 lemmas × 45 usage-pairs (SPAIRs) = 1530 pairs**, each rated by **three annotators** ("Three annotators participated in each experiment; all were native British English speakers", ACL 2009 §3).
- **WSsim** (the companion graded-sense set in the same release) is the one with ~11 lemmas: "This experiment contained a total of 430 sentences spanning 11 lemmas (nouns, verbs and adjectives). For 8 of these lemmas, 50 sentences were included, 25 … randomly sampled from SemCor … and 25 randomly sampled from SE-3 [Senseval-3 English lexical sample]. The remaining 3 lemmas … each had 10 sentences taken from the LEXSUB data." (ACL 2009 §3). WSsim has annotators rate the applicability of *each WordNet 3.0 sense* to a usage on the same 5-point scale (rather than picking one winner) — the second graded signal in the release.

> **Correction note:** an earlier provisional version of this page reported "~11 lemmas, ~430 usage-pair items, 3 annotators, SemCor/SE-3/LEXSUB sources" for **Usim**. The primary source shows those figures describe **WSsim** (a *sentence* count, not pairs); **Usim** itself is **34 lemmas / 1530 SPAIRs (45 per lemma) / 3 annotators**, drawn from LEXSUB only. The 3 LEXSUB lemmas are the overlap between the two sets.

The paper's headline finding — that these graded annotations weaken the case for clear-cut sense boundaries — is now quotable **verbatim from the abstract** (ACL 2009, https://aclanthology.org/P09-1002.pdf):

> "We find that the graded responses correlate with annotations from previous datasets, but sense assignments are used in a way that weakens the case for clear cut sense boundaries."

**WiC (Word-in-Context), the binary cross-check.** Pilehvar & Camacho-Collados, NAACL 2019 (https://aclanthology.org/N19-1128/). Each instance gives a target word (a noun or verb) in two sentence contexts; the task is a **binary** judgment:

> "The task is to identify if the occurrences of *w* in the two contexts correspond to the same meaning or not." (pilehvar.github.io/wic, task description; verbatim)

with labels **T** (same meaning) / **F** (different). It is expert-curated from Wiktionary, WordNet and VerbNet, and is released under **CC BY-NC 4.0** (verified from pilehvar.github.io/wic, 2026-05-29). WiC is the cleanest *binary* same/different-sense behavioral target — but it is binary by design, so it can ground the discrete-collapse contrast and a same/different baseline, **not** the gradience (monotonicity-in-relatedness) prediction.

## What it can ground — and the specific feature that bears

This is the key section (charter rule: cite a resource by the *feature* that bears, not by existence).

- **Usim grounds the gradience prediction.** Because Usim ratings are a **continuous-ish 5-point graded human judgment of usage similarity**, they let one ask whether an LLM's same/different-sense behavior (or a representational similarity signal) is **monotonic in the human-rated similarity** of two usages — the load-bearing test for hypothesis 1 (graded-sense tracking) in [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md). This is the property no binary set has.
- **WiC grounds the discrete contrast and a same/different baseline.** Its binary T/F labels anchor the discrete-sense behavior (hypothesis 2) and give a clean, large, well-known reference point for a same/different-sense behavioral probe.
- **Both are `human-comparison` anchors** for a `distributional`-vs-`referential.sense` question: usage similarity / same-meaning judgments are human `referential.sense` (Fregean mode-of-presentation) signals, and the conjecture's null is that LLM behavior reduces to context-similarity (`distributional`).

Together they let the conjecture's **discriminating control** be set up: hold context-similarity roughly constant while letting human-rated sense relatedness vary (Usim's graded scale supplies the relatedness axis; a separate context-overlap measure supplies the distributional axis), so the distributional-shadow hypothesis is separable from genuine sense-relatedness tracking.

## What it cannot ground

- **Reference / extension.** Like every resource in-repo, these carry no human-agreed *extension* or reference relation (see [`concept/referential-meaning`](../concepts/referential-meaning.md) on the standing reference-anchor gap); they bear on `referential.sense`, not `referential.reference`.
- **Over-/under-splitting against a full sense inventory.** That comparison needs a discrete sense inventory (WordNet) and a sense-tagged corpus (SemCor / OntoNotes), which are on the resources shortlist ([`index.md`](../../index.md)) but not catalogued here. Usim deliberately *avoids* committing to a discrete inventory, so it cannot by itself answer the over-/under-splitting question; WSsim (sense applicability) is the closer instrument for that.
- **Polysemy-vs-homonymy contrast out of the box.** Usim rates usage similarity but does not itself tag which pairs are polysemy vs. homonymy; building that contrast requires adding a polysemy/homonymy stratification (e.g., from a dictionary or from WordNet sense-relatedness), which is an extra annotation step, not a property of the released ratings. The conjecture should treat that stratification as work-to-be-done, not as given by this resource.

## Known limits

- **Data file not fetchable; license still unverified (the two blockers to ratifying Option A).** The Erk landing page (https://www.katrinerk.com/graded-sense-and-usage-annotation) loaded on 2026-05-29 and advertises one combined Usim+WSsim download at https://utexas.box.com/shared/static/eim0x9d6wteiisejndzukveh4elywbnl.tgz — but that link returned **HTTP 404** (Box generic error HTML; the 301 to utexas.app.box.com also 404). The second-round mirror http://www.dianamccarthy.co.uk/downloads/WordMeaningAnno2012/ returned **HTTP 503**. So the **actual ratings file could not be retrieved this run**, and its **format is unverified**. **No formal license/terms statement was found** on the Erk page; the only stated condition is a courtesy request — "We would appreciate it if you could let us know that you downloaded the dataset. Just send us an email to: katrin.erk@utexas.edu" (https://www.katrinerk.com/graded-sense-and-usage-annotation, quoted via a content fetch on 2026-05-29). A web search surfaced no working public mirror. (Note: the ACL Anthology copy of the *paper* J13-3001 carries CC BY-NC-SA 3.0 for the *publication*; that is the paper's license, **not** a license on the released ratings.) **Because neither fetchability nor an explicit data license is confirmed, status stays `external-only`.**
- **What WAS verified this run, from primary sources that loaded:** the exact 5-point scale wording and the "Cannot Decide" option (ACL 2009 PDF §3 + Erk's usage-similarity guidelines page); the Usim counts — 34 lemmas, 45 SPAIRs/lemma, 1530 pairs/annotator, 3 native-British-English annotators, LEXSUB source (ACL 2009 PDF §3); the WSsim counts (430 sentences, 11 lemmas, SemCor/SE-3/LEXSUB); and the abstract's "weakens the case for clear cut sense boundaries" finding (ACL 2009 abstract, quoted verbatim above). These no longer need re-confirmation.
- **Small N.** Usim is **1530 usage-pairs over 34 lemmas (45 pairs/lemma)**; any per-lemma graded claim carries wide uncertainty. It is a *gradience-signal* anchor, not a large-coverage benchmark.
- **WiC is binary.** Re-stated because it is the trap the seed warns about: do not use WiC to ground the gradience (monotonicity) claim; use it for the binary/discrete contrast only.
- **Two graded sub-datasets, distinct roles.** Usim (usage-pair similarity) and WSsim (per-sense applicability) are different instruments; a probe should name which it uses. This page anchors primarily on **Usim** (usage similarity) as the cleanest graded usage-relatedness signal.

## Pointer for next visit

1. **Re-attempt to retrieve the actual ratings file.** The advertised Box link 404'd and the McCarthy mirror 503'd on 2026-05-29. Try again later, or email katrin.erk@utexas.edu (the page's stated contact) for a current download; if/when retrieved, check the in-file license/README and **mirror into `experiments/data/usim/`** (not the wiki) if terms permit, otherwise work against it in place. **This is the remaining blocker** — counts and scale are already verified (above).
2. **Resolve the license question.** No explicit data license was found, only a courtesy email request. Until an explicit license (or author permission) is on record, treat reuse conservatively; this, together with fetchability, is what keeps the page at `external-only`.
3. Decide and queue the **anchor decision** for [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md): is Usim (graded) the ratified gradience anchor, with WiC as the binary cross-check, or is a different graded set preferred? (The conjecture currently marks its anchor as a candidate, not ratified; the open decision is [`lexical-sense-gradience-anchor`](../../decisions/open/lexical-sense-gradience-anchor.md).)
4. Add WordNet + SemCor/OntoNotes as their own resource page(s) if/when the over-/under-splitting arm of the conjecture is pursued.
