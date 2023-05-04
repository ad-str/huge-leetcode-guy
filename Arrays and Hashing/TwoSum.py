from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''First attempt'''
        dic = {}
        for i in range(0, len(nums)):
            if nums[i] in dic.keys() and target - nums[i] == nums[i]:
                return [dic.get(nums[i]), i]
            else:
                dic[nums[i]] = i # key is the number and value is the index
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in dic.keys() and diff != nums[i]:
                return [i, dic.get(diff)]
        
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        '''Optimal solution, will need to review. I remember thinking of doing this but stopped because I 
        thought I needed to look at the rest of the list first, but that's not true because the difference 
        still works the same'''
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,4]
    target = 6

    result = solution.twoSum(nums, target)
    print(result)