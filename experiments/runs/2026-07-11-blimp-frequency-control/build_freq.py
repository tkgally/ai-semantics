#!/usr/bin/env python3
"""build_freq.py — the Q2-A per-paradigm surface-string frequency proxy F(p) for the BLiMP R1
frequency-control (C8 promotion-prep, program A3b). NEW CODE with genuine researcher DoF (freeze
condition G1'): build_cooc_c4.py has NO n-gram frequency counter — only unigram df + cue co-occurrence +
a signed-G² kernel — so ONLY its C4 streaming adapter + tokenization regexes are reused here (import-pinned
below). The n-gram extraction + F(p) aggregation are new and are frozen in PREREG.md BEFORE F(p) is
computed; a fresh-agent verifier independently reproduces this from the PREREG spec on a synthetic fixture
(build_freq_fixture.py) before F(p) touches the real paradigm→H mapping (which happens only in
analyze_partial.py).

F(p) SPEC (Q2-A, frozen — see PREREG.md §F):
  - Corpus items: the 40 frozen s205 paradigms, `items.json → items[uid]` (30 pairs each); use the
    "good" sentence only.
  - Tokenizer: the FROZEN C4 tokenizer reused from build_cooc_c4.py — lowercase, then
    _nonword.sub(" ", s).split() (a-z + whitespace only). Applied identically to item sentences and C4.
  - Content words: tokens NOT in the frozen STOPWORDS set (function words) below.
  - Target n-grams for a good sentence: every ADJACENT-token bigram and trigram of the tokenized sentence
    whose tokens are ALL content words. (A surface-material familiarity proxy.)
  - C4 count c(g): number of occurrences of n-gram g as consecutive tokens across the streamed C4 set
    (shards 00000-00002, the s193-frozen 22,329,495-sentence set).
  - Sentence score: mean over the sentence's content-word n-grams of log(1 + c(g)).
  - F(p) PRIMARY = mean sentence score over the paradigm's 30 good sentences, using bigrams+trigrams.
  - F(p) SENSITIVITY = same but bigrams only (the single pre-specified variant, G7).
  Sentences with zero content-word n-grams are dropped and logged (not silently repaired).

Emits freq.json: raw per-n-gram counts, per-paradigm n-gram lists, and F_primary/F_sensitivity per
paradigm — everything the post-run verifier needs to recompute. Reads NO model output and NO accuracy /
human-agreement value: F(p) is computed blind to the paradigm→H mapping (anti-cheat, G1').
"""
import gzip, io, json, math, os, re, time, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
COOC = os.path.abspath(os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy",
                                    "build_cooc_c4.py"))
ITEMS_PATH = os.path.abspath(os.path.join(HERE, "..", "2026-07-10-blimp-forced-choice-sweep", "items.json"))

# ---- G1'(a): import the frozen C4 script and PIN the actually-reused code (streaming + tokenization),
#      NOT the G² kernel. Assert the tokenizer regexes and shard spec are the frozen strings. ----
_spec = importlib.util.spec_from_file_location("build_cooc_c4", COOC)
_cooc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cooc)
assert _cooc._nonword.pattern == r"[^a-z\s]+", "C4 tokenizer _nonword DRIFT vs build_cooc_c4.py"
assert _cooc._sent.pattern == r"[.!?]+\s", "C4 sentence splitter _sent DRIFT vs build_cooc_c4.py"
assert _cooc.NUM_SHARDS == 3, "C4 shard count DRIFT (expect 00000-00002)"
assert "c4-train.{:05d}-of-01024.json.gz" in _cooc.C4_BASE, "C4 shard URL DRIFT"
stream_sentences = _cooc.stream_sentences          # the ONLY reused compute (yields token lists)
_nonword = _cooc._nonword
S186_NSENT = 21_300_000                              # volume floor carried from build_cooc_c4.py

# ---- FROZEN content-word filter: an explicit English function-word (stopword) list. Frozen in PREREG. ----
STOPWORDS = {
    "a", "an", "the", "this", "that", "these", "those", "some", "any", "no", "every", "each", "either",
    "neither", "both", "all", "half", "many", "much", "more", "most", "few", "little", "less", "least",
    "several", "enough", "such", "what", "which", "whose", "whatever", "whichever",
    "i", "me", "my", "mine", "myself", "we", "us", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
    "itself", "they", "them", "their", "theirs", "themselves", "who", "whom", "one", "ones", "oneself",
    "someone", "somebody", "something", "anyone", "anybody", "anything", "everyone", "everybody",
    "everything", "noone", "nobody", "nothing", "each", "another", "other", "others",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does",
    "did", "doing", "will", "would", "shall", "should", "can", "could", "may", "might", "must", "ought",
    "need", "dare", "used",
    "and", "or", "but", "nor", "so", "yet", "for", "if", "then", "else", "because", "as", "until", "while",
    "of", "at", "by", "on", "off", "in", "into", "out", "onto", "upon", "over", "under", "above", "below",
    "to", "from", "up", "down", "with", "within", "without", "about", "against", "between", "among",
    "through", "during", "before", "after", "behind", "beyond", "beside", "besides", "near", "around",
    "along", "across", "toward", "towards", "than", "though", "although", "whether", "since", "unless",
    "whereas", "however", "therefore", "thus", "hence",
    "not", "only", "just", "even", "also", "too", "very", "quite", "rather", "almost", "still", "already",
    "again", "ever", "never", "always", "often", "sometimes", "here", "there", "where", "when", "why",
    "how", "now", "once", "twice", "yes", "no",
    "s", "t", "re", "ve", "ll", "d", "m",   # tokenizer fragments from contractions (a-z-only splits)
}

