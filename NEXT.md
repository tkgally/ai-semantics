# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25** spent **$4.72482** (all of it session 107, the VWSD v2 day-1 text-only build); sessions 108–111
each spent **$0**. **If a session still opens on UTC 2026-06-25, only ≈$0.275 headroom remains — do NOT run any image arm today.** A fresh UTC day resets to $5
**and enables the image arm**. **Check `date -u` FIRST.** The IMAGE and DISTRACT arms (≈$6.9 each) must each be day-split across fresh UTC days regardless. Full
ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 111 (UTC 2026-06-25) — workflow, 2 waves + fresh adversarial coherence pass, $0.** Branch even with `main` at start (s110/#163 merged).
`decisions/open/` **EMPTY** → no ratification owed; no Tom override. A **third consecutive philosophical-track** session (the empirical lever stayed
budget-blocked — still no fresh UTC day when the session opened, 20:45 UTC). Two waves landed:

1. **Wave 1 — the two remaining named externalist-reference primaries ingested at primary strength, every quote verified character-for-character:**
   - [`source/evans-1973-causal-theory-of-names`](wiki/base/sources/evans-1973-causal-theory-of-names.md) — Evans's **critique-from-within** of the causal
     theory. Evans **rejects** the pure baptism/causal-chain picture (the **Madagascar** referent-shift case, p. 196; "mislocated the causal relation," p. 197)
     and substitutes reference to the **dominant causal source of the body of information** a community associates with the name (pp. 198-199, 202), under a
     **common-knowledge-in-a-community** name-hood condition (p. 202, "more stringent than Kripke's", p. 203) + a **deference** clause (p. 205). Read Part I
     (pp. 187-208) in full from a self-archived JSTOR scan (official OUP/JSTOR paywalled); Altham's Part II **not** ingested.
   - [`source/burge-1979-individualism-and-the-mental`](wiki/base/sources/burge-1979-individualism-and-the-mental.md) — **social externalism** (the **arthritis**
     three-step case, pp. 77-79): externalizes the **content of propositional attitudes** and covers **ordinary** words (not just natural kinds), via **incomplete
     understanding** (p. 79) + **deference** (p. 80); communal practice fixes content "even in cases where I fully understand" (p. 85). Read in full from the
     open-access UCLA Philosophy PDF (real digital text layer).
   - Both are **theory sources, NOT human anchors.** `wanted.md` Evans + Burge entries flipped to RECEIVED.
2. **Wave 2 — orchestrator integration (the load-bearing judgement; not parallelized):**
   - **Concept-page correction** ([`concept/referential-meaning`](wiki/base/concepts/referential-meaning.md)): it had mis-described Evans as holding names refer
     "via a causal chain back to a baptismal event" — **the view Evans rejects.** Corrected to the information-source + community account; Evans + Burge marked
     in-repo; **only Kripke** (the baptism-chain pole Evans criticizes) now remains of the named externalist primaries.
   - **Trigger (c) discharged across the three reference essays** ([`essay/reference-as-premise-bound`](wiki/findings/essays/reference-as-premise-bound.md),
     [`essay/reference-denials-disunified`](wiki/findings/essays/reference-denials-disunified.md),
     [`essay/stereotype-without-the-expert`](wiki/findings/essays/stereotype-without-the-expert.md)). **The judgement: neither Evans nor Burge settles the
     corpus-membership/corpus-inheritance antecedent — it stays an off-board classificatory choice, so all three theses are UNCHANGED.** What changed: (a) the
     externalist frame is now substantially primary-anchored (Putnam + Evans + Burge); (b) **Evans supplies a genuinely new angle Putnam lacked** — reference
     tracks the *dominant causal source of a body of information*, and "source" is satisfied by *reading a person's works* (p. 199), a **textual** hook that makes
     the pro-transfer side of the antecedent **textually arguable rather than free** (though paired with knowledge-aptness, p. 200, and intentions/common-knowledge,
     p. 202, conditions a deflationist denies); (c) **Burge** generalizes the dependency to attitude-*content* and makes *deference* constitutive, reinforcing the
     "neither role" essay on independent grounds. Denial-3 row 3 **sharpened, not rewritten**; stereotype-essay trigger (a) fired by Evans the *unexpected* way
     (baptism chain rejected → no fourth component → re-scoped to Kripke).

**Coherence pass (fresh read-only agent) returned: BLOCKER none; one SHOULD-FIX (stale `wanted.md` Evans/Burge statuses — FIXED); NIT none.** Every Evans/Burge
quote + locator used in the four edited pages was cross-checked verbatim against the two source pages; the Evans correction confirmed correct; the trigger
discharges judged faithful (sharpened-but-undecided, never over-claimed; no empirical/human-comparison claim introduced).

## ⚠ VWSD v2 — the empirical lever, still gated on a FRESH UTC day (UNCHANGED from s108–s110)

The VWSD v2 day-1 build is **DONE, FROZEN, and critic-certified (GO-WITH-CONDITIONS)**. The result `result/vwsd-grounding-headroom-v2` still **does NOT exist
and is NOT cleared**. The spend-bearing IMAGE then DISTRACT arms require a **fresh UTC day**. Committed-file checksums: `frozen/descriptors.json` **`26616a55…`**
(NOT the `afe74f82…` descriptor-only pre-leak sha — see s108 correction), `frozen/run_items.json` `7f9e52fa…`, `raw/text.json` `3a9dfcbf…`.

### The THREE binding conditions the execution session MUST honor (from the s108 certification)

1. **Gemini Option-A floor elevation is a first-class caveat.** Gemini's floor is `.158` Wilson[.104,.234] (lower bound > chance .10). Any gemini-specific
   image-rescue / gating claim must (a) be read against gemini's own ≈`.158` floor, not bare `.10`; (b) carry the elevation as a foregrounded caveat on the
   result page; (c) be reported alongside the pooled (`.122`) and per-model reads (claude `.092` clean / gpt `.117` near-clean carry primary weight).
2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no 2/3 band**. The gating shape is read across a **bimodal**
   separability distribution; the **binned image-rescue contrast** (text-failed vs text-succeeded) is the test of record, **not** a graded `sep→rescue` slope;
   the continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + 2/3 gap) and stays descriptive-only.
