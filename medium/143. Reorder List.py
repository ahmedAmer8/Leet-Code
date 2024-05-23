# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # modify
        first = head
        last = prev
        while first and last.next:
            # print(first.val, last.val)
            temp1 = first.next
            temp2 = last.next
            first.next = last
            last.next = temp1
            # update the two pointers
            first = temp1
            last = temp2
 
