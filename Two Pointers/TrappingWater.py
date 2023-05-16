from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        '''This was my first attempt and I passed! It took me around 45-50 minutes. Basically, I just
        look at the current possible water hieght and increment trapped water based on the height of the
        current block.'''
        
        l = 0
        r = len(height) - 1
        curr_water_height = 0
        trapped_water = 0
        iterate_left = False
        iterate_right = False

        while l < r:
            left = height[l]
            right = height[r]

            minHeight = min(left, right)

            if minHeight > curr_water_height:
                curr_water_height = minHeight
            
            if iterate_left and left < curr_water_height:
                trapped_water += curr_water_height - left
            
            if iterate_right and right < curr_water_height:
                trapped_water += curr_water_height - right
            
            if left < right:
                l += 1
                iterate_left = True
                iterate_right = False
            else:
                r -= 1
                iterate_left = False
                iterate_right = True

        return trapped_water
            

if __name__ == "__main__":
    solution = Solution()

    result = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
            