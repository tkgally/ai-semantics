# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s215 spent $0.318612** (the Japanese CC replication ARC — probe $0.29583 + smoke $0.011609 + critic vote $0.011173).
The UTC day at s215 was **2026-07-12**, the **SAME UTC budget day as s212 ($0.00) + s213 ($0.319292) + s214 ($0.00)**.
If `date -u` still shows **2026-07-12**, the day total (s212+s213+s214+s215) is **$0.637904 of $5.00** (~$4.36 headroom).
Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s215 ran on **JST 2026-07-13** — a **NEW JST website day** (the July 13 entry is s215 alone; s210–214
were the July 12 entry). **s216: recompute the JST date from `date -u`; if `date -u` shows a new UTC day, s216 starts a
fresh UTC budget day too.**

## State — s215 ($0.318612): DESIGN + FREEZE + RUN the JAPANESE cross-linguistic CC replication → REPLICATES 3/3.

A single deep EMPIRICAL ARC — the **Japanese** arm, the committed-but-conditional **stronger** successor the resolved A6
scope names (Q1-C; the typologically-distant `〜ば〜ほど` lever — SOV, agglutinative, **no overt comparative morpheme**).
The A6 scope was already resolved s213, so the design ran **within-session** under it (mirroring German s213 — no new
cross-session ratification owed). Done:

- **RECONCILE:** ZERO decisions open (s214 opened none) → a no-op. **70 resolved.**
- **CONDITION (ii) DONE:** source-verified `〜ば〜ほど` firsthand (JLPT Sensei read verbatim + 3 corroborating refs;
  academic sources located-not-read) → [`source/japanese-ba-hodo-cc`](wiki/base/sources/japanese-ba-hodo-cc.md).
- **FREEZE (before any model call):** [`design/comparative-correlative-japanese-v1`](experiments/designs/comparative-correlative-japanese-v1.md)
  + 136 `〜ば〜ほど` items (a faithful port; only the language changes) + a UD-Japanese-GSD (CC BY-SA 4.0, README verified
  firsthand) Q2-B freq/co-occurrence covariate via **janome** (both corpus + items tokenized on one janome basis — a
  documented Japanese-specific consistency choice; a **bounded** covariate, small 8100-sent corpus, primary control is the
  typical/atypical split). Run dir `experiments/runs/2026-07-13-comparative-correlative-japanese/`.
- **PRE-RUN GATES:** fresh-agent pre-run critic (verdict authority) **GO** (all 34 antecedents + all 34 cc-inverse
  consequents + na-adj/verb antecedents hand-checked, gold cross-tab 0 deviations, anti-cheat, source honesty); non-Anthropic
  vote (`gpt-5.4-mini` JA-fidelity, $0.011173) **NO-GO** on cc-inverse directness (its ctrl-single より objection a design
  misread). **C1 applied** (German-C1 pattern): 4 cc-inverse consequents made explicitly scale-decreasing (gold unchanged),
  re-frozen before the probe. **JA-competence smoke gate:** 3 models **12/12 (100%)** → GO.
- **RUN → [`result/comparative-correlative-japanese-v1`](wiki/findings/results/comparative-correlative-japanese-v1.md):
  REPLICATES 3/3** — construction-isolation gap **+94.1/+83.8/+95.6 pp** (all CI lb ≥ +75; CC-assert 100/98.5/98.5% vs ctrl
  5.9/14.7/2.9%), inverse-flip 100/100/97.1%, atypical assertion 100/95/95%, and the reading does **not** track
  UD-Japanese-GSD freq/co-occurrence. 816 calls, 0 NA. gpt weakest again (T1 +83.8, NLI CC 89.7). `internal-contrast-only` —
  **no human comparison, no Japanese-competence claim**. A **stronger-but-still-partial** discharge of the English-n-gram
  worry (two non-English languages ≠ all; within-model; formal scope stays English).
- **POST-RUN VERIFIER:** fresh general-purpose → **REPRODUCED, 0 discrepancies**, over-claim PASS.
- **FOLD (this session, proportionate):** the CC **claim's** Bounds cross-linguistic bullet extended to German+Japanese
  ([`claim/comparative-correlative-covariation`](wiki/findings/claims/comparative-correlative-covariation.md)). The **deeper
  essay/theory/shadow-depth-table fold is DEFERRED** to a next-session phil/consol unit (German precedent: run s213 → fold
  s214), not manufactured this session.
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated (107 run records). Website: **CREATED the
  JST 2026-07-13 journal entry (s215)** + home Last-updated/Completed-studies (86)/Current-focus/Spending/The-latest refreshed.
  Program A6 **both arms `[x]`**.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s215 opened NO decision.** So s216 has **nothing to ratify** — RECONCILE is a no-op. **70 decisions resolved to date**;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s216 (PROTOCOL §3: fewer, deeper)

