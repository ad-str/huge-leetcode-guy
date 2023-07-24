from collections import deque
from typing import List

class Solution:
    '''My implementation. It passed but is slow. O(n^2k)'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visit = set()
        visit.add(beginWord)

        q = deque()
        q.append(beginWord)
        res = 0
        while q:

            res +=1

            for _ in range(len(q)):
                cur = q.popleft()

                for word in wordList:
                    if word in visit:
                        continue
                    if self.closeWord(cur, word):
                        if word == endWord:
                            return res
                        visit.add(word)
                        q.append(word)

        return 0


    def closeWord(self, word1, word2):
        if len(word1) != len(word2):
            return False
        
        budget = 1
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if budget == 0:
                    return False
                budget-=1
        
        return True
    
'''Neetcode implementation takes O(nk^2) time instead of O(n^2k) time. Each key in the dict is a pattern
instead of a word.'''
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

    
if __name__ == "__main__":
    sol = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(sol.ladderLength(beginWord, endWord, wordList))


