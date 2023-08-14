################
# Leetcode 131 #
################

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        else:
            string_set = []
            n = len(s)
            for i in range(n):
                mid = (i+1)//2
                
                if s[:mid] == s[i+1-mid:i+1][::-1]:
                    substrings_next = self.partition(s[i+1:])
                    for j in substrings_next:
                        s_ = [s[:i+1]]
                        s_.extend(j)
                        string_set.append(s_)
            return string_set