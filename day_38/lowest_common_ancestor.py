################
# Leetcode 236 #
################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TIME LIMIT EXCEEDED SOLUTION

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         current_node = root
#         flag = True
#         while(current_node and flag):
#             if current_node.left and  self.isAncestor(current_node.left, p) and self.isAncestor(current_node.left, q):
#                 current_node = current_node.left
#             elif current_node.right and self.isAncestor(current_node.right, p) and self.isAncestor(current_node.right, q):
#                 current_node = current_node.right
#             else:
#                 flag = False
#         return current_node
            

#     def isAncestor(self, node, child):
#         if node is None:
#             return False
#         elif node == child:
#             return True
#         else:
#             left_child = self.isAncestor(node.left, child)
#             right_child = self.isAncestor(node.right, child)
#             return left_child or right_child

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# accepted solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_nodes = []
        self.isAncestorP(root, p)
        for i in self.p_nodes:
            if self.isAncestor(i, q):
                return i
        return root

    def isAncestor(self, node, child):
        if node is None:
            return False
        elif node == child:
            return True
        else:
            left_child = self.isAncestor(node.left, child)
            right_child = self.isAncestor(node.right, child)
            return left_child or right_child 

    def isAncestorP(self, node, child):
        if node is None:
            return False
        elif node == child:
            self.p_nodes.append(node)
            return True
        else:
            left_child = self.isAncestorP(node.left, child)
            right_child = self.isAncestorP(node.right, child)
            
            if left_child:
                self.p_nodes.append(node.left)
            elif right_child:
                self.p_nodes.append(node.right)
            return left_child or right_child
        
    
        
    