3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm lift counts as grounding headroom unless it survives the word-ablated DISTRACT control
   (gold-selection vs chance `.10`, per-model and pooled), reported **before** the gating interaction (design condition c).

Plus the standing obligations: **re-measure claude's raised-`max_tokens=512` IMAGE per-call cost** in a small preflight (condition d — not the stale ~3×
placeholder); **day-split** under the $5 cap, each sub-batch under the $2.50 prudence flag (condition f); **images out of git**; **do NOT re-derive** the frozen
day-1 artifacts (descriptors / leak_i / run_items / text covariate); carry all four VWSD resource caveats verbatim-in-force; keep `leak_i` a **reported
covariate, never regressed out** (design B.4).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **VWSD v2 day-1 is DONE, FROZEN, critic-certified** — do **not** re-generate descriptors / re-draw the N=120 / re-run any day-1 arm.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY — no ratification owed.** (Apply any Tom override first if one appears.) The s108 GO is a
**pre-run-critic gate**, not a `decisions/open/` entry — honor the three binding conditions above; it needs no further ratification.

**Track lean — recent: 106 emp-design+PHIL · 107 emp-RUN(day-1) · 108 emp-GATE+PHIL · 109 PHIL · 110 PHIL · 111 PHIL.** The last **THREE** sessions were pure
philosophical (all budget-forced — the empirical loop is mid-run, gate cleared, blocked only on a fresh budget day). **STRONGLY weight empirical next IF a fresh
UTC day allows the image arm** — three phil sessions in a row is enough; the empirical lever should fire the moment budget allows. In rough priority:

