# get_close_matches - 模糊匹配, 拼字建議
from difflib import get_close_matches

if __name__ == "__main__":
    words = ["apple", "application", "banana", "apply", "appreciate"]

    # n: 最多回傳幾個
    # cutoff: 相似度門檻 (0 ~ 1), 低於這個值的不回傳
    # 回傳結果會依相似度由高到低排序
    matches = get_close_matches("appla", words, n=3, cutoff=0.6)
    print(matches)  # ['apply', 'apple', 'application']
    # apply 和 appla 只差一個字母, 所以相似度最高排第一

    # 門檻拉高就會篩掉比較不像的
    print(get_close_matches("appla", words, n=3, cutoff=0.8))  # ['apply', 'apple']

    # 完全沒有符合的回傳空 list
    print(get_close_matches("zzz", words))  # []

    # 實際應用: 使用者打錯指令時給建議, 像 git 的 "did you mean"
    commands = ["commit", "checkout", "cherry-pick", "clone", "config"]
    user_input = "comit"
    suggestion = get_close_matches(user_input, commands, n=1)
    if suggestion:
        print(f"'{user_input}' is not a command. Did you mean '{suggestion[0]}'?")
