from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''My first attempt solution. Uses a bunch of or's'''
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target: return m

            if nums[m] < target <= nums[r] or target > nums[m] > nums[r] or nums[m] > nums[r] >= target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
    
    def search2(self, nums: List[int], target: int) -> int:
        '''Another solution. Conditionals might be slightly easier to understand but same thing'''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
