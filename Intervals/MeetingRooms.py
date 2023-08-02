
'''My original solution. Don't have Leetcode premium but I'm pretty positive this works.'''
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort()

        cur = -1
        for interval in intervals:
            if interval[0] < cur:
                return False
            else:
                cur = interval[1]
        
        return True
    
'''Neetcode solution is same idea.'''
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
