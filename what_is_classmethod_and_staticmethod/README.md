# What is the classmethod and staticmethod in python

[Youtube Tutorial - What is the classmethod and staticmethod in python](https://youtu.be/LUQ3dHTkWUE)

這篇文章主要會介紹 classmethod 和 staticmethod，在介紹之前，建議大家對 decorator 有一些基本的認識，

如果不了解，可參考 [What is the python decorator](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_python_decorator)。

python 中有幾個內建的 decorator，今天要來和大家介紹其中的 **classmethod** 和 **staticmethod**。

這邊我不多做解釋，直接來看程式碼，先來看一個 staticmethod 的範例，

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_classmethod_and_staticmethod/demo1.py)

```python
class Dates:
    def __init__(self, date):
        self._date = date

    def get_date(self):
        return self._date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


def main():
    date = Dates("2018-10-10") # <1>
    print('date.get_date():', date.get_date()) # <2>
    date_from_birthday = "2018/12/12"
    date_with_dash = Dates.to_dash_date(date_from_birthday) # <3>
    print('date_with_dash:', date_with_dash)

if __name__ == "__main__":
    main()
```

<1> 的部分，建立一個 date 實例。

<2> 的部分，是我們一般比較常用的方法。

<3> 的部分，就是我們的 **staticmethod**，這邊要注意的是，在 `to_dash_date(date)` 中，

完全沒有使用到任何 Dates class 中的屬性或是 properties，而且也不需要知道 Dates class 中

有哪些東西可以使用，因為他只處理傳進來的參數。( 儘管如此，`to_dash_date(date)` 還是屬於

Dates class 中的一個 method )

接著來看 classmethod 的範例，

[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_classmethod_and_staticmethod/demo2.py)

```python
from datetime import date

# Create simple factory method using class method # <1>
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, birth_year): # <4>
        print('cls:', cls) # <5>
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


def main():
    person = Person('twtrubiks', 18) # <2>
    person.display() # <3>

    person1 = Person.from_birth_year('John', 1985) # <6>
    person1.display() # <7>

if __name__ == "__main__":
    main()
```

<1> 的部分，這段註解說明他是 simple factory method，這其實是 design patterns 的一種，

但這邊先簡單說明，simple factory method 指的是可以定義一個函數，根據輸入參數的不同，而

回傳不同的內容。

( 聽起來有點繞口 :sweat_smile: )

<2> 的部分，建立一個 person 實例。

<3> 的部分，是我們一般比較常用的方法。( 傳入 name 和 age )

<4> 的部分，使用了 **classmethod**，這邊要注意的是，在 `from_birth_year(cls, name, birth_year)` 中，

有幾個點要注意，首先，cls 這個參數 ( 雖然可以寫其他的名稱，但通常都寫 cls ) 指的是 class Person 本身，

看 <5> 的部分，會發現他印出 `cls: <class '__main__.Person'>`，也就是說，我們將 name 以及 birth_year

這兩個參數去 call Person class ( 可以想成是 `Person(name, date.today().year - birth_year)`)。

有了上面這個觀念，當你看 <6> 的部分時，他會 `return cls(name, date.today().year - birth_year)`，

也就是再呼叫一次 Person class，這時候的 `self._name` 為 John，而 `self._age` 為 33 ( 2018-1985 )，

simple factory method 的部分為一個是民國的年份，一個是西元的年份。

<7> 的部分，則是使用 `display()` 這個方法將結果顯示出來。

可以將 classmethod 想成是自己再去 call 自己的 class 本身，而他會使用到 class 裡面的屬性或 properties。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡 :laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
