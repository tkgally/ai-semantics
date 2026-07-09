# REVIEW — s199 RATIFICATION, verb-relation decoupling probe (2026-07-09)

Cross-session adversarial ratification (PROTOCOL §2) of
[`decisions/open/verb-relation-decoupling-design`](../../../wiki/decisions/open/verb-relation-decoupling-design.md)
(opened s198). An **independent fresh-agent adversarial reviewer (verdict authority)** + one **fresh
non-Anthropic decorrelation vote** (`panel.B`, via the probe REST path — QA input, not authoritative).
The lead session did not author the design; both reviewers are decorrelated from s198. Ratification
fixes the yardstick, never the result.

## Verdict: RATIFY-WITH-BINDING-CONDITIONS (Q1-C / Q2-A / Q3 internal-contrast-only)

Both reviewers converge on the provisional defaults. The fresh-agent critic (verdict authority) returned
**RATIFY-WITH-BINDING-CONDITIONS** with a clean FABRICATION SPOT-CHECK PASS and three binding conditions
(B1–B3); the non-Anthropic vote returned **ADOPT-C / ADOPT-A / internal-contrast-only** with the single
caveat folded into B1.

## FABRICATION SPOT-CHECK — PASS (fresh-agent reviewer, firsthand, WordNet 3.0 via nltk)

| structural claim | design/critic | reviewer got | verdict |
|---|---|---|---|
| verb `min_depth()` non-degenerate | 0–12, 13 distinct (synset-level) | `[0..12]`, 13 distinct | PASS |
| adjective `a`+`s` `min_depth()` degenerate | all `{0}`, 28,849 synsets | `{0}`, 28,849 | PASS |
| total verb synsets | ≈ 13,767 | 13,767 | PASS exactly |

The load-bearing structural asymmetry the whole design rests on — verbs computable, adjectives not —
holds. SubTLEX-US is not present in the reviewer's view, so the frequency-band-filtered cue counts were
not re-derived there; the s198 critic reproduced those exactly from scratch (table in
[`REVIEW-design-s198.md`](../2026-07-09-verb-relation-decoupling-design/REVIEW-design-s198.md)). The lead
session independently re-confirmed the three structural facts (verb `min_depth` 0–12/13 distinct;
adjective a+s `{0}`/28,849; verb synsets 13,767). **No fabrication anywhere.**

## Per gate (fresh-agent reviewer)

- **Q1 — ADOPT-C.** 5-relation set; H1 primary + H2 co-primary; powered item-level secondary;
  conditional `cause` sixth. All five clear powered N; a real rank test, richer than adjectives' 4.
  Q1-A drops entailment for no gain; Q1-B loads a floor-binding `cause` into the primary. Requires the
  thin-relation fallback to cover the CORE relations (antonymy 140, entailment 242 are the real floor
  risks) — condition 3 already carries this.
- **Q2 — ADOPT-A.** Verified the noun spec it mirrors (`prep.py:129`, `is_a_depth(cue) =
  wn.synsets(cue,'n')[0].min_depth()`), so `pos="v"` is a genuine byte-parallel; a verb win is a
  replication, not a new bet. Q2-B would not rescue the near-degenerate spread; Q2-C correctly rejected.
- **Q3 — ADOPT internal-contrast-only.** WordNet gold cancels on both sides of the H1/H2 contrasts; no
  human baseline imported; identical to s186/s193/s196; inherits the parent claim's terminal declaration.

## Judgement (fresh-agent reviewer)

1. **Fairness — mostly clean, one asymmetry to bind.** H1 two-sided (REAPPEARS/BREAKS with an explicit
   inconclusive gap; BREAKS a clean falsifier). H2's DEPTH-FAILS protection is the only place selection
   could creep in → B1/B2.
2. **The H2 under-power guard (the crux) — HONEST in substance, but a NUMERIC ex-ante threshold is
   REQUIRED.** The near-degeneracy (eligible-pool means hypernymy 2.469 / synonymy 2.313 / troponymy
   2.239 / entailment 2.236 / antonymy 1.564 — four within 0.23, antonymy confounded with cue-strength)
   is a real design-time structural fact, not a post-hoc rescue. But "a stated threshold" left
   qualitative is an escape hatch. The determination MUST be a single numeric depth-spread bound
   computed on the frozen freq-matched sample **before any model call** (B1), and must apply
   **symmetrically** — below the bound a DEPTH-OUT-PREDICTS is *also* flagged under-powered, not banked
   as noun-equivalent (B2). The non-Anthropic vote independently required the same numeric bound.
3. **Anchor — internal-contrast-only genuinely warranted.** No human key on the scoring path; the WordNet
   gold is a shared target that cancels in both contrasts; none owed.
4. **Modesty — softening adequate, one propagation to bind.** "Decisive → registered next/third-point
   test" is correct (verbs confound POS with hierarchy as nouns do); it must propagate to the run
   artifacts (B3): a single verb confirmation is one point in a 3-point pattern, never the established law.

## Binding conditions (recorded on the resolved decision page)

- **B1** — numeric, outcome-independent degeneracy bound frozen in PREREG on the frozen sample before any
  model call (a floor on the non-antonymy depth range and/or the 5-relation depth SD; one committed
  number).
- **B2** — symmetric application: below the bound, a DEPTH-OUT-PREDICTS is reported under-powered /
  possibly antonymy-driven, never banked as noun-equivalent.
- **B3** — propagate the "decisive → third-point" softening to the eventual result/claim titles + prose.

The seven existing freeze conditions remain in force. With B1–B3 bound, ratified for freeze s199+.

## Non-Anthropic decorrelation vote (verbatim record)

`panel.B` (`openai/gpt-5.4-mini`, $0.00276075) returned **Q1 ADOPT-C / Q2 ADOPT-A / Q3
internal-contrast-only**; fairness mostly fair (outcome set genuinely reachable if metrics frozen and
the 5-set not retuned); Q1-C best (4 too lossy, forced-6 risks post-hoc power chasing via `cause`);
Q2-A the only defensible choice if the point is replication of the noun mechanism; and — the sharpening
folded into B1 — DEPTH-FAILS-as-under-powered is honest **only if that status is frozen ex ante with a
quantitative power bound**, else it over-protects H2. Full text in [`vote-ratify.txt`](vote-ratify.txt).
