'''Ok I gave in and finally decided to try recursion with memoization and it freaking worked. UUUUGH. It feels so wrong to do it
this way for some reason. It just feels a little difficult to understand the running time for algorithms like this. But anyway,
I got this in like 20min and it's really time and space efficient.'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(s) < len(t):
            return 0
        
        dp = {}

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i >= len(s):
                return 0
            if j >= len(t):
                return 1

            if len(s) - i == len(t) - j:
                if s[i:] == t[j:]:
                    dp[(i,j)] = 1
                else:
                    dp[(i,j)] = 0
                return dp[(i,j)]
            
            dp[(i,j)] = dfs(i+1, j)
            if s[i] == t[j]:
                dp[(i,j)] += dfs(i+1, j+1)
            
            return dp[(i,j)]
        
        return dfs(0,0)
            
