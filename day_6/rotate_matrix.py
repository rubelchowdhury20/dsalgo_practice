###############
# Leetcode 48 #
###############

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        k = n-1
        for i in range(n//2):
            for j in range(i, k-i):
                dummy = matrix[i][k-j]
                print(i, k-j)
                matrix[i][k-j] = matrix[j][i]
                print(i, k-j, j, i)
                matrix[j][i] = matrix[k-i][j]
                print(j, i, k-i, j)
                
                matrix[k-i][j] = matrix[k-j][k-i]
                print(k-i, j, k-j, k-i)
                matrix[k-j][k-i] = dummy
                print(k-j, k-i)
                # matrix[k-j][k-i] = matrix[i][k-j]
                print(matrix)
            


            