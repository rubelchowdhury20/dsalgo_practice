################
# Leetcode 496 #
################

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n1 = len(nums1)
        n2 = len(nums2)
        print(n1, n2)
        for i in nums1:
            count = 0
            while(nums2[count] != i):
                count += 1
            if count == n2-1:
                ans.append(-1)
            else:
                count += 1
                while(nums2[count] < i and count < n2-1):
                    count += 1
                if count == n2-1 and nums2[count] < i:
                    ans.append(-1)
                else:
                    ans.append(nums2[count])
        return ans

            