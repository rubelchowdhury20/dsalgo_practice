###############
# Leetcode 21 #
###############

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node
        while(True):
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            if list1.val > list2.val:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            else:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            tail = tail.next
        return dummy_node.next
