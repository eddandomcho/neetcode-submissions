"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x.end, reverse = True)
        current_start, current_end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval.start, interval.end
            if end > current_start:
                return False
            current_start = start
            current_end = end
        return True


