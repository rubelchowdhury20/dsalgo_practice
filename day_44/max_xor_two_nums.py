################
# Leetcode 420 #
################

import math
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.binary_map = {}
        self.root = self.buildTree(nums)
        xor_max = -math.inf
        for i in nums:
            binary = self.binary_map[i]
            current_node = self.root
            for j in binary[::-1]:
                if j == 1:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node = current_node.right
                else:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node = current_node.left
            # print(i, current_node.val)
            xor_val = i ^ current_node.val
            if xor_val > xor_max:
                xor_max = xor_val
        return xor_max


            
        

    def buildTree(self, nums):
        max_ = nums[0]
        for i in nums:
            if i > max_:
                max_ = i
        binary_max_ = self.getBinary(max_)
        binary_max_n = len(binary_max_)
        for i in nums:
            binary = self.getBinary(i)
            binary.extend([0]*(binary_max_n - len(binary)))
            self.binary_map[i] = binary
        
        root = Node()
        for i in nums:
            binary = self.binary_map[i].copy()
            current_node = root
            while(len(binary)>0):
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
            current_node.val = i
        return root

            


    def getBinary(self, num):
        binary = []
        while(num > 1):
            binary.append(num%2)
            num = num//2
        binary.append(num)
        return binary
