# commitizen and pre-commit 教學

[Youtube Tutorial - commitizen 和 pre-commit 套件介紹](https://youtu.be/hdDwy8wb5v8)

今天要介紹兩個東西, 分別是 commitizen 和 pre-commit

## commitizen

commitizen 簡單說就是規格化 commit, 不然大家 commit 都亂打:sweat_smile:

文件可參考 [commitizen](https://github.com/commitizen-tools/commitizen)

```cmd
pip install -U commitizen
```

安裝完後, 當我們 `git add .` 完之後,

執行執行 `cz commit` 或 `cz c` 即可

![img](https://i.imgur.com/OweniDG.png)

接著你會看到要你輸入一些資訊(這些可以依照你們的團隊決定)

![img](https://i.imgur.com/D1YEPLF.png)

![img](https://i.imgur.com/9K2lXaJ.png)

那接下來可能會遇到一個問題,

就是會不會忘記執行 `cz c`, 然後用一般的 commit 方式,

答案是肯定會忘記的 :smile:

所以有了以下的 pre-commit

## pre-commit

文件可參考 [pre-commit](https://pre-commit.com/)

```cmd
pip install pre-commit
```

之後, 建立一個 [.pre-commit-config.yaml](.pre-commit-config.yaml) 放在目錄底下,

內容填入

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.9.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  - repo: https://github.com/python/black
    rev: 23.9.1
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
```

最後安裝你的 git hook scripts

```cmd
pre-commit install --hook-type commit-msg
```

也可以直接執行以下一次全部安裝

```cmd
pre-commit install
```

Install the git hook scripts

![img](https://i.imgur.com/fWFMqRM.png)

這樣子當你下次忘記用 `cz c` 執行 commit,

而是用一般的 commit 時, 就會跳出錯誤提醒你

( 第一次會慢一點, 之後就會很快了:smile: )

![img](https://i.imgur.com/I7vL7KT.png)

不只有 commitizen 可以用在 pre-commit,

像是 `flake8` `black` 這些很多都可以......

簡單說, 你可以把他想成是多一層檢查這樣:smile:
