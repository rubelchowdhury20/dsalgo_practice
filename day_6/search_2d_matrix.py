###############
# Leetcode 74 #
###############

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) > 0:
            rl = 0
            rr = len(matrix)-1
            cl = 0
            cr = len(matrix[0])-1
            rm = (rl + rr)//2
            cm = (cl + cr)//2
            if (rr > 0 or cr > 0):
                print(matrix)
                print(rl, rr, cl , cr, rm , cm)
                if target < matrix[rm][cl]:
                    return self.searchMatrix(matrix[:rm], target)
                elif target > matrix[rm][cr]:
                    return self.searchMatrix(matrix[rm+1:], target)
                else:
                    print("hello")
                    print(matrix)
                    print(rm, cm)
                    print(matrix[rm][cm])
                    print(target)
                    if matrix[rm][cm] == target:
                        print("it's true")
                        return True
                    elif matrix[rm][cm] > target:
                        l = cl
                        r = cm-1
                        m = (l+r)//2
                        while(l <= r):
                            if matrix[rm][m] == target:
                                return True
                            elif matrix[rm][m] > target:
                                r = m - 1
                                m = (l+r)//2
                            else:
                                l = m + 1
                                m = (l+r)//2
                    else:
                        l = cm+1
                        r = cr
                        m = (l+r)//2
                        while(l <= r):
                            if matrix[rm][m] == target:
                                return True
                            elif matrix[rm][m] > target:
                                r = m - 1
                                m = (l+r)//2
                            else:
                                l = m + 1
                                m = (l+r)//2
            else:
                if matrix[rm][cm] == target:
                    return True
        return False
