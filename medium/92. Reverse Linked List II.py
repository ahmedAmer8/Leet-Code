# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        right = right - left + 1
        cur = head
        prev_tail = dummy = ListNode(0, head)
        while cur:
            left -= 1
            if left == 0:
                prev = None
                new_tail = cur
                for i in range(right):
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                prev_tail.next = prev
                new_tail.next = cur
                break
            cur = cur.next
            prev_tail = prev_tail.next
            
        return dummy.next
