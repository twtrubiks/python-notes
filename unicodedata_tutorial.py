# ref. https://docs.python.org/3.6/library/unicodedata.html
import unicodedata


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


if __name__ == "__main__":
    a = unicodedata.category('A')  # 'L'etter, 'u'ppercase
    print('a:', a)
    b = unicodedata.category('\r')  # carriage return Cc : control character
    print('b:', b)
    c = unicodedata.category('\t')  # tab  Cc : control character
    print('c:', c)
    d = unicodedata.category('\v')  # vertical tabulation.  Cc : control character
    print('d:', d)
    demo = "\tA\rB\v"
    print('demo:', demo)
    print('remove_control:', remove_control_characters(demo))
