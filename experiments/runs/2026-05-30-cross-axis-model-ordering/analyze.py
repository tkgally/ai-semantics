"""Cross-axis model-ordering re-analysis (2026-05-30). Pure-Python, NO API, $0.

Question (NEXT.md backlog unit 3): does each panel model's LEXICAL gradience strength
(result/lexical-sense-gradience-v1) predict its CONSTRUCTIONAL performance across the
project's own-design grammatical results? Early sign from the bridge result was "no"
(gemini strongest lexically yet least coercion-sensitive). This makes it a typed finding.

This is a TABULATION of numbers already on the in-repo result pages (each value is
provenance-tagged to its source page below) + rank correlations across the panel of three.
It introduces NO new data and queries NO model. With only n=3 models a Spearman is a blunt
instrument (only a handful of distinct orderings exist) — it is reported as a descriptive
ordering check with the exact rank pattern, NOT a significance test.

PANEL order fixed: claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash.
"""
import json
import math
import os
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = ["claude", "gpt-5.4-mini", "gemini"]

# --- LEXICAL predictor: Spearman rho vs human DURel median (result/lexical-sense-gradience-v1) ---
LEXICAL = {  # durel framing rho (primary); cont in parens on the page
    "claude": 0.679, "gpt-5.4-mini": 0.601, "gemini": 0.804,
}
LEXICAL_CONT = {"claude": 0.696, "gpt-5.4-mini": 0.675, "gemini": 0.825}

# --- CONSTRUCTIONAL outcomes, per model. Each dict is one result page's headline per-model
# number, with `metric`, `source` (result id), and `direction` (+1 = higher is more competent,
# for ranking). Ceiling-for-all rows are flagged ceiling=True and excluded from rank correlation
# (no discriminating order). Values quoted from the result pages (see README provenance table).
CONSTRUCTIONAL = {
    # add-direction Tier-4 positives — at/near ceiling
    "caused-motion-v1 (affirm%, FC)": {
        "vals": {"claude": 100, "gpt-5.4-mini": 90, "gemini": 100},
        "metric": "affirm caused-motion rate %, forced-choice", "ceiling": True,
        "source": "result/caused-motion-minimal-pair-divergence-v1"},
    "way-v1 (affirm%, FC)": {
        "vals": {"claude": 100, "gpt-5.4-mini": 77.8, "gemini": 94.4},
        "metric": "affirm path-traversal rate %, forced-choice", "ceiling": False,
        "source": "result/way-construction-traversal-v1"},
    "conative-v1 (gap pp, FC)": {
        "vals": {"claude": 67, "gpt-5.4-mini": 42, "gemini": 88},
        "metric": "transitive-conative completed-contact gap pp, forced-choice", "ceiling": False,
        "source": "result/conative-minimal-pair-divergence-v1"},
    "conative-v1 (gap pp, NLI)": {
        "vals": {"claude": 54, "gpt-5.4-mini": -8, "gemini": 67},
        "metric": "transitive-conative gap pp, NLI", "ceiling": False,
        "source": "result/conative-minimal-pair-divergence-v1"},
    "CC-v1 (gap pp)": {
        "vals": {"claude": 87.5, "gpt-5.4-mini": 90.0, "gemini": 80.0},
        "metric": "CC covariation vs control gap pp", "ceiling": True,
        "source": "result/comparative-correlative-covariation-v1"},
    "cxnli-distinction (drop pp; LOWER=better)": {
        "vals": {"claude": -30, "gpt-5.4-mini": -45, "gemini": -41},
        "metric": "base->distinction accuracy drop pp (less negative = better)", "ceiling": False,
        "source": "result/cxnli-distinction-divergence-v1"},
    "conative-cancel-v2 (suppress%, FC)": {
        "vals": {"claude": 66.7, "gpt-5.4-mini": 33.3, "gemini": 83.3},
        "metric": "conative suppression-no-cue %, forced-choice", "ceiling": False,
        "source": "result/conative-cancel-direction-v2"},
    "coercion-implicit-v2b (impossible-affirm%, FC; LOWER=more world-knowledge)": {
        "vals": {"claude": 90, "gpt-5.4-mini": 40, "gemini": 100},
        "metric": "affirm physically-impossible coercion %, FC (lower = more WK engagement)",
        "ceiling": False, "source": "result/coercion-implicit-cue-v2b"},
    "CC-v3 (operator-correct%, FC)": {
        "vals": {"claude": 100, "gpt-5.4-mini": 60, "gemini": 100},
        "metric": "operator-scope-correct %, FC (negation/hedge embedding)", "ceiling": False,
        "source": "result/comparative-correlative-covariation-v3"},
    "caused-motion-near-miss-v2c (gap pp, FC)": {
        "vals": {"claude": 68.8, "gpt-5.4-mini": 62.5, "gemini": 100.0},
        "metric": "construction-vs-near-miss causation gap pp, FC", "ceiling": False,
        "source": "result/caused-motion-near-miss-v2c"},
    # THE BRIDGE — the discriminating cross-axis datum
    "coercion-sense-modulation-v1 (gap cont)": {
        "vals": {"claude": 31.4, "gpt-5.4-mini": 20.5, "gemini": 8.3},
        "metric": "coercion sense-shift gap (control-elab - coerced), 0-100", "ceiling": False,
        "source": "result/coercion-sense-modulation-v1"},
}


