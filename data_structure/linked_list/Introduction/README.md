# linked list - data structure

## 什麼是 linked list

[Youtube Tutorial - What is linked list](https://youtu.be/A2VeeXpgs2w)

這邊我們直接來看一張圖，如下

![alt tag](https://imgur.com/Y1GXqGT.png)

有兩件事情需要知道，

第一，一個 linked list 包含節點 ( nodes )，如下

![alt tag](https://i.imgur.com/imFpGqV.png)

第二，每一個節點 ( node ) 由 value 和 pointer ( 指標，指向下一個 node ) 組成

![alt tag](https://i.imgur.com/Y6Ml76V.png)


## 為什麼要使用 linked list

linked list 常常和 arrays 進行比較，array 有固定的大小，但是 linked list 可以動態分配。

以下簡單說明他們的優缺點，

* 優點

linked list 可以節省記憶體，他只需要分配記憶體給儲存 values 的部分即可；相反的，

在 arrays 中，我們必須分配整個 array size 的 values，這樣可以會浪費記憶體。

linked list 的節點可以活在記憶體的任何地方。arrays 需要一開始就分配記憶體去初始化，

而 linked list 只要 references 被更新，每一個 linked list node 都可以彈性地

被移動到不同的位址。

* 缺點

線性 ( Linear ) 的查找時間。當尋找值時候，必須重 linked list 的頭開始一個一個尋找，

假如 linked list 有 n 個元素，最多需要 n 次 ( 複雜度O(n) )。

## linked list in Python

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None # the pointer
```

舉個例子，如下圖，

![alt tag](https://imgur.com/Y1GXqGT.png)

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/data_structure/linked_list/Introduction/demo1.py)

```python
node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(7)

node1.next = node2 # 2->5
node2.next = node3 # 5->7

# the entire linked list : 2->5->7
```

## Traversing values

這邊來看要如何歷遍整個 linked list，

第一種方法，[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/data_structure/linked_list/Introduction/demo2.py)，

```python
while node1:
    print(node1.val)
    node1 = node1.next
```

第二種方法，也可以使用 recursive [demo3.py](https://github.com/twtrubiks/python-notes/blob/master/data_structure/linked_list/Introduction/demo3.py)，

```python
def traversing_recursive(lists):
    if not lists:
        return
    print(lists.val)
    traversing_recursive(lists.next)
    print(lists.val)


traversing_recursive(node1)
```

Linked Lists 基礎的介紹就到這邊，未來如果有碰到 leetcode 的相關練習，會補充到這邊 :smile:

## Reference

* [Data structures in Python, Series 1: Linked Lists](https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d)

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡 :laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
