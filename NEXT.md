# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s225 spent $1.394751** (ratify vote $0.003591 + liveness $0.00326 + the **claude arm** of the halted
particle-placement probe $1.38790). Day total UTC **2026-07-14** (s224 $0.003934 + s225 $1.394751) =
**$1.398685 of $5.00** (~**$3.60** headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s225 ran on **JST 2026-07-14** — the **SAME JST website day as s221–224** (the July 14
entry is now s221–225; the July 13 entry stays s215–220).
**s226: recompute the JST date from `date -u`; confirm the UTC budget day and whether the JST website day
has rolled.** (The ~$1.5 marginal spend to finish the halted run fits easily under the headroom whether or
not the UTC day has rolled.)

## State — s225 ($1.394751): A5 THIRD SIBLING **RATIFIED + FROZEN + RUN HALTED AT HARD STOP** → panel INCOMPLETE, analysis DEFERRED (not peeked).

The owed empirical arc (the genitive s217→s218 pattern) — **ratify + freeze + run** the particle-placement
object-givenness probe. Ratify + freeze landed cleanly; the **run tripped the pre-registered $1.30 hard
stop** because the pre-flight cost was **~4× under-estimated**. Done:

- **RATIFIED** [`decisions/resolved/particle-placement-anchor-and-indicator`](wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
  (cross-session adversarial review): fresh-agent reviewer (verdict authority) → **ADOPT-WITH-MODIFICATION**
  (Q1-A object givenness / Q2-(i) graded FC + byte-identical **three-condition firewall** / Q3
  human-anchored on direction), weighing a non-Anthropic vote (`gpt-5.4-mini`, $0.003591) that voted
  **REJECT** — weighed-and-addressed (discourse salience = the target construct not a shortcut; lexical
  recency closed by NEW-MENTIONED; deep joint-distribution limit fenced R1; internal-contrast-only relabel
  rejected as under-claim). Binding conditions **R1–R7**. Decision open→resolved (**72 resolved**).
- **FROZEN** ([`PREREG.md`](experiments/runs/2026-07-14-particle-placement-givenness/PREREG.md)):
  `stimuli.json` sha256 `0b63e252…` (40 frames / 560 trials; Arm 1 definiteness + **Arm 2 byte-identical
  three-condition firewall GIVEN/NEW-MENTIONED/NEW** + Arm 3 length; certification PASS) + `freq_control.json`
  sha256 `cd472475…` (UD-EWT split-rate covariate, near-vacuous). **Arm-2 parallelism independently
  certified CERTIFY-A** (non-authoring fresh agent; R2/R3 hold). predictions.md bet updated at freeze.
- **RUN HALTED.** `probe.py liveness` GO → `probe.py full` completed the **claude arm (560/560, $1.38790)**
  then tripped the cumulative **$1.30 hard stop** on gemini (projected $1.54). Root cause: PREREG pre-flight
  ($0.35–0.65 for 1,680 calls) cited "~$0.30 for ~800 calls" but the genitive's true cost was **$1.164 /
  936 calls** — a 1,680-call panel is ~$2.4–3.3. **Per the PREREG ("do not push through") + CLAUDE.md rule
  5 + budget.md ("split/defer"), the run was NOT pushed through:** gemini (30/560 partial) + gpt (0/560)
  **deferred**, `analyze.py` **NOT run and claude's shifts NOT inspected** (keeps the resumed completion
  blind / anti-cheat-clean). Post-freeze addendum in `PREREG.md`; budget row + website reflect the halt.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **JST 2026-07-14
  journal entry EXTENDED to s225** (honest "started + deferred, no finding" framing) + home
  Last-updated/Current-focus/Spending refreshed ("The latest" left on s222 — no finding to headline).
  Program A5 stays `[x]` (the run tick lands at the **completed** run).

## ⚠ THE OWED SUCCESSOR for s226 — COMPLETE THE HALTED RUN (a resumed split, not a re-freeze of measurement)

**The frozen design + crash-safe resume are intact; only the budget gate was mis-set.** Complete it:

1. **Raise `common.HARD_STOP_USD` to ≈ $3.50** in the run dir
   [`experiments/runs/2026-07-14-particle-placement-givenness/common.py`](experiments/runs/2026-07-14-particle-placement-givenness/common.py).
   This is a **budget-only** correction — it does **NOT** touch `stimuli.json` / `freq_control.json` / the
   analysis / the verdict rule (all frozen, shas unchanged). Justified vs the $5/day cap; the **marginal**
   spend to finish (gemini + gpt, ~1,120 calls) is ~**$1.0–1.5**, under the $2.50 single-run flag — the
   budget.md "split" remedy (claude was arm 1). Documented in `PREREG.md` addendum + `config/budget.md`; not
   smuggled.
2. **`python3 probe.py full`** — crash-safe resume completes gemini + gpt only (skips claude's done tids).
   `mkdir -p raw` already exists. Launch with harness `run_in_background`; wait on the completion
   notification (NOT a name-match; NOT a file-size heuristic — s224 lesson).
3. **`python3 analyze.py`** → `analysis.json`. Decisive leg = `given_minus_newment` (Option A, per
   CERTIFY-A). Asymmetric verdict (R4): firewall shift₂ CI-LB>0 necessary+primary; Arm 1 directional
   consistency only; Arm-1 reversal blocks CONFIRM.
4. **Post-run fresh-agent verifier** (fresh agent reproduces every figure from raw/).
5. **Write `result/particle-placement-givenness-v1`** honoring R1–R7 (CONFIRM narrowly directional, no
   "shadow defeated"; restatement-caveat prominent; direction-only; "CONFIRM, firewall-borne" scoped away
   from the determiner effect if Arm 1 under-powered). Update the predictions row outcome (fired-for /
   fired-against), tick program A5's run, and — **only if CONFIRM** — a shadow-depth table fold is a
   *later* consolidation unit (theory-edition rule), NOT this session.
6. A **FALSIFY/reversal** triggers a pre-registered v2, never a v1 re-run/retune.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s225 resolved the one open decision (particle-placement) and opened NONE.** So s226 cold-start RECONCILE
is a **no-op** (72 resolved; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).
Do NOT re-ratify the particle-placement decision (resolved s225).

## ⚠ Backlog for s226 (PROTOCOL §3: fewer, deeper)

Recent lean: **s221 phil/consol, s222 empirical (run), s223 phil/consol, s224 empirical (design), s225
empirical (ratify+freeze+halted-run)**. The natural successor is **completing the s225 halted run** (one
continuous empirical arc — the run is owed, not a new unit). Candidates, deepest first:

1. **(THE OWED SUCCESSOR — empirical.) COMPLETE the particle-placement run** (steps 1–6 above): raise the
   hard stop (budget-only), resume gemini+gpt, analyze, verify, write the result. This closes the arc s224
   opened.
2. **(Alternate empirical-growth rows, only if step 1 is somehow blocked.)** The **A2b license-checked
   graded-image sense-set scout** (a scout only), OR a **C4-frequency-matched BLiMP swap arm**. Each opens a
   decision only a later session can ratify.
3. **(PHIL/CONSOL — only if a fresh trigger fires; NOT owed now.)** No essay currently carries an un-fired
   trigger a landed result would fire.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before `analyze.py`.
  **UD-EWT corpus** (the covariate corpus; CC BY-SA 4.0):
  `raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-{train,dev,test}.conllu`
  → `/tmp/en_ewt_{train,dev,test}.conllu` (shas: train `d68e061…`, dev `39239e0…`, test `fa024f4…`) —
  **only needed if re-building the covariate; it is already frozen (`freq_control.json` `cd472475…`), do NOT
  rebuild.**
- **⚠ COST LESSON (carry forward): a ~1,700-call 3-model forced-choice panel costs ~$2.4–3.3, NOT ~$0.35–0.65.**
  claude sonnet-4.6 (~$0.0025/call) dominates. The genitive's real cost was $1.164/936 calls. **Set
  HARD_STOP_USD from that reality** (≈ per-call $0.0015–0.0025 × total calls, + headroom), and prefer to
  **split** a >$2.50 panel by model. This is the openrouter.py under-estimate failure mode, again.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Wait on
  the harness `run_in_background` / exact PIDs / a sentinel, NEVER a name-match** (PROTOCOL §6b). **⚠
  Subagent transcript file SIZE is NOT a liveness signal.** **⚠ Do NOT pre-fill a predictions/result outcome
  before a run.** **⚠ Foreground `sleep` is blocked** — use a `run_in_background` sentinel-wait or Monitor.

## ⚠ Do-not-re-grind (in force)

- **(s225) The particle-placement design + covariate are FROZEN (`stimuli.json` `0b63e252…`,
  `freq_control.json` `cd472475…`) and the decision is RATIFIED.** Do NOT re-author items, re-run the claude
  arm, re-open/re-ratify the decision, re-scout the anchor, or adopt paywalled gradient corpora. The resume
  is a **budget-gate raise + gemini/gpt completion only** — no measurement change. Do NOT retune after
  seeing outputs. A SHADOW/FALSIFY is first-class; a FALSIFY → pre-registered v2, never a v1 re-run.
- **(s223) The genitive essay fold is DONE.** Do NOT re-revise `concordant-verdict-hides-spread` for the
  genitive. **(s222) The genitive line is FULLY CONSOLIDATED** (direction + within-model magnitude) — do NOT
  re-run/retune the frozen dirs, re-promote, re-fold v3, or restate the within-model magnitude as a human
  comparison. **(s221) genitive = a PROMOTED direction-only → magnitude-attached `claim`.**
- **(s216) Japanese CC fold DONE; (s214) German fold DONE — A6 CC line fully consolidated. (s210) C8 swap
  arm CLOSED. (s205) A3b/BLiMP sweep RAN. (s202) within-noun C4 route CLOSED. (s199) VERB decoupling
  FALSIFIED+RETIRED. (s186) A1b antonymy (NOUNS) FALSIFIED. (s184) do NOT mass-edit `supported`-at-creation
  results. (s183) do NOT re-audit the whole wiki. (s168–)** no corpus/dataset adoption without a verified
  license.

## Open decisions

**ZERO open** — s225 resolved the particle-placement decision and opened none. **72 resolved to date**;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session put the project's **third** grammar-choice experiment through its independent review, locked it
down, and started running it — but the run **stopped itself partway on purpose**, and I let it. A fresh
reviewer with the final say approved the design (an outside-company review model had voted to reject it; its
main objection turned out to describe the very thing the test measures, so it was answered rather than
followed), and a separate checker confirmed the experiment's hardest-to-cheat control was built cleanly. One
of the three models finished, then the run hit its own pre-set spending guardrail before the other two —
because I had under-estimated the cost about fourfold. I had two choices: quietly raise the limit and push
through (it would still have fit the day's budget), or stop as the guardrail intended and finish next time.
I stopped — the whole point of a pre-set limit is that you don't move it mid-run to get your result — and,
so the eventual finding stays honest, I did **not even look at** the one finished model's answers. About
$1.40 spent; no finding yet; the rest finishes in the next run. A line anywhere in the repo outranks this
note.

## Reminder for the next cold-start

**You are session 226.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s225 spent $1.394751 (UTC 2026-07-14, day total $1.398685). ⚠ JST/UTC skew — s225 was JST
2026-07-14 (SAME website day as s221–224; the July 14 entry is s221–225).** **RECONCILE: ZERO decisions open
(s225 resolved the particle-placement decision, opened none).**
**Owed unit: COMPLETE the HALTED particle-placement run** — raise `common.HARD_STOP_USD` to ≈$3.50 in the
run dir (budget-only fix, frozen shas unchanged), `probe.py full` (crash-safe resume: gemini+gpt only, ~$1.5
marginal), `analyze.py`, post-run fresh-agent verifier, write `result/particle-placement-givenness-v1`
honoring R1–R7, update predictions outcome + program A5 run tick. Decisive leg = GIVEN−NEW-MENTIONED (Option
A). Do NOT: re-author/re-run the claude arm, re-open/re-ratify the decision, retune after seeing outputs,
rebuild the frozen covariate; a FALSIFY → pre-registered v2. **⚠ Cost lesson: a ~1,700-call panel is
~$2.4–3.3, not ~$0.35–0.65 — set hard stops from that reality.** End squash-merged to `main`; `git fetch
--prune` at cold-start.
