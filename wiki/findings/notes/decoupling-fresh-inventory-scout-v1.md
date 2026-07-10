---
type: note
id: decoupling-fresh-inventory-scout-v1
title: "Fresh-inventory feasibility scout for the s200 decoupling bet — raw material is abundant (incl. a fresh, un-probed candidate head disaligner, instance-hypernymy); BOTH the within-noun sub-inventory and A6 cross-linguistic routes are natural-experiment forward tests (recovery is observed for either), so the binding step is measuring the fresh sub-types' C4 cue-strength to see whether a C2-DISSOCIATING contrast is even assemblable. Within-noun is the lower-cost first move (no license, no POS confound); A6 is the higher-freshness, license-gated alternative"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: refines
    target: conjecture/decoupling-relation-inventory-shape
  - rel: depends-on
    target: conjecture/decoupling-relation-inventory-shape
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-verb-decoupling-v1
  - rel: depends-on
    target: claim/lexical-relation-recovery-cue-strength-decoupling
---

# Fresh-inventory scout: is a within-noun sub-inventory contrast constructible, and how does it compare to A6?

> **A feasibility record (status `recorded`; no model call, no corpus stream, $0).** [`NEXT.md`](../../../NEXT.md)
> named "design the s200 conjecture's fresh-inventory test" the strongest s201 empirical move, but
> flagged — twice — to **weigh constructibility of the within-noun route first**: *"does the noun
> inventory offer a sub-set that removes the off-floor tail while keeping the head disaligner? … if
> not cleanly constructible, the honest move may be a scout/feasibility note, not a full design."*
> This page discharges that instruction. Its finding, after an adversarial coherence pass corrected an
> earlier over-strong draft: the within-noun route has **abundant raw material** — including a fresh,
> **un-probed** candidate head disaligner (`instance-hypernymy`) the coarse instrument never isolated —
> and is **not** disqualified as a forward test; the honest binding step is a **C4 cue-strength
> measurement of the fresh sub-types** to learn whether a **C2-*dissociating*** sub-inventory pair is
> assemblable at all. **No design is frozen and no route is ratified here** — the route commitment is
> left to the design session (surface, don't smuggle).

## What a clean forward test of the bet demands — and a correction about "a priori"

[`conjecture/decoupling-relation-inventory-shape`](../conjectures/decoupling-relation-inventory-shape.md)
says the across-relation cue-strength–recovery decoupling appears **iff** an inventory satisfies both
**(C1)** a low-cue/high-recovery **head disaligner** and **(C2)** **no aligned tail** (its
worst-recovered relations are not the lowest-cue-strength ones). Its load-bearing confirm/falsify
clauses require a **fresh inventory chosen *before recovery is observed*** that dissociates C2 from
POS — because C1/C2 were read off three already-measured scatters, and only a forward test earns the
bet. It names two candidate routes: a **within-noun sub-inventory contrast** (same POS, no POS
confound) and the **A6 cross-linguistic** replication (a language with a different cue-strength
profile).

**The correction (relative to this note's first draft).** It is tempting to argue the within-noun
route "can't be a clean forward test because which relations end up worst-recovered is model behavior,
observed not designed." That is true — **but it is a *universal* property of relatum recovery, not a
route-specific defect**: A6 recovers its scatter by observation too. Every forward test here is a
**natural experiment** — you pre-commit the inventory's *predictor-side* profile a priori (each
relation's contrastive-frame **cue-strength**, measurable from a corpus before any model call, and its
**taxonomic-structure** proxy for "will be a head disaligner"), then **observe** recovery and check
whether the decoupling appears. That is exactly how the noun / adjective / verb runs were already done.
So "recovery is not designable" does **not** discriminate the two routes and is **not** the obstacle;
the real question is which route best **dissociates C2 from POS with a genuinely fresh inventory and
adequate material.**

## Route 1 — within-noun sub-inventory contrast

**Raw material: abundant, and richer than the coarse instrument shows.** WordNet unions three
sub-types into each coarse bucket the frozen s186/s193 instrument probed (`holonymy` =
member/part/substance holonyms; `meronymy` = member/part/substance meronyms), and carries further
un-probed noun relations (**instance-hypernymy / instance-hyponymy, attribute**). Splitting these gives
genuinely un-fit-to noun relations. Eligible-cue pools, counted **disjoint from the 1,319 already-probed
cues** (707 s186 + 612 s193;
[`enumerate_pools.py`](../../../experiments/runs/2026-07-10-decoupling-fresh-inventory-scout/enumerate_pools.py)) —
**upper bounds, no Lg10WF band and no relatum-frequency filter applied** (SubTLEX is gitignored/absent):

| fresh noun sub-relation | eligible-cue pool (upper bound) | family |
|---|---|---|
| member_holonymy | 8,582 | part/whole |
| part_holonymy | 5,043 | part/whole |
| **instance_hypernymy** | **4,497** | **taxonomic (IS-A instance)** |
| member_meronymy | 3,611 | part/whole |
| part_meronymy | 2,737 | part/whole |
| instance_hyponymy | 836 | taxonomic (IS-A instance) |
| substance_meronymy | 516 | part/whole |
| attribute | 502 | attribute |
| substance_holonymy | 432 | part/whole |

Item counts are **not** the binding constraint (even at ~120/relation after the frequency filters,
every pool clears powered N). Two facts shape what a design can do:

1. **There IS a fresh candidate head disaligner.** `instance_hypernymy` (pool 4,497 — the 3rd-largest)
   is a distinct, **un-probed, taxonomically-central IS-A relation** — precisely the profile (low
   contrastive-frame cue-strength, high recovery via taxonomic centrality) the conjecture's C1 vehicle
   predicts should be a head disaligner. It is **not** a meronymy/holonymy sub-type. Its recovery is
   **unmeasured** — but that is the point of running the probe, not a reason to assume it away. So the
   within-noun route is not confined to the already-probed coarse `hypernymy` for its C1 vehicle.
2. **The tail material clusters (but not entirely) under the already-worst-recovered pair.** ~78% of
   the pooled fresh cues (20,921 / 26,756) are meronymy/holonymy sub-types — the two **worst**-recovered
   coarse noun relations at s193 (hit@3 ≈ 0.32 each, vs hypernymy ≈ 0.69, antonymy ≈ 0.95); the
   remaining ~22% (instance-hypernymy/hyponymy + attribute) are the non-part/whole material. So there is
   plenty of plausible low-recovery tail material, plus a fresh head-disaligner candidate and a fresh
   attribute relation of unknown recovery.

**The genuine open question — is a C2-*dissociating* contrast assemblable?** To be a forward test of
the *tail* condition, the design needs two matched noun sub-inventories that differ in whether the
recovery-tail sits at the cue-strength floor — one **C2-satisfying** (like the coarse noun set:
worst-recovered relations *off* the floor) and one **C2-violating** (worst-recovered relations *at* the
floor, as verbs turned out). Whether such a pair exists **cannot be settled from item counts**: it
turns on the fresh sub-types' **contrastive-frame cue-strength**, which is **unmeasured** and requires
**re-streaming the byte-frozen C4 shards 00000–00002** (22.3M sentences) through `build_cooc_c4.py`.
Only then is it known whether any fresh low-recovery-candidate relation sits *at* the cue-strength floor
(needed to build the C2-violating arm) while another equally-low-recovery relation sits *off* it (the
C2-satisfying contrast). **That C4 measurement is the true binding pre-step**, and it is $0-to-modest
(a corpus stream, no model calls).

**Verdict (Route 1): viable as a forward test, no license needed, no POS confound — but gated on a C4
cue-strength scout of the fresh sub-types** to confirm a C2-dissociating pair is assemblable. It also
re-uses the same POS and C4 corpus family as the noun result (the conjecture explicitly blesses the
within-noun sub-inventory as an allowed fresh-inventory route, so fresh *relations* on the same
corpus/POS is in-scope), which is a lower-freshness setting than A6.

## Route 2 — A6 cross-linguistic replication

**Maximal freshness.** A different language's noun relation inventory is genuinely fresh (new relations,
new corpus, new cue-strength profile), which is the strongest guard against a same-corpus artifact, and
POS is not confounded (still nouns). Like Route 1 it is a natural experiment (cue-strength a priori,
recovery observed), so it carries **no** a-priori-recovery advantage over the within-noun route — its
edge is purely **freshness/independence of corpus**.

