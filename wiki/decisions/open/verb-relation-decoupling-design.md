---
id: verb-relation-decoupling-design
title: "Verb-relation decoupling probe — the value-laden gates: the verb relation inventory + registered primary clause (H1 decoupling), the troponymy-depth proxy specification (H2 DOES transfer, unlike adjectives), and the internal-contrast-only anchor"
status: open
opened: 2026-07-09
opened-by: session-198
provisional-default: "Q1-C (5-relation set {hypernymy, troponymy, synonymy, entailment, antonymy} for the across-relation decoupling arm; H1 decoupling registered PRIMARY + H2 troponymy-depth registered CO-PRIMARY; powered item-level SECONDARY descriptive-only; cause added as a 6th only if it survives frequency-matching at >=100 cues) / Q2-A (min_depth over the cue's first VERB synset as the single frozen H2 proxy, predicted sign negative, byte-analogous to the noun is_a_depth; no richer multi-proxy bet, no corpus troponymy-frame arm) / Q3 internal-contrast-only"
contingent-artifacts:
  - design/lexical-relation-recovery-verb-decoupling-v1
---

# Decision: the value-laden gates of the verb-relation decoupling probe

> **OPEN — session 198 (2026-07-09).** This decision is **not** ratified this session (surfacing and
> ratifying are separated by a session boundary; PROTOCOL §2 / CLAUDE.md rule 5). A **later** session
> ratifies via an independent adversarial-review pass (fresh reviewer with verdict authority + one
> non-Anthropic decorrelation vote), recording `resolved-by: autonomous (adversarial review)`. Tom's
> standing override outranks. **Ratification fixes the yardstick, never the result.**
>
> The s198 pre-run design critic (fresh agent) + non-Anthropic decorrelation vote are recorded in
> [`REVIEW-design-s198.md`](../../../experiments/runs/2026-07-09-verb-relation-decoupling-design/REVIEW-design-s198.md)
> as QA input to the *ratifying* reviewer — they do not ratify. The contingent design is
> [`design/lexical-relation-recovery-verb-decoupling-v1`](../../../experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md).

## Why this is owed

The design [`design/lexical-relation-recovery-verb-decoupling-v1`](../../../experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md)
operationalizes [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../../findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)
(registered s197), whose statement names **verbs as the decisive third point**: nouns show the
cue-strength–recovery decoupling and have a hierarchy; adjectives show neither; verbs *have* a hierarchy
(troponymy) but are a different POS, so a verb probe separates "has a hierarchy" from every other
noun/adjective difference. Turning the conjecture's decisive test into a runnable probe forces three
value-laden choices. Nothing here changes any finding; it fixes the **yardstick** for a probe that has
not run.

Design-time feasibility, measured this session (`nltk` WordNet 3.0 + SubTLEX-US Lg10WF band [2.0, 4.5],
excluding all 1,740 prior cue lemmas as a homograph guard;
[`feasibility.txt`](../../../experiments/runs/2026-07-09-verb-relation-decoupling-design/feasibility.txt)):
fresh in-band cue counts — **hypernymy 2,006, synonymy 1,448, troponymy 1,136, verbgroup 429,
entailment 242, antonymy 140, cause 126, alsosee 0**. Verb `min_depth()` is **non-degenerate** (0–11,
12 distinct values on the fresh troponymy pool) — so H2's depth proxy is computable, unlike for
adjectives.

## Gate Q1 — the verb relation inventory + the registered primary clause

Unlike the adjective probe (where the thin inventory made the decoupling arm near-degenerate and pushed
the antonymy-shadow clause to primary), for verbs the **decoupling (H1) is the headline** — the
conjecture's decisive test — and the inventory is adequate.

- **Q1-A — 4-relation taxonomic core {hypernymy, troponymy, synonymy, antonymy}.** Cleanest, centers the
  taxonomic pair, but drops **entailment** (a genuine verb-specific hierarchical relation the conjecture
  names) and gives only 4 rank points.
- **Q1-B — 6-relation {hypernymy, troponymy, synonymy, entailment, antonymy, cause}.** Maximal rank
  spread (matches the noun 6-point structure), but `cause` binds at the floor (126 fresh) and may drop
  below powered N after frequency-matching to a common profile, and is the least central verb relation.
