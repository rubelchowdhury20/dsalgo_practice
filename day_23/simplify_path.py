###############
# Leetcode 71 #
###############

class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        path_bank = []
        slash_flag = False
        word_flag = False
        count = 0
        for i in path:
            if i == "/":
                slash_flag = True
                if word_flag:
                    path_bank.append(word)
                word_flag = False
            else:
                if slash_flag:
                    word = i
                    slash_flag = False
                    word_flag = True
                else:
                    word = word + i
                if count == n-1:
                    path_bank.append(word)
            count += 1
        clean_path_bank = []
        for i in path_bank:
            if i == "..":
                if len(clean_path_bank) > 0:
                    clean_path_bank.pop()
            elif i == ".":
                pass
            else:
                clean_path_bank.append(i)
        print(path_bank)
        print(clean_path_bank)
        return "/" + "/".join(clean_path_bank)


