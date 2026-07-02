# predictions.md — the registered-bet ledger

**What this is.** One scoreboard for every prediction the project has registered — conjecture
confirmation/falsification criteria, essay revision triggers, theory-page predicts/forbids —
with its current status. The project already registers bets and honors outcomes; this page
makes the calibration record *visible in one place* (adopted 2026-07-02, program item B5,
[`decisions/resolved/program-2026-07-adoption`](decisions/resolved/program-2026-07-adoption.md)).

**Status vocabulary.** `open` (registered, not yet tested) · `fired-for` (evidence landed on
the bet's side) · `fired-against` (the bet lost; the page records the loss) · `discharged`
(the trigger/criterion was consumed — e.g. a trigger fired and the revision was made) ·
`retired` (withdrawn for stated reasons other than a test).

**Maintenance (PROTOCOL §3).** Registering a bet adds a row *in the same session*; any firing,
discharge, or retirement updates the row in the session that lands the evidence. Every row
must be verifiable against its source page — **no row is ever added from memory, and none is
retro-fitted**. Rows are never deleted; outcomes accumulate.

> **Back-fill status: partial.** Seeded 2026-07-02 with rows verified against their pages that
> session. The full historical sweep (all conjecture criteria, all essay triggers, all theory
> predicts/forbids across ~49 essays, 18 conjectures, 5 theory pages) is **owed** as
> consolidation work (program B5); until it lands, absence of a row means *not yet collected*,
> not *no bet*.

## Ledger

| Bet (compressed; the page is authoritative) | Registered in | Status | Outcome / where recorded |
|---|---|---|---|
| The observed order-invariance of relational/coined-convention behavior persists (the deflationary relational bet) | [`conjecture/commutative-convention`](findings/conjectures/commutative-convention.md) (2026-05-31) | **fired-against** | Falsified by the conjecture's own clause; bet retired, the positive promoted — recorded in-page (status `retired`). |
| Accommodation gates on the *strength* of a contradicting cue (graded, not on/off) | [`conjecture/presupposition-environment-gated-both-directions`](findings/conjectures/presupposition-environment-gated-both-directions.md) | **fired-for** | s164 [`result/accommodation-cue-strength-v1`](findings/results/accommodation-cue-strength-v1.md): GRADED-GATE (3/3). The s166 commitment-framing PARTIAL is deliberately **not counted** (poles elicitation-designed to separate) — the non-counting note is in-page. |
| Presupposition's "shadow-saturated" placement survives a matched distributional control (surface-cue doppelgängers) | [`essay/shadow-depth-cross-cuts-grain`](findings/essays/shadow-depth-cross-cuts-grain.md) trigger 1 (2026-07-02) | **open** | The deciding control is program item A1a — unrun; the placement is explicitly a bet until it runs. |
| Antonymy's "shadow-saturated" placement survives a contrastive-frame control | same essay, trigger 1 (symmetric clause); operationalized by [`conjecture/lexical-relation-shadow-saturation`](findings/conjectures/lexical-relation-shadow-saturation.md) | **open** | Program item A1b (internal-contrast form runnable now). |
| The presupposition signatures stay environment-*gated* (projection frame-sensitive; accommodation context-sensitive) | same essay, trigger 2; [`essay/presupposition-environment-gated`](findings/essays/presupposition-environment-gated.md) | **open** | An environment-invariant re-run retracts the environment-gated reading and moves the placement. |
| The shadow-beaters (CC covariation; lexical sense gradience) replicate, and their controls hold | same essay, trigger 3 | **open** | **CC-covariation half consolidated s168:** replicated across 3 controlled runs (v1/v2/v3), matched controls held → promoted to [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md) (directional/ordering, `supported`). Bet stays **open**: the lexical-sense-gradience half is not yet powered-replicated, and the CC magnitude+interval still awaits the program A2a powered re-run. A failed replication weakens the "each pole has a beater" structure. |

## How to add a row

One row per *bet*, not per page: compress the criterion to a sentence, link the registering
page (which stays authoritative), date it, and keep the outcome column concrete (verdict +
where recorded). If a page registers several genuinely distinct bets, they get separate rows.
