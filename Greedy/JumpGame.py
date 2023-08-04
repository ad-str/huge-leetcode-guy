'''My original solution. Works and is very efficient. Key idea is to
constantly move the "goal post" and ask if the current element can 
reach that goal post.'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= end - i:
                end = i
        return end == 0