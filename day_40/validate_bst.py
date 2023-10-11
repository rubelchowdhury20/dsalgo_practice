###############
# Leetcode 98 #
###############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         flag, _, _ = self.traverseTree(root)
#         return flag


#     def traverseTree(self, node):
#         if node is not None:
#             left_status = True
#             right_status = True
#             min_left = math.inf
#             max_left = -math.inf
#             min_right = math.inf
#             max_right = -math.inf
#             if node.left is not None:
#                 left_status, min_left, max_left = self.traverseTree(node.left)
#                 if max_left:
#                     if node.left.val < node.val and max_left < node.val:
#                         left_status = left_status and True
#                     else:
#                         left_status = False
#                 else:
#                     if node.left.val < node.val:
#                         left_status = left_status and True
#                     else:
#                         left_status = False
            
#             if node.right is not None:
#                 right_status, min_right, max_right = self.traverseTree(node.right)
#                 if min_right:
#                     if node.right.val > node.val and min_right > node.val:
#                         right_status = right_status and True
#                     else:
#                         right_status = False
#                 else:
#                     if node.right.val > node.val:
#                         right_status = right_status and True
#                     else:
#                         right_status = False

#             if min_left is None:
#                 min_left = math.inf
#             if max_left is None:
#                 max_left = -math.inf
#             if min_right is None:
#                 min_right = math.inf
#             if max_right is None:
#                 max_right = -math.inf

            
#             new_min = min(node.val, min_left, min_right)
#             new_max = max(node.val, max_left, max_right)
#             return left_status and right_status, new_min, new_max
#         else:
#             return True, None, None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_values = self.traverseTree(root)
        # flag = True
        prev = node_values[0]
        for i in node_values[1:]:
            if i <= prev:
                return False
            else:
                prev = i
        return True

    def traverseTree(self, node):
        node_values = []
        if node is not None:
            left_nodes = self.traverseTree(node.left)
            right_nodes = self.traverseTree(node.right)
            node_values.extend(left_nodes)
            node_values.append(node.val)
            node_values.extend(right_nodes)
        return node_values





    