###############
# Leetcode 39 #
###############

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        for i in candidates:
            if target >= i:
                if target == i:
                    combs.append([i])
                elif target > i:
                    current_combinations = self.combinationSum(candidates, target-i)
                    for j in current_combinations:
                        j.append(i)
                        j.sort()
                        if j not in combs:
                            combs.append(j)
        return combs