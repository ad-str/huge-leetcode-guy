'''My original solution. Works and is effecient. Idea is just to restart the running sum once it goes
negative.'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        running_sum = -1
        max_sum = -float("inf")
        for num in nums:
            if running_sum < 0:
                running_sum = num
            else:
                running_sum += num
            
            if running_sum > max_sum:
                max_sum = running_sum
        
        return max_sum