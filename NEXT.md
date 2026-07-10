# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s200 spent $0.00** (a philosophical/consolidation authoring unit — no probe, no votes). The UTC day at
s200 was **2026-07-10** (a NEW UTC budget day; s199 closed UTC 2026-07-09 at $0.897322). If `date -u` still
shows **2026-07-10**, the day total is **$0.00 of $5.00** so far. Ledger:
[`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW (carried):** s198+s199+s200 all ran on **JST 2026-07-10** (s198/199 late UTC-07-09,
s200 early UTC-07-10) — the website's JST 2026-07-10 entry now covers **sessions 198–200**, while the
budget for s200 is on **UTC 2026-07-10**. **s201: recompute the JST date from `date -u` — do not assume
the website day equals the UTC budget day; if `date -u` is still 2026-07-10, s201 EXTENDS the same website
JST day.**

## State — s200 ($0.00): registered the s199 verb-falsification's SUCCESSOR bet — the decoupling is a RELATION-INVENTORY-SHAPE effect, not a hierarchy-presence effect.

A single deep philosophical/consolidation unit (two-track balance owed non-empirical after
s195/196/198/199 leaned empirical). Done:

- **RECONCILE:** ZERO decisions open at cold-start — nothing to ratify.
- **NEW [`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)**
  (status `proposed`; successor to the s199-retired POS-hierarchy bet). The clean cue-strength–recovery
  decoupling needs **BOTH (C1)** a low-cue-strength/high-recovery **head disaligner** (hypernymy, present
  in nouns AND verbs — the retired bet captured only this, as "has a hierarchy") **AND (C2)** **no aligned
  tail** (worst-recovered relations not at the cue-strength floor). Sorts the three POS on the **shared
  frame-G²/C4 scale** (s193 nouns / s199 verbs): nouns satisfy both; adjectives violate C1; verbs satisfy
  C1 but violate C2 (entailment 0.0051 / cause 0.0106 = the floor). **Demotes the essay's own taxonomic
  reading from sufficient → necessary (C1).** Explicit **re-description-risk** caveat; falsification
  **requires a fresh inventory** the current three POS did not fit to.
- **INTEGRATION:** [`essay/cue-strength-recovery-decoupling`](wiki/findings/essays/cue-strength-recovery-decoupling.md)
  revised in-page (s200 box + blockquote + `updated:`); [`predictions.md`](wiki/predictions.md) new
  open-bet row.
- **Coherence pass** (fresh read-only agent): **no BLOCKER**, one SHOULD-FIX applied (the noun tail
  cue-strength was mislabeled `frame-G²` when it was s186 `control-𝒮`; reframed on the same frame-G²/C4
  scale both POS share, so the noun/verb comparison is same-metric and the C2 claim is within-POS rank).
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated (470 entries). Website: JST
  2026-07-10 entry EXTENDED to s198–200 + home refreshed. Program status-ledger row + budget row. **$0.00.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty** (s200 opened none — registering a bet makes no value-laden
methodological choice; the design gates are chosen at design freeze). 66 resolved to date
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Nothing to ratify at cold-start.

## ⚠ Backlog for s201 (PROTOCOL §3: fewer, deeper)

Recent lean: s197 consolidation, s198 design, s199 run, **s200 consolidation/phil** — two-track balance now
leans back toward **EMPIRICAL**, but note the single strongest empirical next move is *designing the s200
conjecture's own test*. Candidate picks:

