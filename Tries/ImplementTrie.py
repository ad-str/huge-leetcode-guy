'''My first attempt and it worked. It uses a bunch of nested maps.'''
class Trie:
    def __init__(self):
        self.chars = {}
        

    def insert(self, word: str) -> None:
        cur = self.chars
        for char in word:
            if char not in cur:
                cur[char] = {}
            
            cur = cur[char]
        
        cur[None] = None

            
        
    def search(self, word: str) -> bool:
        cur = self.chars

        for char in word:
            if char not in cur:
                return False
            
            cur = cur[char]
        
        if None not in cur:
            return False
        else:
            return True

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.chars

        for char in prefix:
            if char not in cur:
                return False
            
            cur = cur[char]
        
        return True
        

'''The solution from neetcode. It uses a helper class for a TrieNode similar for Trees. Pretty similar.'''
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
