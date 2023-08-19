################
# Leetcode 987 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.max_x = 0
        self.min_x = 0
        self.pow = 397
        # self.pow_i = 2003
        self.modulo = 100000000069
        self.node_map = {}
        self.traverseTree(root, 0, 0)
        final_list = []
        for i in range(self.min_x, self.max_x+1):
            dummy_list = []
            for j in sorted(self.node_map[i].keys()):
                dummy_list.extend(sorted(self.node_map[i][j]))
            final_list.append(dummy_list)
        return final_list


        
        

    def traverseTree(self, node, pos_x, pos_y):
        if node is not None:
            if pos_x > self.max_x:
                self.max_x = pos_x
            if pos_x < self.min_x:
                self.min_x = pos_x
            if pos_x in self.node_map:
                if pos_y in self.node_map[pos_x]:
                    self.node_map[pos_x][pos_y].append(node.val)
                    # if self.node_map[pos_x][pos_y][0] < node.val:
                    #     self.node_map[pos_x][pos_y].append(node.val)
                    # else:
                    #     flag = self.node_map[pos_x][pos_y][0]
                    #     self.node_map[pos_x][pos_y][0] = node.val
                    #     self.node_map[pos_x][pos_y].append(flag)
                else:
                    self.node_map[pos_x][pos_y] = [node.val]
            else:
                self.node_map[pos_x] = {}
                self.node_map[pos_x][pos_y] = [node.val]
            self.traverseTree(node.left, pos_x-1, pos_y+1)
            self.traverseTree(node.right, pos_x+1, pos_y+1)
            


