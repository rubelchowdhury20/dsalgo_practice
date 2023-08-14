###############
# Leetcode 94 #
###############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if root is not None:
            left_tree = self.inorderTraversal(root.left)
            if len(left_tree) > 0:
                tree.extend(left_tree)
            tree.append(root.val)
            right_tree = self.inorderTraversal(root.right)
            if len(right_tree) > 0:
                tree.extend(right_tree)
        return tree
