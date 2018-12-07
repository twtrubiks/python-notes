# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # the pointer


node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(7)

node1.next = node2  # 2->5
node2.next = node3  # 5->7

# the entire linked list : 2->5->7
