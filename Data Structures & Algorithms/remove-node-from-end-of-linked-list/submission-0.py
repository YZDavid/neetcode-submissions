# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        idx_remove = length - n
        if idx_remove == 0:
            return head.next
        curr = head
        prev = None
        for i in range(idx_remove):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head