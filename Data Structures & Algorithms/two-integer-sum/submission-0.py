class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], idx]
            seen[value] = idx