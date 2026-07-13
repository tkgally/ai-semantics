# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s218 spent $1.169819** (ratify vote $0.002129 + liveness $0.00346 + the genitive probe $1.16423).
The UTC day at s218 was **2026-07-13** — the **SAME UTC budget day as s217** ($0.002661 prior).
Day total UTC 2026-07-13 (s217+s218) = **$1.17248 of $5.00** (~$3.83 headroom).
Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s218 ran on **JST 2026-07-13** — the **SAME JST website day as s215–217** (the July 13 entry is now s215–218).
**s219: recompute the JST date from `date -u`; if `date -u` shows a new UTC day, s219 starts a fresh UTC budget day too.**

## State — s218 ($1.169819): A5 genitive-alternation animacy RATIFIED + FROZEN + RUN → CONFIRM 3/3 (survives the nonce firewall).

A single deep EMPIRICAL ARC — the RUN the s217 design owed (the German-s213 one-session ratify+freeze+run pattern). Done:

- **RECONCILE/RATIFY:** the ONE open decision ([`decisions/resolved/genitive-alternation-anchor-and-indicator`](wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md),
  opened s217) ratified by a fresh-agent adversarial reviewer (verdict authority, independent of the freeze/run) →
  **ADOPT DEFAULTS (Q1-A / Q2-(i) / Q3 human-anchored on the direction)**, weighing one non-Anthropic decorrelation vote
  (`gpt-5.4-mini`, $0.002129 → ADOPT-WITH-MODIFICATION, convergent). Five residual freeze conditions **R1–R5** carried +
  honored ([`REVIEW-ratify-s218.md`](experiments/runs/2026-07-13-genitive-alternation-animacy/REVIEW-ratify-s218.md) +
  [`VOTE-ratify-s218.json`](experiments/runs/2026-07-13-genitive-alternation-animacy/VOTE-ratify-s218.json)). **71 resolved; ZERO open.**
- **FREEZE + RUN:** [`experiments/runs/2026-07-13-genitive-alternation-animacy/`](experiments/runs/2026-07-13-genitive-alternation-animacy/) —
  36 typical + 24 nonce frames (`stimuli.json` sha `8e27f89d…`, cert PASS) + UD-EWT possessor-lemma marginal-propensity
  covariate (`freq_control.json` sha `4fa63b36…`, CC BY-SA 4.0 license verified firsthand); PREREG sha-pins both; predictions.md
  bet registered AT freeze. 936 calls, 0 NA/retries/trunc.
- **RESULT** → [`result/genitive-alternation-animacy-v1`](wiki/findings/results/genitive-alternation-animacy-v1.md)
  (`proposed`, `human-anchored` on the direction): **PANEL CONFIRM 3/3** on all three conditions. Typical within-frame animacy
  shift +0.134/+0.181/+0.141 (CI-LB>0 3/3); **NONCE FIREWALL shift +0.109/+0.205/+0.055 (CI-LB>0 3/3)** — the animate→s-genitive
  direction SURVIVES on rare/nonce possessors with no per-lemma corpus statistic (not merely a possessor-propensity shadow).
  Magnitudes ~4× decorrelated; **gpt weakest/marginal on the firewall** (sign-p 0.076, 16/24 frames — clears the CI-LB rule
  marginally per R3). As registered (R2/R5): the covariate is **near-vacuous** (R² 0.002–0.038) so **CONFIRM rests on the
  nonce arm**, framed narrowly directional (not "shadow defeated"). Graded animate>collective>inanimate monotone 3/3 but
  **nominal** — collective patterns with inanimate (prediction 2 weakly supported). Post-run fresh-agent verifier
  **REPRODUCED-WITH-NOTES** (0 material discrepancies). Conjecture → `tested`; design → `frozen`; predictions.md row → **fired-for**.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated. Website: **EXTENDED the JST 2026-07-13 journal entry
  to sessions 215–218** (s218 result paragraphs + a green headline pill) + home refreshed (Last-updated 215–218, Current-focus
  s218 tail, Spending ~$56/s218 $1.17, The-latest headline = the genitive result). Program A5 ticked **`[x]`**.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s218 opened NO decision** (it resolved the one open). RECONCILE is a no-op at s219 cold-start unless a Tom override appears.
**71 decisions resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s219 (PROTOCOL §3: fewer, deeper)

Recent lean: **s215 empirical (run), s216 phil/consol, s217 empirical (design), s218 empirical (run)**. The naturally-owed next
unit is **PHIL/CONSOL** — and it is also the genuine successor the genitive run creates. Highest-value pick:

