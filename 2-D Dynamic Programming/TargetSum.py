'''This was my idea but I was a little unsure about it since I was used to each index representing the target but there are 
negative numbers now. Took a little bit of help from other solution to implement right.'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ttl = sum(nums)

        if target > ttl or target < -ttl: return 0

        dp = [0] * (2*ttl + 1)
        dp[ttl] = 1

        for i in range(len(nums)):
            next = [0] * (2*ttl + 1)
            for k in range(len(next)):
                if dp[k] != 0:
                    next[k + nums[i]] += dp[k]
                    next[k - nums[i]] += dp[k]
            dp = next 
        
        return dp[ttl+target]
    

'''Alternative method using memoization and backtracking'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)