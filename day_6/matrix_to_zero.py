###############
# Leetcode 73 #
###############

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'a'
                    for l in range(len(matrix)):
                        if matrix[l][j] != 0:
                            matrix[l][j] = 'a'
                    continue
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0