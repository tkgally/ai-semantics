#!/usr/bin/env python3
"""
derive.py — DERIVED aggregate entrainment table for the Hawkins/Stanford tangrams corpus.

Recipe-not-corpus posture (decisions/resolved/relational-fetchable-anchor, Option A):
the raw corpus is gitignored and NOT redistributed; this script reads the gitignored raw
file and emits only a SMALL AGGREGATE table (no raw utterances) that is committed in-repo.

Input  : experiments/data/hawkins-tangrams/tangrams.csv  (gitignored; re-downloadable, sha256
         pinned in wiki/base/resources/hawkins-tangrams.md)
Output : entrainment_by_repetition.csv  (this directory; committed)

Each row of the raw corpus is one MESSAGE (utterance) in a dyadic reference game.
Columns used:
  - repetitionNum : 1..6, the repetition block of the tangram set (the entrainment x-axis)
  - numRawWords   : word count of the message (the compression / utterance-length signal)
  - correct       : trial outcome (1/0/NA), constant within a (gameid,trialNum) trial.
                    Accuracy is computed at the TRIAL level (one (gameid,trialNum) per trial)
                    to avoid over-weighting trials with more messages.

Pure stdlib (csv only); no numpy.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "..", "data", "hawkins-tangrams", "tangrams.csv"))
OUT = os.path.join(HERE, "entrainment_by_repetition.csv")


def main():
    n_messages = {}          # repetitionNum -> count of messages
    sum_words = {}           # repetitionNum -> sum of numRawWords
    trial_correct = {}       # (gameid,trialNum) -> (repetitionNum, correct_value)

    with open(RAW, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rep = row["repetitionNum"]
            n_messages[rep] = n_messages.get(rep, 0) + 1
            try:
                wcount = int(row["numRawWords"])
            except (ValueError, KeyError):
                wcount = 0
            sum_words[rep] = sum_words.get(rep, 0) + wcount

            key = (row["gameid"], row["trialNum"])
            c = row.get("correct", "NA")
            if key not in trial_correct:
                trial_correct[key] = (rep, c)
            elif trial_correct[key][1] == "NA" and c != "NA":
                trial_correct[key] = (rep, c)

    acc_n = {}
    acc_sum = {}
    for (rep, c) in trial_correct.values():
        if c in ("0", "1"):
            acc_n[rep] = acc_n.get(rep, 0) + 1
            acc_sum[rep] = acc_sum.get(rep, 0) + int(c)

    reps = sorted(n_messages, key=lambda x: int(x))
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["repetitionNum", "n_messages", "mean_numRawWords",
                    "n_scored_trials", "mean_correct"])
        for rep in reps:
            nm = n_messages[rep]
            mean_words = sum_words[rep] / nm if nm else 0.0
            ntrials = acc_n.get(rep, 0)
            mean_corr = (acc_sum.get(rep, 0) / ntrials) if ntrials else None
            w.writerow([rep, nm, f"{mean_words:.4f}", ntrials,
                        f"{mean_corr:.4f}" if ntrials else "NA"])
    print("wrote", OUT)
    with open(OUT) as f:
        print(f.read())


if __name__ == "__main__":
    main()
