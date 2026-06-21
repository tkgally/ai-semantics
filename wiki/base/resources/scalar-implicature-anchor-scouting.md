---
type: resource
id: scalar-implicature-anchor-scouting
title: "Scalar-implicature anchor scouting — feasibility catalog for a human signal on how people read scalar quantifiers (some / many / few = 'not all'?)"
meaning-senses:
  - inferential
  - distributional
status: scouting
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: depends-on
    target: result/function-word-few-many-split
  - rel: depends-on
    target: source/davis-2024-implicature-sep
  - rel: supports
    target: essay/function-words-not-one-category
---

# Scalar-implicature anchor scouting — a human signal for the few→many / "many = not all" question

**Scouted:** 2026-06-21. **Purpose:** anchor-feasibility note for the open
trigger **(b)** of [`essay/function-words-not-one-category`](../../findings/essays/function-words-not-one-category.md):
*why* do the panel models diverge on the "Many X → All X" reading — claude keeps it a
contradiction (scalar-bounded *many*, "many **but not all**"), gpt and gemini relax it to
neutral (lower-bounded-only *many*, "many, possibly all") — as localized by
[`result/function-word-few-many-split`](../../findings/results/function-word-few-many-split.md)?
That result is `internal-contrast-only`: it makes **no human comparison** and asserts nothing about
*which* reading is correct. Trigger (b) asks whether a human anchor could fix the correct reading —
i.e. supply a **human signal for how often people draw the upper-bounding "not all" inference for a
given scalar quantifier**, by quantifier and by context. This is **distinct** from the entailment /
NLI gold labels the project already uses (Scivetti CxNLI, e-SNLI): those label *what is said* / at-issue
entailment; what trigger (b) needs is human data on the *cancelable scalar implicature itself* — the
rate at which people read *some* / *many* / *few* as upper-bounded. The
[`source/davis-2024-implicature-sep`](../sources/davis-2024-implicature-sep.md) typology is the
frame: the "not all" reading is a generalized **conversational (scalar) implicature**, cancelable and
(on the standard view) not entailed — so an entailment instrument can legitimately miss it, and a human
*implicature-rate* dataset is a different kind of resource than an NLI gold key.

