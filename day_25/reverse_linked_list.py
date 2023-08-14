################
# Leetcode 206 #
################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            head, tail = self.recursion(head)
            return head
        else:
            return head

    def recursion(self, head):
        if head.next is None:
            return head, head
        else:
            short_head, short_tail = self.recursion(head.next)
            short_tail.next = head
            head.next = None
            return short_head, short_tail.next