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
        size = 1
        while curr.next:
            size += 1
            curr = curr.next
        # circular linked list
        curr.next = head
        # there is no need to rotate the list a full cycle as it will be the same
        # so we limit the values of rotation to be between 0 and size - 1
        # by make k = k % size 
        k = k % size
        # the last node after rotation should point at None
        # this node can be finde just before the size - k position
        temp = head
        for i in range (size - k - 1):
            temp = temp.next
        result = temp.next
        temp.next = None
        return result
