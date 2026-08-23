# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(head):
            if not head:
                return head
            prev, curr = None, None
            nxt = head
            while nxt:
                prev = curr
                curr = nxt
                nxt = curr.next
                curr.next = prev
            return curr

        def calculate_index(head):
            # Traverses the LL and returns the index to reverse LL from.
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            if length % 2 == 0:
                return length // 2
            return (length // 2) + 1

        mid_index = calculate_index(head)
        prev = None
        curr = head
        tail = None
        index = -1
        while curr:
            index += 1
            if index == mid_index:
                prev.next = None
                tail = reverse_list(curr)
                break
            prev = curr
            curr = curr.next
            

        curr_a = head
        curr_b = tail
        while curr_a:
            if not curr_b:
                curr_a = curr_a.next

            else:
                next_a = curr_a.next
                next_b = curr_b.next
                curr_a.next = curr_b
                curr_b.next = next_a
                curr_a = next_a
                curr_b = next_b
        return