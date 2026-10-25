# HtmlDiff - 產生並排的 HTML 差異比較頁面
from difflib import HtmlDiff
from pathlib import Path

if __name__ == "__main__":
    old = ["apple", "banana", "cherry"]
    new = ["apple", "blueberry", "cherry", "date"]

    # make_file() 產生完整的 HTML 檔 (含 <html> <style>)
    # make_table() 只產生 <table>, 方便塞進自己的頁面
    html = HtmlDiff().make_file(old, new, fromdesc="舊版", todesc="新版")

    output = Path(__file__).with_name("diff.html")
    output.write_text(html, encoding="utf-8")
    print(f"已輸出 {output}, 用瀏覽器打開可以看到並排的彩色差異表")

    # wrapcolumn 可以設定超過幾個字元就自動換行
    # context=True 搭配 numlines 只顯示有差異的區段附近幾行
    html_short = HtmlDiff(wrapcolumn=40).make_table(
        old, new, fromdesc="舊版", todesc="新版", context=True, numlines=1
    )
    print(len(html_short))
