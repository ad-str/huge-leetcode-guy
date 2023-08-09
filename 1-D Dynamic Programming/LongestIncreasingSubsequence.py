'''My original implementation failed. I was close to the right recurrence relation but not quite right. My main idea was that at any
given point, we would either end the subsequence with the current number or we would not. And this is the correct thinking but my
actaul recurrence tried to take the max of dp[i-1] (so not ending in i) and dp[j] + 1 where nums[j] < nums[i]. But the problem is that
dp[j] is not guaranteed to end in nums[j] so it doesn't make sense to use it for the recurrence. So basically dp[i] in my version is
the maximum lenght subsequence so far when it should be the maximum subsequence ending in i.'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
        return dp[len(nums) - 1]

'''Correct solution where dp[i] is the longest subsequence ending in nums[i]. O(n^2)'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)