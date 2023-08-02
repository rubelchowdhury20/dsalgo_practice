##############
# Leetcode 2 #
##############

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode()
        ans = first_node
        reminder = 0
        while(True):
            if l1 is None and l2 is None and reminder == 0:
                break
            elif l1 is None and l2 is None and reminder != 0:
                ans.next = ListNode(reminder)
                reminder = 0
                ans = ans.next
            elif l1 is None:
                val = (reminder + l2.val) % 10
                reminder = (reminder + l2.val) // 10
                ans.next = ListNode(val)
                ans = ans.next
                l2 = l2.next
            elif l2 is None:
                val = (reminder + l1.val) % 10
                reminder = (reminder + l1.val) // 10
                ans.next = ListNode(val)
                ans = ans.next
                l1 = l1.next
            else:
                val = (reminder + l1.val + l2.val) % 10
                reminder = (reminder + l1.val + l2.val) // 10
                ans.next = ListNode(val)
                ans = ans.next
                l1 = l1.next
                l2 = l2.next

        return first_node.next

