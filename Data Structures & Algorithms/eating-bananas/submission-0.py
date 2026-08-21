class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        min_speed = low + (high - low) // 2
        while low <= high:
            mid = low + (high-low) // 2
            total_time = 0
            for pile in piles:
                if pile < mid:
                    total_time +=1
                elif pile >= mid:
                    total_time += -(-pile // mid)
            if total_time > h:
                low = mid + 1
            else:
                high = mid - 1
                min_speed = mid
        return min_speed