This is a **scouting** note, not a typed-resource catalog of any one dataset (cf.
[`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md), whose format this
copies). The project's standing rule applies: a resource may be cited only by the *specific
human-produced feature* that bears on the claim, never by existence alone. **No `anchors:` link is
asserted here** — nothing below has been ratified as the anchor; this only records what was checked.

**Honesty up front.** Several candidates came back *paywalled* (the canonical van Tiel 2016 paper) or
*without a clean license file* (the open data mirrors). That is an honest, expected outcome of scouting,
recorded as such. The recommendation at the end is calibrated to it.

---

## What a fit-for-purpose anchor would look like

To upgrade trigger (b) from a within-model contrast to a human comparison, the project needs a human
resource that supplies, for scalar quantifiers (ideally *some*, *many*, *few*, *most*) — **and crucially
not only adjectival scales** — a graded or rate-valued signal of the form: *what proportion of people,
given the weak term, infer that the strong term is false* (the "not all" / upper-bounding inference
rate). The signal should be human-produced, released, and licensed for at least analysis + verbatim
short-quote mirroring. A per-quantifier or per-context rate is the minimal useful grain; a per-item
graded distribution is the ideal grain.

---

## Candidate 1: van Tiel, van Miltenburg, Zevakhina & Geurts (2016), "Scalar Diversity" — the canonical scalar-inference-rate study

**What it is (verified).** The foundational *scalar diversity* paper: van Tiel et al. 2016, "Scalar
Diversity," *Journal of Semantics* 33(1): 137–175, DOI `10.1093/jos/ffu017`. It measures, per lexical
scale, the **rate at which people draw the upper-bounding ("not all"-type) scalar inference**. Experiment 1
presents a weak scalar in a frame and asks whether participants infer the stronger term is false — exactly
the human signal trigger (b) wants. Verified facts (web search of the abstract + secondary literature
citing the paper's design; full PDF not fetched, see below):

- **43 lexical scales** tested, with inference rates ranging from ~4% to ~100% (the "scalar diversity"
  finding — the *point* is that the "not all" rate is **not** constant across scalars).
- The 43 scales break down (per a secondary source describing the paper's Table) as **32 adjective scales,
  6 main-verb, 2 auxiliary-verb, 2 quantifier, 1 adverb**. The **2 quantifier scales** are the directly
  on-target items; `<some, all>` is reported as near-100% inference rate. This is the in-scope signal —
  human "not all"-inference rates for scalar **quantifiers** — even if only a couple of scales are
  quantifier-class.
- Measure = proportion of participants (Exp 1: 25 subjects) drawing the upper-bounding inference, per
  scale. This is the human implicature-rate signal, not an NLI entailment label.

**License (UNVERIFIED → likely restricted for the version-of-record).** The OUP article page
(`https://academic.oup.com/jos/article-abstract/33/1/137/2362956`) shows the paper as **not open access**
— access is by subscription or 24-hour purchase (the abstract page quoted a ~USD 44 / £34 / €40 paywall).
No data-availability statement or OSF link is visible on the abstract page. A **green open-access PDF**
exists in Radboud University's institutional repository
(`https://repository.ubn.ru.nl/bitstream/handle/2066/159838/1/159838.pdf`); this URL returned **HTTP 403
to anonymous WebFetch this session** (a fetch-access limitation, *not* confirmation of a paywall — the
Radboud repository is a recognized OA self-archive). The 2016 paper predates routine machine-readable data
deposits; I found **no OSF/Zenodo repository for the 2016 dataset itself** in this search (later
scalar-diversity papers do deposit data — see Candidate 2).

**Fetchability verdict: P1-content / P3-clean-data — reachable-as-text, license-restricted, no clean data deposit found.**
The *finding* and the per-scale inference-rate table are the most directly on-target human signal in this
search. But the version-of-record is paywalled, the green-OA PDF was not retrievable via WebFetch this run,
and no openly-licensed machine-readable per-scale dataset for the 2016 study was located. So it is P1 for
*relevance* but not a clean P1 *fetch*: a future session would need to (a) retrieve the Radboud OA PDF by a
route WebFetch cannot use, and (b) extract the per-scale rate table by hand, recording it as short
quotes/figures, not wholesale — and even then the quantifier coverage is only ~2 scales.

**What it would let the project ground (if obtained).** A human "not all"-inference-rate baseline for
`<some, all>` (and the second quantifier scale), against which the panel's NLI treatment of the
*some*/*many* upper bound could be compared — directly addressing trigger (b)'s "which reading is correct"
gap for the quantifier domain. It would **not** by itself ground *many* / *few* unless those scales were
among the 43 (only `<some, all>` is confirmed in scope from this search; *many*/*few* coverage is
**unverified**).

---

## Candidate 2: Pankratz & van Tiel — scalar-diversity follow-ups (2021 relevance study; 2025 *JoS* within/across-scale rates)

**What it is (verified).** Two follow-ups extend the scalar-diversity paradigm with **released, open data** —
but both are restricted to **adjectival** scales, which is the key limitation for trigger (b).

- **Pankratz & van Tiel (2021), "The role of relevance for scalar diversity."** Per-trial scalar-inference
  outcomes for weak/strong **adjective** pairs. A copy is hosted openly on the **QML Data** teaching
  repository (Stefano Coretta, University of Edinburgh): page
  `https://uoelel.github.io/qml-data/data/pankratz2021/si.html`, raw CSV
  `https://raw.githubusercontent.com/uoelel/qml-data/main/data/pankratz2021/si.csv` — **fetched and
  inspected this session.** Columns (verbatim header): `weak_adj, strong_adj, SI, freq, semdist, weak_pol,
  bounded, extreme`. `SI` is a per-trial categorical outcome with values `scalar` / `no_scalar` (whether the
  participant drew the inference); example rows are adjective pairs such as `amazing, miraculous`. So the
  file **is** a real, downloadable per-trial scalar-inference dataset — but for **adjectives only**, no
  quantifiers.
- **Pankratz & van Tiel (2025), "Scalar implicature rates vary within and across adjectival scales,"**
  *Journal of Semantics* 42(1–2): 97– (`https://academic.oup.com/jos/article/42/1-2/97/8098202`). Verified
  via the article page: **open access, CC BY**, with a data-availability statement pointing to an OSF
  repository (`https://osf.io/a2gje/` — a `view_only` anonymized link was shown on the page). Covers **~45
  adjectival scales** (down from 77 after scalehood filtering). Title and abstract are explicit that it is
  **adjective**-based, *not* quantifier-based.

**License (verified for 2025; UNVERIFIED for the 2021 mirror).** The 2025 *JoS* paper is **CC BY** (verified
from the article page) with OSF data. The 2021 QML-Data mirror's license could **not** be verified: the
`uoelel/qml-data` repository has **no top-level LICENSE file** (raw `LICENSE` returned HTTP 404 this
session) and the README contains **no licensing/reuse statement** (fetched and checked). So the 2021 CSV is
*reachable and real* but its reuse terms are **unverified** — treat as "unlicensed mirror; verify against the
original Pankratz & van Tiel 2021 deposit before any use."

**Fetchability verdict: P2 — reachable, partly clean-licensed (2025 CC BY), but OFF the quantifier target.**
These are the cleanest *fetchable* scalar-inference-rate data found — but they ground **adjectival** scalar
diversity, and trigger (b) is about the **quantifier** *many*/*few*/*some*. They would let the project
ground the *general* claim "humans draw the 'not all' inference at scale-specific rates" and "scalar
diversity is real," which contextualizes *why a model panel could legitimately diverge* — but they do **not**
supply a per-quantifier human rate for *many*/*few* specifically. Useful as **supporting context**, not as
the direct quantifier anchor.

---

## Candidate 3: Quantifier-interpretation / "how many is many" datasets (Pezzelle; VAQUUM)

This class targets the *vague-quantifier interpretation* tradition (Moxey & Sanford; Pezzelle) — human data
on which quantifier people choose / endorse at a given proportion. It is **adjacent but not identical** to
the implicature-rate target: it tells you the *mapping between proportion and quantifier choice* (when is
"many" apt?), not directly the *rate of the upper-bounding "not all" inference*. Two released datasets were
checked.

- **Pezzelle et al. — `fill-in-the-quant`** (`https://github.com/sandropezzelle/fill-in-the-quant`, code +
  data for Pezzelle, Steinert-Threlkeld, Bernardi & Szymanik 2018, ACL). The associated human paradigm
  (from the "Probing the mental representation of quantifiers" / *Cognition* line) shows participants visual
  scenes and asks them to pick from a 9-quantifier scale (`none, almost none, the smaller part, few, some,
  many, most, almost all, all`) at 17 proportion levels. **Repo reachable** (confirmed it exists), but its
  **README/LICENSE were not machine-readable via WebFetch this session** — license **UNVERIFIED**; whether
  the *human* judgment data (vs. model code) is in the repo was not confirmed file-by-file.
- **VAQUUM — "Are Vague Quantifiers Grounded in Visual Data?"** (Findings of ACL 2025; arXiv 2502.11874;
  repo `https://github.com/hughmee/vaquum`). **Fetched this session.** Releases **20,300 human ratings from
  203 native English speakers**, graded slider (0–100) "appropriateness" of statements like "There are
  [QUANT] [OBJECT]" for an image, quantifiers `few, a few, some, many, a lot of`, in `data/human_ratings.csv`
  (path reported by the repo). This is a **graded human signal on quantifier appropriateness**, directly in
  the *many/few/some* domain — the closest *quantifier-specific* human data found. **License: mixed /
  UNVERIFIED at the judgment level.** The repo has **no top-level LICENSE file** (checked); the README states
  the **images** derive from FSC-147/FSC-133 (MIT), TallyQA (Apache-2.0), Visual Genome / VQA2 (CC BY 4.0) —
  but the **license of the newly-collected human ratings themselves is not stated**. So the human-rating CSV
  is reachable but its reuse terms are unverified.

**Fetchability verdict: P2 (VAQUUM) / P3 (fill-in-the-quant) — reachable, license-unverified, target-adjacent.**
VAQUUM is the most promising *quantifier-specific* human dataset (graded, *many/few/some*, released), but
(i) it measures *visual appropriateness*, not the *"not all" upper-bounding inference rate* trigger (b) is
defined on, and (ii) the human-rating license is unverified. It would let the project ground a *different*
human signal — "how apt is *many* at proportion p" — which bears on the *many*-vs-*all* boundary
**obliquely** (it shows humans grade *many* short of *all*, but does not measure the cancelable implicature).
A future session weighing VAQUUM must decide whether the appropriateness signal is close enough to the
implicature target, and must resolve the rating-license question.

---

## Candidate 4: In-repo precedent — Scivetti CxNLI (PARTIAL; what it does and does not cover)

**Verified from the in-repo resource page** [`resource/scivetti-2025-cxnli-dataset`](scivetti-2025-cxnli-dataset.md).
The project already holds a human-annotated **constructional NLI** dataset (Scivetti et al. 2025), ratified
as the anchor for four CxG conjectures. It contains a phrasal **scalar** construction — **`let-alone`** — and
a single adjudicated gold inference label per item plus an aggregate native-speaker accuracy baseline
(≈0.90 Exp 1 / ≈0.83 Exp 2).

**What it covers for trigger (b): essentially nothing direct.** `let-alone` is a *phrasal* scalar
construction (a quantity/likelihood scale across a clause), **not** the scalar **quantifiers** *some* /
*many* / *few*. CxNLI gives a **single gold entailment label** per item, **not** a per-item human
*implicature-rate distribution* — so even where a scalar item appears, it grounds an *answer key*, not the
*rate at which humans draw the upper-bounding inference*. It is therefore a **partial in-repo precedent**
only: it shows the project already works with human-annotated scalar *constructional* inference, but it does
**not** carry the quantifier-implicature-rate signal trigger (b) needs. It cannot anchor (b).

---

## Anything else that bears

- **Later scalar-diversity replications with open data** (e.g. degree-estimate / relevance follow-ups; an
  OSF `osf.io/fz4du/` was surfaced for a *different*, more recent scalar-inference-calculation study but
  **not opened/verified** this session) suggest the *adjectival* scalar-inference-rate signal is
  increasingly openly deposited. None found this session extends clean open data to the **quantifier**
  scales specifically.
- The **experimental-pragmatics norm** (the *some*→*not all* inference rate as the canonical generalized
  implicature) is exactly the [`source/davis-2024-implicature-sep`](../sources/davis-2024-implicature-sep.md)
  paradigm case (Davis §2, "Some athletes smoke" → "Not all athletes smoke", cancelable). So the *theory*
  side of trigger (b) is in-repo; only the *human-rate dataset* side is missing.

---

## Recommendation

**No clean, openly-licensed, quantifier-specific human scalar-implicature-rate dataset was found this
session.** The honest posture for trigger (b) is therefore: **the human-comparison upgrade stays blocked**,
and the within-model contrast (`internal-contrast-only`) of
[`result/function-word-few-many-split`](../../findings/results/function-word-few-many-split.md) remains the
calibrated posture meanwhile — exactly as that result and the essay already state.

Ranked, for a *future* session that wants to pursue an anchor:

1. **Most on-target signal, but not a clean fetch: van Tiel et al. 2016 (Candidate 1).** It is the only
   source found that measures the human **"not all"-inference rate for scalar quantifiers** (`<some, all>`).
   But the version-of-record is **paywalled**, the green-OA PDF was **not retrievable via WebFetch**, and no
   openly-licensed machine-readable per-scale dataset was located; quantifier coverage is ~2 of 43 scales
   and *many*/*few* inclusion is **unverified**. A future session could try the Radboud OA PDF by a
   non-WebFetch route and extract the `<some, all>` rate as a short quote — a **P1-priority but
   high-friction** fetch, and even then it grounds *some*, not *many*/*few*.

2. **Cleanest fetchable data, but off-target (adjectives): Pankratz & van Tiel 2025 (Candidate 2).**
   **CC BY**, OSF-deposited, ~45 scales — but **adjectival**, so it grounds *scalar diversity in general*
   (context for "why a panel could diverge"), not the *many*/*few* quantifier reading. Good **supporting**
   citation; not the direct anchor.

3. **Most quantifier-specific released human data, license unverified: VAQUUM (Candidate 3).** Graded human
   *appropriateness* of *many/few/some* (20,300 ratings), reachable — but measures visual appropriateness,
   not the implicature rate, and the **rating license is unstated**. A candidate only if a future session
   judges the appropriateness signal close enough and resolves licensing.

**Bottom line.** Trigger (b)'s human-comparison upgrade has **no clean open anchor available now**. The
single most on-target human signal (van Tiel 2016 quantifier inference rates) is paywalled / not cleanly
fetchable; the cleanly-licensed open data (Pankratz & van Tiel 2025; the QML mirror) is **adjectival**, off
the quantifier target; the quantifier-specific open data (VAQUUM) measures appropriateness, not implicature,
under an unverified rating license. So: **`internal-contrast-only` stays the honest posture for the
few→many split**, and trigger (b) remains open. If a future session does pursue this, the cleanest *first*
move is to fetch the Pankratz & van Tiel 2025 CC-BY OSF data as **supporting context** on scalar diversity
(low-friction, clean license), while treating the genuine quantifier anchor (van Tiel 2016 `<some, all>`
rate) as a separate, higher-friction retrieval task — and recording, before any catalogue, that even it does
not directly cover *many*/*few*.

---

## Candidates with unverified elements (summary)

| Candidate | Reachable? | License | Quantifier coverage | Unverified element |
|-----------|-----------|---------|---------------------|--------------------|
| van Tiel 2016 | VoR paywalled; green-OA PDF 403 via WebFetch | restricted (VoR); OA PDF unverified | `<some,all>` confirmed; *many*/*few* **unverified** | could not fetch OA PDF; no open data deposit found; per-scale table not read |
| Pankratz & van Tiel 2021 (QML mirror) | yes (CSV fetched) | **none** (no LICENSE; README silent) — unverified | none (adjectives only) | mirror reuse terms; relation to a primary deposit |
| Pankratz & van Tiel 2025 (*JoS*) | yes (article page) | **CC BY** (verified) + OSF | none (adjectives only) | OSF contents not opened; `view_only` link |
| Pezzelle `fill-in-the-quant` | repo exists | unverified | *some/many/few/most* (9-quantifier scale) | README/LICENSE not machine-read; whether human data is in repo |
| VAQUUM | yes (repo + arXiv fetched) | images mixed (MIT/Apache/CC BY); **ratings unstated** | *few/a few/some/many/a lot of* | human-rating license; measures appropriateness, not implicature rate |
| Scivetti CxNLI (in-repo) | yes (catalogued) | repo no license observed | `let-alone` only (phrasal, not quantifier) | n/a — verified partial; cannot anchor (b) |
