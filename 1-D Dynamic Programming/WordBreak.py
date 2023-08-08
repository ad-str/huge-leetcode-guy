'''My solution and it passes. It only considers previous substrings that are true and determines if the word after them is in the
dictionary.'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        trues = [0]
        for i in range(len(s)):

            for t in trues:
                if s[t:i+1] in wordSet:
                    trues.append(i+1)
                    break
        
        return trues[-1] == len(s)

'''Neetcode solution is a similar idea but different implementation.'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for w in wordDict:
                if (i - len(w)) >= 0 and s[i - len(w) : i] == w:
                    dp[i] = dp[i - len(w)]
                if dp[i]:
                    break

        return dp[len(s)]
