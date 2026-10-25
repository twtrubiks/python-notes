# Differ / ndiff - 逐行比較, 並標記出行內的差異位置
# restore - 從 diff 結果還原出原始版本
from difflib import Differ, ndiff, restore

if __name__ == "__main__":
    old = ["cat\n", "dog\n", "fish\n"]
    new = ["cat\n", "horse\n", "fish\n", "bird\n"]

    # 每行開頭的符號:
    #   '  ' 兩邊都有, 沒變
    #   '- ' 只在 old 有 (被移除)
    #   '+ ' 只在 new 有 (新增)
    #   '? ' 提示行, 用 ^ - + 標出上一行哪個位置有差異
    diff = Differ().compare(old, new)
    print("".join(diff))

    # 兩行很相似時, 會多給一行 ? 標出差在哪個字元, 這是 unified_diff 做不到的
    old2 = ["print('hello world')\n"]
    new2 = ["print('hello python')\n"]
    print("".join(Differ().compare(old2, new2)))
    # - print('hello world')
    # ?              ^ ^^^
    # + print('hello python')
    # ?              ^^^^ ^

    # ndiff() 是 Differ().compare() 的快捷寫法, 結果一樣
    diff = list(ndiff(old, new))
    print("".join(diff))

    # restore() 可以從 ndiff 的結果還原出原始內容
    # 第二個參數 1 = 還原 old, 2 = 還原 new
    # 適合只存 diff 不存全文的情境
    print("".join(restore(diff, 1)))  # cat dog fish
    print("".join(restore(diff, 2)))  # cat horse fish bird