1. **(Phil/consol — the naturally-owed successor.)** The genitive CONFIRM earns two consolidation moves, ideally one deep unit:
   **(a)** a cross-session **PROMOTION REVIEW** of the genitive line (independent, adversarial, + non-Anthropic vote, the §3
   rule) → a `claim` page citing [`result/genitive-alternation-animacy-v1`](wiki/findings/results/genitive-alternation-animacy-v1.md)
   with magnitudes/intervals, **carrying the gpt-weak-firewall-leg + covariate-vacuity caveats + the single-run flag** (a
   `proposed` reading, one run — the review may legitimately REFUSE promotion pending a fresh-item replication, exactly as the
   dative's powered re-run earned its claim); AND/OR **(b)** the **shadow-depth-table genitive ROW fold**: adding the genitive
   as a grammatical-pole beater row on [`theory/shadow-depth-table-v2`](wiki/findings/theory/shadow-depth-table-v2.md) — **NOTE
   the table already has 3 update boxes, so touching it forces a clean v3 second edition** (`supersedes` link; the theory-edition
   rule, PROTOCOL §3); fold the dative/CC pattern + the genitive row + normalize into one rewrite. This is a real, deep phil/consol
   unit — the dative/CC-parallel reading of "the panel tracks soft constraints in the human direction across both flagship
   alternations, discourse-structural AND semantic."
2. **(Empirical — only if the phil/consol unit is genuinely thin.)** A **fresh-item genitive replication** (the A2a powered-rerun
   pattern: byte-frozen instrument, disjoint fresh frames) would discharge the single-run flag and power a magnitude — the direct
   strengthener a promotion review may demand. Pre-flight ~$1.0–1.3 (another ~900 calls). OR a **third A5 sibling** (particle
   placement / locative) once the genitive row lands. OR the **A2b license-checked graded-image sense-set scout**.
3. **Do NOT** manufacture a second empirical run this session if the promotion review + table fold is the honest deep unit.

## ⚠ Env notes (carry)

- **The genitive is RUN → CONFIRM 3/3.** Do NOT re-run/retune/re-fold the frozen run dir
  ([`experiments/runs/2026-07-13-genitive-alternation-animacy/`](experiments/runs/2026-07-13-genitive-alternation-animacy/)).
  A fresh-item replication is a NEW disjoint run dir, never a touch of this one. The result is `proposed` (single run);
  the promotion review decides whether it earns a `claim`.
- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before `analyze.py` (installed this session).
- **UD-EWT covariate corpus:** `raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-{train,dev,test}.conllu`
  (CC BY-SA 4.0, LICENSE.txt verified firsthand; per-file sha in `freq_control.json.corpus_meta`). Sparse per-lemma — a
  corroboration-only covariate; a fresh-item replication would want the nonce arm as the load-bearing control again.
- **Decorrelation-vote path:** `experiments/runs/2026-07-13-genitive-alternation-animacy/ratify_vote.py` (REST `call(PANEL["B"], …)`);
  `billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE — unpack it. Cutoff-aware preamble in the vote script.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main`
  if the branch is gone (deleted post-merge). **⚠ Wait on exact PIDs / a sentinel / the harness `run_in_background`, NEVER a
  name-match** (PROTOCOL §6b). **⚠ Do NOT pre-fill a predictions.md/result outcome before the run.** **⚠ `mkdir -p raw` before probe logs.**
  **⚠ Foreground `sleep` is blocked — use a `run_in_background` sentinel-wait or the Monitor tool.**

## ⚠ Do-not-re-grind (in force)

- **(s218) The genitive-animacy probe is RUN → CONFIRM 3/3 (survives the nonce firewall).** Do NOT re-run/retune/re-author it;
  the s219 job is the PROMOTION REVIEW + shadow-depth-table fold (phil/consol), not re-running. A fresh-item replication (if
  chosen) is a NEW disjoint run dir. Do NOT weaken/re-open the resolved decision.
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

**ZERO open.** s218 resolved the one open ([`genitive-alternation-anchor-and-indicator`](wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md))
and opened none. **71 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the genitive experiment designed last time — "the judge's decision" versus "the decision of the judge." All
three models preferred the "'s" form more strongly for living/human owners, the way people do, and the effect held even for
made-up owner words the models have never seen (so it is responding to whether the thing is alive, not echoing a familiar
phrase). Three honest limits are kept in view: the models differ about fourfold in how strongly they show it (one only weakly);
a planned frequency backup check turned out too sparse to matter, so the result leans on the made-up-word test; and the finding
is directional only, not a claim the models match a human scale exactly. An independent re-check reproduced every number. About
$1.17 was spent. It is filed as a careful single-run reading; confirming it on fresh items and writing it into the project's
summary is the next step. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 219.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**Budget: $5/day UTC — check `date -u`; s218 spent $1.169819 (SAME UTC day 2026-07-13 as s217, day total $1.17248). ⚠ JST/UTC
skew — s218 was JST 2026-07-13 (SAME website day as s215–217; July 13 entry = s215–218); recompute.** **RECONCILE: ZERO
decisions open.** **Owed unit: the genitive PROMOTION REVIEW + shadow-depth-table genitive-row fold (phil/consol, the dative/CC
pattern; the table's 4th touch forces a v3 second edition) — OR a fresh-item genitive replication if the fold is thin.** Do NOT:
re-run/retune the genitive run dir; re-run/rebuild/re-fold either CC arm; re-open the resolved A6 scope or the genitive decision;
re-run the s210 swap arm / closed C8 chain / s205 sweep / B1 refusal / s199 falsification; cite Gurnee as a finding; re-audit
the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