**Obstacle — resources need a verified license, and the in-repo path is not ready.** A6 needs
**(a)** a license-clear WordNet-like relation inventory in the target language, **(b)** a license-clear
corpus in that language for the contrastive-frame cue-strength control, and **(c)** an instrument port
plus a **panel cross-lingual-competence pilot** (the models' relatum-production skill in the target
language is an untested assumption). This session confirmed firsthand that **nltk's multilingual Open
Multilingual WordNet is not present here** (`wn.langs()` → `['eng']` only; `omw-2.0` un-downloaded), and
OMW's per-language wordnets carry **heterogeneous licenses** — so adoption is barred until a dedicated
scout verifies terms firsthand (the standing s168 rule: *no corpus/dataset adoption without a verified
license*).

**Verdict (Route 2): the higher-freshness route, but a heavier design-precursor — a license +
feasibility + cross-lingual-competence scout must land first.** Not runnable this session or next
without that scout.

> **→ The recommended C4 cue-strength scout RAN s202**
> ([`note/decoupling-within-noun-cue-strength-scout-v1`](decoupling-within-noun-cue-strength-scout-v1.md)).
> Its measured answer **flips recommendation 2**: a C2-dissociating within-noun pair is **NOT cleanly
> assemblable**, and the reason corrects this note's own framing — the blocker is not the tail (both C2
> arms' tail elements exist) but the **head**: instance-hypernymy, nominated below as the fresh C1 head
> disaligner, is measured **cue-strength-RICH** (2nd-highest of 8 fresh sub-types), so it cannot be the
> low-cue head both arms need. **Honest pivot → A6.** Read that note's verdict, not the "provisionally
> favored: within-noun" line below, as the current route standing.

