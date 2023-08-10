'''Figured this one out pretty quickly.'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

'''More optimized solution without a whole 2D array.'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            dp2 = [1]*n
            for j in range(1, n):
                dp2[j] = dp[j] + dp2[j-1]
            dp = dp2
        
        return dp[-1]