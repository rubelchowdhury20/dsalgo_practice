###############
# Leetcode 90 #
###############

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            current_item = nums[0]
            subsets_prev = self.subsetsWithDup(nums[1:])
            new_subsets = []
            new_subsets.extend(subsets_prev)
            subsets_prev_ = subsets_prev.copy()
            if [current_item] in subsets_prev_:
                subsets_prev_ = subsets_prev_[1:]
            
            # print(new_subsets)
            for i in subsets_prev_:
                flag = True
                # if len(nums) >= 2 and nums[1] == current_item and i[-1] != current_item:
                #     flag = False
                if flag:
                    l = i.copy()
                    l.append(current_item)
                    l.sort()
                    if l not in new_subsets:
                        new_subsets.append(l)
            return new_subsets