- **Q1-C (provisional default) — the 5-relation set {hypernymy, troponymy, synonymy, entailment,
  antonymy}** for the across-relation decoupling arm, with **H1 (decoupling) registered PRIMARY and H2
  (troponymy-depth) registered CO-PRIMARY**, plus the item-level cue-strength→recovery arm (~600 cues) as
  a POWERED SECONDARY (the s193/s196 Q1-C discipline: descriptive/robustness-only, can never on its own
  fire H1). `cause` is added as a **sixth relation only if it survives frequency-matching at ≥100 cues**,
  decided mechanically at freeze and pre-registered either way; if it drops out the arm is 5-point and
  this is reported, not patched.

**Why value-laden:** the inventory forces a trade between a clean-but-thin 4-relation test, a
maximal-but-fragile 6-relation one, and whether a floor-binding relation (`cause`) enters conditionally.
Making H1 primary (Q1-C) is warranted here — unlike adjectives — because verbs are the POS the conjecture
pre-registered as decisive and 5 relations is an adequate rank test; but Q1-C must pre-commit that a
5-point across-relation ρ_cue is reported at its true (low) power, never dressed up, with the powered
item-level arm backing it.

## Gate Q2 — the troponymy-depth proxy specification (H2 DOES transfer here)

Unlike adjectives (where `min_depth()` is a degenerate constant 0 and H2 was uncomputable), verbs have a
non-degenerate depth structure. The question is **which** depth proxy is frozen as the H2 primary.

- **Q2-A (provisional default) — min_depth over the cue's FIRST verb synset** (byte-analogous to the noun
  `is_a_depth`, `pos="v"`), predicted sign negative, a single frozen proxy. Cleanest, byte-parallel to the
  noun H2, minimal multiple-comparison surface; makes a verb confirmation a genuine *replication* of the
  noun mechanism.
- **Q2-B — a richer depth proxy** (mean min_depth over all senses, or troponym-branching centrality). More
  faithful in principle to "taxonomic centrality," but opens multiple depth bets → multiple-comparison
  burden, and diverges from the noun H2 spec, breaking the like-for-like parallel.
- **Q2-C — reject up front: a corpus troponymy-frame ("Hearst") arm** analogous to the s193 nominal Hearst
  second arm. **Rejected** — verb troponymy has no clean lexico-syntactic frame analogous to nominal "X
  such as Y" (the s193 nominal Hearst arm *lost* even where well-motivated); a verb-troponymy corpus frame
  would be a weakly-motivated fishing surface. The structural troponymy-depth proxy is the single H2
  vehicle.

**Why value-laden:** whether the verb H2 stays a byte-parallel *replication* of the noun mechanism (Q2-A)
or becomes a new, multi-proxy bet (Q2-B) diluting the two-POS-pattern reading. The default (Q2-A) protects
the "same taxonomic mechanism, second POS" inference the conjecture is testing.

## Gate Q3 — the anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following s186 Q3 / s193 Q4 / s196 Q3
  exactly. Recovery is scored against WordNet as a **shared definitional target that cancels in the
  contrast**; the predictors (contrastive-frame G², troponymy-depth) are corpus/lexicon statistics; no
  human recovery baseline enters, so the result makes **no human-comparison claim** and no `resource`
  anchor is required (CLAUDE.md terminal state; the s186 model-vs-computational-baseline gloss-extension
  applies). Per CLAUDE.md this terminal declaration needs cross-session adversarial ratification — which a
  later session supplies. Until ratified the design carries `anchor: internal-contrast-only` provisionally,
  naming this decision in `contingent-on:`.

## Provisional defaults, together

**Q1-C** (5-relation decoupling arm; H1 primary + H2 troponymy-depth co-primary; powered item-level
secondary; conditional `cause` sixth) · **Q2-A** (single byte-parallel min_depth `pos="v"` proxy) · **Q3
internal-contrast-only**. These cohere: Q2-A keeps the verb H2 a genuine replication of the noun
mechanism, which is what the conjecture's decisive test requires, and Q1-C makes the decoupling (H1) —
the conjecture's headline — the registered primary at adequate (if still weak) power, backed by the
powered item-level arm; Q3 certifies the whole as internal-contrast.

## What ratification would unblock

Fix Q1–Q3 → freeze `prep.py` (fresh disjoint verb cues, freq-matched, outlier-capped, mechanical
`cause`-inclusion rule; byte-freeze the s193 contrastive-frame G² construction, only the cue POS
changing; freeze the troponymy-depth proxy `pos="v"`) + *k* + relation inventory + per-relation N +
ρ_cue-bands + ρ_depth-margin + calibration floor + PREREG before any model call → independent pre-run
critic + one non-Anthropic vote → run on the panel (powered N ~120–150 cues/relation, ≈ $0.35–0.60) →
post-run verifier. Design:
[`design/lexical-relation-recovery-verb-decoupling-v1`](../../../experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md).
