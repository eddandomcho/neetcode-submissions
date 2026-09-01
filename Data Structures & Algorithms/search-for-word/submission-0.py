class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        state = [False]
        row_num = len(board)
        col_num = len(board[0])
        n = len(word)
        def dfs(coords, current):
            row, col = coords
            if row < 0 or row >= row_num or col < 0 or col >= col_num:
                return

            if board[row][col] == "#" or board[row][col] != word[len(current)]:
                return
            current = current + board[row][col]
            if current == word:
                state[0] = True
                return
            temp = board[row][col]
            board[row][col] = "#"
            if not state[0]: dfs((row + 1, col), current)
            if not state[0]: dfs((row - 1, col), current)
            if not state[0]: dfs((row, col + 1), current)
            if not state[0]: dfs((row, col - 1), current)
            board[row][col] = temp
        for r in range(row_num):
            for c in range(col_num):
                if board[r][c] == word[0]:  # Quick start check
                    dfs((r, c), "")
                    if state[0]:
                        return True
        return state[0]