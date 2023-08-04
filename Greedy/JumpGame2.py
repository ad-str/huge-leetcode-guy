'''Couldn't figure this one out on my own. Had to watch neetcode explain 
the idea, then I came back later in the day and coded this up'''
class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = r = 0
        max_jump = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                max_jump = max(max_jump, i + nums[i])
            l = r + 1
            r = max_jump
            res += 1
        
        return res
