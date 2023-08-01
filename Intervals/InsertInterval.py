
'''My original solution I tried to find the exact indices that were conflicting and merge that way. 
Doesn't work when new interval doesn't conflict with anything.'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # determine what intervals conflict
        l = -1
        r = 0
        for i in range(len(intervals)):
            if (
                intervals[i][0] <= newInterval[0] <= intervals[i][1] or
                intervals[i][0] <= newInterval[1] <= intervals[i][1] or
                (newInterval[0] <= intervals[i][0] and intervals[i][1] <= newInterval[1]) or
                (intervals[i][0] <= newInterval[0] and newInterval[1] <= intervals[i][1])
            ):
                if l == -1:
                    l = i
                    r = l
                else:
                    r += 1
        
        # generate new interval
        merged = [min(intervals[l][0], newInterval[0]), max(intervals[r][1], newInterval[1])]

        intervals = intervals[:l] + [merged] + intervals[r+1:]

        return intervals
    
'''After looking at some hints, came up with this more efficient algorithm'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
        
        res.append(newInterval)
        return res

            