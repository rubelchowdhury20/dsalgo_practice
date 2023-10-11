################
# Leetcode 543 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_height = 0
        self.traverseTree(root, 0, 0)
        return self.max_height

    def traverseTree(self, node, pos_x, pos_y):
        if node is not None:
            left_height = self.traverseTree(node.left, pos_x-1, pos_y+1)
            right_height = self.traverseTree(node.right, pos_x+1, pos_y+1)
            if left_height + right_height > self.max_height:
                self.max_height = left_height + right_height
            if left_height > right_height:
                return left_height+1
            else:
                return right_height+1
        return 0