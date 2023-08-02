###############
# Leetcode 25 #
###############

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current_node = head
        while(current_node):
            length += 1
            current_node = current_node.next

        reverse_attempts = length // k
        current_node = head
        for i in range(reverse_attempts):
            # self.print_values(head)
            group_head = current_node
            count = 0
            while(current_node and count < k):
                current_node = current_node.next
                count += 1
            prev_node_pos = current_node
            current_node = group_head
            count = 0
            while(current_node and count < k):
                if (count > 0):
                    prev_node.next = prev_node_pos
                    prev_node_pos = prev_node
                prev_node = current_node
                current_node = current_node.next
                count += 1
            prev_node.next = prev_node_pos
            if i == 0:
                head = prev_node
            else:
                prev_group_head.next = prev_node
            prev_group_head = group_head
        return head

    def print_values(self, head):
        val_list = []
        current_node = head
        while(current_node):
            val_list.append(str(current_node.val))
            current_node = current_node.next
        print("->".join(val_list))

