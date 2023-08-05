'''My algorithm, came up with in 15 min and passed. The recursive idea: say the last house we rob is house i. Return the max of the
last two.'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        nums[2] += nums[0]
        
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        
        return max(nums[-1], nums[-2])
    
'''Neetcode solution slightly better. Slight alteraation of my recursive idea: we ALLOW robbing from houses 0 to i - so don't
require that we rob the last house. Return last one.'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
