################
# Leetcode 121 #
################

import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_diff = []
        for i in range(len(prices)-1):
            price_diff.append(prices[i+1] - prices[i])
        val = self.maxSubArray(price_diff)
        if val >= 0:
            return val
        else:
            return 0
        
    def maxSubArray(self, nums:List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            m = len(nums)//2
            left_sum = self.maxSubArray(nums[:m])
            right_sum = self.maxSubArray(nums[m:])
            mix_sum = self.maxMixSubArray(nums, m)
        if left_sum >= right_sum and left_sum >= mix_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= mix_sum:
            return right_sum
        else:
            return mix_sum

    def maxMixSubArray(self, nums:List[int], m) -> int:
        left_sum = -math.inf
        sum = 0
        for i in range(m-1, -1, -1):
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
        right_sum = -math.inf
        sum = 0
        for i in range(m,len(nums)):
            sum = sum + nums[i]
            if sum > right_sum:
                right_sum = sum
        return left_sum + right_sum
