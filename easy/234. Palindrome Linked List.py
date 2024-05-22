# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # find the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the linkedlist
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
