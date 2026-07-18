# Cross-session promotion review — DAIS verb-bias correspondence (s250)

Fresh-agent reviewer (general-purpose subagent, VERDICT AUTHORITY, independent of the s248/s250 runs;
no paid calls) + one non-Anthropic decorrelation vote (`gpt-5.4-mini`, QA input). Both reviewed the
twice-observed (s248 v1 + s250 rep2) Arm-A verb-bias correspondence and whether it earns a scoped
`claim`. **Both convergent: PROMOTE-WITH-CONDITIONS.**

## Non-Anthropic vote (`gpt-5.4-mini`, `VOTE-promote-s250.json`, $0.002174) — PROMOTE-WITH-CONDITIONS

- **SCOPE:** narrow; drop "tracks the human verb-bias magnitude" → "replicated positive per-verb
  association within the alternating class, on this isolated-pair probe"; drop "magnitude" unless only
  rank/monotone agreement is meant; keep "direction/correspondence", say "not a competence or
  causal-learning claim."
- **CONTAMINATION:** FIX — promotable only as a contamination-vulnerable surface correspondence; the
  memorizability caveat necessary but not sufficient; do not phrase as latent grammatical knowledge or
  generalized dative competence. "Result" too weak given 2/2 replication, but stay conditional/observational.
- **DISTINCTNESS:** OK, with a warning: do not bundle with the givenness claim under any "LLMs get the
  dative" umbrella; keep the anchor explicit (DAIS effect-size correlation on isolated pairs vs
  discourse-context givenness direction on byte-identical items).

## Fresh-agent reviewer (verdict authority) — PROMOTE-WITH-CONDITIONS

Recomputed the evidence from both `analysis.json` files firsthand. Confirmed VERB-BIAS-REPLICATES 3/3 on
all conjuncts, `all_three` true per model (the pre-run critic's cross-model gate-split worry does not
bite). Two adversarial findings the reviewer stressed:

1. **The rep2 point estimates drifted systematically UP** (all three above their v1 point; R3 passes at
   the top edge of v1's CI — gpt +0.7007 vs v1 upper +0.7020). A legitimate consistent-magnitude pass,
   but **not a centered replication** — the correspondence if anything strengthened on fresh items, so any
   fixed-point-ρ magnitude claim is unsupported; only "moderate positive, stable-to-slightly-stronger."
2. **The instrument is filler-sensitive on its sibling arm** — the Arm-B definiteness/length band FLIPPED
   (s248 LENGTH-ONLY → rep2 TRACKS), so demonstrated filler-instability must bound even the arm that
   replicated.

The reviewer judged REFUSE over-strict (the B2 alternating-only control clears 3/3 both runs and the
partial ρ | class+freq is moderate-positive 3/3, jointly ruling out the Levin-class-split confound; what
remains — verb-identity memorization — is handled by *scoping*, per the CLAUDE.md reading-bearing-result
pattern), and PROMOTE-without-conditions unlicensed (the "tracks the human verb-bias magnitude" phrasing
over-reaches; ρ is a *rank* correspondence).

**The 7 binding conditions (all applied in [`claim/dative-verb-bias-graded-correspondence`](../../../wiki/findings/claims/dative-verb-bias-graded-correspondence.md)):**

1. Soften force magnitude → **ordering/correspondence**; no fixed point ρ as the claimed quantity — state
   the range (matched ~+0.61–0.82) + note the rep2 upward drift; replace every "tracks the … magnitude".
2. State exactly what the controls license: alternating-only 3/3 both runs **and** partial ρ | class+freq
   3/3 ⇒ a graded per-verb correspondence *within* the alternating class, not a subcategorization artifact
   — the promotable spine.
3. Contamination vulnerability **in the claim as binding**, not a footnote: DAIS public since 2020;
   per-verb bias is what Hawkins et al. (2020) showed LMs partly capture and is verb-identity-memorizable
   (disjoint *sentences* do not neutralize it — the 200 verbs are the same units) ⇒ replication raises
   confidence in the **correspondence's stability, NOT competence beyond memorized lexical bias**; note it
   is partly a **reproduction** of the DAIS paper's own result via an independent logprob-free indicator.
4. Per-model spread stated, no pooled scalar (gpt persistent weak leg; gemini strongest).
5. Cite the Arm-B band instability as an explicit bound; claim scoped to the verb-bias arm ONLY; must NOT
   ride on / cite / import the rep2 TRACKS-HUMAN-SURFACE band; the definiteness/length dissociation stays
   a `proposed` result.
6. Distinctness fence (a dedicated section, mirroring the givenness claim's "does NOT say"): different
   instrument / construct / anchor / rigor profile; must not re-anchor or restate the givenness claim;
   state explicitly that neither claim alone nor both conjoined licenses "LLMs understand the dative
   alternation."
7. Claim created `supported` (support earned by this review); `result/…-v1` and `…-rep2` stay `proposed`
   with a dated note; `anchor: human-anchored` → `resource/dais-dative-ratings`, scoped to the verb-bias
   gradient. Id `dative-verb-bias-graded-correspondence` (distinct namespace from the givenness claim).

**Reconciliation:** the two gates converge on PROMOTE-WITH-CONDITIONS and on every load-bearing
condition (soften to correspondence/ordering; contamination binding; distinctness; scope to the verb-bias
arm). The reviewer's authority is taken; the vote's decisive concerns are fully honored (they are a subset
of the reviewer's conditions). **Combined verdict: PROMOTE-WITH-CONDITIONS.**
