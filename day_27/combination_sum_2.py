###############
# Leetcode 40 #
###############


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        dummy_candidates = candidates.copy()
        for i in candidates:
            if i in dummy_candidates:
                dummy_candidates.remove(i)
                if target >= i:
                    if target == i:
                        # if [i] not in combs:
                        combs.append([i])
                    else:
                        current_combinations = self.combinationSum2(dummy_candidates, target-i)
                        for j in current_combinations:
                            l = self.insert(j, i)
                            # if l not in combs:
                            combs.append(l)
                while(i in dummy_candidates):
                    dummy_candidates.remove(i)
        return combs

    def insert(self, list, n):
        index = len(list)
        # Searching for the position
        for i in range(len(list)):
            if list[i] > n:
                index = i
                break
    
        # Inserting n in the list
        if index == len(list):
            list = list[:index] + [n]
        else:
            list = list[:index] + [n] + list[index:]
        return list