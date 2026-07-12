"""Non-Anthropic pre-run decorrelation vote — Japanese-fidelity audit (s215).

One gpt-5.4-mini vote weighed by the fresh-agent pre-run critic (verdict authority). Mirrors the
German arm's VOTE-critic-s213.json. Sends the FROZEN items + the gold mapping and asks for a
Japanese-CC-fidelity + gold audit and a GO / GO-WITH-CONDITIONS / NO-GO verdict. Saves
VOTE-critic-s215.json (with billed usage.cost). ~$0.003.

Run: OPENROUTER_API_KEY=... python3 vote_critic.py
"""
import csv, json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                     "comparative-correlative-japanese", "items.csv"))

PREAMBLE = (
    "あなたの学習データは古いかもしれませんが、この作業は自己完結した言語学的監査です。外部知識ではなく、"
    "提示された項目そのものの日本語の文法性と正解ラベルの整合性を判断してください。\n\n"
)

SYS = (
    "You are an independent, adversarial pre-run critic for a frozen Japanese linguistics experiment. "
    "You are a NATIVE-LEVEL Japanese grammar auditor. Do not rubber-stamp; find real defects."
)


def build_listing():
    rows = list(csv.DictReader(open(ITEMS)))
    by_pair = {}
    for r in rows:
        by_pair.setdefault(r["scale_pair"], {})[r["form"]] = r
    lines = []
    for pid, forms in by_pair.items():
        typ = forms["cc-positive"]["typicality"]
        d1 = forms["cc-positive"]["dim1"]; d2 = forms["cc-positive"]["dim2"]
        lines.append(f"[{pid} | {typ} | dim1={d1} dim2={d2}]")
        for f in ("cc-positive", "cc-inverse", "ctrl-two", "ctrl-single"):
            lines.append(f"  {f} (fc_gold={forms[f]['fc_gold']}): {forms[f]['sentence']}")
    return "\n".join(lines)


def main():
    listing = build_listing()
    user = PREAMBLE + (
        "これは、フラッグシップの『比較相関構文 (comparative correlative)』の共変動結果を日本語 (〜ば〜ほど) "
        "で追試する、凍結済みの実験項目です。主張はモデル内部の対比のみ (internal-contrast-only、人間比較なし)："
        "モデルが共変動の読みを『構文』に帰属できるか——CC項目では共変動方向を主張するが、同じ語を使った非CC統制"
        "文では主張しないか。\n\n"
        "4形式 (各スケール対で同じ語を使い回す)：\n"
        "- cc-positive: 〜ば〜ほど で dim2 が上がる → 正解 fc_gold=increase\n"
        "- cc-inverse : 同じ 〜ば〜ほど 前件で dim2 が下がる → 正解 fc_gold=decrease "
        "(FC質問は dim2 を肯定形で尋ねる。反意/減少表現で『名指しされた dim2 スケール』が確実に下がる必要がある)\n"
        "- ctrl-two   : 独立した2文 (依存関係なし) → 正解 undetermined\n"
        "- ctrl-single: スケールを1つだけ述べる (dim2 に触れない) → 正解 undetermined\n\n"
        "監査してください：\n"
        "(1) 文法性：各 cc-positive / cc-inverse は正しい 〜ば〜ほど 構文か (前件 = [述語ば][述語]ほど の反復、"
        "文末述語)。非文・不自然で誤読を招くものを item ごとに指摘。\n"
        "(2) cc-inverse：名指しされた dim2 スケールが確実に『減少』方向になっているか。曖昧なものを指摘。\n"
        "(3) 統制文：ctrl-two / ctrl-single が本当に 〜ば〜ほど を欠くか (undetermined が正しいか)。\n"
        "(4) 正解ラベルの誤りがあれば指摘。\n\n"
        "最後に判定を一語で：GO / GO-WITH-CONDITIONS / NO-GO。問題は item 名を挙げて具体的に。\n\n"
        "=== 項目一覧 ===\n" + listing
    )
    r = call(PANEL["B"], SYS, user, max_tokens=1600)
    cost, have, missing = billed_cost([[r]])
    out = {
        "model": PANEL["B"],
        "role": "pre-run critic decorrelation vote + Japanese-fidelity audit",
        "billed_usd": round(cost, 6),
        "content": r.get("content"),
        "error": r.get("error"),
    }
    with open(os.path.join(HERE, "VOTE-critic-s215.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"billed: ${cost:.6f}  (have={have} missing={missing})")
    print("\n" + (r.get("content") or f"ERROR: {r.get('error')}"))


if __name__ == "__main__":
    main()
