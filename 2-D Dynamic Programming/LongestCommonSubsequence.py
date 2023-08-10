'''I was really close to the right solution but was failing to take into account some cases.'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            for j in range(1, len(text2)+1):
                dp[j] = max(dp[j], dp[j-1])
                if text1[i] == text2[j-1]:
                    dp[j] += 1
        
        return dp[-1]
    
'''Neetcode 2D array solution.'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

'''My optimized Neetcode version.'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            diag = 0
            for j in range(1, len(text2)+1):
                tmp = dp[j]
                if text1[i] == text2[j-1]:
                    dp[j] = diag + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                diag = tmp
        
        return dp[-1]