# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val2 = l2.val if l2 else 0
            val1 = l1.val if l1 else 0
            s = val1 + val2 + carry
            carry = s // 10
            s = s % 10
            curr.next = ListNode(s)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
