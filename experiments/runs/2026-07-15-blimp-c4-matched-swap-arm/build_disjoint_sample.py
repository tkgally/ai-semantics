#!/usr/bin/env python3
"""build_disjoint_sample.py — FREEZE-TIME ($0, BLiMP download only; no C4, no model calls).

G-disjoint (Q2-A): draw the fresh ≈100-pair-per-paradigm subsample for the C4-matched swap arm, GUARANTEED
disjoint from the s210 sample BY CONSTRUCTION — sampled from (paradigm pairs MINUS the s210 kept pair ids),
under a fresh seed. The paradigm SELECTION is inherited byte-frozen from s210 (same 6 uids); this script only
re-draws the item sample and certifies disjointness. Emits disjoint_sample.json (the frozen draw) + its
sha256, which build_swap_c4.py consumes at RUN and the run verifier re-reproduces.

Frozen at freeze; SAMPLE_N drawn, first TARGET_N usable kept by build_swap_c4.py after the dual-band swap.
"""
import hashlib, json, random, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / ".cache"; CACHE.mkdir(exist_ok=True)

SEED = 20260715                    # fresh sample seed (distinct from s210's 20260711)
SAMPLE_N = 160                     # draw this many disjoint pairs/paradigm (build keeps first 100 usable;
                                   #   SHOULD-FIX 7: 130->160 headroom for dual-band attrition)
BLIMP_URL = "https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/{}.jsonl"

# the 6 s210-selected paradigms (selection inherited byte-frozen) + their s210 file sha256 (pinned)
PARADIGM_SHA = {
    "determiner_noun_agreement_2": "8ae7eff7c7bd384ff5ef3113984834f4d78b34559203aa9d5cb14ea8394291a9",
    "determiner_noun_agreement_1": "f48065fd760d0fd1a895012860d38bdf3c2ac115cd221e521684cc430c0f1855",
    "regular_plural_subject_verb_agreement_1": "1a18d94062c8e792c0a200a3b00dff0e051a92bb084c05e9b5e5c73bee32a620",
    "sentential_negation_npi_scope": "6c341ccc39c94bea45c0412986751bf2f6eca48626728e30e23d2b6a22c8b949",
    "only_npi_scope": "ca1f0671643e37936515f02125036bc2904ab9b35c4689b0e7a3ea3914e571f6",
    "superlative_quantifiers_1": "bebc5c5ff28cf226cc35293c60cde1fcf7565a7b58cb219d01ac8908b952a497",
}
STRATA = {"determiner_noun_agreement_2": "shallow", "determiner_noun_agreement_1": "shallow",
          "regular_plural_subject_verb_agreement_1": "shallow", "sentential_negation_npi_scope": "deep",
          "only_npi_scope": "deep", "superlative_quantifiers_1": "deep"}

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

def fetch_paradigm(uid):
    dest = CACHE / f"{uid}.jsonl"
    if not dest.exists():
        for attempt in range(4):
            try:
                urllib.request.urlretrieve(BLIMP_URL.format(uid), dest); break
            except Exception:
                if attempt == 3: raise
    raw = open(dest, "rb").read()
    sha = sha256_bytes(raw)
    assert sha == PARADIGM_SHA[uid], f"{uid} sha mismatch: {sha} != pinned {PARADIGM_SHA[uid]}"
    return [json.loads(l) for l in raw.decode().splitlines() if l.strip()]

def main():
    s210 = json.load(open(HERE / ".." / "2026-07-11-blimp-swap-arm" / "items_swap.json"))
    s210_kept = {u: set(str(p["pairID"]) for p in s210["items"][u]) for u in s210["selected"]}

    sample = {}
    for uid in PARADIGM_SHA:
        pairs = fetch_paradigm(uid)
        excl = s210_kept.get(uid, set())
        pool = [p for p in pairs if str(p.get("pairID")) not in excl]   # disjoint by construction
        rng = random.Random(int(hashlib.sha256(f"{SEED}-{uid}".encode()).hexdigest()[:12], 16))
        draw = rng.sample(pool, min(SAMPLE_N, len(pool)))
        drawn_ids = set(str(p.get("pairID")) for p in draw)
        assert drawn_ids.isdisjoint(excl), f"{uid} draw not disjoint from s210 kept"       # certified
        sample[uid] = [{"pairID": str(p.get("pairID")), "sentence_good": p["sentence_good"],
                        "sentence_bad": p["sentence_bad"]} for p in draw]

    payload = {"seed": SEED, "sample_n": SAMPLE_N, "paradigm_sha256": PARADIGM_SHA, "strata": STRATA,
               "sample": sample, "disjoint_from": "experiments/runs/2026-07-11-blimp-swap-arm (s210 kept ids)"}
    body = json.dumps(payload, sort_keys=True).encode()
    payload["sample_sha256"] = sha256_bytes(body)
    json.dump(payload, open(HERE / "disjoint_sample.json", "w"), indent=1)

    print("=== DISJOINT SAMPLE (frozen at freeze; disjoint from s210 BY CONSTRUCTION) ===")
    for uid in PARADIGM_SHA:
        n_pool = len([1 for _ in sample[uid]])
        overlap = set(p["pairID"] for p in sample[uid]) & s210_kept.get(uid, set())
        print(f"  [{STRATA[uid]:7s}] {uid:46s} drawn={len(sample[uid]):3d}  overlap_with_s210={len(overlap)}")
    print(f"\nsample_sha256: {payload['sample_sha256']}")
    print("ALL PARADIGMS CERTIFIED DISJOINT" if all(
        not (set(p['pairID'] for p in sample[u]) & s210_kept.get(u, set())) for u in PARADIGM_SHA)
        else "DISJOINTNESS FAILURE")

if __name__ == "__main__":
    main()
