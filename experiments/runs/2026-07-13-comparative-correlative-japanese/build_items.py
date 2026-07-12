"""Build and freeze the Japanese CC item set (A6 cross-linguistic replication, 2026-07-13, s215).

A faithful PORT of the frozen English v1/powered comparative-correlative instrument
(experiments/runs/2026-07-02-comparative-correlative-powered) — and byte-parallel in SHAPE to the
German port (experiments/runs/2026-07-12-comparative-correlative-german) — to Japanese, per the
ratified scope decision decisions/resolved/cross-linguistic-cc-replication-scope
(Q1-C: German first, JAPANESE the committed-but-conditional stronger successor / Q2-B same-word +
freq-matched control / Q3-A internal-contrast-only). Same FOUR item forms, same construction-correct
gold answers, same typical/atypical split (24 typical + 10 atypical = 34 scale pairs x 4 forms = 136
items) — the ONLY change vs the German/English instrument is the target LANGUAGE. Japanese is the
STRONGER anti-template lever (Q1-C freeze condition vii): typologically distant (SOV, agglutinative,
NO overt comparative morpheme -er/mehr/desto — the "more" is carried entirely by the ば...ほど frame
+ predicate repetition), so a much larger surface-statistics distance from English than German.

Japanese CC construction (source-verified + self-audited against
base/sources/japanese-ba-hodo-cc.md, freeze conditions ii + viii):
  ANTECEDENT (X scale):  [Pred-ば] [Pred] ほど   (predicate stated in ば-conditional, then REPEATED)
    i-adjective : A-kereba A-i hodo   (厚ければ厚いほど)
    na-adjective: NA-de areba aru hodo / NA nara NA na hodo   (平らであればあるほど)
    verb        : V-ba V hodo   (光れば光るほど)
  CONSEQUENT (Y scale): the ordinary verb-final main clause, whose scalar predicate RISES
    (くなる / になる / 増える / 上がる) or FALLS (antonym predicate / 減る / 下がる / なくなる).

Four forms per scale pair, reusing the SAME scalar lexical material (the same-word non-CC controls,
Q2-A core leg — the scalar words are held constant so the construction-isolation gap is purely the
ば...ほど syntax):
  cc-positive  : "X-ば X-ほど, Y increases"   -> covariation direction = increase
  cc-inverse   : "X-ば X-ほど, Y decreases (antonym)" -> covariation direction = decrease
  ctrl-two     : two independent declarative clauses (both scales asserted, no dependency)
  ctrl-single  : a single scalar clause (only ONE scale mentioned; yori-comparison)

Construction-correct answers (fixed here, BEFORE the run — anti-cheat freeze, condition iii):
  forced-choice (as dim1 increases, does dim2 increase / decrease / undetermined):
    cc-positive -> increase ; cc-inverse -> decrease ; both controls -> undetermined
  NLI (premise = sentence, hypothesis = "<dim1>が増すと、<dim2>も増す。"):
    cc-positive -> 0 entailment ; cc-inverse -> 2 contradiction ; both controls -> 1 neutral

Emits experiments/data/comparative-correlative-japanese/items.csv; committed BEFORE any probe call.
Scale pairs are authored so the covariation direction is NOT world-knowledge-obvious (typical) or is
deliberately absurd (atypical) — the construction, not plausibility, must supply the direction.
"""
import csv, os

