"""Instrument-disagreement re-analysis (2026-05-30).

READ-ONLY re-analysis of two parent runs; NO new API calls, $0.00 spend.

For each model x construction/condition x instrument, we compute:
  - The affirm rate (= affirm-contact for conative, affirm-inference for coercion v2)
  - The KEY gap: transitive-conative gap (conative run) or canonical-cue drop (coercion run)
  - The instrument-disagreement statistic:
      signed disagreement  = NLI_gap - FC_gap   (positive => NLI shows larger gap)
      absolute disagreement = |NLI_gap - FC_gap| (magnitude regardless of direction)

For the coercion v2 run the "gap" is the canonical-minus-cue drop,
which is the construction's core discriminator (parallel to the conative gap).

Sanity-check targets (from parent result pages):
  conative FC gaps:  42-88 pp  (3/3 models)
  conative NLI gaps: 54-67 pp  (2/3 models; gpt NLI = -8 pp)

Arithmetic is entirely from the committed raw/results.json files in each parent run.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.abspath(os.path.join(HERE, ".."))

CONATIVE_RESULTS = os.path.join(
    RUNS_DIR,
    "2026-05-29-conative-minimal-pair-probe-v1",
    "raw", "results.json"
)
COERCION_RESULTS = os.path.join(
    RUNS_DIR,
    "2026-05-29-argument-structure-coercion-probe-v2",
    "raw", "results.json"
)

PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
MODEL_SHORT = {
    "claude-sonnet-4.6": "claude",
    "gpt-5.4-mini": "gpt",
    "gemini-3.5-flash": "gemini",
}

# ── helpers ─────────────────────────────────────────────────────────────────

def sgn(x):
    """Return '+' / '-' / ' 0' prefix for display."""
    if x is None:
        return "None"
    return f"+{x:.1f}" if x >= 0 else f"{x:.1f}"


def absdiff(a, b):
    if a is None or b is None:
        return None
    return abs(a - b)


def signed(a, b):
    """NLI_gap - FC_gap."""
    if a is None or b is None:
        return None
    return round(a - b, 1)


# ── load parent results ─────────────────────────────────────────────────────

def load_conative():
    """Return per-model NLI and FC gaps for the conative run.

    The parent gap is:  transitive_affirm - conative_affirm (pp)
    Positive => construction-class gap is present.
    """
    data = json.load(open(CONATIVE_RESULTS))
    rows = {}
    for slot, name in PANEL.items():
        pm = data["per_model"][slot]
        assert pm["model"] == name, f"unexpected model name: {pm['model']}"
        nli_gap = pm["nli"]["gap_pp"]   # conative-class gap under NLI
        fc_gap  = pm["fc"]["gap_pp"]    # conative-class gap under FC
        rows[name] = {
            "nli_trans": pm["nli"]["transitive_affirm"],
            "nli_conative": pm["nli"]["conative_affirm"],
            "nli_gap": nli_gap,
            "fc_trans": pm["fc"]["transitive_affirm"],
            "fc_conative": pm["fc"]["conative_affirm"],
            "fc_gap": fc_gap,
            "signed_disagree": signed(nli_gap, fc_gap),
            "abs_disagree": round(absdiff(nli_gap, fc_gap), 1),
        }
    return rows


def load_coercion():
    """Return per-model x per-construction NLI and FC drops (canonical-minus-cue).

    The "gap" used here = canonical_minus_cue_drop, which is the main discriminator
    in the coercion v2 result page (parallel role to the conative gap).
    """
    data = json.load(open(COERCION_RESULTS))
    rows = {}
    for slot, name in PANEL.items():
        pm = data["per_model"][slot]
        assert pm["model"] == name, f"unexpected model name: {pm['model']}"
        rows[name] = {}
        for con in ("caused-motion", "way"):
            nli = pm[f"{con}_nli"]
            fc  = pm[f"{con}_fc"]
            nli_drop = nli["canonical_minus_cue_drop"]
            fc_drop  = fc["canonical_minus_cue_drop"]
            nli_canon = nli["canonical"]
            fc_canon  = fc["canonical"]
            nli_cue   = nli["cue"]
            fc_cue    = fc["cue"]
            rows[name][con] = {
                "nli_canon": nli_canon,
                "nli_cue":   nli_cue,
                "nli_drop":  nli_drop,
                "fc_canon":  fc_canon,
                "fc_cue":    fc_cue,
                "fc_drop":   fc_drop,
                "signed_disagree": signed(nli_drop, fc_drop),
                "abs_disagree": round(absdiff(nli_drop, fc_drop), 1),
            }
    return rows


# ── sanity check ─────────────────────────────────────────────────────────────

def sanity_check_conative(con_rows):
    """Verify recomputed gaps match the parent result page's stated ranges.

    The parent page rounds displayed values: e.g. raw 41.7 pp appears as "42 pp".
    We check against raw value ranges, allowing ±0.5 pp for display rounding.
    Parent page states: FC gaps 42-88 pp (3/3); NLI gaps 54-67 pp (2/3);
    gpt NLI gap = -8 pp (stated as ~-8 pp, raw = -8.3 pp).
    """
    errors = []
    for name, r in con_rows.items():
        fc = r["fc_gap"]
        nli = r["nli_gap"]
        short = MODEL_SHORT[name]
        # All 3 models FC gap: parent says 42-88 pp; raw gpt value is 41.7 (rounds to 42)
        # Allow >=41.5 to accommodate rounding of the stated lower bound of 42
        if not (41.5 <= fc <= 88.5):
            errors.append(f"SANITY FAIL: {short} FC gap={fc:.1f} pp, expected 42-88 pp range "
                          f"(41.5-88.5 after rounding allowance)")
        # NLI: claude and gemini in 54-67; gpt at -8 (raw -8.3)
        if short == "gpt":
            if not (-10 <= nli <= -6):
                errors.append(f"SANITY FAIL: {short} NLI gap={nli:.1f} pp, expected ~-8 pp")
        else:
            if not (54 <= nli <= 67.5):
                errors.append(f"SANITY FAIL: {short} NLI gap={nli:.1f} pp, expected 54-67 pp")
    return errors


def sanity_check_coercion(cor_rows):
    """Verify recomputed drops are internally consistent (all 0-100 pp range)."""
    errors = []
    for name, cons in cor_rows.items():
        for con, r in cons.items():
            for instr in ("nli", "fc"):
                drop = r[f"{instr}_drop"]
                if drop is None or not (0 <= drop <= 100):
                    errors.append(
                        f"SANITY FAIL: {MODEL_SHORT[name]} {con} {instr.upper()} "
                        f"drop={drop}, expected 0-100 pp"
                    )
    return errors


# ── pretty tables ──────────────────────────────────────────────────────────

def fmt_conative_table(con_rows):
    """Return the main conative instrument-disagreement table as a markdown string."""
    lines = []
    lines.append("## Table 1: Conative probe — instrument disagreement on the transitive−conative gap")
    lines.append("")
    lines.append("The 'gap' is the transitive_affirm − conative_affirm difference (pp). "
                 "Signed = NLI_gap − FC_gap; abs = |NLI_gap − FC_gap|.")
    lines.append("")
    lines.append("| model | NLI trans | NLI conative | NLI gap | FC trans | FC conative | FC gap | "
                 "signed (NLI−FC) | abs |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for name, r in con_rows.items():
        short = MODEL_SHORT[name]
        lines.append(
            f"| {short} "
            f"| {r['nli_trans']:.1f}% "
            f"| {r['nli_conative']:.1f}% "
            f"| {r['nli_gap']:+.1f} pp "
            f"| {r['fc_trans']:.1f}% "
            f"| {r['fc_conative']:.1f}% "
            f"| {r['fc_gap']:+.1f} pp "
            f"| {r['signed_disagree']:+.1f} pp "
            f"| {r['abs_disagree']:.1f} pp |"
        )
    return "\n".join(lines)


def fmt_coercion_table(cor_rows):
    """Return the coercion v2 instrument-disagreement table as a markdown string."""
    lines = []
    lines.append("## Table 2: Coercion v2 — instrument disagreement on the canonical−cue drop")
    lines.append("")
    lines.append("The 'drop' is the canonical_minus_cue_drop (pp). "
                 "Signed = NLI_drop − FC_drop; abs = |NLI_drop − FC_drop|.")
    lines.append("")
    lines.append("| model | construction | NLI canon | NLI cue | NLI drop | "
                 "FC canon | FC cue | FC drop | signed (NLI−FC) | abs |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for name, cons in cor_rows.items():
        short = MODEL_SHORT[name]
        for con, r in cons.items():
            lines.append(
                f"| {short} "
                f"| {con} "
                f"| {r['nli_canon']:.1f}% "
                f"| {r['nli_cue']:.1f}% "
                f"| {r['nli_drop']:+.1f} pp "
                f"| {r['fc_canon']:.1f}% "
                f"| {r['fc_cue']:.1f}% "
                f"| {r['fc_drop']:+.1f} pp "
                f"| {r['signed_disagree']:+.1f} pp "
                f"| {r['abs_disagree']:.1f} pp |"
            )
    return "\n".join(lines)


def fmt_summary_table(con_rows, cor_rows):
    """Return a compact summary of absolute disagreement per model x construction."""
    lines = []
    lines.append("## Table 3: Summary — absolute instrument disagreement (|NLI gap − FC gap|) per cell")
    lines.append("")
    lines.append("| model | construction | run | NLI gap | FC gap | abs disagree |")
    lines.append("|---|---|---|---:|---:|---:|")
    for name, r in con_rows.items():
        short = MODEL_SHORT[name]
        lines.append(
            f"| {short} | conative | conative-v1 "
            f"| {r['nli_gap']:+.1f} pp "
            f"| {r['fc_gap']:+.1f} pp "
            f"| {r['abs_disagree']:.1f} pp |"
        )
    for name, cons in cor_rows.items():
        short = MODEL_SHORT[name]
        for con, r in cons.items():
            lines.append(
                f"| {short} | {con} | coercion-v2 "
                f"| {r['nli_drop']:+.1f} pp "
                f"| {r['fc_drop']:+.1f} pp "
                f"| {r['abs_disagree']:.1f} pp |"
            )
    return "\n".join(lines)


# ── main ───────────────────────────────────────────────────────────────────

def main():
    print("\n=== INSTRUMENT DISAGREEMENT RE-ANALYSIS (2026-05-30) ===")
    print("Read-only re-analysis of two parent runs — no new API calls, $0.00 spend.\n")

    con_rows = load_conative()
    cor_rows = load_coercion()

    # ── sanity checks ──────────────────────────────────────────────────────
    print("--- Sanity checks (must pass before proceeding) ---")
    errors = sanity_check_conative(con_rows) + sanity_check_coercion(cor_rows)
    if errors:
        print("STOP — sanity check failures:")
        for e in errors:
            print(" ", e)
        raise SystemExit(1)
    print("  All sanity checks PASSED — recomputed numbers reconcile with parent result pages.\n")

    # ── print tables ───────────────────────────────────────────────────────
    t1 = fmt_conative_table(con_rows)
    t2 = fmt_coercion_table(cor_rows)
    t3 = fmt_summary_table(con_rows, cor_rows)

    print(t1)
    print()
    print(t2)
    print()
    print(t3)

    # ── narrative summary ──────────────────────────────────────────────────
    print("\n--- Narrative summary ---")
    print("Conative run:")
    for name, r in con_rows.items():
        short = MODEL_SHORT[name]
        print(f"  {short:7s}: NLI gap={r['nli_gap']:+.1f}pp  FC gap={r['fc_gap']:+.1f}pp  "
              f"abs_disagree={r['abs_disagree']:.1f}pp  signed(NLI-FC)={r['signed_disagree']:+.1f}pp")
    print("Coercion v2:")
    for name, cons in cor_rows.items():
        short = MODEL_SHORT[name]
        for con, r in cons.items():
            print(f"  {short:7s} {con:13s}: NLI drop={r['nli_drop']:+.1f}pp  FC drop={r['fc_drop']:+.1f}pp  "
                  f"abs_disagree={r['abs_disagree']:.1f}pp  signed(NLI-FC)={r['signed_disagree']:+.1f}pp")

    # ── write markdown table file ──────────────────────────────────────────
    md_path = os.path.join(HERE, "instrument-disagreement-table.md")
    header = (
        "# Instrument-disagreement table\n\n"
        "Recomputed 2026-05-30 by `analyze.py` from the committed `raw/results.json` "
        "of the two parent runs. No new API calls; $0.00 spend.\n\n"
        "**Parent runs:**\n"
        "- `experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/` "
        "(git commit `acbcdc4`)\n"
        "- `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/` "
        "(git commit `1f27d92`)\n\n"
        "All figures are recomputed from the raw JSON; arithmetic shown in "
        "[Table 1](#table-1) and [Table 2](#table-2); "
        "[Table 3](#table-3) is the compact summary.\n\n"
    )
    with open(md_path, "w") as fh:
        fh.write(header)
        fh.write(t1 + "\n\n")
        fh.write(t2 + "\n\n")
        fh.write(t3 + "\n")
    print(f"\nWrote {md_path}")


if __name__ == "__main__":
    main()
