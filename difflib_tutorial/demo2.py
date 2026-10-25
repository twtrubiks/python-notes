# unified_diff - 產生類似 git diff 的輸出 (最常用)
from difflib import unified_diff

if __name__ == "__main__":
    old = """def greet(name):
    print("Hello")
    return True
""".splitlines(keepends=True)

    new = """def greet(name):
    print(f"Hello, {name}")
    print("Welcome!")
    return True
""".splitlines(keepends=True)

    # keepends=True 保留每行結尾的換行, 否則輸出會黏在一起
    # fromfile / tofile 是顯示在 --- 和 +++ 後面的名稱
    diff = unified_diff(old, new, fromfile="old.py", tofile="new.py")
    print("".join(diff))

    # n 控制上下文要顯示幾行, 預設 3, 設 0 就只顯示有變動的行
    diff = unified_diff(old, new, fromfile="old.py", tofile="new.py", n=0)
    print("".join(diff))

    # 回傳的是 generator, 想知道有沒有差異可以直接轉成 list
    same = list(unified_diff(old, old))
    print(same)  # [] 代表完全相同
