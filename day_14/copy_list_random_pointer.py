################
# Leetcode 138 #
################

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
        if head:
            new_node_head = Node(head.val)
            current_node = head
            new_current_node = new_node_head
            mapping_dict = {}
            mapping_dict[head] = new_node_head
            while(current_node.next):
                new_current_node.next = Node(current_node.next.val)
                mapping_dict[current_node.next] = new_current_node.next
                current_node = current_node.next
                new_current_node = new_current_node.next
            current_node = head
            new_current_node = new_node_head
            while(current_node):
                if current_node.random:
                    new_current_node.random = mapping_dict[current_node.random]
                current_node = current_node.next
                new_current_node = new_current_node.next

            return new_node_head
        else:
            return None