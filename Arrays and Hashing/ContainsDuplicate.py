from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''This is O(n) time where n is the length of the list. This was my attempt.'''
        numSet: set = set(nums)
        if len(numSet) == len(nums):
            return False
        else:
            return True
        
    def containsDuplicate2(self, nums: List[int]) -> bool:
        '''Condensed version of my first attempt'''
        return len(set(nums)) != len(nums)
    
    def containsDuplicateFastest(self, nums: List[int]) -> bool:
        '''This was a solution I found that is still worst-case O(n) time but slightly faster on average'''
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,1]
    result = solution.containsDuplicate2(nums)
    print(result)