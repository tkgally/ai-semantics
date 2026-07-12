"""Q2-B frequency/co-occurrence control — derive per-scale-pair corpus statistics from UD Japanese-GSD.

Ratified freeze condition (vi) of decisions/resolved/cross-linguistic-cc-replication-scope: carry a
target-language-corpus frequency/co-occurrence-matched control with a DOCUMENTED matching recipe
FROZEN before any model call. UD Japanese-GSD annotations are CC BY-SA 4.0 (README verified firsthand
this session: "These are made available under a CC BY-SA 4.0"; Google asserts no ownership over the
underlying text), in scope under the s168 UD-treebank rule.

WHAT THIS CONTROL IS (and honestly, what it is not) — identical logic to the German arm.
The core construction-isolation leg (Q2-A) already holds LEXIS IDENTICAL between CC items and their
same-word non-CC controls — so there is NO lexical-frequency difference to confound that contrast.
The residual loophole a frequency control can still close is: does the panel's covariation reading
track the CORPUS FREQUENCY / ASSOCIATION of the scalar words rather than the construction? This
script measures, per scale pair, the UD-Japanese-GSD content-word (NOUN/ADJ) frequency of the pair's
scalar words and the pair's in-corpus co-occurrence, so analyze.py can test whether the CC
covariation-assertion rate (and the construction-isolation gap) is INDEPENDENT of corpus
frequency/co-occurrence. It is a COVARIATE/robustness arm, not a separate item arm; the primary
co-occurrence control remains the typical-vs-atypical split (absurd pairs whose scalar words
essentially never co-occur must get their direction from the construction alone).

JAPANESE-SPECIFIC RECIPE NOTE (the deliberate difference from the German build_cooc_de.py).
German is whitespace-segmented, so the German control resolved item words against the treebank's own
form->lemma/UPOS maps directly. Japanese is UNSEGMENTED, so surface-form lookup against the treebank
would fail on every conjugated/agglutinated form. To keep ONE consistent tokenization basis across the
corpus side and the item side, BOTH the UD-Japanese-GSD sentences (their `# text =` lines) AND the
items are tokenized with the SAME analyzer — janome 0.5.0 (pure-Python, self-contained IPAdic; pinned
below) — keeping NOUN (名詞, excluding numerals/pronouns/non-independent/suffix subtypes) and ADJ
(形容詞) base forms. Frequency is therefore a janome-IPAdic count over the licensed UD-GSD sentence
set, not the treebank's gold UniDic lemmas — a deliberate, documented consistency choice (a
covariate, not the primary control). The typical/atypical co-occurrence split (below) is the
functional check that the measure separates the two families as designed.

RECIPE (frozen; fully automatic, no hand-specified lemmas — minimizing fabrication risk):
1. Read every `# text =` sentence from the three UD-Japanese-GSD splits; janome-tokenize; keep
   content tokens (NOUN/ADJ base forms, per CONTENT_POS + subtype exclusions + LEMMA_STOP). Build
   lemma_count[lemma] and sent_lemmas (per-sentence content-lemma sets, for co-occurrence).
2. For each scale pair, janome-tokenize its cc-positive + cc-inverse + two control sentences, take the
   union of content lemmas -> the pair's CONTENT LEMMAS. Words absent from UD-GSD resolve to freq 0
   and are recorded as OOV (itself informative).
3. Per pair record: content lemmas, each lemma's per-million frequency, the pair mean/median content
   frequency, the # of UD-GSD sentences containing >=2 distinct content lemmas of the pair
   (co-occurrence), OOV count, typicality.
4. Emit freq_control.json (the FROZEN artifact, committed before the run) + a corpus-meta block.

Run: python3 build_cooc_ja.py   (reads /tmp/ja_gsd_{train,dev,test}.conllu; needs janome; no API)
"""
import csv, json, os, collections
from janome.tokenizer import Tokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                         "comparative-correlative-japanese", "items.csv"))
CONLLU = [f"/tmp/ja_gsd_{s}.conllu" for s in ("train", "dev", "test")]
SOURCE_URL = "https://raw.githubusercontent.com/UniversalDependencies/UD_Japanese-GSD/master/ja_gsd-ud-{train,dev,test}.conllu"
OUT = os.path.join(HERE, "freq_control.json")

# janome POS: keep 名詞 (NOUN) and 形容詞 (ADJ) as content; drop noun subtypes that carry no
# scalar/referential content (numerals, pronouns, non-independent, suffixes) so the frequency
# measure reflects the scalar adjectives and referent nouns the frequency-exploitation loophole is
# actually about. Verbs (動詞) are held out (mirrors the German ADJ+NOUN choice: light/copula-like
# tokens surface in nearly every pair as a constant offset).
NOUN_DROP_SUBTYPES = {"数", "数詞", "代名詞", "非自立", "接尾", "副詞可能"}
# Very generic content-light nouns excluded (constant across pairs, no scalar/referential content).
LEMMA_STOP = {"もの", "物", "こと", "事", "ため", "とき", "時", "前", "後", "方", "人", "того"}

