# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            a = curr.next        # first node
            b = curr.next.next   # second node

            # swap the nodes
            a.next = b.next
            b.next = a
            curr.next = b
            # updata iterator
            curr = a
        return dummy.next


