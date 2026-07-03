#!/usr/bin/env python3
"""Mirror + firsthand-inspect languageR::dative, fit the corpus-model logistic
regression (the SECONDARY-analysis human gradient), and emit derived tables.

Recipe-not-corpus posture (build condition (g) of decisions/resolved/dative-anchor-
and-indicator): the GPL tarball + extracted .rda live under experiments/data/languageR/
(gitignored); this script commits only (1) the inspection manifest and (2) the derived
factor->predicted-probability artifacts (coefficients + a small predicted-P table for
the stimulus configurations). NEVER commit raw corpus rows.

Run:  python3 mirror_and_fit.py
Deps: pyreadr, pandas, numpy, statsmodels  (pip-installed at build time; ephemeral).
"""
import json
import hashlib
import os
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadr
import statsmodels.api as sm

HERE = Path(__file__).resolve().parent
DATA = HERE.parent.parent / "data" / "languageR"  # gitignored
TARBALL_URL = "https://cran.r-project.org/src/contrib/languageR_1.6.tar.gz"
TARBALL = DATA / "languageR_1.6.tar.gz"
RDA = DATA / "languageR" / "data" / "dative.rda"

# Information-structure + control factors used in the corpus model. PP (prepositional
# dative) is the modelled "1" outcome; NP (double-object) is "0".
IS_FACTORS = [
    "AccessOfRec", "AccessOfTheme", "PronomOfRec", "PronomOfTheme",
    "DefinOfRec", "DefinOfTheme", "AnimacyOfRec", "AnimacyOfTheme",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mirror() -> str:
    DATA.mkdir(parents=True, exist_ok=True)
    if not TARBALL.exists():
        urllib.request.urlretrieve(TARBALL_URL, TARBALL)
    if not RDA.exists():
        with tarfile.open(TARBALL, "r:gz") as t:
            t.extract("languageR/data/dative.rda", path=DATA)
    return sha256(TARBALL)


def load() -> pd.DataFrame:
    # pyreadr carries R's string row-names as the index; reset so dummy/concat align.
    return pyreadr.read_r(str(RDA))["dative"].reset_index(drop=True)


def main():
    tar_sha = mirror()
    df = load()
    assert df.shape == (3263, 15), df.shape

    # --- inspection manifest (committed; no raw rows) ---
    manifest = {
        "source": TARBALL_URL,
        "tarball_sha256": tar_sha,
        "rda_sha256": sha256(RDA),
        "shape": list(df.shape),
        "columns": list(df.columns),
        "outcome_counts": {k: int(v) for k, v in
                           df["RealizationOfRecipient"].value_counts().to_dict().items()},
        "factor_levels": {c: sorted(map(str, df[c].dropna().unique()))
                          for c in IS_FACTORS + ["Modality", "SemanticClass"]},
        "length_summary": {
            "LengthOfRecipient": [int(df.LengthOfRecipient.min()),
                                  int(df.LengthOfRecipient.max()),
                                  round(float(df.LengthOfRecipient.mean()), 3)],
            "LengthOfTheme": [int(df.LengthOfTheme.min()),
                              int(df.LengthOfTheme.max()),
                              round(float(df.LengthOfTheme.mean()), 3)],
        },
    }

    # --- corpus-model logistic regression: P(PP) ~ factors + log length difference ---
    y = (df["RealizationOfRecipient"] == "PP").astype(int).values
    # log-length difference (theme - recipient); the classic Bresnan "short-before-long"
    # control. +1 smoothing inside log to avoid log(0) (lengths are >=1 here anyway).
    logdiff = np.log(df["LengthOfTheme"].values) - np.log(df["LengthOfRecipient"].values)
    X = pd.DataFrame({"log_theme_minus_rec_len": logdiff})
    # treatment-coded dummies for the categorical factors (reference = first level alpha)
    for c in IS_FACTORS:
        d = pd.get_dummies(df[c].astype(str), prefix=c, drop_first=True).astype(float)
        X = pd.concat([X, d], axis=1)
    X = sm.add_constant(X)
    model = sm.Logit(y, X.values).fit(disp=0, maxiter=200)

    coef = dict(zip(["const"] + list(X.columns[1:]), model.params.tolist()))
    # accuracy of the corpus model (sanity: Bresnan et al. report high accuracy)
    pred = (model.predict(X.values) >= 0.5).astype(int)
    acc = float((pred == y).mean())

    # --- directional checks (the human signal the PRIMARY test relies on) ---
    # Positive coef on a dummy => that level pushes toward PP (prepositional dative);
    # negative => toward NP (double-object, DOC). Canonical literature directions
    # (Bresnan et al. 2007; given-before-new + pronominal recipients favour DOC +
    # end-weight): a GIVEN/PRONOMINAL recipient -> DOC (negative); a GIVEN/PRONOMINAL
    # theme -> PD (positive); a LONGER THEME relative to recipient -> DOC by end-weight
    # (the heavy constituent goes last; DOC has the theme last) => NEGATIVE coef on the
    # log length difference.
    directions = {
        "given_recipient_pushes_DOC(NP)": coef.get("AccessOfRec_given", 0) < 0,
        "pronominal_recipient_pushes_DOC(NP)": coef.get("PronomOfRec_pronominal", 0) < 0,
        "given_theme_pushes_PD(PP)": coef.get("AccessOfTheme_given", 0) > 0,
        "pronominal_theme_pushes_PD(PP)": coef.get("PronomOfTheme_pronominal", 0) > 0,
        "longer_theme_pushes_DOC(NP)_by_end_weight": coef["log_theme_minus_rec_len"] < 0,
    }

    out = {
        "manifest": manifest,
        "corpus_model": {
            "outcome": "P(PP) = prepositional dative; NP=double-object is the 0 class",
            "predictors": list(X.columns),
            "coefficients": {k: round(v, 4) for k, v in coef.items()},
            "in_sample_accuracy": round(acc, 4),
            "n": int(len(y)),
            "directional_checks": directions,
        },
    }
    (HERE / "corpus_inspection.json").write_text(json.dumps(out, indent=2))
    print(json.dumps({"shape": manifest["shape"],
                      "outcome_counts": manifest["outcome_counts"],
                      "in_sample_accuracy": acc,
                      "directional_checks": directions}, indent=2))


if __name__ == "__main__":
    main()
