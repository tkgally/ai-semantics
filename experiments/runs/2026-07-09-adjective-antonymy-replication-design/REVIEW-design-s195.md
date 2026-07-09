# Pre-run DESIGN review — adjective-antonymy replication probe (s195, 2026-07-09)

Design: [`experiments/designs/adjective-antonymy-replication-v1.md`](../../designs/adjective-antonymy-replication-v1.md)
Decision (gates, OPEN): [`wiki/decisions/open/adjective-antonymy-replication-design.md`](../../../wiki/decisions/open/adjective-antonymy-replication-design.md)

Two independent decorrelated reviews, per PROTOCOL §2/§A3: an **independent fresh-agent pre-run critic
with verdict authority** (a different agent from the one that authored the design), and **one
non-Anthropic decorrelation vote** (`panel.B` = `openai/gpt-5.4-mini`, via the probe REST path,
cutoff-aware preamble) as QA input to the critic's verdict. **Design-only session: nothing frozen,
nothing run; gates ratifiable s196+.**

## Fresh-agent critic (verdict authority) — GO-WITH-CONDITIONS, no BLOCKERS, FABRICATION-CHECK PASS

**Gates:** Q1-C endorse · Q2-A endorse (clearly correct — do NOT open Q2-B) · Q3 internal-contrast-only
endorse.

**Fabrication check — ALL PASS** (every load-bearing quote/number verified against its source page):
- J&K "63% (139/219)…" / "Fully 164 (75%)…" / "extrapolation beyond J&K's data" — verbatim match.
- s186 antonymy residual +0.61–0.67 (table +0.67/+0.61/+0.66), Spearman −0.086, calibration mean
  control 𝒮 0.029 < 0.05 — all match.
- s193 H1 ρ_cue +0.14/+0.09/+0.09 3/3 — source +0.143/+0.086/+0.086, rounds correctly.
- **H2 cannot transfer — empirically confirmed:** adjective `cold.a.01` has `hypernyms() == []` and
  `min_depth() == 0` (a **degenerate constant** across adjective synsets, not "undefined"). The critic
  flagged the "undefined" wording as an accuracy nit — corrected in the design to "degenerate constant
  0," which *strengthens* the H2-doesn't-transfer claim.
- prep.py header quote verbatim; feasibility counts (antonymy 701 etc.) plausible as
  frequency-filtered subsets of the raw WordNet edge counts.

**Central residual risk the critic named:** if the calibration gate refires (likely, given s186's
0.029), the registered PRIMARY (antonymy-shadow, control-dependent) goes descriptive-only AND the
co-primary (H1) is underpowered on ≤4 relations — leaving the item-level and frame-ablation arms as the
powered evidence. → Mitigation C1 (frame-ablation mandatory), treated as mandatory not optional.

**Critic's six freeze-time conditions:** (1) make antonymy frame-ablation NON-optional; (2) name the
H1 dead-band [+0.3,+0.5] explicitly as inconclusive/null; (3) the ≤4-point asymmetry means the
across-relation H1 arm cannot on its own carry claim promotion (promotion rests on the noun
replications + this); (4) similar-to/synonymy near-duplication contingency (route to item-level arm);
(5) carry HIT@3/size-matched scoring on the antonymy-shadow primary; (6) fix "undefined" → "degenerate
constant 0".

## Non-Anthropic decorrelation vote (`panel.B`, $0.00269775) — ADOPT-C / ADOPT-A / internal-contrast

Converges with the critic on all three gates. Endorsed the H2-honesty ("right that adjectives cannot
replicate the noun IS-A proxy … honest to drop H2 rather than smuggle in a derivative proxy — good
call"). Added conditions: a **numeric calibration floor + failure protocol before freeze** (its
strongest flag — "the descriptive-only fallback is too flexible"); **predefine tie/near-tie handling**
for the 4-relation Spearman; **lock the item-level arm as purely exploratory OR specify multiplicity
control** (do not let "robustness-only" informally sway inference); and an **explicit relation-agnostic
decision rule** for the antonymy-shadow "largest vs smallest/near-zero" verdict (else narrative-fit).

## Disposition (applied this session; design-only, nothing frozen/run)

- Verdict of record: **GO-WITH-CONDITIONS** (the fresh critic holds verdict authority; the vote
  converges).
- Wording fix applied now: "undefined" → "degenerate constant 0" (a fabrication-accuracy improvement
  that strengthens the honest claim; no result touched — the probe has not run).
- Frame-ablation arm promoted from optional → **mandatory** in the design item scheme (C1).
- **Seven freeze-time conditions** bound to the design's *Freeze-time conditions* section (the critic's
  six, with the vote's numeric-calibration-floor and item-level-inference-lane specifics merged in as
  conditions 3 and 7).
- Gates remain **open**; ratification (fixing Q1–Q3) is a later session's independent adversarial review,
  never this one.

Billed: **$0.00269775** (one non-Anthropic design vote; the fresh-agent critic and design authoring are
harness-model / $0).
