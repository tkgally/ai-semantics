# REVIEW — s198 pre-run DESIGN review, verb-relation decoupling probe (2026-07-09)

Decorrelated pre-run review of [`design/lexical-relation-recovery-verb-decoupling-v1`](../../designs/lexical-relation-recovery-verb-decoupling-v1.md)
per PROTOCOL §A3: an **independent fresh-agent design critic (verdict authority)** + one
**non-Anthropic decorrelation vote** (`panel.B`, via the probe REST path — QA input, not authoritative).
This review is QA input to the *ratifying* reviewer (a later session); it does **not** ratify the
decision [`decisions/open/verb-relation-decoupling-design`](../../../wiki/decisions/open/verb-relation-decoupling-design.md).
**Nothing frozen, nothing run.**

## Verdict: GO-WITH-CONDITIONS (no BLOCKER; FABRICATION-CHECK PASS)

Both reviewers converge on the provisional defaults **Q1-C / Q2-A / Q3 internal-contrast-only**. The
fresh-agent critic (verdict authority) returned **GO-WITH-CONDITIONS** with a clean fabrication PASS and
one substantive catch (the near-degenerate verb depth spread, condition 1 below); the non-Anthropic vote
returned **ADOPT-C / ADOPT-A / internal-contrast-only** with two flagged blocker-risks (conditions 3–5).
Seven freeze-time conditions bind the eventual freeze (recorded on the design page's *Freeze-time
conditions* section). Ratification fixes the yardstick, never the result.

## FABRICATION-CHECK: PASS — every cited number reproduced exactly

The critic re-measured independently (its own script, WordNet 3.0 + SubTLEX-US, band Lg10WF [2.0, 4.5],
RELMIN 1.5, excluding the 1,740 prior cue lemmas from the three prior `items.json`). Every design-cited
feasibility figure reproduced **exactly**:

| relation | in-band (design / critic) | fresh (design / critic) |
|---|---|---|
| hypernymy | 2580 / **2580** | 2006 / **2006** |
| synonymy | 1874 / **1874** | 1448 / **1448** |
| troponymy | 1479 / **1479** | 1136 / **1136** |
| verbgroup | 553 / **553** | 429 / **429** |
| entailment | 320 / **320** | 242 / **242** |
| antonymy | 200 / **200** | 140 / **140** |
| cause | 173 / **173** | 126 / **126** |
| alsosee | 1 / **1** | 0 / **0** |

Prior-exclusion count **1,740** reproduced. Verb `min_depth` non-degenerate (troponymy fresh pool
0–11, 12 distinct, mean 2.24; synset-level 0–12, 13 distinct) reproduced. Adjective degeneracy confirmed
**stronger** than the conjecture claimed: `pos="a"` 18,156 synsets + satellites `a`+`s` 28,849 synsets
**all share the single min_depth value 0** — H2 genuinely uncomputable for adjectives, genuinely
computable for verbs. No fabrication anywhere.

## Per-gate

