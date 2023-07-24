###############
# Leetcode 31 #
###############

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while(nums[i] <= nums[i-1] and i > 0):
            i = i-1
        i = i - 1
        if i >= 0:
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    flag = nums[i]
                    nums[i] = nums[j]
                    nums[j] = flag
                    break
        m = (i + 1 + len(nums))//2
        k = 0
        for j in range(i+1, m):
            nums[j], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[j]
            
            k = k+1
        return nums




# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)-2, -1, -1):
#             print(nums, nums[i])
            
#             j = len(nums)-1
#             changed_flag = False
#             while(j > i):
#                 if nums[j] > nums[i]:
#                     flag = nums[j]
#                     nums[j] = nums[i]
#                     nums[i] = flag
#                     changed_flag = True
#                     break
#                 else:
#                     j = j-1
#             if changed_flag:
#                 nums = self.merge_sort(nums, i+1, len(nums))
#                 return nums
#         return self.merge_sort(nums, 0,  len(nums))
                

#     def merge_sort(self, array, p, r):
#         if p<r:
#             q = math.floor((p+r)/2)
#             if r-p>=2:
#                 array = self.merge_sort(array, p, q)
#                 array = self.merge_sort(array, q, r)
#             array = self.combine(array, p, q, r)
#         return array


#     def combine(self, array, p, q, r):
#         left = array[p:q]
#         right = array[q:r]
#         left.append(math.inf)
#         right.append(math.inf)
#         combined_array = []
#         li = 0
#         ri = 0
#         while(li!=len(left) and ri!=len(right)):
#             if left[li] < right[ri]:
#                 combined_array.append(left[li])
#                 li += 1
#             else:
#                 combined_array.append(right[ri])
#                 ri += 1
#         if li!=len(left):
#             combined_array.extend(left[li:])
#         else:
#             combined_array.extend(right[ri:])
#         array[p:r] = combined_array[:-2]
#         return array


            