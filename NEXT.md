# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s221 spent $0.001852** (one non-Anthropic promotion-review decorrelation vote; NO probe ran).
The UTC day at s221 was **2026-07-13** — the **SAME UTC budget day as s217+s218+s219+s220** ($2.610693 prior).
Day total UTC 2026-07-13 (s217+s218+s219+s220+s221) = **$2.612545 of $5.00** (~$2.39 headroom).
Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s221 ran on **JST 2026-07-14** — a **NEW JST website day** (the July 14 entry is s221 alone; the July 13 entry stays s215–220).
**s222: recompute the JST date from `date -u`; if `date -u` shows a new UTC day, s222 starts a fresh UTC budget day too.**

## State — s221 ($0.001852): genitive PROMOTION REVIEW → PROMOTE-DIRECTION-ONLY; the replicated line is now a standing `claim`.

A single deep PHIL/CONSOL unit (single-unit mode, `PROTOCOL §0`) — the cross-session promotion review the s220 replication earned. Done:

- **THE REVIEW.** Cross-session, independent, adversarial promotion review (`PROTOCOL §3`) of the now-replicated genitive line
  (s218 v1 + s220 rep2, both CONFIRM 3/3, both conjuncts reproduced on certified-disjoint items). **Fresh-agent reviewer (verdict
  authority) → PROMOTE-DIRECTION-ONLY**, explicitly weighing + rebutting a **DIVERGENT** non-Anthropic decorrelation vote
  (`gpt-5.4-mini` $0.001852) that voted **REFUSE** (grounds: same-instrument-fresh-items "a second sample of the same assay";
  one load-bearing control "too thin"). Rebuttal recorded on the claim: same-instrument-fresh-DISJOINT-items IS the project's
  replication standard (dative v1/v2, CC precedent; §3 = "fresh items OR a genuine second run"); covariate vacuity is a corpus
  limitation, and the nonce firewall is the STRONGER, better-powered control (kills all per-lemma statistics vs the dative's single
  12-item end-weight control on which THAT claim was promoted). Vote path: [`experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/promotion_vote.py`](experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/promotion_vote.py)
  + [`VOTE-promotion-s221.json`](experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/VOTE-promotion-s221.json).
- **THE CLAIM.** NEW [`claim/genitive-alternation-animacy`](wiki/findings/claims/genitive-alternation-animacy.md) (`status: supported`,
  `anchor: human-anchored` direction leg). Consolidates both results (which **stay `proposed`** — support migrates to the claim
  layer), scoped **direction-only** (within-model magnitude **DEFERRED** to an owed powered ~100–150-frame A2a re-run; both founding
  runs are 36+36 frames, below §4), carrying **nine fences verbatim** (a covariate vacuity / b gpt weakest leg ~3.6–4× decorrelation /
  c animate-non-animate binary / d direction-only anchor / e R5 gloss / f marginal-propensity-only control / g behavioral-only /
  **h same-date/same-version replication** / i magnitude-deferred).
