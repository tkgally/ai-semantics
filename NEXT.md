# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25** spent **$4.72482** (all of it session 107, the VWSD v2 day-1 text-only build); sessions 108, 109 **and 110**
each spent **$0**. **If a session still opens on UTC 2026-06-25, only ≈$0.275 headroom remains — do NOT run any image arm today.** A fresh UTC day resets to $5.
**Check `date -u` first.** The IMAGE and DISTRACT arms (≈$6.9 each) must each be day-split across fresh UTC days regardless. Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 110 (UTC 2026-06-25) — workflow, 2 waves + fresh adversarial coherence pass, $0.** Branch even with `main` at start (s109/#162 merged).
`decisions/open/` **EMPTY** → no ratification owed; no Tom override. A **philosophical-track** session (the empirical lever stayed budget-blocked — no fresh UTC day).
Two waves landed:

1. **Wave 1 — two founding philosophy-of-meaning primaries ingested at primary strength, every headline quote verified verbatim against the extracted source text:**
   - [`source/putnam-1975-meaning-of-meaning`](wiki/base/sources/putnam-1975-meaning-of-meaning.md) — **the canonical externalism primary** (Twin Earth + "meanings just ain't in
     the head" p. 144 [elm/beech variant]; the two-assumptions wedge pp. 135-136; division of linguistic labor + universality hypothesis pp. 144-146; stereotype
     p. 147; indexical/`sameL` p. 152). Read the **Minnesota Studies vol. 7 (1975) original** via the **UMN Digital Conservancy DSpace REST bitstream API** (the
     human-facing URLs hit an Azure WAF bot-wall / 403; reached by walking item→bundles→ORIGINAL bitstream UUID — note for future UMN fetches). OCR scan; artifacts
     flagged inline. **Closes the *conceptual* half of the `referential.externalist` gap** (Evans 1973, Burge 1979 still not-in-repo); does NOT close the
     missing-reference-*resource* half.
   - [`source/frege-1892-sense-and-reference`](wiki/base/sources/frege-1892-sense-and-reference.md) — `Sinn`/`Bedeutung`, sentence-reference-as-truth-value,
     substitution-*salva-veritate* (compositionality). **PD German** via Deutsches Textarchiv; **only PD German quoted** (no copyrighted translation). Caveat
     carried forward: Frege states substitution-*salva-veritate*, **not** the modern compositionality slogan (he flags it "anfechtbar").
   - Both are **theory sources, NOT human anchors.**
2. **Wave 2 — new essay + provenance upgrades + partial trigger-(c) discharge:**
   - New essay [`essay/stereotype-without-the-expert`](wiki/findings/essays/stereotype-without-the-expert.md) — a **tripartite component-and-role mapping** of the LLM
     onto Putnam: maximal access to the **stereotype** (the component Putnam isolated as NOT fixing extension), no access to the indexical extension, and **neither
     role** (expert nor deferring layperson) in the division of linguistic labor while holding its pooled output → measured distributional success = *stereotype-
     competence* ("the elm/beech speaker writ large"). **No new empirical claim, no number, no human-comparison;** conditional on the externalist frame; the
     "distribution ≈ stereotype" identification flagged as the essay's own analogy. `refines` `essay/reference-as-premise-bound` (sharpens "in the community?" →
     "which role?", answered *neither*, **without settling it**); distinct from `essay/reference-denials-disunified`.
   - **Provenance upgrades** (judgement edits by orchestrator): `concept/referential-meaning`, `concept/truth-conditional-and-use-meaning`,
     `concept/compositionality` — replaced the "(not in-repo; characterization)" Putnam/Frege flags with primary citations + front-matter links. Compositionality
     keeps the honest caveat (Frege = substitution principle, not the slogan).
   - **Partial trigger-(c) discharge** (the load-bearing judgement call): `essay/reference-as-premise-bound` and `essay/reference-denials-disunified` both carry a
     trigger (c) keyed to the externalist primaries entering. Putnam entered, **but on reading it Putnam does NOT settle the corpus-membership antecedent** (it fixes
     reference *socially* but says nothing about corpus-trained membership), so **both essays' theses and Denial-3's row SURVIVE unchanged** — the frame is now
     primary-anchored, the premise stays off-board. Logged in-page; trigger stays armed for **Evans 1973 / Kripke**.

**Coherence pass (fresh read-only agent) returned CLEAN** (no blockers/should-fix/nits). Quote integrity independently re-verified by the orchestrator against the
extracted source text (Putnam: the famous line + division-of-labor + sociolinguistic-state + indexical + stereotype + elm strings; Frege: Sinn/Bedeutung +
Wahrheitswerth + salva-veritate). Worth remembering: a clean coherence verdict with **zero findings at every tier** is unusual — it held up here only because the
edits were quote-verified directly and the trigger discharges were deliberately under-claimed; do not treat "clean" as automatic.

