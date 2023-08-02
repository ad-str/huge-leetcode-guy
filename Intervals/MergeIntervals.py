
'''First attempt. Got it right within like 15 min.'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            right = intervals[i]

            if cur[1] < right[0]:
                res.append(cur)
                cur = right
                continue
            else:
                cur[1] = max(cur[1], right[1])
        
        res.append(cur)
        return res

'''Slightly faster implementation I found but does the same thing.'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x [0])

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans