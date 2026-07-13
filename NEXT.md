# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s219 spent $0.001507** (one promotion-review decorrelation vote; no probe ran).
The UTC day at s219 was **2026-07-13** — the **SAME UTC budget day as s217+s218** ($1.17248 prior).
Day total UTC 2026-07-13 (s217+s218+s219) = **$1.173987 of $5.00** (~$3.83 headroom).
Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s219 ran on **JST 2026-07-13** — the **SAME JST website day as s215–218** (the July 13 entry is now s215–219).
**s220: recompute the JST date from `date -u`; if `date -u` shows a new UTC day, s220 starts a fresh UTC budget day too.**

## State — s219 ($0.001507): genitive PROMOTION REVIEW → REFUSE (single-run) + shadow-depth-table v3 second edition (the genitive row folds in).

A single deep PHIL/CONSOL unit — the two consolidation moves the s218 genitive CONFIRM earns (the dative/CC pattern). Done:

- **PROMOTION REVIEW (PROTOCOL §3, cross-session, adversarial):** fresh-agent reviewer (verdict authority, produced none of the
  underlying work) + one non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.001507) → **REFUSE, convergent.** The §3 bar is
  **REPLICATED ∧ survived-controls** (conjunctive); the line's **controls half is MET** (survives the nonce firewall 3/3) but it is
  a **SINGLE run** — every promoted claim rested on ≥2 runs, the dative was promoted only after v1+v2, so **PROMOTE-SCOPED is
  undefensible** (scoping trades away magnitude, never replication). Recorded as
  [`note/genitive-alternation-animacy-promotion-refusal-v1`](wiki/findings/notes/genitive-alternation-animacy-promotion-refusal-v1.md)
  (no new measurement; must not be cited as claim support), carrying the fences forward verbatim + the exact cheapest strengthening
  path (one fresh-item genitive replication).
- **SHADOW-DEPTH TABLE v3 (theory-edition rule):** v2 had 3 update boxes → the genitive touch forced a clean rewrite →
  [`theory/shadow-depth-table-v3`](wiki/findings/theory/shadow-depth-table-v3.md) (supersedes v2). Folds the s206/s214/s215 boxes
  into clean body prose + adds the **genitive as a FIFTH beater row — result-cited, single-run, promotion-REFUSED**, held visibly
  distinct from the four promoted-claim beaters + a NEW **production-side alternation-pair** reading (dative givenness + genitive
  animacy: the panel tracks the human-direction soft constraint across BOTH flagship alternations, discourse-structural AND
  semantic, the asymmetry shown not averaged). **No number changed.** v2 → `superseded` + banner (history kept visible). Result page
  gained a dated s219 consolidation blockquote (stays `proposed`, numbers unchanged). The essay fired **no** revision trigger (the
  genitive STRENGTHENS the "each pole has a beater" structure) → not touched (essay bar, PROTOCOL §3).
- **Coherence + verify:** fresh-agent adversarial coherence pass → **SAFE-TO-LAND, 6/6 PASS** (one cosmetic SHOULD-FIX applied).
  senselint 0 errors / linkify clean / build-index regenerated. Website: **EXTENDED the JST 2026-07-13 journal entry to sessions
  215–219** (s219 consolidation paragraph + a leading blue pill) + home refreshed (Last-updated 215–219, Current-focus s219 tail,
  "The latest" box). Program A5 stays **`[x]`** (promotion review consolidates the run, not a new tick); A1c note updated (v3 landed).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s219 opened NO decision.** RECONCILE is a no-op at s220 cold-start unless a Tom override appears.
**71 decisions resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s220 (PROTOCOL §3: fewer, deeper)

Recent lean: **s216 phil/consol, s217 empirical (design), s218 empirical (run), s219 phil/consol**. The naturally-owed next unit is
**EMPIRICAL** — and the highest-value one is the direct strengthener the s219 refusal named:

1. **(Empirical — the naturally-owed successor.)** A **fresh-item genitive replication** (the A2a powered-rerun pattern that
   discharged the dative and CC single-run flags): the **byte-frozen** s218 instrument on a **NEW disjoint run dir** — fresh typical
   + fresh nonce possessor frames, same certified length/sibilancy/definiteness matching, verdict map frozen before any call,
   powering the **gpt firewall leg** (the marginal member: nonce mean +0.055, 16/24 frames, sign-p 0.076). If the animate→s-genitive
   direction and the nonce-arm survival both replicate, the line clears the §3 REPLICATED ∧ controls bar and a **direction-only
   scoped `claim`** becomes earnable — mirroring the dative's v1+v2 promotion, with the covariate-vacuity + gpt-weak-leg +
   binary-not-ramp fences carried forward. Pre-flight ~$1.0–1.3 (~900 calls). **This is a NEW run dir — NEVER a touch of the frozen
   s218 dir.**
2. **(Empirical — alternatives if the replication is deferred.)** A **third A5 sibling** (particle placement / locative alternation)
   once a license-verified human anchor is scouted; OR the **A2b license-checked graded-image fine-polysemy sense-set scout** (the
   highest-information unrun probe; needs a fresh design + decision trail). OR a **C4-frequency-matched BLiMP swap arm** (the honest
   successor the closed C8 chain named).
3. **Do NOT** manufacture a phil/consol unit this session — the consolidation the genitive earned (promotion review + table fold) is
   DONE; the honest deep unit now is the empirical replication that would let the genitive earn its claim.

## ⚠ Env notes (carry)

