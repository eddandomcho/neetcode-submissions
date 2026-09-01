class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):
            if total == target:
                res.append(current[:])
                return
            if i >= len(nums) or total > target:
                return
            current.append(nums[i])
            backtrack(i, current, total + nums[i]) # try same one
            current.pop()
            backtrack(i + 1, current, total) # try next number
        
        backtrack(0, [], 0)
        return res