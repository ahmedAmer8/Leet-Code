# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get list size
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        index = size - n
        prev = curr = head
        while curr and index:
            index -= 1
            prev = curr
            curr = curr.next
        if curr is not prev:
            prev.next = curr.next
        else:
            head = head.next
        return head
        
