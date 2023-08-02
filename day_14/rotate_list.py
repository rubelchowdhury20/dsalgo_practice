###############
# Leetcode 61 #
###############

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current_node = head
        while(current_node):
            length += 1
            current_node = current_node.next
        if length > 0:
            cut = k % length
        else:
            cut = 0
        if length > 0 and cut > 0 and length != cut:

            current_node = head
            count = 0
            
            while(current_node.next):
                if count == length - cut - 1:
                    last_node = current_node
                if count == length - cut:
                    new_head = current_node
                count += 1
                current_node = current_node.next
            if count == length - cut - 1:
                last_node = current_node
            if count == length - cut:
                new_head = current_node

            current_node.next = head
            last_node.next = None

            return new_head
        else:
            return head