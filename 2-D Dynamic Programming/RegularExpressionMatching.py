from typing import List

'''I had to use the help of neetcode. This one was really hard for me. I did get that s can only be matched with p if certain
substrings of s are matched with certain substrings of p. However, I first designed an algorithm that was greedy in which I tried
to use as many asterisk as possible. And it returns incorrectly when the pattern is something like "a*a". So I figured out after that
that I need to test all possible number of uses of an asterisk. When I reviewed the solution, the top-down solution didn't really
make sense to me completely and especially why it ran in O(mn) time. Now I think I understand that it is because we sometimes to 
repeated work (albeit not that common for most inputs) when there are patterns like "a*a*". So we only ever want to consider each 
pair of i and j ONCE. There are mn pairs hence O(mn) time. So we implement a cache each time we compute an i,j pair. And perform
a recursive call based on the state we are in (asterisk or not).'''
class Solution:
    def isMatch(self, s: str, p: str):
        cache = {}

        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True # if we match all of s and have used all of pattern
            if j >= len(p):
                return False # if we run out of pattern without matching all of s

            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # current chars are same
            if j + 1 < len(p) and p[j+1] == "*": # current state is asterisk
                cache[(i,j)] = dfs(i, j+2) # option1: don't use
                if match:
                    cache[(i,j)] = dfs(i+1, j) or cache[(i,j)] # option2: use
            else:
                if match:
                    cache[(i,j)] = dfs(i+1, j+1)
                else:
                    cache[(i,j)] = False

            return cache[(i,j)]

        return dfs(0,0)

'''The bottom up solution was tricky for me to get even after understanding the recursive top-down solution. I forgot the base case
of when we are matching the empty string s to asterisks since we can use 0 and that would technically be true. It was also hard for me
to get that we build up at the asterisk character when we are in the asterisk state instead of building up from the character that
comes right before the asterisk.'''
class Solution2:
    def isMatch(self, s: str, p: str):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # base case: could use 0 of asterisks
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j-1] == "*" and dp[0][j-2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # if there is a match between s_i and p_j. note: this will never be true when p_j == "*"
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                # otherwise ask if we are in asterisk state
                elif p[j-1] == "*":
                    # true if we can match up to p_{j-2} (case where we use 0) or if previous char matches s_i and we can match
                    # up through s_{i-1} using up through p_j
                    dp[i][j] = dp[i][j-2] or ((p[j-2] == s[i-1] or p[j-2]==".") and dp[i-1][j])
                    
        return dp[len(s)][len(p)]

if __name__ == "__main__":
    sol = Solution()

    print(sol.isMatch('aaaab', 'a*a*a*b'))