# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        n //= k
        new_head = prev_tail = ListNode(0)
        for i in range(n):
            prev = None
            temp_pointer = head
            for j in range(k):
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            # now prev is the head of the reversed group
            # head points to the first item of the following group
            prev_tail.next = prev
            prev_tail = temp_pointer
        # link the un-reversed part to the last tail in the reversed parts
        prev_tail.next = head
        return new_head.next