## Provisional recommendation (for the design session; not ratified here)

1. **Both routes are legitimate natural-experiment forward tests** of C1∧C2; neither is disqualified by
   "recovery is observed" (that is universal). The choice is freshness (favors A6) vs cost / no-license /
   no-POS-confound / in-repo instrument (favors within-noun).
2. **Provisionally favored as the lower-cost first move: the within-noun route** — but its next concrete
   unit is **not** a full frozen design; it is a **$0-to-modest C4 cue-strength scout** of the fresh
   sub-types (member/part/substance holonyms & meronyms, instance-hypernymy/hyponymy, attribute) to
   decide whether a **C2-dissociating** sub-inventory pair is assemblable. If it is, freeze the design
   (fresh head-disaligner candidate = instance-hypernymy; matched C2-satisfying vs C2-violating tails);
   if it is not, that null is itself informative and the honest pivot is A6.
3. **A6 remains the higher-freshness alternative**, gated on its own license + cross-lingual-competence
   scout; worth opening in parallel if the within-noun C4 scout returns no assemblable dissociating pair.
4. The conjecture stands unchanged as a **registered bet at re-description risk**; nothing here confirms
   or weakens it, and the nouns-only
   [`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md)
   is untouched.

## Honesty caps (read before citing)

- **No new measurement of meaning.** This is a `note`: a WordNet enumeration ($0) plus a design
  analysis. It measures **no** recovery and asserts **no** empirical claim about model behavior; it is
  never a citation for the decoupling itself. Every model-behavior number here (s193 recovery, cue
  strengths) is a *citation of the prior result* used as design background.
- **The pool counts are upper bounds** — no Lg10WF band, no RELMIN relatum filter, no C4 cue-strength.
  They establish that item counts are *not* the constraint and that a fresh head-disaligner candidate
  exists, **not** that any specific sub-inventory is powered or that a dissociating pair exists.
- **Whether a C2-dissociating within-noun pair is assemblable is UNKNOWN** until the fresh sub-types'
  C4 cue-strength is measured; this note does not settle it, and "instance-hypernymy is a head
  disaligner" is a *prediction from the C1 vehicle* (H2 taxonomic centrality — itself only 2/3,
  single-run, between-relation, Hearst-arm-lost at s193), not a measured fact.
- **The route preference is provisional and opens no decision.** Reporting feasibility and a favored
  first move makes no value-laden methodological commitment; the route choice and its gates are fixed at
  design freeze by a later session.
- **Within-distributional throughout.** Every quantity named (cue-strength, taxonomic depth, recovery)
  is form-internal; nothing here bears on reference or truth
  ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)).
