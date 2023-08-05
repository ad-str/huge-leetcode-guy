'''Came up with this after I tried a brute force recursive method. The key idea is that to reach stair n,
you either get to stair n-2 then hop 2 or get to stair n-1 and hop 1.'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]

'''The slow brute-force way.'''
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        def rec(size, steps):
            nonlocal res
            if size == 0:
                res += 1
                return
            elif size > 0:
                rec(size-2, steps+2)
                rec(size-1, steps+1)
        
        rec(n, 0)
        return res