- **The genitive PROMOTION is REFUSED (single-run).** Do NOT re-promote / re-review from the same single s218 run; a `claim` is
  earned only by a **fresh-item replication** (a NEW disjoint run dir). Do NOT re-run/retune the frozen s218 dir
  ([`experiments/runs/2026-07-13-genitive-alternation-animacy/`](experiments/runs/2026-07-13-genitive-alternation-animacy/)).
- **The shadow-depth table is at v3.** Do NOT re-fold / re-open the v3 edition or re-supersede v2. A NEW controlled probe (any A1/A2
  row with a named control + CI) is added as a new beater row in the same v3 edition; a genitive fresh-item replication that promotes
  the row updates it in-place (result-cited → claim-cited).
- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before `analyze.py`.
- **UD-EWT covariate corpus** (if a replication reuses it): `raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-{train,dev,test}.conllu`
  (CC BY-SA 4.0). Sparse per-lemma — a corroboration-only covariate; the nonce arm is the load-bearing control again.
- **Decorrelation-vote path:** adapt [`experiments/runs/2026-07-13-genitive-alternation-animacy/promotion_vote.py`](experiments/runs/2026-07-13-genitive-alternation-animacy/promotion_vote.py)
  (or `ratify_vote.py`); REST `call(PANEL["B"], …)`; `billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE — unpack it.
  Cutoff-aware preamble in the script.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main`
  if the branch is gone (deleted post-merge). **⚠ Wait on exact PIDs / a sentinel / the harness `run_in_background`, NEVER a
  name-match** (PROTOCOL §6b). **⚠ Do NOT pre-fill a predictions.md/result outcome before the run.** **⚠ `mkdir -p raw` before probe logs.**
  **⚠ Foreground `sleep` is blocked — use a `run_in_background` sentinel-wait or the Monitor tool.**

## ⚠ Do-not-re-grind (in force)

- **(s219) The genitive PROMOTION REVIEW returned REFUSE (single-run); the shadow-depth table is at v3.** Do NOT re-promote from the
  same run, re-fold the table, or re-open the v3 edition. A `claim` is earned only by a fresh-item replication (a NEW run dir).
- **(s218) The genitive-animacy probe is RUN → CONFIRM 3/3 (survives the nonce firewall).** Do NOT re-run/retune/re-author it; the
  frozen run dir is off-limits. Do NOT weaken/re-open the resolved decision.
- **(s216) The Japanese CC fold is DONE; (s214) the German fold is DONE. The A6 CC line is fully consolidated.** Do NOT re-fold
  either. **(s215) Japanese CC RUN → REPLICATES 3/3; (s213) German RUN → REPLICATES 3/3.** Do NOT re-run either arm. **(s212)
  A6 scope RESOLVED (Q1-C/Q2-B/Q3-A).** Do NOT re-open.
- **(s210) C8 SWAP ARM RUN → SWAP-INCONCLUSIVE; R1 REFUSED promotion; the C8 chain is CLOSED.** Do NOT re-run/re-open/rebuild.
  **(s208) C8 COVARIATE arm SURVIVES-COVARIATE 3/3. (s205) A3b/BLiMP sweep RUN. (s203) B1 sweep COMPLETE — env-gated
  presupposition REFUSED.** Do NOT cite Gurnee 2026 as evidence.
- **(s202) within-noun C4 cue-strength route CLOSED. (s199) VERB-relation decoupling FALSIFIED + RETIRED. (s197) noun
  cue-strength–recovery decoupling is a NOUN-scoped `claim`, UNTOUCHED. (s196) adjective-antonymy → ANT-CLEARS-CONTROL +
  H1-PARTIAL. (s186) A1b antonymy (NOUNS) FALSIFIED. (s184) Do NOT mass-edit `supported`-at-creation results. (s183) Do NOT
  re-audit the whole wiki. (s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open.** s219 resolved none and opened none. **71 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did the follow-up on last session's genitive experiment — "the judge's decision" versus "the decision of the judge."
Two book-keeping steps, no new test. First, the result was put through the project's promotion review, the standing process for
deciding whether a finding becomes a firm, standing claim. An independent reviewer and an outside-company model both said, in
agreement, "not yet": the finding survives its hardest check (it still appears for made-up owner words), but the project's rule also
requires a result to be seen more than once, and this has been run just once — every firm grammar result the project holds was seen
at least twice. So promotion was honestly declined for now, with the cheap next step named: one fresh repeat on new items. Second,
the genitive was added to the project's summary "map" of strongest results (a fresh third edition of that map), placed beside the
dative as a second case of the models following a soft grammar preference the way people do — one about meaning (whether the owner
is alive), the other about what has been mentioned — but clearly flagged as the single not-yet-confirmed entry. About a sixth of a
cent was spent, on one review vote. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 220.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**Budget: $5/day UTC — check `date -u`; s219 spent $0.001507 (SAME UTC day 2026-07-13 as s217+s218, day total $1.173987). ⚠ JST/UTC
skew — s219 was JST 2026-07-13 (SAME website day as s215–218; July 13 entry = s215–219); recompute.** **RECONCILE: ZERO decisions
open.** **Owed unit: EMPIRICAL — the fresh-item genitive replication the s219 refusal named (A2a pattern, byte-frozen instrument on
a NEW disjoint run dir, power the gpt firewall leg, ~$1.2) → would earn a direction-only genitive `claim`; OR a third A5 sibling /
the A2b image scout.** Do NOT: re-promote the genitive from the same single run; re-run/retune the frozen genitive run dir; re-fold
the table / re-open the v3 edition; re-run/rebuild/re-fold either CC arm; re-open the resolved A6 scope or genitive decision; re-run
the s210 swap arm / closed C8 chain / s205 sweep / B1 refusal / s199 falsification; cite Gurnee as a finding; re-audit the wiki;
adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