# pid, typicality, dim1 (Japanese scale NP so "<dim1>が増す" reads), dim2 (Japanese scale NP),
# cc_pos, cc_inv, ctrl_two, ctrl_single
PAIRS = [
    # ---- typical (24): plausible-either-direction pairs (direction not obvious) ----
    ("roman", "typical", "小説の厚さ", "読者の辛抱強さ",
     "小説が厚ければ厚いほど、読者は辛抱強くなった。",
     "小説が厚ければ厚いほど、読者は飽きっぽくなった。",
     "小説は厚かった。読者は辛抱強かった。",
     "小説は前作より厚かった。"),
    ("oven", "typical", "オーブンの熱さ", "客の数",
     "オーブンが熱ければ熱いほど、客が増えた。",
     "オーブンが熱ければ熱いほど、客が減った。",
     "オーブンは熱かった。客が大勢来た。",
     "オーブンはいつもより熱かった。"),
    ("seminar", "typical", "セミナーの大きさ", "議論の量",
     "セミナーが大きければ大きいほど、議論が増えた。",
     "セミナーが大きければ大きいほど、議論が減った。",
     "セミナーは大きかった。議論は活発だった。",
     "セミナーは講義より大きかった。"),
    ("summer", "typical", "夏の暑さ", "りんごの甘さ",
     "夏が暑ければ暑いほど、りんごは甘くなった。",
     "夏が暑ければ暑いほど、りんごの甘みが減った。",
     "夏は暑かった。りんごは甘かった。",
     "夏は去年より暑かった。"),
    ("road", "typical", "道路の広さ", "運転手の速さ",
     "道路が広ければ広いほど、運転手は速く走った。",
     "道路が広ければ広いほど、運転手はゆっくり走った。",
     "道路は広かった。運転手は速く走った。",
     "道路は旧道より広かった。"),
    ("gallery", "typical", "ギャラリーの暗さ", "来場者のささやき",
     "ギャラリーが暗ければ暗いほど、来場者はひそひそと話した。",
     "ギャラリーが暗ければ暗いほど、来場者は声高に話した。",
     "ギャラリーは暗かった。来場者はひそひそと話した。",
     "ギャラリーはロビーより暗かった。"),
    ("startup", "typical", "スタートアップの規模", "投資家の慎重さ",
     "スタートアップが大きければ大きいほど、投資家は慎重になった。",
     "スタートアップが大きければ大きいほど、投資家は慎重でなくなった。",
     "スタートアップは大きかった。投資家は慎重だった。",
     "スタートアップは競合より大きかった。"),
    ("harbor", "typical", "港の忙しさ", "魚の値段",
     "港が忙しければ忙しいほど、魚の値段が上がった。",
     "港が忙しければ忙しいほど、魚の値段が下がった。",
     "港は忙しかった。魚の値段は高かった。",
     "港は冬より忙しかった。"),
    ("clinic", "typical", "待合室の暖かさ", "患者の眠気",
     "待合室が暖かければ暖かいほど、患者は眠くなった。",
     "待合室が暖かければ暖かいほど、患者は目が冴えた。",
     "待合室は暖かかった。患者は眠そうだった。",
     "待合室は廊下より暖かかった。"),
    ("vineyard", "typical", "ぶどう畑の険しさ", "摘み手の賃金",
     "ぶどう畑が険しければ険しいほど、摘み手の賃金が上がった。",
     "ぶどう畑が険しければ険しいほど、摘み手の賃金が下がった。",
     "ぶどう畑は険しかった。摘み手の賃金は高かった。",
     "ぶどう畑は果樹園より険しかった。"),
    ("pool", "typical", "プールの冷たさ", "泳者の泳ぐ距離",
     "プールが冷たければ冷たいほど、泳者は長く泳いだ。",
     "プールが冷たければ冷たいほど、泳者は短く泳いだ。",
     "プールは冷たかった。泳者は長く泳いだ。",
     "プールは海より冷たかった。"),
    ("shelves", "typical", "棚の高さ", "司書の歩く速さ",
     "棚が高ければ高いほど、司書は速く歩いた。",
     "棚が高ければ高いほど、司書はゆっくり歩いた。",
     "棚は高かった。司書は速く歩いた。",
     "棚は閲覧机より高かった。"),
    ("band", "typical", "バンドの音の大きさ", "踊る人の数",
     "バンドの音が大きければ大きいほど、踊る人が増えた。",
     "バンドの音が大きければ大きいほど、踊る人が減った。",
     "バンドの音は大きかった。踊る人は多かった。",
     "バンドの音は前座より大きかった。"),
    ("field", "typical", "畑の平らさ", "農家の収穫",
     "畑が平らであればあるほど、農家の収穫が増えた。",
     "畑が平らであればあるほど、農家の収穫が減った。",
     "畑は平らだった。農家の収穫は多かった。",
     "畑は斜面より平らだった。"),
    ("brochure", "typical", "パンフレットの美しさ", "買い手の信頼",
     "パンフレットが美しければ美しいほど、買い手はそれを信頼した。",
     "パンフレットが美しければ美しいほど、買い手はそれを信頼しなくなった。",
     "パンフレットは美しかった。買い手はそれを信頼した。",
     "パンフレットはチラシより美しかった。"),
    ("theater", "typical", "劇場の暗さ", "観客のざわめき",
     "劇場が暗ければ暗いほど、観客はざわついた。",
     "劇場が暗ければ暗いほど、観客は静かになった。",
     "劇場は暗かった。観客はざわついた。",
     "劇場はゲネプロのときより暗かった。"),
    ("curry", "typical", "カレーの辛さ", "客のおしゃべり",
     "カレーが辛ければ辛いほど、客はおしゃべりになった。",
     "カレーが辛ければ辛いほど、客は無口になった。",
     "カレーは辛かった。客はよくしゃべった。",
     "カレーは前菜より辛かった。"),
    ("syllabus", "typical", "シラバスの長さ", "学生の熱意",
     "シラバスが長ければ長いほど、学生は熱心になった。",
     "シラバスが長ければ長いほど、学生は無気力になった。",
     "シラバスは長かった。学生は熱心だった。",
     "シラバスは前学期より長かった。"),
    ("current", "typical", "流れの速さ", "釣り人の苛立ち",
     "流れが速ければ速いほど、釣り人はいらだった。",
     "流れが速ければ速いほど、釣り人は落ち着いた。",
     "流れは速かった。釣り人はいらだっていた。",
     "流れは明け方より速かった。"),
    ("kitchen", "typical", "厨房のきれいさ", "料理人の雑談",
     "厨房がきれいであればあるほど、料理人はよく雑談した。",
     "厨房がきれいであればあるほど、料理人は口数が少なくなった。",
     "厨房はきれいだった。料理人はよく雑談した。",
     "厨房は食料庫よりきれいだった。"),
    ("path", "typical", "小道の狭さ", "登山者の間隔",
     "小道が狭ければ狭いほど、登山者の間隔が広がった。",
     "小道が狭ければ狭いほど、登山者の間隔が縮まった。",
     "小道は狭かった。登山者の間隔は広かった。",
     "小道は林道より狭かった。"),
    ("auction", "typical", "競売場の明るさ", "収集家の滞在時間",
     "競売場が明るければ明るいほど、収集家は長く留まった。",
     "競売場が明るければ明るいほど、収集家は早く立ち去った。",
     "競売場は明るかった。収集家は長く留まった。",
     "競売場は金庫室より明るかった。"),
    ("soil", "typical", "土の砂っぽさ", "水やりの頻度",
     "土が砂っぽければ砂っぽいほど、庭師はよく水をやった。",
     "土が砂っぽければ砂っぽいほど、庭師はあまり水をやらなくなった。",
     "土は砂っぽかった。庭師はよく水をやった。",
     "土は粘土の花壇より砂っぽかった。"),
    ("hall", "typical", "会場の大きさ", "ファンの盛り上がり",
     "会場が大きければ大きいほど、ファンは盛り上がった。",
     "会場が大きければ大きいほど、ファンはおとなしくなった。",
     "会場は大きかった。ファンは盛り上がった。",
     "会場はクラブより大きかった。"),
    # ---- atypical (10): deliberately absurd pairings (world knowledge gives NO direction;
    #      covariation can ONLY come from the construction) ----
    ("teacup", "atypical", "ティーカップの丸さ", "渋滞の長さ",
     "ティーカップが丸ければ丸いほど、渋滞は長くなった。",
     "ティーカップが丸ければ丸いほど、渋滞は短くなった。",
     "ティーカップは丸かった。渋滞は長かった。",
     "ティーカップは湯のみより丸かった。"),
    ("carpet", "atypical", "じゅうたんの赤さ", "エレベーターの速さ",
     "じゅうたんが赤ければ赤いほど、エレベーターは速くなった。",
     "じゅうたんが赤ければ赤いほど、エレベーターは遅くなった。",
     "じゅうたんは赤かった。エレベーターは速かった。",
     "じゅうたんはカーテンより赤かった。"),
    ("pancake", "atypical", "パンケーキの柔らかさ", "山の高さ",
     "パンケーキが柔らかければ柔らかいほど、山は高くそびえた。",
     "パンケーキが柔らかければ柔らかいほど、山は低くなった。",
     "パンケーキは柔らかかった。山は高くそびえていた。",
     "パンケーキはワッフルより柔らかかった。"),
    ("stapler", "atypical", "ホチキスの重さ", "夕日の明るさ",
     "ホチキスが重ければ重いほど、夕日は明るく輝いた。",
     "ホチキスが重ければ重いほど、夕日は暗くなった。",
     "ホチキスは重かった。夕日は明るく輝いていた。",
     "ホチキスはテープカッターより重かった。"),
    ("sock", "atypical", "靴下の縞の多さ", "雷の大きさ",
     "靴下の縞が多ければ多いほど、雷は大きく鳴った。",
     "靴下の縞が多ければ多いほど、雷は小さく鳴った。",
     "靴下には縞が多かった。雷は大きく鳴った。",
     "靴下は手袋より縞が多かった。"),
    ("lampshade", "atypical", "ランプシェードの広さ", "ヨーグルトの酸っぱさ",
     "ランプシェードが広ければ広いほど、ヨーグルトは酸っぱくなった。",
     "ランプシェードが広ければ広いほど、ヨーグルトは甘くなった。",
     "ランプシェードは広かった。ヨーグルトは酸っぱかった。",
     "ランプシェードは台座より広かった。"),
    ("keyboard", "atypical", "キーボードのほこりっぽさ", "収穫の多さ",
     "キーボードがほこりっぽければほこりっぽいほど、収穫が増えた。",
     "キーボードがほこりっぽければほこりっぽいほど、収穫が減った。",
     "キーボードはほこりっぽかった。収穫は多かった。",
     "キーボードはモニターよりほこりっぽかった。"),
    ("balloon", "atypical", "風船の輝き", "井戸の深さ",
     "風船が光れば光るほど、井戸は深くなった。",
     "風船が光れば光るほど、井戸は浅くなった。",
     "風船は光っていた。井戸は深かった。",
     "風船はリボンより光っていた。"),
    ("envelope", "atypical", "封筒のしわの多さ", "列車の速さ",
     "封筒のしわが多ければ多いほど、列車は速く走った。",
     "封筒のしわが多ければ多いほど、列車は遅く走った。",
     "封筒にはしわが多かった。列車は速く走った。",
     "封筒は小包よりしわが多かった。"),
    ("pinecone", "atypical", "松ぼっくりのべたつき", "散髪の値段",
     "松ぼっくりがべたつけばべたつくほど、散髪の値段が上がった。",
     "松ぼっくりがべたつけばべたつくほど、散髪の値段が下がった。",
     "松ぼっくりはべたついていた。散髪の値段は高かった。",
     "松ぼっくりはどんぐりよりべたついていた。"),
]

