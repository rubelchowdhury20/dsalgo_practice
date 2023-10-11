################
# Leetcode 700 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if root is not None:
#             if root.val == val:
#                 return root
#             if val < root.val:
#                 return self.searchBST(root.left, val)
#             else:
#                 return self.searchBST(root.right, val)
#         else:
#             return None

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node is not None:
            if current_node.val == val:
                return current_node
            elif current_node.val > val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None




