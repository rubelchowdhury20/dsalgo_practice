################
# Leetcode 234 #
################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        current_node = head
        while current_node:
            n += 1
            current_node = current_node.next
        current_node = head

        if n == 1:
            return True
        else:
        
            mid_n = n//2
            count = 0
            stack = []
            while(count < mid_n and current_node):
                stack.append(current_node.val)
                current_node = current_node.next
                count += 1
            
            if n%2 == 1:
                count += 1

            while(count <= n and current_node):
                if stack[-1] == current_node.val:
                    stack.pop()
                current_node = current_node.next
                count += 1

            if len(stack) == 0:
                return True
