class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find if a sequence starter exists
        nums_set = set(nums)
        if not nums:
            return 0
        max_len = float("-inf")
        for i in nums:
            if i - 1 in nums_set:
                # not a sequence starter
                continue
            increment = 1
            length = 1
            while True:
                if i + increment not in nums_set:
                    break
                increment += 1
                length += 1

            max_len = max(max_len, length)
        return max_len