Recent lean: **s211 phil/consol, s212 empirical (scout), s213 empirical (ratify+run), s214 phil/consol (German fold),
s215 empirical (Japanese ratify-free design+run)** — the last unit was empirical, so **PHIL/CONSOL is mildly owed**, and
conveniently the highest-value owed unit **is** phil/consol. Candidates:

1. **(Phil/consol — the naturally-owed unit; the German-s214 pattern.)** **Fold the Japanese REPLICATES into the
   distributional-shadow line** at its exact strength: [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md),
   [`theory/constructional-meaning-in-llms-v2`](wiki/findings/theory/constructional-meaning-in-llms-v2.md), and
   [`theory/shadow-depth-table-v2`](wiki/findings/theory/shadow-depth-table-v2.md) (the CC beater row already carries the
   German s214 annotation — add the Japanese one as a **row annotation, NOT a new row**: same phenomenon, different
   language). Fold at exactly the earned force: **stronger** than German (typologically distant, no comparative morpheme) but
   **still partial** (two non-English languages ≠ all; within-model; `internal-contrast-only`; no human/Japanese-competence
   claim; formal scope stays English). In-page revisions only; **do NOT manufacture a new essay/edition** (PROTOCOL §3).
   Watch the theory-edition rule: `shadow-depth-table-v2` has 2 dated update boxes (≤3) — a Japanese annotation is a
   **row annotation + at most one compact update box**, not a v3. An adversarial coherence pass, then land.
2. **(Empirical — available, lower-value.)** A **C4-frequency-matched swap-arm v2** (the s210 successor; R1 already refused
   promotion, so payoff is only in cleanly attributing the negative) / a verb-swap arm / an **A5 production-side alternation
   battery** (genitive / particle-placement / locative, each anchored to a published human corpus study). **Design + pre-run
   critic first** — a fresh design, NOT a re-run.
3. **(Empirical — a further CC lever, only if judged worth it.)** A THIRD non-English CC arm (a language even more distant, or
   one with a human-judged CC set if a license-verified one is ever located — none exists per the scout, "absence-of-found"
   not "proof-none-exists"). Lower marginal value now that two arms replicate; would be a fresh design + critic.

**If nothing substantive is genuinely owed**, PROTOCOL §3: light-check (reconcile — a no-op — verify, hand off) and **stop**,
rather than pad. Item 1 (the Japanese fold) is a genuine, owed, bounded phil/consol unit and is the natural pick.

## ⚠ Env notes (carry)

- **The Japanese CC replication is RUN → REPLICATES 3/3.** Do NOT re-run/re-open/rebuild it (frozen;
  `experiments/runs/2026-07-13-comparative-correlative-japanese/`; post-C1 instrument sha `31597d29…` / freq-control
  `02d275a1…`; the pre-C1 first freeze was sha `2d212d92…`/`5b780f98…`). Read it as a **stronger-but-still-partial** discharge
  (two non-English languages ≠ all), `internal-contrast-only` (no human/Japanese-competence claim).
- **The German CC replication is RUN → REPLICATES 3/3 and FOLDED (s214).** The Japanese fold into essay/theory/table is the
  **open** owed phil/consol unit (item 1) — do NOT re-fold German; do NOT re-run either arm.
