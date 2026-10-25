# SequenceMatcher - 計算兩個序列的相似度
from difflib import SequenceMatcher

if __name__ == "__main__":
    a = "hello world"
    b = "hello python"

    sm = SequenceMatcher(None, a, b)

    # ratio() 回傳 0 ~ 1 的相似度, 1 代表完全相同
    # 公式: 2.0 * M / T, M 是配對到的字元數, T 是兩個序列的總長度
    print(sm.ratio())  # 0.6086956521739131

    # get_opcodes() 列出 a 要怎麼變成 b
    # tag 有 'equal', 'replace', 'delete', 'insert'
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        print(f"{tag:8} a[{i1}:{i2}]={a[i1:i2]!r:12} b[{j1}:{j2}]={b[j1:j2]!r}")

    # 不只字串, list 也可以比
    print(SequenceMatcher(None, [1, 2, 3, 4], [1, 2, 4]).ratio())  # 0.857...
