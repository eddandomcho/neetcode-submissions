class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start_ind, path):
            res.append(path[:])
            for i in range(start_ind, len(nums)):
                num = nums[i]
                path.append(num)
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res