def ranks(z):
    order = sorted(range(len(z)), key=lambda i: z[i])
    r = [0.0] * len(z)
    i = 0
    while i < len(z):
        j = i
        while j + 1 < len(z) and z[order[j + 1]] == z[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y))
    vx = math.sqrt(sum((a - mx) ** 2 for a in x))
    vy = math.sqrt(sum((b - my) ** 2 for b in y))
    return cov / (vx * vy) if vx and vy else 0.0


def spearman(x, y):
    return pearson(ranks(x), ranks(y))


def order_str(d):
    return " > ".join(sorted(d, key=lambda k: -d[k]))


def main():
    lex = [LEXICAL[m] for m in MODELS]
    lex_order = order_str(LEXICAL)
    out = {"panel": MODELS,
           "lexical_predictor_durel": LEXICAL, "lexical_predictor_cont": LEXICAL_CONT,
           "lexical_order": lex_order,
           "note": "n=3 models: Spearman is descriptive only (few distinct orderings); "
                   "report the exact rank pattern. Ceiling-for-all rows excluded from rho.",
           "per_result": {}}
    print(f"\n===== CROSS-AXIS MODEL-ORDERING (n=3 models) =====")
    print(f"LEXICAL predictor (durel rho): {LEXICAL}  order: {lex_order}\n")
    rhos = []
    for name, info in CONSTRUCTIONAL.items():
        cvals = [info["vals"][m] for m in MODELS]
        rho = spearman(lex, cvals)
        co = order_str(info["vals"])
        agree = "CEILING" if info["ceiling"] else ("MATCH" if co == lex_order else "DIVERGE")
        out["per_result"][name] = {"vals": info["vals"], "order": co,
                                   "rho_vs_lexical": round(rho, 3),
                                   "ceiling_for_all": info["ceiling"],
                                   "lexical_order_agreement": agree,
                                   "metric": info["metric"], "source": info["source"]}
        if not info["ceiling"]:
            rhos.append(rho)
        print(f"  {name:<52} order: {co:<34} rho={rho:+.2f}  [{agree}]")
    # summary across discriminating (non-ceiling) results
    if rhos:
        mean_rho = sum(rhos) / len(rhos)
        n_match = sum(1 for v in out["per_result"].values()
                      if v["lexical_order_agreement"] == "MATCH")
        n_div = sum(1 for v in out["per_result"].values()
                    if v["lexical_order_agreement"] == "DIVERGE")
        n_ceil = sum(1 for v in out["per_result"].values()
                     if v["lexical_order_agreement"] == "CEILING")
        out["summary"] = {
            "n_results": len(CONSTRUCTIONAL), "n_ceiling_excluded": n_ceil,
            "n_discriminating": len(rhos),
            "mean_rho_vs_lexical (discriminating)": round(mean_rho, 3),
            "n_order_match": n_match, "n_order_diverge": n_div,
            "gpt_is_weakest_lexically": LEXICAL["gpt-5.4-mini"] == min(LEXICAL.values()),
            "bridge_inverts": (order_str(CONSTRUCTIONAL["coercion-sense-modulation-v1 (gap cont)"]["vals"])
                               != lex_order),
        }
        print(f"\n  mean rho (lexical vs constructional, {len(rhos)} discriminating results) "
              f"= {mean_rho:+.3f}")
        print(f"  order MATCH={n_match}  DIVERGE={n_div}  CEILING(excluded)={n_ceil}")
        print(f"  bridge (coercion-sense-modulation) order = "
              f"{order_str(CONSTRUCTIONAL['coercion-sense-modulation-v1 (gap cont)']['vals'])} "
              f"(lexical order = {lex_order}) -> "
              f"{'INVERTS' if out['summary']['bridge_inverts'] else 'matches'}")
    json.dump(out, open(os.path.join(HERE, "raw", "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(HERE, 'raw', 'results.json')}")


if __name__ == "__main__":
    main()
