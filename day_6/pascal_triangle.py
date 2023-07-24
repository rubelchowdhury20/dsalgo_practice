##################
#  Leetcode 118  #
##################

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]
        if numRows == 1:
            return [triangle[0]]
        elif numRows == 2:
            return triangle
        else:
            for i in range(2, numRows):
                dummy = [1]
                for j in range(len(triangle[-1])-1):
                    dummy.append(triangle[-1][j] + triangle[-1][j+1])
                dummy.append(1)
                triangle.append(dummy)
            return triangle

        