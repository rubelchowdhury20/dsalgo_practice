################
# Leetcode 226 #
################

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            left_node = root.left
            right_node = root.right
            inverted_left_node = None
            inverted_right_node = None
            if left_node is not None:
                inverted_left_node = self.invertTree(left_node)
            if right_node is not None:
                inverted_right_node = self.invertTree(right_node)
            root.left = inverted_right_node
            root.right = inverted_left_node
            return root