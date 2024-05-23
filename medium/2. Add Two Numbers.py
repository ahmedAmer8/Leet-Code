# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        remainder = 0
        while l1 and l2:
            s = l1.val + l2.val + remainder
            if s > 9:
                remainder = 1
                s = s % 10
            else:
                remainder = 0
            new_node = ListNode(s)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + remainder
            if s > 9:
                remainder = 1
                s = s % 10
            else:
                remainder = 0
            new_node = ListNode(s)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next
        while l2:
            s = l2.val + remainder
            if s > 9:
                remainder = 1
                s = s % 10
            else:
                remainder = 0
            new_node = ListNode(s)
            curr.next = new_node
            curr = curr.next
            l2 = l2.next
        if remainder:
            new_node = ListNode(remainder)
            curr.next = new_node
            curr = curr.next
        return dummy.next
