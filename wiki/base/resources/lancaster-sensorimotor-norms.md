---
type: resource
id: lancaster-sensorimotor-norms
title: Lancaster Sensorimotor Norms (Lynott et al. 2020)
status: catalogued
url: https://osf.io/7emr6/
url-note: "OSF project https://osf.io/7emr6/ ; the aggregate data file `Lancaster_sensorimotor_norms_for_39707_words.csv` lives in the OSF 'Data' component (node rwhs6, file id 48wsc). Download https://osf.io/download/48wsc/ — fetched + verified THIS session (2026-05-30): 17,196,336 bytes, sha256 445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5. Interactive lookup tool: https://www.lancaster.ac.uk/psychology/lsnorms/."
paper: "Lynott, D., Connell, L., Brysbaert, M., Brand, J., & Carney, J. (2020). The Lancaster Sensorimotor Norms: multidimensional measures of perceptual and action strength for 40,000 English words. Behavior Research Methods 52(3): 1271–1291."
venue: "Behavior Research Methods 52(3): 1271–1291 (2020)"
license: "Creative Commons Attribution 4.0 International (CC BY 4.0) — confirmed. Permits use, sharing, adaptation, distribution, and reproduction with attribution, including derivative works."
local-path: "experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/lemma_perceptual.csv (small derived join table only; full CSV gitignored, sha256-pinned, re-downloadable)"
meaning-senses:
  - grounded
  - grounded.perceptual
  - human-comparison
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
  - rel: depends-on
    target: concept/embodied-cognition
---

# Lancaster Sensorimotor Norms (Lynott et al. 2020)

> **Verification status (2026-05-30):** Citation, dimension structure, rater counts, derived columns, and license were confirmed against the primary paper. The aggregate CSV was **downloaded and checksummed this session** — `Lancaster_sensorimotor_norms_for_39707_words.csv`, 17,196,336 bytes, sha256 `445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5` from `https://osf.io/download/48wsc/` (OSF node rwhs6). License **CC BY 4.0** confirmed. The full CSV is gitignored (re-downloadable, sha256 pinned); a small derived join table is committed in-repo (see *Where it lives*). This page catalogs the resource as the **text-side perceptual-grounding moderator** for prediction 1 of [`conjecture/multimodal-lexical-grounding-divergence`](../../findings/conjectures/multimodal-lexical-grounding-divergence.md).

This page catalogs the Lancaster Sensorimotor Norms — the text-side perceptual-grounding resource scouted as **Candidate 3** in [`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md) and recommended there as "the cleanest text-side bridge to the multimodal axis." The scouting note verified license, counts, and OSF URL; this page records that the aggregate data file has since been fetched and checksummed, and states precisely what the norms can and cannot anchor.

## What it is

The Lancaster Sensorimotor Norms provide human ratings of **39,707 English words** on **11 sensorimotor dimensions**, split into two groups:

- **6 perceptual modalities:** Auditory, Gustatory, Haptic, Interoceptive, Olfactory, Visual.
- **5 action effectors:** Foot/leg, Hand/arm, Head, Mouth/throat, Torso.

Each word carries a **mean strength score on a 0–5 scale** per dimension — how strongly, on average, raters reported experiencing the word's referent through that modality or with that effector. The rating prompt is direct and perceptual; e.g., "to what extent do you experience THUNDER by hearing?" The signal is a **multi-rater human mean**, not a derived or automatic label.

### How it was made

Each word was rated by **at least 10 participants**; words averaged **~18.0 ratings** on the perceptual side and **~19.1** on the action side. The total rater pool was **3,500 unique participants** recruited via Amazon Mechanical Turk. Every cell of the aggregate norms is the mean of multiple independent human judgments about a single word along a single sensorimotor dimension.

### Derived summary columns

Beyond the 11 per-dimension means, the aggregate CSV ships derived summary columns that pre-compute the most common aggregate measures of perceptual/action strength:

- `Max_strength.perceptual` — the maximum across the six perceptual modalities (how strongly a word is grounded in its single dominant perceptual channel).
- `Minkowski3.perceptual` — a Minkowski-distance (order 3) aggregate across the perceptual dimensions.
- `Exclusivity.perceptual` — how concentrated a word's perceptual strength is in one modality vs. spread across many.
- `Dominant.perceptual` — the modality with the highest strength (e.g., "Visual").
- `.action` and `.sensorimotor` variants of the above (the latter aggregating over all 11 dimensions).
- `Percent_known` — the proportion of raters who reported knowing the word.

## License

**Verified license (2026-05-30): Creative Commons Attribution 4.0 International (CC BY 4.0).** This is one of the cleanest licenses among the multimodal-anchor candidates: it permits use, sharing, adaptation, distribution, and reproduction in any medium, including derivative works, subject only to attribution. Unlike [`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md) (CC BY-**ND** 4.0, which prohibits distributing modified versions), CC BY **permits distributing a derived/augmented table** — so the derived join table committed in-repo (a perceptual-strength annotation of the DWUG EN lemmas) is licensed-clean to commit and share with attribution.

