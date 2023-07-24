################
# Leetcode 128 #
################

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        else:
            nums = set(nums)
            length_list = []
            for num in nums:
                if num-1 not in nums:
                    length = 1
                    i = 1
                    while(num+i in nums):
                        length += 1
                        i += 1
                    length_list.append(length)
            return max(length_list)



    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) > 0:
    #         max_ = nums[0]
    #         min_ = nums[0]
    #         n = len(nums)
    #         for i in nums:
    #             if i > max_:
    #                 max_ = i
    #             if i < min_:
    #                 min_ = i
    #         hash_ = [0] * (max_ - min_ + 1)
    #         for i in nums:
    #             hash_[i-min_] = 1
    #         seq_list = []
    #         longest_seq = 0
    #         for i in hash_:
    #             if i == 1:
    #                 longest_seq += 1
    #             else:
    #                 seq_list.append(longest_seq)
    #                 longest_seq = 0
    #         seq_list.append(longest_seq)
    #         if len(seq_list) > 0:
    #             longest_seq = max(seq_list)
    #         else:
    #             longest_seq = 0
    #         return longest_seq
    #     else:
    #         return 0