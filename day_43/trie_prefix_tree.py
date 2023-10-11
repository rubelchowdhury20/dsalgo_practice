################
# Leetcode 208 #
################

class Node:
    def __init__(self):
        self.alphabets = {}
        self.word_stop = False

class Trie:

    def __init__(self):
        self.root = Node() 
        

    def insert(self, word: str) -> None:
        current_node = self.root
        for i in word:
            if i not in current_node.alphabets:
                current_node.alphabets[i] = Node()
                current_node = current_node.alphabets[i]
            else:
                current_node = current_node.alphabets[i]
        current_node.word_stop = True

        

    def search(self, word: str) -> bool:
        current_node = self.root
        for i in word:
            if i not in current_node.alphabets:
                return False
            else:
                current_node = current_node.alphabets[i]
        if current_node.word_stop:
            return True
        else:
            return False
        
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for i in prefix:
            if i not in current_node.alphabets:
                return False
            else:
                current_node = current_node.alphabets[i]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)