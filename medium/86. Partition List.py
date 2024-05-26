# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.val < x:
            curr = curr.next
        last_node = curr
        while curr and curr.next:
            if curr.next.val < x:
                temp1 = curr.next
                curr.next = curr.next.next
                temp2 = last_node.next
                last_node.next = temp1
                temp1.next = temp2
                last_node = last_node.next
            else:
                curr = curr.next
        return dummy.next
