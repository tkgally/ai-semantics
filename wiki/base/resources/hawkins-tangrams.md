---
type: resource
id: hawkins-tangrams
title: Hawkins/Stanford Tangrams Repeated-Reference Corpus (Hawkins, Frank & Goodman 2020)
status: verified
url: https://github.com/hawkrobe/tangrams
url-note: "Raw corpus file `data/tangrams.csv` fetched THIS session (2026-05-31) from https://raw.githubusercontent.com/hawkrobe/tangrams/master/data/tangrams.csv — HTTP 200, 3,133,874 bytes, sha256 db8cee9d1008688b37816e2a3b45644e0a41e9abc34ba59bf181d302c5c9c52e. The `master` branch path resolved (the `main` fallback was not needed). Raw corpus NOT mirrored in-repo (recipe-not-corpus posture, see License)."
paper: "Hawkins, R. D., Frank, M. C., & Goodman, N. D. (2020). Characterizing the dynamics of learning in repeated reference games. Cognitive Science 44(6): e12845. https://doi.org/10.1111/cogs.12845"
venue: "Cognitive Science 44(6): e12845 (2020)"
license: "GitHub repository declares `license: null` (no LICENSE file / no SPDX identifier). The only release statement is the authors' published claim that they release an open corpus (see License section). Recipe-not-corpus posture applied: read/compare under academic-research norms; raw data NOT redistributed."
local-path: "experiments/runs/2026-05-31-hawkins-tangrams-catalog/entrainment_by_repetition.csv (small DERIVED aggregate entrainment table only; raw tangrams.csv gitignored, sha256-pinned, re-downloadable). Derivation script: experiments/runs/2026-05-31-hawkins-tangrams-catalog/derive.py."
meaning-senses:
  - relational
  - distributional
  - human-comparison
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: anchors
    target: open-question/relational-meaning-pilot
  - rel: depends-on
    target: concept/relational-meaning
---

# Hawkins/Stanford Tangrams Repeated-Reference Corpus (Hawkins, Frank & Goodman 2020)

> **Verification status (2026-05-31):** Raw corpus `data/tangrams.csv` was **downloaded and checksummed this session** — 3,133,874 bytes, sha256 `db8cee9d1008688b37816e2a3b45644e0a41e9abc34ba59bf181d302c5c9c52e`, from `https://raw.githubusercontent.com/hawkrobe/tangrams/master/data/tangrams.csv` (HTTP 200; the `master` branch path resolved, no `main` fallback needed). The actual column header, row counts, dyad/repetition counts, and the per-repetition entrainment curve below were all **read off the actual file** (no figure here is from the paper or fabricated). The raw corpus is **gitignored** (recipe-not-corpus posture); a small **derived aggregate** entrainment table is committed (see *Where it lives*). License is **`license: null` on GitHub** — only the authors' "open corpus" release statement supports use; this page applies the same conservative posture as [`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md). This catalogs the resource ratified by Tom on 2026-05-31 ([`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md), Option A) as the in-repo **human convergence/entrainment baseline** for [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md).

This page catalogs the Hawkins/Stanford tangrams repeated-reference corpus — the modern, released, corpus-scale replication of the Clark & Wilkes-Gibbs 1986 tangram referential-communication paradigm. It was scouted in [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md) and ratified there (Option A) as the fetchable human baseline that unblocks the relational pilot's entrainment groundwork while the ratified-but-unfetchable Clark & Wilkes-Gibbs 1986 stays queued in `base/wanted.md`.

## What it is

The corpus is a record of **human dyads playing an iterated tangram reference game**. Two participants (one *director*, one *matcher*) repeatedly refer to a fixed set of hard-to-name abstract tangram figures across several repetition blocks; over repetitions, dyads coin and compress a shared label for each figure. This is the canonical lexical-entrainment / convention-formation paradigm.