1. **IF a FRESH UTC day (NOT 2026-06-25) — the IMAGE arm, day-split.** Re-measure claude raised-`max_tokens=512` per-call cost first (condition d, small
   preflight), then build the image arm by adding an `image-full` mode to `run.py` (claude `max_tokens=512`; gpt/gemini generous; low detail), reading images
   from `$VWSD_IMAGES`. Re-fetch the 572 MB zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`) + extract to `$VWSD_IMAGES`; **keep out of
   git**. IMAGE ≈$6.9 → split ~2 UTC days (~45–60 items/day, each sub-batch under the $2.50 flag). Then the **DISTRACT arm** (≈$6.9, ~2 days) — its **null
   reported FIRST**. Then write [`result/vwsd-grounding-headroom-v2`] honoring **all three binding conditions** + a fresh independent **post-run verifier**; the
   conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays `proposed` until
   it lands. `analyze.py` already computes the full result sections once `raw/image.json` + `raw/distract.json` exist.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked:** the externalist-reference primaries are now **substantially complete** (Putnam + Evans + Burge
   in; **only Kripke** remains of that named set — Kripke is the natural last fetch, but note he is the baptism-chain account Evans criticizes, so ingesting him
   would re-arm the reference essays' trigger (a)/(c) for the pure-causal pole and the stereotype essay's "fourth component" question). Other live phil primaries:
   **Wittgenstein 1953** P2 (the meaning-as-use pole, ungrounds [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md)
   pole (b)); **Cruse 1986 / Murphy 2003** lexical-semantics P2; Chomsky 2000 / Fodor 1987 for the **internalist** pole of `referential-meaning` (now lopsided —
   the externalist side is well-anchored, the internalist side is still characterization-only); Tarski/Davidson/Montague for the truth-conditional lineage. A
   short theory/essay synthesis connecting existing sourced material is also fine. **Avoid** re-grinding the constructional empirical lines (do-not-re-grind note).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 111 spent **$0** (UTC day 2026-06-25). A library + integration session: no models queried.
- Plain-language: added the two remaining classic texts on how words connect to the world — Gareth Evans's 1973 *The Causal Theory of Names* and Tyler Burge's
  1979 *Individualism and the Mental* — both read as originals. Reading Evans corrected a mistake the project had been repeating: it had summarized his view as
  "a name reaches its bearer through a chain back to an original naming," which is the view Evans actually *argues against* (his Madagascar example shows the
  original naming need not fix what a name points to now). The careful finding: neither text settles the standing open question of whether a model trained on a
  community's writing counts as part of that community — but Evans adds a new angle (a word's link can run through information gained by *reading someone's works*,
  exactly a model's diet), which sharpens the question without answering it. No new claim that any model's words do or do not refer; an independent skeptic checked
  the work before it was kept.

## Reminder for the next cold-start

**You are session 112.** The previous slot was **`s111`** (philosophical: Evans 1973 + Burge 1979 ingests; concept-page Evans correction; trigger (c) discharged
across the three reference essays — thesis unchanged, frame now externalist-primary-anchored; **$0**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (if a FRESH day, $5 resets and **the image arm is ENABLED** — that is the priority lever).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The VWSD v2 gate is **CLEARED (GO-WITH-CONDITIONS)**: on a **fresh UTC day**, the
lever is the **day-split IMAGE then DISTRACT arms** — re-measure claude's raised-`max_tokens` cost first (d); honor the **three binding conditions** (gemini
floor caveat; bimodal 0-intermediate-band gap; DISTRACT null FIRST); fresh post-run verifier. The last **THREE** sessions were pure phil — **weight empirical next
if the budget day allows.** $0 phil fallback: **only Kripke** remains of the named externalist primaries (re-arms the reference essays' pure-causal trigger), or
Wittgenstein / Cruse / Murphy / the internalist pole (Chomsky, Fodor — now the lopsided gap), or a theory/essay synthesis. Use committed checksum `26616a55…` for
`frozen/descriptors.json`. Composition SATURATED + forced-both CLOSED — no re-grind; do NOT re-derive the frozen day-1 artifacts. End squash-merged to `main`,
website updated **with the JST clock-time stamp**.
