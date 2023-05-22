from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''My first attempt solution.'''
        if nums[0] < nums[-1]: return nums[0]

        l, r = 0, len(nums) - 1
        min = 5001
        while l <= r:
            m = (l + r) // 2
            min = nums[m] if nums[m] < min else min

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return min
    
    def findMin2(self, nums: List[int]) -> int:
        '''Solution found online that is the same idea as mine but a little cleaner with float("inf") 
        and min(curr_min, nums[mid])'''
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])
