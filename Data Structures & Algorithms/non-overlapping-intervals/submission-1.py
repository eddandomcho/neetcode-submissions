class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        curr_end = float("-inf")
        result = []
        for interval in intervals:
            if interval[0] >= curr_end:
                result.append(interval)
                curr_end = interval[1]
        return len(intervals) - len(result)