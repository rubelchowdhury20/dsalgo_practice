################
# Leetcode 101 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            left_node = root.left
            right_node = root.right
            inverted_right_node = self.invertTree(right_node)
            return self.isSame(left_node, inverted_right_node)

    def isSame(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            queue = []
            queue.append([p, q])
            while(len(queue)>0):
                current_nodes = queue.pop()
                if current_nodes[0].val == current_nodes[1].val:
                    if current_nodes[0].left is None and current_nodes[1].left is None:
                        pass
                    elif current_nodes[0].left is None or current_nodes[1].left is None:
                        return False
                    else:
                        queue.append([current_nodes[0].left, current_nodes[1].left])
                    if current_nodes[0].right is None and current_nodes[1].right is None:
                        pass
                    elif current_nodes[0].right is None or current_nodes[1].right is None:
                        return False
                    else:
                        queue.append([current_nodes[0].right, current_nodes[1].right])
                else:
                    return False
        return True

                


    def invertTree(self, node):
        if node is not None:
            left_node = node.left
            right_node = node.right
            left_node_inverted = None
            right_node_inverted = None
            if left_node is not None:
                left_node_inverted = self.invertTree(left_node)
            if right_node is not None:
                right_node_inverted = self.invertTree(right_node)
            node.left = right_node_inverted
            node.right = left_node_inverted
        return node
