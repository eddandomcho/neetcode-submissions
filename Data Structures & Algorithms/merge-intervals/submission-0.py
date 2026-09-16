class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        result = []
        prev = intervals[0]
        for interval in intervals:
            if interval[0] > prev[1]:
                result.append(prev)
                prev = interval
                continue
            prev[0] = min(prev[0], interval[0])
            prev[1] = max(prev[1], interval[1])
        result.append(prev)
        return result
            
