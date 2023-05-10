from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''This was my first attempt and I finished in like 10 min! My fastest one so far and way better
        than the ThreeSum earlier today haha. But anyway, I use a two pointer algorithm and start with
        the endpoints. I noticed that the bar with smaller height will never be bigger since we are moving
        inward. So we just move to the next one.'''
        l = 0
        r = len(height) - 1

        max = 0
        while l < r:
            minheight = min(height[l], height[r])
            if minheight * (r-l) > max:
                max = minheight * (r-l)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return max