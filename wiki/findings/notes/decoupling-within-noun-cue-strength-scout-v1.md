---
type: note
id: decoupling-within-noun-cue-strength-scout-v1
title: "C4 cue-strength scout of the fresh noun sub-relations (s202): the within-noun route to a fresh forward test of the decoupling bet's C2 (tail-alignment) condition is NOT cleanly constructible — not for lack of tail material, but because the fresh inventory lacks a low-cue-strength HEAD DISALIGNER (C1). The s201 candidate head disaligner, instance-hypernymy, is measured cue-strength-RICH (frame-G²/C4 0.031, 2nd-highest of 8; robust across freq-matched + hit@3), the opposite of the predicted low-cue role. Both C2 arms need a shared C1 head disaligner; with none available fresh within nouns, the honest pivot is A6 (or a hybrid reusing coarse hypernymy as a non-fresh fixed head)"
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
    target: note/decoupling-fresh-inventory-scout-v1
  - rel: depends-on
    target: note/decoupling-fresh-inventory-scout-v1
  - rel: depends-on
    target: conjecture/decoupling-relation-inventory-shape
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-verb-decoupling-v1
  - rel: depends-on
    target: claim/lexical-relation-recovery-cue-strength-decoupling
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: concept/distributional-meaning
---

# C4 cue-strength scout: is a C2-dissociating within-noun sub-inventory pair assemblable?

> **A feasibility record (status `recorded`; a $0 corpus computation — the C4 cue-strength scout the
> s201 note named as the binding pre-step; NO model call, NO verdict-bearing output, NO human anchor).**
> [`note/decoupling-fresh-inventory-scout-v1`](decoupling-fresh-inventory-scout-v1.md) closed with a
> single recommended next unit: *measure the fresh noun sub-types' contrastive-frame C4 cue-strength, to
> decide whether a **C2-dissociating** within-noun sub-inventory pair is assemblable — if it is, freeze
> the within-noun design; if not, that null is informative and the honest pivot is A6.* This page
> discharges that measurement and returns the decision. **The measured answer: NOT cleanly assemblable —
> and for a sharper reason than the s201 note anticipated.** The blocker is not the *tail*; the fresh
> noun inventory supplies tail materials for both C2 arms. The blocker is the **head**: the fresh
> taxonomic candidate the s201 note nominated as the C1 head disaligner — **instance-hypernymy** — is
> measured **cue-strength-rich, not cue-strength-poor**, so it cannot play the low-cue/high-recovery
> head-disaligner role that coarse hypernymy played. **No route is ratified here** (the pivot is a
> route-choice fixed by the design session; surface, don't smuggle).

## What the forward test needs, and what this measures

[`conjecture/decoupling-relation-inventory-shape`](../conjectures/decoupling-relation-inventory-shape.md)
(a registered bet at re-description risk — **not** a confirmed finding) says the across-relation
cue-strength–recovery decoupling appears **iff** an inventory has **(C1)** a **head disaligner** — a
relation **low in contrastive-frame cue-strength yet high in recovery** — **and (C2)** **no aligned
tail** — its worst-recovered relations are **not** the lowest-cue-strength ones. A within-noun forward
test of C2 needs two matched sub-inventories, each carrying a C1 head disaligner, that differ only in
whether the recovery-tail sits **at** the cue-strength floor (a **C2-violating** arm, predicting the
decoupling breaks, as on verbs) or **off** it (a **C2-satisfying** arm, predicting it holds, as on the
coarse noun set). Whether such a pair is assemblable turns on the fresh sub-types' **contrastive-frame
cue-strength**, which the s201 scout left unmeasured.

This scout measures it. For each of **8 fresh noun sub-relations** — the sub-types WordNet splits
meronymy/holonymy into (member/part/substance {meronyms, holonyms}) plus the fresh **instance-hypernymy**
and **instance-hyponymy** — it builds up to 120 cues **disjoint from the 1,319 already-probed cues**
(707 s186 + 612 s193), each with its **direct** (single-step) word-form gold, in the **byte-identical**
frequency band ([2.0, 4.5] Lg10WF, RELMIN 1.5) the coarse numbers used
([`prep.py`](../../../experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/prep.py)). It then
computes each cue's contrastive-frame cue-strength on the **byte-frozen s193/s186 G² apparatus** (K=3,
FRAME_WIN=4, the s193 CONNECTIVES — imported and freeze-asserted) over the **same C4 shard set** the s193
noun and s199 verb decoupling numbers were measured on (shards 00000–00002; the deterministic
**22,329,495 sentences / 388,243,981 tokens**;
[`build_cooc_c4.py`](../../../experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/build_cooc_c4.py)).
Per-relation cue-strength = mean 𝒮(control top-3 frame candidates, gold) — the exact quantity s186/s193
call cue-strength
([`analyze.py`](../../../experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/analyze.py)).

