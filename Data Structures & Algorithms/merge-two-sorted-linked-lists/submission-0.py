# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = list1
        l2_curr = list2
        head = ListNode()
        curr = head

        while l1_curr or l2_curr:
            if l1_curr and not l2_curr:
                curr.next = l1_curr
                break
            elif l2_curr and not l1_curr:
                curr.next = l2_curr
                break
            elif l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                l1_curr = l1_curr.next
            else:
                curr.next = l2_curr
                l2_curr = l2_curr.next
            curr = curr.next
        
        return head.next
                
