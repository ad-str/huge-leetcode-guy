'''I passed with this solution but it's O(n^2). I thought that would be enough but apparently you can do O(n) by keeping
track of the state (of which there are 2 - buying or not) so 2n possibilities. It is 98% space efficient though lol.'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProf = [0] * (len(prices) + 2)

        for i in range(len(prices) - 1, -1, -1):

            for j in range(i + 1, len(prices)):
                maxProf[i] = max(maxProf[i], prices[j] - prices[i] + maxProf[j+2])
            
            maxProf[i] = max(maxProf[i], maxProf[i+1])
        
        return maxProf[0]

'''Edited version of my code that runs in O(n) time by keeping track of the maximum difference between price in prev and max prof 2 before
that.'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProf = [0] * len(prices)
        maxDiff = -float("inf")
        for i in range(1, len(prices)):
            if i > 2:
                maxDiff = max(maxDiff, maxProf[i-3] - prices[i-1])
            else:
                maxDiff = max(maxDiff, -prices[i-1])
            maxProf[i] = max(maxProf[i-1], maxDiff + prices[i])
        
        return maxProf[-1]

'''This solution from Neetcode is a doozy. Need to review.'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
