'''Couldn't figure out on my own. Need to review.'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def hr1(nums):
            prev2, prev1 = 0, 0

            for num in nums:
                temp = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = temp
            
            return prev1
        
        return max(hr1(nums[0:-1]), hr1(nums[1:]))