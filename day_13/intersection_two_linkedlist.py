################
# Leetcode 160 #
################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_A = []
        current_node = headA
        while(current_node):
            list_A.append(current_node)
            current_node = current_node.next

        list_B = []
        current_node = headB
        while(current_node):
            list_B.append(current_node)
            current_node = current_node.next

        a = len(list_A)
        b = len(list_B)
        n = min(a, b)
        count = 0
        flag = True
        while(count < n and flag):
            if list_A[a-count-1] == list_B[b-count-1]:
                count += 1
            else:
                flag = False

        if flag == False:
            if count == 0:
                return None
            else:
                return list_A[a-count]
        else:
            if count == n:
                return list_A[a-count]
            else:
                return None

        
    
    
    def print_values(self, head):
        val_list = []
        current_node = head
        while(current_node):
            val_list.append(str(current_node.val))
            current_node = current_node.next
        return "->".join(val_list)
