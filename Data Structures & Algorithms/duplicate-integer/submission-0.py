class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contained = list()
        for number in nums:
            if number not in contained:
                contained.append(number)
                continue
            else: 
                return True
        return False