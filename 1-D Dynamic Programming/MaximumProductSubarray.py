'''Couldn't figure out by myself. I knew that positive numbers would mean increased product. However I should've thought about it more
and realized that no matter what, if the next number is an integer, then the running product will either become a new minimum or a
new maximum. The other trick is to initialize curMin and curMax both at 1 so it will "skip" over the first negative. Also need to reset
the running product once a zero is encountered.'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
