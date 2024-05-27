# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            duplicates_founded = False
            while curr and curr.next and curr.val == curr.next.val:
                duplicates_founded = True
                curr = curr.next
            if duplicates_founded:
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next
