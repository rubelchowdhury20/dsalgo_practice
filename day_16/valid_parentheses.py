###############
# Leetcode 20 #
###############

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")",
                    "{": "}",
                    "[": "]"}
        open_braces = ["(", "{", "["]
        dummy_stack = []
        for last in s:
            if len(dummy_stack)>0:
                print(dummy_stack[-1])
                if dummy_stack[-1] in open_braces and  mapping[dummy_stack[-1]] == last:
                    dummy_stack.pop()
                else:
                    dummy_stack.append(last)
            else:
                dummy_stack.append(last)
        if len(dummy_stack) == 0:
            return True
        else:
            return False