**`attribute` is dropped** from this scout: its relata are **adjectives** (WordNet `attributes()` returns
POS `a`), incommensurable with the noun candidate pool V (the frame control's top-k are nouns), so an
adjective gold would read as a spurious cue-strength floor. Measuring it needs a separate cross-POS
control; out of scope.

## The measured table (frame-G²/C4, sorted by cue-strength; floor → ceiling)

Predicted recovery is **inherited a priori from the s193 coarse hit@3** (meronymy/holonymy ≈0.32 worst;
hypernymy ≈0.69; hyponymy ≈0.42) — a **prediction from the coarse parent, NOT measured** on the fresh
sub-types. Cue-strength is **measured**. "matched" = the same cue-strength recomputed on a
frequency-matched cue subset (matched to the sparsest relation's Lg10WF profile); "hit@3" = the
gold-size-robust co-metric (fraction of cues with ≥1 top-3 frame candidate in gold).

| fresh sub-relation | n | pred. recovery | **frame cue-strength** | matched | hit@3 | gold size |
|---|---|---|---|---|---|---|
| member_meronymy | 99 | LOW (~0.32) | **0.0034**  ← floor | 0.000 | 0.010 | 1.86 |
| member_holonymy | 119 | LOW | 0.0112 | 0.017 | 0.034 | 1.49 |
| instance_hyponymy | 120 | MID (~0.42) | 0.0167 | 0.020 | 0.042 | 5.57 |
| substance_holonymy | 49 | LOW | 0.0204 | 0.020 | 0.061 | 1.73 |
| substance_meronymy | 58 | LOW | 0.0230 | 0.027 | 0.069 | 1.34 |
| part_meronymy | 120 | LOW | 0.0250 | 0.043 | 0.058 | 2.88 |
| **instance_hypernymy** | 120 | **HIGH (~0.69)** | **0.0306**  ← 2nd highest | 0.041 | 0.092 | 1.92 |
| part_holonymy | 120 | LOW | 0.0333  ← ceiling | 0.034 | 0.100 | 1.98 |

(s193 coarse frame-G²/C4 reference, different gold construction — see the control below: synonymy 0.006 /
hypernymy 0.008 / meronymy 0.019 / holonymy 0.031 / hyponymy 0.036 / antonymy 0.149.)

## The finding: the head, not the tail, is missing

**1. The C1 head disaligner is unavailable in the fresh noun inventory.** A head disaligner must be **low
in cue-strength yet high in recovery**. The s201 note nominated **instance-hypernymy** — the fresh,
un-probed, taxonomically-central IS-A "kind" relation — as exactly that vehicle, from the C1 mechanism
("low contrastive-frame cue-strength, high recovery via taxonomic centrality"). **The measurement refutes
the cue-strength half of that prediction:** instance-hypernymy is the **2nd-highest** cue-strength of the
8 fresh sub-types (frame 0.0306; **robust** — freq-matched 0.041, hit@3 0.092 both keep it near the top),
sitting **9× above** the fresh-inventory floor (member_meronymy 0.0034), not at it. Because a head
disaligner is **low-cue by definition**, a measured **high**-cue relation **cannot** be one — *regardless
of its recovery.* And no other fresh sub-type qualifies: the two relations at the cue-strength floor
(member_meronymy 0.0034, member_holonymy 0.0112) are both **low-recovery**-predicted, so the floor is
occupied by aligned (low-cue/low-recovery) relations, not a disaligner. **The fresh noun sub-inventory
therefore patterns like adjectives — no head disaligner — not like the coarse noun set.**

**2. The tail is *not* the blocker — both C2 arms' tail materials exist.** The recovery-tail (the
low-recovery-predicted meronymy/holonymy sub-types) genuinely **spans** the cue-strength range: one
low-recovery relation, **member_meronymy**, sits **at** the floor (0.0034) — an *aligned* tail element,
the C2-**violating** ingredient (like verbs' entailment/cause) — while another, **part_holonymy**, sits
**at the ceiling** (0.0333) — an *anti-aligned* tail element, the C2-**satisfying** ingredient (like the
coarse holonymy that kept the noun tail off the floor). So the raw tail materials for **both** C2 arms
are present within nouns.

**3. …but both arms require a *shared* C1 head disaligner, and there is none.** A clean C2 dissociation
holds C1 fixed (a head disaligner present in **both** arms) and varies only the tail. With no fresh
low-cue/high-recovery relation to fix as that head, neither a C2-satisfying nor a C2-violating **arm**
can be built as specified. So a **fully-fresh within-noun forward test of C2 is not cleanly
constructible** — the constraint is **C1-vehicle availability**, not tail span or item counts.

## Gold-construction control: is coarse hypernymy's low cue-strength a closure-gold artifact?

The obvious objection to "instance-hypernymy is cue-strength-rich, unlike coarse hypernymy (0.008)":
they used **different gold**. Coarse hypernymy's gold was a **depth-4 hypernym closure** (abstract
superordinates); instance-hypernymy's is the **direct single-step kind**. So we recomputed the **same 120
s193 coarse-hypernymy cues** on the same C4 shard set + frozen apparatus under **both** golds
([`control_hypernymy_gold.py`](../../../experiments/runs/2026-07-10-fresh-subrelation-cue-strength-scout/control_hypernymy_gold.py)):

| coarse hypernymy gold | mean gold size | frame cue-strength |
|---|---|---|
| depth-4 **closure** (s193 construction) | 12.57 | **0.0083** — reproduces s193's 0.0083 exactly (pipeline sanity check) |
| **direct** depth-1 "kind" | 3.68 | **0.0056** — *lower*, not higher |

**The artifact hypothesis is refuted.** Rebuilding coarse hypernymy on the *same* direct construction
instance-hypernymy uses does **not** lift its cue-strength toward instance-hypernymy's 0.0306 — it *drops*
it (0.0083 → 0.0056). Coarse hypernymy is cue-strength-**poor under both golds**; instance-hypernymy is
cue-strength-**rich**. So the gap is **not** a direct-vs-closure gold artifact — it is a genuine relational
property: the *instance* relation's kind-terms (national_capital, city, town, author, …) sit in strongly
contrastive-framed company with their proper-noun instances (*"Paris and other capitals"*, *"scientists
such as Darwin"*), whereas ordinary hypernymy's superordinates do not, under either gold. Two consequences:
(i) the fresh-vs-coarse comparison the C1 read leans on is **not** confounded by gold construction; (ii) a
genuine refinement of the conjecture's C1 — *"taxonomic centrality supplies a low-cue head disaligner"*
holds for **ordinary** hypernymy (low-cue under both golds, 0.006–0.008) but **fails for
instance-hypernymy** (cue-rich): not every IS-A/"name-the-kind" relation is a head disaligner, only the
ones whose kind-terms keep little contrastive-frame company.

## Verdict and the honest pivot (for the design session; not ratified here)

1. **The within-noun sub-inventory route to a *fully-fresh* forward test of C2 is NOT cleanly
   constructible.** The fresh noun inventory lacks a low-cue-strength **head disaligner** (C1); the fresh
   taxonomic candidate is cue-strength-rich. This is a clean, informative feasibility **null** on the
   route the s201 note provisionally favored — exactly the outcome that note pre-named as "informative,"
   flipping the recommendation.
2. **Honest pivot → A6 (cross-linguistic).** With the within-noun route blocked on C1, the higher-freshness
   [`conjecture` A6 route](../conjectures/decoupling-relation-inventory-shape.md) becomes the favored
   forward-test path — gated, as the s201 note recorded, on its own **verified-license** wordnet +
   cue-strength corpus + a panel cross-lingual-competence pilot (nltk's OMW multilingual is absent here;
   per-language licenses are heterogeneous; s168 no-unlicensed-adoption rule binds).
3. **Residual within-noun option, flagged not favored: a *hybrid*** that reuses the already-probed
   **coarse hypernymy** as a fixed (non-fresh) C1 head disaligner across both arms, varying only a fresh
   tail (member_meronymy-type at the floor vs part_holonymy-type off it). This *is* constructible, but it
   **sacrifices C1 freshness** (coarse hypernymy is already fit-to data) and only forward-tests C2 given a
   re-used head — a weaker test than A6's fully-fresh inventory. The design session weighs it against A6.

## Honesty caps (read before citing)

- **No new measurement of model behavior.** This is a `note`: a WordNet item build + a C4 corpus
  computation. Every cue-strength number is a property of the **corpus** (a design predictor), not of any
  model; **no** recovery, verdict, or LLM-meaning quantity is measured here. It is **never** a citation
  for the decoupling, for the conjecture, or for any claim about model meaning.
- **Predicted recovery is a prediction, not a measurement.** "instance-hypernymy is high-recovery",
  "meronymy/holonymy sub-types are low-recovery" are inherited a priori from the s193 **coarse** hit@3 and
  the H2 taxonomic-centrality vehicle (itself only 2/3, single-run, between-relation, Hearst-arm-lost).
  The load-bearing disqualification of instance-hypernymy as a head disaligner rests on the **measured**
  fact that it is **high-cue-strength** — which suffices on its own, since a head disaligner is low-cue by
  definition.
- **The fresh-vs-coarse cue-strength comparison mixes gold constructions** (direct vs depth-4 closure); the
  gold-construction control above quantifies it. The **within-fresh-inventory** comparison (all 8 sub-types
  on direct gold) is apples-to-apples and is what the C1/C2 read stands on.
- **Sparse sub-types under-power the tail (member_meronymy n=99, substance_holonymy n=49, substance_meronymy
  n=58).** The floor/ceiling identities are stable across frame + freq-matched + hit@3, but a frozen design
  would re-power them.
- **The route pivot opens no decision.** Reporting feasibility and a favored next route makes no value-laden
  methodological commitment; the route choice + its gates are fixed at design freeze by a later session.
- **Within-distributional throughout.** Every quantity (cue-strength, predicted recovery) is form-internal;
  nothing here bears on reference or truth
  ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)), and the nouns-only
  [`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md)
  is untouched.
