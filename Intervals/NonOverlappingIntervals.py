
'''My original solution. Works and is efficient. Finished within 20 min.'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = -1
        prev = float("inf")
        for interval in intervals:
            if interval[0] < prev:
                prev = min(prev, interval[1])
                ans += 1
            else:
                prev = interval[1]
        
        return ans
