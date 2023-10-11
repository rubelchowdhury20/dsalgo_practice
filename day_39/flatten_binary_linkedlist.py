################
# Leetcode 114 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            if root.left is not None and root.right is not None:
                straightened_left_last = self.flatten(root.left)
                straightened_right_last = self.flatten(root.right)
                right_flag = root.right
                root.right = root.left
                straightened_left_last.right = right_flag
                root.left = None
                return straightened_right_last
            elif root.left is not None:
                straightened_left_last = self.flatten(root.left)
                root.right = root.left
                root.left = None
                return straightened_left_last
            elif root.right is not None:
                straightened_right_last = self.flatten(root.right)
                return straightened_right_last
            else:
                return root