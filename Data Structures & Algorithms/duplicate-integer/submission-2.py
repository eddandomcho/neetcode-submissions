class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contained = set()
        for number in nums:
            if number not in contained:
                contained.add(number)
                continue
            else: 
                return True
        return False