"""Q2-B frequency/co-occurrence control — derive per-scale-pair corpus statistics from UD German-GSD.

Ratified freeze condition (vi) of decisions/resolved/cross-linguistic-cc-replication-scope: carry a
UD-German-GSD-derived frequency/co-occurrence-matched control with a DOCUMENTED matching recipe
FROZEN before any model call. UD German-GSD annotations are CC BY-SA 4.0 (scout-verified, in scope
under the s168 UD-treebank rule).

WHAT THIS CONTROL IS (and honestly, what it is not).
The core construction-isolation leg (Q2-A) already holds LEXIS IDENTICAL between CC items and their
same-word non-CC controls — so there is NO lexical-frequency difference to confound that contrast.
The residual loophole a frequency control can still close is the one the reviewer + the non-Anthropic
vote named: does the panel's covariation reading track the CORPUS FREQUENCY / ASSOCIATION of the
scalar words, rather than the construction? This script measures, per scale pair, the UD-German-GSD
content-word frequency of the pair's scalar words and the pair's in-corpus co-occurrence, so
analyze.py can test whether the CC covariation-assertion rate (and the construction-isolation gap)
is INDEPENDENT of corpus frequency/co-occurrence. It is a COVARIATE/robustness arm, not a separate
item arm; the primary co-occurrence control remains the typical-vs-atypical split (absurd pairs whose
words essentially never co-occur must get their direction from the construction alone).

RECIPE (frozen; fully automatic, grounded in the treebank's own annotations — no hand-specified
lemmas, minimizing fabrication risk).
1. Parse the UD German-GSD conllu splits. Build:
   - lemma_count[lemma]  = # tokens with that LEMMA whose UPOS is a content class {ADJ, NOUN, VERB};
   - form2lemma[form.lower()] = the most frequent lemma for that surface form (content POS only);
   - form2pos[form.lower()]   = the UPOS set attested for that surface form (content POS only);
   - sent_lemmas = per-sentence set of content lemmas (for co-occurrence).
2. For each scale pair, tokenize its cc-positive + cc-inverse + two control sentences (lowercase,
   strip punctuation), keep tokens whose surface form is attested in UD-GSD as ADJ or NOUN, resolve
   each to its treebank lemma -> the pair's CONTENT LEMMAS (deduped). Words absent from UD-GSD
   (e.g. rare 'Tannenzapfen') resolve to nothing and are recorded as OOV (freq 0) — itself informative.
3. Per pair record: content lemmas, each lemma's per-million frequency, the pair mean/median content
   frequency, the # of UD-GSD sentences containing >=2 distinct content lemmas of the pair
   (co-occurrence), OOV count, and typicality.
4. Emit freq_control.json (the FROZEN artifact, committed before the run) + a corpus-meta block
   (source URL, split sizes, token totals) so the recipe is reproducible.

Run: python3 build_cooc_de.py   (reads /tmp/de_gsd_{train,dev,test}.conllu; no network, no API)
"""
import csv, json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                         "comparative-correlative-german", "items.csv"))
CONLLU = [f"/tmp/de_gsd_{s}.conllu" for s in ("train", "dev", "test")]
SOURCE_URL = "https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-{train,dev,test}.conllu"
# Scalar ADJ + referent NOUN only — these carry the construction's scales and referents, and are
# exactly the words a "the model just reads covariation off frequent/associated content words"
# loophole would exploit. Light/copula VERBs (sein, werden, bleiben) are held out: they occur in
# every pair (a constant offset that cannot differentially confound the typical/atypical contrast)
# and would swamp the scalar-word signal.
CONTENT_POS = {"ADJ", "NOUN"}
# Light/copula/possessive lemmas that surface in (nearly) every pair as a constant and carry no
# scalar/referential content — excluded so the frequency measure reflects the scalar adjectives and
# referent nouns the frequency-exploitation loophole is actually about.
LEMMA_STOP = {"sein", "werden", "bleiben", "haben", "viel", "mehr", "wenig", "als", "so"}
OUT = os.path.join(HERE, "freq_control.json")

_TOKEN_RE = re.compile(r"[^\W\d_]+", re.UNICODE)  # unicode letter runs (keeps ä ö ü ß)


def parse_conllu(paths):
    lemma_count = collections.Counter()
    form2lemma_counts = collections.defaultdict(collections.Counter)
    form2pos = collections.defaultdict(set)
    sent_lemmas = []          # list of sets of content lemmas per sentence
    n_sent = 0
    n_tok = 0
    cur = set()
    for path in paths:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    if cur:
                        sent_lemmas.append(cur)
                        cur = set()
                    n_sent += 1
                    continue
                if line.startswith("#"):
                    continue
                cols = line.split("\t")
                if len(cols) < 5 or "-" in cols[0] or "." in cols[0]:
                    continue  # skip multiword-token ranges and empty nodes
                form, lemma, upos = cols[1], cols[2], cols[3]
                n_tok += 1
                if upos in CONTENT_POS:
                    lemma_count[lemma] += 1
                    form2lemma_counts[form.lower()][lemma] += 1
                    form2pos[form.lower()].add(upos)
                    cur.add(lemma)
    if cur:
        sent_lemmas.append(cur)
    form2lemma = {f: c.most_common(1)[0][0] for f, c in form2lemma_counts.items()}
    return lemma_count, form2lemma, form2pos, sent_lemmas, n_sent, n_tok


