from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''Here's what I came up with. I encountered a few bugs. It also ended up failing the time limit.
        The biggest problem was nested for loop. I can apparently save time by doing work in the while
        loop instead.'''
        areas = []
        stack = []

        for bar in heights:
            new_length = 1
            while stack and bar <= stack[-1][0]:
                new_length += stack[-1][1]
                stack.pop(-1)
            stack.append((bar, new_length))

            # compute possible rectangles with current bar at the end
            max_area = 0
            length = 0
            for i in range(len(stack) - 1, -1 , -1):
                length += stack[i][1]
                area = stack[i][0] * length
                max_area = area if area > max_area else max_area
            areas.append(max_area)
        
        return max(max(heights), max(areas))
    
    def largestRectangleArea2(self, heights: List[int]) -> int:
        '''Solution I found online. Has some similar patterns, namely the nested while loop that keeps
        track of tuples (mine kept track of length explicitly, this just uses index). However, it does
        the max area work in the while loop and iterates through the stack outside of the for loop, at
        the end of everything.'''
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

    
    


if __name__ == "__main__":
    solution = Solution()

    print(solution.largestRectangleArea([3,6,5,7,4,8,1,0]))