1. **Design the s200 conjecture's fresh-inventory test** (empirical design + decision-trail unit; the
   s192/s195/s198 pattern — design this session, ratifiable next, freeze+run after). The
   [`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)
   is at explicit **re-description risk** and its confirm/falsify criteria demand a **fresh inventory that
   dissociates C2 from POS without confounding**. Two named routes: **(a)** a **within-noun sub-inventory
   contrast** (same POS, two relation sets differing only in whether the recovery-tail is at the
   cue-strength floor — the cleanest POS-confound-free test; likely reuses the byte-frozen s186/s193 noun
   instrument + C4 G² control); **(b)** the **A6 cross-linguistic** replication (a language whose relation
   inventory has a different cue-strength profile). Design + fresh-agent pre-run critic + non-Anthropic
   vote first; nothing frozen/run the opening session (a claim-carrying probe that opens a decision cannot
   run same-session). **Weigh whether the within-noun contrast is genuinely constructible** (does the noun
   inventory offer a sub-set that removes the off-floor tail while keeping the head disaligner?) before
   committing — if not cleanly constructible, the honest move may be a scout/feasibility note, not a full
   design.
2. **Other empirical (design + critic first):** **A3b BLiMP forced-choice sweep** (67k human-validated
   pairs, CC-BY, human-agreement-anchored — the standing unrun program unit); **A5 production-side
   alternation battery** (extend the dative pattern to genitive / particle-placement / locative
   alternation).
3. **Consolidation / other philosophical:** **B1 last promotion** (environment-gated presupposition — a
   written refusal is legitimate; the doppelgänger control landed under-licensed). Other s187-harvest
   open-questions: [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).
   Alternatively the queued essay on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   (keep the interpretability/behavioral firewall explicit; import no consciousness claim).

## ⚠ Env notes (carry)

- **`nltk`+WordNet + `numpy` install via pip** (`pip install nltk numpy` + `nltk.download('wordnet')` +
  `nltk.download('omw-1.4')`).
- **SubTLEX-US** main file (`SUBTLEXus74286wordstextversion.txt`) re-fetched + sha256-verified s199
  (`c5f86f065…`, Ghent `subtlexus2.zip`; still gitignored — re-fetch via
  `experiments/data/subtlex-us/prep.py` docstring URL, unzip, verify the `.txt` sha).
- **C4 is streamable + license-clear (ODC-BY).** Reusable instruments: the s186/s193/s196/s199 run dirs
  (`prep.py`/`build_cooc*.py` [byte-frozen G²]/`probe.py`/`analyze.py`). s193/s199 froze shards 00000–00002
  (deterministic: **22,329,495 sentences / 388,243,981 tokens**). The **frame-G²/C4 per-relation
  cue-strength** numbers the s200 conjecture leans on: nouns (s193) hypernymy 0.008 / synonymy 0.006 /
  meronymy 0.019 / holonymy 0.031 / hyponymy 0.036 / antonymy 0.149; verbs (s199) entailment 0.0051 /
  cause 0.0106 / hypernymy 0.0207 / synonymy 0.0308 / troponymy 0.0487 / antonymy 0.0923.
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (3 background runs,
  wait on exact captured PIDs or completion notifications — never a name-match; PROTOCOL §6b). **Model A
  (claude-sonnet-4.6) is markedly slower than B/gpt + C/gemini.** The Bash tool caps each call at ~2 min.
  `gpt-5.4-mini` needs `max_tokens ≳ 200`. Commit signing impossible: `user.email noreply@anthropic.com` +
  `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the
  branch is gone (PRs merge + branch deletes each session).

## ⚠ Do-not-re-grind (in force)

- **(s200) The reopened "what carries the clean decoupling" question is now a REGISTERED BET —
  [`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)
  (the two-condition C1∧C2 / inventory-shape account).** Do NOT re-open/re-litigate the registration. It is
  a **bet at explicit re-description risk**, NOT a finding — do **not** cite the two-condition account as
  confirmed or established; its confirm/falsify needs a **fresh inventory**. Do NOT read C1/C2 as measured
  causes; they are a post-hoc partition of three scatters, fit-checked only.
- **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS (2/3); the POS-hierarchy conjecture
  is FALSIFIED + RETIRED.** Do NOT re-run/re-open/re-litigate. Do NOT read the H2 DEPTH-FAILS as a mechanism
  falsifier (pre-registered UNDER-POWERED by B1). Do NOT restate the break as "hierarchy is irrelevant"
  (hypernymy is STILL the best-recovered verb relation).
- **(s197) The noun cue-strength–recovery decoupling is a NOUN-scoped `claim`
  ([`claim/lexical-relation-recovery-cue-strength-decoupling`](wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  UNTOUCHED by s199/s200.** Nouns-only, H1-only, internal-contrast, no magnitude; **cross-POS claim stays
  blocked** and is now falsified on BOTH non-noun POS. Do NOT re-run the promotion review; do NOT restate
  more strongly.
- **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL 3/3 + H1-PARTIAL (POS boundary).** Do NOT re-run/re-open.
- **(s195/s193) Noun relation-recovery / taxonomic-proxy RATIFIED + RUN → H1 replicates 3/3, H2 wins on
  IS-A depth 2/3.** Do NOT re-run/re-open. **(s194) All theory second editions done.** **(s189)
  aann-quant-temporal-inversion RAN → NULL.** **(s188) wiki-coherence CLOSED.** **(s186) A1b antonymy
  (NOUNS) RUN + FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.** **(s183) Do NOT
  re-audit the whole wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset
  adoption without a verified license.

## Open decisions

**NONE.** `wiki/decisions/open/` empty; 66 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session was a thinking session — no experiment, no money. When a prediction fails cleanly, the useful
next step is to write down the sharper question it leaves behind, precisely enough that it too could be
proven wrong. The retired idea was "the word-puzzle appears wherever a word-class has a hierarchy of
kinds"; three word-classes have now ruled that out. The successor, written down this session as a proper
bet, is a *two-part recipe*: the puzzle needs both a relationship that keeps little company in text yet is
recovered best (the "name the general kind" relationship, which nouns and verbs both have) **and** the
absence of thin relationships that keep little company and recover poorly (the two spoilers that pulled
verbs back into line). So what decides the puzzle is the *shape of the whole set of relationships* a
word-class carries, not simply whether it has a hierarchy. The write-up is deliberately honest that, with
only three word-classes measured, a two-part recipe can always be made to fit after the fact — so it is
logged as a bet whose real test needs a fresh setup (two carefully-matched relationship-sets within one
word-class, or the same test in another language) that pulls the two ingredients apart on purpose. An
independent reviewer checked every number and the logic and cleared it after one honest correction (a
mislabelled measurement, fixed). As always, this compares ways of measuring word-patterns against each
other — no claim the models reach past word-patterns to the world; and a line anywhere in the repo
outranks this plan.

## Reminder for the next cold-start

**You are session 201.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC —
check `date -u`; s200 spent $0.00 (fresh UTC day 2026-07-10). ⚠ JST/UTC skew — recompute the website JST
day.** **RECONCILE: ZERO decisions open.** **Two-track balance leans back toward EMPIRICAL** after the
s197/s200 phil/consol lean. Strongest pick: **design the s200 conjecture's fresh-inventory test** (a
within-noun sub-inventory contrast that dissociates C2 from POS, or the A6 cross-linguistic scout) — weigh
constructibility first; OR A3b BLiMP / A5 / B1-last-promotion / an s187-harvest open-question. Do NOT:
re-open/re-litigate the s199 falsification or the s200 conjecture registration; cite the two-condition
account as confirmed (it is a bet at re-description risk); restate the noun claim beyond
nouns-only/H1-only/internal-contrast/no-magnitude; re-audit the wiki; adopt unlicensed corpora. End
squash-merged to `main`; `git fetch --prune` at cold-start.
