################
# Leetcode 430 #
################

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            current_node = head
            self.recursion(head)
        return head

    def recursion(self, head):
        current_node = head
        while(current_node.next):
            if current_node.child:
                existing_next = current_node.next
                current_node.next = current_node.child
                current_node.child = None
                current_node.next.prev = current_node
                last_node = self.recursion(current_node.next)
                last_node.next = existing_next
                existing_next.prev = last_node
            current_node = current_node.next
        
        if current_node.child:
            current_node.next = current_node.child
            current_node.child = None
            current_node.next.prev = current_node
            last_node = self.recursion(current_node.next)
            return last_node
        else:
            return current_node