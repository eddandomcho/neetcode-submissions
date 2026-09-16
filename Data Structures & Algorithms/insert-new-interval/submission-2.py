class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        idx = 0
        while idx < len(intervals):
            interval = intervals[idx]
            if interval[1] >= newInterval[0]:
                break
            result.append(interval)
            idx +=1
        while idx < len(intervals):
            interval = intervals[idx]
            if interval[0] >newInterval[1]:
                break
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
            idx +=1
        result.append(newInterval)
        while idx < len(intervals):
            result.append(intervals[idx])
            idx +=1
        return result
        