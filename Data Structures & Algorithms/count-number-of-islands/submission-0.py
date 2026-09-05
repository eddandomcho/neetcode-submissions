class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return
            # mark as visited in-place
            grid[r][c] = '0'
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands +=1
                    dfs(r, c)
                    # marks everything as visited
        return islands