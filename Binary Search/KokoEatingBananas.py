# 2024-08-05
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            m = (l + r) // 2

            if self.canFinish(m, piles, h):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
    
    # helper function to determine if can finish eating all piles within h hours given k eating speed
    def canFinish(self, k: int, piles: List[int], h: int) -> int:
        h_req = 0
        for n in piles:
            h_req += math.ceil(n / k)
        return h_req <= h
