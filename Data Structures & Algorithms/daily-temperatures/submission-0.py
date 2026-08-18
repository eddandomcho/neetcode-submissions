class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        res = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                prev_idx, prev_val = stack.pop()
                res[prev_idx] = idx - prev_idx
            
            stack.append([idx, val])
        return res
                