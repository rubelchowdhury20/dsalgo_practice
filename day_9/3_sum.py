###############
# Leetcode 15 #
###############
# the failed solution has time complexity of O(n^2logn) while the
# the accepted solution has the time complexity of O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, triplets = len(nums), []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start, end = i+1, n-1
            while(start<end):
                if nums[start] + nums[end] == -nums[i]:
                    triplet = [nums[i], nums[start], nums[end]]
                    # triplet.sort()
                    triplets.append(triplet)
                    start = start+1
                    while(start < end and nums[start] == nums[start-1]):
                        start = start + 1
                elif nums[start] + nums[end] < -nums[i]:
                    start = start + 1
                else:
                    end = end - 1
        return triplets




    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # nums = sorted(nums)
    #     nums.sort()
    #     triplets = []
    #     n = len(nums)
    #     for i in range(1, n-1):
    #         for j in range(0, i):
    #             anchor = -(nums[i] + nums[j])
    #             if self.binarySearch(nums[i+1:], anchor):

    #                 triplet = [nums[i], nums[j], anchor]
    #                 triplet.sort()
    #                 if triplet not in triplets:
    #                     triplets.append(triplet)
       
    #     return triplets


    # def binarySearch(self, array, anchor):
    #     if len(array) == 0:
    #             return False
    #     else:
    #         m = len(array)//2
    #         if array[m] == anchor:
    #             return True
    #         elif array[m] > anchor:
    #             return self.binarySearch(array[0:m], anchor)
    #         else:
    #             return self.binarySearch(array[m+1:], anchor)


