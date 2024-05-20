# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = prev = curr = head
        if not head:
            return None
        while curr.next:
            curr = curr.next
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
        if curr.val != prev.val:
                prev.next = curr
                prev = curr
        else:
            prev.next = None
        return new_head
            
