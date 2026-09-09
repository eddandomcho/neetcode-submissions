class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        DIRECTIONS = [(1,0), (-1,0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, ocean_set):
            if not (0 <= r < rows and 0 <= c < cols):
                return 
            curr = heights[r][c]
            if prev and curr < prev:
                return
            if (r, c) in ocean_set:
                return

            ocean_set.add((r, c))

            for r_op, c_op in DIRECTIONS:
                dfs(r + r_op, c+ c_op, curr, ocean_set)
        
        # pacific
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dfs(i, j, heights[i][j], pacific)

        # atlantic
        for i in range(rows):
            for j in range(cols):
                if i == rows - 1 or j == cols -1:
                    dfs(i, j, heights[i][j], atlantic)
        
        return list(pacific.intersection(atlantic))