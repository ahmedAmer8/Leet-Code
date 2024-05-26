# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if we have less than two nodes, then no rotation available
        if not head or not head.next:
            return head
        # find list size
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        # there is no need to rotate the list a full cycle as it will be the same
        # so we limit the values of rotation to be between 0 and size - 1
        # by make k = k % size 
        k = k % size
        while k:
            curr = head
            while curr and curr.next.next:
                curr = curr.next
            last_node = curr.next
            curr.next = curr.next.next
            last_node.next = head
            head = last_node
            k -= 1
        return head