## What it can ground

This is the key section (charter rule: cite a resource by the *feature* that actually bears).

**The Lancaster Sensorimotor Norms are a TEXT resource about the *perceptual grounding of words*** — they grade how strongly each English word is experienced through each modality and effector. They do not contain images, audio, or any non-verbal stimulus; they are human *verbal* ratings of perceptual associations. In the gradual-grounding framing the project adopts ([`concept/grounding`](../concepts/grounding.md), Lyre's "grounding comes in degrees"), the norms supply a continuous, human-produced **gradient of perceptual groundedness** for ~40k words — exactly the moderator a non-binary grounding probe needs. Harnad's symbol-grounding problem ([`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md)) and Barsalou's perceptual-symbols / embodied-cognition line ([`concept/embodied-cognition`](../concepts/embodied-cognition.md)) are the conceptual backdrop — the norms operationalize "how perceptual is this word" without committing to either's strong theoretical claims.

**Specifically, the norms anchor prediction 1 of [`conjecture/multimodal-lexical-grounding-divergence`](../../findings/conjectures/multimodal-lexical-grounding-divergence.md).** That prediction is the **$0, text-side, runnable-now** bridge to the multimodal axis: re-analyze the *already-collected* text-only panel ratings from [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md), moderated by each lemma's Lancaster perceptual strength, and ask whether the text-only panel's DWUG sense-relatedness **monotonicity is stronger for perceptually grounded lemmas** than for abstract ones. The norms become a **continuous moderator variable** (the perceptual groundedness of the target word); the DV is the model's rank-agreement with the human DURel signal. This is a join of two already-validated human resources — no new API probe — and it respects Tom's no-local-compute constraint.

More precisely, the norms ground:

- `grounded.perceptual` × `human-comparison`: a continuous, multi-rater human signal of *how perceptually grounded* a word is, against which a text-only model's sense-tracking quality can be moderated. This is the perceptual analogue of the project's DURel-graded lexical probe, on the word axis.
- A **modality-typed** moderation: because the norms separate Visual / Haptic / Auditory etc., one can ask whether the *type* of grounding (not just the amount) predicts model behavior — though this is a richer claim than prediction 1 strictly requires.

The derived join table actually committed in-repo carries the `Max_strength.perceptual`, `Minkowski3.perceptual`, `Visual.mean`, `Haptic.mean`, `Auditory.mean`, `Dominant.perceptual`, and `Percent_known.perceptual` columns for the DWUG EN lemmas (see *Where it lives*).

## What it cannot ground

Be honest about the limits — they are sharp:

- **Word-level, not word-SENSE-level.** The norms give one perceptual-strength score *per word*, aggregated across all its senses. A polysemous word (e.g. *bank*) gets a single Visual/Haptic/… profile that does not distinguish its senses. So the norms **cannot** supply a sense-disambiguated perceptual contrast and **cannot** by themselves ground the polysemy/homonymy discreteness question.
- **No images, no sense-level perceptual contrast.** The norms carry no visual stimuli and no per-usage depiction. They therefore bear on **prediction 1 only** of the multimodal conjecture — the text-side moderation — and **not** on predictions 2–3, which require actual image input paired to each usage. They are a moderator on existing text data, not a substitute for an image-paired anchor.
- **Not a usage-pair / gradience anchor.** The norms do not carry graded usage-pair proximity for the same lemma (that is DWUG's contribution; see [`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md)). They cannot replace the DWUG anchor for the monotonicity/gradience probe — they moderate it.
- **Perceptual strength is not reference-fixing.** Rating how strongly a word is experienced visually says nothing about what it picks out in the world. The norms bear on `grounded.perceptual` and (as a moderator) `referential.sense`; they **do not touch `referential.externalist`** (Putnam/Evans, still un-anchored in-repo). Do not let a perceptual-strength effect be read as the model tracking *reference*.
- **Not a constructional resource.** The norms are about word properties, not construction meaning; they cannot anchor a constructional-inference claim.
- **Perceptual association ≠ a perceptual symbol system.** Consistent with the embodied-cognition caveat ([`concept/embodied-cognition`](../concepts/embodied-cognition.md)): a high Visual rating is a human *verbal report* of a perceptual association, not evidence of Barsalou-style modal simulators in either humans or models.

## Where it lives — download and in-repo handling

- **OSF project:** https://osf.io/7emr6/ (the Lancaster Sensorimotor Norms project).
- **Aggregate data file:** `Lancaster_sensorimotor_norms_for_39707_words.csv`, in the OSF "Data" component (node `rwhs6`, file id `48wsc`). Direct download: https://osf.io/download/48wsc/ — **fetched and verified this session:** 17,196,336 bytes, sha256 `445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5`.
- **Interactive lookup tool:** https://www.lancaster.ac.uk/psychology/lsnorms/ (word lookup and export).
- **In-repo handling:** The full CSV is **gitignored** (re-downloadable, sha256 pinned above). A small derived join table — the **42 of the 43 DWUG EN lemmas that are covered × their perceptual scores** — is committed at `experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/lemma_perceptual.csv`. CC BY 4.0 permits committing this derived table. The single DWUG EN lemma **absent from the Lancaster norms is `lass`** (`lass_nn`, marked `covered=0` in the join table); all other DWUG EN lemmas are covered.

## Known limits / scope

- **CC BY 4.0 (clean).** Permits derivative distribution with attribution — a derived join table may be committed in-repo, unlike the DWUG ND license.
- **Word-level aggregate only.** One score per word across all senses; no sense disambiguation, no images. Bears on prediction 1 of the multimodal conjecture, not 2–3.
- **Coverage of DWUG EN:** 42/43 lemmas covered; `lass` is the lone absentee. The norms cover 39,707 common English words, so most content words of interest are present.
- **Data: aggregate CSV fetched + checksummed (2026-05-30), gitignored.** The derived join table is committed and inspected; the full per-word CSV is re-downloadable from the pinned sha256.

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Citation (Lynott, Connell, Brysbaert, Brand & Carney 2020, BRM 52(3):1271–1291) | **VERIFIED** | Primary paper |
| 39,707 words; 11 dimensions (6 perceptual + 5 action) | **VERIFIED** | Primary paper + aggregate CSV header |
| 0–5 mean strength per dimension | **VERIFIED** | Primary paper |
| ≥10 raters/word; ~18.0 perceptual / ~19.1 action; 3,500 unique MTurk raters | **VERIFIED** | Primary paper |
| Derived columns (Max_strength / Minkowski3 / Exclusivity / Dominant per perceptual/action/sensorimotor; Percent_known) | **VERIFIED** | Aggregate CSV header |
| License CC BY 4.0 | **VERIFIED** | Primary paper (PMC full text) |
| OSF aggregate CSV: 17,196,336 bytes, sha256 445d363f… | **VERIFIED (downloaded this session)** | curl from https://osf.io/download/48wsc/ (node rwhs6, file 48wsc), 2026-05-30 |
| 42/43 DWUG EN lemmas covered; `lass` absent | **VERIFIED** | Derived join table `lemma_perceptual.csv` (covered column) |
| Per-sense perceptual contrast | **NOT PROVIDED** | Norms are word-level; one score across all senses |
| Image / non-verbal stimuli | **NOT PROVIDED** | Norms are human verbal ratings only |

## Pointer for next visit

1. **Use as the prediction-1 moderator now.** The join table is committed; run the moderated re-analysis of [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md) (does text-only monotonicity strengthen with perceptual grounding?). Any result is contingent on the `multimodal-panel-and-grounding-theory` decision until ratified.
2. **Decide which perceptual aggregate to privilege** (Max_strength vs. Minkowski3 vs. a single modality like Visual.mean) and freeze it before reporting, per charter §8 (instrument-before-results). The PREREG in the run directory should fix this.
3. **Do not over-reach to predictions 2–3.** Those need an image-paired, sense-level resource; the Lancaster norms cannot supply per-sense perceptual contrast.
4. **Handle `lass` explicitly** (the one uncovered DWUG lemma) — drop or note it in any moderation analysis.
