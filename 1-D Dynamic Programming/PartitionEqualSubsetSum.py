'''Really need to review this one, couldn't figure out on own.'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # get sum
        target = sum(nums)
        if target % 2:
            return False

        sumList = set()
        sumList.add(0)

        for num in nums:
            tmp = set()
            for s in sumList:
                if s + num == target / 2:
                    return True
                elif s + num < target / 2:
                    tmp.add(s + num)
                tmp.add(s)
            sumList = tmp
        
        return False

        