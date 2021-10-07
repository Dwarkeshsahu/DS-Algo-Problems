"""
https://www.lintcode.com/problem/920/description

sort by start time and check overlapping of current end time with next start time.

"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        end_time = -1
        for interval in intervals:
            if interval.start < end_time:
                return False
            end_time = interval.end 
        return True
