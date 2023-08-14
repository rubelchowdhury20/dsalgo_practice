################
# Leetcode 144 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []
        if root is not None:
            node_list.append(root.val)
            if root.left:
                left_list = self.preorderTraversal(root.left)
                node_list.extend(left_list)
            if root.right:
                right_list = self.preorderTraversal(root.right)
                node_list.extend(right_list)
        return node_list


