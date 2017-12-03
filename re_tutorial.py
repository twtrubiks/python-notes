import re

'''
ref.
https://docs.python.org/3/library/re.html 
http://www.runoob.com/python/python-reg-expressions.html
https://goo.gl/cPmofe

使用 re module 之前，先思考一下你的問題是否可以用其他方法解決，
像是 replace , split , translate
'''

if __name__ == "__main__":
    '''
    re.sub(pattern, repl, string, count=0, flags=0)    
    '''

    # ex1. 符合 "a", "b", 或 "c" 中的任意一個字
    str_ex1 = "1a2b3c4d"
    num = re.sub(r'[abc]', "", str_ex1)
    print('num:', num)

    # ex2. 符合 "a", "b", 或 "c" 中的任意一個字, a 到 c 區間
    # str_ex2 = "1a2b3c4d"
    # num = re.sub(r'[a-c]', "", str_ex2)
    # print('num:', num)

    # ex1 和 ex2 功能相同

    # ex3. 符合小寫英文字母
    # str_ex3 = "1a2b3c4dABC"
    # num = re.sub(r'[a-z]', "", str_ex3)
    # print('num:', num)

    # ex4. [^5] 將符合除了 "5" 之外的任意字
    # str_ex4 = "1a2b3c4dABC55"
    # num = re.sub(r'[^5]', "", str_ex4)
    # print('num:', num)

    # ex5. [abc$] 將符合 "a" , "b" , "c" , "$"
    # str_ex5 = "d1abs$"
    # num = re.sub(r'[abc$]', "", str_ex5)
    # print(num)

    '''
    非常重要的字符為反斜槓 "\" ，
    如果你需要匹配 "[" 或 """，你可以在它們之前用"\"來取消它們的特殊意義： \[ 或 \"。
    
    這類特殊字符都可以包含在一個字符類中。如 [\s,.] 字符類將匹配任何空白字符或 "," 或 "."
    '''

    # ex6_1
    # str_ex6_1 = "swedaf\"gb"
    # print(str_ex6_1)
    # num = re.sub(r"\"", "", str_ex6_1)
    # print(num)

    # ex6_2
    # str_ex6_2 = "swedaf[gb"
    # print(str_ex6_2)
    # num = re.sub(r'\[', "", str_ex6_2)
    # print(num)

    '''
    \d  匹配任何十進制數；它相當於類 [0-9]。
    \D  匹配任何非數字字符；它相當於類 [^0-9]。
    \s  匹配任何空白字符；它相當於類  [ "t"n"r"f"v]。 
    \S  匹配任何非空白字符；它相當於類 [^ "t"n"r"f"v]。 
    \w  匹配任何字母數字字符；它相當於類 [a-zA-Z0-9_]。
    \W  匹配任何非字母數字字符；它相當於類 [^a-zA-Z0-9_]。
    '''

    '''
    正則表達式通常在 Python 中都用這種 raw 字符表示。
    在字符前加個 "r" 反斜槓就不會被任何特殊方式處理，
    所以 r"\n" 就是包含"\" 和 "n" 的兩個字，
    而 "\n" 則是一個字，表示一個換行。
    '''
    # ex7_1
    # print("\n")
    # print("len:", len("\n"))
    # ex7_2
    # print(r"\n")
    # print("len:", len(r"\n"))
    # ex7_3  符合 \section
    # str_ex7_3 = "aaa\sectionbc"
    # print('origin:', str_ex7_3)
    # num = re.sub(r'\\section', "", str_ex7_3)
    # print('new:', num)

    '''        
    match()	    決定 RE 是否在字符串剛開始的位置匹配
    search()	掃瞄字符串，找到這個 RE 匹配的位置
    findall()	找到 RE 匹配的所有子串，並把它們作為一個列表返回
    finditer()	找到 RE 匹配的所有子串，並把它們作為一個迭代器返回
    
    如果沒有匹配到的話，match() 和 search() 將返回 None。
    如果成功的話，就會返回一個 `MatchObject` 實例。
    
    '''

    '''
    re.match
    re.match(pattern, string, flags=0)
    '''
    # ex8_1 回傳 None
    # '+' 的意思是 「一個或更多的重複次數」
    # num = re.match(r'[a-z]+', '')
    # print(num)
    # ex8_2 回傳一個 MatchObject
    # num = re.match(r'[a-z]+', 's')
    # print(num)

    '''
    group()	返回被 RE 匹配的字符串
    start()	返回匹配開始的位置
    end()	返回匹配結束的位置
    span()	返回一個元組包含匹配 (開始,結束) 的位置
    '''
    # ex9_1
    # num = re.match('[a-z]+', 's123')
    # print('num.group()', num.group())
    # print('num.start()', num.start())
    # print('num.end()', num.end())
    # print('num.span()', num.span())

    # ex9_2
    # p = re.compile('[a-z]+')
    # print(p.match('::: message'))
    # m = p.search('::: message')
    # print('m.group()', m.group())
    # print('m.span()', m.span())

    '''     
    m = re.compile(pattern)
    result = m.match(string)
    # 等同與
    result = re.match(pattern, string)
    '''

    # ex10
    # p = re.compile('\d+')
    # m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    # print(m)

    # ex11_1
    # m = re.match(r'From\s+', 'Fromage amk')
    # print(m)
    # ex11_2
    # m1 = re.match(r'From\s+', 'From age amk')
    # print(m1)

    '''
    DOTALL,     S	使 . 匹配包括換行在內的所有字符
    IGNORECASE, I	使匹配對大小寫不敏感
    LOCALE,     L	做本地化識別（locale-aware）匹配
    MULTILINE,  M	多行匹配，影響 ^ 和 $
    VERBOSE,    X	能夠使用 REs 的 verbose 狀態，使之被組織得更清晰易懂
    '''
    # ex12
    # 符合不分大小寫英文字母 輸出會空的 IGNORECASE
    # str1 = 'dasAWAa'
    # num = re.sub(r'[a-z]', "", str1, flags=re.I)
    # print('output:', num)

    # ex13
    # |  可選項，或者 "or" 操作符
    # m = re.findall(r'From|amk', 'Fromage amkdasd')
    # print(m)

    # ^ 匹配行首
    # ex14
    # m = re.findall(r'^From', 'Fromage amkdasd')
    # print(m)

    # 匹配行尾，行尾被定義為要麼是字符串尾
    # ex15
    # m = re.findall('13$', '{blo3ck}13')
    # print(m)
    # p.s 匹配一個 "$"，使用 "$ 或將其包含在字符類中，如[$],請參考範例 ex5

    #  \b 單詞邊界。這是個零寬界定符（zero-width assertions）只用以匹配單詞的詞首和詞尾。
    # 下面的例子只匹配 "class" 整個單詞；而當它被包含在其他單詞中時不匹配。
    # ex16_1
    # m = re.findall(r'class\b', 'no class at all')
    # print('output:', m)
    # ex16_2
    # m1 = re.findall(r'class\b', 'no classat all')
    # print('output:', m1)

    #  \B 另一個零寬界定符（zero-width assertions），它正好同 \b 相反，
    # 只在當前位置不在單詞邊界時匹配。
    # ex17_1
    # m = re.findall(r'class\B', 'no class at all')
    # print('output:', m)
    # ex17_2
    # m1 = re.findall(r'class\B', 'no classat all')
    # print('output:', m1)

    '''
    split()	將字符串在 RE 匹配的地方分片並生成一個列表，
    sub()	找到 RE 匹配的所有子串，並將其用一個不同的字符串替換
    subn()	與 sub() 相同，但返回新的字符串和替換次數
    '''
    # \W  匹配任何非字母數字字符；它相當於類 [^a-zA-Z0-9_]。
    # ex18_1
    # m = re.split(r'[T]', 'This is a test, short and sweet, of split().')
    # print(m)
    # ex18_2
    # m = re.split(r'\W+', 'This is a test, short and sweet, of split().')
    # print(m)

    # sub(replacement, string[, count = 0])
    # ex19_1
    # num = re.sub(r'[abc$]', "", 'd1as$')
    # print(num)
    # ex19_2
    # m = re.sub(r'blue|white|red', '', 'blue socks and red shoe')
    # print(m)

    '''
    match() vs search()
    match() 函數只檢查 RE 是否在字符串開始處匹配，而 search() 則是掃瞄整個字符串。
    記住，match() 只報告一次成功的匹配，它將從 0 處開始；
    如果匹配不是從 0 開始的，match() 將不會報告它。
    '''
    # ex20_1
    # print(re.match('super', 'superstition').span())
    # print(re.match('super', 'insuperable'))
    # # ex20_2
    # print(re.search('super', 'superstition').span())
    # print(re.search('super', 'insuperable'))
