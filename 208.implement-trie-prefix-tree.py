#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    class Node:
        def __init__(self, val: chr):
            self.val = val
            self.next = [None for i in range(26)]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root = self._insert(word, currNode)

    def _insert(self, word: str, currNode: Node) -> Node:
        if len(word) == 0:
            return
        
        if currNode == None:
            currNode = self._insert(word[1:], )


            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

