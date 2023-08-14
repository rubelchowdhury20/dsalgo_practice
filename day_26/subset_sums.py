class SolutionSubsets:
    def subsets(self, arr, N):
        # if N == 1:
        #     return [arr]
        if N == 0:
            return [[]]
        else:
            current_item = arr[0]
            subsets_prev = self.subsets(arr[1:], N-1)
            new_subsets = []
            new_subsets.extend(subsets_prev)
            print(subsets_prev)
            print(new_subsets)
            for i in subsets_prev:
                l = i.copy()
                l.append(current_item)
                new_subsets.append(l)
            # new_subsets.append([current_item])
            print(new_subsets)
            print(".....")
            return new_subsets
        
class SolutionSubsetsSum:
    def subsetSums(self, arr, N):
        if N == 0:
            return [0]
        else:
            current_item = arr[0]
            subset_sums_prev = self.subsetSums(arr[1:], N-1)
            subset_sums_new = []
            subset_sums_new.extend(subset_sums_prev)
            for i in subset_sums_prev:
                l = i
                l = l + current_item
                subset_sums_new.append(l)
            return subset_sums_new


test1 = [1, 2, 3, 4] 
test2 = [2, 3]
# sol = SolutionSubsets()
# print(sol.subsets(test1, len(test1)))

sol_sum = SolutionSubsetsSum()
print(sol_sum.subsetSums(test1, len(test1)))
print(sol_sum.subsetSums(test2, len(test2)))