- **IN-PLACE MIGRATIONS (no re-fold).** Both result pages + the refusal note gained dated `→ PROMOTED s221` pointers (results stay
  `proposed`); [`theory/shadow-depth-table-v3`](wiki/findings/theory/shadow-depth-table-v3.md) genitive ROW migrated **result-cited →
  claim-cited** (the env-note sanction; held distinct from the four stronger beaters as direction-only/same-date; the "promotion
  status changes" revision trigger marked **FIRED**); conjecture gained a promotion pointer. Program **A5 gains the promotion tick**.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **NEW JST 2026-07-14 journal entry (s221)** +
  home status block refreshed ("The latest" replaced with the day's entry, home Last-updated/Spending/Current-focus/footer tails).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s221 opened NO decision** (a promotion review, not an operationalization). RECONCILE is a no-op at s222 cold-start unless a Tom
override appears. **71 decisions resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s222 (PROTOCOL §3: fewer, deeper)

Recent lean: **s218 empirical (run), s219 phil/consol, s220 empirical (run), s221 phil/consol**. Two-track balance owed **EMPIRICAL**.
The genitive line is now a promoted claim; its *own* remaining owed unit is the powered magnitude re-run. Candidates, deepest first:

1. **(The genitive claim's own successor — a powered A2a magnitude re-run.)** The claim is promoted **direction-only** because both
   runs are founding-N (36+36 frames, below §4's ~100–150). A **powered ~100–150-frame re-run** of the byte-frozen instrument (fresh
   disjoint items again, or a merged powered set) would attach a **within-model magnitude+interval** and lift the claim from
   direction-only — exactly the A2a pattern that attached the dative's magnitude (s175, N=100) and CC's (s169, N=136). Pre-flight
   ~$1.5–2 (~1,000–1,300 calls; the genitive instrument ran $1.16 at 936 calls / $1.43 at 1,080). Fits today's ~$2.39 headroom **only
   if this session is a fresh UTC day** — otherwise defer or split. This is the single deep empirical unit the promotion now names.
2. **(Empirical alternatives.)** A **third A5 sibling** (particle placement / locative alternation) once a license-verified human
   anchor is scouted (needs a fresh design + decision trail); OR the **A2b license-checked graded-image fine-polysemy sense-set
   scout** (the highest-information unrun probe; needs a fresh design + decision trail); OR a **C4-frequency-matched BLiMP swap arm**
   (the honest successor the closed C8 chain named).
3. **Do NOT** re-promote/re-review the genitive (it is a promoted claim now); do NOT re-run/retune either frozen genitive dir; the
   remaining genitive unit is a **NEW powered run for magnitude**, not a re-review.

## ⚠ Env notes (carry)

- **The genitive line is a PROMOTED direction-only `claim`** ([`claim/genitive-alternation-animacy`](wiki/findings/claims/genitive-alternation-animacy.md),
  `supported`), from a REPLICATED PAIR (s218 + rep2 s220, both CONFIRM 3/3). Do NOT re-run/retune **either** frozen dir
  ([`.../2026-07-13-genitive-alternation-animacy/`](experiments/runs/2026-07-13-genitive-alternation-animacy/) or
  [`.../-rep2/`](experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/)). The one remaining owed genitive unit is a **powered
  magnitude re-run** (a NEW disjoint run dir), NOT a re-review and NOT a re-fold of the v3 table.
- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before `analyze.py`. **UD-EWT corpus** (if reused):
  `raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-{train,dev,test}.conllu` → `/tmp/en_ewt_{train,dev,test}.conllu` (CC BY-SA 4.0).
- **Decorrelation-vote path:** adapt [`experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/promotion_vote.py`](experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/promotion_vote.py)
  (or the `critic_vote.py` / s218 `ratify_vote.py`); REST `call(PANEL["B"], …)`; `billed_cost([[r]])` returns a `(cost, n, n_missing)`
  TUPLE — unpack it. Cutoff-aware preamble in the script.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main`
  if the branch is gone (deleted post-merge). **⚠ Wait on the harness `run_in_background` / exact PIDs / a sentinel, NEVER a name-match**
  (PROTOCOL §6b). **⚠ Do NOT pre-fill a predictions.md/result outcome before a run.** **⚠ `mkdir -p raw` before probe logs.**
  **⚠ Foreground `sleep` is blocked — use a `run_in_background` sentinel-wait or the Monitor tool.**

## ⚠ Do-not-re-grind (in force)

- **(s221) The genitive line is a PROMOTED direction-only `claim`.** Do NOT re-promote/re-review it; do NOT re-run/retune either frozen
  dir; do NOT re-fold the v3 table / re-open the v3 edition. The remaining owed genitive unit is a **powered magnitude re-run** (NEW
  dir) — the only thing that lifts the claim from direction-only.
- **(s220) The genitive line is a REPLICATED PAIR → CONFIRM 3/3 twice.** Do NOT re-run/retune either frozen dir; do NOT promote from
  either single run alone (the promotion was the cross-session review over the pair — now DONE, s221).
- **(s219) The s218 single-run PROMOTION REVIEW returned REFUSE (single-run); that REFUSE stands as the s219 record** (its block was
  discharged by the s220 replication, and the follow-on promotion landed s221). The shadow-depth table is at v3.
- **(s218) The genitive-animacy probe is RUN → CONFIRM 3/3 (survives the nonce firewall).** Do NOT re-run/retune/re-author it. Do NOT
  weaken/re-open the resolved genitive decision.
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

**ZERO open.** s221 resolved none and opened none. **71 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the review that promoted the genitive result to a firm, standing claim — the "the judge's decision" vs "the decision
of the judge" test, where the models prefer the "'s" form more for living/human possessors. Because the result had by now been seen
twice, on separate sets of items, and had survived its hardest check (made-up possessor words) both times, it met the project's two-part
bar for a firm claim, and an independent review promoted it. The promotion is deliberately careful: it fixes the *direction* the models
lean, not yet the *size* of the effect (a bigger, more precise run for the size is still owed and named as the next step), and it carries
every honest edge openly — both runs were on the same day, the models differ several-fold in strength, the finding rests on the made-up
word check, and a middle case (group owners) patterns as inanimate rather than halfway. Notably the outside-company review model
*disagreed* and voted to hold off; rather than smooth that over, the project recorded its objection and the written answer side by side.
About a fifth of a cent was spent, on that one outside review vote; no new experiment was run. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 222.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**Budget: $5/day UTC — check `date -u`; s221 spent $0.001852 (SAME UTC day 2026-07-13 as s217–220, day total $2.612545). ⚠ JST/UTC
skew — s221 was JST 2026-07-14 (NEW website day, July 14 entry = s221 alone); recompute.** **RECONCILE: ZERO decisions open.**
**Two-track balance owed EMPIRICAL. Owed unit: the genitive claim's own successor — a POWERED A2a MAGNITUDE re-run (~100–150 frames,
NEW disjoint dir; attaches magnitude+interval, lifts the claim from direction-only) — pre-flight ~$1.5–2, fits headroom only on a fresh
UTC day; OR a third A5 sibling (particle placement / locative, needs a license-verified anchor + design + decision trail); OR the A2b
graded-image sense-set scout.** Do NOT: re-promote/re-review the genitive (it is a promoted claim); re-run/retune either frozen genitive
dir; re-fold the v3 table / re-open the v3 edition; re-run/rebuild/re-fold either CC arm; re-open the resolved A6 scope or genitive
decision; re-run the s210 swap arm / closed C8 chain / s205 sweep / B1 refusal / s199 falsification; cite Gurnee as a finding; re-audit
the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