_tok = Tokenizer()


def content_lemmas_of_text(text):
    """janome-tokenize -> list of (lemma) for NOUN/ADJ content tokens (deduped-preserving upstream)."""
    out = []
    for t in _tok.tokenize(text):
        pos = t.part_of_speech.split(",")  # e.g. ['名詞','一般','*','*'] or ['形容詞','自立','*','*']
        major, sub = pos[0], (pos[1] if len(pos) > 1 else "*")
        base = t.base_form if t.base_form and t.base_form != "*" else t.surface
        if major == "形容詞":
            out.append(base)
        elif major == "名詞" and sub not in NOUN_DROP_SUBTYPES:
            if base not in LEMMA_STOP and len(base) >= 1:
                out.append(base)
    return out


def parse_corpus(paths):
    lemma_count = collections.Counter()
    sent_lemmas = []
    n_sent = 0
    for path in paths:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("# text ="):
                    text = line.split("=", 1)[1].strip()
                    n_sent += 1
                    lems = content_lemmas_of_text(text)
                    for l in lems:
                        lemma_count[l] += 1
                    sent_lemmas.append(set(lems))
    return lemma_count, sent_lemmas, n_sent


def dedupe(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out


def main():
    lemma_count, sent_lemmas, n_sent = parse_corpus(CONLLU)
    total_content = sum(lemma_count.values())
    per_million = lambda lem: round(1e6 * lemma_count.get(lem, 0) / total_content, 3)

    rows = list(csv.DictReader(open(ITEMS_CSV)))
    by_pair = collections.defaultdict(dict)
    for r in rows:
        by_pair[r["scale_pair"]][r["form"]] = r

    pairs_out = {}
    for pid, forms in by_pair.items():
        typ = forms["cc-positive"]["typicality"]
        all_lem = []
        for form in ("cc-positive", "cc-inverse", "ctrl-two", "ctrl-single"):
            all_lem.extend(content_lemmas_of_text(forms[form]["sentence"]))
        lemmas = dedupe(all_lem)
        freqs = {lem: per_million(lem) for lem in lemmas}
        oov = sorted([lem for lem in lemmas if lemma_count.get(lem, 0) == 0])
        mean_f = round(sum(freqs.values()) / len(freqs), 3) if freqs else 0.0
        median_f = round(sorted(freqs.values())[len(freqs) // 2], 3) if freqs else 0.0
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
        "recipe": "UD-Japanese-GSD `# text =` sentences + items BOTH tokenized with janome 0.5.0 "
                  "(IPAdic); content = NOUN(名詞, minus numeral/pronoun/non-independent/suffix "
                  "subtypes)+ADJ(形容詞) base forms; per-lemma per-million frequency + per-pair "
                  "co-occurrence (# sentences with >=2 distinct pair content lemmas). FROZEN before "
                  "the run. Consistency choice (Japanese is unsegmented): one janome basis across "
                  "corpus and items, not the treebank gold UniDic lemmas — a bounded covariate, the "
                  "primary co-occurrence control is the typical/atypical split.",
        "tokenizer": "janome 0.5.0 (IPAdic, bundled)",
        "source": SOURCE_URL,
        "license": "CC BY-SA 4.0 (UD Japanese-GSD annotations; README verified firsthand s215, in scope s168)",
        "corpus_meta": {"n_sentences": n_sent, "n_content_tokens": total_content,
                        "n_distinct_content_lemmas": len(lemma_count)},
        "pairs": pairs_out,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    typ = [p for p in pairs_out.values() if p["typicality"] == "typical"]
    aty = [p for p in pairs_out.values() if p["typicality"] == "atypical"]
    def avg(xs, k): return round(sum(x[k] for x in xs) / len(xs), 3)
    print(f"corpus: {n_sent} sentences, {total_content} content tokens, "
          f"{len(lemma_count)} distinct content lemmas")
    print(f"typical  (n={len(typ)}): mean_freq/M={avg(typ,'mean_freq_per_million')}  "
          f"cooc>=2={avg(typ,'cooc_sentences_ge2')}  oov={avg(typ,'n_oov')}  "
          f"n_lemmas={avg(typ,'n_content_lemmas')}")
    print(f"atypical (n={len(aty)}): mean_freq/M={avg(aty,'mean_freq_per_million')}  "
          f"cooc>=2={avg(aty,'cooc_sentences_ge2')}  oov={avg(aty,'n_oov')}  "
          f"n_lemmas={avg(aty,'n_content_lemmas')}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
