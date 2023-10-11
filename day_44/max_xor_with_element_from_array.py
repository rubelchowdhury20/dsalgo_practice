#################
# Leetcode 1707 #
#################

import math
class Node:
    def __init__(self, val=None):
        self.val = val
        self.min = None
        self.max = None
        self.left = None
        self.right = None


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.binary_max_n = len(self.getBinary(max(max(nums), max([i[0] for i in queries]))))
        
        self.binary_map = {}
        self.root = self.buildTree(nums)
        # xor_max = -math.inf
        answer = []
        for i in queries:
            m = i[1]
            # binary = self.binary_map[i[0]]
            binary = self.getBinary(i[0])
            binary.extend([0]*(self.binary_max_n - len(binary)))
            current_node = self.root
            if m >= current_node.min:
                for j in binary[::-1]:
                    if j == 1:
                        if current_node.left is not None:
                            current_node = current_node.left
                        else:
                            current_node = current_node.right
                    else:
                        if current_node.right is not None and m >= current_node.right.min:
                            current_node = current_node.right
                        else:
                            current_node = current_node.left
                # print(i, current_node.val)
                xor_val = i[0] ^ current_node.val
                # if xor_val > xor_max:
                #     xor_max = xor_val
                answer.append(xor_val)
            else:
                answer.append(-1)
        return answer


            
        

    def buildTree(self, nums):
        for i in nums:
            binary = self.getBinary(i)
            binary.extend([0]*(self.binary_max_n - len(binary)))
            self.binary_map[i] = binary
        
        root = Node()
        for i in nums:
            binary = self.binary_map[i].copy()
            current_node = root
            while(len(binary)>0):
                if current_node.min is None:
                    current_node.min = i
                else:
                    if i < current_node.min:
                        current_node.min = i
                if current_node.max is None:
                    current_node.max = i
                else:
                    if i > current_node.max:
                        current_node.max = i
                current = binary.pop()
                if current == 0:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node()
                        current_node = current_node.left
                else:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node()
                        current_node = current_node.right
            current_node.min = i
            current_node.max = i
            current_node.val = i
        return root

            


    def getBinary(self, num):
        binary = []
        while(num > 1):
            binary.append(num%2)
            num = num//2
        binary.append(num)
        return binary
