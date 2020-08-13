# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        res = head
        carry = 0
        while l1 is not None or l2 is not None:
            
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            currsum = l1_val+l2_val+carry
            carry = int(currsum/10)
            ldigit = currsum%10
            new_node = ListNode(ldigit)
            res.next = new_node
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            res = res.next   #600+600 = 1200
            
        if carry>0:
            new_node = ListNode(carry)
            res.next = new_node
            res = res.next
            
        return head.next
