class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if board[r][c] != 'O':
                return
            
            board[r][c] = '#'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # loop through the board, and dfs every border 'O'
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r,c)
        

        # loop through the board, and convert surrounded Os to X and #s to Os
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'

            




        