# 208. Implement Trie (Prefix Tree)
class Node:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word
        
class Trie:
    def __init__(self):
        self.root = Node()   

    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        
        for w in word:
            if w not in node.children: # if it doesnt exist, create that child 
                node.children[w] = Node()

            if i == len(word) - 1:
                node.children[w].is_word = True # mark last character as is word
                
            node = node.children[w] # move to grandchild
            i += 1

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        
        for w in word:
            if w not in node.children: # there is no such as character in the trie
                return False
            
            if i == len(word) - 1 and node.children[w].is_word: # is word found
                return True
            
            node = node.children[w]
            i += 1
        
        return False # word length is smaller than depth, word length is reached and it is not a word
                
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for p in prefix:
            if p not in node.children:
                return False
            
            node = node.children[p]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