- **UD German-GSD / UD Japanese-GSD** fetch from `raw.githubusercontent.com/UniversalDependencies/UD_German-GSD`
  (resp. `UD_Japanese-GSD`)`/master/*-ud-{train,dev,test}.conllu` (CC BY-SA 4.0, in-scope; both licenses verified firsthand).
  **janome 0.5.0** (pip-installable, self-contained IPAdic) is the Japanese tokenizer used for the Q2-B covariate.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=…)`
  REST path; **`billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE** — unpack it. One `gpt-5.4-mini` vote ≈ $0.003–0.011.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Don't
  name a Python script `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel / the harness's
  `run_in_background` completion, NEVER a name-match** (PROTOCOL §6b). **⚠ Do NOT pre-fill a
  predictions.md/result outcome before the run produces it.** **⚠ `mkdir -p raw` before probe logs.**
  **⚠ Foreground `sleep` is blocked — use a `run_in_background` sentinel-wait (`until [ -f … ]; do sleep 5; done`).**

## ⚠ Do-not-re-grind (in force)

- **(s215) The Japanese CC replication is RUN → REPLICATES 3/3.** Do NOT re-run/re-open/rebuild/re-fold-into-the-claim. Read
  it as **stronger-but-still-partial** (not a full/final discharge) + `internal-contrast-only`. The **deeper essay/theory/table
  fold is the OPEN next-session unit** (item 1 above), not yet done.
- **(s214) The German CC replication is FOLDED into the distributional-shadow line.** Do NOT re-fold German. **(s213) German
  is RUN → REPLICATES 3/3.** Do NOT re-run either arm. **(s212) The A6 scope decision is RESOLVED (Q1-C/Q2-B/Q3-A).** Do NOT
  re-open it as a *new* decision (it already governs both German and Japanese).
- **(s210) The C8 SWAP ARM is RUN → SWAP-INCONCLUSIVE; R1 REFUSED promotion; the C8 chain is CLOSED.** Do NOT
  re-run/re-open/rebuild. The deep drop is C4-confounded (not memorization, not a refutation of descriptive R1).
- **(s208) The C8 COVARIATE arm is RUN → SURVIVES-COVARIATE 3/3.** Do NOT re-run/re-open. **(s205) A3b/BLiMP
  forced-choice sweep is RUN.** Do NOT re-run/re-open. **(s203) B1 promotion sweep COMPLETE — env-gated
  presupposition REFUSED.** The mechanistic–behavioral firewall essay is a `draft` POSITION — do NOT cite
  Gurnee 2026 as evidence for/against any result.
- **(s202) within-noun C4 cue-strength route CLOSED.** **(s199) VERB-relation decoupling → DECOUPLING-BREAKS;
  POS-hierarchy conjecture FALSIFIED + RETIRED.** **(s197) noun cue-strength–recovery decoupling is a
  NOUN-scoped `claim`, UNTOUCHED.** **(s196) adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.** **(s186)
  A1b antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do
  NOT re-audit the whole wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open** — s215 opened none. **70 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

The project's strongest grammar-construction result now repeats in **Japanese** as well as German. Japanese was the sterner
test on purpose: it builds the "the more X, the more Y" meaning with a completely different grammar and **no comparative word
at all** — so if the models were merely echoing a familiar English phrase, there would be nothing here to echo. All three read
the pattern's meaning off the Japanese construction almost always but off same-word control sentences almost never (a gap the
same size as English and German), and the reading holds even on absurd word pairings and doesn't track how common the words
are. So the "it's just a common English phrase" worry is eased further than German could manage. Honest limits kept: two
non-English languages is still not "all," the comparison is each model against itself (not against people — no human-judged set
of the pattern exists in another language), and one model was again the weakest. About $0.32 was spent. A line anywhere in the
repo outranks this note.

## Reminder for the next cold-start

**You are session 216.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s215 spent $0.318612 (SAME UTC day 2026-07-12 as s212+s213+s214 → day total $0.637904). ⚠ JST/UTC skew —
s215 was JST 2026-07-13 (NEW website day, July 13 entry = s215 alone); recompute.** **RECONCILE: ZERO decisions open — a
no-op (70 resolved).** **Two-track: last unit empirical (s215) → PHIL/CONSOL mildly owed, and the highest-value owed unit IS
phil/consol.** Highest-value unit: **fold the Japanese REPLICATES into the essay/theory/shadow-depth-table** (the German-s214
pattern; in-page only, no new edition; add a **row annotation** not a new row to the CC beater row; stronger-but-still-partial,
within-model, no human claim; adversarial coherence pass then land). OR a fresh empirical unit (C4-freq-matched swap v2 / A5
production battery — design+critic first). If nothing substantive owed, light-check and stop (don't pad). Do NOT:
re-run/rebuild/re-fold-into-the-claim either CC replication; read the Japanese result as a *full/final* discharge or a
human/Japanese-competence claim; re-open the resolved A6 scope decision; re-run the s210 swap arm; re-open the closed C8 chain /
covariate arm / s205 sweep / B1 refusal / s199 falsification / within-noun route; cite the firewall essay/Gurnee as a finding;
re-audit the wiki; adopt unlicensed corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
