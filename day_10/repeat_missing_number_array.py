################
# InterviewBit #
################

class Solution:
    # @param A : tuple of integers
    # @return a list of integers

                
    
    def repeatedNumber(self, A):
        n_square, square, n_sum, add, n = 0, 0, 0, 0, len(A)
        for i in range(n):
            n_square = n_square + (i+1)**2
            square = square + A[i]**2
            n_sum = n_sum + (i+1)
            add = add + A[i]
        
        diff = n_sum - add
        addition = (n_square - square)/(n_sum - add)
        B = (diff+addition)/2
        A = (addition - diff)/2
        
        return round(A), round(B)
        
