"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Create a hashmap to map original Nodes to copied Nodes
        node_mapping = dict()
        # Create deep copy head
        head_copy = Node(head.val)
        node_mapping[head] = head_copy
        # Create rest of the linked list without any random node pointers
        prev_new_node = head_copy
        curr = head.next
        while curr:
            new_node = Node(curr.val)
            prev_new_node.next = new_node
            node_mapping[curr] = new_node
            prev_new_node = new_node
            curr = curr.next
        # Create the random node pointers in the deep copy
        curr = head
        new_curr = head_copy
        while curr:
            curr_random = curr.random
            if curr_random:
                new_curr_random = node_mapping[curr_random]
                new_curr.random = new_curr_random
            curr = curr.next
            new_curr = new_curr.next
        return head_copy

