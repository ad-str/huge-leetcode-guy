'''I know zero bit manipulation so I had to look this up. It use the XOR operation in which two bits are compared, if they are different,
evaluates to 1, otherwise 0. The XOR operator is ^ in python. Works because if you XOR all elements, each duplicate will cancel out.
Another way to think about it is that at each bit, there will be an even amount of either 1 or 0, and an odd amount of the other. Obviously,
the one with an odd amount is the bit that should be used for the result.'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
