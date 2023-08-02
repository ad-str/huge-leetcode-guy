'''I had a solution that ran very inefficiently using heaps to constantly ask how many intervals were
overlapping with the current interval which would take at least O(n^2)'''

'''After reviewing Neetcode's insight into how to think of the problem, this is how I implemented it.
O(n) way faster.'''
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval[0], 1))
            times.append((interval[1], -1))
        
        times.sort(key = lambda x: (x[0], x[1])) # need to also add x[1] in there because we allow meetings to end at the same time a new one starts in the same room

        cou = 0
        res = 0
        for time in times:
            cou += time[1]
            if cou > res:
                res = cou
        
        return res