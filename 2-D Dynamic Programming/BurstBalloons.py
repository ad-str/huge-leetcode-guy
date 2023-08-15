'''I was on the right track thinking of starting with popping balloon i last but I couldn't quite get the correct recursive relation.
I didn't realize that popping balloon i last mean I could recurse on the subarrays to the left and right since they would never be 
connected. This is a solution I found that I understand.'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for gap in range(len(nums)):
            for left in range(len(nums)-gap):
                right = left + gap
                
                res = 0
                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    res = max(res, coins + dp[left][i] + dp[i][right])
                dp[left][right] = res
                
        return dp[0][len(nums)-1]