def content_lemmas_of(sentence, form2lemma, form2pos):
    """Tokens whose surface form is attested in UD-GSD as ADJ or NOUN -> their treebank lemma."""
    lemmas, oov = [], []
    for tok in _TOKEN_RE.findall(sentence):
        f = tok.lower()
        pos = form2pos.get(f)
        if pos and (("ADJ" in pos) or ("NOUN" in pos)) and form2lemma[f] not in LEMMA_STOP:
            lemmas.append(form2lemma[f])
        elif len(tok) > 3 and tok[0].isupper():
            # a capitalized non-attested word is a likely content noun that is OOV in UD-GSD
            oov.append(tok)
    # dedupe preserving order
    seen, dl = set(), []
    for l in lemmas:
        if l not in seen:
            seen.add(l); dl.append(l)
    return dl, sorted(set(oov))


def main():
    lemma_count, form2lemma, form2pos, sent_lemmas, n_sent, n_tok = parse_conllu(CONLLU)
    total_content = sum(lemma_count.values())
    per_million = lambda lem: round(1e6 * lemma_count.get(lem, 0) / total_content, 3)

    rows = list(csv.DictReader(open(ITEMS_CSV)))
    by_pair = collections.defaultdict(dict)
    for r in rows:
        by_pair[r["scale_pair"]][r["form"]] = r

    pairs_out = {}
    for pid, forms in by_pair.items():
        typ = forms["cc-positive"]["typicality"]
        # union the content lemmas across all four (same-word) forms of the pair
        all_lem, all_oov = [], []
        for form in ("cc-positive", "cc-inverse", "ctrl-two", "ctrl-single"):
            dl, oov = content_lemmas_of(forms[form]["sentence"], form2lemma, form2pos)
            all_lem.extend(dl); all_oov.extend(oov)
        seen, lemmas = set(), []
        for l in all_lem:
            if l not in seen:
                seen.add(l); lemmas.append(l)
        oov = sorted(set(all_oov))
        freqs = {lem: per_million(lem) for lem in lemmas}
        nonzero = [v for v in freqs.values() if v > 0]
        mean_f = round(sum(freqs.values()) / len(freqs), 3) if freqs else 0.0
        median_f = round(sorted(freqs.values())[len(freqs) // 2], 3) if freqs else 0.0
        # co-occurrence: # UD-GSD sentences containing >=2 distinct content lemmas of this pair
        lemset = set(lemmas)
        cooc = sum(1 for s in sent_lemmas if len(s & lemset) >= 2)
        pairs_out[pid] = {
            "typicality": typ,
            "content_lemmas": lemmas,
            "oov_content_words": oov,
            "freq_per_million": freqs,
            "mean_freq_per_million": mean_f,
            "median_freq_per_million": median_f,
            "n_content_lemmas": len(lemmas),
            "n_oov": len(oov),
            "cooc_sentences_ge2": cooc,
        }

    out = {
        "recipe": "UD-German-GSD content-word (ADJ/NOUN/VERB) lemma frequencies + per-pair "
                  "co-occurrence; content lemmas resolved automatically from the treebank's own "
                  "form->lemma and form->UPOS maps (ADJ/NOUN surface tokens). FROZEN before the run.",
        "source": SOURCE_URL,
        "license": "CC BY-SA 4.0 (UD German-GSD annotations; scout-verified, s168 in scope)",
        "corpus_meta": {"n_sentences": n_sent, "n_tokens": n_tok,
                        "n_content_tokens": total_content,
                        "n_distinct_content_lemmas": len(lemma_count)},
        "pairs": pairs_out,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    # console summary: typical vs atypical mean frequency + co-occurrence (the design's key contrast)
    typ = [p for p in pairs_out.values() if p["typicality"] == "typical"]
    aty = [p for p in pairs_out.values() if p["typicality"] == "atypical"]
    def avg(xs, k): return round(sum(x[k] for x in xs) / len(xs), 3)
    print(f"corpus: {n_sent} sentences, {n_tok} tokens, {total_content} content tokens, "
          f"{len(lemma_count)} distinct content lemmas")
    print(f"typical  (n={len(typ)}): mean_freq/M={avg(typ,'mean_freq_per_million')}  "
          f"cooc>=2={avg(typ,'cooc_sentences_ge2')}  oov={avg(typ,'n_oov')}")
    print(f"atypical (n={len(aty)}): mean_freq/M={avg(aty,'mean_freq_per_million')}  "
          f"cooc>=2={avg(aty,'cooc_sentences_ge2')}  oov={avg(aty,'n_oov')}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
