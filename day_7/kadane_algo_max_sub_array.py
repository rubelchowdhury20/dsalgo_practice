###############
# Leetcode 53 #
###############

import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            m = len(nums)//2
            left_sum = self.maxSubArray(nums[:m])
            right_sum = self.maxSubArray(nums[m:])
            mid_sum = self.maxCrossSubArray(nums, m)
            if left_sum >= right_sum and left_sum >= mid_sum:
                return left_sum
            elif right_sum >= left_sum and right_sum >= mid_sum:
                return right_sum
            else:
                return mid_sum



    def maxCrossSubArray(self, nums: List[int], m) -> int:
        left_sum = -math.inf
        sum = 0
        for i in range(m-1, -1, -1):
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
        right_sum = -math.inf
        sum = 0
        for i in range(m, len(nums)):
            sum = sum + nums[i]
            if sum > right_sum:
                right_sum = sum
        return left_sum + right_sum
