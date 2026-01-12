'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # function to convert LinkedList into Array
        def toArr(l : ListNode) -> list[int]:
            _l : ListNode = l
            arr : list[int] = []
            while(_l.next != None):
                arr.append(_l.val)
                _l = _l.next
            arr.append(_l.val)
            return arr
        # function to convert Array into LinkedList
        def toLinkedList(arr : list[int]) -> ListNode:
            l : ListNode = ListNode(arr[0])
            _l : ListNode = l
            for x in arr[1:]:
                _l.next = ListNode(x)
                _l = _l.next
            return l
        # convert both LinkedLists to Array
        _l1 : list[int] = toArr(l1)
        _l2 : list[int] = toArr(l2)
        # create new array for sum
        arr : list[int] = []
        carry : int = 0
        c : int = 0
        # loop until the 2 lists have been added together
        while (len(arr) < max(len(_l1), len(_l2))):
            l_arr : int = len(arr)
            # add both if there are still numbers left in each
            if (len(_l1) > l_arr and len(_l2) > l_arr):
                c = _l1[l_arr] + _l2[l_arr] + carry
            # add only one if one array has numbers left
            elif (len(_l1) > l_arr):
                c = _l1[l_arr] + carry
            else:
                c = _l2[l_arr] + carry
            # set carry to 1 if c > 9, and modulo
            if (c > 9):
                carry = 1
                c %= 10
            else:
                carry = 0
            # add to array
            arr.append(c)
        # add carry in the end
        if carry == 1:
            arr.append(1)
        return toLinkedList(arr)