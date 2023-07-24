###############
# Leetcode 56 #
###############

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.sort_interval(intervals, level=0)

    def sort_interval(self, intervals, level):
        if len(intervals) == 1:
            return intervals
        m = 0
        for i in range(len(intervals)-1):
            if intervals[i][0] <= intervals[-1][0]:
                intervals[m], intervals[i] = intervals[i], intervals[m]
                m += 1
        intervals[-1], intervals[m] = intervals[m], intervals[-1]
        if m > 0 and m < len(intervals)-1:
            left_interval = self.sort_interval(intervals[:m], level=level+1)
            right_interval = self.sort_interval(intervals[m+1:], level=level+1)
            array = left_interval
            array.append(intervals[m])
            array.extend(right_interval)

            if level==0:
                # del_list = []
                # for i in range(1, len(array)):
                #     if array[i-1][1] >= array[i][0]:
                #         array[i] = [array[i-1][0], max(array[i-1][1], array[i][1])]
                #         del_list.append(array[i-1])
                # for i in del_list:
                #     array.remove(i)
            # return array
                merged_array = [array[0]]
                for i in range(1, len(array)):
                    if merged_array[-1][1] >= array[i][0]:
                        merged_array[-1] = [merged_array[-1][0], max(merged_array[-1][1], array[i][1])]
                    else:
                        merged_array.append(array[i])
                return merged_array
            else:
                return array
            
        elif m == 0:
            right_interval = self.sort_interval(intervals[m+1:], level=level+1)
            array = [intervals[m]]
            array.extend(right_interval)
            if level==0:
                # del_list = []
                # for i in range(1, len(array)):
                #     if array[i-1][1] >= array[i][0]:
                #         array[i] = [array[i-1][0], max(array[i-1][1], array[i][1])]
                #         del_list.append(array[i-1])
                # for i in del_list:
                #     array.remove(i)
            # return array
                merged_array = [array[0]]
                for i in range(1, len(array)):
                    if merged_array[-1][1] >= array[i][0]:
                        merged_array[-1] = [merged_array[-1][0], max(merged_array[-1][1], array[i][1])]
                    else:
                        merged_array.append(array[i])
                return merged_array
            else:
                return array
            
        elif m == len(intervals)-1:
            left_interval = self.sort_interval(intervals[:m], level=level+1)
            array = left_interval
            left_interval.append(intervals[m])
            if level==0:
                # del_list = []
                # for i in range(1, len(array)):
                #     if array[i-1][1] >= array[i][0]:
                #         array[i] = [array[i-1][0], max(array[i-1][1], array[i][1])]
                #         del_list.append(array[i-1])
                # for i in del_list:
                #     array.remove(i)
            # return array
                merged_array = [array[0]]
                for i in range(1, len(array)):
                    if merged_array[-1][1] >= array[i][0]:
                        merged_array[-1] = [merged_array[-1][0], max(merged_array[-1][1], array[i][1])]
                    else:
                        merged_array.append(array[i])
                return merged_array
            else:
                return array
            

