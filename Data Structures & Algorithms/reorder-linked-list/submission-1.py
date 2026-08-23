# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        if head.next == None:
            return None
        # Phase 1 - find midpoint
        slow, fast = head, head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Phase 2 - reverse second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # Phase 3 - merge lists
        left = head
        right = prev
        while left and right:
            ltmp = left.next
            rtmp = right.next
            left.next = right
            right.next = ltmp
            left = ltmp
            right = rtmp
        return None

