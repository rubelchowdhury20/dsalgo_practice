################
# Leetcode 141 #
################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        if current_node:
            while(current_node.next):
                if current_node.next.val == "a":
                    return True
                else:
                    current_node.val = "a"
                    current_node = current_node.next
        return False