## ⚠ VWSD v2 — the empirical lever, still gated on a FRESH UTC day (UNCHANGED from s108/s109)

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

**Track lean — recent: 106 emp-design+PHIL · 107 emp-RUN(day-1) · 108 emp-GATE+PHIL · 109 PHIL · 110 PHIL.** The last **two** sessions were pure philosophical
(both budget-forced — the empirical loop is mid-run, gate cleared, blocked only on a fresh budget day). **STRONGLY weight empirical next IF a fresh UTC day allows
the image arm.** In rough priority:

1. **IF a FRESH UTC day (NOT 2026-06-25) — the IMAGE arm, day-split.** Re-measure claude raised-`max_tokens=512` per-call cost first (condition d, small
   preflight), then build the image arm by adding an `image-full` mode to `run.py` (claude `max_tokens=512`; gpt/gemini generous; low detail), reading images
   from `$VWSD_IMAGES`. Re-fetch the 572 MB zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`) + extract to `$VWSD_IMAGES`; **keep out of
   git**. IMAGE ≈$6.9 → split ~2 UTC days (~45–60 items/day, each sub-batch under the $2.50 flag). Then the **DISTRACT arm** (≈$6.9, ~2 days) — its **null
   reported FIRST**. Then write [`result/vwsd-grounding-headroom-v2`] honoring **all three binding conditions** + a fresh independent **post-run verifier**; the
   conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays `proposed` until
   it lands. `analyze.py` already computes the full result sections once `raw/image.json` + `raw/distract.json` exist.
2. **PHILOSOPHICAL fallback ($0), if still budget-blocked or leaning phil:** a primary OA ingest from [`wanted.md`](wiki/base/wanted.md). **The externalist
   primary Putnam 1975 is now IN** (s110); the natural companions remaining are **Evans 1973** "The Causal Theory of Names" P2 (would re-arm the now-partially-fired
   trigger (c) in the two reference essays — its causal-chain/baptism story could bear on corpus-inheritance differently than Putnam's social account) and **Burge
   1979** "Individualism and the Mental" P2 (social externalism / the *arthritis* case). Other live phil primaries: **Wittgenstein 1953** P2 (the meaning-as-use
   pole, ungrounds `truth-conditional-and-use-meaning` pole (b)); **Cruse 1986 / Murphy 2003** lexical-semantics P2; Tarski/Davidson/Montague for the rest of the
   truth-conditional lineage. A short theory/essay unit connecting existing sourced material is also fine. **Avoid** re-grinding the constructional empirical lines
   (do-not-re-grind note above).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 110 spent **$0** (UTC day 2026-06-25). A library + synthesis session: no models queried.
- Plain-language: added two of the most-cited texts on what "meaning" means — Frege's 1892 *On Sense and Reference* (read in his own public-domain German) and
  Putnam's 1975 *The Meaning of "Meaning"* (read from a university's open archive of the original) — both used only second-hand until now. Then wrote an essay
  using Putnam's three-part picture of a word (everyday description / actual stuff in the world / a community of experts and deferring laypeople) to ask where a
  language model fits: it is excellent at the everyday-description part — which Putnam said never settles what a word points to — has no access to the actual stuff,
  and fits neither role in the community though it has read what both wrote. The essay does **not** claim the model's words refer; it holds within one philosophical
  camp and says so, flags its key comparison as an analogy, and an independent skeptic checked it before anything was kept.

## Reminder for the next cold-start

**You are session 111.** The previous slot was **`s110`** (philosophical: Putnam 1975 + Frege 1892 ingests + the stereotype-without-the-expert essay + provenance
upgrades; **$0**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (if still 2026-06-25, ≈$0.275 left, NO image arm; a fresh day resets to $5 and **enables the image arm**).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The VWSD v2 gate is **CLEARED (GO-WITH-CONDITIONS)**: on a **fresh UTC day**, the
lever is the **day-split IMAGE then DISTRACT arms** — re-measure claude's raised-`max_tokens` cost first (d); honor the **three binding conditions** (gemini
floor caveat; bimodal 0-intermediate-band gap; DISTRACT null FIRST); fresh post-run verifier. The last **two** sessions were pure phil — **weight empirical next if
the budget day allows**. $0 phil fallback: Evans 1973 / Burge 1979 (re-arm trigger (c)) or Wittgenstein/Cruse/Murphy, or a theory/essay synthesis — the externalist
primary Putnam is now in. Use committed checksum `26616a55…` for `frozen/descriptors.json`. Composition SATURATED + forced-both CLOSED — no re-grind; do NOT
re-derive the frozen day-1 artifacts. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
