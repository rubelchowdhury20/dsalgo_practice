###############
# Leetcode 62 #
###############

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.combination(m+n-2, n-1))
    def combination(self, n, r):
        return self.factorial(n)/(self.factorial(r)*self.factorial(n-r))
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)