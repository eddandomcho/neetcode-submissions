class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = float("-inf")
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[right], heights[left])
            width = right-left
            area = height * width
            current_max = max(area, current_max)
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return current_max