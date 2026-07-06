#!/usr/bin/env python3
"""Non-Anthropic decorrelation votes for the TWO s183-opened decisions being ratified s184.
Routed via the probe REST path (openrouter.py) per PROTOCOL 2 (decorrelation rule).
Model: openai/gpt-5.4-mini (non-Anthropic w.r.t. the harness reviewer + the fresh-agent reviewers).
Each vote is QA INPUT to a fresh-agent reviewer, which keeps verdict authority. Cutoff-aware preamble.
"""
import os, sys, json, time
sys.path.insert(0, "/home/user/ai-semantics/experiments/lib")
from openrouter import call, billed_cost

RUNDIR = "/home/user/ai-semantics/experiments/runs/2026-07-06-s184-ratification-votes"

PREAMBLE = ("Today is 2026-07-06. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.\n\n"
            "You are an independent, adversarial reviewer for an autonomous research project on "
            "LLM semantics. You are adjudicating a METADATA/CONVENTION decision (not a research "
            "finding). You are ONE decorrelation vote; a separate reviewer holds final authority. "
            "Be skeptical and concrete. Ratification fixes the yardstick, never a result — flag "
            "any sign the rule is motivated by wanting a different empirical result.")

VOTE_FORMAT = ("\n\nAnswer EXACTLY in this format:\n"
               "VERDICT: <ADOPT-A | ADOPT-B | ADOPT-C | KEEP-OPEN>\n"
               "REASONS: <2-5 sentences, concrete>\n"
               "CONDITIONS: <numbered, only if any; else 'none'>")

D1 = """DECISION 1 — "result-status-upgrade-semantics".

The project's page schema gives RESULT pages a status vocabulary {proposed | supported |
contested | retired} but never wrote a TRANSITION RULE. Practice diverged silently:
- ~13 result pages carry `status: supported` SELF-ASSIGNED at creation with no in-page promotion
  or replication record (mostly $0 mechanical "gate"/"calibration" pages, plus some function-word
  pages).
- Meanwhile the project's THRICE-REPLICATED flagship results (comparative-correlative, AANN
  gradient, dative info-structure) sit at `status: proposed`, each explicitly stating that what is
  `proposed` is the *reading/interpretation*, not the measured numbers.
- The operative THEORY pages (two "-v2" second editions + the flagship table) all carry
  `status: draft`, though the theory vocabulary offers `live`.

Nothing here changes any finding; it is pure status semantics, but status fields steer readers and
future promotion reviews.

OPTIONS:
A (provisional default): result `status` describes the READING's lifecycle; only a RECORDED DATED
  EVENT moves it (a replication, a promotion review citing it, or a contested/retired call).
  `supported`-at-creation is deprecated going forward. The ~13 existing pages each get a one-line
  dated normalization note AT THE NEXT TOUCH of that page (no mass edit now) — the note may keep
  `supported` (e.g. a mechanical gate whose "support" is a check that passed) or set `proposed`.
  Theory syntheses may move draft->live at their next substantive touch; a `live` page that gains a
  `supersedes` successor becomes `superseded`.
B: freeze all statuses; only DOCUMENT the two observed conventions in the schema file (describe,
  don't normalize). Cheapest; leaves the flagship-vs-gate inversion standing.
C: mass-normalize now — all un-promoted results -> `proposed` in one sweep. Cleanest graph, but
  rewrites ~13 pages without per-page judgement, and a gate page's `supported` arguably IS the right
  description of a mechanical check that passed.

Which option should be ratified, and why?"""

D2 = """DECISION 2 — "meaning-senses-methodology-tags".

The project maintains a CONTROLLED VOCABULARY of "meaning-senses" (distributional, referential,
inferential, grounded, constructional, functional-vs-formal, model-internal, relational,
human-comparison). Every findings/ page must tag >=1; the vocabulary page instructs: "If the sense
you mean is not in this list, propose an addition in decisions/open/ rather than inventing a tag
inline." A mechanical linter enforces the vocabulary on findings/ pages ONLY, not on base/ pages.

Six base/sources/ pages nonetheless carry tags NOT in the vocabulary — `operational` on five
measurement-methodology ingests (Cronbach & Meehl, Messick, Campbell & Fiske, Borsboom,
Freiesleben) and `methodological` on one (Hitchcock & Redei). They passed silently because the
linter skips base/. These pages are about MEASUREMENT ITSELF (construct validity, operationalization,
instrument competence) — not about a sense of *meaning*. The vocabulary describes senses OF meaning;
none currently covers "the measurement of meaning".

OPTIONS:
A (provisional default): add ONE new tag `measurement-epistemic` to the controlled vocabulary
  ("about the measurement of meaning rather than a sense of meaning: operationalization, construct
  validity, instrument competence"). Retag the six pages operational/methodological ->
  measurement-epistemic (mechanical; their other tags stay). One new tag; some methodology essays
  gain a legitimate co-tag.
B: add BOTH existing strings (`operational`, `methodological`) to the vocabulary as-is. Zero
  retagging, but two near-synonyms enter the controlled list.
C: retag the six using only existing vocabulary (e.g. drop the tags — they are optional on base/
  pages). Cheapest, but loses the real information that these six are a distinct kind.

A subtlety the decision NOTES but explicitly does NOT decide: the vocabulary already has four
documented sub-tags with zero uses, and the linter accepts any `known-prefix.suffix` string, so
sub-tag control is loose. Should ratification bundle that, or leave it to a later vocabulary touch?

Which option should be ratified, and why? Consider whether adding a tag that is explicitly NOT a
sense of meaning, into a controlled vocabulary of senses of meaning, is coherent."""

def cast(tag, body):
    r = call("openai/gpt-5.4-mini", PREAMBLE, body + VOTE_FORMAT, max_tokens=800, temperature=0)
    print(f"\n===== {tag} CONTENT =====")
    print(r.get("content"))
    print(f"===== {tag} ERROR =====", r.get("error"))
    json.dump({"ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               "decision": tag, "model": "openai/gpt-5.4-mini",
               "content": r.get("content"), "error": r.get("error"), "usage": r.get("usage")},
              open(f"{RUNDIR}/vote_{tag}.json", "w"), indent=1)
    return r

def main():
    r1 = cast("result-status", D1)
    r2 = cast("meaning-senses-tags", D2)
    total, have, missing = billed_cost([[r1], [r2]])
    print(f"\n===== TOTAL billed usage.cost: ${total:.6f} (have={have} missing={missing}) =====")

if __name__ == "__main__":
    main()
