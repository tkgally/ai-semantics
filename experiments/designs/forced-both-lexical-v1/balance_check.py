#!/usr/bin/env python3
"""Q1-ii independent (not-model-based) balance check for the forced-both lexical build.

The resolved gate (decisions/resolved/forced-both-lexical-operationalization, Q1-ii) requires,
on top of the zeugma/co-predication structural frame (Q1-i), an INDEPENDENT (not model-based)
check that *neither sense dominates* — otherwise a forced-both frame can still LEAN, and a lean
suppresses UNCLEAR (within-lexical caveat 2), biasing spuriously toward commit / reading (A).

The only in-repo / reachable corpus signal that decomposes word frequency BY SENSE is the
SemCor sense-tagged corpus, surfaced through WordNet lemma tag counts (resource/wordnet-sense-
inventory; SemCor underlies WordNet's frequency-ordered senses). SUBTLEX (resource/subtlex-us-
frequency) is word-level only; DWUG (resource/dwug-usage-graphs) "does not tag pairs as polysemy
vs. homonymy" and gives no per-sense frequency. So SemCor-via-WordNet is the candidate Q1-ii
instrument.

This script applies it to the candidate items and reports, per item, the two target senses'
SemCor tag counts and a balance ratio min/(a+b). A 'certifiable-balanced' item would need BOTH
counts non-trivial (enough tags to have any power) AND a ratio near 0.5. The output is read by
README.md, which records the trigger-(c) verdict.

Run: python3 balance_check.py   (requires nltk + the 'wordnet' corpus; pip install nltk;
python3 -c "import nltk; nltk.download('wordnet')").
No API, no model call.
"""
import json
import os
from nltk.corpus import wordnet as wn

HERE = os.path.dirname(os.path.abspath(__file__))

# candidate word -> (synset_a, synset_b) ; the two UNRELATED homonym senses the co-predication
# frame in candidate_items.json yokes together.
SENSE_MAP = {
    "bank":   ("bank.n.01", "depository_financial_institution.n.01"),
    "club":   ("club.n.03", "club.n.02"),
    "pen":    ("pen.n.02", "pen.n.01"),
    "file":   ("file.n.01", "file.n.02"),
    "pitch":  ("football_field.n.01", "pitch.n.02"),
    "seal":   ("seal.n.02", "seal.n.01"),
    "bark":   ("bark.n.02", "bark.n.01"),
    "spring": ("spring.n.02", "spring.n.01"),
}

# minimum SemCor tags on EACH sense for the balance ratio to carry any power at all.
MIN_TAGS_FOR_POWER = 5


def lemma_count(synset_name, word):
    """SemCor tag count for the lemma of `synset_name` that surfaces as `word` (fallback: first lemma)."""
    syn = wn.synset(synset_name)
    matching = [l for l in syn.lemmas() if l.name().lower() == word.lower()]
    if matching:
        return sum(l.count() for l in matching)
    return sum(l.count() for l in syn.lemmas())


def main():
    results = []
    for word, (sa, sb) in SENSE_MAP.items():
        na = lemma_count(sa, word)
        nb = lemma_count(sb, word)
        tot = na + nb
        ratio = (min(na, nb) / tot) if tot > 0 else None
        powered = (na >= MIN_TAGS_FOR_POWER and nb >= MIN_TAGS_FOR_POWER)
        # "balanced" only if powered AND ratio within [0.40, 0.60]
        balanced = bool(powered and ratio is not None and 0.40 <= ratio <= 0.60)
        results.append({
            "word": word,
            "synset_a": sa, "count_a": na,
            "synset_b": sb, "count_b": nb,
            "total_tags": tot,
            "balance_ratio_min_over_total": round(ratio, 3) if ratio is not None else None,
            "powered_each_sense_ge_%d" % MIN_TAGS_FOR_POWER: powered,
            "certifiable_balanced": balanced,
        })

    n_balanced = sum(r["certifiable_balanced"] for r in results)
    n_powered = sum(r["powered_each_sense_ge_%d" % MIN_TAGS_FOR_POWER] for r in results)
    summary = {
        "wordnet_version_note": "WordNet 3.0 via NLTK; SemCor tag counts (lemma.count()).",
        "min_tags_for_power": MIN_TAGS_FOR_POWER,
        "balanced_band": [0.40, 0.60],
        "n_candidates": len(results),
        "n_with_power_each_sense": n_powered,
        "n_certifiable_balanced": n_balanced,
        "verdict": (
            "Q1-ii NOT satisfiable from SemCor: only %d/%d candidates have >= %d tags on BOTH "
            "senses (the rest are statistically powerless), and SemCor measures GENERAL-USAGE "
            "balance, not the balance of the constructed co-predication sentence. See README.md."
            % (n_powered, len(results), MIN_TAGS_FOR_POWER)
        ),
        "items": results,
    }
    out = os.path.join(HERE, "balance_check.json")
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
