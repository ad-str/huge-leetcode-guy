'''My attempt did not work but it was close to the solution. If I spent a bit more time on it I could 
have probably figured it out.'''
class WordDictionary:

    def __init__(self):
        self.chars = {}
        

    def addWord(self, word: str) -> None:
        cur = self.chars

        for char in word:
            if char not in cur:
                cur[char] = {}
            
            cur = cur[char]

        cur[None] = None
        

    def search(self, word: str) -> bool:
        def searchRecurse(map, word):
            cur = map
            for i in range(len(word)):
                char = word[i]
                if char==".":
                    for child in cur:
                        if searchRecurse(cur[child], word[i+1:]):
                            return True
                
                if char not in cur:
                    return False
                cur = cur[char]
            
            return True

        return searchRecurse(self.chars, word)
    


'''Neetcode solution. I had the same idea to conduct a recursive search for '.' characters.'''
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