- **Q1 — ADOPT-C** (both). 5-relation {hypernymy, troponymy, synonymy, entailment, antonymy}; H1
  primary, H2 co-primary, item-level powered secondary; conditional `cause` sixth. Warranted: the
  conjecture pre-registered verbs as the decisive H1 test, and 5 relations is an adequate rank test
  (richer than adjectives' 4). Critic note: the thin-fallback rule must cover the *core* relations, not
  only `cause` — antonymy (140) and entailment (242) are the real floor risks once matched to antonymy's
  binding profile (condition 3).
- **Q2 — ADOPT-A** (both). Single `min_depth` of the cue's first verb synset, `pos="v"`, predicted
  negative. Correct given the near-degenerate depth spread — a richer proxy (Q2-B) would not rescue H2
  and would add multiple-comparison surface; byte-parallelism to the noun H2 is what makes a verb
  confirmation a genuine *replication*. Bind the under-power condition (condition 1).
- **Q3 — ADOPT internal-contrast-only** (both). Recovery scored against a shared WordNet target that
  cancels; both predictors (contrastive-frame G², troponymy-depth) are corpus/lexicon statistics; no
  human baseline. Follows s186/s193/s196 exactly. No `resource` anchor owed.

## The substantive catch (critic condition 1) — the H2 near-degenerate depth spread

The critic's primary catch, which the design as first written did **not** surface: the between-relation
mean cue depths on the frozen-eligible pools are **hypernymy 2.469, synonymy 2.313, troponymy 2.239,
entailment 2.236, antonymy 1.564** — four relations within 0.23 (differences 0.003/0.07/0.16, swamped by
sampling noise at N≈120), antonymy the lone shallow outlier. So a 5-point ρ_depth is effectively decided
by antonymy's recovery rank, and — condition 2 — **antonymy is simultaneously the shallowest-depth
relation (predicts recovers-well under H2) AND typically the highest contrastive-frame cue-strength
relation** (its frames "X versus Y" / "neither X nor Y" are literally antonym frames). So on the one
relation that carries the depth spread, ρ_depth-negative and ρ_cue-positive are **aligned**, not
orthogonal — the *reverse* of the noun case where hypernymy was low-cue-strength-but-central and thus
*disaligned* them. Consequence, bound at freeze: a `DEPTH-FAILS` outcome on verbs is **UNDER-POWERED /
uninformative**, NOT a clean fire-against of conjecture-falsifier-2; and a coincidental H2 win/loss on
verbs is **not** mechanistically equivalent to the noun H2. **H1 stands on its own** and is unaffected —
this scopes H2, it does not block the probe.

## Freeze-time conditions (bind PREREG/`prep.py` at freeze; verbatim on the design page)

1. **H2 near-degenerate-depth guard.** Compute + freeze the achieved per-relation mean depths in the
   actual frozen sample; pre-register that if the non-antonymy spread is degenerate (heavy ties / range
   below a stated threshold), H2 is reported **UNDER-POWERED/uninformative, not a clean DEPTH-FAILS
   falsifier**.
2. **Antonymy depth×cue-strength confound.** Pre-register as a stated construct caveat that on verbs the
   depth-carrying relation (antonymy) aligns ρ_depth-negative with ρ_cue-positive (reverse of the noun
   case); do not read an H2 verb win/loss as mechanistically equivalent to the noun H2.
3. **Thin-relation fallback for the CORE set (not only `cause`).** Fix the binding profile explicitly
   (antonymy's fresh profile). Any core relation dropping below powered N after frequency-matching is
   reported at achieved N and **never silently dropped or reweighted**; set a hard floor (e.g. <80) and
   pre-commit both branches (drop → 4-point arm, or keep-and-flag), decided mechanically.
4. **Exact fresh-in-band cue definition.** A cue is *fresh* iff its surface lemma ∉ the 1,740 prior cue
   lemmas (**POS-agnostic surface match**, the stricter guard the code implements, covering homographs
   like *run/fall/light*); *in-band* iff single-word, `isalpha`, Lg10WF ∈ [2.0,4.5]; gold aggregated
   across **all** verb senses; relatum single-word Lg10WF ≥ 1.5. Disclose the carried construct caveat:
   gold is all-sense while the depth proxy is **first-synset** (byte-identical to the noun run).
5. **Lock the `cause`-inclusion rule before any inspection.** ≥100 cues *after frequency-matching to the
   binding profile* (define the matched-N computation), decided mechanically at freeze, both branches
   pre-registered; `cause` never enters or exits after recovery is seen.
6. **Byte-freeze integrity.** Byte-identity applies to the G²/co-occurrence computation (frames, window,
   K, `signed_g2`) verified unchanged vs s193 `build_cooc_c4.py`; only the cue POS (→verbs) and candidate
   pool V (→single-word SubTLEX verbs) change; C4 shards = s193-frozen 00000–00002. Assert in PREREG.
7. **Close the band arithmetic + inherit the calibration gate.** Exhaustive mutually-exclusive ρ_cue
   bands (reappears ≤+0.30 / inconclusive (+0.30,+0.50) / breaks ≥+0.50) + a numeric H2 margin
   (|ρ_depth|−|ρ_cue| ≥ 0.20, negative direction), fixed before any model call. Carry the s186/s193
   calibration-gate floor (residual arm descriptive-only if mean control 𝒮 < floor; weight shifts to the
   corpus-control-independent H1/H2 rank tests). Set `ABORT_USD`; register the `predictions.md` row at
   freeze (co-registered with the s197 bet); assert per-relation 0-overlap with the 1,740 prior lemmas.

## Applied to the design this session (design-time, no gate rewrite)

Per the critic's framing concern that **"decisive" overstates the design's logic** (verbs confound POS
with hierarchy exactly as nouns do — a verb confirmation is confirmatory third-point evidence, not a
crucial experiment that *isolates* hierarchy; the clean falsifier is DECOUPLING-BREAKS), the design's
framing is softened this session: "decisive" is to be read as **"the registered next / third-point
test,"** not "identifying," and scope cap 5 is strengthened to state H2 is **strictly weaker on verbs
than on nouns** (5 rank points vs 6, a near-constant depth predictor across 4 relations, the noun
item-level depth arm already ρ≈0). The seven freeze conditions are recorded verbatim on the design's
*Freeze-time conditions* section; conditions 1–2 (the H2 under-power guard + antonymy confound) are also
folded into the design's scope caps and verdict map so the eventual freeze cannot miss them.

## Non-Anthropic decorrelation vote (verbatim record)

`panel.B` returned **ADOPT-C / ADOPT-A / internal-contrast-only** and flagged: (i) the fresh-in-band cue
definition needs an exact lemma/sense operational definition (→ condition 4); (ii) a pre-registered
thin-relation fallback is needed so the core test can't be silently reweighted, and the `cause`-inclusion
rule must be locked before inspection (→ conditions 3, 5); (iii) the "breaks" band must be isolated from
POS-shifted artifacts in G²/inventory/cue-selection, okay only if all frozen with the same pipeline
(→ condition 6). Full text in [`vote-design.txt`](vote-design.txt) ($0.0028815, `openai/gpt-5.4-mini`).

## Remaining concerns (from the critic; carried, non-blocking)

- **"Decisive" is "registered next test," not "isolating."** Verbs carry their own aspect/argument-structure
  differences; a positive is confirmatory third-point evidence. DECOUPLING-BREAKS is the clean falsifier.
- **H2 strictly weaker on verbs than nouns** (condition 1); a verb DEPTH-OUT-PREDICTS is informative, a
  DEPTH-FAILS near non-diagnostic.
- **Hypernymy gold-size confound carried** (median gold 9 vs antonymy's 1); Soundness/HIT@3 can be easier
  at large gold — hypernymy's recovery advantage is partly a gold-size artifact (inherited from s186/s193,
  mitigated by HIT@3, disclosed).
- **Frequency-matching may shift the depth means** (matches on Lg10WF, not depth); re-measure on the
  frozen sample (condition 1), do not assume from eligible-pool figures.
- **H1 both-directions reachable, not rigged**; `verbgroup` (429) correctly excluded (near-dup with
  synonymy), `alsosee` (0) correctly unusable.
