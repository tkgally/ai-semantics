# Pre-run DESIGN review — fresh relation-recovery / taxonomic-proxy probe (H1 + H2)

**Session 192 (2026-07-08).** Design:
[`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../designs/lexical-relation-recovery-taxonomic-proxy-v1.md);
decision opened:
[`decisions/open/lexical-relation-recovery-taxonomic-proxy-design`](../../../wiki/decisions/open/lexical-relation-recovery-taxonomic-proxy-design.md).
This is a **design** pre-run review (PROTOCOL §A3), not a ratification (that is s193+). The design is
GO-WITH-CONDITIONS; nothing is frozen or run.

## Two independent reviews (decorrelated per PROTOCOL §2/§A3)

**(1) Fresh-agent pre-run critic — VERDICT AUTHORITY.** An independent agent (not the s192 orchestrator
that drafted the design) read the design + decision, verified every load-bearing quote against source
pages (essay, pilot note, s186 result, corpus scout, the reused ratified decision), and spot-checked the
s186 `build_cooc.py` construction and `items.json` disjointness.

> **OVERALL: GO-WITH-CONDITIONS. BLOCKERS: none. FABRICATION-CHECK: PASS.**
> Q1 GO-WITH-CONDITIONS · Q2 GO-WITH-CONDITIONS · Q3 GO-WITH-CONDITIONS · Q4 ADOPT internal-contrast-only.
> Faithfulness PASS (H2 is genuinely the essay's across-relation bet; IS-A depth spec + negative sign +
> the ≥2/3 |ρ| rule reproduced verbatim; the pilot's principled refusal of gloss length is respected,
> not reinstated; the Q3 Hearst arm is the corpus construct the pilot *licensed* for the fresh design,
> not the refused echo). Anti-cheat real (fresh disjoint cues; freeze-before-recovery; nulls +
> H1-break/H2-lose pre-named first-class). Every spot-checked quote/number accurate (Spearman −0.086;
> hypernymy best-recovered / meronymy worst; `min_depth` + NEGATIVE sign; the Wikipedia CC BY-SA + C4
> ODC-BY license strings verbatim; s186 = Simple English Wikipedia; nouns-only, n=3 orderings, residual
> arm descriptive-only). Verified the fresh antonymy pool is genuinely capped (~103 in-band fresh after
> excluding the 130 s186 cues).

**(2) Non-Anthropic decorrelation vote** (`openai/gpt-5.4-mini`, cutoff-aware preamble; QA input to the
fresh-agent critic, no verdict authority; `vote.json`, **$0.0035265**):

> **OVERALL: GO-WITH-CONDITIONS.** Q1 C · **Q2 B (dissent — see below)** · Q3 A · Q4 ADOPT
> internal-contrast-only. Reasoned that Q1-C is right *only if* the item-level arm is explicitly
> non-decisive (else "it will quietly become the real test because it has power and prettier
> p-values"); that Q3-A's Hearst arm is legitimately close to the essay's named definitional-frame idea;
> and Q4 is fine as internal-contrast.

**Convergence / divergence.** Both reviewers land **GO-WITH-CONDITIONS**, both independently make the
**Q1** item-level-must-be-non-decisive point the load-bearing condition, and both endorse **Q3-A** and
**Q4 internal-contrast-only**. The one substantive **divergence is Q2**: the non-Anthropic vote picks
**B (C4 primary)** over the design's default **C (Wikipedia primary + C4 sensitivity)**, arguing full
Wikipedia "staying within the encyclopedia family is too close to the original register and weakens the
falsifier for H1"; the fresh-agent critic reaches the same concern from the other side — it keeps C but
binds a **scope-cap** (a Wikipedia-only H1-REPLICATES reading must not be presented as fully discharging
H1's "different corpus" route, and C4 is strongly preferred / at minimum run whenever tractable). **This
Q2 signal is carried to the s193 ratifier to weigh** — it is NOT resolved this session (ratifying a
decision the opening session surfaced is forbidden; PROTOCOL §2).

## The six freeze-time conditions (bound to the freeze; recorded on the design)

All are `prep.py`/PREREG specifications, not gate rewrites — the critic states "no gate is a NO-GO … my
conditions are all freeze-time specifications." They bind the eventual freeze session:

1. **Q1 verdict-of-record binding.** PREREG must state as a hard commitment that the **across-relation
   (n=6) result is the sole verdict of record for H1 and H2**, with the item-level cue-depth arm
   **descriptive/robustness-only** — it can never on its own fire H2 or upgrade an across-relation
   H2-loss to a win. A level-divergence is a pre-named first-class reported outcome.
2. **Close the ρ_cue band gap.** Replace the illustrative "e.g." thresholds with **exhaustive,
   mutually-exclusive** H1 bands over the whole line (no uncovered [+0.3, +0.5] middle), and a **numeric**
   H2 margin for "|ρ_proxy| clearly greater than |ρ_cue|," all fixed before any model call.
3. **Q2 register scope-cap + C4.** If H1 REPLICATES on full-Wikipedia only, the reading carries an
   explicit scope note (**same-source-family corpus, register-decorrelation untested**) and does not
   claim to fully discharge H1's "different control corpus" route; **C4 strongly preferred as
   co-primary, or run whenever tractable**, with a documented reason if deferred. *(Reinforced by the
   non-Anthropic vote's Q2-B dissent.)*
4. **Clarify "byte-frozen."** Byte-identity applies to the **G²/co-occurrence computation** (`FRAME_WIN`,
   connective set, K, weighting, `signed_g2`) — verified unchanged against s186 `build_cooc.py` — while
   the sentence-streaming/IO adapter necessarily changes per corpus format; the IO change must not touch
   any counting/weighting logic.
5. **Q3 multiple-comparison rule + Hearst sign.** IS-A depth is the **primary** proxy, the Hearst-frame
   proxy **secondary**; freeze the Hearst construction (frames, window, weighting) **and its theory-set
   predicted sign** before any corpus counting on the fresh cues; a Hearst-only H2 win (IS-A depth loses)
   is reported as a **qualified/weaker** result, not an equal-status H2-WINS.
6. **Disjointness + fresh-N reporting.** Exclude the exact committed 780 s186 cue lemmas
   (`items.json`, verified) with asserted per-relation 0-overlap; report the achieved fresh per-relation
   N (antonymy expected ~100, capped by WordNet nominal sparsity).

## One construct-validity caveat (scope note, not a gate)

The critic flags that IS-A depth and the recovery-scoring key **share a source** (WordNet) — mitigated
because the pilot uses **cue-first-synset, gold-independent** depth ("a property of the cue, not a
restatement of the answer set"). Carry this as a scope caveat on the eventual result, not a Q4 anchor
issue (Q4 stands as internal-contrast-only).

## Status after this review

Design **GO-WITH-CONDITIONS** → proceeds to **cross-session ratification (s193+)** of the four gates,
then the freeze (honoring conditions 1–6), then the run. `anchor: pending`; conjecture/essay bets
unchanged (H1/H2 stay **open** — they fire only on the run). $0.0035265 (one vote); no probe.
