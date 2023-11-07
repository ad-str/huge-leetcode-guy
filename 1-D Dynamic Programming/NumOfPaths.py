class Solution:
    def numOfPaths(self, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # number of paths from up or left
        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfPaths(5,5))