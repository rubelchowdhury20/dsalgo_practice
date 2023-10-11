###############
# Leetcode 99 #
###############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = self.inorderTraverse(root)
        print([i.val for i in node_list])
        for idx, i in enumerate(node_list[:-1]):
            if i.val > node_list[idx+1].val:
                wrong_one = i
                break
        for idx, i in enumerate(node_list[1:]):
            if i.val < node_list[idx].val:
                wrong_two = i
                # break
        flag = wrong_one.val
        wrong_one.val = wrong_two.val
        wrong_two.val = flag

        
        
    def inorderTraverse(self, node):
        node_list = []
        if node is not None:
            left_list = self.inorderTraverse(node.left)
            right_list = self.inorderTraverse(node.right)
            node_list.extend(left_list)
            node_list.append(node)
            node_list.extend(right_list)
        return node_list
