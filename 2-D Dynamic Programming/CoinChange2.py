'''Came up with myself. Passes but can be made more efficient using a 1D array.'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0] * (len(coins)) for _ in range(amount + 1)]
        
        for j in range(len(coins)):
            dp[0][j] = 1
        
        for i in range(1, amount+1):
            if i - coins[0] >= 0:
                dp[i][0] = dp[i-coins[0]][0]

        for i in range(1, amount + 1):
            for j in range(1, len(coins)):
                if i - coins[j] >= 0:
                    dp[i][j] = dp[i][j-1] + dp[i-coins[j]][j]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[amount][-1]