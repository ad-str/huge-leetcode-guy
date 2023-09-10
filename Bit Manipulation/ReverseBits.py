class Solution:
    '''
    Build up solution by putting the rightmost bit at the new leftmost bit
    '''
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


class Solution:
    '''
    My modified solution is actually faster.
    '''
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans = (ans << 1) | bit
        return ans