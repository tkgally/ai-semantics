---
type: note
id: genitive-alternation-animacy-promotion-refusal-v1
title: "Promotion review of the genitive-alternation animacy line — REFUSE (records a refusal, not a claim): the animate→s-genitive DIRECTION survived its load-bearing shadow control (the nonce firewall, 3/3), but the line is a SINGLE run and the §3 bar requires REPLICATED ∧ survived-controls — conjunctive; the honest successor is one fresh-item replication, exactly as the dative earned its claim from v1+v2"
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: recorded
anchor: human-anchored
contingent-on: []
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: depends-on
    target: result/genitive-alternation-animacy-v1
  - rel: depends-on
    target: conjecture/genitive-alternation-animacy
  - rel: depends-on
    target: claim/dative-information-structure-givenness
  - rel: anchors
    target: resource/genitive-animacy-human-anchor
---

# Promotion review — genitive-alternation animacy line — **REFUSE**

> **Verdict: REFUSE (2026-07-13, s219).** Cross-session, independent, adversarial claims-promotion
> review ([`PROTOCOL.md §3`](../../../PROTOCOL.md)) of whether the animate→s-genitive result
> ([`result/genitive-alternation-animacy-v1`](../results/genitive-alternation-animacy-v1.md),
> `status: proposed`, s218 — PANEL CONFIRM 3/3, survives the nonce firewall 3/3) should be promoted
> to a standing `claim`. The fresh reviewer produced none of the underlying work. **The decision is
> to NOT promote — not yet.** The animacy *direction* is real, human-aligned, and survived the
> load-bearing shadow control; what is missing is the **replication** half of the §3 bar. This note
> **records the refusal** and names the single cheap probe that would earn promotion.
>
> **This note carries NO new measurement.** It is a $0.0015 promotion-review record (the only spend
> is one non-Anthropic decorrelation vote). Per the `note` discipline
> ([`CLAUDE.md`](../../../CLAUDE.md) §Page types), it must **never** be cited as support for any
> claim; it neither strengthens nor weakens the underlying result, which stands exactly as written
> (`proposed`).
>
> `anchor: human-anchored` — inherited from the line: the result's direction leg is a genuine
> human-comparison against the Dubois et al. (2023) native-speaker sign fact
> ([`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md)).
> This note makes no *new* human comparison; it records a governance decision about the existing one.

## The bar

PROTOCOL §3 promotes a result line to a standing `claim` only when it has **(1) REPLICATED** (fresh
items or a genuine second run) **AND (2) SURVIVED ITS CONTROLS** — the two conjuncts are joined by
*and*, not *or*; the output is a `claim` citing results/magnitudes/anchors, **or a written refusal**.
A written refusal is a first-class outcome: the review does not promote to look productive, and does
not refuse reflexively. Promotion would fix the *yardstick*, never the result.

## What survived (this is real, and stays a `proposed` reading)

The **controls** half is genuinely met — and this is the strength of the line, not a formality:

- **The animacy direction is human-aligned, 3/3.** Every panel model rates the s-genitive more
  natural for an animate possessor than an inanimate one (*the judge's decision* over *the decision
  of the judge*), possessor length + final-sibilancy + definiteness held fixed by construction —
  the Dubois et al. (2023) native-speaker direction. Typical-frame shift **+0.134 / +0.181 / +0.141**
  (claude / gemini / gpt), all bootstrap CI-LB > 0.
- **It survived the load-bearing shadow control (the nonce firewall), 3/3.** On rare/nonce
  possessors — where the model has *no per-lemma corpus genitive statistic* to read off, animacy is
  conveyed only by a gloss, and nonce string-forms are balanced so orthography cannot telegraph
  animacy — the shift **persists**: **+0.109 / +0.205 / +0.055**, all CI-LB > 0. A no-animacy reader
  that had only learned "which possessor lemma takes 's more often" scores **zero** here by
  construction. So the effect is not merely a distributional shadow of the possessor's marginal
  s-genitive propensity; the panel generalizes from the animacy *category*.

An independent post-run verifier **REPRODUCED-WITH-NOTES** every headline statistic (0 material
discrepancies). So the "survives its controls" half of the §3 bar is cleanly met — as *corroboration*
(the nonce arm is a within-model shortcut control), correctly fenced on the result page (R5) as
risk-reducing, not a proof the distributional shadow is causally defeated.

## What is missing (why this is a reading, not yet a claim)

The line fails the §3 *replicated* half **outright**, and that is dispositive:

1. **It is a single run.** There is no fresh-item replication. §3's two conjuncts require *both*
   replicated *and* controls-survived; one met and one absent ⇒ the bar is not cleared. This is not
   an adversarial stretch — it is the **result page's own stated stopping point**: it files itself as
   "a careful single-run reading" whose natural successor is "a cross-session promotion review …
   *once this replicates on fresh items*; not promoted from a single run."
2. **The precedent threshold is hard, and uniform.** Every promoted claim in this project rested on
   **≥2 runs**. The sibling dative alternation
   ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md))
   was promoted **direction-only** only after a **replicated pair** (v1 + v2, disjoint items), with
   the *magnitude* deferred to a later powered re-run; the comparative-correlative likewise. Scoping
   a claim trades away **magnitude**, never **replication** — replication is the non-negotiable first
   conjunct and cannot be scoped around. So **PROMOTE-SCOPED from a single run is not defensible**:
   promoting it scoped would set the precedent that surviving controls *once* substitutes for
   replication — precisely the erosion §3 exists to prevent, and a break from every prior promotion.

Add the honest fences the result page already carries, each of which a future claim would have to
state verbatim and none of which a promotion would erase:

- **Covariate vacuity.** The frozen UD-EWT possessor-lemma marginal-propensity covariate has
  essentially no predictive validity (R² 0.002 / 0.032 / 0.038; slope negative for gpt), so the
  covariate-adjusted-intercept leg of the pre-registered B3 rule is **near-vacuous** and is **not**
  independent corroboration — CONFIRM rests entirely on the nonce arm.
- **gpt is the weak firewall leg.** Nonce mean **+0.055**, only 16/24 frames positive, one-sided
  sign-test **p = 0.076** — it *clears* the CI-LB rule but **marginally**, and must be displayed, not
  averaged into a "3/3 panel tracks animacy" scalar (the [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)
  discipline; the nonce-arm effect spans ~4×).
- **The graded ramp is only weakly supported.** Monotone animate > collective > inanimate passes
  3/3 but **nominally**: collective patterns *with* inanimate (~0.005–0.027 above it), not midway, so
  the panel draws a **sharp animate/non-animate binary**, not the Zaenen five-level scale. A claim
  must state the binary, not a smooth scale.
- **Direction-only anchor.** No per-item human gradient, no human-level competence claim.

## The decorrelation vote (convergent — recorded)

The non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.001507,
[`VOTE-promotion-s219.json`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy/VOTE-promotion-s219.json))
returned **REFUSE**, decisive reason verbatim: *"Single run is the blocker. A strong shadow control
does not substitute for replication; it only says the one run survived a control … PROMOTE-SCOPED is
not defensible here because the dative analogy still had v1+v2; this genitive result does not."* Its
cheapest-flip answer matched the fresh review's independently: *"one fresh-item replication run with
the same pre-registered firewall/control logic, showing the same directional animacy shift and
CI-LB > 0."* **Convergence here is signal, not merely comfort** — a fresh Anthropic reviewer and a
non-Anthropic model reached REFUSE on the same specific gap (replication absent; controls passed),
from the same verified page. Verdict authority rests with the fresh review; the vote is recorded as
corroboration.

## The exact strengthening path that WOULD earn promotion

This is a "not yet," with a named probe — the A2a powered-replication pattern that discharged the
dative's and CC's single-run flags:

- **One fresh-item replication run** of the **already-frozen** instrument on a **disjoint** frame set
  (fresh typical + fresh nonce possessors, same certified length / sibilancy / definiteness matching,
  verdict map frozen before any call), run as a NEW disjoint run dir — **never** a touch of the s218
  frozen dir. Target the known weak point: give the **gpt firewall leg** enough nonce frames to power
  its paired contrast (gpt is the member most likely to flicker, exactly the dative's
  gpt-at-founding-N pattern). Pre-flight ~$1.2 (~900 calls). If the animate→s-genitive direction and
  the nonce-arm survival both replicate, a **direction-only scoped `claim`** becomes earnable —
  mirroring the dative's v1+v2 promotion, with the covariate-vacuity + gpt-weak-leg + binary-not-ramp
  fences carried forward verbatim.

Until then the line remains a `proposed` result at `human-anchored` (direction-only) strength, and it
enters the shadow-depth table as a **result-cited, not-yet-promoted** beater row (see
[`theory/shadow-depth-table-v3`](../theory/shadow-depth-table-v3.md)), explicitly distinguished from
the four promoted-claim beaters.

## Status

`status: recorded`. **REFUSE** — the genitive-alternation animacy line is **not** promoted to a
standing claim this session; the block is **single-run**, not a controls failure (the controls
passed). The underlying result is unchanged (`proposed`). `contingent-on: []`. This note carries **no
new measurement** and **must not be cited as support for any claim**.
