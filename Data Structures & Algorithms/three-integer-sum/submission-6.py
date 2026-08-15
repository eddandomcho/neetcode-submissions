class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = list()
        for idx, value in enumerate(nums):
            if idx > 0 and value == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums)-1
            while left < right:
                sum = value + nums[left] + nums[right]
                if sum == 0:
                    triplets.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -=1
                else:
                    left +=1
        return triplets