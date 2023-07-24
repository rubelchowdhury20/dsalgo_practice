###############
# Leetcode 75 #
###############

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        two_idx = len(nums)
        i = 0
        while i != two_idx:
            if nums[i] == 0:
                flag = nums[i]
                nums[i] = nums[zero_idx + 1]
                nums[zero_idx+1] = flag
                zero_idx += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                if nums[two_idx-1] == 2:
                    two_idx -= 1
                elif nums[two_idx-1] == 1:
                    flag = nums[two_idx-1]
                    nums[two_idx-1] = nums[i]
                    nums[i] = flag
                    two_idx -= 1
                    i += 1
                else:
                    flag = nums[two_idx-1]
                    nums[two_idx-1] = nums[i]
                    nums[i] = flag
                    two_idx -= 1