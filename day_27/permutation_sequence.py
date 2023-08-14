###############
# Leetcode 60 #
###############

import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        number_list = list(range(1, n+1))
        number = ""
        count = 0
        while(count < n-1):
            prev_perm = self.factorial(n-1-count)
            current_number_index = math.ceil(k / prev_perm)-1
            k = k % prev_perm
            current_number = number_list[current_number_index]
            
            number = number + str(current_number)
            number_list.remove(current_number)
            count += 1
        number = number + str(number_list[0])
        return number
        

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)