# NEXT.md

## State

Workflow-mode continuous run: **9 waves** (orchestrator + parallel generation subagents + an adversarial coherence pass per wave, plus a closing identity/coherence audit), one PR. All waves gated clean (senselint 0 errors; linkify clean). What landed:

- **Scivetti 2025 dataset catalogued + surfaced.** New [`resource/scivetti-2025-cxnli-dataset`](wiki/base/resources/scivetti-2025-cxnli-dataset.md) (CxNLI 435 triples/8 constructions; CxNLI-Distinction 99/5; native-speaker baseline ≈0.90/≈0.83; 3-way NLI). Documented at the **paper level only** — the release repo (`anonymous.4open.science/...`) was **not reachable** this run, so `status: external-only`, item-level inspection pending. **Surfaced (not auto-resolved)** as a candidate Option D in `caused-motion-anchor`, `conative-anchor`, `way-construction-anchor`, and (default Option A) the new `comparative-correlative-anchor`.
- **First human-anchored claim.** [`claim/constructional-divergent-form-generalization-gap`](wiki/findings/claims/constructional-divergent-form-generalization-gap.md) — LLMs track constructional form–meaning pairings "up to a point" but show a >40% (GPT-o1) divergent-form gap vs. the human baseline. Anchored to the Scivetti resource; aggregate-scoped so `contingent-on: []`. Carefully bounded (a gap, not an absence).
- **Comparative-correlative wedge added.** New [`source/weissweiler-2022-comparative-correlative`](wiki/base/sources/weissweiler-2022-comparative-correlative.md) (encoder PLMs recognise CC form but fail to use its meaning), [`conjecture/comparative-correlative-construction`](wiki/findings/conjectures/comparative-correlative-construction.md) (the project's first *longitudinal* construction conjecture: 2022 encoders → 2025 decoders), and [`design/comparative-correlative-v1`](experiments/designs/comparative-correlative-v1.md) (covariation-inference probe, NLI + forced-choice, cost <$1).
- **Mahowald 2023 AANN paper** now has its own [`source/mahowald-2023-aann-judgments`](wiki/base/sources/mahowald-2023-aann-judgments.md) (argument/findings; the dataset was already the stimuli resource); directly grounds the AANN-ceiling claim.
- **Theory page** folded in the four filled concepts + the Scivetti claim at the Tier 3→4 boundary; outbound link graph completed in the audit.
- **Relational axis sharpened.** [`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md) is now a concrete iterated-reference-game pilot (live-vs-shuffled trajectory-dependence discriminator); opened `relational-anchor-shortlist`; added relational wants.
- **Lexical axis seeded.** [`open-question/lexical-polysemy-gradience`](wiki/findings/open-questions/lexical-polysemy-gradience.md) — first non-grammatical wedge (graded polysemy vs. discrete sense; candidate anchors WiC / graded usage-similarity / WordNet-SemCor; no decision opened).
- **New methodological open-question + decision.** [`open-question/constructional-divergence-probe`](wiki/findings/open-questions/constructional-divergence-probe.md) (turning the external Scivetti negative into a project-run result) and `constructional-divergence-operationalization` (instrument/thresholds/frequency-matching for the divergence-probe family).
- **Identity/coherence audit (wave 9 capstone)** across the whole findings layer: no BLOCKERs; fixed stale conjecture counts, the theory link block, and two over-tight phrasings.

Run stopped at ~53 min (under the ~2h budget) per `PROTOCOL.md §A5`: the backlog of genuinely-tractable, non-blocked, non-fabricating units was exhausted — the remaining high-value steps all gate on Tom's open decisions or on the Scivetti repo becoming reachable. Continuing would have meant padding (mechanical extra conjectures) or further bloating the decision queue. Subagent tokens this run ≈ 0.65M across 9 generation + 4 coherence/audit passes.

## Next concrete action

Default is **workflow mode** (`PROTOCOL.md §A`). The single biggest unblock is external (Tom ratifies decisions, or a future environment can reach the Scivetti repo). Tractable units for the next wave, in priority order:

1. **If the Scivetti release repo is reachable** (`https://anonymous.4open.science/r/beyond-memorization-B82B` — was 403/proxied this run): mirror it into `experiments/data/` (license-check first), inspect item-level structure, confirm per-construction counts and **whether per-item human labels are released**, and upgrade [`resource/scivetti-2025-cxnli-dataset`](wiki/base/resources/scivetti-2025-cxnli-dataset.md) from `external-only`. This unblocks the four CxG anchor decisions and the divergence-probe designs at once.
2. **Develop the lexical wedge**: read the WiC / graded usage-similarity / WSD-as-classification line, then turn [`open-question/lexical-polysemy-gradience`](wiki/findings/open-questions/lexical-polysemy-gradience.md) into a conjecture + catalogue a *gradience-bearing* sense resource (verify it carries graded, not just discrete, annotations). Non-blocked; broadens beyond the grammatical wedge.
3. **Deepen a still-section-level source toward page-level** (`piantadosi-hill-2022`, `weissweiler-2023`, `lyre-2024`) — only if a finding needs the page-level numbers, and only if re-fetchable; never fabricate pagination.
4. **Do NOT** mechanically add more construction conjectures (resultative, let-alone, …) just to fill the Scivetti 8 — that is padding and adds to the decision queue. Add one only if a specific finding needs it.

Match the shape of the existing typed pages. Run `senselint.py` (0 errors) + `linkify.py` before commit.

## Blocked pending Tom

**Nine** open decisions gate promotion of contingent work. **Consolidation note:** four of them name the *same* Scivetti dataset as candidate anchor, gated on the *same* repo inspection — they can be ratified as **one bundle**.

**Scivetti-anchor bundle (one decision for Tom — "adopt Scivetti for these four pending repo inspection, or not"):**
- [`decisions/open/caused-motion-anchor`](wiki/decisions/open/caused-motion-anchor.md) — provisional default B (VerbNet/PropBank); Scivetti surfaced as Option D.
- [`decisions/open/conative-anchor`](wiki/decisions/open/conative-anchor.md) — provisional default B (Levin/VerbNet); Scivetti Option D (its verified example item is directly on Prediction 1).
- [`decisions/open/way-construction-anchor`](wiki/decisions/open/way-construction-anchor.md) — provisional default A (Goldberg seed); Scivetti Option D realizes the gestured Option C.
- [`decisions/open/comparative-correlative-anchor`](wiki/decisions/open/comparative-correlative-anchor.md) — provisional default A (Scivetti CC subset pending inspection); fallback B (Weissweiler-2022 seed).

**AANN line:**
- [`decisions/open/aann-stimulus-source`](wiki/decisions/open/aann-stimulus-source.md) — ratify Mahowald 2023 as primary AANN anchor (default), or switch.
- [`decisions/open/aann-operationalization`](wiki/decisions/open/aann-operationalization.md) — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- [`decisions/open/cxg-probing-anchor`](wiki/decisions/open/cxg-probing-anchor.md) — scope the CxG-probing-validity claim to AANN (default), acquire a CxG-native broad anchor (Scivetti is now a candidate), or split the claim.

**Operationalization / relational:**
- [`decisions/open/constructional-divergence-operationalization`](wiki/decisions/open/constructional-divergence-operationalization.md) — instrument (NLI vs forced-choice vs both) + thresholds + frequency-matching for the divergence-probe family (default: both instruments, 30pp/70%/15pp, frozen at item-commit). Governs the CC design.
- [`decisions/open/relational-anchor-shortlist`](wiki/decisions/open/relational-anchor-shortlist.md) — human dyadic-interaction anchor for the relational pilot (default: Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004 backdrop).

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md` — **"continue working" ⇒ workflow mode (§0/§A)**: plan a wave, fan out parallel subagents, run an adversarial coherence pass, integrate + verify, commit per wave, loop until any stated deadline OR until the non-blocked backlog is exhausted (§A5 — don't pad). Read `wiki/index.md` before opening pages. **Reconcile `wiki/decisions/open/` first** (nine entries; four are the Scivetti-anchor bundle). **Run `python3 tools/senselint.py` (0 errors) and `python3 tools/linkify.py` before each commit.** **The Scivetti release repo was unreachable this run** — re-test reachability early; it is the gate on the most valuable next step. Commit and merge to the default branch before stopping.
