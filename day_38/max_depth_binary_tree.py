################
# Leetcode 104 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left_depth, right_depth = 0, 0
        if root is not None:
            if root.left is not None:
                left_depth = self.maxDepth(root.left)
            if root.right is not None:
                right_depth = self.maxDepth(root.right)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
        return left_depth
