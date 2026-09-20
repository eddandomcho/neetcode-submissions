class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # target is 8
        first_column = [row[0] for row in matrix]
        def find_row(first_column: List[int], target: int) -> int:
            low, high = 0, len(first_column) - 1
            if target < first_column[low]:
                return -1
            while low <= high:
                mid = (low + high) //2
                if first_column[mid] <= target:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        row = matrix[find_row(first_column, target)]
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) //2
            if row[mid] == target:
                return True
            if row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