BIGRAM_MIN, BIGRAM_MAX = 2, 2
SEED_NOTE = "F(p) is computed blind to accuracy/human-agreement; no post-hoc tuning (G1')."


def tokenize(s):
    return _nonword.sub(" ", s.lower()).split()


def content_ngrams(toks):
    """Adjacent-token bigrams and trigrams whose tokens are ALL content words. Returns (bigrams, trigrams)
    as tuples-of-tokens."""
    bi, tri = [], []
    for i in range(len(toks) - 1):
        a, b = toks[i], toks[i + 1]
        if a not in STOPWORDS and b not in STOPWORDS:
            bi.append((a, b))
    for i in range(len(toks) - 2):
        a, b, c = toks[i], toks[i + 1], toks[i + 2]
        if a not in STOPWORDS and b not in STOPWORDS and c not in STOPWORDS:
            tri.append((a, b, c))
    return bi, tri


def build_targets():
    items = json.load(open(ITEMS_PATH))
    uids = [p["uid"] for p in items["paradigms"]]
    per_para = {}          # uid -> list of {sentence bigrams, trigrams, unigrams}
    target = set()         # union of all n-grams to count in C4
    utarget = set()        # union of all content-word unigrams (for the G7 audit)
    for uid in uids:
        sents = []
        for pair in items["items"][uid]:
            toks = tokenize(pair["good"])
            bi, tri = content_ngrams(toks)
            uni = [t for t in toks if t not in STOPWORDS]
            sents.append({"bi": bi, "tri": tri, "uni": uni})
            target.update(bi)
            target.update(tri)
            utarget.update(uni)
        per_para[uid] = sents
    return uids, per_para, target, utarget


def count_in_c4(target, utarget):
    """Stream C4 (frozen adapter) and count each target n-gram + content-word unigram's occurrences as
    consecutive tokens. Unigrams feed the G7 proxy-validity audit only (not F(p))."""
    counts = {g: 0 for g in target}
    ucounts = {w: 0 for w in utarget}
    Nsent = Ntok = 0
    t0 = time.time()
    for toks in stream_sentences():
        Nsent += 1
        Ntok += len(toks)
        n = len(toks)
        for i in range(n):
            w = toks[i]
            if w in ucounts:
                ucounts[w] += 1
            if i < n - 1:
                g = (w, toks[i + 1])
                if g in counts:
                    counts[g] += 1
            if i < n - 2:
                g = (w, toks[i + 1], toks[i + 2])
                if g in counts:
                    counts[g] += 1
        if Nsent % 2_000_000 == 0:
            print(f"  {Nsent} sentences, {Ntok} tokens, {time.time()-t0:.0f}s", flush=True)
    print(f"total {Nsent} sentences, {Ntok} tokens in {time.time()-t0:.0f}s", flush=True)
    assert Nsent >= S186_NSENT, f"C4 volume {Nsent} < {S186_NSENT} — stream more shards"
    return counts, ucounts, Nsent, Ntok


def score(ngrams, counts):
    """mean over the n-grams of log(1 + count). ngrams: list of tuples. Returns None if empty."""
    if not ngrams:
        return None
    vals = [math.log1p(counts.get(g, 0)) for g in ngrams]
    return sum(vals) / len(vals)


def f_of_paradigm(sents, counts, use_tri):
    ss, dropped = [], 0
    for s in sents:
        ng = list(s["bi"]) + (list(s["tri"]) if use_tri else [])
        v = score(ng, counts)
        if v is None:
            dropped += 1
        else:
            ss.append(v)
    return (sum(ss) / len(ss) if ss else None), dropped


def main():
    uids, per_para, target, utarget = build_targets()
    print(f"targets: {len(target)} distinct n-grams, {len(utarget)} unigrams over {len(uids)} paradigms",
          flush=True)
    counts, ucounts, Nsent, Ntok = count_in_c4(target, utarget)
    F_primary, F_sens, drop_log, uni_logfreq, mean_wlen = {}, {}, {}, {}, {}
    for uid in uids:
        fp, dp = f_of_paradigm(per_para[uid], counts, use_tri=True)
        fs, _ = f_of_paradigm(per_para[uid], counts, use_tri=False)
        F_primary[uid] = fp
        F_sens[uid] = fs
        drop_log[uid] = dp
        # G7 audit inputs (computed here, blind to accuracy/H): per-paradigm mean content-word unigram
        # log-freq and mean content-word length.
        unis = [w for s in per_para[uid] for w in s["uni"]]
        uni_logfreq[uid] = (sum(math.log1p(ucounts.get(w, 0)) for w in unis) / len(unis)) if unis else None
        mean_wlen[uid] = (sum(len(w) for w in unis) / len(unis)) if unis else None
    out = {
        "spec": "Q2-A surface-string content-word bigram+trigram log-frequency; blind to paradigm→H (G1').",
        "Nsent": Nsent, "Ntok": Ntok, "n_targets": len(target), "n_unigrams": len(utarget),
        "stopwords_n": len(STOPWORDS),
        "F_primary": F_primary, "F_sensitivity": F_sens, "dropped_sentences": drop_log,
        "audit_uni_logfreq": uni_logfreq, "audit_mean_wlen": mean_wlen,
        "counts": {" ".join(g): c for g, c in counts.items()},
        "ucounts": ucounts,
    }
    json.dump(out, open(os.path.join(HERE, "freq.json"), "w"), indent=1)
    print("freq.json written.")
    print("F(p) primary (bi+tri):")
    for uid in uids:
        print(f"  {uid:52s} F={F_primary[uid]:.4f}  (bi-only {F_sens[uid]:.4f}, dropped {drop_log[uid]})")


if __name__ == "__main__":
    main()
