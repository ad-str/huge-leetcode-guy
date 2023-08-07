'''My top down DP is TLE. I think this isn't quite DP. Even though it takes the minimum over remainders, it still needs to 
go all the way down the recursion tree for some, I guess so O(2^n) ?'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def minCoins(amt):
            if amt < 0:
                return float("inf")
            elif amt == 0:
                return 0
            else:
                num = float("inf")
                for coin in coins:
                    if minCoins(amt - coin) < num:
                        num = minCoins(amt - coin)
                return 1 + num
            
        return minCoins(amount)

'''With memoization slightly faster but still TLE.'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def minCoins(amt, cache):
            if amt < 0:
                return float("inf")
            elif amt == 0:
                return 0
            
            if amt in cache:
                return cache[amt]
            
            num = float("inf")
            for coin in coins:
                if minCoins(amt - coin, cache) < num:
                    num = minCoins(amt - coin, cache)
                    cache[amt-coin] = num
            return 1 + num
            
        res = minCoins(amount, {})
        return res if res != float("inf") else -1

'''Apparently bottom up with an array of size amount is best. I felt allergic to looping one at a time to the amount. Something about
it felt wrong but apparently it's right.'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