# construction-correct gold: (form, fc_gold, nli_gold)
FORMS = [
    ("cc-positive",   "increase",     "0"),
    ("cc-inverse",    "decrease",     "2"),
    ("ctrl-two",      "undetermined", "1"),
    ("ctrl-single",   "undetermined", "1"),
]


def sentence_for(pair, form):
    _, _, _, _, cc_pos, cc_inv, ctrl_two, ctrl_single = pair
    return {"cc-positive": cc_pos, "cc-inverse": cc_inv,
            "ctrl-two": ctrl_two, "ctrl-single": ctrl_single}[form]


def main():
    out = os.path.join(os.path.dirname(__file__), "..", "..",
                       "data", "comparative-correlative-japanese", "items.csv")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # integrity guards (ENFORCED): unique pids, correct split, four forms each.
    pids = [p[0] for p in PAIRS]
    assert len(pids) == len(set(pids)), f"duplicate pid: {[p for p in pids if pids.count(p) > 1]}"
    n_typ = sum(1 for p in PAIRS if p[1] == "typical")
    n_aty = sum(1 for p in PAIRS if p[1] == "atypical")
    assert (n_typ, n_aty) == (24, 10), f"split drifted: {n_typ} typical + {n_aty} atypical"
    rows = []
    for pair in PAIRS:
        pid, typ, dim1, dim2 = pair[0], pair[1], pair[2], pair[3]
        for form, fc_gold, nli_gold in FORMS:
            sent = sentence_for(pair, form)
            rows.append({
                "item_id": f"{pid}-{form}",
                "scale_pair": pid,
                "typicality": typ,
                "form": form,
                "dim1": dim1,
                "dim2": dim2,
                "sentence": sent,
                "fc_gold": fc_gold,
                "nli_hypothesis": f"{dim1}が増すと、{dim2}も増す。",
                "nli_gold": nli_gold,
            })
    cols = ["item_id", "scale_pair", "typicality", "form", "dim1", "dim2",
            "sentence", "fc_gold", "nli_hypothesis", "nli_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} items ({len(PAIRS)} pairs x {len(FORMS)} forms) -> {out}")
    print(f"  typical pairs: {n_typ}, atypical pairs: {n_aty}")


if __name__ == "__main__":
    main()
