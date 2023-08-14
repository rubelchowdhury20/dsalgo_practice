#################
# Leetcode 2261 #
#################

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        # subarray_list = []
        subarray_dict = {}
        divisible_dict = {}
        count = 0
        for i in nums:
            if i%p == 0:
                divisible_dict[i] = True
        for i in range(n):
            sub_array = nums[0:i+1]
            divisible_count = 0
            subarray_str = ""
            for j in sub_array:
                subarray_str = subarray_str + str(j) + "_"
                if j in divisible_dict:
                    divisible_count += 1
            if divisible_count <= k:
                if subarray_str not in subarray_dict:
                    subarray_dict[subarray_str] = True
                    count += 1
                    # subarray_list.append(sub_array)
            for j in range(i+1, n):
                if sub_array[0] in divisible_dict:
                    divisible_count -= 1
                dummy = str(sub_array[0])
                sub_array = sub_array[1:]
                subarray_str = subarray_str[len(dummy)+1:]
                sub_array.append(nums[j])
                if sub_array[-1] in divisible_dict:
                    divisible_count += 1
                
                subarray_str = subarray_str + str(nums[j]) + "_"
                if divisible_count <= k:
                    if subarray_str not in subarray_dict:
                        subarray_dict[subarray_str] = True
                        count += 1
                        # subarray_list.append(sub_array)
        # print(subarray_dict)
        return count