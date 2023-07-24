##############
# Leetcode 3 #
##############

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        else:
            n = len(s)
            length_list = [1]
            left = 0
            right = 1
            while(right < n):
                if s[right] not in s[left:right]:
                    right += 1
                    if right == n:
                        length_list.append(right-left)
                else:
                    length_list.append(right-left)
                    while(s[left] != s[right] and left < n):
                        left += 1
                    left += 1
                    right += 1
            return max(length_list)
            