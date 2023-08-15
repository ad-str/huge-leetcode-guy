'''Figured this one out quickly using DP. Easier to think about using a 2D array but I also optimized after - see below.'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2)+1):
            dp[0][j] = j
        
        for i in range(len(word1)+1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        
        print(dp)
        return dp[-1][-1]

'''Optimized code'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        prev = [j for j in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            new = [0] * (len(word2) + 1)
            new[0] = i

            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    new[j] = prev[j-1]
                else:
                    new[j] = 1 + min(prev[j-1], new[j-1], prev[j])
            
            prev = new
        
        return prev[-1]