The authors describe the release as an open corpus. The associated repository / paper states (per the scouting note's verbatim record and [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md)):

> "We release an open corpus (>15,000 utterances) of extended dyadic interactions."

The actual `data/tangrams.csv` inspected this session contains **17,431 data rows** (one row per message/utterance), consistent with the ">15,000 utterances" release statement (the exact total depends on what is counted as an "utterance"; the file row count is reported here as the measured figure).

### Verified structure (read off the file, 2026-05-31)

- **Rows:** 17,432 lines total = 1 header + **17,431 data rows**. Each data row is **one message (utterance)** in a dyad's interaction.
- **Distinct dyads (`gameid`):** **137**.
- **Distinct trials (`gameid` × `trialNum`):** **6,030**.
- **Roles (`role` column):** `director` (13,315 messages) and `matcher` (4,116 messages) — directors talk far more, as expected in this paradigm.
- **Repetition blocks (`repetitionNum`):** 1–6, with message counts 4875 / 3327 / 2726 / 2249 / 2105 / 2149 (note the message count itself drops across repetitions — fewer words *and* fewer turns are needed as a convention forms).
- **`correct` column:** the trial outcome, recorded as `1` (7,821 messages), `0` (1,246 messages), or `NA` (8,364 messages). The value is **constant within a trial** (0 of 6,030 trials carry conflicting non-NA values), so accuracy is correctly computed at the trial level, not the message level (see *Derived entrainment curve*). The NA messages are turns where no per-trial outcome was attached.
- **`numRawWords` column:** integer word count of each message; **no blank/NA values** (every one of the 17,431 messages carries a numeric word count). This is the load-bearing utterance-length / compression signal.

### Actual column header (verbatim, all 21 columns)

```
gameid,msgTime,trialNum,repetitionNum,role,intendedName,timeElapsed,contents,totalLength,thinksHuman,comments,ratePartner,nativeEnglish,time,intendedObj,clickedObj,objBox,correct,numRawWords,repetitionScore,taskVersion
```

The columns expected by the task brief (`gameid, repetitionNum, role, contents, correct, numRawWords`) are all present; the file carries many additional columns (timestamps, the matcher's `clickedObj` vs the director's `intendedObj`, a `repetitionScore`, a `taskVersion`, post-game survey fields like `thinksHuman`/`ratePartner`/`nativeEnglish`/`comments`).

## The load-bearing feature

The feature that makes this corpus the right anchor for the relational pilot is **ORDERED per-dyad referring-expression histories**: for each `gameid`, the messages are time-stamped (`msgTime`, `time`) and tagged with `trialNum`, `repetitionNum`, `role`, the trial outcome (`correct`), and the utterance length (`numRawWords`), with the actual referring expression in `contents`. This preserves, per dyad, the *trajectory* by which a shared convention is coined and compressed — not merely the set of utterances that occurred.

That ordered structure supplies two things the relational pilot ([`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md)) names explicitly:

1. **A human entrainment/compression curve** — utterance length should drop and accuracy should rise across repetitions — against which the LLM dyads' convergence is calibrated (so "convergence" is not an artifact of a trivially easy referent set; this is commitment (c) of the pilot's evidential bar).
2. **A human reference point for what trajectory-dependent convergence looks like** — because the histories are ordered, not bagged.

## Derived entrainment curve (computed from the raw file, 2026-05-31)

`experiments/runs/2026-05-31-hawkins-tangrams-catalog/derive.py` (pure stdlib, no numpy) reads the gitignored raw `tangrams.csv` and emits the committed aggregate table `entrainment_by_repetition.csv`. Per `repetitionNum`: message count, mean message length (`numRawWords`), and trial-level mean accuracy (`correct`, computed once per trial to avoid over-weighting multi-message trials). **These are the measured human numbers, not the paper's:**

| repetitionNum | n_messages | mean utterance length (numRawWords) | n_scored_trials | mean accuracy (correct) |
|---|---|---|---|---|
| 1 | 4875 | 7.73 | 996 | 0.780 |
| 2 | 3327 | 6.27 | 996 | 0.867 |
| 3 | 2726 | 5.25 | 996 | 0.902 |
| 4 | 2249 | 4.52 | 996 | 0.920 |
| 5 | 2105 | 4.15 | 996 | 0.949 |
| 6 | 2149 | 4.10 | 996 | 0.942 |

The curve is exactly the textbook signature of human lexical entrainment: **mean utterance length falls monotonically (7.73 → 4.10 words, a ~47% compression) while accuracy rises (0.78 → ~0.94)** across the six repetition blocks. This is the human compression/convergence baseline the relational pilot calibrates against. (The slight accuracy dip and message-count uptick at repetition 6 are within the corpus and reported as measured, not smoothed.)

## What it CAN ground

This is the key section (charter rule: cite a resource by the *feature* that actually bears).

**The Hawkins tangrams corpus grounds the human convergence/entrainment baseline for the relational pilot.** It supplies, in-repo and machine-readable (via the derived table), the human entrainment/compression curve — the scaffolding measures the pilot reports: referential-success rate over rounds and the lexical-convergence/compression curve. These are commitment (c) of the pilot's concrete evidential bar: the LLM dyads' live-condition convergence dynamics must be *at least as history-shaped* as this human baseline, so that observed "convergence" is not an artifact of trivially easy referents.

Specifically it grounds:

- `relational` × `human-comparison`: a human dyadic-interaction resource (not model-agreement) for what convention-formation between agents looks like — exactly the kind of independent human signal the pilot requires (commitment 2: "the comparison is against independent human data, never model agreement").
- `distributional` × `human-comparison`: the entrainment/compression curve is the eye-catching coordination signal that the *deflationary* (purely distributional) story predicts equally. The corpus thus also calibrates the **floor** the pilot must beat — it shows what convergence-without-a-constitution-test looks like at human scale.

## What it CANNOT ground

Be honest about the limits — they are sharp:

- **It does NOT anchor the live-vs-shuffled trajectory-dependence measure — the pilot's load-bearing contrast.** The corpus records *live* human dyads only; it contains **no order-scrambled / shuffled-history replay condition** and **no single-agent-with-self baseline**. The live-vs-shuffled gap is **NOVEL to the LLM probe** and is **NOT anchored by Hawkins**. Hawkins grounds the human convergence/entrainment baseline (commitment c), not the discriminating trajectory-dependence contrast (commitments a–b). This is stated as ratified in [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md): "the live-vs-shuffled trajectory-dependence measure (novel to the LLM probe) is still not anchored by Hawkins." A relational *positive* cannot be earned from this corpus alone.
- **It supplements, does not replace, the ratified theoretical anchor.** Clark & Wilkes-Gibbs 1986 remains the ratified theoretical reference ([`decisions/resolved/relational-anchor-shortlist`](../../decisions/resolved/relational-anchor-shortlist.md), Option A); Hawkins is the fetchable empirical *replication* of that paradigm. It does not discharge the C&W-G fetch obligation for any claim that turns on the original demonstration.
- **No reference/externalism, no LLM-vs-human meaning claim by itself.** The corpus is a human convergence baseline; it does not by itself license a claim that an LLM *means* anything. It bears on `relational` convergence dynamics, not on `referential.reference` or `referential.externalist`.
- **Tangram referents are deliberately hard-to-name and culture/visual-specific.** Calibration transfers to LLM dyads only insofar as the LLM referents are matched in difficulty; the corpus does not certify that any chosen LLM referent set is comparably hard.
- **Not a constructional or lexical-sense resource.** It carries no minimal pairs, no sense annotation, no acceptability ratings; it cannot anchor constructional or lexical-gradience probes (that is DWUG / CxG territory).

## License

**Verified posture (2026-05-31):** The GitHub repository `hawkrobe/tangrams` declares **`license: null`** — there is no `LICENSE` file and no SPDX identifier. The only basis for use is the authors' published release statement that they release an *open corpus* (Hawkins, Frank & Goodman 2020, *Cognitive Science*; "We release an open corpus (>15,000 utterances) of extended dyadic interactions"). There is **no** explicit grant of redistribution rights.

This page therefore applies the **same conservative recipe-not-corpus posture** the project already applies to CC BY-ND DWUG ([`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md)) — and which Tom ratified for this corpus specifically ([`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md), Option A):

- **Permitted (as applied here):** Reading the corpus and computing aggregate analyses under academic-research norms; committing the **download recipe + sha256** and a **small derived aggregate table** (the per-repetition entrainment curve — no raw utterances).
- **NOT done / not redistributed:** The raw `data/tangrams.csv` (which contains 17,431 verbatim human utterances and post-game free-text comments) is **gitignored and NOT mirrored or redistributed in-repo**. No raw utterance text is committed anywhere in this repository.
- **Mirrors DWUG wording:** As with DWUG ("Data not mirrored in-repo"; commit only the recipe), the wiki stays license-clean regardless of the unspecified redistribution terms, because the load-bearing raw text never enters the repo.

If a future use needs to redistribute the raw corpus (it does not, for the entrainment baseline), that requires explicit author license confirmation (Option B of the decision), which was *not* taken.

## Where it lives — download and in-repo handling

- **Repository:** https://github.com/hawkrobe/tangrams
- **Raw corpus file:** `data/tangrams.csv`. Direct download (verified this session): `https://raw.githubusercontent.com/hawkrobe/tangrams/master/data/tangrams.csv` — HTTP 200, **3,133,874 bytes**, sha256 `db8cee9d1008688b37816e2a3b45644e0a41e9abc34ba59bf181d302c5c9c52e`. The `master` branch path resolved; the `main` fallback was not needed.
- **In-repo handling:** The raw CSV is **gitignored** at `experiments/data/hawkins-tangrams/` (re-downloadable; sha256 pinned above). The committed artifacts are:
  - `experiments/runs/2026-05-31-hawkins-tangrams-catalog/derive.py` — the pure-stdlib derivation script (reads the gitignored raw, emits the aggregate table).
  - `experiments/runs/2026-05-31-hawkins-tangrams-catalog/entrainment_by_repetition.csv` — the small derived aggregate entrainment table (no raw utterances).

To reproduce: download the file to `experiments/data/hawkins-tangrams/tangrams.csv`, verify the sha256, then run `python3 experiments/runs/2026-05-31-hawkins-tangrams-catalog/derive.py`.

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Citation (Hawkins, Frank & Goodman 2020, *Cognitive Science* 44(6):e12845) | **VERIFIED (from brief + decision)** | Task brief + [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md); DOI not independently re-fetched this session |
| Download URL `…/master/data/tangrams.csv` HTTP 200 | **VERIFIED (this session)** | curl 2026-05-31 |
| File size 3,133,874 bytes; sha256 `db8cee9d…c9c52e` | **VERIFIED (this session)** | sha256sum 2026-05-31 |
| Column header (21 columns, verbatim above) | **VERIFIED (this session)** | head of tangrams.csv |
| 17,431 data rows; 137 dyads; 6,030 trials; reps 1–6 | **VERIFIED (this session)** | csv parse of tangrams.csv |
| `correct` constant within trial (0 conflicting trials) | **VERIFIED (this session)** | csv parse |
| Entrainment curve (length 7.73→4.10; accuracy 0.78→0.94) | **VERIFIED (this session, measured)** | `derive.py` → `entrainment_by_repetition.csv` |
| "We release an open corpus (>15,000 utterances)…" | **VERIFIED verbatim (secondary, via decision + open-question page)** | Quoted in [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md) and [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md); **paper PDF not fetched this session** |
| GitHub `license: null` (no LICENSE/SPDX) | **VERIFIED (from scouting + decision)** | [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md); GitHub API not independently re-queried this session |
| Live-vs-shuffled / trajectory-dependence anchor | **NOT PROVIDED** | Corpus is live dyads only; control is novel to the LLM probe |
| Exact ">15,000 utterances" vs. measured 17,431 rows reconciliation | **OPEN (definitional)** | "Utterance" counting rule not confirmed against the paper |

## Provenance gaps (honest)

- **The paper PDF was NOT fetched this session.** The citation (*Cognitive Science* 44(6):e12845, DOI 10.1111/cogs.12845), the venue, and the "We release an open corpus (>15,000 utterances)…" release statement are carried from the scouting note and the ratified decision page, not re-verified against the primary paper here. Every *count and the entrainment curve*, by contrast, is read directly off the downloaded file.
- **The ">15,000 utterances" claim vs. the measured 17,431 rows is a definitional, not a contradiction:** the file has one row per message; what the authors count as an "utterance" (message vs. turn vs. cleaned utterance) is not confirmed. The 17,431 is the file row count; the >15,000 is the authors' statement. Both are reported as-is.
- **License is `license: null`.** Use rests on the authors' "open corpus" statement plus academic-research norms; redistribution terms are unspecified. The recipe-not-corpus posture (raw gitignored, no redistribution) keeps the repo license-clean regardless. This is the conservative reading Tom ratified.

## Pointer for next visit

1. **Anchor use is bounded:** Hawkins grounds the human convergence/entrainment *baseline* (commitment c of the pilot's bar) — NOT the live-vs-shuffled trajectory-dependence contrast (commitments a–b), which is novel to the LLM probe and unanchored by any human resource. Keep this distinction in any relational `result` that links here.
2. **Fetch the primary paper** when convenient to verify the "open corpus / >15,000 utterances" statement verbatim and the e12845 details against the PDF (currently secondary).
3. **Clark & Wilkes-Gibbs 1986 remains the ratified theoretical anchor** and is still unfetched ([`base/wanted.md`](../wanted.md)); Hawkins supplements, does not replace it.
4. **Re-download + sha256-verify** before any analysis run (the raw is gitignored); the derivation is reproducible via `derive.py`.
